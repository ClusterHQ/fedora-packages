%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif
%if ( 0%{?fedora} > 19 )
%global with_python3 1
%endif

Name:           python-netifaces
Version:        0.10.4
Release:        1%{?dist}
Summary:        Python library to retrieve information about network interfaces

Group:          Development/Libraries
License:        MIT
URL:            http://alastairs-place.net/netifaces/
Source0:        https://pypi.python.org/packages/source/n/netifaces/netifaces-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif # with_python3

Requires:       python

%if 0%{?with_python3}
%package -n python3-netifaces
Summary:        Python library to retrieve information about network interfaces
Requires:       python3
%endif # with_python3

%description
This package provides a cross platform API for getting address information
from network interfaces.

%if 0%{?with_python3}
%description -n python3-netifaces
This package provides a cross platform API for getting address information
from network interfaces.
%endif # with_python3


%prep
%setup -q -n netifaces-%{version}
rm -rf netifaces-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif # with_python3

%install
rm -rf $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc README.rst
%{python_sitearch}/netifaces-%{version}-py?.?.egg-info/
%{python_sitearch}/netifaces.so

%if 0%{?with_python3}
%files -n python3-netifaces
%doc README.rst
%{python3_sitearch}/netifaces.*.so
%{python3_sitearch}/netifaces-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 1 2011 Ryan Rix <ry@n.rix.si> 0.5-1
- Initial packaging effort
