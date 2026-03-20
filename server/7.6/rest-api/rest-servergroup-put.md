---
title: Renaming Groups
description: Server groups can be renamed with the <code>PUT
  /pools/default/serverGroups/<:uuid></code> HTTP method and URI.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-servergroup-put.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:rest-api:rest-servergroup-put.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/rest-servergroup-put.html)

# Renaming Groups

> Server groups can be renamed with the `PUT /pools/default/serverGroups/<:uuid>` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

PUT /pools/default/serverGroups/<:uuid>

## [](#description)Description

This renames a server group. The new name must be unique, across the cluster. Names cannot be longer than 64 bytes.

## [](#curl-syntax)Curl Syntax

curl -X PUT -u <administrator>:<password>
http://<host>:<port>/pools/default/serverGroups/<uuid>
-d name=<newGroupName>

As this indicates, the `uuid` of the group to be renamed must be appended to the URI. The `uuid` can be determined by means of the procedure explained in [Getting Server Group Information](rest-servergroup-get.md). Note that the group’s `uuid` is itself _unchanged_ by the changing of the group’s name.

## [](#responses)Responses

Success gives `200 OK`, and returns and empty object. An incorrectly specified `uuid` gives `404 Object Not Found`, and returns an object of the form `["Could not find group with uuid: <submitted-uuid>"]`. Specifying a name already assigned to an existing group gives `400 Bad Request`, and returns an object of the form `{"name": "already exists"}`. Failure to authenticate gives `401 Unauthorized`.

## [](#example)Example

The following example assumes that the procedure described in [Getting Server Group Information](rest-servergroup-get.md) has provided output containing the following:

"name": "Group 2",
      "uri": "/pools/default/serverGroups/3b66b3c3177f44a3ffa6771ffeb31f36",

This indicates that the cluster contains a group named `Group 2`, whose `uuid` is `3b66b3c3177f44a3ffa6771ffeb31f36`.

Therefore, by specifying `3b66b3c3177f44a3ffa6771ffeb31f36`, the following request changes the name of `Group 2` to `Group X`:

curl -X PUT -u Administrator:password \
http://10.143.190.101:8091/pools/default/serverGroups/\
3b66b3c3177f44a3ffa6771ffeb31f36 \
-d 'name="Group X"'

## [](#see-also)See Also

See [Getting Server Group Information](rest-servergroup-get.md) for getting information on the current node-to-group configuration for the server. See [Server Group Awareness](../learn/clusters-and-availability/groups.md), for a conceptual overview of groups. See [Updating Server Group Memberships](rest-servergroup-put-membership.md) for an example of changing the node-to-group configuration. See [Manage Groups](../manage/manage-groups/manage-groups.md), for examples of managing groups by means of Couchbase Web Console.