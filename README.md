# Parazip

## Introduction

Parallel (multi-threaded) tar.bz2 archiving of a directory with lowest priority CPU and I/O scheduling. Utilizes all cpu cores and detaches into background, will syslog when it's done. Will install missing dependancies on RHEL based operating systems.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3957b4329a2f43348d6c90049f6d427f)](https://www.codacy.com/app/chotaire/parazip?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=chotaire/parazip&amp;utm_campaign=Badge_Grade)

## Dependencies on CentOS/RHEL/Fedora
*   util-linux
*   coreutils
*   pbzip2

## Installation
*   Download from [Github](https://github.com/chotaire/parazip/releases) or [Chotaire Git](https://git.chotaire.net/chotaire/parazip/releases)
*   tar -jxvf parazip.tar.bz2
*   mv parazip.sh /usr/local/bin/parazip

## Usage

### Install Dependencies

`parazip install`

Will check for dependencies and install if not available.

### Run Parazip

`parazip <dir>`

Where \<dir\> is a directory name found in the current directory.
