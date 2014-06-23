# Created by pyp2rpm-1.1.0b
%global pypi_name treq

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        A requests-like API built on top of twisted.web's Agent

License:        MIT
URL:            http://github.com/dreid/treq
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-sphinx
# For tests
BuildRequires:  python-twisted >= 12.1.0
BuildRequires:  python-mock
 
Requires:       python-twisted >= 12.1.0

%description
treq is an HTTP library inspired by requests but written on top of Twisted's Agents

It provides a simple, higher level API for making HTTP requests when using Twisted.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%{__python2} setup.py build

# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%check
trial treq

%files
%doc html README.rst LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jun 20 2014 tomprince - 0.2.1-1
- Initial package.
