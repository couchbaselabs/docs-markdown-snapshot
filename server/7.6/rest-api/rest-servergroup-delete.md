---
title: Deleting Groups
description: Server groups can be deleted with the <code>DELETE
  /pools/default/serverGroups/<:uuid></code> HTTP method and URI.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-servergroup-delete.adoc
  xref: xref:7.6@server:rest-api:rest-servergroup-delete.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/rest-servergroup-delete.html)

# Deleting Groups

> Server groups can be deleted with the `DELETE /pools/default/serverGroups/<:uuid>` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

DELETE /pools/default/serverGroups/<:uuid>

This deletes a specified server group. The server group must be empty, for the request to succeed.

## [](#curl-syntax)Curl Syntax

curl -X DELETE -u <administrator>:<password>
  http://<host>:<port>/pools/default/serverGroups/<uuid>

As this indicates, the `uuid` of the group to be deleted must be appended to the URI. The `uuid` can be determined by means of the procedure explained in [Getting Server Group Information](rest-servergroup-get.md).

## [](#responses)Responses

Success gives `200 OK`, and returns an empty object. An incorrectly specified `uuid` gives `404 Object Not Found`, and returns an empty object. Specifying a name already assigned to an existing group gives `400 Bad Request`, and returns an object of the form `{"name": "already exists"}`. Attempting to delete a non-empty group gives `400 Bad Request`, and returns an object of the form `{"_":"group is not empty"}`. Failure to authenticate gives `401 Unauthorized`.

## [](#example)Example

The following example assumes that the procedure described in [Getting Server Group Information](rest-servergroup-get.md) has provided output containing the following:

{
  "name": "Group 2",
  "uri": "/pools/default/serverGroups/dfbed23035cc57eac0f4e72ce0c8667a",
  "addNodeURI": "/pools/default/serverGroups/dfbed23035cc57eac0f4e72ce0c8667a/addNode",
  "nodes": []
}

This indicates that the cluster contains a group named `Group 2`, whose `uuid` is `dfbed23035cc57eac0f4e72ce0c8667a`. The value of `node` is an empty array, indicating that there are no nodes assigned to the group: therefore, the group may be deleted.

Therefore, the following request deletes `Group 2`, by specifying `dfbed23035cc57eac0f4e72ce0c8667a`:

curl -X DELETE -u Administrator:password \
http://10.143.190.101:8091/pools/default/serverGroups/\
dfbed23035cc57eac0f4e72ce0c8667a

## [](#see-also)See Also

See [Getting Server Group Information](rest-servergroup-get.md) for getting information on the current node-to-group configuration for the server. See [Server Group Awareness](../learn/clusters-and-availability/groups.md), for a conceptual overview of groups. See [Updating Server Group Memberships](rest-servergroup-put-membership.md) for an example of changing the node-to-group configuration. See [Manage Groups](../manage/manage-groups/manage-groups.md), for examples of managing groups by means of Couchbase Web Console.