---
title: Non-Root Install and Upgrade
description: Couchbase Server can be installed on any supported Linux
  distribution by users who do not have <em>root</em> or <em>sudo</em>
  privileges.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/non-root.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:install:non-root.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/install/non-root.html)

# Non-Root Install and Upgrade

Couchbase Server can be installed on any supported Linux distribution by users who do not have _root_ or _sudo_ privileges. A non-root server, once installed, can be upgraded by the same users.

## [](#understanding-non-root-install)Understanding Non-Root Install

Whereas the standard _package-based_ installation of Couchbase Server requires _root_ or _sudo_ privileges on all supported Linux distributions, an alternative, _non-root_ installation can be also performed on all such distributions: this does _not_ require _root_ or _sudo_ privileges.

The procedures for non-root install, uninstall, stopping, and starting are:

* Identical across all supported Linux distributions.
* In each case, different from the equivalent procedure used for standard, package-based installation.

All _non-root_ procedures are described below.

## [](#prepare)Prepare

Before non-root install can be performed, the machine must be appropriately prepared. Note that preparations typically _will_ require root or sudo privileges.

### [](#disable-thp)Disable THP

_Transparent Huge Pages_ are enabled by default on most Linux systems; but are detrimental to the performance of Couchbase Server, and should therefore be _disabled_. To do this, follow the instructions provided in [Disabling Huge Transparent Pages (THP)](thp-disable.md).

### [](#configure-kernel-swappiness)Configure Kernel Swappiness

Optimal Couchbase-Server performance can be achieved by appropriately configuring kernel swappiness. To do this, follow the instructions provided in [Swap Space and Kernel Swappiness](install-swap-space.md).

### [](#establish-limits-for-user-processes-and-file-descriptors)Establish Limits for User Processes and File Descriptors

The maximum permitted number of _concurrent user processes_, and the maximum permitted number of _currently open file descriptors_, are both established on Linux systems with default values that are too low for running Couchbase Server with optimal performance and scale. The maximum number of user processes must therefore be reset to at least 10,000; and the maximum number of file descriptors to at least 200,000.

Note that Linux establishes such limits _per user_; and that since Couchbase Server will not, following non-root install, run as a _service_, but as a user process, the limits must be established separately for each user or group designated to run the non-root Couchbase Server.

Proceed as follows:

1. Check the current setting for user processes, as it applies to the current administrator:  
ulimit -u  
The response indicates the maximum number of user processes currently permitted for the administrator, which this example assumes to be the default value, applied to all users.  
3829  
In this case, the number, `3829`, is evidently lower than the Couchbase-Server requirement of `10000`.
2. Check the current setting for file descriptors as follows:  
ulimit -n  
The response indicates the maximum number of file descriptors currently permitted for the administrator, which this example assumes to be the default value, applied to all users.  
1024  
Again, in this case, the number, `1024`, is lower than the Couchbase-Server requirement of `200000`.
3. Raise the current limits on user processes and file descriptors, for the user or group designated to perform non-root install and then run Couchbase Server. To do this, access `/etc/security/limits.conf`, and add `hard` and `soft` lines for the `nproc` and `nofile` types, specifying appropriate values. The `domain` value, in the left-most column, should be the user-name of the user, or the group-name of the group, designated to install and run Couchbase Server.  
Following these additions, the lines should appear as follows:  
nameofuserorgroup       soft    nproc           10000  
nameofuserorgroup       hard    nproc           10000  
nameofuserorgroup       soft    nofile          200000  
nameofuserorgroup       hard    nofile          200000  
Save the file and exit.
4. Reboot the machine.
5. Following reboot, the designated user or group-member can check all the limits that currently apply to them, as follows:  
ulimit -a  
This displays a list of limits for the designated user or group, among which appear the modified values for user processes and file descriptors:  
core file size          (blocks, -c) 0  
data seg size           (kbytes, -d) unlimited  
scheduling priority             (-e) 0  
file size               (blocks, -f) unlimited  
pending signals                 (-i) 3829  
max locked memory       (kbytes, -l) 64  
max memory size         (kbytes, -m) unlimited  
open files                      (-n) 200000  
pipe size            (512 bytes, -p) 8  
POSIX message queues     (bytes, -q) 819200  
real-time priority              (-r) 0  
stack size              (kbytes, -s) 8192  
cpu time               (seconds, -t) unlimited  
max user processes              (-u) 10000  
virtual memory          (kbytes, -v) unlimited  
file locks                      (-x) unlimited

This concludes the procedure for establishing and verifying new limits for user processes and file descriptors.

## [](#perform-non-root-installation)Install

To perform a non-root installation of Couchbase Server on any supported Linux distribution, proceed as follows:

1. Download the Couchbase Server RPM from the [Couchbase Downloads](https://www.couchbase.com/downloads/) page.
2. Using `wget` or `curl`, download the appropriate binary for your platform (the URI is the same for all supported x86\_64 or aarch64 Linux distributions):  
<https://packages.couchbase.com/cb-non-package-installer/cb-non-package-installer-aarch64>  
<https://packages.couchbase.com/cb-non-package-installer/cb-non-package-installer-x86%5F64>  
> [!NOTE]  
> In the following examples, use the appropriate suffix (`"x86_64"` or `"aarch64"`) instead of `<platform-suffix>` for the `cb-non-package-installer`.
3. Make the binary executable.  
```console  
chmod u+x ./cb-non-package-installer-<platform-suffix>  
```
4. Choose — and if necessary, create — an empty directory into which installation will occur. For example:  
mkdir ./cb-install
5. Run the `cb-non-package-installer-<platform-suffix>` binary, to install Couchbase Server. For example:  
```console  
 ./cb-non-package-installer-<platform-suffix> --install --install-location ./cb-install \
 --package ./couchbase-server-enterprise-8.0.0-linux.<platform-suffix>.rpm  
```  
> [!NOTE]  
> the program performs dependency checking, prior to installation. If installation cannot proceed, due to missing dependencies, the program displays corresponding notifications, and stops running.
6. If dependencies have been flagged as missing, restore those dependencies by performing the necessary installations. Then, run the `cb-non-package-installer-<platform-suffix>` binary again.

When installation is complete, the following notification is displayed:

Successfully installed.

Couchbase Server can now be started: see immediately below.

## [](#start-stop-and-get-status)Start, Stop, and Get Status

To start, stop, or get status on a non-root Couchbase Server, use the `couchbase-server` command, provided in the `opt/couchbase/bin` directory that now resides under the specified install location. For example, the command's directory might be accessed as follows:

cd ./cb-install/opt/couchbase/bin

Note that a reference page for this command is provided at [couchbase-server](../cli/couchbase-server.md).

### [](#start-non-root-couchbase-server)Start

To start a non-root Couchbase Server, enter the following command:

./couchbase-server --start

This starts a non-root Couchbase Server. No output is displayed.

### [](#get-status-on-non-root-couchbase-server)Get Status

To get status on whether a non-root Couchbase Server is running, enter the following command.

./couchbase-server --status

If a non-root Couchbase Server is running, the following is displayed:

Couchbase Server is running

If a non-root-installed Couchbase Server is _not_ running, the following is displayed:

Couchbase Server is not running

### [](#stop-non-root-couchbase-server)Stop

To stop a non-root Couchbase Server, enter the following command:

./couchbase-server --stop

This stops a running, non-root Couchbase Server. The output might appear as follows:

2020-06-30 09:33:03 cb_dist: terminating with reason: shutdown

If no non-root Couchbase Server was running, no output is displayed.

## [](#uninstall-non-root-couchbase-server)Uninstall

To uninstall, stop the running non-root Couchbase Server, then remove the directory used as the install location, along with all its contents. For example:

./cb-install/opt/couchbase/bin/couchbase-server --stop
rm -rf ./cb-install

## [](#perform-non-root-upgrade)Upgrade

To upgrade an existing non-root Couchbase Server,

1. Ensure that the previous version of Couchbase Server is still installed, and has been _configured_ (since the upgrade process will make use of the post-configuration install location and directory contents).
2. Stop the server, if it is still running.
3. Use the `cb-non-package-installer` binary again, this time specifying the `--upgrade` flag, instead of the `--install` flag. Specify the new package to be used for upgrade; and specify the install location of the currently resident Couchbase Server. For example:  
```console  
./cb-non-package-installer-<platform-suffix> --upgrade --install-location ./cb-install \
--package ./couchbase-server-enterprise-8.0.0-linux.<platform-suffix>.rpm  
```

During upgrade, the following message may appear:

Running cbupgrade this could take some time

When upgrade has completed, the following notification is displayed:

Upgrade has completed successfully

Note that important, additional information on upgrade is provided in [Upgrading Couchbase Server](upgrade.md).