---
title: System Resource Requirements
description: Although resource requirements will largely depend on the size and
  resource demands of your Couchbase deployment, there are some minimum and
  recommended specifications that you should follow.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/sys-resource-req.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/install/sys-resource-req.html)

# System Resource Requirements

> Although resource requirements will largely depend on the size and resource demands of your Couchbase deployment, there are some minimum and recommended specifications that you should follow. 

* x86 Processors
* ARM Processors

|                          | Minimum Specifications\*                                                                              | Recommended Specifications\*\*                                                                                  |
| ------------------------ | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **CPU**                  | 2 GHz dual core x86\_64 CPU supporting AVX2 or later                                                  | 3 GHz quad core x86\_64 CPU supporting AVX2 or later                                                            |
| **RAM**                  | 4 GB (physical)                                                                                       | 32 GB (physical) and more                                                                                       |
| **Storage (disk space)** | 8 GB (block-based; HDD, SSD, EBS, iSCSI) Network file systems such as CIFS and NFS are not supported. | 16 GB and more (block-based; HDD, SSD, EBS, iSCSI) Network file systems such as CIFS and NFS are not supported. |

|                          | Minimum Specifications\*                                                                              | Recommended Specifications\*\*                                                                                  |
| ------------------------ | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **CPU**                  | 2 Ghz dual core 64bit ARM v8 CPU                                                                      | 2.5 Ghz quad core 64bit ARM v8 CPU                                                                              |
| **RAM**                  | 4 GB (physical)                                                                                       | 32 GB (physical) and more                                                                                       |
| **Storage (disk space)** | 8 GB (block-based; HDD, SSD, EBS, iSCSI) Network file systems such as CIFS and NFS are not supported. | 16 GB and more (block-based; HDD, SSD, EBS, iSCSI) Network file systems such as CIFS and NFS are not supported. |

* You can reduce the CPU and RAM resources lesser than the Minimum Specifications for development and testing purposes. Resources can be as low as 1 GB of free RAM beyond operating system requirements, and a single CPU core. However, you must adhere to the Minimum Specifications for production.

  * The Recommended Specifications do not take into account your intended workload.

Clock Source on Linux

The Linux kernel uses the Clock Source to obtain the current clock value and this information is stored in `/sys/devices/system/clocksource/clocksource0/current_clocksource`. Couchbase has several clock sources, such as TSC, XEN, and others, that are used depending on the hardware clock capabilities, and the OS installation. The XEN source, which is the default on AWS setups, can use up to 25% of all available CPU time to obtain the current timestamp. The TSC clock source, on the other hand, incurs little CPU cost. Couchbase recommends changing the clock source to TSC if it’s set to anything else.

Check the clock source on your Linux OS using the following command:

```bash
cat /sys/devices/system/clocksource/clocksource0/current_clocksource
```

Change the clock source using the following commands:

```bash
echo tsc > /sys/devices/system/clocksource/clocksource0/current_clocksource
```

To verify the current setting of the clock source, use:

```bash
cat /sys/devices/system/clocksource/clocksource0/current_clocksource
```

The output should read `tsc`.