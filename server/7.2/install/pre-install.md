---
title: System Resource Requirements
description: Although resource requirements will largely depend on the size and
  resource demands of your Couchbase deployment, there are some minimum and
  recommended specifications that you should follow.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/pre-install.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:install:pre-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/pre-install.html)

# System Resource Requirements

> Although resource requirements will largely depend on the size and resource demands of your Couchbase deployment, there are some minimum and recommended specifications that you should follow. 

* x86 Processors
* ARM Processors

|                          | Minimum Specifications\*                                                                              | Recommended Specifications\*\*                                                                                                                                |
| ------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CPU**                  | 2 GHz dual core x86\_64 CPU supporting SSE4.2                                                         | 3 GHz quad core x86\_64 CPU supporting SSE4.2 and above 3 GHz six core x86\_64 CPU supporting SSE4.2 when using Cross Datacenter Replication (XDCR) and Views |
| **RAM**                  | 4 GB (physical)                                                                                       | 16 GB (physical) and above                                                                                                                                    |
| **Storage (disk space)** | 8 GB (block-based; HDD, SSD, EBS, iSCSI) Network file systems such as CIFS and NFS are not supported. | 16 GB and above (block-based; HDD, SSD, EBS, iSCSI) Network file systems such as CIFS and NFS are not supported.                                              |

|                          | Minimum Specifications\*                                                                              | Recommended Specifications\*\*                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **CPU**                  | 2 Ghz dual core 64bit ARM v8 CPU                                                                      | 2.5 Ghz quad core 64bit ARM v8 CPU                                                                               |
| **RAM**                  | 4 GB (physical)                                                                                       | 16 GB (physical) and above                                                                                       |
| **Storage (disk space)** | 8 GB (block-based; HDD, SSD, EBS, iSCSI) Network file systems such as CIFS and NFS are not supported. | 16 GB and above (block-based; HDD, SSD, EBS, iSCSI) Network file systems such as CIFS and NFS are not supported. |

\*_You can reduce the CPU and RAM resources below the Minimum Specifications for development and testing purposes. Resources can be as low as 1 GB of free RAM beyond operating system requirements, and a single CPU core. However, you must adhere to the Minimum Specifications for production._

\*\*_The Recommended Specifications don’t take into account your intended workload. You should follow the [sizing guidelines](sizing-general.md) when determining system specifications for your Couchbase Server deployment._

Clock Source on Linux

The Query service uses the OS monotonic clock for profiling and network timeout purposes.

The Linux kernel uses the _Clock Source_ to obtain the current clock value and this information is stored in `/sys/devices/system/clocksource/clocksource0/current_clocksource`. There are several clock sources (TSC, XEN, and others), which are used depending on the hardware clock capabilities, and the OS installation. The XEN source, which is seen to be the default on AWS setups, can use up to 25% of all available CPU time to obtain the current timestamp. The TSC clock source, on the other hand, incurs very little CPU cost. We recommend changing the clock source to TSC if it is set to anything else.

Check the clock source on your Linux OS using the following command:

```bash
cat /sys/devices/system/clocksource/clocksource0/current_clocksource
```

\+ Change the clock source using the following commands:

```bash
echo tsc > /sys/devices/system/clocksource/clocksource0/current_clocksource
```

\+ To verify the current setting of the clock source, use:

```bash
cat /sys/devices/system/clocksource/clocksource0/current_clocksource
```

\+ The output should read `tsc`.