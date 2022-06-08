import argparse
import logging
import subprocess
import sys
from pathlib import Path
from re import findall, match
from typing import Dict

from termcolor import cprint

vers = {}


class vnu:

    installed_versions: dict = {}

    def __init__(self, args):
        logging.basicConfig(level=args.loglevel, format="\033[2m%(message)s\033[0m")
        self.installed_versions = self.get_installed_versions()
        if args.list:
            self.print_installed_versions()
            exit()
        if args.version != None:
            version = self.match_version(args.version)
            if self.uninstall(version):
                cprint("✌️ Success!", "green", attrs=["bold"])

    def get_installed_versions(self) -> Dict:
        """Try and get a list of installed node versions from the Volta command

        Returns:
            dict: indexed dictionary containing versions
        """
        try:
            process = subprocess.Popen(
                ["volta", "list", "node", "--format", "plain"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
        except:
            cprint("Volta not found!", color="white", on_color="on_red")
            exit()
        logging.info(" ".join(process.args))
        versions = process.stdout.read().decode()
        logging.info(versions)
        versions = findall(r"node@([0-9.]+)", versions)
        for index, version in enumerate(versions):
            vers[index] = version
        return vers

    def print_installed_versions(self) -> None:
        """Print the available Node versions from Volta"""
        cprint("Currently installed versions:", "yellow")
        print("\n".join(self.installed_versions.values()))

    def match_version(self, version: str):
        """Filter list of available versions using regex "^{version}.+?"

        Args:
            version (str): version string to match against

        Returns:
            str: the chosen version string
        """
        filtered = {}
        if version in self.installed_versions.values():
            return version
        _i = 1
        for i, v in self.installed_versions.items():
            if match(rf"^{version}.+?", v):
                filtered[_i] = v
                _i += 1
        if len(filtered) > 0:
            cprint(
                f"We found the following versions for {version}. Which one would you like to uninstall?"
            )
            for i, v in filtered.items():
                print(f"{i}.", v)
            print("0. Cancel")
            choice = int(input("\nYour choice: "))
            if choice == 0:
                exit()
            elif choice in filtered:
                return filtered[choice]
            else:
                print("Invalid Choice")
        else:
            cprint(f"❌ Version {version} is not installed!", "red", attrs=["bold"])
            exit()

    def uninstall(self, version: str):
        """Uninstall the desired Node version by removing it from Volta's folder

        Args:
            version (str): the version to remove
        """
        print(f"Removing Node v{version}")
        remove_image = subprocess.run(
            ["rm", "-r", f"{Path.home()}/.volta/tools/image/node/{version}"],
            text=True,
            capture_output=True,
        )
        logging.info(f"{' '.join(remove_image.args)}")
        logging.info(remove_image.stdout)
        remove_archives = subprocess.run(
            [
                "find",
                f"{Path.home()}/.volta/tools/inventory/node",
                "-type",
                "f",
                "-name",
                f"'*v{version}*'",
                "-delete",
            ],
            text=True,
            capture_output=True,
        )
        logging.info(f"{' '.join(remove_archives.args)}")
        logging.info(remove_archives.stdout)
        return remove_image and remove_archives


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.WARNING,
        help="Enable verbose logging",
    )
    parser.add_argument("-V", "--version", type=str, help="Version to uninstall")
    parser.add_argument(
        "-l", "--list", help="List all installed versions", action="store_true"
    )

    args = parser.parse_args()
    cprint("VNU (Volta Node Uninstaller)", attrs=["bold"])
    if len(sys.argv) <= 1:
        parser.print_help()
        exit()

    vnu(args)


if __name__ == "__main__":
    main()
