---
title: Swap Space and Kernel Swappiness
description: On Linux, the kernel's <em>swappiness</em> level indicates how
  likely the system is to swap pages out of physical memory based on RAM usage.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/install-swap-space.adoc
  xref: xref:server:install:install-swap-space.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/install/install-swap-space.html)

# Swap Space and Kernel Swappiness

> On Linux, the kernel's _swappiness_ level indicates how likely the system is to swap pages out of physical memory based on RAM usage. Swappiness should be set to 1 or 0 on most Linux systems to achieve optimal Couchbase Server performance. 

Couchbase Server efficiently uses available RAM for your working set data; ideally, sufficient RAM remains available to the operating system above and beyond your cluster's configured server RAM quota. It's always a good idea to configure a reasonable amount of virtual memory or swap space on Linux-based nodes. (There are no recommended virtual memory optimizations for Windows-based nodes.) Sufficient virtual memory helps prevent Couchbase Server processes from being killed by the OS, such as by the Linux out of memory (OOM) killer.

The Linux kernel's _swappiness_ setting defines how aggressively the kernel will swap memory pages versus dropping pages from the page cache. A higher value increases swap aggressiveness, while a lower value tells the kernel to swap as little as possible to disk and favor RAM. The swappiness range is from 0 to 100, and most Linux distributions have swappiness set to 60 by default.

Couchbase Server is optimized with its managed cache to use RAM, and is capable of managing what should be in RAM and what shouldn't be. Allowing the OS to have too much control over what memory pages are in RAM is likely to lower Couchbase Server's performance. Therefore, it's recommended that swappiness be set to the levels listed below.

__Table 1\. Recommended Swappiness Settings for Linux__
| Linux Kernel Version | Recommended Swappiness |
| -------------------- | ---------------------- |
| 3.5-rc1 and higher   | 1\*                    |
| Older versions       | 0                      |

\*Linux kernel 3.5-rc1 and higher introduced a change in behavior for `swappiness=0`. Depending on how a Linux OS implements this change, it has the potential to increase the risk of OOM killing under strong memory and I/O pressure. As a result, the recommended swappiness setting for these Linux platforms is 1\. (Though, it may be the case that a given Linux OS has implemented or patched this change in such a way that a swappiness setting of 0 is still preferred.)

## [](#changing-swappiness-setting)Changing Swappiness Setting

The Linux kernel's swappiness setting tells the virtual memory subsystem how much it should attempt to swap to disk. Linux operating systems often default to a setting of 60, which can cause the OS to swap out items from memory even when there is plenty of RAM available. This behavior is undesirable given Couchbase Server's memory-first architecture.

### [](#red-hat-enterprise-linux-8-users)Red Hat Enterprise Linux 8 users

Follow the instructions in this section if you are running RHEL8\. This will ensure that the swappiness value is changed system-wide.

For other Linux systems, use the instructions in the [Other Linux (non-RHEL8) Users](#non-RHEL8-section) section.

1. Create a backup of your `/etc/sysctl.conf` file.  
```console  
sudo cp -p /etc/sysctl.conf /etc/sysctl.conf.`date +%Y%m%d-%H:%M`  
```
2. Add the new value for `vm.force_cgroup_v2_swappiness`.  
```console  
sudo sh -c 'echo "vm.force_cgroup_v2_swappiness = 1" >> /etc/sysctl.conf'  
```
3. Restart the system.

> [!NOTE]
> For more information, see <https://access.redhat.com/solutions/6785021>

### [](#non-RHEL8-section)Other Linux (non-RHEL8) Users

1. Verify your current system's swappiness setting.  
```console  
cat /proc/sys/vm/swappiness  
```  
If the output doesn't match the [recommended settings](#recommended-swappiness-settings), proceed to the next step.
2. Change the swappiness setting.

  1. Set the value for the running system.  
  ```console  
  sudo sh -c 'echo 1 > /proc/sys/vm/swappiness'  
  ```
  2. Backup `sysctl.conf`.  
  ```console  
  sudo cp -p /etc/sysctl.conf /etc/sysctl.conf.`date +%Y%m%d-%H:%M`  
  ```
  3. Set the value in `/etc/sysctl.conf` so it stays after reboot.  
  ```console  
  sudo sh -c 'echo "" >> /etc/sysctl.conf'  
  ```  
  ```console  
  sudo sh -c 'echo "#Set swappiness to 1 to minimize swapping" >> /etc/sysctl.conf'  
  ```  
  ```console  
  sudo sh -c 'echo "vm.swappiness = 1" >> /etc/sysctl.conf'  
  ```

Setting swappiness needs to be a part of the build process for any new Couchbase node. Make sure to modify any continuous deployment process that builds the OS. This also applies to golden master OS images and configuration automation systems. It is especially critical for public/private clouds where it is easy to bring up new instances.