---
title: Verify VPC Peering Connectivity
description: Use the procedures on this page to verify that a VPC peering
  connection is working correctly and help troubleshoot connectivity issues.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clouds/pages/vpc-peering/verify-troubleshoot.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clouds:vpc-peering/verify-troubleshoot.adoc[]
---

[View original HTML](/cloud/clouds/vpc-peering/verify-troubleshoot.html)

# Verify VPC Peering Connectivity

> Use the procedures on this page to verify that a VPC peering connection is working correctly and help troubleshoot connectivity issues. 

## [](#verify-connectivity)Verify VPC Peering Connection

With a new VPC Peering connection, check that applications connecting from the application VPC are using the private network correctly.

### [](#hostname-resolution)Check Hostname Resolution

When an application connects to a Capella cluster, its first step is to resolve the hostnames of all nodes in the cluster. Use the following procedure to check that hostname resolution is working correctly:

1. In the Capella UI, retrieve the DNS SRV record for your cluster by clicking the **Connect** tab.
2. With the DNS SRV record, use `nslookup` to resolve the hostname. For example:  
```console  
nslookup -type=SRV _couchbases._tcp.cb.a-lxzt-gdkzoqfuu.cloud.couchbase.com  
```  
```console  
Server:   	 127.0.0.53  
Address:    127.0.0.53#53  
Non-authoritative answer:  
_couchbases._tcp.cb.a-lxzt-gdkzoqfuu.cloud.couchbase.com    service = 0 0 11207 9qvj8x-f2oxhahtz.a-lxzt-gdkzoqfuu.cloud.couchbase.com.  
_couchbases._tcp.cb.a-lxzt-gdkzoqfuu.cloud.couchbase.com    service = 0 0 11207 jkzlapnfpklgjhtl.a-lxzt-gdkzoqfuu.cloud.couchbase.com.  
_couchbases._tcp.cb.a-lxzt-gdkzoqfuu.cloud.couchbase.com    service = 0 0 11207 4ncgebm6lmtbxmkr.a-lxzt-gdkzoqfuu.cloud.couchbase.com.  
```
3. Use `nslookup` to resolve one of the hostnames returned from the SRV record. For example:  
```console  
nslookup 9qvj8x-f2oxhahtz.a-lxzt-gdkzoqfuu.cloud.couchbase.com  
```  
```console  
Server:   	 127.0.0.53  
Address:    127.0.0.53#53  
Non-authoritative answer:  
Name:    9qvj8x-f2oxhahtz.a-lxzt-gdkzoqfuu.cloud.couchbase.com  
Address: 10.0.18.110  
```
4. When the DNS resolution is working correctly, `nslookup` returns the private IP of the Capella node—​an IP from the cluster’s CIDR block. If the `nslookup` returns the public IP for this node and you’re using AWS, check that you have:

  * Enabled DNS resolution
  * Enabled DNS hostnames
  * Associated the hosted zone with your VPC  
  For more information, see [Create a VPC Peering Connection with AWS](peer-aws.md).

### [](#check-network-connectivity)Check Network Connectivity

If DNS resolution is working correctly, use the following procedure to check the network connectivity between your application instances and your Capella cluster:

1. To check that the routing works for your VPC, use `traceroute` with one of the nodes in your cluster that you resolved when [checking DNS resolution](#hostname-resolution). For example:  
```console  
traceroute -T 9qvj8x-f2oxhahtz.a-lxzt-gdkzoqfuu.cloud.couchbase.com -p 18091  
```  
```console  
traceroute to 9qvj8x-f2oxhahtz.a-lxzt-gdkzoqfuu.cloud.couchbase.com (10.0.18.110), 30 hops max, 60 byte packets  
 1  ip-10-0-18-110.us-west-2.compute.internal (10.0.18.110)  0.303 ms  0.288 ms  0.302 ms  
```
2. The result from this `traceroute` should return quickly. If it’s slow, this can indicate issues with your routing. Validate the route table associated with the VPC to check that you have associated the correct CIDR block with the VPC peering connection.
3. Use `curl` to validate that Couchbase Server is responding correctly over the private network:  
```console  
$ curl -k https://9qvj8x-f2oxhahtz.a-lxzt-gdkzoqfuu.cloud.couchbase.com:18091  
```  
```console  
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN"><html><head><title>301 Moved Permanently</title></head><body><h1>Moved Permanently</h1><p>The document has moved <a href="https://9qvj8x-f2oxhahtz.a-lxzt-gdkzoqfuu.cloud.couchbase.com:18091/ui/index.html>here</a>.</p></body></html>  
```

## [](#troubleshooting)Troubleshooting

> [!TIP]
> Tools such as the [AWS VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) can be useful to verify communications.

If you entered an incorrect CIDR block, application VPC, VPC ID, or other information when creating a VPC peering connection, you must delete that connection and create a new one with the correct values.

AWS

* On your AWS VPC, check that you have enabled the DNS hostname and DNS resolution settings. If you need to change these settings, allow time for DNS caching before trying again. For more information, see [AWS VPC Peering Prerequisites](peer-gcp.md#Prerequisites).

Azure

* While Capella supports multiple subscriptions within a single Azure tenant, VNet peering across two or more Azure tenants is not supported.
* Check that you have accepted the permissions request from Capella.

GCP

* Check that you have finished the setup by running the `gcloud` commands to accept the peering request and link your VPC to the appropriate DNS server for hostname resolution. For more information, see [Finish GCP VPC Connection Setup](peer-gcp.md#finish-gcp-peer).

### [](#status-information)Status Information

The following table provides information about the possible VPC connection statuses:

__Table 1\. VPC Peering Connection Status__
| Status                      | Description                                                                                                                 |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Not Setup (Default state)   | No networks exist and no infrastructure has been provisioned.                                                               |
| Linking Network             | One or more networks are being connected, the infrastructure is being provisioned, or both.                                 |
| Linking Failed              | One or more networks have failed to connect, but the infrastructure was provisioned successfully.                           |
| Infrastructure Failed       | Infrastructure provisioning failed.                                                                                         |
| Ready                       | One or more networks are linked successfully.                                                                               |
| No Networks                 | No networks are linked but the infrastructure has been provisioned for your cluster.                                        |
| Infrastructure Provisioning | The infrastructure is being provisioned. This is an intermediate state that’s only possible for the first VPC peering link. |

> [!NOTE]
> Creating multiple networks rapidly may cause both the Linking and Provisioning states to display as 'Failed'.