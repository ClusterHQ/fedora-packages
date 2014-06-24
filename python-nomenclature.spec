%if 0%{?fedora}
%global with_python3 1
%endif

%global srcname nomenclature

Name:           python-%{srcname}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Linux Namespace Manipulation

License:        ASL 2.0
URL:            https://github.com/hybridcluster/nomenclature/
Source0:        https://pypi.python.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
# For tests and docs
BuildRequires:  python-cffi

Requires:       python
Requires:       python-cffi

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# For tests
BuildRequires:  python3-cffi
%endif # with_python3


%if 0%{?with_python3}
%package -n python3-nomenclature
Summary:        Linux Namespace Manipulation
Requires:       python3
Requires:	python3-cffi
%endif # with_python3

%description
Nomenclautre is a library providing access to linux's namespace manipulation functions.
The current version exposes the raw syscalls.

%if 0%{?with_python3}
%description -n python3-nomenclature
Nomenclautre is a library providing access to linux's namespace manipulation functions.
The current version exposes the raw syscalls.
%endif # with_python3

%prep
%setup -q -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3



%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif # with_python3

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
rm -rf %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root %{buildroot}

%check
%{__python2} -m unittest discover nomenclature.tests

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} -m unittest discover nomenclature.tests
popd
%endif # with_python3

%clean
rm -rf %{buildroot}

%files
%doc html README.rst LICENSE
%{python2_sitearch}/%{srcname}
%{python2_sitearch}/%{srcname}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-nomenclature
%doc html README.rst LICENSE
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Thu Jun 05 2014 Tom Prince - 0.1.0-1
- Initial package.
