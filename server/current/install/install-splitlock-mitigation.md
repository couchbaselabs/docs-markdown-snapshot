---
title: How to mitigate Split Lock Issues
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/install-splitlock-mitigation.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:install:install-splitlock-mitigation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/install/install-splitlock-mitigation.html)

# How to mitigate Split Lock Issues

> Disable Linux split lock mitigation on systems where it causes performance degradation with Couchbase Server. 

On some Linux kernels that support split lock detection, the kernel’s split lock mitigation can cause severe performance degradation when a process triggers a misaligned atomic memory access. This may appear as high latency and reduced throughput under load on Couchbase Server hosts.

## [](#prerequisites)Prerequisites

* You have confirmed that split lock mitigation is contributing to performance degradation on your system.
* You have root or sudo access to the affected host.
* You understand that disabling split lock mitigation changes kernel behavior intended to reduce the impact of split locks on system performance.

## [](#procedure)Procedure

Choose 1 of the following methods to disable split lock mitigation:

### [](#method-1-kernel-boot-parameter-recommended)Method 1: Kernel Boot Parameter (Recommended)

1. Open your bootloader configuration file (for example, `/etc/default/grub`).
2. Add the following to the `GRUB_CMDLINE_LINUX` parameter:  
```text  
split_lock_detect=off  
```
3. Update your bootloader configuration:  
```bash  
sudo update-grub  
```
4. Reboot the host for the change to take effect.

### [](#method-2-runtime-setting)Method 2: Runtime Setting

1. Run the following command to disable mitigation via `/proc`:  
```bash  
echo 0 | sudo tee /proc/sys/kernel/split_lock_mitigate  
```  
> [!NOTE]  
> This change does not persist across reboots. To make it permanent, add this command to a startup script or use the kernel boot parameter method.
2. Verify the setting was applied:  
```bash  
cat /proc/sys/kernel/split_lock_mitigate  
```  
The output should be `0`.

## [](#next-steps)Next Steps

* Monitor your Couchbase Server performance to confirm the issue is resolved.
* [Learn more about monitoring Couchbase Server](../manage/monitor/monitor-intro.md).