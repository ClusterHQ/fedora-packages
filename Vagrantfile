# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$bootstrap = <<SCRIPT
yum localinstall -y http://archive.zfsonlinux.org/fedora/zfs-release$(rpm -E %dist).noarch.rpm
curl https://copr.fedoraproject.org/coprs/tomprince/hybridlogic/repo/fedora-20-x86_64/tomprince-hybridlogic-fedora-20-x86_64.repo >/etc/yum.repos.d/hybridlogic.repo
yum install @buildsys-build rpmdevtools rpmlint mock
SCRIPT


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "tomprince/fedora20-updated"
  config.vm.provision :shell, :inline => $bootstrap, :privileged => true

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
    config.cache.enable :generic, {
      "mock" => { :cache_dir => "/var/cache/some" },
    }
  end
end
