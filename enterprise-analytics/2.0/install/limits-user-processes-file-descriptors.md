---
title: Establish Limits for User Processes and File Descriptors
description: You can configure Linux system limits for user processes and file
  descriptors to meet Enterprise Analytics requirements.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/install/pages/limits-user-processes-file-descriptors.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:install:limits-user-processes-file-descriptors.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/install/limits-user-processes-file-descriptors.html)

# Establish Limits for User Processes and File Descriptors

The maximum permitted number of concurrent user processes, and currently open file descriptors, are established on Linux systems with default values that are low for running Enterprise Analytics with optimal performance and scale. The maximum number of user processes must be reset to at least 10,000 and the maximum number of file descriptors to at least 200,000.

To establish limits for user processes and file descriptors:

1. To check the current setting for user processes for the current administrator, use:  
ulimit -u  
The response indicates the maximum number of user processes permitted for the administrator, which this example assumes to be the default value, applied to all users.  
3829  
In this case, the number `` 3829`is lesser than the Enterprise-Analytics requirement of `10000 ``.
2. To check the current setting for file descriptors, use:  
ulimit -n  
The response indicates the maximum number of file descriptors permitted for the administrator, which this example assumes to be the default value, applied to all users.  
1024  
In this case, the number `1024` is lesser than the Enterprise-Analytics requirement of `200000`.
3. To raise the current limits on user processes and file descriptors, access `/etc/security/limits.conf`, and add `hard` and `soft` lines for the `nproc` and `nofile` types, specifying appropriate values. The `domain` value should be the user-name of the user, or the group-name of the group, designated to install and run Enterprise Analytics.  
Following these additions, the lines should appear as follows:  
nameofuserorgroup       soft    nproc           10000  
nameofuserorgroup       hard    nproc           10000  
nameofuserorgroup       soft    nofile          200000  
nameofuserorgroup       hard    nofile          200000  
Save the file and exit.
4. Reboot the machine.
5. Following reboot, the designated user or group-member can check all the limits that apply to them, as follows:  
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