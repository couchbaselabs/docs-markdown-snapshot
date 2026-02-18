---
title: Configure Allowed IP Addresses
description: Before a client can connect to a Capella Analytics cluster, you
  must add the client's IP address to the cluster's allowed IP list.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/ip-allowed-list.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/analytics/admin/ip-allowed-list.html)

# Configure Allowed IP Addresses

> Before a client can connect to a Capella Analytics cluster, you must add the client’s IP address to the cluster’s allowed IP list. 

## [](#overview)Overview

Capella Analytics only allows trusted IP addresses to connect to a cluster. For each cluster, you can configure a list of up to 75 trusted, allowed IP addresses.

* Each entry can be a single IP address or an IP address space.
* When you add an IP address to this list, you can specify an expiration period to permit access temporarily, or make access available permanently.
* You add the first IP address to the allowed list using the UI. After you add the first IP address, you can add more IP addresses using either the UI or the Capella Analytics services Management API.

Capella automatically denies any connection attempts to and from an IP address that’s not in the list.

> [!NOTE]
> You configure the list of IP addresses that can access a Capella Analytics cluster and the list of IP addresses that can access a Couchbase Capella operational database separately. To configure access to a Capella operational database, see [Configure Allowed IP Addresses](../../cloud/clusters/allow-ip-address.md).

## [](#prerequisites)Prerequisites

To view and configure the list of allowed IP addresses, you must have the Organization Owner, Project Owner, or Project Manager role. See [Organization Roles](../../cloud/organizations/organization-user-roles.md).

## [](#accessing-the-allowed-ip-addresses-list)Accessing the Allowed IP Addresses List

To view the allowed IP addresses:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Select a Capella Analytics cluster and then click **Settings**.
3. Under **Networking**, select **Allowed IP Addresses**.

The page that opens displays the following information about each allowed IP address:

IP Address/CIDR block

The allowed IP address or address space.

Status

The current status of the allowed IP, which can be:

* **Active**: The IP address is allowed to connect. An IP with this status can connect to and from the current cluster.
* **Pending**: The allowed IP address is not yet allowed to connect. An IP with this status is in the process of becoming active.
* **Failed**: The connection for this IP address failed to activate. To allow this IP to connect, you must delete and then re-add it.
* **Expired**: The IP address is no longer allowed to connect as its temporary access period has expired. To allow an IP with this status to connect, you must delete and then re-add it.

Expiration

The expiration date and time of an allowed IP that has access only for a defined time period.

Type

The type of allowed IP, which is either **Temporary** or **Permanent**.

Comment

The comment included with the allowed IP.

## [](#add-allowed-ip)Add an Allowed IP Address

To add an allowed IP address:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Select a Capella Analytics cluster and then click **Settings**.
3. Under **Networking**, select **Allowed IP Addresses**. The **Allowed IP Addresses** list opens.
4. Click **Add Allowed IP**. The **Add Allowed IP** page opens with the following options for adding an IP address:

  * To add the IP address of your current device, click **Add Current IP Address**. The **Allowed IP Address/CIDR Block** field fills with the IP address being used to communicate with Couchbase Capella.
  * To allow any IP address to connect to your cluster, click **Allow Access from Anywhere**. A confirmation dialog opens.
  * To add a specific IP address or address space, enter the address in the **Allowed IP Address/CIDR Block** field.
5. For the **Time to Retain**, choose **Permanent** or select a pre-defined time period to provide access only temporarily. Temporary access can be useful for development and testing, and expires automatically.
6. Optionally, add a comment of up to 128 characters. The **Comment** appears on the Allowed IP Address to provide information about why the IP address is allowed, its expiration period, and so on.
7. When you’re satisfied with the configuration, click **Add Allowed IP**. It can take a few minutes for the cluster to activate access for a newly added IP address. If you immediately try to connect to the cluster from a newly added IP, its connection might be blocked.

## [](#modify-an-allowed-ip-address)Modify an Allowed IP Address

You cannot change the configuration for an allowed IP address. Instead, you [delete](#delete-allowed-ip) the allowed IP and then [add](#add-allowed-ip) it again with the updated configuration.

## [](#delete-allowed-ip)Delete an Allowed IP Address

To delete an allowed IP address:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Select a Capella Analytics cluster and then click **Settings**.
3. Under **Networking**, select **Allowed IP Addresses**. The **Allowed IP Addresses** list opens.
4. Locate the IP address you want to delete, and click the trashcan icon that appears at the end of its row. A confirmation dialog opens.
5. Type `delete` into the provided field.
6. Click **Delete Allowed IP**.  
When you delete an allowed IP, it can take a few minutes for the cluster to begin rejecting traffic from that address.

## [](#see-also)See Also

* [Manage Deployments with the Capella Analytics Management API](../management-api-guide/management-api-intro.md)
* [VPC Peering with AWS](vpc-peering.md)
* [VPC Peering with GCP](vpc-peering-gcp.md)
* [AWS PrivateLink Connection](private-endpoint.md)
* [Manage Access to Cluster Data](auth/auth-data.md)
* [Configure Allowed IP Addresses](../../cloud/clusters/allow-ip-address.md) for a Capella database