# VNU (Volta Node Uninstaller)
VNU is a simple utility to simplify the task of removing (or "uninstalling") Node from [Volta](https://volta.sh/).
Volta, as of June 2nd, 2022 is still missing this functionality.

## Why?
At work we we're thinking about implementing `volta` instead of `n` and one of the pushback reasons we got to not implement it was the inability to remove unused Node versions.

I took it upon myself to try and automate this seemingly trivial task. Enter VNU.

## Usage
`vnu -l` will list all available Node versions on Volta.

`vnu -V VERSION` will uninstall `VERSION` or show matching versions based on regex, e.g.:
```
❯ vnu -V 10
VNU (Volta Node Uninstaller)
We found the following versions for 10. Which one would you like to uninstall?
1. 10.8.0
2. 10.23.1
3. 10.24.1
0. Cancel
```

## Disclaimer
I'm not a programmer. I learn by doing and this is one of my small projects to help me do exactly that.
What this means is - this project and the code within it might be ugly and could probably be implemented in a million of better ways. This is exactly why I am sharing this with you, the smart people of the internet.

*I AM looking for feedback.* I do want to improve this little utility for everyone with your assistance.