---
title: Creating Groups
description: Server groups are created with the <code>POST
  /pools/default/serverGroups</code> HTTP method and URI.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-servergroup-post-create.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/rest-api/rest-servergroup-post-create.html)

# Creating Groups

> Server groups are created with the `POST /pools/default/serverGroups` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

POST /pools/default/serverGroups

## [](#description)Description

This creates a server group. A name for the group, unique across the server, must be specified. Names cannot be longer than 64 bytes.

## [](#curl-syntax)Curl Syntax

curl -X POST -u <administrator>:<password>
http://<host>:<port>/pools/default/serverGroups
-d name="<groupName>"

## [](#responses)Responses

Success gives `200 OK`, and returns an empty object. Specifying a name already assigned to an existing group gives `400 Bad Request`, and returns an object of the form `{"name": "already exists"}`. Failure to authenticate gives `401 Unauthorized`.

## [](#example)Example

The following request creates a new group on the cluster.

curl -X POST -u myAdmin:myPassword \
http://10.143.190.101:8091/pools/default/serverGroups \
-d 'name="Group 3"'

If successful, this duly creates a new, empty group; named `Group 3`.

## [](#see-also)See Also

See [Server Group Awareness](../learn/clusters-and-availability/groups.md), for a conceptual overview of groups. See [Getting Server Group Information](rest-servergroup-get.md) for getting information on the current node-to-group configuration for the server. See [Updating Server Group Memberships](rest-servergroup-put-membership.md) for an example of changing the node-to-group configuration. For examples of performing rebalance, see [Rebalancing Nodes](rest-cluster-rebalance.md). See [Adding Servers to Server Groups](rest-servergroup-post-add.md), for information on adding nodes to groups. See [Manage Groups](../manage/manage-groups/manage-groups.md), for examples of managing groups by means of Couchbase Web Console.