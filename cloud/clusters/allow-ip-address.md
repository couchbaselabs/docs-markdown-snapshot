[View original HTML](/cloud/clusters/allow-ip-address.html)

> Before a cluster can connect to a client, you must add the client’s IP address to the cluster’s Allowed IP list. 

Couchbase Capella only allows clusters to connect to trusted IP addresses. Each cluster has a configurable Allowed IP list that can include up to 75 entries. Each entry can be a single IP address or an IP address space in [ipv4](https://en.wikipedia.org/wiki/IPv4) format.

For example, you could set a specific allowed IP address, like `141.193.213.10` or a range using a CIDR block like `141.193.213.0/24`.

You can set any IP address on this list to have a specific expiration time for temporary access or be permanent. Capella automatically denies any connection attempts to and from an IP not in the allowed IP list.

## [](#prerequisites)Prerequisites

* You must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner), [Project Owner](../projects/project-roles.md#project-owner-role), or [Cluster Manager](../projects/project-roles.md#project-cluster-manager-role) role to view or update the list of allowed IP addresses on your cluster.

## [](#view-allowed-ip-addresses-for-a-cluster)View Allowed IP Addresses for a Cluster

To view the current allowed IP addresses for your cluster:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Settings** **Allowed IP Addresses**.

This **Allowed IP** summary displays the following information about each IP:

| Information           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IP Address/CIDR block | The allowed IP address or address space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Status                | The current status of the allowed IP, which can include the following: **Active**: The allowed IP address is active. An IP with this status can connect to and from the current cluster. **Pending**: The allowed IP address is not yet active. An IP with this status is in the process of becoming active. **Failed**: The allowed IP address is in a failed state. An IP with this status failed to activate and needs to be deleted and recreated. **Expired**: The allowed IP address was configured as temporary and has expired. An IP with this status is currently disallowed and needs to be deleted and recreated to be allowed again. |
| Expiration            | The expiration date and time of a temporary allowed IP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Type                  | The type of allowed IP, which is either **Temporary** or **Permanent**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Comment               | The comment included with the allowed IP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

A Trash icon displayed at the end of each row can [delete an allowed IP](#delete-allowed-ip).

## [](#add-allowed-ip)Add an Allowed IP Address

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Settings** **Allowed IP Addresses**.
4. Click **Add Allowed IP**.
5. Enter the IP address or CIDR block range in ipv4 format that you want to have access to your cluster:

  1. Click **Add Current IP Address** to populate the **Allowed IP / CIDR Block** field with the external IP address of your current device.
  2. Click **Allow Access from Anywhere** to allow all IP addresses to connect to your cluster.  
  This option adds the IP address `0.0.0.0/0` as an allowed IP on your cluster.

|  | Couchbase does not recommend allowing access from all IP addresses on production clusters. |
|  | ------------------------------------------------------------------------------------------ |
  3. Enter an IP address or IP address range in ipv4 CIDR notation in the **Allowed IP / CIDR Block** field.  
  You can get the external IP address for a device from:

    * Your networking or router configuration
    * A DNS lookup, using a command like `nslookup myip.opendns.com`
    * An external service or website that identifies your IP address
6. In the **Time to retain** list, choose how long you want Capella to retain the allowed IP address and allow connections from it to your cluster.

|  | After your chosen amount of time has passed, the IP address entry expires, and the cluster stops taking connections from the IP address. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------- |
7. (Optional) In the **Comment** field, add a comment about the allowed IP address entry.  
This can help inform other users in your organization about why the IP address is being allowed.

|  | Comments cannot exceed 128 characters. |
|  | -------------------------------------- |
8. To save and add the allowed IP address or CIDR block, click **Add Allowed IP**.

It can take a few minutes for your cluster to start allowing connections from a new allowed IP address. If you try to immediately connect to your cluster from a newly allowed IP, your connection may be blocked.

## [](#edit-an-allowed-ip-address)Edit an Allowed IP Address

You cannot make changes to an existing allowed IP address. To change the configuration for an allowed IP, [delete](#delete-allowed-ip) the IP address and [add](#add-allowed-ip) it again.

## [](#delete-allowed-ip)Delete an Allowed IP Address

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Settings** **Allowed IP Addresses**.
4. In the list of allowed IP addresses, next to the entry you want to delete, click the trashcan.
5. Confirm that you want to delete the allowed IP address.
6. Click **Delete Allowed IP**.

After you delete an allowed IP, it can take a few minutes for the cluster to begin rejecting traffic from that address.

## [](#see-also)See Also

* [Connect to Your Cluster](../get-started/connect.md)
* [Configure Cluster Credentials](manage-database-users.md)