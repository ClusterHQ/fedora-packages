# Build with `rpmbuild -D "_sourcedir $PWD" -ba clusterhq-release.spec`
Name:           clusterhq-release
Version:        1
Release:        1%{?dist}
Summary:        ClusterHQ Repository Configuration

License:        ASL 2.0
URL:            http://clusterhq.com/
Source0:        clusterhq.repo

Requires:       zfs-release
BuildArch:      noarch

%description
ClusterHQ repository for fedora

%install
cd %{_sourcedir}
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 clusterhq.repo $RPM_BUILD_ROOT/etc/yum.repos.d

%files
%config(noreplace) /etc/yum.repos.d/clusterhq.repo


%changelog
* Tue Jul 15 2014 tom.prince@ualberta.net - 1-1.fc20
- Initial Package 
