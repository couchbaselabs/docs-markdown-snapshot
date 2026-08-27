---
title: Manage Connections and Disks
description: Couchbase-Server security can be enhanced by proper management of
  connections and disks.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-security/manage-connections-and-disks.adoc
  xref: xref:enterprise-analytics:manage:manage-security/manage-connections-and-disks.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-security/manage-connections-and-disks.html)

# Manage Connections and Disks

> Couchbase-Server security can be enhanced by proper management of connections and disks. 

## [](#network-security-recommendations)Network Security Recommendations

Attaining a fully secure Enterprise Analytics network-environment requires appropriate measures in the following areas.

### [](#establishing-firewalls-and-protecting-files)Establishing Firewalls and Protecting Files

The following measures are strongly recommended:

* Set up a firewall to block `epmd` port 4369 from access from outside the cluster-network.
* Set up a firewall to block `erlang` ports from access from outside the cluster-network. These ports are configurable: in the default installation, their range is: 21100 to 21299.
* Restrict access to the below directory:

  * On Linux: `/opt/enterprise-analytics`

See [Manage System Secrets](manage-system-secrets.md) for details on how to define and use the master password.

### [](#securing-the-network)Securing the Network

To secure the network on which your Enterprise Analytics-cluster resides:

* Allow administrative access to Enterprise Analytics only through specific machines, such as _jump servers_. To perform auditing on access-attempts made from these machines, turn on the OS-level auditing facility on each.
* Use IPSec on your local network. For guidance, consult the following online information-resources:

  * [About IPSec](http://en.wikipedia.org/wiki/Ipsec)
  * [Configuring IPSec on Windows](https://www.youtube.com/watch?v=3hve3ZQJIdk)
  * [Configuring IPSec on Linux](http://www.infond.fr/2010/04/basics-9-tutorial-ipsec-transport-mode.html)

### [](#controlling-access-to-files)Controlling Access to Files

To restrict user-access to files and directories, traditional file-permissions can be used. Additionally, Red Hat Enterprise Linux (RHEL) provides the following options:

* [Security Enhanced Linux](https://access.redhat.com/documentation/en-US/Red%5FHat%5FEnterprise%5FLinux/6/html/Security-Enhanced%5FLinux/)
* [Access Control Lists](https://access.redhat.com/documentation/en-US/Red%5FHat%5FEnterprise%5FLinux/6/html/Storage%5FAdministration%5FGuide/ch-acls.html).

### [](#configuring-ip-tables)Configuring IP Tables

SSH-access to Enterprise Analytics and access to the Enterprise Analytics administrative ports (8091 and 8092) can be restricted to specified machines. Such restrictions can be established either at the network or at the system level, using _IP tables rules_. Specifically, you can either:

* Execute the `iptables` command.
* Edit the file _/etc/sysconfig/iptables_:  
##allow everyone to access port 80 and 443##
      -A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT
      -A INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT

For more information, see [IP tables rules](https://access.redhat.com/documentation/en-US/Red%5FHat%5FEnterprise%5FLinux/6/html/Security%5FGuide/sect-Security%5FGuide-IPTables.html). Additionally, a sample of IP tables rules can be found in [this blog](http://blog.couchbase.com/iptables-firewall-settings-couchbase-db-and-couchbase-mobile-syncgateway).

### [](#controlling-ports)Controlling Ports

Access to Enterprise Analytics ports may need to be controlled. For a complete list of ports, see [Enterprise Analytics Ports](../../install/cb-enterprise-analytics-ports.md).

A sample script for configuring the IP-tables firewall-settings is located in the following blog posting: [IPTables Firewall Settings for Couchbase DB and Couchbase Mobile Sync\_gateway](http://blog.couchbase.com/iptables-firewall-settings-couchbase-db-and-couchbase-mobile-syncgateway)

## [](#securing-on-disk-data)Securing On-Disk Data: Encryption at Rest

Data that resides on physical media, and is intended to be used by Enterprise Analytics, should be protected.

### [](#protecting-physical-media)Protecting Physical Media

Enterprise Analytics uses physical media to store files and indexes. If media are stolen, data becomes vulnerable to illicit access.

Therefore, to secure such data, encrypt all important data and index storage-locations, using _transparent data encryption_, provided by 3rd party on-disk encryption software-vendors; which denies data-access to anyone who either does not possess an appropriate encryption-key, or is otherwise non-compliant with the configured security policy. Such encryption ensures that stored data cannot be compromised; even if the database is stolen, copied, lost, or otherwise improperly accessed.

Commonly used 3rd party encryption tools include:

* [Linux Unified Key Setup (LUKS)](https://access.redhat.com/documentation/en-us/red%5Fhat%5Fenterprise%5Flinux/7/html/security%5Fguide/sec-encryption#sec-Using%5FLUKS%5FDisk%5FEncryption).
* Thales CipherTrust (formerly known as Vormetric/Gemalto): see [Product Details](https://cpl.thalesgroup.com/encryption/transparent-encryption) and [Documentation](https://thalesdocs.com/ctp/cte/Books/Online-Files/index.html).
* [Protegrity](https://www.protegrity.com/).

### [](#encryption-targets)Encryption Targets

The tools listed above all allow either _full disk_ or _file-level_ encryption to be used. If _file-level_ is chosen, the following Couchbase directories and files should be encrypted:

* Data and index file paths

  * Linux: `/opt/enterprise-analytics/var/lib/couchbase/data`
  * Windows: `C:\Program Files\couchbase\server\var\lib\couchbase\data`
* Global Secondary Index file paths

  * Linux: `/opt/enterprise-analytics/var/lib/couchbase/data/@2i`
  * Windows: `C:\Program Files\couchbase\server\var\lib\couchbase\data\@2i`
* Couchbase configuration files and directory

  * Linux: `/opt/enterprise-analytics/var/lib/couchbase/data`
  * Windows: `C:\Program Files\couchbase\server\var\lib\couchbase\data`
* Couchbase password files

  * Linux: `/opt/enterprise-analytics/var/lib/couchbase/isasl.pw` and `/opt/enterprise-analytics/var/lib/couchbase/config/`.
  * Windows: `C:\Program Files\couchbase\server\var\lib\couchbase\isasl.pw` and `C:\Program Files\couchbase\server\var\lib\couchbase\var\lib\config\`.

For more information, see the webinar provided at [Understanding Database Encryption with Couchbase and Vormetric](http://www.couchbase.com/nosql-resources/webinar/recorded).

### [](#luks-encryption-procedure)LUKS Encryption Procedure

The following command sequence can be used on Linux systems to deploy a LUKS-encrypted partition, and mount it as a data directory. The sequence makes use of:

* `/dev/sdb1`, which is the partition to be encrypted.
* `luks_keyfile.key`, which is a file containing the key to be used to unlock and to access the encrypted partition.
* `cbefs` (_Couchbase Encrypted Filesystem_), which is the name of the new filesystem on the encrypted partition.

Proceed as follows. (Note that `sudo` may be required for some commands.)

1. Ensure that `cryptsetup` is installed:  
apt-get install cryptsetup
2. Format the partition:  
cryptsetup luksFormat -d luks_keyfile.key --batch-mode /dev/sdb1
3. Unlock the partition, and make it accessible as a device named `cbefs`.  
cryptsetup luksOpen -d luks_keyfile.key /dev/sdb1 cbefs
4. Create a new filesystem:  
mkfs.xfs /dev/mapper/cbefs
5. Mount `/data` on the created filesystem:  
mount /dev/mapper/cbefs /data
6. Give user `couchbase` permission to access `/data`:  
chown couchbase:couchbase /data
7. Add entries to `fstab`:  
sed -i '/data/c\/dev/mapper/cbefs /data xfs defaults 0 2' /etc/fstab
8. Add entries to `crypttab`:  
echo "cbefs /dev/sdb1 /root/luks_keyfile.key luks" > /etc/crypttab

This concludes the sequence.

Note that this procedure can also be performed by means of the script [create\_luks\_fs.sh](https://github.com/couchbase/perfrunner/blob/master/scripts/create%5Fluks%5Ffs.sh).