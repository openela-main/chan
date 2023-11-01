Name: chan
Version: 0.0.4
Release: 6%{?dist}
Summary: Pure C implementation of Go channels
License: ASL 2.0
URL: https://github.com/tylertreat/%{name}
Source0: https://github.com/tylertreat/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc autoconf automake libtool
BuildRequires: make
#Requires:       

%description
Pure C implementation of Go channels. Unbuffered, buffered
and closing channels are available.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}


%build
./autogen.sh
%configure --disable-static
%make_build

%check
%make_build src/chan_test
./src/chan_test

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_post

%ldconfig_postun


%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.0.0.0
%{_libdir}/lib%{name}.so.0

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/queue.h
%{_includedir}/%{name}/%{name}.h
%{_libdir}/lib%{name}.so


%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.0.4-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 0.0.4-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Lukáš Zapletal 0.0.4-1
- Initial package version
