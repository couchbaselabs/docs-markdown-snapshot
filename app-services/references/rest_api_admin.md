[View original HTML](/app-services/references/rest_api_admin.html)

* Introduction
* Session
  * getGet information about the current user
  * postCreate a new user session
  * getGet session information
  * delRemove session
  * delRemove all of a users sessions
  * delRemove session with user validation
* Database Security
  * getGet a user
  * putUpsert a user
  * delDelete a user
  * headCheck if user exists
  * getGet all names of the roles
  * postCreate a new role
  * getGet a role
  * putUpsert a role
  * delDelete a role
  * headCheck if role exists

[API docs by Redocly](https://redocly.com/redoc/)

# App Services Admin API (4.0)

Download OpenAPI specification:

License: [Business Source License 1.1 (BSL)](https://github.com/couchbase/sync%5Fgateway/blob/master/LICENSE) 

[⬆️ Manage App Services with the App Services API](rest-api-introduction.html)

## [](#section/Introduction)Introduction

App Services manages access and synchronization between Couchbase Lite and Couchbase Capella. The App Services Admin REST API is used to administer user accounts and roles, and to run administrative tasks in superuser mode.

## [](#tag/Session)Session

## [](#tag/Session/operation/get%5Fdb-%5Fsession)Get information about the current user 

This will get the information about the current user.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Properties associated with a user session

**404** 

Resource could not be found

get/{db}/\_session

Admin API

https://{hostname}:4985/{db}/\_session

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "authentication_handlers": [
  * "string"  
],
* "ok": true,
* "userCtx": {
  * "channels": { },
  * "name": "string"  
}
}`

## [](#tag/Session/operation/post%5Fdb-%5Fsession)Create a new user session 

Generates a login session for a user and returns the session ID and cookie name for that session. If no TTL is provided, then the default of 24 hours will be used.

A session cannot be generated for an non-existent user or the `GUEST` user.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

The body can depend on if using the Public or Admin APIs.

| name | string User name to generate the session for.                                                                                   |
| ---- | ------------------------------------------------------------------------------------------------------------------------------- |
| ttl  | integer Time until the session expires. Uses default value of 24 hours if left blank. This value must be greater or equal to 1. |

### Responses

**200** 

Session created successfully. Returned body is dependant on if using Public or Admin APIs.

**400** 

Origin is not in the approved list of allowed origins

**404** 

Resource could not be found

post/{db}/\_session

Admin API

https://{hostname}:4985/{db}/\_session

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "string",
* "ttl": 0
}`

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

`{
* "session_id": "c5af80a039db4ed9d2b6865576b6999935282689",
* "expires": "2022-01-21T15:24:44Z",
* "cookie_name": "SyncGatewaySession"
}`

## [](#tag/Session/operation/get%5Fdb-%5Fsession-sessionid)Get session information 

Retrieve session information such as the user the session belongs too and what channels that user can access.

##### path Parameters

| dbrequired        | string Example: db1The name of the database to run the operation against. |
| ----------------- | ------------------------------------------------------------------------- |
| sessionidrequired | string The ID of the session to target.                                   |

### Responses

**200** 

Properties associated with a user session

**404** 

Resource could not be found

get/{db}/\_session/{sessionid}

Admin API

https://{hostname}:4985/{db}/\_session/{sessionid}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "authentication_handlers": [
  * "string"  
],
* "ok": true,
* "userCtx": {
  * "channels": { },
  * "name": "string"  
}
}`

## [](#tag/Session/operation/delete%5Fdb-%5Fsession-sessionid)Remove session 

Invalidates the session provided so that anyone using it is logged out and is prevented from future use.

##### path Parameters

| dbrequired        | string Example: db1The name of the database to run the operation against. |
| ----------------- | ------------------------------------------------------------------------- |
| sessionidrequired | string The ID of the session to target.                                   |

### Responses

**200** 

Successfully removed the user session

**404** 

Resource could not be found

delete/{db}/\_session/{sessionid}

Admin API

https://{hostname}:4985/{db}/\_session/{sessionid}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Session/operation/delete%5Fdb-%5Fuser-name-%5Fsession)Remove all of a users sessions 

Invalidates all the sessions that a user has.

Will still return a `200` status code if the user has no sessions.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| namerequired | string The name of the user.                                              |

### Responses

**200** 

User now has no sessions

**404** 

Resource could not be found

delete/{db}/\_user/{name}/\_session

Admin API

https://{hostname}:4985/{db}/\_user/{name}/\_session

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Session/operation/delete%5Fdb-%5Fuser-name-%5Fsession-sessionid)Remove session with user validation 

Invalidates the session only if it belongs to the user.

##### path Parameters

| dbrequired        | string Example: db1The name of the database to run the operation against. |
| ----------------- | ------------------------------------------------------------------------- |
| namerequired      | string The name of the user.                                              |
| sessionidrequired | string The ID of the session to target.                                   |

### Responses

**200** 

Session has been successfully removed as the user was associated with the session

**404** 

Resource could not be found

delete/{db}/\_user/{name}/\_session/{sessionid}

Admin API

https://{hostname}:4985/{db}/\_user/{name}/\_session/{sessionid}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Security)Database Security

## [](#tag/Database-Security/operation/get%5Fdb-%5Fuser-name)Get a user 

Retrieve a single users information.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| namerequired | string The name of the user.                                              |

### Responses

**200** 

Properties associated with a user

**404** 

Resource could not be found

get/{db}/\_user/{name}

Admin API

https://{hostname}:4985/{db}/\_user/{name}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "string",
* "password": "string",
* "admin_channels": [
  * "string"  
],
* "all_channels": [
  * "string"  
],
* "email": "string",
* "disabled": false,
* "admin_roles": [
  * "string"  
],
* "roles": [
  * "string"  
],
* "jwt_roles": [
  * "string"  
],
* "jwt_channels": [
  * "string"  
],
* "jwt_issuer": "string",
* "jwt_last_updated": "2019-08-24T14:15:22Z",
* "collection_access": {
  * "scopename1": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ],
      * "all_channels": [
        * "string"  
            ],
      * "jwt_channels": [
        * "string"  
            ],
      * "jwt_last_updated": "2019-08-24T14:15:22Z"  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ],
      * "all_channels": [
        * "string"  
            ],
      * "jwt_channels": [
        * "string"  
            ],
      * "jwt_last_updated": "2019-08-24T14:15:22Z"  
      }  
  },
  * "scopename2": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ],
      * "all_channels": [
        * "string"  
            ],
      * "jwt_channels": [
        * "string"  
            ],
      * "jwt_last_updated": "2019-08-24T14:15:22Z"  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ],
      * "all_channels": [
        * "string"  
            ],
      * "jwt_channels": [
        * "string"  
            ],
      * "jwt_last_updated": "2019-08-24T14:15:22Z"  
      }  
  }  
}
}`

## [](#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)Upsert a user 

If the user does not exist, create a new user otherwise update the existing user.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| namerequired | string The name of the user.                                              |

##### Request Body schema: application/json

Properties associated with a user

| name               | string The name of the user. User names can only have alphanumeric ASCII characters and underscores.                                                      |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| password           | string The password of the user. Mandatory. unless allow\_empty\_password is true in the database configs.                                                |
| admin\_channels    | Array of strings A list of channels to explicitly grant to the user for the default collection. See collection\_access for channels in named collections. |
| email              | string The email address of the user.                                                                                                                     |
| disabled           | boolean Default: false If true, the user will not be able to login to the account as it is disabled.                                                      |
| admin\_roles       | Array of strings A list of roles to explicitly grant to the user.                                                                                         |
| collection\_access | object A set of access grants by scope and collection for a specific collection.                                                                          |

### Responses

**200** 

Existing user modified successfully

**201** 

New user created

**404** 

Resource could not be found

put/{db}/\_user/{name}

Admin API

https://{hostname}:4985/{db}/\_user/{name}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "string",
* "password": "string",
* "admin_channels": [
  * "string"  
],
* "email": "string",
* "disabled": false,
* "admin_roles": [
  * "string"  
],
* "collection_access": {
  * "scopename1": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ]  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ]  
      }  
  },
  * "scopename2": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ]  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ]  
      }  
  }  
}
}`

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Security/operation/delete%5Fdb-%5Fuser-name)Delete a user 

Delete a user from the database.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| namerequired | string The name of the user.                                              |

### Responses

**200** 

User deleted successfully

**404** 

Resource could not be found

delete/{db}/\_user/{name}

Admin API

https://{hostname}:4985/{db}/\_user/{name}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Security/operation/head%5Fdb-%5Fuser-name)Check if user exists 

Check if the user exists by checking the status code.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| namerequired | string The name of the user.                                              |

### Responses

**200** 

User exists

**404** 

Not Found

head/{db}/\_user/{name}

Admin API

https://{hostname}:4985/{db}/\_user/{name}

## [](#tag/Database-Security/operation/get%5Fdb-%5Frole-)Get all names of the roles 

Retrieves all the roles that are in the database.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| deleted | boolean Default: false Enum: true false Indicates that roles marked as deleted should be included in the result. |
| ------- | ---------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Roles retrieved successfully

**404** 

Resource could not be found

get/{db}/\_role/

Admin API

https://{hostname}:4985/{db}/\_role/

### Response samples 

* 200
* 404

Content type

application/json

Copy

`[
* "Administrator",
* "Moderator"
]`

## [](#tag/Database-Security/operation/post%5Fdb-%5Frole-)Create a new role 

Create a new role using the request body to specify the properties on the role.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

Properties associated with a role

| name               | string The name of the role. Role names can only have alphanumeric ASCII characters and underscores.                                                      |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| admin\_channels    | Array of strings A list of channels to explicitly grant to the role for the default collection. See collection\_access for channels in named collections. |
| collection\_access | object A set of access grants by scope and collection for a specific collection.                                                                          |

### Responses

**201** 

New role created successfully

**404** 

Resource could not be found

**409** 

Resource already exists under that name

post/{db}/\_role/

Admin API

https://{hostname}:4985/{db}/\_role/

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "string",
* "admin_channels": [
  * "string"  
],
* "collection_access": {
  * "scopename1": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ]  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ]  
      }  
  },
  * "scopename2": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ]  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ]  
      }  
  }  
}
}`

### Response samples 

* 404
* 409

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Security/operation/get%5Fdb-%5Frole-name)Get a role 

Retrieve a single roles properties.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| namerequired | string The name of the role.                                              |

### Responses

**200** 

Properties associated with a role

**404** 

Resource could not be found

get/{db}/\_role/{name}

Admin API

https://{hostname}:4985/{db}/\_role/{name}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "string",
* "admin_channels": [
  * "string"  
],
* "all_channels": [
  * "string"  
],
* "collection_access": {
  * "scopename1": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ],
      * "all_channels": [
        * "string"  
            ],
      * "jwt_channels": [
        * "string"  
            ],
      * "jwt_last_updated": "2019-08-24T14:15:22Z"  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ],
      * "all_channels": [
        * "string"  
            ],
      * "jwt_channels": [
        * "string"  
            ],
      * "jwt_last_updated": "2019-08-24T14:15:22Z"  
      }  
  },
  * "scopename2": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ],
      * "all_channels": [
        * "string"  
            ],
      * "jwt_channels": [
        * "string"  
            ],
      * "jwt_last_updated": "2019-08-24T14:15:22Z"  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ],
      * "all_channels": [
        * "string"  
            ],
      * "jwt_channels": [
        * "string"  
            ],
      * "jwt_last_updated": "2019-08-24T14:15:22Z"  
      }  
  }  
}
}`

## [](#tag/Database-Security/operation/put%5Fdb-%5Frole-name)Upsert a role 

If the role does not exist, create a new role otherwise update the existing role.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| namerequired | string The name of the role.                                              |

##### Request Body schema: application/json

Properties associated with a role

| name               | string The name of the role. Role names can only have alphanumeric ASCII characters and underscores.                                                      |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| admin\_channels    | Array of strings A list of channels to explicitly grant to the role for the default collection. See collection\_access for channels in named collections. |
| collection\_access | object A set of access grants by scope and collection for a specific collection.                                                                          |

### Responses

**200** 

OK

**201** 

Created

**404** 

Resource could not be found

put/{db}/\_role/{name}

Admin API

https://{hostname}:4985/{db}/\_role/{name}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "string",
* "admin_channels": [
  * "string"  
],
* "collection_access": {
  * "scopename1": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ]  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ]  
      }  
  },
  * "scopename2": {
    * "collectionname1": {
      * "admin_channels": [
        * "string"  
            ]  
      },
    * "collectionname2": {
      * "admin_channels": [
        * "string"  
            ]  
      }  
  }  
}
}`

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Security/operation/delete%5Fdb-%5Frole-name)Delete a role 

Delete a role from the database.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| namerequired | string The name of the role.                                              |

### Responses

**200** 

OK

**404** 

Resource could not be found

delete/{db}/\_role/{name}

Admin API

https://{hostname}:4985/{db}/\_role/{name}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Security/operation/head%5Fdb-%5Frole-name)Check if role exists 

Check if the role exists by checking the status code.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| namerequired | string The name of the role.                                              |

### Responses

**200** 

Role exists

**404** 

Resource could not be found

head/{db}/\_role/{name}

Admin API

https://{hostname}:4985/{db}/\_role/{name}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`