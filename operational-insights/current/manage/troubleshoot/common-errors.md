---
title: Common Errors
description: Common errors that occur during management of Operational Insights.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/troubleshoot/common-errors.adoc
  xref: xref:enterprise-analytics:manage:troubleshoot/common-errors.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/troubleshoot/common-errors.html)

# Common Errors

> Common errors that occur during management of Operational Insights. 

Process and file descriptor limits

When Operational Insights starts, it checks the limits of the `couchbase` user. If the maximum number of open files is below 200000, or the maximum number of processes is below 10000, it prints a warning such as the following, and then continues to start:

The maximum number of open files for the couchbase user is set too low (1024).
It must be at least 200000.

When Operational Insights is installed as a package, the `operational-insights` systemd service sets the open-file limit to 200000\. If you start Operational Insights some other way, for example with the [operational-insights](../../cli/operational-insights.md) command after a non-root install, raise the limits for the `couchbase` user by adding entries such as the following to `/etc/security/limits.conf`, where each value is at least the minimum shown in the warning:

couchbase soft nofile 200000
couchbase hard nofile 200000
couchbase soft nproc 10000
couchbase hard nproc 10000

IP address seems to have changed

Error message:

IP address seems to have changed. Unable to listen on 'ns_1@'

This message means that Operational Insights had a problem opening a port with that address. Operational Insights listens on all interfaces (0.0.0.0), and chooses which interface to use for its cluster host name (Erlang OTP hostname, not DNS hostname, though the two values can be the same) (ns\_1@IP) by determining which interface would lead out to external networks. This is defined by your routing table. This error often occurs due to a networking issue, particularly around DHCP and DNS resolution.

Cluster version compatibility mismatch

Error message:

 This node cannot add another node (ns@xx.xx.xx) because of cluster compatibility mismatch.
 Cluster works in [version xx] mode and only support [version xx].

This message means that the cluster is at version XX and only supports adding nodes XX or higher. Typically, to enable certain features like client-server SSL, all the nodes of the cluster to be at a required compatibility level or higher that supports the feature.

Difficulties communicating with the cluster. Displaying cached information.

Error message:

Lost connection to server at <IP>:8091. Repeating in XX seconds. Retry now. Repeating failed XHR request...

You are seeing the cached UI. This issue is mostly due to the network connection between your system and the Operational Insights node. Verify your connectivity to the Operational Insights node using `ping` and `telnet`.

Transparent huge server pages enabled

Linux distributions such as Red Hat Enterprise Linux (RHEL) manage huge pages by default with Transparent Huge Pages (THP). It combines smaller memory pages into Huge Pages without the running processes knowing. The idea is to reduce the number of lookups on TLB required and therefore increase performance. It introduces an abstraction for automation and management of huge page. Couchbase Engineering has determined that under some conditions, **Operational Insights can be negatively impacted by severe page allocation delays when THP is enabled**. Couchbase therefore recommends that THP be disabled on all Operational Insights nodes. For the full procedure, see [Disabling Transparent Huge Pages (THP)](../../install/thp-disable.md).

To disable THPs on a running system temporarily, run the following commands:

 # Disable THP on a running system
      sudo echo never > /sys/kernel/mm/transparent_hugepage/enabled
      sudo echo never > /sys/kernel/mm/transparent_hugepage/defrag

To disable this permanently, do the following:

# Backup rc.local
      sudo cp -p /etc/rc.local /etc/rc.local.`date +%Y%m%d-%H:%M`

Then copy the following into the bottom of /etc/rc.local.

if test -f /sys/kernel/mm/transparent_hugepage/enabled; then
      echo never > /sys/kernel/mm/transparent_hugepage/enabled
      fi

      if test -f /sys/kernel/mm/transparent_hugepage/defrag; then
      echo never > /sys/kernel/mm/transparent_hugepage/defrag
      fi

Swappiness enabled

Swappiness levels tell the virtual memory subsystem how much it should try and swap to disk. The thing is, the system will try to swap out items in memory even when there is plenty of RAM available to the system. The OS default is usually 60, and you can see what value your system is set to by running the following command:

 cat /proc/sys/vm/swappiness

Operational Insights is tuned to operate in memory as much as possible. On systems that use cgroups v1, the `operational-insights` service sets swappiness to 0 for its own cgroup when it starts; the steps below set it for the whole system. For more information, see [Configure Kernel Swappiness](../../install/swap-space-kernel-swappiness.md). You can gain or at minimum not lose performance by just changing the swappiness value to 0\. This tells the virtual memory subsystem of the OS to not swap items from RAM to disk unless it really has to. If you have correctly sized your nodes, swapping should not be needed. To set this, run the following commands as root, or with `sudo`.

1. Set the value for the running system:  
sudo echo 0 > /proc/sys/vm/swappiness
2. Backup sysctl.conf:  
sudo cp -p /etc/sysctl.conf /etc/sysctl.conf.`date +%Y%m%d-%H:%M`
3. Set the value in /etc/sysctl.conf so it stays after reboot:  
sudo echo '' >> /etc/sysctl.conf  
       sudo echo '#Set swappiness to 0 to avoid swapping' >> /etc/sysctl.conf  
       sudo echo 'vm.swappiness = 0' >> /etc/sysctl.conf  
Make sure that you either have or modify your process that builds your OSs to do this. This is especially critical for public/private clouds where it is so easy to bring up new instances. You need to make this part of your build process for an Operational Insights node.