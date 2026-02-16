[View original HTML](/enterprise-analytics/current/reference/rest-servergroup-post-create.html)

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

See [Getting Server Group Information](rest-servergroup-get.md) for getting information about the current node-to-group configuration for the server. See [Updating Server Group Memberships](rest-servergroup-put-membership.md) for an example of changing the node-to-group configuration. See [Adding Servers to Server Groups](rest-servergroup-post-add.md), For information about adding nodes to groups.