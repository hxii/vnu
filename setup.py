from setuptools import setup

setup(
    name="VNU",
    version="0.1.0",
    description='A small utility to automate "uninstalling" Node from Volta',
    url="http://github.com/hxii/vnu",
    author="Paul (hxii) Glushak",
    author_email="paul@glushak.net",
    license="MIT",
    packages=["vnu"],
    scripts=["bin/vnu"],
    zip_safe=False,
    entry_points={"console_scripts": ["vnu = vnu.main:main"]},
)
