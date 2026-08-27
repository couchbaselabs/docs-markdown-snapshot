---
title: Manage Server Groups
description: Nodes can be assigned to server <em>groups</em>, in order to
  protect a cluster from large-scale infrastructure failure.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-groups/manage-groups.adoc
  xref: xref:enterprise-analytics:manage:manage-groups/manage-groups.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-groups/manage-groups.html)

# Manage Server Groups

> Nodes can be assigned to server _groups_, in order to protect a cluster from large-scale infrastructure failure. 

## [](#creating-and-maintaining-server-groups)Creating and Maintaining Server Groups

Server _groups_ can be administrator-defined to contain a number of the nodes within a Enterprise Analytics Cluster. It protects the cluster against large-scale infrastructure failure.

> [!NOTE]
> When you initialize a new Enterprise Analytics cluster, the first node is automatically placed in a server group named Group 1\. Once you create additional server groups, the **Assign Group** field becomes available when adding new server nodes to the cluster.

## [](#examples-on-this-page)Examples on This Page

The examples in the subsections show how to create and manage groups, using the [UI](#manage-groups-with-the-ui), the [CLI](#manage-groups-with-the-cli), and the [REST API](#manage-groups-with-the-rest-api) respectively.

## [](#manage-groups-with-the-ui)Manage Groups with the UI

To manage groups, navigate to the **Servers** section in the navigation bar and follow these steps:

1. In the servers screen, click the **Groups** option to use the server groups interface.
2. The **Server Groups** screen displays information about your cluster's current server groups. Initially, you'll see that the cluster contains the servers organized under default group names. By default, Enterprise Analytics places each new server into a group named Group 1.
3. To modify a group name, look for an edit option adjacent to the group name. This opens an **Edit Group Name** dialog where you can change the group name in the text field and save your changes by clicking the **Rename Group** button.

### [](#add-a-group-with-the-ui)Add a Group, with the UI

To add a new group, proceed as follows:

1. Look for an **Add Group** option, typically located in the upper area of the **Server Groups** screen.
2. Click the **Add Group** option to open the **Add New Group** dialog.
3. In the dialog:

  * Enter an appropriate name for the new group in the text field.
  * Click the **Add Group** button to create the group.

Once you enter the information, the system adds a new group and displays it in the **Server Groups** page.

### [](#move-a-server-between-groups-with-the-ui)Move a Server Between Groups, with the UI

To move a server between groups, proceed as follows:

1. On the **Server Groups** screen, locate the server you want to move in the server list.
2. Look for a **move to** option or list in the server's row.
3. Click this option to see a list of available groups that can receive the server.
4. Select the destination group from the list. Once selected, a **pending move** notification appears, indicating that the move is in the queue but not yet applied.

> [!NOTE]
> You can cancel the pending move by clicking the **Cancel move** option in the server's row.

\+ . After selecting the move, you'll notice that: - A **Reset** option and an **Apply Changes** button become available. - You can cancel the pending move by clicking the **Reset** option. . To complete the move, click the **Apply Changes** button. . After applying changes, you may see warning notifications indicating: - The cluster has unbalanced server groups. For more information see [Unequal Groups](../../../../server/current/learn/clusters-and-availability/groups.md#vbucket-distribution-across-unequal-groups). - Perform a rebalance. . Return to the **Servers** screen to see the updated group assignments and perform a rebalance if recommended. . If you need a rebalance, click the **Rebalance** button to start the rebalancing process.

### [](#delete-a-group-with-the-ui)Delete a Group, with the UI

To delete a group, you must first remove all nodes from the group. You can either do this by moving them to other groups, or by removing them entirely from the cluster. After the group is empty, you can delete it.

To delete a group by removing servers:

1. Go to the **Servers** screen and locate each server you need to remove from the group.
2. Click on the server's row to expand the details view.
3. Click **Remove** button on the bottom. A confirmation dialog appears asking you to confirm the server removal.
4. Click **Remove Server** to confirm the removal. The server shows a **REMOVAL pending rebalance** status. A **Cancel Remove** option is also available if you need to cancel the operation.
5. Click the **Rebalance** button to complete the server removal process. Repeat this process for all servers in the group you want to delete.
6. Once the group is empty, go to the **Server Groups** screen.
7. The empty group displays a notification indicating it contains no servers.
8. Click the **delete group** option for the empty group.
9. A confirmation dialog appears asking you to confirm the group deletion.
10. Click **Delete Group** to permanently remove the group.

The system deletes the group, and it no longer appears as a row on the Server Groups screen.

### [](#assign-a-group-when-adding-a-server-with-the-ui)Assign a Group when Adding a Server, with the UI

When adding a server to a cluster where multiple groups exist, you can assign the server to a specific group during the addition process.

In the **Add Server** dialog, you'll find an **Assign Group** field with a list of controls that allow you to select from existing groups. Choose the appropriate group from this list before completing the server addition.

## [](#manage-groups-with-the-cli)Manage Groups with the CLI

Use the CLI `group-manage` command to manage groups. The following subsections give examples. See also the full command reference, at [group-manage](../../cli/couchbase-cli-group-manage.md).

### [](#get-group-information-with-the-cli)Get Group Information, with the CLI

To see a list of the current groups in the cluster and which nodes are in each group, run the following command:

/opt/enterprise-analytics/bin/couchbase-cli
-u Administrator \
-p password \
--list

The output shows each group, and the nodes within it:

Group 1
 server: 10.143.190.101:8091
 server: 10.143.190.102:8091
 server: 10.143.190.103:8091

This confirms that a single group, `Group 1`, exists and has three nodes assigned to it.

### [](#add-a-group-with-the-cli)Add a Group, with The CLI

To add a new empty group, named `Group 2`, enter the following:

/opt/enterprise-analytics/bin/couchbase-cli
-u Administrator \
-p password \
--create \
--group-name 'Group 2'

If successful, this produces the following output:

SUCCESS: Server group created

Check the node-to-group assignment again, by means of the `--list` flag:

/opt/enterprise-analytics/bin/couchbase-cli
-u Administrator \
-p password \
--list

This now returns the following:

Group 1
 server: 10.143.190.101:8091
 server: 10.143.190.102:8091
 server: 10.143.190.103:8091
Group 2

The output confirms that the system created `Group 2` and left it empty.

### [](#assign-a-group-when-adding-a-server-with-the-cli)Assign a Group when Adding a Server, with the CLI

Added new nodes to a cluster by means of the `server-add` command. [Server-add](../../cli/couchbase-cli-server-add.md) provides full details. The command optionally takes a `--group-name` parameter. You can specify the name of an existing server group, and the system adds the new node to this group.

To add an _already provisioned_ node, enter the following. Specifying the administrator username and password of the new, provisioned node.

> [!NOTE]
> Adding a provisioned node removes all former provisioning, and reprovisions the node according to what's specified during addition. Also that if the node is **unprovisioned**, no username or password for the node is required.

See [Nodes](../../../../server/current/learn/clusters-and-availability/nodes.md), for more information.

/opt/enterprise-analytics/bin/couchbase-cli
--username Administrator \
--password password \
--server-add 10.143.190.104:8091 \
--server-add-username Administrator \
--server-add-password password \
--group-name 'Group 2' \

If successful, the command returns the following:

SUCCESS: Server added

The node-to-group assignment can now be checked again. This provides the following output:

Group 1
 server: 10.143.190.101:8091
 server: 10.143.190.102:8091
 server: 10.143.190.103:8091
Group 2
 server: 10.143.190.104:8091

This confirms that `10.143.190.104` has been added to `Group 2`. A rebalance should now be performed, to integrate the new node and distribute data appropriately across the cluster. See [Rebalance](../../cli/couchbase-cli-rebalance.md), for details.

### [](#move-a-server-between-groups-with-the-CLi)Move a Server Between Groups, with the CLI

To move a node to a different group, specify it's origin, the destination groups, and the node to be moved, as follows:

/opt/enterprise-analytics/bin/couchbase-cli
-u Administrator \
-p password \
--move-servers 10.143.190.104 \
--from-group 'Group 2' \
--to-group 'Group 1'

Success returns the following output:

SUCCESS: Servers moved between groups

The node-to-group assignment can now be checked again. This provides the following output:

Group 1
 server: 10.143.190.101:8091
 server: 10.143.190.102:8091
 server: 10.143.190.103:8091
 server: 10.143.190.104:8091
Group 2

This confirms that `10.143.190.104` has been moved into `Group 1`, and `Group 2` is empty.

### [](#delete-a-group-with-the-cli)Delete a Group, with the CLI

To delete an empty group, enter the following:

couchbase-cli group-manage -c 10.143.190.101:8091 \
-u Administrator \
-p password \
--delete \
--group-name 'Group 2'

If successful, the command returns the following:

SUCCESS: Server group deleted

The node-to-group assignment can now be checked again. This provides the following output:

Group 1
 server: 10.143.190.101:8091
 server: 10.143.190.102:8091
 server: 10.143.190.103:8091
 server: 10.143.190.104:8091

This confirms that `Group 2` has been deleted.

## [](#manage-groups-with-the-rest-api)Manage Groups with the REST API

The REST API can be used to gather information about existing groups, and to manage groups. The following subsections give examples of the methods and URI that can be used. All are described in greater detail in the section [Server Groups API](../../reference/rest-rza.md).

### [](#get-group-information-with-the-rest-api)Get Group Information, with the REST API

Group information can be retrieved with the `GET /pools/default/serverGroups` HTTP method and URI. The following example returns information about groups within the cluster `10.143.190.101`.

> [!NOTE]
> The output is piped to `jq`, to enhance readability.

curl -u Administrator:password -v -X GET \
http://10.143.190.101:8091/pools/default/serverGroups | jq

If successful, `200 OK` is given and an object is returned that contains information about each group. For the full output, and an explanation of the information provided, see [Getting Group Information](../../reference/rest-servergroup-get.md).

For general management purposes, the output contains the following, both of which are used in examples further:

* The _URI path and revision integer_ for the overall group-configuration. This must be specified when the configuration is to be changed.
* The group's _URI path and UUID string_. The allows the individual group to be referenced, when nodes are to be moved between groups, or are to be added.

### [](#add-a-group-with-the-rest-api)Add a Group, with the REST API

Server groups are created with the `POST /pools/default/serverGroups` HTTP method and URI. See [Creating Groups](../../reference/rest-servergroup-post-create.md) for full details.

The following example creates a new empty group on `10.143.190.101` named `Group 3`.

curl -X POST -u myAdmin:myPassword \
http://10.143.190.101:8091/pools/default/serverGroups \
-d 'name="Group 3"'

### [](#move-a-server-between-groups-with-the-rest-api)Move a Server Between Groups, with the REST API

Server group membership is changed by means of the `PUT /pools/default/serverGroups` HTTP method and URI. For full details, see [Updating Group Membership](../../reference/rest-servergroup-put-membership.md)

The following example specifies a new group-membership configuration:

curl -d@groupChangeDefinition.json -X PUT \
http://Administrator:password http://10.143.190.101:8091/pools/default/serverGroups?rev=112632175

The URI path is terminated with the _revision integer_ that specifies the current, overall group-configuration. This integer can be obtained by the procedure referred in [Get Group Information, with the REST API](#get-group-information-with-the-rest-api).

The specified file, `groupChangeDefinition.json`, provides the new configuration for group membership. For an example, see [Node-to-Group Assignment](../../reference/rest-servergroup-put-membership.md#configuration-statement).

> [!NOTE]
> The content of this file can also be directly specified on the command-line, if required.

Success gives `200 OK`, and returns an empty array.

### [](#delete-a-group-with-the-rest-api)Delete a Group, with the REST API

Server groups can be deleted with the `DELETE /pools/default/serverGroups/<:uuid>` HTTP method and URI. The group must be empty, for the request to succeed. For full details, see [Deleting Groups](../../reference/rest-servergroup-delete.md).

The procedure described in [Getting Server Group Information](../../reference/rest-servergroup-get.md) should be used to determine the `uuid` of the group to be deleted and to ascertain the group's emptiness. The following request deletes the group, which is specified by means of the `uuid`.

curl -X DELETE -u Administrator:password \
http://10.143.190.101:8091/pools/default/serverGroups/\
dfbed23035cc57eac0f4e72ce0c8667a

Success gives `200 OK`, and returns an empty object.

### [](#assign-a-group-when-adding-a-server-with-the-rest-api)Assign a Group when Adding a Server, with the REST API

A node can be added to the cluster and simultaneously added to an existing server group with the `POST /pools/default/serverGroups/<:uuid>/addNode` HTTP method and URI. Optionally, services can be added to the node. Following addition, rebalance is required. For full details, see [Adding Nodes to Groups](../../reference/rest-servergroup-post-add.md).

The following example assumes that the cluster has two groups, `Group 1` and `Group 2`. The `uuid` for `Group 2` has been returned as `246b5de857e100dbfd8b6dee0406420a`, by the procedure described in [Getting Server Group Information](../../reference/rest-servergroup-get.md). The following request therefore adds a new node, `10.143.190.104` to the cluster, and assigns it to `Group 2`. The Data and Index Services are deployed to the new node.

curl -X POST -d hostname=10.143.190.104:8091 \
-d services=kv%2Cindex \
-d user=Administrator -d password=password \
-u Administrator:password \
http://10.143.190.101:8091/pools/default/serverGroups/\
3b66b3c3177f44a3ffa6771ffeb31f36/addNode

Success gives `200 OK`, and returns an object signifying that the nodes specified for addition has been duly added to the cluster:

{"otpNode":"ns_1@10.143.190.104"}