Name: parazip
Version: 0.4
Release: 1%{?dist}
Summary: Multi-threaded (parallel) tar.bz2 archiving of a directory with lowest priority CPU and I/O scheduling.

License: MPL2.0
URL: https://github.com/chotaire/parazip
Source0: https://github.com/chotaire/parazip/archive/v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Vendor: Chotaire
Packager: Chotaire

Requires: util-linux
Requires: coreutils
Requires: pbzip2
Requires: bash

%description

Multi-threaded (parallel) tar.bz2 archiving of a directory with lowest
priority CPU and I/O scheduling. Utilizes all cpu cores and detaches into
background, will syslog when it's done.

%prep
%autosetup

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Apr 12 2019 chotaire <chotaire@chotaire.net>
- Redesigned command syntax, still subject to change.
- Now able to define optional destination directory.
- Removed debug code, added toggable verbose output
- Now evaluating parameter strictness and count.
- New arguments: -V,--verbose,--no-verbose
- New arguments: -F,--foreground,--no-foreground
- New arguments: -S,--syslog,--no-syslog
- New arguments: -M,--message,--no-message
- New arguments: -I,--install
- New argument:  -h,--help
- New argument:  -v,--version
- Logging to syslog is now toggled off by default.
- 'foreground' and 'message' is not yet implemented.

* Tue Apr  9 2019 chotaire <chotaire@chotaire.net>
- Fixed missing output (and made more verbose), syslogging improved.
- Now accepting multiple args, added some debug code (use debug=1).
- Parazip will now save archive into current working directory.
- This way it is now possible to pack directories from outside CWD.

* Mon Apr  8 2019 chotaire <chotaire@chotaire.net>
- Now displays version when viewing --help.
- This release is also used for testing dnf updates and autobuild.

* Mon Apr  8 2019 chotaire <chotaire@chotaire.net>
- Initial RPM release.
