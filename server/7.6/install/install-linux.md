---
title: Install Couchbase Server on Linux
description: Couchbase Server can be installed and run on several different
  versions of Linux.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/install-linux.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:install:install-linux.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/install/install-linux.html)

# Install Couchbase Server on Linux

> Couchbase Server can be installed and run on several different versions of Linux. 

## [](#supported-linux-platforms)Supported Linux Platforms

Couchbase Server can be installed and run on Red Hat, CentOS, Ubuntu, Debian, SUSE Enterprise, Oracle Enterprise, and Amazon Linux.

The following procedures use Couchbase packages, and require the user who performs the install to have _root_ or _sudo_ privileges:

* [Install on Red Hat Enterprise and CentOS](rhel-suse-install-intro.md).
* [Install on Ubuntu and Debian](ubuntu-debian-install.md).
* [Install on SUSE Enterprise](install%5Fsuse.md).
* [Install on Oracle Enterprise](install-oracle.md).
* [Install on Amazon Linux 2](amazon-linux2-install.md).

Additionally, a _non-package-based_ install can be performed on all the above platforms. Unlike the package-based install, this does _not_ require root or sudo privileges. After the non-package-based install, the same user can stop, start, and get status on the server; and can also perform upgrade.

The non-package-based procedure is the same for all the above platforms: see [Non-Root Install and Upgrade](non-root.md) for detailed information.