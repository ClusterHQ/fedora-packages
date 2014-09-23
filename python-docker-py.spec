# disable debug package cause archful
%global         debug_package   %{nil}

Name:           python-docker-py
Version:        0.5.0
Release:        1%{?dist}
Summary:        An API client for docker written in Python
License:        ASL 2.0
URL:            http://www.docker.com
# Arch follows docker-io
# only x86_64 for now: https://github.com/dotcloud/docker/issues/136
ExclusiveArch:  x86_64
Source0:        https://pypi.python.org/packages/source/d/docker-py/docker-py-%{version}.tar.gz
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-tools
BuildRequires:  python-requests
BuildRequires:  python-websocket-client

# Resolves: rhbz#1132604 (epel7 only)

%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
BuildRequires:  docker
Requires:       docker
%else
BuildRequires:  docker-io
Requires:       docker-io
%endif

Requires:       python-requests
Requires:       python-websocket-client
Requires:       python-six

%description
%{summary}

%prep
%setup -q -n docker-py-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root %{buildroot}

%files
%doc LICENSE README.md
%dir %{python_sitelib}/docker
%dir %{python_sitelib}/docker_py-%{version}-py2*.egg-info
%{python_sitelib}/docker/*
%{python_sitelib}/docker_py-%{version}-py2*.egg-info/*

%changelog
* Mon Sep 22 2014 Tom Prince <tom.prince@clusterhq.com> - 0.5.0-1
- Resolves: rhbz#1145511 - version bump to 0.5.0

* Tue Aug 26 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.4.0-3
- correct bogus date

* Tue Aug 26 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.4.0-2
- rewrite BR&R conditionals for docker/docker-io

* Thu Aug 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.4.0-1
- update to 0.4.0
- Resolves: rhbz#1132604 (epel7 only)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.3.2-1
- version bump to 0.3.2
- Resolves: rhbz#1097415

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-8
- Bug 1063369 - Fix APIError for python-requests-1.1 on rhel6

* Sat Feb 08 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-7
- Bug 1048667 - disable debug package cause archful

* Fri Feb 07 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-6
- doesn't need python-mock at runtime

* Thu Jan 09 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-5
- python3 to be added after python3-websocket-client (BZ 1049424)

* Tue Jan 07 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-4
- double '%' to comment macros
- check section not considered for now
- python3- description in python3- subpackage conditional

* Tue Jan 07 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-3
- Everything goes in main package
- python3 package requires corrected
- package name python-docker-py
- both packages require docker-io

* Mon Jan 06 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-2
- python3 subpackage
- upstream uses PyPI
- package owns directories it creates
- build and runtime deps updated

* Sun Jan 05 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-1
- Initial fedora package
