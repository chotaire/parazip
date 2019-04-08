Name: parazip
Version: 0.1.1
Release: 1%{?dist}
Summary: Parallel (multi-threaded) tar.bz2 archiving of a directory with lowest priority CPU and I/O scheduling.

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

Parallel (multi-threaded) tar.bz2 archiving of a directory with lowest
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
* Mon Apr  8 2019 chotaire <chotaire@chotaire.net>
- Initial release