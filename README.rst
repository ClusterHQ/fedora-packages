Packages for ClusterHQ's flocker that aren't available in fedora.


clusterhq-release package
~~~~~~~~~~~~~~~~~~~~~~~~~

This is a meta-package that contains the yum repository definitions for archive.clusterhq.com.

To build and upload the package, run the following commands on a fedora 20 machine
(if the version of the spec file is updated, the filename below will need to be updated)::

   rpmbuild --define="_sourcedir ${PWD}" --define="_rpmdir ${PWD}/results" -ba clusterhq-release.spec
   gsutil cp -a public-read results/noarch/clusterhq-release-1-?.fc20.noarch.rpm gs://archive.clusterhq.com/fedora/clusterhq-release.fc20.noarch.rpm
