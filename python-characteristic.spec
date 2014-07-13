%if 0%{?fedora}
%global with_python3 1
%endif

%global srcname characteristic

Name:           python-%{srcname}
Version:        0.1.0
Release:        2%{?dist}
Summary:        Say 'yes' to types but 'no' to typing!

License:        MIT
URL:            https://github.com/hynek/characteristic/
Source0:        https://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  pytest

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%endif # with_python3

Requires:       python


%description
characteristic is a Python package with class decorators that ease the chores
of implementing the most common attribute-related object protocols.

You just specify the attributes to work with and ``characteristic`` gives you:

- a nice human-readable ``__repr__``,
- a complete set of comparison methods,
- and a kwargs-based initializer (that cooperates with your existing one)

*without* writing dull boilerplate code again and again.

So put down that type-less data structures and welcome some class into your life!


%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        Say 'yes' to types but 'no' to typing!
Requires:	python3

%description -n python3-%{srcname}
characteristic is a Python package with class decorators that ease the chores
of implementing the most common attribute-related object protocols.

You just specify the attributes to work with and ``characteristic`` gives you:

- a nice human-readable ``__repr__``,
- a complete set of comparison methods,
- and a kwargs-based initializer (that cooperates with your existing one)

*without* writing dull boilerplate code again and again.

So put down that type-less data structures and welcome some class into your life!
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
%{__python3} setup.py build
popd
%endif # with_python3

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root %{buildroot}

%check
py.test --pyargs test_characteristic

%if 0%{?with_python3}
pushd %{py3dir}
py.test-%{python3_version} --pyargs test_characteristic
popd
%endif # with_python3


%files
%doc README.rst LICENSE

%{python2_sitelib}/%{srcname}.py*
%{python2_sitelib}/test_characteristic.py*
%{python2_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{srcname}
%doc README.rst LICENSE

%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/test_%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*.py[co]
%{python3_sitelib}/__pycache__/test_%{srcname}.*.py[co]
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Sat Jul 12 2014 Tom Prince - 0.1.0-2
- Add python3 support.

* Tue Jun 10 2014 Tom Prince - 0.1.0-1
- Initial package.
