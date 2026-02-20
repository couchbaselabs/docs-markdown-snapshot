---
title: Deleting Groups
description: Server groups can be deleted with the <code>DELETE
  /pools/default/serverGroups/<:uuid></code> HTTP method and URI.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-servergroup-delete.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:reference:rest-servergroup-delete.adoc[]
---

[View original HTML](/enterprise-analytics/current/reference/rest-servergroup-delete.html)

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

See [Getting Server Group Information](rest-servergroup-get.md) for getting information about the current node-to-group configuration for the server.