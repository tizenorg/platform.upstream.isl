Name:           isl
Version:        0.12
Release:        0
License:        MIT
Summary:        Integer Set Library
Url:            http://www.kotnet.org/~skimo/isl/
Group:          Development/Toolchain
Source:         isl-%{version}.tar.bz2
BuildRequires:  gmp-devel

%description
ISL is a library for manipulating sets and relations of integer points
bounded by linear constraints.
It is used by Cloog and the GCC Graphite optimization framework.

%package devel
Summary:        Development tools for ISL
Requires:       libisl = %{version}

%description devel
Development tools and headers for the ISL.

%package -n libisl
Summary:        The ISL shared library

%description -n libisl
The shared library for the ISL.

%prep
%setup -q

%build
%autogen
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
rm -f %{buildroot}%{_libdir}/libisl.so.*-gdb.py

%post -n libisl -p /sbin/ldconfig

%postun -n libisl -p /sbin/ldconfig

%files -n libisl
%defattr(-,root,root,-)
%license LICENSE
%{_libdir}/libisl.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/isl
%{_libdir}/libisl.so
%{_libdir}/pkgconfig/*.pc

%changelog
