%if 0%{?fedora}
%global with_python3 0
%endif

%global srcname eliot

Name:           python-%{srcname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Logging as Storytelling

License:        ASL 2.0
URL:            https://github.com/hybridcluster/eliot/
Source0:        https://pypi.python.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
# For tests and docs
BuildRequires:  python-six
BuildRequires:  python-zope-interface

Requires:       python-six
Requires:       python-zope-interface

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# For tests
BuildRequires:  python3-six
BuildRequires:  python3-zope-interface
%endif # with_python3
 

%if 0%{?with_python3}
%package -n python3-eliot
Summary:        Logging as Storytelling
Requires:       python3-six
Requires:       python3-zope-interface
%endif # with_python3

%description
Eliot provides a structured logging and tracing system for Python that
generates log messages describing a forest of nested actions.  Actions start
and eventually finish, successfully or not.  Log messages thus tell a story:
what happened and what caused it.

Features:

* Structured, typed log messages.
* Ability to log actions, not just point-in-time information: log messages
  become a trace of program execution.  Excellent support for unit testing your
  logging code.
* Emphasis on performance, including no blocking I/O in logging code path.
* Optional Twisted support.
* Designed for JSON output, usable by Logstash/Elasticsearch.
* Supports CPython 2.7, 3.3 and PyPy.

%if 0%{?with_python3}
%description -n python3-eliot
Eliot provides a structured logging and tracing system for Python that
generates log messages describing a forest of nested actions.  Actions start
and eventually finish, successfully or not.  Log messages thus tell a story:
what happened and what caused it.

Features:

* Structured, typed log messages.
* Ability to log actions, not just point-in-time information: log messages
  become a trace of program execution.  Excellent support for unit testing your
  logging code.
* Emphasis on performance, including no blocking I/O in logging code path.
* Optional Twisted support.
* Designed for JSON output, usable by Logstash/Elasticsearch.
* Supports CPython 2.7, 3.3 and PyPy.
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
sphinx-build docs/source html
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
%{__python2} -m unittest discover eliot.tests

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} -m unittest discover eliot.tests
popd
%endif # with_python3

%clean
rm -rf %{buildroot}

%files
%doc html README.rst LICENSE
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-eliot
%doc html README.rst LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Thu Jun 05 2014 Tom Prince - 0.4.0-1
- Initial package.
