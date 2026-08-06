---
title: Disabling Transparent Huge Pages (THP)
description: Transparent huge pages (THP) is a memory management system that is
  enabled by default in most Linux operating systems.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/thp-disable.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:install:thp-disable.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/install/thp-disable.html)

# Disabling Transparent Huge Pages (THP)

> Transparent huge pages (THP) is a memory management system that is enabled by default in most Linux operating systems.
> 
> You must disable THP in order for Enterprise Analytics to function on Linux, since THP enabled can worsen performance and increasing the risk of out-of-memory (OOM) conditions.

In Linux operating systems, THP is a feature that provides a way for the CPU and OS to create pre-allocated contiguous memory space to improve application performance. THP automates the creation of contiguous memory space and conceals much of the complexity of using actual huge pages on systems with large amounts of memory.

THP is enabled by default in most Linux operating systems, and functions well for most applications and processes. However, THP is detrimental to Couchbase's performance.

Since you tend to have more random, sparse data access, you allocate pages that can remain mostly empty. This leads to memory fragmentation as portions of memory are not used but still accounted for in the RSS. As a result, the data stored may be smaller while RSS can be more, increasing the risk of out-of-memory (OOM) conditions. Therefore, you must disable THP on Linux systems so that Enterprise Analytics performs optimally.

## [](#init-script)Using Init Script

1. Create the init script:  
```console  
vi /etc/init.d/disable-thp  
```  
Add the following contents:  
```bash  
#!/bin/bash  
### BEGIN INIT INFO  
# Provides:          disable-thp  
# Required-Start:    $local_fs  
# Required-Stop:  
# X-Start-Before:    enterprise-analytics  
# Default-Start:     2 3 4 5  
# Default-Stop:      0 1 6  
# Short-Description: Disable THP  
# Description:       Disables transparent huge pages (THP) on boot, to improve  
#                    Couchbase performance.  
### END INIT INFO  
case $1 in  
  start)  
    if [ -d /sys/kernel/mm/transparent_hugepage ]; then  
      thp_path=/sys/kernel/mm/transparent_hugepage  
    elif [ -d /sys/kernel/mm/redhat_transparent_hugepage ]; then  
      thp_path=/sys/kernel/mm/redhat_transparent_hugepage  
    else  
      return 0  
    fi  
    echo 'never' > ${thp_path}/enabled  
    echo 'never' > ${thp_path}/defrag  
    re='^[0-1]+$'  
    if [[ $(cat ${thp_path}/khugepaged/defrag) =~ $re ]]  
    then  
      # RHEL 7  
      echo 0  > ${thp_path}/khugepaged/defrag  
    else  
      # RHEL 6  
      echo 'no' > ${thp_path}/khugepaged/defrag  
    fi  
    unset re  
    unset thp_path  
    ;;  
esac  
```  
Save and close your editor.
2. Make the script executable:  
```console  
sudo chmod 755 /etc/init.d/disable-thp  
```
3. Configure the OS to run the script on boot:

  * Red Hat
  * Ubuntu and Debian  
```console  
sudo chkconfig --add disable-thp  
```  
```console  
sudo update-rc.d disable-thp defaults  
```
4. Override `tuned` and `ktune`, if necessary:  
If you use `tuned` or `ktune` (for example, if you run Red Hat 7+) you must also [configure them to preserve the above settings after reboot](#tuned-ktune).
5. Reboot the system and [verify that THP is disabled](#verify-thp):

### [](#tuned-ktune)If Using `tuned` and `ktune`

`tuned` and `ktune` are system monitoring and tuning tools available on Red Hat. When they're in use on a system, you can use them to enable and disable THP.

To disable THP in `tuned` and `ktune`, you need to edit or create a new profile that sets THP to `never`.

* Red Hat 7

1. Create a new `tuned` directory for the new profile:  
```console  
sudo mkdir /etc/tuned/no-thp  
```
2. Create and edit `tuned.conf`:  
```console  
vi /etc/tuned/no-thp/tuned.conf  
```  
Add the following contents:  
```console  
[main]  
include=virtual-guest  
[vm]  
transparent_hugepages=never  
```  
Save and close your editor.
3. Enable the new profile:  
```console  
sudo tuned-adm profile no-thp  
```

## [](#verify-thp)Verify THP Status

You can check the THP status by issuing the following commands.

* Red Hat  
```console  
cat /sys/kernel/mm/transparent_hugepage/enabled  
```  
```console  
cat /sys/kernel/mm/transparent_hugepage/defrag  
```
* Other Linux Variants  
```console  
cat /sys/kernel/mm/transparent_hugepage/enabled  
```  
```console  
cat /sys/kernel/mm/transparent_hugepage/defrag  
```

If THP is properly disabled, the output of both commands should be the following:

```console
always madvise [never]
```

## [](#using-thp-service)Using a THP Service

1. Create a service file:  
```console  
vi /etc/systemd/system/disable-thp.service  
```
2. Add the service configuration details to the file and then save it:  
```console  
[Unit]  
Description=Disable Transparent Huge Pages (THP)  
DefaultDependencies=no  
After=sysinit.target local-fs.target  
Before=enterprise-analytics.service  
[Service]  
Type=oneshot  
ExecStart=/bin/sh -c 'echo never | tee /sys/kernel/mm/transparent_hugepage/enabled > /dev/null'  
ExecStart=/bin/sh -c 'echo never | tee /sys/kernel/mm/transparent_hugepage/defrag > /dev/null'  
[Install]  
WantedBy=basic.target  
```
3. Reload the `systemctl` files:  
```console  
sudo systemctl daemon-reload  
```
4. Start the service:  
```console  
sudo systemctl start disable-thp  
```
5. Make sure that the service starts whenever you reboot it.  
```console  
sudo systemctl enable disable-thp  
```

## [](#verify-thp-service)Verify THP is Disabled

Execute the following commands to make sure the service has disabled the THP.

```console
cat /sys/kernel/mm/transparent_hugepage/enabled
cat /sys/kernel/mm/transparent_hugepage/defrag
```