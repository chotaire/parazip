# Parazip

## Introduction

Parallel (multi-threaded) tar.bz2 archiving of a directory with lowest priority CPU and I/O scheduling. Utilizes all cpu cores and detaches into background, will syslog when it's done. Will install missing dependancies on RHEL based operating systems.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3957b4329a2f43348d6c90049f6d427f)](https://www.codacy.com/app/chotaire/parazip?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=chotaire/parazip&amp;utm_campaign=Badge_Grade)

## Dependencies on CentOS/RHEL/Fedora
*   util-linux
*   coreutils
*   pbzip2

## Installation

RPMs are [built from releases](https://copr.fedorainfracloud.org/coprs/chotaire/parazip/ "Parazip Repos on Fedora copr") for CentOS 7 (requires EPEL) and all currently supported Fedora versions.

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

### Install Dependencies

`parazip install`

Will check for dependencies and install if not available.

### Run Parazip

`parazip <dir>`

\<dir\>.tar.bz2 will be saved in your current working directory.