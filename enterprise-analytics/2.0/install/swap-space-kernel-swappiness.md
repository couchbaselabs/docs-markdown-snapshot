---
title: Swap Space and Kernel Swappiness
description: pass:On Linux, the kernel's swappiness level indicates how likely
  the system is to swap pages out of physical memory based on RAM usage.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/install/pages/swap-space-kernel-swappiness.adoc
  xref: xref:2.0@enterprise-analytics:install:swap-space-kernel-swappiness.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/install/swap-space-kernel-swappiness.html)

# Swap Space and Kernel Swappiness

> pass:On Linux, the kernel's swappiness level indicates how likely the system is to swap pages out of physical memory based on RAM usage. You should set Swappiness to 1 or 0 on most Linux systems to achieve optimal Enterprise Analytics performance. 

Enterprise Analytics efficiently uses available RAM for your working set data. Ideally, sufficient RAM remains available to the operating system beyond your cluster's configured RAM quota. It's always a good idea to configure a reasonable amount of virtual memory or swap space on Linux-based nodes. There are no recommended virtual memory optimizations for Windows-based nodes. Sufficient virtual memory helps prevent Enterprise Analytics processes from being killed by the OS, such as by the Linux out of memory (OOM) killer.

The Linux kernel's swappiness setting defines how aggressively the kernel swaps memory pages versus dropping pages from the page cache. A greater value increases swap aggressiveness, while a lesser value tells the kernel to swap as little as possible to disk and favor RAM. The swappiness range is from 0 to 100, and most Linux distributions have swappiness set to 60 by default.

Enterprise Analytics is optimized with its managed cache to use RAM, and is capable of managing what should be in RAM and what should not. Allowing the OS to have too much control over what memory pages are in RAM can reduce its performance. Couchbase recommends the following swappiness settings:

Recommended Swappiness Settings for Linux

Linux OS has the potential to increase the risk of OOM killing under strong memory and I/O pressure, based on how it implements this change. As a result, the recommended swappiness setting for these Linux platforms is 1.

A swappiness setting of 0 is preferred depending on how Linux OS has implements or patches this change.

## [](#changing-swappiness-setting)Changing Swappiness Setting

The Linux kernel's swappiness setting tells the virtual memory subsystem how much it should attempt to swap to disk. Linux operating systems often default to a setting of 60, which can cause the OS to swap out items from memory even when there is plenty of RAM available. This behavior is undesirable given that Enterprise Analytics has a memory-first architecture.

### [](#red-hat-enterprise-linux-8-users)Red Hat Enterprise Linux 8 users

Follow the instructions in this section if you're running RHEL8\. This ensures that the swappiness value is changed system-wide.

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
If the output does not match the [recommended settings](#recommended-swappiness-settings), proceed to the next step.
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

Setting swappiness needs to be a part of the build process for any new Couchbase node. Make sure to modify any continuous deployment process that builds the OS. This also applies to golden master OS images and configuration automation systems. It's critical for public/private clouds where it's easy to bring in new instances.