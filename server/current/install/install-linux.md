---
title: Install Couchbase Server on Linux
description: Couchbase Server can be installed and run on several different
  versions of Linux.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/install-linux.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:install:install-linux.adoc[]
---

[View original HTML](/server/current/install/install-linux.html)

# Install Couchbase Server on Linux

> Couchbase Server can be installed and run on several different versions of Linux. 

## [](#supported-linux-platforms)Supported Linux Platforms

Couchbase Server can be installed and run on Red Hat-based distributions, Oracle Enterprise, Amazon Linux, Ubuntu, Debian, and SUSE Enterprise.

The following procedures use Couchbase packages, and require the user who performs the install to have root or sudo privileges:

* [Install on Red Hat-based distributions, Oracle Linux, or Amazon Linux](rhel-suse-install-intro.md).
* [Install on Ubuntu and Debian](ubuntu-debian-install.md).
* [Install on SUSE Enterprise](install%5Fsuse.md).

Additionally, a non-package-based install is performed on all the above platforms. Unlike the package-based install, this does not require root or sudo privileges. After the non-package-based install, the same user can stop, start, and get status on the server; and can also perform upgrade.

The non-package-based procedure is the same for all the above platforms: see [Non-Root Install and Upgrade](non-root.md) for detailed information.