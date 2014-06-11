# Created by pyp2rpm-1.1.0b
%global pypi_name characteristic

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Say 'yes' to types but 'no' to typing!

License:        MIT
URL:            https://github.com/hynek/characteristic/
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  pytest


Requires:	python


%description
characteristic: Say ‘yes’ to types but ‘no’ to typing!

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
py.test --pyargs test_characteristic


%files
%doc README.rst LICENSE

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/test_characteristic.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Jun 10 2014 Tom Prince - 0.1.0-1
- Initial package.
