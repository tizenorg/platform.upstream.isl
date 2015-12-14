%define keepstatic 1
Name:           isl-static
Version:        0.12.2
Release:        0
License:        MIT
Summary:        Integer Set Library
Url:            http://www.kotnet.org/~skimo/isl/
Group:          Development/Toolchain
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  gmp-static

%description
ISL is a library for manipulating sets and relations of integer points
bounded by linear constraints.
It is used by Cloog and the GCC Graphite optimization framework.

%prep
%setup -q

%build
%autogen
%configure --disable-shared --enable-static
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
rm -f %{buildroot}%{_libdir}/libisl.so.*-gdb.py

%files
%defattr(-,root,root,-)
%{_includedir}/isl
%{_libdir}/libisl.a
%{_libdir}/pkgconfig/*.pc

