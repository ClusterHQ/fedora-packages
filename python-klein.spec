# Created by pyp2rpm-1.1.0b
%global pypi_name klein

Name:           python-%{pypi_name}
Version:        0.2.3
Release:        1%{?dist}
Summary:        werkzeug + twisted.web

License:        MIT
URL:            http://github.com/twisted/klein
Source0:        https://pypi.python.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
# For tests
BuildRequires:  python-twisted >= 12.1.0
BuildRequires:	python-werkzeug
BuildRequires:  python-mock

Requires:       python-twisted >= 12.1.0
Requires:	python-werkzeug

%description
Klein is a micro-framework for developing production ready web services with
python.  It is 'micro' in that it has an incredibly small API similar to bottle
and flask.  It is not 'micro' in that it depends on things outside the standard
library.  This is primarily because it is built on widely used and well tested
components like werkzeug and Twisted.

A Klein bottle is an example of a non-orientable surface, and a glass Klein
bottle looks like a twisted bottle or twisted flask. This, of course, made it
too good of a pun to pass up.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%check
trial klein

%files
%doc README.rst LICENSE AUTHORS NEWS.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Oct 09 2014 tomprince - 0.2.3-1
- Initial package.
