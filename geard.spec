%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%bcond_without  systemd
%endif

# modifying the dockerinit binary breaks the SHA1 sum check by docker
%global __os_install_post %{_rpmconfigdir}/brp-compress

#debuginfo not supported with Go
%global debug_package %{nil}
%global gopath  %{_datadir}/gocode

%global commit      4f8177dc2c53a02a817141e4ecb32c016c6f1808
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           geard
Version:        0
Release:        0.12.1.1.git%{shortcommit}%{?dist}
Summary:        Geard
License:        ASL 2.0
URL:            http://github.com/openshift/geard
ExclusiveArch:  x86_64
Source0:        https://github.com/openshift/geard/archive/%{commit}/geard-%{shortcommit}.tar.gz

%if 0%{?fedora} >= 21
Patch0:         selinux-impl.patch
%endif

#BuildRequires:  glibc-static
# ensure build uses golang 1.2-7 and above
BuildRequires:  gcc
BuildRequires:  golang >= 1.2-7
BuildRequires:  golang(github.com/fsouza/go-dockerclient)
BuildRequires:  golang(github.com/godbus/dbus)
BuildRequires:  golang(github.com/kraman/libcontainer)
BuildRequires:  golang(github.com/openshift/go-json-rest)
BuildRequires:  golang(github.com/openshift/go-systemd/dbus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/syndtr/gocapability/capability)
BuildRequires:  libselinux-devel

# btrfs not available for rhel yet
BuildRequires:  pkgconfig(systemd)
Requires:       systemd-units
# make sure package is docker-io
# https://bugzilla.redhat.com/show_bug.cgi?id=1097638
Requires:       docker-io

%description
%{summary}

%prep
%setup -q -n geard-%{commit}

%if 0%{?fedora} >= 21
%patch0 -p1 -b selinux-impl
%endif

%build
mkdir _build

pushd _build
  mkdir -p src/github.com/openshift
  ln -s $(dirs +1 -l) src/github.com/openshift/geard
popd

export GOPATH=$(pwd)/_build
contrib/build -s -l -n

%install
# install binary
install -d %{buildroot}%{_bindir}
install -p -m 4755 _build/bin/switchns %{buildroot}%{_bindir}
install -p -m 755 _build/bin/gear %{buildroot}%{_bindir}
install -d %{buildroot}%{_sbindir}
install -p -m 755 _build/bin/gear-auth-keys-command %{buildroot}%{_sbindir}
# install unitfile
install -d %{buildroot}%{_unitdir}
install -p -m 644 contrib/geard.service %{buildroot}%{_unitdir}

install -d -p %{buildroot}%{_sharedstatedir}/containers

%pre

%post
%systemd_post geard.service

%preun
%systemd_preun geard.service

%postun
%systemd_postun_with_restart geard.service

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/gear
%{_bindir}/switchns
%{_sbindir}/gear-auth-keys-command
%{_unitdir}/geard.service
%dir %{_sharedstatedir}/containers

%changelog
* Wed Jun 11 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.12.1.git8b2dcfc
- Remove sti binary as per upstream feedback
- Conditionally patch for selinux F20 vs F21+

* Wed Jun 11 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.12.git8b2dcfc
- New builds from upstream master at commit id 8b2dcfc
- Add sti binary

* Mon Jun 09 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.11.git8b2dcfc
- New builds from upstream master at commit id 8b2dcfc

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.git3c781d0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.9.git
- update to latest master 3c781d0cd8a961a85449d362fb5d8c88c5a34a22
- fix selinux build issue with
  https://github.com/pmorie/geard/commit/cd1475c12ab622115e27fefc2fd9481e24ae99c0
- Require docker-io to fix BZ 1097638

* Sat May 17 2014 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.8.git
- update to latest master
- make sure required package is docker-io

* Wed May 07 2014 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.7.git
- make tests more resilient

* Fri May 02 2014 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.6.git
- release 6

* Tue Apr 29 2014 Colin Walters <walters@redhat.com> - 0-0.5.1.git
- Change requires to be /usr/bin/docker to adapt to package rename

* Fri Apr 11 2014 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.5.git
- release 5

* Thu Apr 10 2014 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.4.git
- docs update, only run daemon in unitfile

* Wed Apr 09 2014 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.3.git
- make geard aware of binaries' locations

* Tue Apr 08 2014 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.2.git
- systemd pre post operations

* Mon Apr 07 2014 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.1.git
- initial package
