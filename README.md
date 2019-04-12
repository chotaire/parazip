# Parazip

## Introduction

Multi-threaded (parallel) tar.bz2 archiving of a directory with lowest priority CPU and I/O scheduling. Utilizes all cpu cores and detaches into background, will syslog when it's done.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3957b4329a2f43348d6c90049f6d427f)](https://www.codacy.com/app/chotaire/parazip?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=chotaire/parazip&amp;utm_campaign=Badge_Grade)

[![asciicast](https://asciinema.org/a/240434.svg)](https://asciinema.org/a/240434)

## Dependencies on CentOS/RHEL/Fedora
*   util-linux
*   coreutils
*   pbzip2

## Installation

RPMs are [built from releases](https://copr.fedorainfracloud.org/coprs/chotaire/parazip/ "Parazip Repos on Fedora copr") for CentOS 6/7 (requires EPEL) and all currently supported Fedora versions.

### Fedora
```Shell
dnf copr enable chotaire/parazip
dnf install parazip
```

### CentOS / RHEL
```Shell
yum install yum-plugin-copr
yum copr enable chotaire/parazip
yum install parazip
```

### Other Linux
*   Download from [Github](https://github.com/chotaire/parazip/releases) or [Chotaire Git](https://git.chotaire.net/chotaire/parazip/releases)
*   Unpack source code

```Shell
chmod ugo+x parazip ; mv parazip /usr/local/bin
```

## Usage

```Shell
Usage: parazip [-V|--(no-)verbose] [-F|--(no-)foreground] [-S|--(no-)syslog]
[-M|--(no-)message] [-v|--version] [-I|--install] <source-dir> [<dest-dir>]

<source-dir>                      Source directory (single mandatory option)
<dest-dir>                        Destination directory (default: '.')

-V,--verbose,--no-verbose         Display more verbose output  (off by default)
-F,--foreground,--no-foreground   No detaching into background (off by default)
-S,--syslog,--no-syslog           Log start/end time to syslog (off by default)
-M,--message,--no-message         Send tty msg upon completion (off by default)
-I,--install:                     Check for and install software dependencies
-h,--help:                        Prints this help
-v,--version:                     Prints version

You need to pass at least one argument (the 'source-dir' to be archived).
```