---
title: Sync Gateway Admin API Reference
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/rest-api/pages/rest_api_admin.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:sync-gateway:rest-api:rest_api_admin.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/rest-api/rest_api_admin.html)

# Sync Gateway Admin API Reference

* Introduction
* Authentication
  * getOpenID Connect authentication initiation via Location header redirect
  * getOpenID Connect authentication initiation via WWW-Authenticate header
  * getOpenID Connect authentication callback
  * getOpenID Connect token refresh
  * postCreate a new Facebook-based session
  * postCreate a new Google-based session
* Server
  * getGet server configuration
  * putSet runtime configuration
  * getGet the server status
  * getGet the status of the Sync Gateway Collect Info
  * postStart Sync Gateway Collect Info
  * delCancel the Sync Gateway Collect Info job
  * postRun the post upgrade process on all databases
  * getGet server information
  * headCheck if server online
  * getCheck if API is available
  * getGet console logging settings
  * putSet console logging settings
  * postUpdate console logging settings
* Database Management
  * getGet database information
  * delRemove a database
  * headCheck if database exists
  * putCreate a new Sync Gateway database
  * getGet a list of all the databases
  * getGet resync status
  * postStart or stop Resync
  * postStart asynchronous index initialization
  * getGet status of index initialization
  * postBring the database online
  * postTake the database offline
  * postManage a compact operation
  * getGet the status of the most recent compact operation
  * postManage a attachment migration operation
  * getGet the status of the most recent attachment migration operation
  * postEnsure Full Commit
* Database Configuration
  * getGet database configuration
  * putReplace database configuration
  * postUpdate database configuration
  * getGet database audit configuration
  * putReplace database audit configuration
  * postUpdate database audit configuration
  * getGet database sync function
  * putSet database sync function
  * delRemove custom sync function
  * getGet database import filter
  * putSet database import filter
  * delDelete import filter
* Database Security
  * getGet all the names of the users
  * postCreate a new user
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
* Session
  * getGet information about the current user
  * postCreate a new user session
  * getGet session information
  * delRemove session
  * delRemove all of a users sessions
  * delRemove session with user validation
* Document
  * getGet a document with the corresponding metadata
  * postPurge a document
  * postCreate a new document
  * getGet changes list
  * postGet changes list
  * postCompare revisions to what is in the database
  * getGet local document
  * putUpsert a local document
  * delDelete a local document
  * headCheck if local document exists
  * getGet a document
  * putUpsert a document
  * delDelete a document
  * headCheck if a document exists
  * getGet an attachment from a document
  * putCreate or update an attachment on a document
  * headCheck if attachment exists
  * delDelete an attachment on a document
  * getGets all the documents in the database with the given parameters
  * postGet all the documents in the database using a built-in view
  * postBulk document operations
  * postGet multiple documents in a MIME multipart response
* Replication
  * getGet all replication configurations
  * postUpsert a replication
  * getGet a replication configuration
  * putUpsert a replication
  * delStop and delete a replication
  * headCheck if a replication exists
  * getGet all replication statuses
  * getGet replication status
  * putControl a replication state
  * headCheck if replication exists
  * getHandle incoming BLIP Sync web socket request
* Metrics
  * getGet memory statistics
  * getGet all Sync Gateway statistics in JSON format
* Profiling
  * postCreate point-in-time profile
  * postStart or Stop continuous CPU profiling
  * postDump heap profile
  * getGet goroutine profile
  * postGet goroutine profile
  * getGet passed in command line parameters
  * postGet passed in command line parameters
  * getGet symbol pprof debug information
  * postGet symbol pprof debug information
  * getGet the heap pprof debug file
  * postGet the heap pprof debug file
  * getGet the profile pprof debug file
  * postGet the profile pprof debug file
  * getGet block profile
  * postGet block profile
  * getGet the threadcreate pprof debug file
  * postGet the threadcreate pprof debug file
  * getGet mutex profile
  * postGet mutex profile
  * getGet trace profile
  * postGet trace profile
  * getGet fgprof profile
  * postGet fgprof profile
* Unsupported
  * getRevision tree structure in Graphviz Dot format | Unsupported
  * postFlush the entire database bucket | Unsupported
  * getDump a view | Unsupported
  * getQuery a view on the default design document | Unsupported
  * getDump all the documents in a channel | Unsupported
  * postDisabled endpoint
  * getGet views of a design document | Unsupported
  * putUpdate views of a design document | Unsupported
  * delDelete a design document | Unsupported
  * headCheck if view of design document exists | Unsupported
  * getQuery a view on a design document | Unsupported
  * getOpenID Connect mock provider
  * getOpenID Connect mock login page
  * postOpenID Connect mock login page
  * postOpenID Connect mock token
  * getOpenID Connect public certificates for signing keys
  * getOpenID Connect mock login page handler
  * postOpenID Connect mock login page handler

[API docs by Redocly](https://redocly.com/redoc/)

# Sync Gateway Admin REST API (4.0)

Download OpenAPI specification:

License: [Business Source License 1.1 (BSL)](https://github.com/couchbase/sync%5Fgateway/blob/master/LICENSE) 

[⬆️ Admin REST API Overview](rest-api-admin.html)

## [](#section/Introduction)Introduction

The Sync Gateway Admin REST API is used to administer user accounts and roles, and to run administrative tasks in superuser mode.

## [](#tag/Authentication)Authentication

Manage authentication

## [](#tag/Authentication/operation/get%5Fdb-%5Foidc)OpenID Connect authentication initiation via Location header redirect 

Called by clients to initiate the OpenID Connect Authorization Code Flow. Redirects to the OpenID Connect provider if successful. 

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| provider | string The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used.                                               |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| offline  | string If true, the OpenID Connect provider is requested to confirm with the user the permissions requested and refresh the OIDC token. To do this, access\_type=offline and prompt=consent is set on the redirection link. |

### Responses

**302** 

Successfully connected with the OpenID Connect provider so now redirecting to the requested OIDC provider for authentication.

**400** 

The provider provided is not defined in the Sync Gateway config. If no provided was specified then there is no default provider set. 

**404** 

Resource could not be found

**500** 

Unable to connect and validate with the OpenID Connect provider requested

get/{db}/\_oidc

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Authentication/operation/get%5Fdb-%5Foidc%5Fchallenge)OpenID Connect authentication initiation via WWW-Authenticate header 

Called by clients to initiate the OpenID Connect Authorization Code Flow. This will establish a connection with the provider, then put the redirect URL in the `WWW-Authenticate` header.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| provider | string The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used.                                               |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| offline  | string If true, the OpenID Connect provider is requested to confirm with the user the permissions requested and refresh the OIDC token. To do this, access\_type=offline and prompt=consent is set on the redirection link. |

### Responses

**400** 

The provider provided is not defined in the Sync Gateway config. If no provided was specified then there is no default provider set. 

**401** 

Successfully connected with the OpenID Connect provider so now the client can login.

**404** 

Resource could not be found

**500** 

Unable to connect and validate with the OpenID Connect provider requested

get/{db}/\_oidc\_challenge

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_challenge

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Authentication/operation/get%5Fdb-%5Foidc%5Fcallback)OpenID Connect authentication callback 

The callback URL that the client is redirected to after authenticating with the OpenID Connect provider.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| error        | string The OpenID Connect error, if any occurred.                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| coderequired | string The OpenID Connect authentication code.                                                                                                                                                                                  |
| provider     | string The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used.                                                   |
| state        | string The OpenID Connect state to verify against the state cookie. This is used to prevent cross-site request forgery (CSRF). This is not required if disable\_callback\_state=true for the provider config (NOT recommended). |

### Responses

**200** 

Successfully authenticated with OpenID Connect.

**400** 

A problem occurred when reading the callback request body

**401** 

An error was received from the OpenID Connect provider. This means the error query parameter was filled.

**404** 

Resource could not be found

**500** 

A problem occurred in regards to the token

get/{db}/\_oidc\_callback

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_callback

### Response samples 

* 200
* 404
* 500

Content type

application/json

Copy

`{
* "id_token": "string",
* "refresh_token": "string",
* "session_id": "string",
* "name": "string",
* "access_token": "string",
* "token_type": "string",
* "expires_in": 0
}`

## [](#tag/Authentication/operation/get%5Fdb-%5Foidc%5Frefresh)OpenID Connect token refresh 

Refresh the OpenID Connect token based on the provided refresh token.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| refresh\_tokenrequired | string The OpenID Connect refresh token.                                                                                                                                      |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| provider               | string The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used. |

### Responses

**200** 

Successfully authenticated with OpenID Connect.

**400** 

The provider provided is not defined in the Sync Gateway config. If no provided was specified then there is no default provider set. 

**404** 

Resource could not be found

**500** 

Unable to connect and validate with the OpenID Connect provider requested

get/{db}/\_oidc\_refresh

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_refresh

### Response samples 

* 200
* 404

Content type

application/json

Copy

`{
* "id_token": "string",
* "refresh_token": "string",
* "session_id": "string",
* "name": "string",
* "access_token": "string",
* "token_type": "string",
* "expires_in": 0
}`

## [](#tag/Authentication/operation/post%5Fdb-%5Ffacebook)Create a new Facebook-based session  Deprecated 

Creates a new session based on a Facebook user. On a successful session creation, a session cookie is stored to keep the user authenticated for future API calls.

If `Origin` header is passed to this endpoint, the `Origin` header must match both the `cors.login_origin` and `cors.origin` configuration options.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

| access\_tokenrequired | string Facebook access token to base the new session on. |
| --------------------- | -------------------------------------------------------- |

### Responses

**200** 

Session created successfully

**400** 

Value of `Origin` is not in the approved list of allowed origins in `LoginOrigin` of Sync Gateway bootstrap or database configuration.

**401** 

Received error from Facebook verifier

**404** 

Resource could not be found

**502** 

Received invalid response from the Facebook verifier

**504** 

Unable to send request to Facebook API

post/{db}/\_facebook

Admin API

{protocol}://{hostname}:4985/{db}/\_facebook

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "access_token": "string"
}`

### Response samples 

* 400
* 401
* 404
* 502
* 504

Content type

application/json

Copy

`{
* "error": "Bad Request",
* "reason": "No CORS"
}`

## [](#tag/Authentication/operation/post%5Fdb-%5Fgoogle)Create a new Google-based session  Deprecated 

Creates a new session based on a Google user. On a successful session creation, a session cookie is stored to keep the user authenticated for future API calls.

If `Origin` header is passed to this endpoint, the `Origin` header must match both the `cors.login_origin` and `cors.origin` configuration options.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

| id\_tokenrequired | string Google ID token to base the new session on. |
| ----------------- | -------------------------------------------------- |

### Responses

**200** 

Session created successfully

**400** 

Value of `Origin` is not in the approved list of allowed origins in `LoginOrigin` of Sync Gateway bootstrap or database configuration.

**401** 

Received error from Google token verifier or invalid application ID in the config

**404** 

Resource could not be found

**502** 

Received invalid response from the Google token verifier

**504** 

Unable to send request to the Google token verifier

post/{db}/\_google

Admin API

{protocol}://{hostname}:4985/{db}/\_google

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "id_token": "string"
}`

### Response samples 

* 400
* 401
* 404
* 502

Content type

application/json

Copy

`{
* "error": "Bad Request",
* "reason": "No CORS"
}`

## [](#tag/Server)Server

Manage server activities

## [](#tag/Server/operation/get%5F%5Fconfig)Get server configuration 

This will return the configuration that the Sync Gateway node was initially started up with, or the currently config if `include_runtime` is set.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| redact           | boolean Deprecated Default: true No longer supported field.                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| include\_runtime | boolean Default: false Whether to include the values set after starting (at runtime), default values, and all loaded databases. |

### Responses

**200** 

Successfully returned server configuration

**400** 

There was a problem with your request

get/\_config

Admin API

{protocol}://{hostname}:4985/\_config

### Response samples 

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "api": {
  * "admin_interface": "127.0.0.1:4985",
  * "admin_interface_authentication": true,
  * "compress_responses": true,
  * "cors": {
    * "headers": [
      * "Accept-Encoding",
      * "Authorization",
      * "Content-Type",
      * "If-Match"  
      ],
    * "login_origin": [
      * "<https://example.com>"  
      ],
    * "max_age": 0,
    * "origin": [
      * "<https://example.com>"  
      ]  
  },
  * "enable_advanced_auth_dp": true,
  * "hide_product_version": true,
  * "https": {
    * "tls_cert_path": "string",
    * "tls_key_path": "string",
    * "tls_minimum_version": "tlsv1.2"  
  },
  * "idle_timeout": "90s",
  * "max_connections": 0,
  * "metrics_interface": "127.0.0.1:4986",
  * "metrics_interface_authentication": true,
  * "profile_interface": "string",
  * "public_interface": ":4984",
  * "read_header_timeout": "5s",
  * "server_read_timeout": "string",
  * "server_write_timeout": "string",
  * "pretty": true  
},
* "auth": {
  * "bcrypt_cost": 10  
},
* "bootstrap": {
  * "ca_cert_path": "string",
  * "config_update_frequency": "10s",
  * "group_id": "default",
  * "password": "string",
  * "server": "string",
  * "server_tls_skip_verify": false,
  * "use_tls_server": true,
  * "username": "string",
  * "x509_cert_path": "string",
  * "x509_key_path": "string"  
},
* "bucket_credentials": {
  * "bucketname1": {
    * "username": "string",
    * "password": "string",
    * "x509_cert_path": "string",
    * "x509_key_path": "string"  
  },
  * "bucketname2": {
    * "username": "string",
    * "password": "string",
    * "x509_cert_path": "string",
    * "x509_key_path": "string"  
  }  
},
* "database_credentials": {
  * "databasename1": {
    * "username": "string",
    * "password": "string",
    * "x509_cert_path": "string",
    * "x509_key_path": "string"  
  },
  * "databasename2": {
    * "username": "string",
    * "password": "string",
    * "x509_cert_path": "string",
    * "x509_key_path": "string"  
  }  
},
* "heap_profile_collection_threshold": 0,
* "heap_profile_disable_collection": false,
* "logging": {
  * "log_file_path": "string",
  * "redaction_level": "none",
  * "console": {
    * "log_level": "none",
    * "log_keys": [
      * [
        * "CRUD",
        * "HTTP",
        * "Query"  
            ]  
      ],
    * "color_enabled": false,
    * "file_output": "string",
    * "enabled": false,
    * "rotation": {
      * "max_size": 100,
      * "localtime": false,
      * "rotated_logs_size_limit": 1024,
      * "rotation_interval": "",
      * "max_age": 0  
      },
    * "collation_buffer_size": 10  
  },
  * "error": {
    * "enabled": true,
    * "rotation": {
      * "max_size": 100,
      * "localtime": false,
      * "rotated_logs_size_limit": 1024,
      * "rotation_interval": "",
      * "max_age": 360  
      },
    * "collation_buffer_size": 0  
  },
  * "warn": {
    * "enabled": true,
    * "rotation": {
      * "max_size": 100,
      * "localtime": false,
      * "rotated_logs_size_limit": 1024,
      * "rotation_interval": "",
      * "max_age": 180  
      },
    * "collation_buffer_size": 0  
  },
  * "info": {
    * "enabled": true,
    * "rotation": {
      * "max_size": 100,
      * "localtime": false,
      * "rotated_logs_size_limit": 1024,
      * "rotation_interval": "",
      * "max_age": 6  
      },
    * "collation_buffer_size": 0  
  },
  * "debug": {
    * "enabled": false,
    * "rotation": {
      * "max_size": 100,
      * "localtime": false,
      * "rotated_logs_size_limit": 1024,
      * "rotation_interval": "",
      * "max_age": 2  
      },
    * "collation_buffer_size": 1000  
  },
  * "trace": {
    * "enabled": false,
    * "rotation": {
      * "max_size": 100,
      * "localtime": false,
      * "rotated_logs_size_limit": 1024,
      * "rotation_interval": "",
      * "max_age": 2  
      },
    * "collation_buffer_size": 1000  
  },
  * "stats": {
    * "enabled": true,
    * "rotation": {
      * "max_size": 100,
      * "localtime": false,
      * "rotated_logs_size_limit": 1024,
      * "rotation_interval": "",
      * "max_age": 6  
      },
    * "collation_buffer_size": 0  
  },
  * "audit": {
    * "enabled": false,
    * "rotation": {
      * "max_size": 100,
      * "localtime": false,
      * "rotated_logs_size_limit": 1024,
      * "rotation_interval": "",
      * "max_age": 6  
      },
    * "audit_log_file_path": "string",
    * "enabled_events": [
      * 1234,
      * 5678  
      ]  
  }  
},
* "max_file_descriptors": 5000,
* "replicator": {
  * "blip_compression": 9,
  * "max_concurrent_changes_batches": 2,
  * "max_concurrent_replications": 0,
  * "max_concurrent_revs": 5,
  * "max_heartbeat": "string"  
},
* "unsupported": {
  * "allow_dbconfig_env_vars": true,
  * "diagnostic_interface": "",
  * "http2": {
    * "enabled": false  
  },
  * "serverless": {
    * "enabled": true,
    * "min_config_fetch_interval": "1s"  
  },
  * "stats_log_frequency": "1m",
  * "use_stdlib_json": false,
  * "use_xattr_config": false  
},
* "couchbase_keepalive_interval": 0
}`

## [](#tag/Server/operation/put%5F%5Fconfig)Set runtime configuration 

This endpoint is used to dynamically set runtime options, like logging without needing a restart.

These options are not persisted, and will not survive a restart of Sync Gateway.

The endpoint only accepts a limited number of options that can be changed at runtime. See request body schema for allowable options.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### Request Body schema: application/json

| logging                       | object                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| max\_concurrent\_replications | integer Default: 0 Maximum number of concurrent replication connections allowed. If set to 0 this limit will be ignored. |

### Responses

**200** 

Successfully set runtime options

**400** 

There was a problem with your request

put/\_config

Admin API

{protocol}://{hostname}:4985/\_config

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "logging": {
  * "console": {
    * "log_level": "none",
    * "log_keys": [
      * [
        * "CRUD",
        * "HTTP",
        * "Query"  
            ]  
      ]  
  },
  * "error": {
    * "enabled": true  
  },
  * "warn": {
    * "enabled": true  
  },
  * "info": {
    * "enabled": true  
  },
  * "debug": {
    * "enabled": false  
  },
  * "trace": {
    * "enabled": false  
  },
  * "stats": {
    * "enabled": true  
  },
  * "audit": {
    * "enabled": false  
  }  
},
* "max_concurrent_replications": 0
}`

### Response samples 

* 400

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Server/operation/get%5F%5Fstatus)Get the server status 

This will retrieve the status of each database and the overall server status.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

Returned the status successfully

**400** 

There was a problem with your request

get/\_status

Admin API

{protocol}://{hostname}:4985/\_status

### Response samples 

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "databases": {
  * "dbname1": {
    * "seq": 0,
    * "server_uuid": "string",
    * "require_resync": true,
    * "state": "Online",
    * "replication_status": [
      * {
        * "replication_id": "string",
        * "config": {
          * "adhoc": false,
          * "batch_size": 200,
          * "collections_enabled": false,
          * "collections_local": [
            * "scope1.collection1",
            * "scope1.collection3",
            * "scope1.collection6"  
                              ],
          * "collections_remote": [
            * "scope1.collectionA",
            * null,
            * "scope1.collectionF"  
                              ],
          * "conflict_resolution_type": "default",
          * "continuous": false,
          * "custom_conflict_resolver": "",
          * "direction": "push",
          * "enable_delta_sync": false,
          * "filter": "sync_gateway/bychannel",
          * "initial_state": "running",
          * "max_backoff_time": 5,
          * "purge_on_removal": false,
          * "query_params": [
            * "string"  
                              ],
          * "remote": "string",
          * "remote_password": "string",
          * "remote_username": "string",
          * "replication_id": "string",
          * "run_as": "string",
          * "password": "string",
          * "username": "string"  
                    },
        * "status": "running",
        * "error_message": "string",
        * "docs_read": 0,
        * "docs_checked_pull": 0,
        * "docs_purged": 0,
        * "rejected_by_local": 0,
        * "last_seq_pull": "string",
        * "deltas_recv": 0,
        * "deltas_requested": 0,
        * "docs_written": 0,
        * "docs_checked_push": 0,
        * "doc_write_failures": 0,
        * "doc_write_conflicts": 0,
        * "rejected_by_remote": 0,
        * "last_seq_push": "string",
        * "deltas_sent": 0  
            }  
      ],
    * "cluster": {
      * "cluster_uuid": "string",
      * "replication": {
        * "replication_id": {
          * "replication_id": "string",
          * "adhoc": false,
          * "batch_size": 200,
          * "collections_enabled": false,
          * "collections_local": [
            * "scope1.collection1",
            * "scope1.collection3",
            * "scope1.collection6"  
                              ],
          * "collections_remote": [
            * "scope1.collectionA",
            * null,
            * "scope1.collectionF"  
                              ],
          * "conflict_resolution_type": "default",
          * "continuous": false,
          * "custom_conflict_resolver": "",
          * "direction": "push",
          * "enable_delta_sync": false,
          * "filter": "sync_gateway/bychannel",
          * "initial_state": "running",
          * "max_backoff_time": 5,
          * "purge_on_removal": false,
          * "query_params": [
            * "string"  
                              ],
          * "remote": "string",
          * "remote_password": "string",
          * "remote_username": "string",
          * "run_as": "string",
          * "password": "string",
          * "username": "string",
          * "assigned_node": "string",
          * "target_state": "running",
          * "cluster_uuid": "string"  
                    }  
            },
      * "nodes": {
        * "node_uuid": {
          * "uuid": "string",
          * "host": "string"  
                    }  
            }  
      }  
  },
  * "dbname2": {
    * "seq": 0,
    * "server_uuid": "string",
    * "require_resync": true,
    * "state": "Online",
    * "replication_status": [
      * {
        * "replication_id": "string",
        * "config": {
          * "adhoc": false,
          * "batch_size": 200,
          * "collections_enabled": false,
          * "collections_local": [
            * "scope1.collection1",
            * "scope1.collection3",
            * "scope1.collection6"  
                              ],
          * "collections_remote": [
            * "scope1.collectionA",
            * null,
            * "scope1.collectionF"  
                              ],
          * "conflict_resolution_type": "default",
          * "continuous": false,
          * "custom_conflict_resolver": "",
          * "direction": "push",
          * "enable_delta_sync": false,
          * "filter": "sync_gateway/bychannel",
          * "initial_state": "running",
          * "max_backoff_time": 5,
          * "purge_on_removal": false,
          * "query_params": [
            * "string"  
                              ],
          * "remote": "string",
          * "remote_password": "string",
          * "remote_username": "string",
          * "replication_id": "string",
          * "run_as": "string",
          * "password": "string",
          * "username": "string"  
                    },
        * "status": "running",
        * "error_message": "string",
        * "docs_read": 0,
        * "docs_checked_pull": 0,
        * "docs_purged": 0,
        * "rejected_by_local": 0,
        * "last_seq_pull": "string",
        * "deltas_recv": 0,
        * "deltas_requested": 0,
        * "docs_written": 0,
        * "docs_checked_push": 0,
        * "doc_write_failures": 0,
        * "doc_write_conflicts": 0,
        * "rejected_by_remote": 0,
        * "last_seq_push": "string",
        * "deltas_sent": 0  
            }  
      ],
    * "cluster": {
      * "cluster_uuid": "string",
      * "replication": {
        * "replication_id": {
          * "replication_id": "string",
          * "adhoc": false,
          * "batch_size": 200,
          * "collections_enabled": false,
          * "collections_local": [
            * "scope1.collection1",
            * "scope1.collection3",
            * "scope1.collection6"  
                              ],
          * "collections_remote": [
            * "scope1.collectionA",
            * null,
            * "scope1.collectionF"  
                              ],
          * "conflict_resolution_type": "default",
          * "continuous": false,
          * "custom_conflict_resolver": "",
          * "direction": "push",
          * "enable_delta_sync": false,
          * "filter": "sync_gateway/bychannel",
          * "initial_state": "running",
          * "max_backoff_time": 5,
          * "purge_on_removal": false,
          * "query_params": [
            * "string"  
                              ],
          * "remote": "string",
          * "remote_password": "string",
          * "remote_username": "string",
          * "run_as": "string",
          * "password": "string",
          * "username": "string",
          * "assigned_node": "string",
          * "target_state": "running",
          * "cluster_uuid": "string"  
                    }  
            },
      * "nodes": {
        * "node_uuid": {
          * "uuid": "string",
          * "host": "string"  
                    }  
            }  
      }  
  }  
},
* "version": "string",
* "vendor": {
  * "name": "Couchbase Sync Gateway",
  * "version": 3.1  
}
}`

## [](#tag/Server/operation/get%5F%5Fsgcollect%5Finfo)Get the status of the Sync Gateway Collect Info 

This will return the status of whether Sync Gateway Collect Info (sgcollect\_info) is currently running or not.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

Returned sgcollect\_info status

get/\_sgcollect\_info

Admin API

{protocol}://{hostname}:4985/\_sgcollect\_info

### Response samples 

* 200

Content type

application/json

Copy

`{
* "status": "stopped"
}`

## [](#tag/Server/operation/post%5F%5Fsgcollect%5Finfo)Start Sync Gateway Collect Info 

This endpoint is used to start a Sync Gateway Collect Info (sgcollect\_info) job so that Sync Gateway diagnostic data can be outputted to a file.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### Request Body schema: application/json

sgcollect\_info options

| redact\_level | string Default: "partial" Enum: "partial" "none" The redaction level to use for redacting the collected logs.                                                                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| redact\_salt  | string The salt to use for the log redactions.                                                                                                                                                                                                                       |
| output\_dir   | string Default: "The configured path set in the startup config \`logging.log\_file\_path\`" The directory to output the collected logs zip file at. This overrides the configured default output directory configured in the startup config logging.log\_file\_path. |
| upload        | boolean If set, upload the logs to Couchbase Support. A customer name must be set if this is set.                                                                                                                                                                    |
| upload\_host  | string Default: "https://uploads.couchbase.com" The host to send the logs too.                                                                                                                                                                                       |
| upload\_proxy | string The proxy to use while uploading the logs.                                                                                                                                                                                                                    |
| customer      | string The customer name to use when uploading the logs.                                                                                                                                                                                                             |
| ticket        | string \[ 1 .. 7 \] characters The Zendesk ticket number to use when uploading logs.                                                                                                                                                                                 |

### Responses

**200** 

Successfully started sgcollect\_info

**400** 

There was a problem with your request

**500** 

An error occurred while trying to run sgcollect\_info

post/\_sgcollect\_info

Admin API

{protocol}://{hostname}:4985/\_sgcollect\_info

### Request samples 

* Payload

Content type

application/json

Copy

`` {
* "redact_level": "partial",
* "redact_salt": "string",
* "output_dir": "The configured path set in the startup config `logging.log_file_path`",
* "upload": true,
* "upload_host": "<https://uploads.couchbase.com>",
* "upload_proxy": "string",
* "customer": "string",
* "ticket": "string"
} ``

### Response samples 

* 200
* 400
* 500

Content type

application/json

Copy

`{
* "status": "started"
}`

## [](#tag/Server/operation/delete%5F%5Fsgcollect%5Finfo)Cancel the Sync Gateway Collect Info job 

This endpoint is used to cancel a current Sync Gateway Collect Info (sgcollect\_info) job that is running.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

Job cancelled successfully

**400** 

There was a problem with your request

delete/\_sgcollect\_info

Admin API

{protocol}://{hostname}:4985/\_sgcollect\_info

### Response samples 

* 200
* 400

Content type

application/json

Copy

`{
* "status": "cancelled"
}`

## [](#tag/Server/operation/post%5F%5Fpost%5Fupgrade)Run the post upgrade process on all databases 

The post upgrade process involves removing obsolete design documents and indexes when they are no longer needed.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| preview | boolean Default: false If set, a dry-run will be done to return what would be removed. |
| ------- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

Returned results

post/\_post\_upgrade

Admin API

{protocol}://{hostname}:4985/\_post\_upgrade

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`` {
* "post_upgrade_results": {
  * "db1": {
    * "removed_design_docs": [
      * "string"  
      ],
    * "removed_indexes": [
      * "`_default`.`_default`.syncDocs_x1`",
      * "`scope`.`collection1`.sg_allDocs_1"  
      ]  
  },
  * "db2": {
    * "removed_design_docs": [
      * "string"  
      ],
    * "removed_indexes": [
      * "`_default`.`_default`.syncDocs_x1`",
      * "`scope`.`collection1`.sg_allDocs_1"  
      ]  
  }  
},
* "preview": true
} ``

## [](#tag/Server/operation/get%5F-)Get server information 

Returns information about the Sync Gateway node.

### Responses

**200** 

Returned server information

get/

Admin API

{protocol}://{hostname}:4985/

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "ADMIN": true,
* "couchdb": "Welcome",
* "vendor": {
  * "name": "Couchbase Sync Gateway",
  * "version": 3.1  
},
* "version": "Couchbase Sync Gateway/3.1.0(1;a765231) EE",
* "persistent_config": true
}`

## [](#tag/Server/operation/head%5F-)Check if server online 

Check if the server is online by checking the status code of response.

### Responses

**200** 

Server is online

head/

Admin API

{protocol}://{hostname}:4985/

## [](#tag/Server/operation/get%5F%5Fping)Check if API is available 

Returns OK status if API is available.

### Responses

**200** 

Returned status

get/\_ping

Admin API

{protocol}://{hostname}:4985/\_ping

### Response samples 

* 200

Content type

text/plain

Copy

OK

## [](#tag/Server/operation/get%5F%5Flogging)Get console logging settings  Deprecated 

**Deprecated in favour of `GET /_config`**This will return a map of the log keys being used for the console logging.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

Returned map of console log keys

get/\_logging

Admin API

{protocol}://{hostname}:4985/\_logging

### Response samples 

* 200

Content type

application/json

Copy

`{
* "HTTP": true,
* "CRUD": false,
* "Changes": true
}`

## [](#tag/Server/operation/put%5F%5Flogging)Set console logging settings  Deprecated 

**Deprecated in favour of `PUT /_config`**Enable or disable console log keys and optionally change the console log level.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| logLevel | string Enum: "none" "error" "warn" "info" "debug" "trace" The is what to set the console log level too.                                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| level    | integer \[ 1 .. 3 \] Deprecated **Deprecated: use log level instead.** This sets the console log level depending on the value provide. 1 sets to info, 2 sets to warn, and 3 sets to error.' |

##### Request Body schema: application/json

The map of log keys to use for console logging.

| property name\*additional property | boolean The log key and whether it is enabled or not. |
| ---------------------------------- | ----------------------------------------------------- |

### Responses

**200** 

Log keys successfully replaced.

**400** 

There was a problem with your request

put/\_logging

Admin API

{protocol}://{hostname}:4985/\_logging

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "HTTP": true,
* "CRUD": false,
* "Changes": true
}`

### Response samples 

* 400

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Server/operation/post%5F%5Flogging)Update console logging settings  Deprecated 

**Deprecated in favour of `PUT /_config`**This is for enabling the log keys provided and optionally changing the console log level.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| logLevel | string Enum: "none" "error" "warn" "info" "debug" "trace" The is what to set the console log level too.                                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| level    | integer \[ 1 .. 3 \] Deprecated **Deprecated: use log level instead.** This sets the console log level depending on the value provide. 1 sets to info, 2 sets to warn, and 3 sets to error.' |

##### Request Body schema: application/json

The console log keys to upsert.

| property name\*additional property | boolean The log key and whether it is enabled or not. |
| ---------------------------------- | ----------------------------------------------------- |

### Responses

**200** 

Log keys successfully updated.

**400** 

There was a problem with your request

post/\_logging

Admin API

{protocol}://{hostname}:4985/\_logging

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "HTTP": true,
* "CRUD": false,
* "Changes": true
}`

### Response samples 

* 400

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Management)Database Management

Create and manage Sync Gateway databases

## [](#tag/Database-Management/operation/get%5Fdb-)Get database information 

Retrieve information about the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Successfully returned database information

**404** 

Resource could not be found

get/{db}/

Admin API

{protocol}://{hostname}:4985/{db}/

### Response samples 

* 200
* 404

Content type

application/json

Copy

`{
* "db_name": "db",
* "update_seq": 123456,
* "committed_update_seq": 123456,
* "instance_start_time": 1644600082279583,
* "compact_running": true,
* "purge_seq": 0,
* "disk_format_version": 0,
* "state": "Online",
* "server_uuid": "995618a6a6cc9ac79731bd13240e19b5",
* "require_resync": true,
* "init_in_progress": true
}`

## [](#tag/Database-Management/operation/delete%5Fdb-)Remove a database 

Removes a database from the Sync Gateway cluster

**Note:** If running in legacy mode, this will only delete the database from the current node.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Successfully removed the database

**404** 

Resource could not be found

**500** 

Cannot remove database from bucket

delete/{db}/

Admin API

{protocol}://{hostname}:4985/{db}/

### Response samples 

* 200
* 404
* 500

Content type

application/json

Copy

`{ }`

## [](#tag/Database-Management/operation/head%5Fdb-)Check if database exists 

Check if a database exists by using the response status code.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Database exists

**404** 

Resource could not be found

head/{db}/

Admin API

{protocol}://{hostname}:4985/{db}/

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Management/operation/put%5Fdb-)Create a new Sync Gateway database 

This is to create a new database for Sync Gateway.

The new database name will be the name specified in the URL, not what is specified in the request body database configuration.

If the bucket is not provided in the database configuration, Sync Gateway will attempt to find and use the database name as the bucket.

By default, the new database will be brought online immediately. This can be avoided by including `"offline": true` in the configuration in the request body.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| disable\_oidc\_validation | boolean Default: false If set, will not attempt to validate the configured OpenID Connect providers are reachable. |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

The configuration to use for the new database

| allow\_empty\_password                  | boolean Default: false This controls whether users that are created can have an empty password or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket                                  | string Default: "The database name" The Couchbase Server backing bucket for the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| bucket\_op\_timeout\_ms                 | number This is the amount of milliseconds should pass before a bucket operation times out. An error will be returned if the bucket operation times out saying: operation timed out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| cacertpath                              | string The root CA cert path for X.509 bucket authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| cache                                   | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| certpath                                | string The cert path (public key) for X.509 bucket auth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| changes\_request\_plus                  | boolean Default: false Sets the default value of request\_plus for one-shot/non-continuous changes feeds, which when true, ensures all valid documents written prior to the request being issued are included in the response. Setting this option at the database level is required to ensure Couchbase Lite utilizes this changes feed mode. This also sets the default value of query param request\_plus for [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or request\_plus for [POST /{keyspace}/\_changes](#operation/post%5Fkeyspace-%5Fchanges).                                                                                                                                |
| client\_partition\_window\_secs         | integer Default: 2592000 How long (in seconds) clients can remain offline for without losing replication metadata. Defaults to 30 days (in seconds)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| compact\_interval\_days                 | number Default: 1 The interval between scheduled tombstone compaction runs (in days). This can be a floating point number. If set to 0, compaction will not run automatically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| cors                                    | object (Cors Configuration) CORS configuration for this database; if present, overrides server's config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| delta\_sync                             | object Delta sync configuration settings. **This is an Enterprise Edition feature only**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| disable\_password\_auth                 | boolean Default: false Whether to disable username/password authentication and only allow OIDC and guest access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| disable\_public\_all\_docs              | boolean Default: false This controls whether the [GET /{keyspace}/\_all\_docs](#operation/get%5Fkeyspace-%5Fall%5Fdocs) REST API endpoint is publicly accessible or not. Disabling this endpoint is recommended for larger datasets or production workloads. [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or [POST /{keyspace}/\_bulk\_get](#operation/post%5Fkeyspace-%5Fbulk%5Fget) have more efficient implementations and should be used instead. If set to true, the endpoint will not be publicly accessible, and will only be available on the Admin API. Setting this to false, or leaving it as the default value is deprecated, and may default to true in a future release. |
| event\_handlers                         | object These are the settings for webhooks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| guest                                   | object (User) Properties associated with a user                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| import\_backup\_old\_rev                | boolean Default: false This controls whether import should attempt to create a temporary backup of the previous revision body (if available) when the document is modified in the bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| import\_docs                            | boolean If true, documents will be imported in to Sync Gateway from the bucket in the background. Documents will be ran through the set import\_filter if any is set. The default value depends on the edition of Sync Gateway being used. If the edition is the Community Edition, then this will default to false or else in the Enterprise Edition, it will default to true. This value requires enable\_shared\_bucket\_access=true. This can also be set to the string continuous which maps to true.                                                                                                                                                                                                  |
| import\_filter                          | string This is the function that all imported documents in the default scope and collection are ran through in order to filter out what to import and what not to import. This allows you to control what is made available to Couchbase Mobile clients. If it is not set, then no documents are filtered when imported. import\_docs must be true to make this field applicable. If scopes parameter is set, this is ignored.                                                                                                                                                                                                                                                                              |
| import\_partitions                      | number \[ 1 .. 1024 \] Default: 16 \*\* This is an Enterprise Edition feature only\*\* This is how many import partitions should be used for import sharding. Partitions are distributed among all Sync Gateway nodes participating in import processing (import\_docs=true), and each process a subset of the server's vbuckets. Each partition is processed by an independent function that runs simultaneously to others, so import\_partitions can be used to tune concurrency based on the number of Sync Gateway nodes, and the number of cores per node.                                                                                                                                             |
| index                                   | object Global Secondary Index Settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| javascript\_timeout\_secs               | number Default: 60 The maximum number of seconds the sync, import filter, and custom conflict resolver JavaScript functions are allowed to run for before timing out. Set to 0 to allow the JS functions to run uncapped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| keypath                                 | string The key path (private key) for X.509 bucket auth                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| kv\_tls\_port                           | integer Default: 11207 The Memcached TLS port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| local\_doc\_expiry\_secs                | integer Default: 7776000 The number of seconds before a \_local document should expire.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| local\_jwt                              | object Configuration for Local JWT authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| logging                                 | object Per-database logging configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| max\_concurrent\_query\_ops             | integer Default: 1000 The maximum amount of query operations that can be running at any one point.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| name                                    | string The name of the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| offline                                 | boolean Default: false Start the database in an offline state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| oidc                                    | object Configuration for OpenID Connect authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| old\_rev\_expiry\_seconds               | number Default: 300 The number of seconds before old revisions are removed from the Couchbase Server bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| password                                | string The password for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| query\_pagination\_limit                | integer Default: 5000 The query limit to be used during pagination of large queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| replications                            | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| revs\_limit                             | number \>= 0 Default: 50 The maximum depth a document's revision tree can grow to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| roles                                   | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scopes                                  | object <= 1 properties An object keyed by scope name containing config for the specific collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| send\_www\_authenticate\_header         | boolean Default: true Controls whether to send a WWW-Authenticate header in 401 Unauthorized HTTP responses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| serve\_insecure\_attachment\_types      | boolean Default: false If set, always serve attachments with the Content-Type header set to the type of the attachment. When serving an attachment, usually the Content-Type header is set to the type of the attachment but the Content-Disposition response header will be set instead if the content type is vulnerable to a phishing attack, causing the browser to download the file instead of display it. This option will override that behaviour and always set the Content-Type header.                                                                                                                                                                                                           |
| server                                  | string This is the Couchbase Server address or addresses that the database connect to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| session\_cookie\_http\_only             | boolean Default: false Make all session cookies for the database set the HttpOnly flag so they are inaccessible to JavaScript.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| session\_cookie\_name                   | string This can be used to define a custom per-database session cookie name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| session\_cookie\_secure                 | boolean Override the session cookie secure flag. If set, the cookie will have the secure flag. This will default to true if startup config api.https.tls\_cert\_path is set otherwise it will default to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| sgreplicate\_enabled                    | boolean Default: true Whether the node should accept assign replications (true) or not (false).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| sgreplicate\_websocket\_heartbeat\_secs | integer Default: 300 Use a custom heartbeat interval (in seconds) for websocket ping frames.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| slow\_query\_warning\_threshold         | number Default: 500 The amount of milliseconds a N1QL query should run before logging a warning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| store\_legacy\_revtree\_data            | boolean Default: true Controls whether Sync Gateway stores additional legacy revision tree pointer data to support 3.x/early 4.x clients that still use RevTree IDs (for example when used as delta sources). Disable this when you are confident all clients use newer CV-based revisions and no longer require legacy RevTree ID lookups.                                                                                                                                                                                                                                                                                                                                                                 |
| suspendable                             | boolean Default: false Set to true to allow the database to be suspended. Defaults to true when running in serverless mode otherwise defaults to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| sync                                    | string Default: "function(doc){channel(doc.channels);}" The Javascript function that newly created documents are ran through for the default scope and collection. If scopes parameter is set, this is ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| unsupported                             | object These are unsupported options and therefore it is not recommended to use them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| use\_views                              | boolean Default: false Force the use of views instead of GSI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| user\_xattr\_key                        | string <= 15 The key to use for the user xattr that will be accessible from the sync function. If empty, the feature will be disabled. This is an Enterprise Edition feature only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| username                                | string The username for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| users                                   | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| view\_query\_timeout\_secs              | integer Default: 75 The number of seconds before a view query should timeout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| allow\_conflicts                        | boolean Deprecated Default: false Since Sync Gateway 4.0, this option has no effect. If this option is set to true on an existing database, the database must be modified to remove this parameter in order allow the database to come online. Otherwise, the database will be in the offline state.                                                                                                                                                                                                                                                                                                                                                                                                        |
| enable\_shared\_bucket\_access          | boolean Deprecated Default: true Since Sync Gateway 4.0, this option has no effect. If this option is set to true on an existing database, the database must be modified to remove this parameter in order allow the database to come online. Otherwise, the database will be in the offline state.                                                                                                                                                                                                                                                                                                                                                                                                         |
| feed\_type                              | string Deprecated Default: "DCP" Value: "DCP" The type of feed to use to communicate with Couchbase Server. This will use DCP regardless of specification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| num\_index\_replicas                    | number Deprecated Default: 1 **Deprecated, please use the database setting index.num\_replicas instead**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| pool                                    | string Deprecated Default: "default" This field is unsupported and ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| rev\_cache\_size                        | number Deprecated **Deprecated, please use the database setting cache.rev\_cache.size instead** The maximum number of revisions to store in the revision cache.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Responses

**201** 

Database created successfully

**400** 

There was a problem with your request

**403** 

An authentication failure occurred

**409** 

A database already exists for this bucket

**412** 

A database under that name already exists

**500** 

A server error occurred

put/{db}/

Admin API

{protocol}://{hostname}:4985/{db}/

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "allow_empty_password": false,
* "bucket": "The database name",
* "bucket_op_timeout_ms": 0,
* "cacertpath": "string",
* "cache": {
  * "channel_cache": {
    * "compact_high_watermark_pct": 80,
    * "compact_low_watermark_pct": 60,
    * "expiry_seconds": 60,
    * "max_length": 500,
    * "max_num_pending": 10000,
    * "max_number": 50000,
    * "max_wait_pending": 5000,
    * "max_wait_skipped": 3600000,
    * "min_length": 50,
    * "enable_star_channel": true,
    * "query_limit": 5000  
  },
  * "rev_cache": {
    * "max_memory_count_mb": 0,
    * "shard_count": 16,
    * "size": 5000  
  },
  * "channel_cache_expiry": 0,
  * "channel_cache_max_length": 0,
  * "channel_cache_min_length": 0,
  * "enable_star_channel": true,
  * "max_num_pending": 0,
  * "max_wait_pending": 0,
  * "max_wait_skipped": 0  
},
* "certpath": "string",
* "changes_request_plus": false,
* "client_partition_window_secs": 2592000,
* "compact_interval_days": 1,
* "cors": {
  * "headers": [
    * "Accept-Encoding",
    * "Authorization",
    * "Content-Type",
    * "If-Match"  
  ],
  * "login_origin": [
    * "<https://example.com>"  
  ],
  * "max_age": 0,
  * "origin": [
    * "<https://example.com>"  
  ]  
},
* "delta_sync": {
  * "enabled": false,
  * "rev_max_age_seconds": 86400  
},
* "disable_password_auth": false,
* "disable_public_all_docs": false,
* "event_handlers": {
  * "db_state_changed": {
    * "handler": "webhook",
    * "url": "string",
    * "filter": "string",
    * "timeout": 0  
  },
  * "document_changed": {
    * "handler": "webhook",
    * "url": "string",
    * "filter": "string",
    * "timeout": 0,
    * "options": {
      * "winning_rev_only": false  
      }  
  },
  * "max_processes": "string",
  * "wait_for_process": "string"  
},
* "guest": {
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
},
* "import_backup_old_rev": false,
* "import_docs": true,
* "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }",
* "import_partitions": 16,
* "index": {
  * "num_partitions": 1,
  * "num_replicas": 1  
},
* "javascript_timeout_secs": 60,
* "keypath": "string",
* "kv_tls_port": 11207,
* "local_doc_expiry_secs": 7776000,
* "local_jwt": {
  * "providername1": {
    * "algorithms": [
      * "string"  
      ],
    * "channels_claim": "string",
    * "client_id": "string",
    * "disable_session": true,
    * "issuer": "string",
    * "keys": [
      * {
        * "alg": "string",
        * "crv": "P-256",
        * "e": "string",
        * "kid": "string",
        * "kty": "RSA",
        * "n": "string",
        * "use": "sig",
        * "x": "string",
        * "y": "string"  
            }  
      ],
    * "register": true,
    * "roles_claim": "string",
    * "user_prefix": "string",
    * "username_claim": "string"  
  },
  * "providername2": {
    * "algorithms": [
      * "string"  
      ],
    * "channels_claim": "string",
    * "client_id": "string",
    * "disable_session": true,
    * "issuer": "string",
    * "keys": [
      * {
        * "alg": "string",
        * "crv": "P-256",
        * "e": "string",
        * "kid": "string",
        * "kty": "RSA",
        * "n": "string",
        * "use": "sig",
        * "x": "string",
        * "y": "string"  
            }  
      ],
    * "register": true,
    * "roles_claim": "string",
    * "user_prefix": "string",
    * "username_claim": "string"  
  }  
},
* "logging": {
  * "audit": {
    * "disabled_roles": [
      * {
        * "domain": "cbs",
        * "name": "string"  
            }  
      ],
    * "disabled_users": [
      * {
        * "domain": "cbs",
        * "name": "string"  
            }  
      ],
    * "enabled": false,
    * "enabled_events": [
      * [
        * 1234,
        * 5678  
            ]  
      ]  
  },
  * "console": {
    * "log_keys": [
      * "CRUD",
      * "HTTP",
      * "Query"  
      ],
    * "log_level": "debug"  
  }  
},
* "max_concurrent_query_ops": 1000,
* "name": "string",
* "offline": false,
* "oidc": {
  * "default_provider": "string",
  * "providers": {
    * "providername1": {
      * "InsecureSkipVerify": false,
      * "IsDefault": true,
      * "Name": "string",
      * "allow_unsigned_provider_tokens": true,
      * "callback_url": "string",
      * "channels_claim": "string",
      * "client_id": "string",
      * "disable_callback_state": false,
      * "disable_cfg_validation": false,
      * "disable_session": true,
      * "discovery_url": "string",
      * "include_access": true,
      * "issuer": "string",
      * "register": true,
      * "roles_claim": "string",
      * "scope": [
        * "string"  
            ],
      * "user_prefix": "string",
      * "username_claim": "string",
      * "validation_key": "string"  
      },
    * "providername2": {
      * "InsecureSkipVerify": false,
      * "IsDefault": true,
      * "Name": "string",
      * "allow_unsigned_provider_tokens": true,
      * "callback_url": "string",
      * "channels_claim": "string",
      * "client_id": "string",
      * "disable_callback_state": false,
      * "disable_cfg_validation": false,
      * "disable_session": true,
      * "discovery_url": "string",
      * "include_access": true,
      * "issuer": "string",
      * "register": true,
      * "roles_claim": "string",
      * "scope": [
        * "string"  
            ],
      * "user_prefix": "string",
      * "username_claim": "string",
      * "validation_key": "string"  
      }  
  }  
},
* "old_rev_expiry_seconds": 300,
* "password": "string",
* "query_pagination_limit": 5000,
* "replications": {
  * "replication_id": {
    * "adhoc": false,
    * "batch_size": 200,
    * "collections_enabled": false,
    * "collections_local": [
      * "scope1.collection1",
      * "scope1.collection3",
      * "scope1.collection6"  
      ],
    * "collections_remote": [
      * "scope1.collectionA",
      * null,
      * "scope1.collectionF"  
      ],
    * "conflict_resolution_type": "default",
    * "continuous": false,
    * "custom_conflict_resolver": "",
    * "direction": "push",
    * "enable_delta_sync": false,
    * "filter": "sync_gateway/bychannel",
    * "initial_state": "running",
    * "max_backoff_time": 5,
    * "purge_on_removal": false,
    * "query_params": [
      * "string"  
      ],
    * "remote": "string",
    * "remote_password": "string",
    * "remote_username": "string",
    * "replication_id": "string",
    * "run_as": "string",
    * "password": "string",
    * "username": "string"  
  }  
},
* "revs_limit": 50,
* "roles": {
  * "rolename1": {
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
  },
  * "rolename2": {
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
  }  
},
* "scopes": {
  * "scopename": {
    * "collections": {
      * "collectionname1": {
        * "sync": "function(doc){channel(\"collection name\");}",
        * "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            },
      * "collectionname2": {
        * "sync": "function(doc){channel(\"collection name\");}",
        * "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            }  
      }  
  }  
},
* "send_www_authenticate_header": true,
* "serve_insecure_attachment_types": false,
* "server": "string",
* "session_cookie_http_only": false,
* "session_cookie_name": "string",
* "session_cookie_secure": true,
* "sgreplicate_enabled": true,
* "sgreplicate_websocket_heartbeat_secs": 300,
* "slow_query_warning_threshold": 500,
* "store_legacy_revtree_data": true,
* "suspendable": false,
* "sync": "function(doc){channel(doc.channels);}",
* "unsupported": {
  * "api_endpoints": {
    * "enable_couchbase_bucket_flush": true  
  },
  * "dcp_read_buffer": 0,
  * "force_api_forbidden_errors": true,
  * "guest_read_only": true,
  * "kv_buffer": 0,
  * "oidc_test_provider": {
    * "enabled": true  
  },
  * "oidc_tls_skip_verify": true,
  * "remote_config_tls_skip_verify": true,
  * "same_site_cookie": "Default",
  * "sgr_tls_skip_verify": true,
  * "user_views": {
    * "enabled": true  
  },
  * "warning_thresholds": {
    * "access_and_role_grants_per_doc": 0,
    * "channel_name_size": 0,
    * "channels_per_doc": 0,
    * "channels_per_user": 0,
    * "xattr_size_bytes": 0  
  }  
},
* "use_views": false,
* "user_xattr_key": "string",
* "username": "string",
* "users": {
  * "username1": {
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
  },
  * "username2": {
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
  }  
},
* "view_query_timeout_secs": 75,
* "allow_conflicts": false,
* "enable_shared_bucket_access": true,
* "feed_type": "DCP",
* "num_index_replicas": 1,
* "pool": "default",
* "rev_cache_size": 0
}`

### Response samples 

* 400
* 403
* 409
* 412
* 500

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Management/operation/get%5F%5Fall%5Fdbs)Get a list of all the databases 

This retrieves all the databases that are in the current Sync Gateway node. If verbose, returns bucket and state information for each database, otherwise returns names only.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| verbose | boolean |
| ------- | ------- |

### Responses

**200** 

Successfully retrieved all database names

get/\_all\_dbs

Admin API

{protocol}://{hostname}:4985/\_all\_dbs

### Response samples 

* 200

Content type

application/json

Example

SimpleVerboseSimple

Copy

`[
* "db1",
* "db2"
]`

## [](#tag/Database-Management/operation/get%5Fdb-%5Fresync)Get resync status 

This will retrieve the status of last resync operation (whether it is running or not) in the Sync Gateway cluster.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

successfully retrieved the most recent resync operation status

**404** 

Resource could not be found

get/{db}/\_resync

Admin API

{protocol}://{hostname}:4985/{db}/\_resync

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "running",
* "start_time": "string",
* "last_error": "string",
* "docs_changed": 0,
* "docs_processed": 0,
* "collections_processing": {
  * "scopeName": [
    * "collection1",
    * "collection2"  
  ]  
}
}`

## [](#tag/Database-Management/operation/post%5Fdb-%5Fresync)Start or stop Resync 

This can be used to start or stop a resync operation. A resync operation will cause all documents in the keyspace to be reprocessed through the sync function.

Generally, a resync operation might be wanted when the sync function has been modified in such a way that the channel or access mappings for any existing documents would change as a result.

A resync operation cannot be run if the database is online. The database can be taken offline by calling [POST /{db}/\_config](#operation/post%5Fdb-%5Fconfig) with `{"offline": true}` to set the database to offline.

The `requireUser()` and `requireRole()` calls in the sync function will always return `true`.

* **action=start** \- This is an asynchronous operation, and will start resync in the background.
* **action=stop** \- This will stop the currently running resync operation.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| action                | string Default: "start" Enum: "start" "stop" This is whether to start a new resync job or stop an existing one.                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| regenerate\_sequences | boolean **Use this only when requested to do so by the Couchbase support team** This request will regenerate the sequence numbers for each document processed. If scopes parameter is specified, the principal sequence documents will not have their sequences updated. |
| reset                 | boolean Default: false This forces a fresh resync run instead of trying to resume the previous resync operation                                                                                                                                                          |

##### Request Body schema: application/json

| scopes                | object This controls for which collections resync will run                                                                                                                                                                       |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| regenerate\_sequences | boolean Default: false This can be used as an alternative to query param regenerate\_sequences. If either query param or this is set to true, then the request will regenerate the sequence numbers for each document processed. |

### Responses

**200** 

successfully changed the status of the resync operation

**503** 

Service Unavailable

post/{db}/\_resync

Admin API

{protocol}://{hostname}:4985/{db}/\_resync

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "scopes": {
  * "scopeName": [
    * "collection1",
    * "collection2"  
  ]  
},
* "regenerate_sequences": false
}`

### Response samples 

* 200
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "running",
* "start_time": "string",
* "last_error": "string",
* "docs_changed": 0,
* "docs_processed": 0,
* "collections_processing": {
  * "scopeName": [
    * "collection1",
    * "collection2"  
  ]  
}
}`

## [](#tag/Database-Management/operation/post%5Fdb-%5Findex%5Finit)Start asynchronous index initialization 

This can be used to start index initialization with different parameters from a running database. The typical workflow is:

1. Start the process of creating new indexes with [POST /{db}/\_index\_init](#operation/post%5Fdb-%5Findex%5Finit).
2. Wait for index initialization to complete with [GET /{db}/\_index\_init](#operation/get%5Fdb-%5Findex%5Finit).
3. Update the database configuration to use these new indexes with [POST /{db}/\_config](#operation/post%5Fdb-%5Fconfig).
4. Call [POST /\_post\_upgrade](#operation/post%5F%5Fpost%5Fupgrade) to remove the original indexes.

This operation will start creation of indexes, and the creation of indexes can not be stopped on Couchbase Server once it has been started.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| action | string Default: "start" Enum **Description**startStarts the creation of indexes. stopStops tracking the index creation by Sync Gateway. These indexes will still be created on Couchbase Server. Defines whether the index creation operation is being started or stopped. |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| create\_separate\_principal\_indexes | boolean Default: false Whether to create separate indexes for users and roles instead of a single larger syncDocs index. The separate principal indexes are smaller and used automatically for new database deployments. To remove the syncDocs index, wait for this to complete, restart all Sync Gateway instances and run [POST /\_post\_upgrade](#operation/post%5F%5Fpost%5Fupgrade).                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| num\_partitions                      | number (Number of Index Partitions) Default: 1 The number of partitions to use for the large indexes created by Sync Gateway. It is not recommended to set this unless you require additional horizontal scalability for individual indexes and have appropriately scaled your Query nodes to handle the increased query parallelism. If set, the recommended number is 8 and does not need to be directly related to the number of your Query nodes. Ensure documentation is read to understand the performance tradeoffs and instructions for migration if you have previously run with only one partition. See [/{db}/\_index\_init](#operation/post%5Fdb-%5Findex%5Finit) for more information. If not specified or 1, all indexes will be non partitioned. |

### Responses

**200** 

successfully changed the status of the index initialization operation

**503** 

Service Unavailable

post/{db}/\_index\_init

Admin API

{protocol}://{hostname}:4985/{db}/\_index\_init

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "create_separate_principal_indexes": false,
* "num_partitions": 1
}`

### Response samples 

* 200
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "completed",
* "start_time": "string",
* "last_error": "string",
* "index_status": {
  * "scopename1": {
    * "collectionname1": "queued",
    * "collectionname2": "queued"  
  },
  * "scopename2": {
    * "collectionname1": "queued",
    * "collectionname2": "queued"  
  }  
},
* "settings": {
  * "create_separate_principal_indexes": false,
  * "num_partitions": 1  
}
}`

## [](#tag/Database-Management/operation/get%5Fdb-%5Findex%5Finit)Get status of index initialization 

This will retrieve the status of last index initialization operation (whether it is running or not) in the Sync Gateway cluster.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

successfully retrieved the most recent index initialization

**404** 

Resource could not be found

get/{db}/\_index\_init

Admin API

{protocol}://{hostname}:4985/{db}/\_index\_init

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "completed",
* "start_time": "string",
* "last_error": "string",
* "index_status": {
  * "scopename1": {
    * "collectionname1": "queued",
    * "collectionname2": "queued"  
  },
  * "scopename2": {
    * "collectionname1": "queued",
    * "collectionname2": "queued"  
  }  
},
* "settings": {
  * "create_separate_principal_indexes": false,
  * "num_partitions": 1  
}
}`

## [](#tag/Database-Management/operation/post%5Fdb-%5Fonline)Bring the database online 

This will bring the database online on this node only so the Public and full Admin REST API requests can be served.

If using persistent config, call [POST /{db}/\_config](#operation/post%5Fdb-%5Fconfig) with `{"offline": false}` to set the database to online.

Bringing a database online will:

* Close the database connection to the backing Couchbase Server bucket.
* Reload the database configuration, and connect to the backing Couchbase Server bucket.
* Re-establish access to the database from the Public REST API and accept all Admin API requests.

A specific delay before bringing the database online may be wanted to:

* Make the database available for Couchbase Lite clients at a specific time.
* Make the databases on several Sync Gateway instances available at the same time.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

Add an optional delay to wait before bringing the database online

| delay | integer Default: 0 The amount of seconds to delay bringing the database online. |
| ----- | ------------------------------------------------------------------------------- |

### Responses

**200** 

Database will be brought online immediately or with the specified delay

**404** 

Resource could not be found

**503** 

An error occurred

post/{db}/\_online

Admin API

{protocol}://{hostname}:4985/{db}/\_online

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "delay": 0
}`

### Response samples 

* 404
* 503

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Management/operation/post%5Fdb-%5Foffline)Take the database offline 

This will take the database offline on this node only. Actions can be taken without disrupting current operations ungracefully or having the restart the Sync Gateway instance.

If using persistent config, call [POST /{db}/\_config](#operation/post%5Fdb-%5Fconfig) with `{"offline": true}` to set the database to offline.

This will not take the backing Couchbase Server bucket offline.

Taking a database offline that is in the progress of coming online will take the database offline after it comes online.

Taking the database offline will:

* Close all active `_changes` feeds for the database.
* Reject all access to the database via the Public REST API (returning a 503 Service Unavailable code).
* Reject most Admin API requests (by returning a 503 Service Unavailable code). The only endpoints to be available are: the resync endpoints, the configuration endpoints, `DELETE, GET, HEAD /{db}/`, `POST /{db}/_offline`, and `POST /{db}/_online`.
* Stops webhook event handlers.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Database has been taken offline successfully

**404** 

Resource could not be found

**503** 

An error occurred while trying to take the database offline

post/{db}/\_offline

Admin API

{protocol}://{hostname}:4985/{db}/\_offline

### Response samples 

* 404
* 503

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Management/operation/post%5Fdb-%5Fcompact)Manage a compact operation 

This allows a new compact operation to be done on the database, or to stop an existing running compact operation.

The type of compaction that is done depends on what the `type` query parameter is set to. The 2 options will:

* `tombstone` \- purge the JSON bodies of non-leaf revisions. This is known as database compaction. Database compaction is done periodically automatically by the system. JSON bodies of leaf nodes (conflicting branches) are not removed therefore it is important to resolve conflicts in order to re-claim disk space.
* `attachment` \- purge all unlinked/unused legacy (pre 3.0) attachments. If the previous attachment compact operation failed, this will attempt to restart the `compact_id` at the appropriate phase (if possible).

Both types can each have a maximum of 1 compact operation running at any one point. This means that an attachment compaction can be running at the same time as a tombstone compaction but not 2 tombstone compactions.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| type     | string Default: "tombstone" Enum: "attachment" "tombstone" This is the type of compaction to use. The type must be either: attachment for cleaning up legacy (pre-3.0) attachments tombstone for purging the JSON bodies of non-leaf revisions.' |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| action   | string Default: "start" Enum: "start" "stop" Defines whether the compact operation is being started or stopped.                                                                                                                                  |
| reset    | boolean **Attachment compaction only** This forces a fresh compact start instead of trying to resume the previous failed compact operation.                                                                                                      |
| dry\_run | boolean **Attachment compaction only** This will run through all 3 stages of attachment compact but will not purge any attachments. This can be used to check how many attachments will be purged.'                                              |

### Responses

**200** 

Started or stopped compact operation successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

**503** 

Cannot start compaction due to another compaction operation still running.

post/{db}/\_compact

Admin API

{protocol}://{hostname}:4985/{db}/\_compact

### Response samples 

* 400
* 404
* 503

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Management/operation/get%5Fdb-%5Fcompact)Get the status of the most recent compact operation 

This will retrieve the current status of the most recent compact operation.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| type | string Default: "tombstone" Enum: "attachment" "tombstone" This is the type of compaction to use. The type must be either: attachment for cleaning up legacy (pre-3.0) attachments tombstone for purging the JSON bodies of non-leaf revisions.' |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### Responses

**200** 

Compaction status retrieved successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{db}/\_compact

Admin API

{protocol}://{hostname}:4985/{db}/\_compact

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

`{
* "status": "string",
* "start_time": "string",
* "last_error": "string",
* "docs_purged": "string",
* "marked_attachments": "string",
* "purged_attachments": "string",
* "compact_id": "string",
* "phase": "string",
* "dry_run": "mark"
}`

## [](#tag/Database-Management/operation/post%5Fdb-%5Fattachment%5Fmigration)Manage a attachment migration operation 

This allows a new attachment migration operation to be done on the database, or to stop an existing running attachment migration operation.

Attachment Migration is a single node process and can only one node can be running it at one point.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| action | string Default: "start" Enum: "start" "stop" Defines whether the an attachment migration operation is being started or stopped. |
| ------ | ------------------------------------------------------------------------------------------------------------------------------- |
| reset  | boolean This forces a fresh attachment migration start instead of trying to resume the previous failed migration operation.     |

### Responses

**200** 

Started or stopped compact operation successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

**503** 

Cannot start attachment migration due to another migration operation still running.

post/{db}/\_attachment\_migration

Admin API

{protocol}://{hostname}:4985/{db}/\_attachment\_migration

### Response samples 

* 400
* 404
* 503

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Management/operation/get%5Fdb-%5Fattachment%5Fmigration)Get the status of the most recent attachment migration operation 

This will retrieve the current status of the most recent attachment migration operation.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Attachment migration status retrieved successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{db}/\_attachment\_migration

Admin API

{protocol}://{hostname}:4985/{db}/\_attachment\_migration

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

`{
* "status": "running",
* "start_time": "string",
* "last_error": "string",
* "migration_id": "string",
* "docs_changed": 0,
* "docs_processed": 0,
* "docs_failed": 0
}`

## [](#tag/Database-Management/operation/post%5Fdb-%5Fensure%5Ffull%5Fcommit)Ensure Full Commit  Deprecated 

This endpoint is non-functional but is present for CouchDB compatibility. This was deprecated in CouchDB 3.0.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**201** 

OK

post/{db}/\_ensure\_full\_commit

Admin API

{protocol}://{hostname}:4985/{db}/\_ensure\_full\_commit

### Response samples 

* 201

Content type

application/json

Copy

`{
* "instance_start_time": 1644600082279583,
* "ok": true
}`

## [](#tag/Database-Configuration)Database Configuration

Configure Sync Gateway databases

## [](#tag/Database-Configuration/operation/get%5Fdb-%5Fconfig)Get database configuration 

Retrieve the full configuration for the database specified.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| redact              | boolean Deprecated Default: true No longer supported field.                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| include\_javascript | boolean Default: true Include the fields that have Javascript functions in the response. E.g. sync function, import filter, and event handlers. |
| include\_runtime    | boolean Default: false Whether to include the values set at runtime, and default values.                                                        |
| refresh\_config     | boolean Default: false Forces the configuration to be reloaded on the Sync Gateway node.                                                        |

### Responses

**200** 

Successfully retrieved database configuration

**404** 

Resource could not be found

get/{db}/\_config

Admin API

{protocol}://{hostname}:4985/{db}/\_config

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "allow_empty_password": false,
* "bucket": "The database name",
* "bucket_op_timeout_ms": 0,
* "cacertpath": "string",
* "cache": {
  * "channel_cache": {
    * "compact_high_watermark_pct": 80,
    * "compact_low_watermark_pct": 60,
    * "expiry_seconds": 60,
    * "max_length": 500,
    * "max_num_pending": 10000,
    * "max_number": 50000,
    * "max_wait_pending": 5000,
    * "max_wait_skipped": 3600000,
    * "min_length": 50,
    * "enable_star_channel": true,
    * "query_limit": 5000  
  },
  * "rev_cache": {
    * "max_memory_count_mb": 0,
    * "shard_count": 16,
    * "size": 5000  
  },
  * "channel_cache_expiry": 0,
  * "channel_cache_max_length": 0,
  * "channel_cache_min_length": 0,
  * "enable_star_channel": true,
  * "max_num_pending": 0,
  * "max_wait_pending": 0,
  * "max_wait_skipped": 0  
},
* "certpath": "string",
* "changes_request_plus": false,
* "client_partition_window_secs": 2592000,
* "compact_interval_days": 1,
* "cors": {
  * "headers": [
    * "Accept-Encoding",
    * "Authorization",
    * "Content-Type",
    * "If-Match"  
  ],
  * "login_origin": [
    * "<https://example.com>"  
  ],
  * "max_age": 0,
  * "origin": [
    * "<https://example.com>"  
  ]  
},
* "delta_sync": {
  * "enabled": false,
  * "rev_max_age_seconds": 86400  
},
* "disable_password_auth": false,
* "disable_public_all_docs": false,
* "event_handlers": {
  * "db_state_changed": {
    * "handler": "webhook",
    * "url": "string",
    * "filter": "string",
    * "timeout": 0  
  },
  * "document_changed": {
    * "handler": "webhook",
    * "url": "string",
    * "filter": "string",
    * "timeout": 0,
    * "options": {
      * "winning_rev_only": false  
      }  
  },
  * "max_processes": "string",
  * "wait_for_process": "string"  
},
* "guest": {
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
},
* "import_backup_old_rev": false,
* "import_docs": true,
* "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }",
* "import_partitions": 16,
* "index": {
  * "num_partitions": 1,
  * "num_replicas": 1  
},
* "javascript_timeout_secs": 60,
* "keypath": "string",
* "kv_tls_port": 11207,
* "local_doc_expiry_secs": 7776000,
* "local_jwt": {
  * "providername1": {
    * "algorithms": [
      * "string"  
      ],
    * "channels_claim": "string",
    * "client_id": "string",
    * "disable_session": true,
    * "issuer": "string",
    * "keys": [
      * {
        * "alg": "string",
        * "crv": "P-256",
        * "e": "string",
        * "kid": "string",
        * "kty": "RSA",
        * "n": "string",
        * "use": "sig",
        * "x": "string",
        * "y": "string"  
            }  
      ],
    * "register": true,
    * "roles_claim": "string",
    * "user_prefix": "string",
    * "username_claim": "string"  
  },
  * "providername2": {
    * "algorithms": [
      * "string"  
      ],
    * "channels_claim": "string",
    * "client_id": "string",
    * "disable_session": true,
    * "issuer": "string",
    * "keys": [
      * {
        * "alg": "string",
        * "crv": "P-256",
        * "e": "string",
        * "kid": "string",
        * "kty": "RSA",
        * "n": "string",
        * "use": "sig",
        * "x": "string",
        * "y": "string"  
            }  
      ],
    * "register": true,
    * "roles_claim": "string",
    * "user_prefix": "string",
    * "username_claim": "string"  
  }  
},
* "logging": {
  * "audit": {
    * "disabled_roles": [
      * {
        * "domain": "cbs",
        * "name": "string"  
            }  
      ],
    * "disabled_users": [
      * {
        * "domain": "cbs",
        * "name": "string"  
            }  
      ],
    * "enabled": false,
    * "enabled_events": [
      * [
        * 1234,
        * 5678  
            ]  
      ]  
  },
  * "console": {
    * "log_keys": [
      * "CRUD",
      * "HTTP",
      * "Query"  
      ],
    * "log_level": "debug"  
  }  
},
* "max_concurrent_query_ops": 1000,
* "name": "string",
* "offline": false,
* "oidc": {
  * "default_provider": "string",
  * "providers": {
    * "providername1": {
      * "InsecureSkipVerify": false,
      * "IsDefault": true,
      * "Name": "string",
      * "allow_unsigned_provider_tokens": true,
      * "callback_url": "string",
      * "channels_claim": "string",
      * "client_id": "string",
      * "disable_callback_state": false,
      * "disable_cfg_validation": false,
      * "disable_session": true,
      * "discovery_url": "string",
      * "include_access": true,
      * "issuer": "string",
      * "register": true,
      * "roles_claim": "string",
      * "scope": [
        * "string"  
            ],
      * "user_prefix": "string",
      * "username_claim": "string",
      * "validation_key": "string"  
      },
    * "providername2": {
      * "InsecureSkipVerify": false,
      * "IsDefault": true,
      * "Name": "string",
      * "allow_unsigned_provider_tokens": true,
      * "callback_url": "string",
      * "channels_claim": "string",
      * "client_id": "string",
      * "disable_callback_state": false,
      * "disable_cfg_validation": false,
      * "disable_session": true,
      * "discovery_url": "string",
      * "include_access": true,
      * "issuer": "string",
      * "register": true,
      * "roles_claim": "string",
      * "scope": [
        * "string"  
            ],
      * "user_prefix": "string",
      * "username_claim": "string",
      * "validation_key": "string"  
      }  
  }  
},
* "old_rev_expiry_seconds": 300,
* "password": "string",
* "query_pagination_limit": 5000,
* "replications": {
  * "replication_id": {
    * "adhoc": false,
    * "batch_size": 200,
    * "collections_enabled": false,
    * "collections_local": [
      * "scope1.collection1",
      * "scope1.collection3",
      * "scope1.collection6"  
      ],
    * "collections_remote": [
      * "scope1.collectionA",
      * null,
      * "scope1.collectionF"  
      ],
    * "conflict_resolution_type": "default",
    * "continuous": false,
    * "custom_conflict_resolver": "",
    * "direction": "push",
    * "enable_delta_sync": false,
    * "filter": "sync_gateway/bychannel",
    * "initial_state": "running",
    * "max_backoff_time": 5,
    * "purge_on_removal": false,
    * "query_params": [
      * "string"  
      ],
    * "remote": "string",
    * "remote_password": "string",
    * "remote_username": "string",
    * "replication_id": "string",
    * "run_as": "string",
    * "password": "string",
    * "username": "string"  
  }  
},
* "revs_limit": 50,
* "roles": {
  * "rolename1": {
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
  },
  * "rolename2": {
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
  }  
},
* "scopes": {
  * "scopename": {
    * "collections": {
      * "collectionname1": {
        * "sync": "function(doc){channel(\"collection name\");}",
        * "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            },
      * "collectionname2": {
        * "sync": "function(doc){channel(\"collection name\");}",
        * "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            }  
      }  
  }  
},
* "send_www_authenticate_header": true,
* "serve_insecure_attachment_types": false,
* "server": "string",
* "session_cookie_http_only": false,
* "session_cookie_name": "string",
* "session_cookie_secure": true,
* "sgreplicate_enabled": true,
* "sgreplicate_websocket_heartbeat_secs": 300,
* "slow_query_warning_threshold": 500,
* "store_legacy_revtree_data": true,
* "suspendable": false,
* "sync": "function(doc){channel(doc.channels);}",
* "unsupported": {
  * "api_endpoints": {
    * "enable_couchbase_bucket_flush": true  
  },
  * "dcp_read_buffer": 0,
  * "force_api_forbidden_errors": true,
  * "guest_read_only": true,
  * "kv_buffer": 0,
  * "oidc_test_provider": {
    * "enabled": true  
  },
  * "oidc_tls_skip_verify": true,
  * "remote_config_tls_skip_verify": true,
  * "same_site_cookie": "Default",
  * "sgr_tls_skip_verify": true,
  * "user_views": {
    * "enabled": true  
  },
  * "warning_thresholds": {
    * "access_and_role_grants_per_doc": 0,
    * "channel_name_size": 0,
    * "channels_per_doc": 0,
    * "channels_per_user": 0,
    * "xattr_size_bytes": 0  
  }  
},
* "use_views": false,
* "user_xattr_key": "string",
* "username": "string",
* "users": {
  * "username1": {
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
  },
  * "username2": {
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
  }  
},
* "view_query_timeout_secs": 75,
* "allow_conflicts": false,
* "enable_shared_bucket_access": true,
* "feed_type": "DCP",
* "num_index_replicas": 1,
* "pool": "default",
* "rev_cache_size": 0
}`

## [](#tag/Database-Configuration/operation/put%5Fdb-%5Fconfig)Replace database configuration 

Replaces the database configuration with the one sent in the request.

The bucket and database name cannot be changed. If these need to be changed, the database will need to be deleted then recreated with the new settings.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application (sync function only)

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| disable\_oidc\_validation | boolean Default: false If set, will not attempt to validate the configured OpenID Connect providers are reachable. |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |

##### header Parameters

| If-Match | string If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

The new database configuration to use

| allow\_empty\_password                  | boolean Default: false This controls whether users that are created can have an empty password or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket                                  | string Default: "The database name" The Couchbase Server backing bucket for the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| bucket\_op\_timeout\_ms                 | number This is the amount of milliseconds should pass before a bucket operation times out. An error will be returned if the bucket operation times out saying: operation timed out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| cacertpath                              | string The root CA cert path for X.509 bucket authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| cache                                   | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| certpath                                | string The cert path (public key) for X.509 bucket auth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| changes\_request\_plus                  | boolean Default: false Sets the default value of request\_plus for one-shot/non-continuous changes feeds, which when true, ensures all valid documents written prior to the request being issued are included in the response. Setting this option at the database level is required to ensure Couchbase Lite utilizes this changes feed mode. This also sets the default value of query param request\_plus for [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or request\_plus for [POST /{keyspace}/\_changes](#operation/post%5Fkeyspace-%5Fchanges).                                                                                                                                |
| client\_partition\_window\_secs         | integer Default: 2592000 How long (in seconds) clients can remain offline for without losing replication metadata. Defaults to 30 days (in seconds)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| compact\_interval\_days                 | number Default: 1 The interval between scheduled tombstone compaction runs (in days). This can be a floating point number. If set to 0, compaction will not run automatically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| cors                                    | object (Cors Configuration) CORS configuration for this database; if present, overrides server's config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| delta\_sync                             | object Delta sync configuration settings. **This is an Enterprise Edition feature only**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| disable\_password\_auth                 | boolean Default: false Whether to disable username/password authentication and only allow OIDC and guest access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| disable\_public\_all\_docs              | boolean Default: false This controls whether the [GET /{keyspace}/\_all\_docs](#operation/get%5Fkeyspace-%5Fall%5Fdocs) REST API endpoint is publicly accessible or not. Disabling this endpoint is recommended for larger datasets or production workloads. [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or [POST /{keyspace}/\_bulk\_get](#operation/post%5Fkeyspace-%5Fbulk%5Fget) have more efficient implementations and should be used instead. If set to true, the endpoint will not be publicly accessible, and will only be available on the Admin API. Setting this to false, or leaving it as the default value is deprecated, and may default to true in a future release. |
| event\_handlers                         | object These are the settings for webhooks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| guest                                   | object (User) Properties associated with a user                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| import\_backup\_old\_rev                | boolean Default: false This controls whether import should attempt to create a temporary backup of the previous revision body (if available) when the document is modified in the bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| import\_docs                            | boolean If true, documents will be imported in to Sync Gateway from the bucket in the background. Documents will be ran through the set import\_filter if any is set. The default value depends on the edition of Sync Gateway being used. If the edition is the Community Edition, then this will default to false or else in the Enterprise Edition, it will default to true. This value requires enable\_shared\_bucket\_access=true. This can also be set to the string continuous which maps to true.                                                                                                                                                                                                  |
| import\_filter                          | string This is the function that all imported documents in the default scope and collection are ran through in order to filter out what to import and what not to import. This allows you to control what is made available to Couchbase Mobile clients. If it is not set, then no documents are filtered when imported. import\_docs must be true to make this field applicable. If scopes parameter is set, this is ignored.                                                                                                                                                                                                                                                                              |
| import\_partitions                      | number \[ 1 .. 1024 \] Default: 16 \*\* This is an Enterprise Edition feature only\*\* This is how many import partitions should be used for import sharding. Partitions are distributed among all Sync Gateway nodes participating in import processing (import\_docs=true), and each process a subset of the server's vbuckets. Each partition is processed by an independent function that runs simultaneously to others, so import\_partitions can be used to tune concurrency based on the number of Sync Gateway nodes, and the number of cores per node.                                                                                                                                             |
| index                                   | object Global Secondary Index Settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| javascript\_timeout\_secs               | number Default: 60 The maximum number of seconds the sync, import filter, and custom conflict resolver JavaScript functions are allowed to run for before timing out. Set to 0 to allow the JS functions to run uncapped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| keypath                                 | string The key path (private key) for X.509 bucket auth                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| kv\_tls\_port                           | integer Default: 11207 The Memcached TLS port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| local\_doc\_expiry\_secs                | integer Default: 7776000 The number of seconds before a \_local document should expire.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| local\_jwt                              | object Configuration for Local JWT authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| logging                                 | object Per-database logging configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| max\_concurrent\_query\_ops             | integer Default: 1000 The maximum amount of query operations that can be running at any one point.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| name                                    | string The name of the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| offline                                 | boolean Default: false Start the database in an offline state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| oidc                                    | object Configuration for OpenID Connect authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| old\_rev\_expiry\_seconds               | number Default: 300 The number of seconds before old revisions are removed from the Couchbase Server bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| password                                | string The password for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| query\_pagination\_limit                | integer Default: 5000 The query limit to be used during pagination of large queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| replications                            | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| revs\_limit                             | number \>= 0 Default: 50 The maximum depth a document's revision tree can grow to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| roles                                   | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scopes                                  | object <= 1 properties An object keyed by scope name containing config for the specific collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| send\_www\_authenticate\_header         | boolean Default: true Controls whether to send a WWW-Authenticate header in 401 Unauthorized HTTP responses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| serve\_insecure\_attachment\_types      | boolean Default: false If set, always serve attachments with the Content-Type header set to the type of the attachment. When serving an attachment, usually the Content-Type header is set to the type of the attachment but the Content-Disposition response header will be set instead if the content type is vulnerable to a phishing attack, causing the browser to download the file instead of display it. This option will override that behaviour and always set the Content-Type header.                                                                                                                                                                                                           |
| server                                  | string This is the Couchbase Server address or addresses that the database connect to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| session\_cookie\_http\_only             | boolean Default: false Make all session cookies for the database set the HttpOnly flag so they are inaccessible to JavaScript.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| session\_cookie\_name                   | string This can be used to define a custom per-database session cookie name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| session\_cookie\_secure                 | boolean Override the session cookie secure flag. If set, the cookie will have the secure flag. This will default to true if startup config api.https.tls\_cert\_path is set otherwise it will default to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| sgreplicate\_enabled                    | boolean Default: true Whether the node should accept assign replications (true) or not (false).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| sgreplicate\_websocket\_heartbeat\_secs | integer Default: 300 Use a custom heartbeat interval (in seconds) for websocket ping frames.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| slow\_query\_warning\_threshold         | number Default: 500 The amount of milliseconds a N1QL query should run before logging a warning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| store\_legacy\_revtree\_data            | boolean Default: true Controls whether Sync Gateway stores additional legacy revision tree pointer data to support 3.x/early 4.x clients that still use RevTree IDs (for example when used as delta sources). Disable this when you are confident all clients use newer CV-based revisions and no longer require legacy RevTree ID lookups.                                                                                                                                                                                                                                                                                                                                                                 |
| suspendable                             | boolean Default: false Set to true to allow the database to be suspended. Defaults to true when running in serverless mode otherwise defaults to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| sync                                    | string Default: "function(doc){channel(doc.channels);}" The Javascript function that newly created documents are ran through for the default scope and collection. If scopes parameter is set, this is ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| unsupported                             | object These are unsupported options and therefore it is not recommended to use them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| use\_views                              | boolean Default: false Force the use of views instead of GSI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| user\_xattr\_key                        | string <= 15 The key to use for the user xattr that will be accessible from the sync function. If empty, the feature will be disabled. This is an Enterprise Edition feature only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| username                                | string The username for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| users                                   | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| view\_query\_timeout\_secs              | integer Default: 75 The number of seconds before a view query should timeout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| allow\_conflicts                        | boolean Deprecated Default: false Since Sync Gateway 4.0, this option has no effect. If this option is set to true on an existing database, the database must be modified to remove this parameter in order allow the database to come online. Otherwise, the database will be in the offline state.                                                                                                                                                                                                                                                                                                                                                                                                        |
| enable\_shared\_bucket\_access          | boolean Deprecated Default: true Since Sync Gateway 4.0, this option has no effect. If this option is set to true on an existing database, the database must be modified to remove this parameter in order allow the database to come online. Otherwise, the database will be in the offline state.                                                                                                                                                                                                                                                                                                                                                                                                         |
| feed\_type                              | string Deprecated Default: "DCP" Value: "DCP" The type of feed to use to communicate with Couchbase Server. This will use DCP regardless of specification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| num\_index\_replicas                    | number Deprecated Default: 1 **Deprecated, please use the database setting index.num\_replicas instead**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| pool                                    | string Deprecated Default: "default" This field is unsupported and ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| rev\_cache\_size                        | number Deprecated **Deprecated, please use the database setting cache.rev\_cache.size instead** The maximum number of revisions to store in the revision cache.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Responses

**201** 

Database configuration successfully updated

**400** 

There was a problem with your request

**404** 

Resource could not be found

**412** 

Precondition Failed

The supplied If-Match header did not match the current version of the configuration.

Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update.

put/{db}/\_config

Admin API

{protocol}://{hostname}:4985/{db}/\_config

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "allow_empty_password": false,
* "bucket": "The database name",
* "bucket_op_timeout_ms": 0,
* "cacertpath": "string",
* "cache": {
  * "channel_cache": {
    * "compact_high_watermark_pct": 80,
    * "compact_low_watermark_pct": 60,
    * "expiry_seconds": 60,
    * "max_length": 500,
    * "max_num_pending": 10000,
    * "max_number": 50000,
    * "max_wait_pending": 5000,
    * "max_wait_skipped": 3600000,
    * "min_length": 50,
    * "enable_star_channel": true,
    * "query_limit": 5000  
  },
  * "rev_cache": {
    * "max_memory_count_mb": 0,
    * "shard_count": 16,
    * "size": 5000  
  },
  * "channel_cache_expiry": 0,
  * "channel_cache_max_length": 0,
  * "channel_cache_min_length": 0,
  * "enable_star_channel": true,
  * "max_num_pending": 0,
  * "max_wait_pending": 0,
  * "max_wait_skipped": 0  
},
* "certpath": "string",
* "changes_request_plus": false,
* "client_partition_window_secs": 2592000,
* "compact_interval_days": 1,
* "cors": {
  * "headers": [
    * "Accept-Encoding",
    * "Authorization",
    * "Content-Type",
    * "If-Match"  
  ],
  * "login_origin": [
    * "<https://example.com>"  
  ],
  * "max_age": 0,
  * "origin": [
    * "<https://example.com>"  
  ]  
},
* "delta_sync": {
  * "enabled": false,
  * "rev_max_age_seconds": 86400  
},
* "disable_password_auth": false,
* "disable_public_all_docs": false,
* "event_handlers": {
  * "db_state_changed": {
    * "handler": "webhook",
    * "url": "string",
    * "filter": "string",
    * "timeout": 0  
  },
  * "document_changed": {
    * "handler": "webhook",
    * "url": "string",
    * "filter": "string",
    * "timeout": 0,
    * "options": {
      * "winning_rev_only": false  
      }  
  },
  * "max_processes": "string",
  * "wait_for_process": "string"  
},
* "guest": {
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
},
* "import_backup_old_rev": false,
* "import_docs": true,
* "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }",
* "import_partitions": 16,
* "index": {
  * "num_partitions": 1,
  * "num_replicas": 1  
},
* "javascript_timeout_secs": 60,
* "keypath": "string",
* "kv_tls_port": 11207,
* "local_doc_expiry_secs": 7776000,
* "local_jwt": {
  * "providername1": {
    * "algorithms": [
      * "string"  
      ],
    * "channels_claim": "string",
    * "client_id": "string",
    * "disable_session": true,
    * "issuer": "string",
    * "keys": [
      * {
        * "alg": "string",
        * "crv": "P-256",
        * "e": "string",
        * "kid": "string",
        * "kty": "RSA",
        * "n": "string",
        * "use": "sig",
        * "x": "string",
        * "y": "string"  
            }  
      ],
    * "register": true,
    * "roles_claim": "string",
    * "user_prefix": "string",
    * "username_claim": "string"  
  },
  * "providername2": {
    * "algorithms": [
      * "string"  
      ],
    * "channels_claim": "string",
    * "client_id": "string",
    * "disable_session": true,
    * "issuer": "string",
    * "keys": [
      * {
        * "alg": "string",
        * "crv": "P-256",
        * "e": "string",
        * "kid": "string",
        * "kty": "RSA",
        * "n": "string",
        * "use": "sig",
        * "x": "string",
        * "y": "string"  
            }  
      ],
    * "register": true,
    * "roles_claim": "string",
    * "user_prefix": "string",
    * "username_claim": "string"  
  }  
},
* "logging": {
  * "audit": {
    * "disabled_roles": [
      * {
        * "domain": "cbs",
        * "name": "string"  
            }  
      ],
    * "disabled_users": [
      * {
        * "domain": "cbs",
        * "name": "string"  
            }  
      ],
    * "enabled": false,
    * "enabled_events": [
      * [
        * 1234,
        * 5678  
            ]  
      ]  
  },
  * "console": {
    * "log_keys": [
      * "CRUD",
      * "HTTP",
      * "Query"  
      ],
    * "log_level": "debug"  
  }  
},
* "max_concurrent_query_ops": 1000,
* "name": "string",
* "offline": false,
* "oidc": {
  * "default_provider": "string",
  * "providers": {
    * "providername1": {
      * "InsecureSkipVerify": false,
      * "IsDefault": true,
      * "Name": "string",
      * "allow_unsigned_provider_tokens": true,
      * "callback_url": "string",
      * "channels_claim": "string",
      * "client_id": "string",
      * "disable_callback_state": false,
      * "disable_cfg_validation": false,
      * "disable_session": true,
      * "discovery_url": "string",
      * "include_access": true,
      * "issuer": "string",
      * "register": true,
      * "roles_claim": "string",
      * "scope": [
        * "string"  
            ],
      * "user_prefix": "string",
      * "username_claim": "string",
      * "validation_key": "string"  
      },
    * "providername2": {
      * "InsecureSkipVerify": false,
      * "IsDefault": true,
      * "Name": "string",
      * "allow_unsigned_provider_tokens": true,
      * "callback_url": "string",
      * "channels_claim": "string",
      * "client_id": "string",
      * "disable_callback_state": false,
      * "disable_cfg_validation": false,
      * "disable_session": true,
      * "discovery_url": "string",
      * "include_access": true,
      * "issuer": "string",
      * "register": true,
      * "roles_claim": "string",
      * "scope": [
        * "string"  
            ],
      * "user_prefix": "string",
      * "username_claim": "string",
      * "validation_key": "string"  
      }  
  }  
},
* "old_rev_expiry_seconds": 300,
* "password": "string",
* "query_pagination_limit": 5000,
* "replications": {
  * "replication_id": {
    * "adhoc": false,
    * "batch_size": 200,
    * "collections_enabled": false,
    * "collections_local": [
      * "scope1.collection1",
      * "scope1.collection3",
      * "scope1.collection6"  
      ],
    * "collections_remote": [
      * "scope1.collectionA",
      * null,
      * "scope1.collectionF"  
      ],
    * "conflict_resolution_type": "default",
    * "continuous": false,
    * "custom_conflict_resolver": "",
    * "direction": "push",
    * "enable_delta_sync": false,
    * "filter": "sync_gateway/bychannel",
    * "initial_state": "running",
    * "max_backoff_time": 5,
    * "purge_on_removal": false,
    * "query_params": [
      * "string"  
      ],
    * "remote": "string",
    * "remote_password": "string",
    * "remote_username": "string",
    * "replication_id": "string",
    * "run_as": "string",
    * "password": "string",
    * "username": "string"  
  }  
},
* "revs_limit": 50,
* "roles": {
  * "rolename1": {
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
  },
  * "rolename2": {
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
  }  
},
* "scopes": {
  * "scopename": {
    * "collections": {
      * "collectionname1": {
        * "sync": "function(doc){channel(\"collection name\");}",
        * "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            },
      * "collectionname2": {
        * "sync": "function(doc){channel(\"collection name\");}",
        * "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            }  
      }  
  }  
},
* "send_www_authenticate_header": true,
* "serve_insecure_attachment_types": false,
* "server": "string",
* "session_cookie_http_only": false,
* "session_cookie_name": "string",
* "session_cookie_secure": true,
* "sgreplicate_enabled": true,
* "sgreplicate_websocket_heartbeat_secs": 300,
* "slow_query_warning_threshold": 500,
* "store_legacy_revtree_data": true,
* "suspendable": false,
* "sync": "function(doc){channel(doc.channels);}",
* "unsupported": {
  * "api_endpoints": {
    * "enable_couchbase_bucket_flush": true  
  },
  * "dcp_read_buffer": 0,
  * "force_api_forbidden_errors": true,
  * "guest_read_only": true,
  * "kv_buffer": 0,
  * "oidc_test_provider": {
    * "enabled": true  
  },
  * "oidc_tls_skip_verify": true,
  * "remote_config_tls_skip_verify": true,
  * "same_site_cookie": "Default",
  * "sgr_tls_skip_verify": true,
  * "user_views": {
    * "enabled": true  
  },
  * "warning_thresholds": {
    * "access_and_role_grants_per_doc": 0,
    * "channel_name_size": 0,
    * "channels_per_doc": 0,
    * "channels_per_user": 0,
    * "xattr_size_bytes": 0  
  }  
},
* "use_views": false,
* "user_xattr_key": "string",
* "username": "string",
* "users": {
  * "username1": {
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
  },
  * "username2": {
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
  }  
},
* "view_query_timeout_secs": 75,
* "allow_conflicts": false,
* "enable_shared_bucket_access": true,
* "feed_type": "DCP",
* "num_index_replicas": 1,
* "pool": "default",
* "rev_cache_size": 0
}`

### Response samples 

* 400
* 404
* 412

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig)Update database configuration 

This is used to update the database configuration fields specified. Only the fields specified in the request will have their values replaced.

The bucket and database name cannot be changed. If these need to be changed, the database will need to be deleted then recreated with the new settings.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application (sync function only)

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### header Parameters

| If-Match | string If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

The database configuration fields to update

| allow\_empty\_password                  | boolean Default: false This controls whether users that are created can have an empty password or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket                                  | string Default: "The database name" The Couchbase Server backing bucket for the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| bucket\_op\_timeout\_ms                 | number This is the amount of milliseconds should pass before a bucket operation times out. An error will be returned if the bucket operation times out saying: operation timed out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| cacertpath                              | string The root CA cert path for X.509 bucket authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| cache                                   | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| certpath                                | string The cert path (public key) for X.509 bucket auth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| changes\_request\_plus                  | boolean Default: false Sets the default value of request\_plus for one-shot/non-continuous changes feeds, which when true, ensures all valid documents written prior to the request being issued are included in the response. Setting this option at the database level is required to ensure Couchbase Lite utilizes this changes feed mode. This also sets the default value of query param request\_plus for [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or request\_plus for [POST /{keyspace}/\_changes](#operation/post%5Fkeyspace-%5Fchanges).                                                                                                                                |
| client\_partition\_window\_secs         | integer Default: 2592000 How long (in seconds) clients can remain offline for without losing replication metadata. Defaults to 30 days (in seconds)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| compact\_interval\_days                 | number Default: 1 The interval between scheduled tombstone compaction runs (in days). This can be a floating point number. If set to 0, compaction will not run automatically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| cors                                    | object (Cors Configuration) CORS configuration for this database; if present, overrides server's config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| delta\_sync                             | object Delta sync configuration settings. **This is an Enterprise Edition feature only**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| disable\_password\_auth                 | boolean Default: false Whether to disable username/password authentication and only allow OIDC and guest access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| disable\_public\_all\_docs              | boolean Default: false This controls whether the [GET /{keyspace}/\_all\_docs](#operation/get%5Fkeyspace-%5Fall%5Fdocs) REST API endpoint is publicly accessible or not. Disabling this endpoint is recommended for larger datasets or production workloads. [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or [POST /{keyspace}/\_bulk\_get](#operation/post%5Fkeyspace-%5Fbulk%5Fget) have more efficient implementations and should be used instead. If set to true, the endpoint will not be publicly accessible, and will only be available on the Admin API. Setting this to false, or leaving it as the default value is deprecated, and may default to true in a future release. |
| event\_handlers                         | object These are the settings for webhooks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| guest                                   | object (User) Properties associated with a user                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| import\_backup\_old\_rev                | boolean Default: false This controls whether import should attempt to create a temporary backup of the previous revision body (if available) when the document is modified in the bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| import\_docs                            | boolean If true, documents will be imported in to Sync Gateway from the bucket in the background. Documents will be ran through the set import\_filter if any is set. The default value depends on the edition of Sync Gateway being used. If the edition is the Community Edition, then this will default to false or else in the Enterprise Edition, it will default to true. This value requires enable\_shared\_bucket\_access=true. This can also be set to the string continuous which maps to true.                                                                                                                                                                                                  |
| import\_filter                          | string This is the function that all imported documents in the default scope and collection are ran through in order to filter out what to import and what not to import. This allows you to control what is made available to Couchbase Mobile clients. If it is not set, then no documents are filtered when imported. import\_docs must be true to make this field applicable. If scopes parameter is set, this is ignored.                                                                                                                                                                                                                                                                              |
| import\_partitions                      | number \[ 1 .. 1024 \] Default: 16 \*\* This is an Enterprise Edition feature only\*\* This is how many import partitions should be used for import sharding. Partitions are distributed among all Sync Gateway nodes participating in import processing (import\_docs=true), and each process a subset of the server's vbuckets. Each partition is processed by an independent function that runs simultaneously to others, so import\_partitions can be used to tune concurrency based on the number of Sync Gateway nodes, and the number of cores per node.                                                                                                                                             |
| index                                   | object Global Secondary Index Settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| javascript\_timeout\_secs               | number Default: 60 The maximum number of seconds the sync, import filter, and custom conflict resolver JavaScript functions are allowed to run for before timing out. Set to 0 to allow the JS functions to run uncapped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| keypath                                 | string The key path (private key) for X.509 bucket auth                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| kv\_tls\_port                           | integer Default: 11207 The Memcached TLS port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| local\_doc\_expiry\_secs                | integer Default: 7776000 The number of seconds before a \_local document should expire.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| local\_jwt                              | object Configuration for Local JWT authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| logging                                 | object Per-database logging configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| max\_concurrent\_query\_ops             | integer Default: 1000 The maximum amount of query operations that can be running at any one point.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| name                                    | string The name of the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| offline                                 | boolean Default: false Start the database in an offline state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| oidc                                    | object Configuration for OpenID Connect authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| old\_rev\_expiry\_seconds               | number Default: 300 The number of seconds before old revisions are removed from the Couchbase Server bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| password                                | string The password for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| query\_pagination\_limit                | integer Default: 5000 The query limit to be used during pagination of large queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| replications                            | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| revs\_limit                             | number \>= 0 Default: 50 The maximum depth a document's revision tree can grow to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| roles                                   | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scopes                                  | object <= 1 properties An object keyed by scope name containing config for the specific collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| send\_www\_authenticate\_header         | boolean Default: true Controls whether to send a WWW-Authenticate header in 401 Unauthorized HTTP responses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| serve\_insecure\_attachment\_types      | boolean Default: false If set, always serve attachments with the Content-Type header set to the type of the attachment. When serving an attachment, usually the Content-Type header is set to the type of the attachment but the Content-Disposition response header will be set instead if the content type is vulnerable to a phishing attack, causing the browser to download the file instead of display it. This option will override that behaviour and always set the Content-Type header.                                                                                                                                                                                                           |
| server                                  | string This is the Couchbase Server address or addresses that the database connect to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| session\_cookie\_http\_only             | boolean Default: false Make all session cookies for the database set the HttpOnly flag so they are inaccessible to JavaScript.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| session\_cookie\_name                   | string This can be used to define a custom per-database session cookie name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| session\_cookie\_secure                 | boolean Override the session cookie secure flag. If set, the cookie will have the secure flag. This will default to true if startup config api.https.tls\_cert\_path is set otherwise it will default to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| sgreplicate\_enabled                    | boolean Default: true Whether the node should accept assign replications (true) or not (false).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| sgreplicate\_websocket\_heartbeat\_secs | integer Default: 300 Use a custom heartbeat interval (in seconds) for websocket ping frames.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| slow\_query\_warning\_threshold         | number Default: 500 The amount of milliseconds a N1QL query should run before logging a warning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| store\_legacy\_revtree\_data            | boolean Default: true Controls whether Sync Gateway stores additional legacy revision tree pointer data to support 3.x/early 4.x clients that still use RevTree IDs (for example when used as delta sources). Disable this when you are confident all clients use newer CV-based revisions and no longer require legacy RevTree ID lookups.                                                                                                                                                                                                                                                                                                                                                                 |
| suspendable                             | boolean Default: false Set to true to allow the database to be suspended. Defaults to true when running in serverless mode otherwise defaults to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| sync                                    | string Default: "function(doc){channel(doc.channels);}" The Javascript function that newly created documents are ran through for the default scope and collection. If scopes parameter is set, this is ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| unsupported                             | object These are unsupported options and therefore it is not recommended to use them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| use\_views                              | boolean Default: false Force the use of views instead of GSI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| user\_xattr\_key                        | string <= 15 The key to use for the user xattr that will be accessible from the sync function. If empty, the feature will be disabled. This is an Enterprise Edition feature only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| username                                | string The username for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| users                                   | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| view\_query\_timeout\_secs              | integer Default: 75 The number of seconds before a view query should timeout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| allow\_conflicts                        | boolean Deprecated Default: false Since Sync Gateway 4.0, this option has no effect. If this option is set to true on an existing database, the database must be modified to remove this parameter in order allow the database to come online. Otherwise, the database will be in the offline state.                                                                                                                                                                                                                                                                                                                                                                                                        |
| enable\_shared\_bucket\_access          | boolean Deprecated Default: true Since Sync Gateway 4.0, this option has no effect. If this option is set to true on an existing database, the database must be modified to remove this parameter in order allow the database to come online. Otherwise, the database will be in the offline state.                                                                                                                                                                                                                                                                                                                                                                                                         |
| feed\_type                              | string Deprecated Default: "DCP" Value: "DCP" The type of feed to use to communicate with Couchbase Server. This will use DCP regardless of specification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| num\_index\_replicas                    | number Deprecated Default: 1 **Deprecated, please use the database setting index.num\_replicas instead**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| pool                                    | string Deprecated Default: "default" This field is unsupported and ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| rev\_cache\_size                        | number Deprecated **Deprecated, please use the database setting cache.rev\_cache.size instead** The maximum number of revisions to store in the revision cache.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Responses

**201** 

Database configuration successfully updated

**400** 

There was a problem with your request

**404** 

Not Found

**412** 

Precondition Failed

The supplied If-Match header did not match the current version of the configuration.

Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update.

post/{db}/\_config

Admin API

{protocol}://{hostname}:4985/{db}/\_config

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "allow_empty_password": false,
* "bucket": "The database name",
* "bucket_op_timeout_ms": 0,
* "cacertpath": "string",
* "cache": {
  * "channel_cache": {
    * "compact_high_watermark_pct": 80,
    * "compact_low_watermark_pct": 60,
    * "expiry_seconds": 60,
    * "max_length": 500,
    * "max_num_pending": 10000,
    * "max_number": 50000,
    * "max_wait_pending": 5000,
    * "max_wait_skipped": 3600000,
    * "min_length": 50,
    * "enable_star_channel": true,
    * "query_limit": 5000  
  },
  * "rev_cache": {
    * "max_memory_count_mb": 0,
    * "shard_count": 16,
    * "size": 5000  
  },
  * "channel_cache_expiry": 0,
  * "channel_cache_max_length": 0,
  * "channel_cache_min_length": 0,
  * "enable_star_channel": true,
  * "max_num_pending": 0,
  * "max_wait_pending": 0,
  * "max_wait_skipped": 0  
},
* "certpath": "string",
* "changes_request_plus": false,
* "client_partition_window_secs": 2592000,
* "compact_interval_days": 1,
* "cors": {
  * "headers": [
    * "Accept-Encoding",
    * "Authorization",
    * "Content-Type",
    * "If-Match"  
  ],
  * "login_origin": [
    * "<https://example.com>"  
  ],
  * "max_age": 0,
  * "origin": [
    * "<https://example.com>"  
  ]  
},
* "delta_sync": {
  * "enabled": false,
  * "rev_max_age_seconds": 86400  
},
* "disable_password_auth": false,
* "disable_public_all_docs": false,
* "event_handlers": {
  * "db_state_changed": {
    * "handler": "webhook",
    * "url": "string",
    * "filter": "string",
    * "timeout": 0  
  },
  * "document_changed": {
    * "handler": "webhook",
    * "url": "string",
    * "filter": "string",
    * "timeout": 0,
    * "options": {
      * "winning_rev_only": false  
      }  
  },
  * "max_processes": "string",
  * "wait_for_process": "string"  
},
* "guest": {
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
},
* "import_backup_old_rev": false,
* "import_docs": true,
* "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }",
* "import_partitions": 16,
* "index": {
  * "num_partitions": 1,
  * "num_replicas": 1  
},
* "javascript_timeout_secs": 60,
* "keypath": "string",
* "kv_tls_port": 11207,
* "local_doc_expiry_secs": 7776000,
* "local_jwt": {
  * "providername1": {
    * "algorithms": [
      * "string"  
      ],
    * "channels_claim": "string",
    * "client_id": "string",
    * "disable_session": true,
    * "issuer": "string",
    * "keys": [
      * {
        * "alg": "string",
        * "crv": "P-256",
        * "e": "string",
        * "kid": "string",
        * "kty": "RSA",
        * "n": "string",
        * "use": "sig",
        * "x": "string",
        * "y": "string"  
            }  
      ],
    * "register": true,
    * "roles_claim": "string",
    * "user_prefix": "string",
    * "username_claim": "string"  
  },
  * "providername2": {
    * "algorithms": [
      * "string"  
      ],
    * "channels_claim": "string",
    * "client_id": "string",
    * "disable_session": true,
    * "issuer": "string",
    * "keys": [
      * {
        * "alg": "string",
        * "crv": "P-256",
        * "e": "string",
        * "kid": "string",
        * "kty": "RSA",
        * "n": "string",
        * "use": "sig",
        * "x": "string",
        * "y": "string"  
            }  
      ],
    * "register": true,
    * "roles_claim": "string",
    * "user_prefix": "string",
    * "username_claim": "string"  
  }  
},
* "logging": {
  * "audit": {
    * "disabled_roles": [
      * {
        * "domain": "cbs",
        * "name": "string"  
            }  
      ],
    * "disabled_users": [
      * {
        * "domain": "cbs",
        * "name": "string"  
            }  
      ],
    * "enabled": false,
    * "enabled_events": [
      * [
        * 1234,
        * 5678  
            ]  
      ]  
  },
  * "console": {
    * "log_keys": [
      * "CRUD",
      * "HTTP",
      * "Query"  
      ],
    * "log_level": "debug"  
  }  
},
* "max_concurrent_query_ops": 1000,
* "name": "string",
* "offline": false,
* "oidc": {
  * "default_provider": "string",
  * "providers": {
    * "providername1": {
      * "InsecureSkipVerify": false,
      * "IsDefault": true,
      * "Name": "string",
      * "allow_unsigned_provider_tokens": true,
      * "callback_url": "string",
      * "channels_claim": "string",
      * "client_id": "string",
      * "disable_callback_state": false,
      * "disable_cfg_validation": false,
      * "disable_session": true,
      * "discovery_url": "string",
      * "include_access": true,
      * "issuer": "string",
      * "register": true,
      * "roles_claim": "string",
      * "scope": [
        * "string"  
            ],
      * "user_prefix": "string",
      * "username_claim": "string",
      * "validation_key": "string"  
      },
    * "providername2": {
      * "InsecureSkipVerify": false,
      * "IsDefault": true,
      * "Name": "string",
      * "allow_unsigned_provider_tokens": true,
      * "callback_url": "string",
      * "channels_claim": "string",
      * "client_id": "string",
      * "disable_callback_state": false,
      * "disable_cfg_validation": false,
      * "disable_session": true,
      * "discovery_url": "string",
      * "include_access": true,
      * "issuer": "string",
      * "register": true,
      * "roles_claim": "string",
      * "scope": [
        * "string"  
            ],
      * "user_prefix": "string",
      * "username_claim": "string",
      * "validation_key": "string"  
      }  
  }  
},
* "old_rev_expiry_seconds": 300,
* "password": "string",
* "query_pagination_limit": 5000,
* "replications": {
  * "replication_id": {
    * "adhoc": false,
    * "batch_size": 200,
    * "collections_enabled": false,
    * "collections_local": [
      * "scope1.collection1",
      * "scope1.collection3",
      * "scope1.collection6"  
      ],
    * "collections_remote": [
      * "scope1.collectionA",
      * null,
      * "scope1.collectionF"  
      ],
    * "conflict_resolution_type": "default",
    * "continuous": false,
    * "custom_conflict_resolver": "",
    * "direction": "push",
    * "enable_delta_sync": false,
    * "filter": "sync_gateway/bychannel",
    * "initial_state": "running",
    * "max_backoff_time": 5,
    * "purge_on_removal": false,
    * "query_params": [
      * "string"  
      ],
    * "remote": "string",
    * "remote_password": "string",
    * "remote_username": "string",
    * "replication_id": "string",
    * "run_as": "string",
    * "password": "string",
    * "username": "string"  
  }  
},
* "revs_limit": 50,
* "roles": {
  * "rolename1": {
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
  },
  * "rolename2": {
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
  }  
},
* "scopes": {
  * "scopename": {
    * "collections": {
      * "collectionname1": {
        * "sync": "function(doc){channel(\"collection name\");}",
        * "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            },
      * "collectionname2": {
        * "sync": "function(doc){channel(\"collection name\");}",
        * "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            }  
      }  
  }  
},
* "send_www_authenticate_header": true,
* "serve_insecure_attachment_types": false,
* "server": "string",
* "session_cookie_http_only": false,
* "session_cookie_name": "string",
* "session_cookie_secure": true,
* "sgreplicate_enabled": true,
* "sgreplicate_websocket_heartbeat_secs": 300,
* "slow_query_warning_threshold": 500,
* "store_legacy_revtree_data": true,
* "suspendable": false,
* "sync": "function(doc){channel(doc.channels);}",
* "unsupported": {
  * "api_endpoints": {
    * "enable_couchbase_bucket_flush": true  
  },
  * "dcp_read_buffer": 0,
  * "force_api_forbidden_errors": true,
  * "guest_read_only": true,
  * "kv_buffer": 0,
  * "oidc_test_provider": {
    * "enabled": true  
  },
  * "oidc_tls_skip_verify": true,
  * "remote_config_tls_skip_verify": true,
  * "same_site_cookie": "Default",
  * "sgr_tls_skip_verify": true,
  * "user_views": {
    * "enabled": true  
  },
  * "warning_thresholds": {
    * "access_and_role_grants_per_doc": 0,
    * "channel_name_size": 0,
    * "channels_per_doc": 0,
    * "channels_per_user": 0,
    * "xattr_size_bytes": 0  
  }  
},
* "use_views": false,
* "user_xattr_key": "string",
* "username": "string",
* "users": {
  * "username1": {
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
  },
  * "username2": {
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
  }  
},
* "view_query_timeout_secs": 75,
* "allow_conflicts": false,
* "enable_shared_bucket_access": true,
* "feed_type": "DCP",
* "num_index_replicas": 1,
* "pool": "default",
* "rev_cache_size": 0
}`

### Response samples 

* 400
* 412

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Configuration/operation/get%5Fdb-%5Fconfig-audit)Get database audit configuration 

Retrieve the audit configuration for the database specified.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| verbose    | boolean Default: false Whether to show name and description with each audit event. |
| ---------- | ---------------------------------------------------------------------------------- |
| filterable | boolean Default: false Whether to show only filterable audit events.               |

### Responses

**200** 

Successfully retrieved database configuration

**404** 

Resource could not be found

get/{db}/\_config/audit

Admin API

{protocol}://{hostname}:4985/{db}/\_config/audit

### Response samples 

* 200
* 404

Content type

application/json

Example

SimpleVerboseSimple

Copy

 Expand all  Collapse all 

`{
* "enabled": true,
* "events": {
  * "audit_id1": true,
  * "audit_id2": true  
},
* "disabled_users": [
  * {
    * "domain": "cbs",
    * "name": "string"  
  }  
],
* "disabled_roles": [
  * {
    * "domain": "cbs",
    * "name": "string"  
  }  
]
}`

## [](#tag/Database-Configuration/operation/put%5Fdb-%5Fconfig-audit)Replace database audit configuration 

Replaces the database audit configuration with the one sent in the request.

Unspecified audit events will be reset to their default enabled value. Use POST if you want upsert-style semantics.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

The new database audit configuration to use

One of 

SimpleVerbose

| enabled         | boolean                                                                                |
| --------------- | -------------------------------------------------------------------------------------- |
| events          | object                                                                                 |
| disabled\_users | Array of objects List of users for which audit logging is disabled.                    |
| disabled\_roles | Array of objects List of roles for which audit logging is disabled. Either cbs or sgw. |

### Responses

**200** 

Database audit configuration successfully updated

**400** 

There was a problem with your request

**404** 

Resource could not be found

put/{db}/\_config/audit

Admin API

{protocol}://{hostname}:4985/{db}/\_config/audit

### Request samples 

* Payload

Content type

application/json

Example

SimpleVerboseSimple

Copy

 Expand all  Collapse all 

`{
* "enabled": true,
* "events": {
  * "audit_id1": true,
  * "audit_id2": true  
},
* "disabled_users": [
  * {
    * "domain": "cbs",
    * "name": "string"  
  }  
],
* "disabled_roles": [
  * {
    * "domain": "cbs",
    * "name": "string"  
  }  
]
}`

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig-audit)Update database audit configuration 

This is used to update the database configuration fields specified. Only the fields specified in the request will have their values replaced.

Unspecified audit events will be unaffected. Use PUT if you want to reset events to their default state.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| verbose | boolean Default: false Whether to show name and description with each audit event. |
| ------- | ---------------------------------------------------------------------------------- |

##### Request Body schema: application/json

The database configuration fields to update

One of 

SimpleVerbose

| enabled         | boolean                                                                                |
| --------------- | -------------------------------------------------------------------------------------- |
| events          | object                                                                                 |
| disabled\_users | Array of objects List of users for which audit logging is disabled.                    |
| disabled\_roles | Array of objects List of roles for which audit logging is disabled. Either cbs or sgw. |

### Responses

**200** 

Database audit configuration successfully updated

**400** 

There was a problem with your request

**404** 

Not Found

post/{db}/\_config/audit

Admin API

{protocol}://{hostname}:4985/{db}/\_config/audit

### Request samples 

* Payload

Content type

application/json

Example

SimpleVerboseSimple

Copy

 Expand all  Collapse all 

`{
* "enabled": true,
* "events": {
  * "audit_id1": true,
  * "audit_id2": true  
},
* "disabled_users": [
  * {
    * "domain": "cbs",
    * "name": "string"  
  }  
],
* "disabled_roles": [
  * {
    * "domain": "cbs",
    * "name": "string"  
  }  
]
}`

### Response samples 

* 400

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Configuration/operation/get%5Fkeyspace-%5Fconfig-sync)Get database sync function 

This returns the database's sync function.

Response will be blank if there has been no sync function set.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully retrieved the sync function

**404** 

Resource could not be found

get/{keyspace}/\_config/sync

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_config/sync

### Response samples 

* 200
* 404

Content type

application/javascript

Copy

function (doc, oldDoc) {
  channel(doc.channels);
}

## [](#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)Set database sync function 

This will allow you to update the sync function.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| disable\_oidc\_validation | boolean Default: false If set, will not attempt to validate the configured OpenID Connect providers are reachable. |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |

##### header Parameters

| If-Match | string If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/javascript

The new sync function to use

string

### Responses

**200** 

Updated sync function successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

**412** 

Precondition Failed

The supplied If-Match header did not match the current version of the configuration.

Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update.

put/{keyspace}/\_config/sync

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_config/sync

### Request samples 

* Payload

Content type

application/javascript

Copy

function (doc, oldDoc) {
  channel(doc.channels);
}

### Response samples 

* 400
* 404
* 412

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Configuration/operation/delete%5Fkeyspace-%5Fconfig-sync)Remove custom sync function 

This will remove the custom sync function from the database configuration.

The default sync function is equivalent to:

```javascript
function (doc) {
  channel(doc.channels);
}

```

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### header Parameters

| If-Match | string An optimistic concurrency control (OCC) value used to prevent conflicts. Use the value returned in the ETag response header of the GET request for the resource being updated, or the latest known Revision Tree ID or Current Version of the document. |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully reset the sync function

**404** 

Resource could not be found

**412** 

Precondition Failed

The supplied If-Match header did not match the current version of the configuration.

Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update.

delete/{keyspace}/\_config/sync

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_config/sync

### Response samples 

* 404
* 412

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Configuration/operation/get%5Fkeyspace-%5Fconfig-import%5Ffilter)Get database import filter 

This returns the database's import filter that documents are ran through when importing.

Response will be blank if there has been no import filter set.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully retrieved the import filter

**404** 

Resource could not be found

get/{keyspace}/\_config/import\_filter

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_config/import\_filter

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-import%5Ffilter)Set database import filter 

This will allow you to update the database's import filter.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| disable\_oidc\_validation | boolean Default: false If set, will not attempt to validate the configured OpenID Connect providers are reachable. |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |

##### header Parameters

| If-Match | string If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/javascript

The import filter to use

string

### Responses

**200** 

Updated import filter successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

**412** 

Precondition Failed

The supplied If-Match header did not match the current version of the configuration.

Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update.

put/{keyspace}/\_config/import\_filter

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_config/import\_filter

### Response samples 

* 400
* 404
* 412

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Database-Configuration/operation/delete%5Fkeyspace-%5Fconfig-import%5Ffilter)Delete import filter 

This will remove the custom import filter function from the database configuration so that Sync Gateway will not filter any documents during import.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### header Parameters

| If-Match | string If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully deleted the import filter

**404** 

Resource could not be found

**412** 

Precondition Failed

The supplied If-Match header did not match the current version of the configuration.

Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update.

delete/{keyspace}/\_config/import\_filter

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_config/import\_filter

### Response samples 

* 404
* 412

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Security)Database Security

Create and manage database users and roles

## [](#tag/Database-Security/operation/get%5Fdb-%5Fuser-)Get all the names of the users 

Retrieves all the names of the users that are in the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| name\_only | boolean Default: true Whether to return user names only, or more detailed information for each user. |
| ---------- | ---------------------------------------------------------------------------------------------------- |
| limit      | integer How many results to return. Using a value of 0 results in no limit.                          |

### Responses

**200** 

Users retrieved successfully

**404** 

Resource could not be found

get/{db}/\_user/

Admin API

{protocol}://{hostname}:4985/{db}/\_user/

### Response samples 

* 200
* 404

Content type

application/json

Copy

`[
* "Alice",
* "Bob"
]`

## [](#tag/Database-Security/operation/post%5Fdb-%5Fuser-)Create a new user 

Create a new user using the request body to specify the properties on the user.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

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

**201** 

New user created successfully

**404** 

Resource could not be found

**409** 

Resource already exists under that name

post/{db}/\_user/

Admin API

{protocol}://{hostname}:4985/{db}/\_user/

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
* 409

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Security/operation/get%5Fdb-%5Fuser-name)Get a user 

Retrieve a single users information.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

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

{protocol}://{hostname}:4985/{db}/\_user/{name}

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

{protocol}://{hostname}:4985/{db}/\_user/{name}

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

{protocol}://{hostname}:4985/{db}/\_user/{name}

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

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

{protocol}://{hostname}:4985/{db}/\_user/{name}

## [](#tag/Database-Security/operation/get%5Fdb-%5Frole-)Get all names of the roles 

Retrieves all the roles that are in the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

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

{protocol}://{hostname}:4985/{db}/\_role/

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

{protocol}://{hostname}:4985/{db}/\_role/

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

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

{protocol}://{hostname}:4985/{db}/\_role/{name}

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

{protocol}://{hostname}:4985/{db}/\_role/{name}

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

{protocol}://{hostname}:4985/{db}/\_role/{name}

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

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

{protocol}://{hostname}:4985/{db}/\_role/{name}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Session)Session

Manage user sessions

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

{protocol}://{hostname}:4985/{db}/\_session

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "authentication_handlers": [
  * "default",
  * "cookie"  
],
* "ok": true,
* "userCtx": {
  * "channels": {
    * "!": 1,
    * "channelA": 2  
  },
  * "name": "string"  
}
}`

## [](#tag/Session/operation/post%5Fdb-%5Fsession)Create a new user session 

Generates a login session for a user and returns the session ID and cookie name for that session. If no TTL is provided, then the default of 24 hours will be used.

A session cannot be generated for an non-existent user or the `GUEST` user.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

**401** 

User does not have access to resource, or resource does not exist

**404** 

Return if database does not exist

post/{db}/\_session

Admin API

{protocol}://{hostname}:4985/{db}/\_session

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
* 401
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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

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

{protocol}://{hostname}:4985/{db}/\_session/{sessionid}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "authentication_handlers": [
  * "default",
  * "cookie"  
],
* "ok": true,
* "userCtx": {
  * "channels": {
    * "!": 1,
    * "channelA": 2  
  },
  * "name": "string"  
}
}`

## [](#tag/Session/operation/delete%5Fdb-%5Fsession-sessionid)Remove session 

Invalidates the session provided so that anyone using it is logged out and is prevented from future use.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

{protocol}://{hostname}:4985/{db}/\_session/{sessionid}

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

{protocol}://{hostname}:4985/{db}/\_user/{name}/\_session

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

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

{protocol}://{hostname}:4985/{db}/\_user/{name}/\_session/{sessionid}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Document)Document

Create and manage documents and attachments

## [](#tag/Document/operation/get%5Fkeyspace-%5Fraw-docid)Get a document with the corresponding metadata 

Returns a document's latest revision with its metadata as stored.

Note: The direct use of this endpoint is unsupported. The sync metadata is maintained internally by Sync Gateway and its structure can change. It should not be used to drive business logic of applications since the response to the `/{db}/_raw/{id}` endpoint can change at any time.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| include\_doc | string Include the body associated with the document.                                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| redact       | boolean This redacts sensitive parts of the response. Cannot be used when include\_doc=true                                                                                           |
| salt         | string Whether to apply redaction with a custom salt - the intention here is to allow consistent hashing with a log collection. If this value is not set, a random salt will be used. |

### Responses

**200** 

Document found successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_raw/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_raw/{docid}

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "channels": [
  * "a",
  * "ecWZjZjcpg"  
],
* "myblob": {
  * "length": 11,
  * "content_type": "text/plain",
  * "digest": "sha1-Kq5sNclPz7QV2+lfQIuc6R7oRu0=",
  * "@type": "blob"  
},
* "_xattrs": {
  * "_sync": {
    * "cas": "0x000097d3e4e45418",
    * "channel_set": [
      * {
        * "name": "a",
        * "start": 3128  
            },
      * {
        * "name": "ecWZjZjcpg",
        * "start": 3128  
            }  
      ],
    * "channel_set_history": null,
    * "channels": {
      * "a": null,
      * "ecWZjZjcpg": null  
      },
    * "cluster_uuid": "ba2606db6dccedbcf4a6d3f66e242b8b",
    * "history": {
      * "channels": [
        * [
          * "a",
          * "ecWZjZjcpg"  
                    ]  
            ],
      * "parents": [
        * -1  
            ],
      * "revs": [
        * "1-525e04f141fbd0394d693531593105b88dbe0b25"  
            ]  
      },
    * "recent_sequences": [
      * 3128  
      ],
    * "rev": {
      * "rev": "1-525e04f141fbd0394d693531593105b88dbe0b25",
      * "src": "zTWkmBiYZgNQo7BHVZrB/Q",
      * "ver": "0x000097d3e4e45418"  
      },
    * "sequence": 3128,
    * "time_saved": "2025-07-23T14:37:06.407392+01:00",
    * "value_crc32c": "0x38db3c8c"  
  },
  * "_globalSync": {
    * "attachments_meta": {
      * "blob_/myblob": {
        * "content_type": "text/plain",
        * "digest": "sha1-Kq5sNclPz7QV2+lfQIuc6R7oRu0=",
        * "length": 11,
        * "revpos": 1,
        * "stub": true,
        * "ver": 2  
            }  
      }  
  },
  * "_mou": null,
  * "_vv": {
    * "cvCas": "0x000097d3e4e45418",
    * "src": "zTWkmBiYZgNQo7BHVZrB/Q",
    * "ver": "0x000097d3e4e45418"  
  }  
}
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fpurge)Purge a document 

The purge command provides a way to remove a document from the database. The operation removes _all_ revisions (active and tombstones) for the specified document(s). A common usage of this endpoint is to remove tombstone documents that are no longer needed, thus recovering storage space and reducing data replicated to clients. Other clients are not notified when a revision has been purged; so in order to purge a revision from the system it must be done from all databases (on Couchbase Lite and Sync Gateway).

When `enable_shared_bucket_access` is enabled, this endpoint removes the document and its associated extended attributes.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

Purge request body

| doc\_id\*additional property | Array of stringsItems Value: "\*" The document ID to purge. The array must only be 1 element which is \*. All revisions will be permanently removed for that document. |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Attempted documents purge. Check output to verify the documents that were purged. The document IDs will not be listed if they have not been purged (for example, due to no existing).

**400** 

Bad request. This could be due to the documents listed in the request body not having the `["*"]` value for each document ID.

**404** 

Resource could not be found

post/{keyspace}/\_purge

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_purge

### Request samples 

* Payload

Content type

application/json

Example

Single documentMultiple documentsSingle document

Copy

 Expand all  Collapse all 

`{
* "doc_id": [
  * "*"  
]
}`

### Response samples 

* 200
* 400
* 404

Content type

application/json

Example

Single documentMultiple documentsSingle document

Copy

 Expand all  Collapse all 

`{
* "purged": {
  * "doc_id": [
    * "*"  
  ]  
}
}`

## [](#tag/Document/operation/post%5Fkeyspace-)Create a new document 

Create a new document in the keyspace.

This will generate a random document ID unless specified in the body.

A document can have a maximum size of 20MB.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| roundtrip | boolean Block until document has been received by change cache |
| --------- | -------------------------------------------------------------- |

##### Request Body schema: application/json

| \_id                               | string The ID of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_rev                              | string The revision of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \_exp                              | string Expiry time after which the document will be purged. The expiration time is set and managed on the Couchbase Server document. The value can be specified in two ways; in ISO-8601 format, for example the 6th of July 2022 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; it can also be specified as a numeric Couchbase Server expiry value. Couchbase Server expiry values are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server). The document expiration time is returned in the response of GET /{db}/{doc}  when show\_exp=true is included in the query. As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication. This expiration time is not propagated when the document is replicated. The purge of the document does not cause it to be deleted on any other database. |
| \_deleted                          | boolean Whether the document is a tombstone or not. If true, it is a tombstone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \_revisions                        | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| \_attachments                      | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| property name\*additional property | any                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Responses

**200** 

New document revision created successfully.

**400** 

There was a problem with your request

**404** 

Resource could not be found

**409** 

Resource already exists under that name

**415** 

Invalid content type

post/{keyspace}/

Admin API

{protocol}://{hostname}:4985/{keyspace}/

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "_id": "string",
* "_rev": "string",
* "_exp": "string",
* "_deleted": true,
* "_revisions": {
  * "start": 0,
  * "ids": [
    * "string"  
  ]  
},
* "_attachments": {
  * "attachmentname1": {
    * "content_type": "string",
    * "data": "string"  
  },
  * "attachmentname2": {
    * "content_type": "string",
    * "data": "string"  
  }  
}
}`

### Response samples 

* 200
* 400
* 404
* 409
* 415

Content type

application/json

Copy

`{
* "id": "string",
* "ok": true,
* "rev": "string",
* "cv": "string"
}`

## [](#tag/Document/operation/get%5Fkeyspace-%5Fchanges)Get changes list 

This request retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| limit         | integer Maximum number of changes to return.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| since         | string Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response.                                                                                                                                                                                                                                                                                                                         |
| style         | string Default: "main\_only" Enum: "main\_only" "all\_docs" Controls whether to return the current winning revision (main\_only) or all the leaf revision including conflicts and deleted former conflicts (all\_docs).                                                                                                                                                                                                                                                                                         |
| active\_only  | boolean Default: false Set true to exclude deleted documents and notifications for documents the user no longer has access to from the changes feed.                                                                                                                                                                                                                                                                                                                                                            |
| include\_docs | boolean Include the body associated with each document.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| revocations   | boolean If true, revocation messages will be sent on the changes feed.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| filter        | string Enum: "sync\_gateway/bychannel" "\_doc\_ids" Set a filter to either filter by channels or document IDs.                                                                                                                                                                                                                                                                                                                                                                                                  |
| channels      | string A comma-separated list of channel names to filter the response to only the channels specified. To use this option, the filter query option must be set to sync\_gateway/bychannels.                                                                                                                                                                                                                                                                                                                      |
| doc\_ids      | Array of strings A valid JSON array of document IDs to filter the documents in the response to only the documents specified. To use this option, the filter query option must be set to \_doc\_ids and the feed parameter must be normal. Also accepts a comma separated list of document IDs instead.                                                                                                                                                                                                          |
| heartbeat     | integer Default: 0 The interval (in milliseconds) to send an empty line (CRLF) in the response. This is to help prevent gateways from deciding the socket is idle and therefore closing it. This is only applicable to feed=longpoll or feed=continuous. This will override any timeouts to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. The maximum heartbeat can be set in the server replication configuration. If heartbeat is non zero, it must be at least 25000 milliseconds. |
| timeout       | integer \[ 0 .. 900000 \] Default: 300000 This is the maximum period (in milliseconds) to wait for a change before the response is sent, even if there are no results. This is only applicable for feed=longpoll or feed=continuous changes feeds. Setting to 0 results in no timeout.                                                                                                                                                                                                                          |
| feed          | string Default: "normal" Enum: "normal" "longpoll" "continuous" "websocket" The type of changes feed to use.                                                                                                                                                                                                                                                                                                                                                                                                    |
| request\_plus | boolean Default: false When true, ensures all valid documents written prior to the request being issued are included in the response. This is only applicable for non-continuous feeds.                                                                                                                                                                                                                                                                                                                         |
| version\_type | string Default: "rev" Enum **Description**revRevision Tree IDs. For example: 1-293a80ce8f4874724732f27d35b3959a13cd96e0 cvCurrent Version. For example: 1854e4e557cc0000@zTWkmBiYZgNQo7BHVZrB/Q The preferred type of document versioning to use for the changes feed.                                                                                                                                                                                                                                          |

### Responses

**200** 

Successfully returned the changes feed

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_changes

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_changes

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "results": [
  * {
    * "seq": 0,
    * "id": "string",
    * "changes": [
      * {
        * "rev": "string"  
            }  
      ]  
  }  
],
* "last_seq": "string"
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fchanges)Get changes list 

This request retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| limit         | string Maximum number of changes to return.                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| style         | string Controls whether to return the current winning revision (main\_only) or all the leaf revision including conflicts and deleted former conflicts (all\_docs).                                                                                                                                                                                                                                                                |
| active\_only  | string Set true to exclude deleted documents and notifications for documents the user no longer has access to from the changes feed.                                                                                                                                                                                                                                                                                              |
| include\_docs | string Include the body associated with each document.                                                                                                                                                                                                                                                                                                                                                                            |
| revocations   | string If true, revocation messages will be sent on the changes feed.                                                                                                                                                                                                                                                                                                                                                             |
| filter        | string Set a filter to either filter by channels or document IDs.                                                                                                                                                                                                                                                                                                                                                                 |
| channels      | string A comma-separated list of channel names to filter the response to only the channels specified. To use this option, the filter query option must be set to sync\_gateway/bychannels.                                                                                                                                                                                                                                        |
| doc\_ids      | string A valid JSON array of document IDs to filter the documents in the response to only the documents specified. To use this option, the filter query option must be set to \_doc\_ids and the feed parameter must be normal.                                                                                                                                                                                                   |
| heartbeat     | string The interval (in milliseconds) to send an empty line (CRLF) in the response. This is to help prevent gateways from deciding the socket is idle and therefore closing it. This is only applicable to feed=longpoll or feed=continuous. This will override any timeouts to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. The maximum heartbeat can be set in the server replication configuration. |
| timeout       | string This is the maximum period (in milliseconds) to wait for a change before the response is sent, even if there are no results. This is only applicable for feed=longpoll or feed=continuous changes feeds. Setting to 0 results in no timeout.                                                                                                                                                                               |
| feed          | string The type of changes feed to use.                                                                                                                                                                                                                                                                                                                                                                                           |
| request\_plus | boolean Default: false When true, ensures all valid documents written prior to the request being issued are included in the response. This is only applicable for non-continuous feeds.                                                                                                                                                                                                                                           |
| version\_type | string Default: "rev" Enum **Description**revRevision Tree IDs. For example: 1-293a80ce8f4874724732f27d35b3959a13cd96e0 cvCurrent Version. For example: 1854e4e557cc0000@zTWkmBiYZgNQo7BHVZrB/Q The preferred type of document versioning to use for the changes feed.                                                                                                                                                            |

### Responses

**200** 

Successfully returned the changes feed

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{keyspace}/\_changes

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_changes

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "limit": "string",
* "style": "string",
* "active_only": "string",
* "include_docs": "string",
* "revocations": "string",
* "filter": "string",
* "channels": "string",
* "doc_ids": "string",
* "heartbeat": "string",
* "timeout": "string",
* "feed": "string",
* "request_plus": false,
* "version_type": "rev"
}`

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "results": [
  * {
    * "seq": 0,
    * "id": "string",
    * "changes": [
      * {
        * "rev": "string"  
            }  
      ]  
  }  
],
* "last_seq": "string"
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Frevs%5Fdiff)Compare revisions to what is in the database 

Takes a set of document IDs, each with a set of Revision Tree IDs. For each document, an array of unknown revisions are returned with an array of known revisions that may be recent ancestors.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| docid | Array of strings The document ID with an array of revisions to use for the comparison. |
| ----- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

Comparisons successful

**404** 

Resource could not be found

post/{keyspace}/\_revs\_diff

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_revs\_diff

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "docid": [
  * "string"  
]
}`

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "docid": {
  * "missing": [
    * "string"  
  ],
  * "possible_ancestors": [
    * "string"  
  ]  
}
}`

## [](#tag/Document/operation/get%5Fkeyspace-%5Flocal-docid)Get local document 

This request retrieves a local document.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string The name of the local document ID excluding the \_local/ prefix.                                                                                                                                                                                                                                                                   |

### Responses

**200** 

Successfully found local document

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_local/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_local/{docid}

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Document/operation/put%5Fkeyspace-%5Flocal-docid)Upsert a local document 

This request creates or updates a local document. Updating a local document requires that the Revision Tree ID be put in the body under `_rev`.

Local document IDs are given a `_local/` prefix. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by the client's replicator, as a place to store replication checkpoint data.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string The name of the local document ID excluding the \_local/ prefix.                                                                                                                                                                                                                                                                   |

##### Request Body schema: application/json

The body of the document

| \_rev | string Revision to replace. Required if updating existing local document. |
| ----- | ------------------------------------------------------------------------- |

### Responses

**201** 

Document successfully written. The document ID will be prefixed with `_local/`.

**400** 

There was a problem with your request

**404** 

Resource could not be found

**409** 

A conflict would result from updating this document revision.

put/{keyspace}/\_local/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_local/{docid}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "_rev": "2-5145e1086bb8d1d71a531e9f6b543c58"
}`

### Response samples 

* 201
* 400
* 404

Content type

application/json

Copy

`{
* "id": "string",
* "ok": true,
* "rev": "string",
* "cv": "string"
}`

## [](#tag/Document/operation/delete%5Fkeyspace-%5Flocal-docid)Delete a local document 

This request deletes a local document.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string The name of the local document ID excluding the \_local/ prefix.                                                                                                                                                                                                                                                                   |

##### query Parameters

| revrequired | string The Revision Tree ID of the revision to delete. |
| ----------- | ------------------------------------------------------ |

### Responses

**200** 

Successfully removed the local document.

**400** 

There was a problem with your request

**404** 

Resource could not be found

**409** 

A conflict would result from deleting this document revision.

delete/{keyspace}/\_local/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_local/{docid}

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Document/operation/head%5Fkeyspace-%5Flocal-docid)Check if local document exists 

This request checks if a local document exists.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string The name of the local document ID excluding the \_local/ prefix.                                                                                                                                                                                                                                                                   |

### Responses

**200** 

Document exists

**400** 

There was a problem with your request

**404** 

Resource could not be found

head/{keyspace}/\_local/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_local/{docid}

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Document/operation/get%5Fkeyspace-docid)Get a document 

Retrieve a document from the database by its doc ID.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. This can be a RevTree ID or a CV (Current Version) ID. If this is a CV value, ensure the query parameter is URL encoded (+\->%2B, @\->%40, etc.)                                                                                                                                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| open\_revs  | Array of strings Option to fetch specified revisions of the document. The value can be all to fetch all leaf revisions or an array of revision numbers (i.e. open\_revs=\["rev1", "rev2"\]). Only leaf revision bodies that haven't been pruned are guaranteed to be returned. If this option is specified the response will be in multipart format. Use the Accept: application/json request header to get the result as a JSON object. |
| show\_exp   | boolean Whether to show the expiry property (\_exp) in the response.                                                                                                                                                                                                                                                                                                                                                                     |
| revs\_from  | Array of strings Trim the revision history to stop at the first revision in the provided list. If no match is found, the revisions will be trimmed to the revs\_limit.                                                                                                                                                                                                                                                                   |
| atts\_since | Array of strings Include attachments only since specified revisions. Excludes the attachments for the specified revisions. Only gets used if attachments=true.                                                                                                                                                                                                                                                                           |
| revs\_limit | integer Maximum amount of revisions to return for each document.                                                                                                                                                                                                                                                                                                                                                                         |
| attachments | boolean Include attachment bodies in response.                                                                                                                                                                                                                                                                                                                                                                                           |
| replicator2 | boolean Returns the document with the required properties for replication. This is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                   |

### Responses

**200** 

Document found and returned successfully

**400** 

Document ID is not in an allowed format therefore is invalid.

This could be because it is over 250 characters or is prefixed with an underscore ("\_").

**404** 

Resource could not be found

**501** 

Not Implemented. It is likely this error was caused due to trying to use an enterprise-only feature on the community edition.

get/{keyspace}/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/{docid}

### Response samples 

* 200
* 400
* 404
* 501

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "FailedLoginAttempts": 5,
* "Friends": [
  * "Bob"  
],
* "_id": "AliceSettings",
* "_rev": "1-64d4a1f179db5c1848fe52967b47c166",
* "_cv": "1@src"
}`

## [](#tag/Document/operation/put%5Fkeyspace-docid)Upsert a document 

This will upsert a document, meaning if it does not exist then it will be created. Otherwise a new revision will be made for the existing document. A previous known version must be provided if targeting an existing document to prevent conflicts.

A document ID must be specified for this endpoint. To let Sync Gateway generate the ID, use the `POST /{db}/` endpoint.

If a document does exist, then replace the document content with the request body. This means unspecified fields will be removed in the new revision.

The maximum size for a document is 20MB.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| roundtrip   | boolean Block until document has been received by change cache                                                                                                                                                                                                                                                                                            |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| replicator2 | boolean Returns the document with the required properties for replication. This is an enterprise-edition only feature.                                                                                                                                                                                                                                    |
| new\_edits  | boolean Default: true Setting this to false indicates that the request body is an already-existing revision that should be directly inserted into the database, instead of a modification to apply to the current document. This mode is used for replication. This option must be used in conjunction with the \_revisions property in the request body. |
| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. This can be a RevTree ID or a CV (Current Version) ID. If this is a CV value, ensure the query parameter is URL encoded (+\->%2B, @\->%40, etc.)                                                                                                                   |

##### header Parameters

| If-Match | string An optimistic concurrency control (OCC) value used to prevent conflicts. Use the value returned in the ETag response header of the GET request for the resource being updated, or the latest known Revision Tree ID or Current Version of the document. |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| \_id                               | string The ID of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_rev                              | string The revision of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \_exp                              | string Expiry time after which the document will be purged. The expiration time is set and managed on the Couchbase Server document. The value can be specified in two ways; in ISO-8601 format, for example the 6th of July 2022 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; it can also be specified as a numeric Couchbase Server expiry value. Couchbase Server expiry values are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server). The document expiration time is returned in the response of GET /{db}/{doc}  when show\_exp=true is included in the query. As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication. This expiration time is not propagated when the document is replicated. The purge of the document does not cause it to be deleted on any other database. |
| \_deleted                          | boolean Whether the document is a tombstone or not. If true, it is a tombstone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \_revisions                        | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| \_attachments                      | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| property name\*additional property | any                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Responses

**201** 

Created

**400** 

There was a problem with your request

**404** 

Resource could not be found

**409** 

Resource already exists under that name

**415** 

Invalid content type

put/{keyspace}/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/{docid}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "_id": "string",
* "_rev": "string",
* "_exp": "string",
* "_deleted": true,
* "_revisions": {
  * "start": 0,
  * "ids": [
    * "string"  
  ]  
},
* "_attachments": {
  * "attachmentname1": {
    * "content_type": "string",
    * "data": "string"  
  },
  * "attachmentname2": {
    * "content_type": "string",
    * "data": "string"  
  }  
}
}`

### Response samples 

* 201
* 400
* 404
* 409
* 415

Content type

application/json

Copy

`{
* "id": "string",
* "ok": true,
* "rev": "string",
* "cv": "string"
}`

## [](#tag/Document/operation/delete%5Fkeyspace-docid)Delete a document 

Delete a document from the database. A new revision is created so the database can track the deletion in synchronized copies.

A revision ID either in the header or on the query parameters is required.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. This can be a RevTree ID or a CV (Current Version) ID. If this is a CV value, ensure the query parameter is URL encoded (+\->%2B, @\->%40, etc.) |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### header Parameters

| If-Match | string An optimistic concurrency control (OCC) value used to prevent conflicts. Use the value returned in the ETag response header of the GET request for the resource being updated, or the latest known Revision Tree ID or Current Version of the document. |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

New revision created successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

delete/{keyspace}/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/{docid}

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

`{
* "id": "string",
* "ok": true,
* "rev": "string",
* "cv": "string"
}`

## [](#tag/Document/operation/head%5Fkeyspace-docid)Check if a document exists 

Return a status code based on if the document exists or not.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. This can be a RevTree ID or a CV (Current Version) ID. If this is a CV value, ensure the query parameter is URL encoded (+\->%2B, @\->%40, etc.)                                                                                                                                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| open\_revs  | Array of strings Option to fetch specified revisions of the document. The value can be all to fetch all leaf revisions or an array of revision numbers (i.e. open\_revs=\["rev1", "rev2"\]). Only leaf revision bodies that haven't been pruned are guaranteed to be returned. If this option is specified the response will be in multipart format. Use the Accept: application/json request header to get the result as a JSON object. |
| show\_exp   | boolean Whether to show the expiry property (\_exp) in the response.                                                                                                                                                                                                                                                                                                                                                                     |
| revs\_from  | Array of strings Trim the revision history to stop at the first revision in the provided list. If no match is found, the revisions will be trimmed to the revs\_limit.                                                                                                                                                                                                                                                                   |
| atts\_since | Array of strings Include attachments only since specified revisions. Excludes the attachments for the specified revisions. Only gets used if attachments=true.                                                                                                                                                                                                                                                                           |
| revs\_limit | integer Maximum amount of revisions to return for each document.                                                                                                                                                                                                                                                                                                                                                                         |
| attachments | boolean Include attachment bodies in response.                                                                                                                                                                                                                                                                                                                                                                                           |
| replicator2 | boolean Returns the document with the required properties for replication. This is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                   |

### Responses

**200** 

Document exists

**400** 

Document ID is not in an allowed format therefore is invalid.

This could be because it is over 250 characters or is prefixed with an underscore ("\_").

**404** 

Resource could not be found

head/{keyspace}/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/{docid}

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Document/operation/get%5Fkeyspace-docid-attach)Get an attachment from a document 

This request retrieves a file attachment associated with the document.

The raw data of the associated attachment is returned (just as if you were accessing a static file). The `Content-Type` response header is the same content type set when the document attachment was added to the database. The `Content-Disposition` response header will be set if the content type is considered unsafe to display in a browser (unless overridden by by database config option `serve_insecure_attachment_types`) which will force the attachment to be downloaded.

If the `meta` query parameter is set then the response will be in JSON with the additional metadata tags.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| attachrequired   | string The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)).                                                                                                 |

##### query Parameters

| rev               | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. This can be a RevTree ID or a CV (Current Version) ID. If this is a CV value, ensure the query parameter is URL encoded (+\->%2B, @\->%40, etc.) |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| content\_encoding | boolean Default: true Set to false to disable the Content-Encoding response header.                                                                                                                                                     |
| meta              | boolean Default: false Return only the metadata of the attachment in the response body.                                                                                                                                                 |

##### header Parameters

| Range | string Example: bytes=123-456RFC-2616 bytes range header. |
| ----- | --------------------------------------------------------- |

### Responses

**200** 

Found attachment successfully.

**206** 

Partial attachment content returned

**404** 

Resource could not be found

**416** 

Requested range exceeds content length

get/{keyspace}/{docid}/{attach}

Admin API

{protocol}://{hostname}:4985/{keyspace}/{docid}/{attach}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Document/operation/put%5Fkeyspace-docid-attach)Create or update an attachment on a document 

This request adds or updates an attachment associated with the document. If the document does not exist, it will be created and the attachment will be added to it.

If the attachment already exists, the data of the existing attachment will be replaced in the new revision.

The maximum content size of an attachment is 20MB. The `Content-Type` header of the request specifies the content type of the attachment.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| attachrequired   | string The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)).                                                                                                 |

##### query Parameters

| rev | string The existing document revision ID to modify. Required only when modifying an existing document. |
| --- | ------------------------------------------------------------------------------------------------------ |

##### header Parameters

| Content-Type | string Default: application/octet-stream The content type of the attachment. |
| ------------ | ---------------------------------------------------------------------------- |
| If-Match     | string An alternative way of specifying the document revision ID.            |

##### Request Body schema: Attachment content type

The attachment data

string

The content to store in the body

### Responses

**201** 

Attachment added to new or existing document successfully

**404** 

Resource could not be found

**409** 

Resource already exists under that name

put/{keyspace}/{docid}/{attach}

Admin API

{protocol}://{hostname}:4985/{keyspace}/{docid}/{attach}

### Response samples 

* 201
* 404
* 409

Content type

application/json

Copy

`{
* "id": "string",
* "ok": true,
* "rev": "string",
* "cv": "string"
}`

## [](#tag/Document/operation/head%5Fkeyspace-docid-attach)Check if attachment exists 

This request check if the attachment exists on the specified document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| attachrequired   | string The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)).                                                                                                 |

##### query Parameters

| rev | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. This can be a RevTree ID or a CV (Current Version) ID. If this is a CV value, ensure the query parameter is URL encoded (+\->%2B, @\->%40, etc.) |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

The document exists and the attachment exists on the document.

**404** 

Resource could not be found

head/{keyspace}/{docid}/{attach}

Admin API

{protocol}://{hostname}:4985/{keyspace}/{docid}/{attach}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Document/operation/delete%5Fkeyspace-docid-attach)Delete an attachment on a document 

This request deletes an attachment associated with the document.

If the attachment exists, the attachment will be removed from the document.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| attachrequired   | string The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)).                                                                                                 |

##### query Parameters

| rev | string The existing document revision ID to modify. |
| --- | --------------------------------------------------- |

##### header Parameters

| If-Match | string An alternative way of specifying the document revision ID. |
| -------- | ----------------------------------------------------------------- |

### Responses

**200** 

Attachment removed from the document successfully

**404** 

Resource could not be found

**409** 

Resource already exists under that name

delete/{keyspace}/{docid}/{attach}

Admin API

{protocol}://{hostname}:4985/{keyspace}/{docid}/{attach}

### Response samples 

* 200
* 404
* 409

Content type

application/json

Copy

`{
* "id": "string",
* "ok": true,
* "rev": "string",
* "cv": "string"
}`

## [](#tag/Document/operation/get%5Fkeyspace-%5Fall%5Fdocs)Gets all the documents in the database with the given parameters 

Returns all documents in the database based on the specified parameters.

This endpoint is not recommended for larger datasets or production workloads. [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or [POST /{keyspace}/\_bulk\_get](#operation/post%5Fkeyspace-%5Fbulk%5Fget) have more efficient implementations and should be used instead.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| include\_docs | boolean Include the body associated with each document.                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| channels      | boolean Include the channels each document is part of that the calling user also has access too.              |
| access        | boolean Include what user/roles that each document grants access too.                                         |
| revs          | boolean Include all the revisions for each document under the \_revisions property.                           |
| update\_seq   | boolean Include the document sequence number update\_seq property for each document.                          |
| keys          | Array of strings An array of document ID strings to filter by.                                                |
| startkey      | string Return records starting with the specified key.                                                        |
| endkey        | string Stop returning records when this key is reached.                                                       |
| limit         | number This limits the number of result rows returned. Using a value of 0 has the same effect as the value 1. |

### Responses

**200** 

Operation ran successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_all\_docs

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_all\_docs

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "rows": [
  * {
    * "key": "string",
    * "id": "string",
    * "value": {
      * "rev": "string",
      * "cv": "string"  
      }  
  }  
],
* "total_rows": 0,
* "update_seq": 0
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fall%5Fdocs)Get all the documents in the database using a built-in view 

Returns all documents in the database based on the specified parameters.

This endpoint is not recommended for larger datasets or production workloads. [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or [POST /{keyspace}/\_bulk\_get](#operation/post%5Fkeyspace-%5Fbulk%5Fget) have more efficient implementations and should be used instead.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| include\_docs | boolean Include the body associated with each document.                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| channels      | boolean Include the channels each document is part of that the calling user also has access too.              |
| access        | boolean Include what user/roles that each document grants access too.                                         |
| revs          | boolean Include all the revisions for each document under the \_revisions property.                           |
| update\_seq   | boolean Include the document sequence number update\_seq property for each document.                          |
| startkey      | string Return records starting with the specified key.                                                        |
| endkey        | string Stop returning records when this key is reached.                                                       |
| limit         | number This limits the number of result rows returned. Using a value of 0 has the same effect as the value 1. |

##### Request Body schema: application/json

| keysrequired | Array of strings List of the documents to retrieve. |
| ------------ | --------------------------------------------------- |

### Responses

**200** 

Operation ran successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{keyspace}/\_all\_docs

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_all\_docs

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "keys": [
  * "string"  
]
}`

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "rows": [
  * {
    * "key": "string",
    * "id": "string",
    * "value": {
      * "rev": "string",
      * "cv": "string"  
      }  
  }  
],
* "total_rows": 0,
* "update_seq": 0
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fbulk%5Fdocs)Bulk document operations 

This will allow multiple documented to be created, updated or deleted in bulk.

To create a new document, simply add the body in an object under `docs`. A doc ID will be generated by Sync Gateway unless `_id` is specified.

To update an existing document, provide the document ID (`_id`) and Revision Tree ID (`_rev`) as well as the new body values.

To delete an existing document, provide the document ID (`_id`), Revision Tree ID (`_rev`), and set the deletion flag (`_deleted`) to true.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| new\_edits   | boolean Default: true This controls whether to assign new revision identifiers to new edits (true) or use the existing ones (false). |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| docsrequired | Array of objects                                                                                                                     |

### Responses

**201** 

Executed all operations.

Each object in the returned array represents a document. Each document should be checked to make sure it was successfully added to the database.

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{keyspace}/\_bulk\_docs

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_bulk\_docs

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "new_edits": true,
* "docs": [
  * {
    * "_id": "FooBar",
    * "foo": "bar"  
  },
  * {
    * "_id": "AliceSettings",
    * "_rev": "5-832a6db48ed130adadede928aee54576",
    * "FailedLoginAttempts": 7  
  },
  * {
    * "_id": "BobSettings",
    * "_rev": "1-fa76ba41ee5fdfee1b91fc478ed09e59",
    * "_deleted": true  
  }  
]
}`

### Response samples 

* 201
* 400
* 404

Content type

application/json

Example

SuccessPartialSuccessSuccess

Copy

 Expand all  Collapse all 

`[
* {
  * "id": "FooBar",
  * "rev": "1-cd809becc169215072fd567eebd8b8de"  
},
* {
  * "id": "AliceSettings",
  * "rev": "6-b3e8dcf825b71ccee112f3572ec4323c"  
},
* {
  * "id": "BobSettings",
  * "rev": "2-5145e1086bb8d1d71a531e9f6b543c58"  
}
]`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fbulk%5Fget)Get multiple documents in a MIME multipart response 

This request returns any number of documents, as individual bodies in a MIME multipart response.

Each enclosed body contains one requested document. The bodies appear in the same order as in the request, but can also be identified by their `X-Doc-ID` and `X-Rev-ID` headers (if the `attachments` query is `true`).

A body for a document with no attachments will have content type `application/json` and contain the document itself.

A body for a document that has attachments will be written as a nested `multipart/related` body.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| attachments | boolean Default: false This is for whether to include attachments in each of the documents returned or not.                                                                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| revs        | boolean Include all the revisions for each document under the \_revisions property.                                                                                                                                                                |
| revs\_limit | integer The number of revisions to include in the response from the document history. This parameter only makes a different if the revs query parameter is set to true. The full revision history will be returned if revs is set but this is not. |

##### header Parameters

| X-Accept-Part-Encoding | string If this header includes gzip then the part HTTP compression encoding will be done.                                                                                                                                                                                                       |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accept-Encoding        | string If this header includes gzip then the the HTTP response will be compressed. This takes priority over X-Accept-Part-Encoding. Only part compression will be done if X-Accept-Part-Encoding=gzip and the User-Agent is below 1.2 due to clients not being able to handle full compression. |

##### Request Body schema: application/json

| docsrequired | Array of objects |
| ------------ | ---------------- |

### Responses

**200** 

Returned the requested docs as `multipart/mixed` response type

**400** 

Bad Request

**404** 

Resource could not be found

post/{keyspace}/\_bulk\_get

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_bulk\_get

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "docs": [
  * {
    * "id": "FooBar"  
  },
  * {
    * "id": "attachment"  
  },
  * {
    * "id": "AliceSettings"  
  }  
]
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

## [](#tag/Replication)Replication

Create and manage inter-Sync Gateway replications

## [](#tag/Replication/operation/get%5Fdb-%5Freplication-)Get all replication configurations 

This will retrieve all database replication definitions.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Retrieved replication configurations successfully. The `assigned_node` fields will end with `(local)` or `(non-local)` depending on if the replication is running on this Sync Gateway node.

**404** 

Resource could not be found

get/{db}/\_replication/

Admin API

{protocol}://{hostname}:4985/{db}/\_replication/

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "replication_id": {
  * "replication_id": "string",
  * "adhoc": false,
  * "batch_size": 200,
  * "collections_enabled": false,
  * "collections_local": [
    * "scope1.collection1",
    * "scope1.collection3",
    * "scope1.collection6"  
  ],
  * "collections_remote": [
    * "scope1.collectionA",
    * null,
    * "scope1.collectionF"  
  ],
  * "conflict_resolution_type": "default",
  * "continuous": false,
  * "custom_conflict_resolver": "",
  * "direction": "push",
  * "enable_delta_sync": false,
  * "filter": "sync_gateway/bychannel",
  * "initial_state": "running",
  * "max_backoff_time": 5,
  * "purge_on_removal": false,
  * "query_params": [
    * "string"  
  ],
  * "remote": "string",
  * "remote_password": "string",
  * "remote_username": "string",
  * "run_as": "string",
  * "password": "string",
  * "username": "string",
  * "assigned_node": "string",
  * "target_state": "running",
  * "cluster_uuid": "string"  
}
}`

## [](#tag/Replication/operation/post%5Fdb-%5Freplication-)Upsert a replication 

Create or update a replication in the database.

If an existing replication is being updated, that replication must be stopped first.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

If the `replication_id` matches an existing replication then the existing configuration will be updated. Only the specified fields in the request will be used to update the existing configuration. Unspecified fields will remain untouched.

| adhoc                      | boolean Default: false Set to true to run the replication as an adhoc replication instead of a persistent one. This means that the replication will only last the period of the replication until the status is changed to stopped and then it will be removed automatically. It will also be removed if Sync Gateway restarts or if removed due to user action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| batch\_size                | integer Default: 200 The amount of changes to be sent in one batch of replications. Changing this is an Enterprise Edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| collections\_enabled       | boolean Default: false If true, the replicator will run with collections, and will replicate all collections, unless otherwise limited by collections\_local. If false, the replicator will only replicate the default collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| collections\_local         | Array of strings Default: \[\] Limits the set of collections replicated to those listed in this array. The replication will use all collections defined on the database if this list is empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| collections\_remote        | Array of strings or null Default: \[\] Remaps the local collection name to the one specified in this array when replicating with the remote. If only a subset of collections need remapping, elements in this array can be specified as null to preserve the local collection name. The same index is used for both collections\_remote and collections\_local, and both arrays must be the same length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| conflict\_resolution\_type | string Default: "default" Enum **Description**defaultThis will use: Timestamp based conflict resolution (often referred to as "last write wins", or LWW). Which uses a document timestamp from most recent document revisions to compare. The revision with the most recent timestamp wins. If replicating a document that was last updated/written pre upgrade to SG 4.x, the default policy for versions < 4.x will be used. localWinsThis will result in local revisions always being the winner in any conflict. remoteWinsThis will result in remote revisions always being the winner in any conflict. customThis will result in conflicts going through your own custom conflict resolver. You must provide this logic as a Javascript function in the custom\_conflict\_resolver parameter. This defines what conflict resolution policy Sync Gateway should use to apply when resolving conflicting revisions. Changing this is an Enterprise Edition only feature.                                                                                                                                                                                                                                                                                                                                                                           |
| continuous                 | boolean Default: false If true, changes will be immediately synced when they happen. This is known as a continuous replication. If false, all changes will be synced until they have been processed. The replication will then cease and not process any future changes (unless started again by the user). This is known as a one-shot replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| custom\_conflict\_resolver | string Default: "" This specifies the Javascript function to use to resolve conflicts between conflicting revisions. This **must** be used when conflict\_resolution\_type=custom. This property will be ignored when conflict\_resolution\_type is not custom. The Javascript function to provide this property should be in backticks (like the sync function). The function takes 1 parameter which is a struct that represents the conflict. This struct has 2 properties: LocalDocument \- The local document. This contains the document ID under the \_id key. RemoteDocument \- The remote document The function should return the new document's body. This can be the winning revision (for example, return conflict.LocalDocument), a new body, or nil to resolve as a delete. Example: function(conflict) {   console.log("Doc ID: "+conflict.LocalDocument.\_id);   console.log("Full remote doc: "+JSON.stringify(conflict.RemoteDocument));   return conflict.RemoteDocument; } Using complex custom\_conflict\_resolver functions can noticeably degrade performance. Use a built-in resolver whenever possible. If a document merge is being done, the \_rev and \_cv properties should not be included in the returned document body as Sync Gateway will generate new values for these. This is an Enterprise Edition only feature. |
| directionrequired          | string Enum **Description**pullchanges are pulled from the remote database pushchanges are pushed to the remote database pushAndPullchanges are both push-to and pulled-from the remote database This specifies which direction the replication will be replicating with the remote replicator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| enable\_delta\_sync        | boolean Default: false This will turn on delta-sync for the replication. In order to enable delta-sync for a replication, the database level setting delta\_sync.enabled must also be set to true. Using delta-sync is an Enterprise Edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| filter                     | string Enum **Description**Do not filter any documents. sync\_gateway/bychannelIf set, a pull replication will be limited to a specific set of channels specified by the query\_param.channels property. This defines whether to filter documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| initial\_state             | string Default: "running" Enum **Description**runningThe replication will immediately start running. stoppedThe replication configuration will be created but the replication will not start running until the user explicitly starts it. This is what state to start the replication in when creating a new replication. This allows you to control if the replication starts in a stopped start or running state. Replications prior to Sync Gateway 2.8 will run in the default state running.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| max\_backoff\_time         | integer Default: 5 Specifies the maximum time-period (in minutes) that Sync Gateway will attempt to reconnect to a lost or unreachable remote. When a disconnection happens, Sync Gateway will do an exponential backoff up to this specified value. When this value is met, it will attempt to reconnect indefinitely every max\_backoff\_time minutes. If this is set to 0, Sync Gateway will do the normal exponential backoff after the disconnect happens but then attempting 10 minutes and stop the replication. Note: this defaults to 5 minutes for replications created prior to Sync Gateway 2.8.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| purge\_on\_removal         | boolean Default: false Specifies whether to purge a document if the remote user loses access to all of the channels on the document when attempting to pull it from the remote. If false, documents will not be replicated and not be purged when the user loses access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| query\_params              | Array of strings This is a set of key/value pairs used in the query string of the replication. If filters=sync\_gateway/bychannel then this can be used to set the channels to filter by in a pull replication. To do this, set the channels key to a string array of the channels to filter by. For example: "filter":"sync\_gateway/bychannel", "query\_params": {   "channels":\["chanUser1"\] },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| remote                     | string This is the endpoint of the database for the remote Sync Gateway that is the subject of this replication's push, pull, or pushAndPull action. Typically this would include the URI, port, and database name. For example, https://localhost:4985/db.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| remote\_password           | string The password to use to authenticate with the remote. This password will be redacted in the replication config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| remote\_username           | string The username to use to authenticate with the remote.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| replication\_id            | string <= 160 This is the ID of the replication. When creating a new replication using a POST request, this will be set to a random UUID if not explicitly set. When the replication ID is specified in the URL, this must be set to the same replication ID if specifying it at all.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| run\_as                    | string This is used if you want to specify a user to run the replication as. This means that the replication will only be able to replicate what the user access to what the user has access to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| password                   | string Deprecated **This has been deprecated in favour of remote\_password.** This is the password to use to authenticate with the remote. This password will be redacted in the replication config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| username                   | string Deprecated **This has been deprecated in favour of remote\_username.** This is the username to use to authenticate with the remote.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Responses

**200** 

Updated existing configuration successfully

**201** 

Created new replication successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{db}/\_replication/

Admin API

{protocol}://{hostname}:4985/{db}/\_replication/

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "adhoc": false,
* "batch_size": 200,
* "collections_enabled": false,
* "collections_local": [
  * "scope1.collection1",
  * "scope1.collection3",
  * "scope1.collection6"  
],
* "collections_remote": [
  * "scope1.collectionA",
  * null,
  * "scope1.collectionF"  
],
* "conflict_resolution_type": "default",
* "continuous": false,
* "custom_conflict_resolver": "",
* "direction": "push",
* "enable_delta_sync": false,
* "filter": "sync_gateway/bychannel",
* "initial_state": "running",
* "max_backoff_time": 5,
* "purge_on_removal": false,
* "query_params": [
  * "string"  
],
* "remote": "string",
* "remote_password": "string",
* "remote_username": "string",
* "replication_id": "string",
* "run_as": "string",
* "password": "string",
* "username": "string"
}`

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Replication/operation/get%5Fdb-%5Freplication-replicationid)Get a replication configuration 

Retrieve a replication configuration from the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired            | string Example: db1The name of the database to run the operation against.     |
| --------------------- | ----------------------------------------------------------------------------- |
| replicationidrequired | string \[ 1 .. 160 \] What replication to target based on its replication ID. |

### Responses

**200** 

Successfully retrieved the replication configuration

**404** 

Resource could not be found

get/{db}/\_replication/{replicationid}

Admin API

{protocol}://{hostname}:4985/{db}/\_replication/{replicationid}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "replication_id": "string",
* "adhoc": false,
* "batch_size": 200,
* "collections_enabled": false,
* "collections_local": [
  * "scope1.collection1",
  * "scope1.collection3",
  * "scope1.collection6"  
],
* "collections_remote": [
  * "scope1.collectionA",
  * null,
  * "scope1.collectionF"  
],
* "conflict_resolution_type": "default",
* "continuous": false,
* "custom_conflict_resolver": "",
* "direction": "push",
* "enable_delta_sync": false,
* "filter": "sync_gateway/bychannel",
* "initial_state": "running",
* "max_backoff_time": 5,
* "purge_on_removal": false,
* "query_params": [
  * "string"  
],
* "remote": "string",
* "remote_password": "string",
* "remote_username": "string",
* "run_as": "string",
* "password": "string",
* "username": "string",
* "assigned_node": "string",
* "target_state": "running",
* "cluster_uuid": "string"
}`

## [](#tag/Replication/operation/put%5Fdb-%5Freplication-replicationid)Upsert a replication 

Create or update a replication in the database.

The replication ID does **not** need to be set in the request body.

If an existing replication is being updated, that replication must be stopped first and, if the `replication_id` is specified in the request body, it must match the replication ID in the URI.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired            | string Example: db1The name of the database to run the operation against.     |
| --------------------- | ----------------------------------------------------------------------------- |
| replicationidrequired | string \[ 1 .. 160 \] What replication to target based on its replication ID. |

##### Request Body schema: application/json

If the `replication_id` matches an existing replication then the existing configuration will be updated. Only the specified fields in the request will be used to update the existing configuration. Unspecified fields will remain untouched.

| adhoc                      | boolean Default: false Set to true to run the replication as an adhoc replication instead of a persistent one. This means that the replication will only last the period of the replication until the status is changed to stopped and then it will be removed automatically. It will also be removed if Sync Gateway restarts or if removed due to user action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| batch\_size                | integer Default: 200 The amount of changes to be sent in one batch of replications. Changing this is an Enterprise Edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| collections\_enabled       | boolean Default: false If true, the replicator will run with collections, and will replicate all collections, unless otherwise limited by collections\_local. If false, the replicator will only replicate the default collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| collections\_local         | Array of strings Default: \[\] Limits the set of collections replicated to those listed in this array. The replication will use all collections defined on the database if this list is empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| collections\_remote        | Array of strings or null Default: \[\] Remaps the local collection name to the one specified in this array when replicating with the remote. If only a subset of collections need remapping, elements in this array can be specified as null to preserve the local collection name. The same index is used for both collections\_remote and collections\_local, and both arrays must be the same length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| conflict\_resolution\_type | string Default: "default" Enum **Description**defaultThis will use: Timestamp based conflict resolution (often referred to as "last write wins", or LWW). Which uses a document timestamp from most recent document revisions to compare. The revision with the most recent timestamp wins. If replicating a document that was last updated/written pre upgrade to SG 4.x, the default policy for versions < 4.x will be used. localWinsThis will result in local revisions always being the winner in any conflict. remoteWinsThis will result in remote revisions always being the winner in any conflict. customThis will result in conflicts going through your own custom conflict resolver. You must provide this logic as a Javascript function in the custom\_conflict\_resolver parameter. This defines what conflict resolution policy Sync Gateway should use to apply when resolving conflicting revisions. Changing this is an Enterprise Edition only feature.                                                                                                                                                                                                                                                                                                                                                                           |
| continuous                 | boolean Default: false If true, changes will be immediately synced when they happen. This is known as a continuous replication. If false, all changes will be synced until they have been processed. The replication will then cease and not process any future changes (unless started again by the user). This is known as a one-shot replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| custom\_conflict\_resolver | string Default: "" This specifies the Javascript function to use to resolve conflicts between conflicting revisions. This **must** be used when conflict\_resolution\_type=custom. This property will be ignored when conflict\_resolution\_type is not custom. The Javascript function to provide this property should be in backticks (like the sync function). The function takes 1 parameter which is a struct that represents the conflict. This struct has 2 properties: LocalDocument \- The local document. This contains the document ID under the \_id key. RemoteDocument \- The remote document The function should return the new document's body. This can be the winning revision (for example, return conflict.LocalDocument), a new body, or nil to resolve as a delete. Example: function(conflict) {   console.log("Doc ID: "+conflict.LocalDocument.\_id);   console.log("Full remote doc: "+JSON.stringify(conflict.RemoteDocument));   return conflict.RemoteDocument; } Using complex custom\_conflict\_resolver functions can noticeably degrade performance. Use a built-in resolver whenever possible. If a document merge is being done, the \_rev and \_cv properties should not be included in the returned document body as Sync Gateway will generate new values for these. This is an Enterprise Edition only feature. |
| directionrequired          | string Enum **Description**pullchanges are pulled from the remote database pushchanges are pushed to the remote database pushAndPullchanges are both push-to and pulled-from the remote database This specifies which direction the replication will be replicating with the remote replicator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| enable\_delta\_sync        | boolean Default: false This will turn on delta-sync for the replication. In order to enable delta-sync for a replication, the database level setting delta\_sync.enabled must also be set to true. Using delta-sync is an Enterprise Edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| filter                     | string Enum **Description**Do not filter any documents. sync\_gateway/bychannelIf set, a pull replication will be limited to a specific set of channels specified by the query\_param.channels property. This defines whether to filter documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| initial\_state             | string Default: "running" Enum **Description**runningThe replication will immediately start running. stoppedThe replication configuration will be created but the replication will not start running until the user explicitly starts it. This is what state to start the replication in when creating a new replication. This allows you to control if the replication starts in a stopped start or running state. Replications prior to Sync Gateway 2.8 will run in the default state running.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| max\_backoff\_time         | integer Default: 5 Specifies the maximum time-period (in minutes) that Sync Gateway will attempt to reconnect to a lost or unreachable remote. When a disconnection happens, Sync Gateway will do an exponential backoff up to this specified value. When this value is met, it will attempt to reconnect indefinitely every max\_backoff\_time minutes. If this is set to 0, Sync Gateway will do the normal exponential backoff after the disconnect happens but then attempting 10 minutes and stop the replication. Note: this defaults to 5 minutes for replications created prior to Sync Gateway 2.8.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| purge\_on\_removal         | boolean Default: false Specifies whether to purge a document if the remote user loses access to all of the channels on the document when attempting to pull it from the remote. If false, documents will not be replicated and not be purged when the user loses access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| query\_params              | Array of strings This is a set of key/value pairs used in the query string of the replication. If filters=sync\_gateway/bychannel then this can be used to set the channels to filter by in a pull replication. To do this, set the channels key to a string array of the channels to filter by. For example: "filter":"sync\_gateway/bychannel", "query\_params": {   "channels":\["chanUser1"\] },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| remote                     | string This is the endpoint of the database for the remote Sync Gateway that is the subject of this replication's push, pull, or pushAndPull action. Typically this would include the URI, port, and database name. For example, https://localhost:4985/db.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| remote\_password           | string The password to use to authenticate with the remote. This password will be redacted in the replication config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| remote\_username           | string The username to use to authenticate with the remote.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| replication\_id            | string <= 160 This is the ID of the replication. When creating a new replication using a POST request, this will be set to a random UUID if not explicitly set. When the replication ID is specified in the URL, this must be set to the same replication ID if specifying it at all.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| run\_as                    | string This is used if you want to specify a user to run the replication as. This means that the replication will only be able to replicate what the user access to what the user has access to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| password                   | string Deprecated **This has been deprecated in favour of remote\_password.** This is the password to use to authenticate with the remote. This password will be redacted in the replication config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| username                   | string Deprecated **This has been deprecated in favour of remote\_username.** This is the username to use to authenticate with the remote.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Responses

**200** 

Updated existing configuration successfully

**201** 

Created new replication successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

put/{db}/\_replication/{replicationid}

Admin API

{protocol}://{hostname}:4985/{db}/\_replication/{replicationid}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "adhoc": false,
* "batch_size": 200,
* "collections_enabled": false,
* "collections_local": [
  * "scope1.collection1",
  * "scope1.collection3",
  * "scope1.collection6"  
],
* "collections_remote": [
  * "scope1.collectionA",
  * null,
  * "scope1.collectionF"  
],
* "conflict_resolution_type": "default",
* "continuous": false,
* "custom_conflict_resolver": "",
* "direction": "push",
* "enable_delta_sync": false,
* "filter": "sync_gateway/bychannel",
* "initial_state": "running",
* "max_backoff_time": 5,
* "purge_on_removal": false,
* "query_params": [
  * "string"  
],
* "remote": "string",
* "remote_password": "string",
* "remote_username": "string",
* "replication_id": "string",
* "run_as": "string",
* "password": "string",
* "username": "string"
}`

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Replication/operation/delete%5Fdb-%5Freplication-replicationid)Stop and delete a replication 

This will delete a replication causing it to stop and no longer exist.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired            | string Example: db1The name of the database to run the operation against.     |
| --------------------- | ----------------------------------------------------------------------------- |
| replicationidrequired | string \[ 1 .. 160 \] What replication to target based on its replication ID. |

### Responses

**200** 

Replication successfully deleted

**400** 

There was a problem with your request

**404** 

Resource could not be found

delete/{db}/\_replication/{replicationid}

Admin API

{protocol}://{hostname}:4985/{db}/\_replication/{replicationid}

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Replication/operation/head%5Fdb-%5Freplication-replicationid)Check if a replication exists 

Check if a replication exists.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired            | string Example: db1The name of the database to run the operation against.     |
| --------------------- | ----------------------------------------------------------------------------- |
| replicationidrequired | string \[ 1 .. 160 \] What replication to target based on its replication ID. |

### Responses

**200** 

Replication exists

**404** 

Replication does not exist

head/{db}/\_replication/{replicationid}

Admin API

{protocol}://{hostname}:4985/{db}/\_replication/{replicationid}

## [](#tag/Replication/operation/get%5Fdb-%5FreplicationStatus-)Get all replication statuses 

Retrieve all the replication statuses in the Sync Gateway node.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| activeOnly    | boolean Default: false Only return replications that are actively running (state=running).                |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| localOnly     | boolean Default: false Only return replications that were started on the current Sync Gateway node.       |
| includeError  | boolean Default: true Include replications that have stopped due to an error (state=error).               |
| includeConfig | boolean Default: false Include the replication configuration with each replicator status in the response. |

### Responses

**200** 

Successfully retrieved all replication statuses.

**400** 

There was a problem with your request

get/{db}/\_replicationStatus/

Admin API

{protocol}://{hostname}:4985/{db}/\_replicationStatus/

### Response samples 

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "replication_id": "string",
  * "config": {
    * "adhoc": false,
    * "batch_size": 200,
    * "collections_enabled": false,
    * "collections_local": [
      * "scope1.collection1",
      * "scope1.collection3",
      * "scope1.collection6"  
      ],
    * "collections_remote": [
      * "scope1.collectionA",
      * null,
      * "scope1.collectionF"  
      ],
    * "conflict_resolution_type": "default",
    * "continuous": false,
    * "custom_conflict_resolver": "",
    * "direction": "push",
    * "enable_delta_sync": false,
    * "filter": "sync_gateway/bychannel",
    * "initial_state": "running",
    * "max_backoff_time": 5,
    * "purge_on_removal": false,
    * "query_params": [
      * "string"  
      ],
    * "remote": "string",
    * "remote_password": "string",
    * "remote_username": "string",
    * "replication_id": "string",
    * "run_as": "string",
    * "password": "string",
    * "username": "string"  
  },
  * "status": "running",
  * "error_message": "string",
  * "docs_read": 0,
  * "docs_checked_pull": 0,
  * "docs_purged": 0,
  * "rejected_by_local": 0,
  * "last_seq_pull": "string",
  * "deltas_recv": 0,
  * "deltas_requested": 0,
  * "docs_written": 0,
  * "docs_checked_push": 0,
  * "doc_write_failures": 0,
  * "doc_write_conflicts": 0,
  * "rejected_by_remote": 0,
  * "last_seq_push": "string",
  * "deltas_sent": 0  
}
]`

## [](#tag/Replication/operation/get%5Fdb-%5FreplicationStatus-replicationid)Get replication status 

Retrieve the status of a replication.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired            | string Example: db1The name of the database to run the operation against.     |
| --------------------- | ----------------------------------------------------------------------------- |
| replicationidrequired | string \[ 1 .. 160 \] What replication to target based on its replication ID. |

##### query Parameters

| activeOnly    | boolean Default: false Only return replications that are actively running (state=running).                |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| localOnly     | boolean Default: false Only return replications that were started on the current Sync Gateway node.       |
| includeError  | boolean Default: true Include replications that have stopped due to an error (state=error).               |
| includeConfig | boolean Default: false Include the replication configuration with each replicator status in the response. |

### Responses

**200** 

Successfully retrieved replication status

**400** 

There was a problem with your request

**404** 

Could not find replication

get/{db}/\_replicationStatus/{replicationid}

Admin API

{protocol}://{hostname}:4985/{db}/\_replicationStatus/{replicationid}

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "replication_id": "string",
* "config": {
  * "adhoc": false,
  * "batch_size": 200,
  * "collections_enabled": false,
  * "collections_local": [
    * "scope1.collection1",
    * "scope1.collection3",
    * "scope1.collection6"  
  ],
  * "collections_remote": [
    * "scope1.collectionA",
    * null,
    * "scope1.collectionF"  
  ],
  * "conflict_resolution_type": "default",
  * "continuous": false,
  * "custom_conflict_resolver": "",
  * "direction": "push",
  * "enable_delta_sync": false,
  * "filter": "sync_gateway/bychannel",
  * "initial_state": "running",
  * "max_backoff_time": 5,
  * "purge_on_removal": false,
  * "query_params": [
    * "string"  
  ],
  * "remote": "string",
  * "remote_password": "string",
  * "remote_username": "string",
  * "replication_id": "string",
  * "run_as": "string",
  * "password": "string",
  * "username": "string"  
},
* "status": "running",
* "error_message": "string",
* "docs_read": 0,
* "docs_checked_pull": 0,
* "docs_purged": 0,
* "rejected_by_local": 0,
* "last_seq_pull": "string",
* "deltas_recv": 0,
* "deltas_requested": 0,
* "docs_written": 0,
* "docs_checked_push": 0,
* "doc_write_failures": 0,
* "doc_write_conflicts": 0,
* "rejected_by_remote": 0,
* "last_seq_push": "string",
* "deltas_sent": 0
}`

## [](#tag/Replication/operation/put%5Fdb-%5FreplicationStatus-replicationid)Control a replication state 

Control the replication by changing its state.

This is done through the action query parameter, which has 3 valid values:

* `start` \- starts a stopped replication
* `stop` \- stops an active replication
* `reset` \- resets the replication checkpoint to 0\. For bidirectional replication, both push and pull checkpoints are reset to 0\. The replication must be stopped to use this.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired            | string Example: db1The name of the database to run the operation against.     |
| --------------------- | ----------------------------------------------------------------------------- |
| replicationidrequired | string \[ 1 .. 160 \] What replication to target based on its replication ID. |

##### query Parameters

| actionrequired | string Enum: "start" "stop" "reset" The target state to put the replicator into. |
| -------------- | -------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully changed target state of replicator

**400** 

There was a problem with your request

**404** 

Resource could not be found

put/{db}/\_replicationStatus/{replicationid}

Admin API

{protocol}://{hostname}:4985/{db}/\_replicationStatus/{replicationid}

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "replication_id": "string",
* "config": {
  * "adhoc": false,
  * "batch_size": 200,
  * "collections_enabled": false,
  * "collections_local": [
    * "scope1.collection1",
    * "scope1.collection3",
    * "scope1.collection6"  
  ],
  * "collections_remote": [
    * "scope1.collectionA",
    * null,
    * "scope1.collectionF"  
  ],
  * "conflict_resolution_type": "default",
  * "continuous": false,
  * "custom_conflict_resolver": "",
  * "direction": "push",
  * "enable_delta_sync": false,
  * "filter": "sync_gateway/bychannel",
  * "initial_state": "running",
  * "max_backoff_time": 5,
  * "purge_on_removal": false,
  * "query_params": [
    * "string"  
  ],
  * "remote": "string",
  * "remote_password": "string",
  * "remote_username": "string",
  * "replication_id": "string",
  * "run_as": "string",
  * "password": "string",
  * "username": "string"  
},
* "status": "running",
* "error_message": "string",
* "docs_read": 0,
* "docs_checked_pull": 0,
* "docs_purged": 0,
* "rejected_by_local": 0,
* "last_seq_pull": "string",
* "deltas_recv": 0,
* "deltas_requested": 0,
* "docs_written": 0,
* "docs_checked_push": 0,
* "doc_write_failures": 0,
* "doc_write_conflicts": 0,
* "rejected_by_remote": 0,
* "last_seq_push": "string",
* "deltas_sent": 0
}`

## [](#tag/Replication/operation/head%5Fdb-%5FreplicationStatus-replicationid)Check if replication exists 

Check if a replication exists.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### path Parameters

| dbrequired            | string Example: db1The name of the database to run the operation against.     |
| --------------------- | ----------------------------------------------------------------------------- |
| replicationidrequired | string \[ 1 .. 160 \] What replication to target based on its replication ID. |

##### query Parameters

| activeOnly    | boolean Default: false Only return replications that are actively running (state=running).                |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| localOnly     | boolean Default: false Only return replications that were started on the current Sync Gateway node.       |
| includeError  | boolean Default: true Include replications that have stopped due to an error (state=error).               |
| includeConfig | boolean Default: false Include the replication configuration with each replicator status in the response. |

### Responses

**200** 

Replication exists

**400** 

There was a problem with your request

**404** 

Resource could not be found

head/{db}/\_replicationStatus/{replicationid}

Admin API

{protocol}://{hostname}:4985/{db}/\_replicationStatus/{replicationid}

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Replication/operation/get%5Fdb-%5Fblipsync)Handle incoming BLIP Sync web socket request 

This handles incoming BLIP Sync requests from either Couchbase Lite or another Sync Gateway node. The connection has to be upgradable to a websocket connection or else the request will fail.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| client | string Default: "cbl2" Enum: "cbl2" "sgr2" This is the client type that is making the BLIP Sync request. Used to control client-type specific replication behaviour. |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**101** 

Upgraded to a web socket connection

**404** 

Resource could not be found

**426** 

Cannot upgrade connection to a web socket connection

get/{db}/\_blipsync

Admin API

{protocol}://{hostname}:4985/{db}/\_blipsync

### Response samples 

* 404
* 426

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Metrics)Metrics

Get Sync Gateway statistics

## [](#tag/Metrics/operation/get%5F%5Fstats)Get memory statistics 

This will return the current Sync Gateway nodes memory statistics such as current memory usage.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Dev Ops
* External Stats Reader

### Responses

**200** 

Returned memory usage statistics

get/\_stats

Admin API

{protocol}://{hostname}:4985/\_stats

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "memstats": { }
}`

## [](#tag/Metrics/operation/get%5F%5Fexpvar)Get all Sync Gateway statistics in JSON format 

This returns a snapshot of all metrics in Sync Gateway for debugging and monitoring purposes.

This includes per database stats, replication stats, and server stats.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Dev Ops
* External Stats Reader

### Responses

**200** 

Successfully returned statistics. For details, see [JSON Metrics](stats-monitoring-json.html).

get/\_expvar

Admin API

{protocol}://{hostname}:4985/\_expvar

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "cmdline": { },
* "memstats": { },
* "cb": { },
* "mc": { },
* "syncGateway_changeCache": {
  * "maxPending": { },
  * "lag-tap-0000ms": { },
  * "lag-queue-0000ms": { },
  * "lag-total-0000ms": { },
  * "outOfOrder": { },
  * "view_queries": { }  
},
* "syncGateway_db": {
  * "channelChangesFeeds": { },
  * "channelLogAdds": { },
  * "channelLogAppends": { },
  * "channelLogCacheHits": { },
  * "channelLogRewrites": { },
  * "channelLogRewriteCollisions": { },
  * "document_gets": { },
  * "revisionCache_adds": { },
  * "revisionCache_hits": { },
  * "revisionCache_misses": { },
  * "revs_added": { },
  * "sequence_gets": { },
  * "sequence_reserves": { }  
},
* "syncgateway": {
  * "global": {
    * "resource_utilization": {
      * "admin_net_bytes_recv": 0,
      * "admin_net_bytes_sent": 0,
      * "error_count": 0,
      * "go_memstats_heapalloc": 0,
      * "go_memstats_heapidle": 0,
      * "go_memstats_heapinuse": 0,
      * "go_memstats_heapreleased": 0,
      * "go_memstats_pausetotalns": 0,
      * "go_memstats_stackinuse": 0,
      * "go_memstats_stacksys": 0,
      * "go_memstats_sys": 0,
      * "goroutines_high_watermark": 0,
      * "num_goroutines": 0,
      * "num_idle_kv_ops": 0,
      * "num_idle_query_ops": 0,
      * "process_cpu_percent_utilization": 0.1,
      * "node_cpu_percent_utilization": 0.1,
      * "process_memory_resident": 0,
      * "pub_net_bytes_recv": 0,
      * "pub_net_bytes_sent": 0,
      * "system_memory_total": 0,
      * "warn_count": 0,
      * "uptime": 0  
      }  
  },
  * "per_db": [
    * {
      * "cache": { },
      * "database": { },
      * "per_replication": { },
      * "collections": { },
      * "security": { }  
      }  
  ],
  * "per_replication": [
    * {
      * "$replication_id": {
        * "sgr_active": true,
        * "sgr_docs_checked_sent": 0,
        * "sgr_num_attachments_transferred": 0,
        * "sgr_num_attachment_bytes_transferred": 0,
        * "sgr_num_docs_failed_to_push": 0,
        * "sgr_num_docs_pushed": 0  
            }  
      }  
  ]  
}
}`

## [](#tag/Profiling)Profiling

Generate information to help debug and fine-tune Sync Gateway

## [](#tag/Profiling/operation/post%5F%5Fprofile-profilename)Create point-in-time profile 

This endpoint allows you to create a pprof snapshot of the given type.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### path Parameters

| profilenamerequired | string Enum: "heap" "block" "threadcreate" "mutex" "goroutine" The handler to use for profiling. |
| ------------------- | ------------------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| file | string This is the file to output the pprof profile at. |
| ---- | ------------------------------------------------------- |

### Responses

**200** 

Successfully created profile

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/\_profile/{profilename}

Admin API

{protocol}://{hostname}:4985/\_profile/{profilename}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "file": "string"
}`

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Profiling/operation/post%5F%5Fprofile)Start or Stop continuous CPU profiling 

This endpoint allows you to start and stop continuous CPU profiling.

To start profiling the CPU, call this endpoint and supply a file to output the pprof file to.

To stop profiling, call this endpoint but don't supply the `file` in the body.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### Request Body schema: application/json

| file | string This is the file to output the pprof profile at. |
| ---- | ------------------------------------------------------- |

### Responses

**200** 

Successfully started or stopped CPU profiling

**400** 

There was a problem with your request

post/\_profile

Admin API

{protocol}://{hostname}:4985/\_profile

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "file": "string"
}`

### Response samples 

* 400

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Profiling/operation/post%5F%5Fheap)Dump heap profile 

This endpoint will dump a pprof heap profile.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### Request Body schema: application/json

| file | string This is the file to output the pprof profile at. |
| ---- | ------------------------------------------------------- |

### Responses

**200** 

Successfully dumped heap profile

**400** 

There was a problem with your request

post/\_heap

Admin API

{protocol}://{hostname}:4985/\_heap

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "file": "string"
}`

### Response samples 

* 400

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Profiling/operation/get%5F%5Fdebug-pprof-goroutine)Get goroutine profile 

Stack traces of all current goroutines.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer If set, collect a delta profile for the given duration, instead of a snapshot. |
| ------- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

OK

get/\_debug/pprof/goroutine

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/goroutine

## [](#tag/Profiling/operation/post%5F%5Fdebug-pprof-goroutine)Get goroutine profile 

Stack traces of all current goroutines.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer If set, collect a delta profile for the given duration, instead of a snapshot. |
| ------- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

OK

post/\_debug/pprof/goroutine

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/goroutine

## [](#tag/Profiling/operation/get%5F%5Fdebug-pprof-cmdline)Get passed in command line parameters 

Gets the command line parameters that was passed in to Sync Gateway which will include the binary, flags (if any) and startup configuration.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

OK

get/\_debug/pprof/cmdline

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/cmdline

## [](#tag/Profiling/operation/post%5F%5Fdebug-pprof-cmdline)Get passed in command line parameters 

Gets the command line parameters that was passed in to Sync Gateway which will include the binary, flags (if any) and startup configuration.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

OK

post/\_debug/pprof/cmdline

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/cmdline

## [](#tag/Profiling/operation/get%5F%5Fdebug-pprof-symbol)Get symbol pprof debug information 

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

OK

get/\_debug/pprof/symbol

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/symbol

## [](#tag/Profiling/operation/post%5F%5Fdebug-pprof-symbol)Get symbol pprof debug information 

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

OK

post/\_debug/pprof/symbol

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/symbol

## [](#tag/Profiling/operation/get%5F%5Fdebug-pprof-heap)Get the heap pprof debug file 

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer If set, collect a delta profile for the given duration, instead of a snapshot. |
| ------- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

OK

get/\_debug/pprof/heap

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/heap

## [](#tag/Profiling/operation/post%5F%5Fdebug-pprof-heap)Get the heap pprof debug file 

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer If set, collect a delta profile for the given duration, instead of a snapshot. |
| ------- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

OK

post/\_debug/pprof/heap

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/heap

## [](#tag/Profiling/operation/get%5F%5Fdebug-pprof-profile)Get the profile pprof debug file 

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer If set, collect a delta profile for the given duration, instead of a snapshot. |
| ------- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

OK

get/\_debug/pprof/profile

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/profile

## [](#tag/Profiling/operation/post%5F%5Fdebug-pprof-profile)Get the profile pprof debug file 

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer If set, collect a delta profile for the given duration, instead of a snapshot. |
| ------- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

OK

post/\_debug/pprof/profile

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/profile

## [](#tag/Profiling/operation/get%5F%5Fdebug-pprof-block)Get block profile 

Returns stack traces that led to blocking on synchronization primitives.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer \>= 0 Default: 30 The amount of seconds to run the profiler for. |
| ------- | ------------------------------------------------------------------------ |

### Responses

**200** 

OK

**403** 

Forbidden

get/\_debug/pprof/block

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/block

### Response samples 

* 403

Content type

application/json

Copy

`{
* "error": "forbidden",
* "reason": "Can only run one mutex profile at a time"
}`

## [](#tag/Profiling/operation/post%5F%5Fdebug-pprof-block)Get block profile 

Returns stack traces that led to blocking on synchronization primitives.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer \>= 0 Default: 30 The amount of seconds to run the profiler for. |
| ------- | ------------------------------------------------------------------------ |

### Responses

**200** 

OK

**403** 

Forbidden

post/\_debug/pprof/block

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/block

### Response samples 

* 403

Content type

application/json

Copy

`{
* "error": "forbidden",
* "reason": "Can only run one mutex profile at a time"
}`

## [](#tag/Profiling/operation/get%5F%5Fdebug-pprof-threadcreate)Get the threadcreate pprof debug file 

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

OK

get/\_debug/pprof/threadcreate

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/threadcreate

## [](#tag/Profiling/operation/post%5F%5Fdebug-pprof-threadcreate)Get the threadcreate pprof debug file 

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

### Responses

**200** 

OK

post/\_debug/pprof/threadcreate

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/threadcreate

## [](#tag/Profiling/operation/get%5F%5Fdebug-pprof-mutex)Get mutex profile 

Returns stack traces of holders of contended mutexes.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer \>= 0 Default: 30 The amount of seconds to run the profiler for. |
| ------- | ------------------------------------------------------------------------ |

### Responses

**200** 

OK

**403** 

Forbidden

get/\_debug/pprof/mutex

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/mutex

### Response samples 

* 403

Content type

application/json

Copy

`{
* "error": "forbidden",
* "reason": "Can only run one mutex profile at a time"
}`

## [](#tag/Profiling/operation/post%5F%5Fdebug-pprof-mutex)Get mutex profile 

Returns stack traces of holders of contended mutexes.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer \>= 0 Default: 30 The amount of seconds to run the profiler for. |
| ------- | ------------------------------------------------------------------------ |

### Responses

**200** 

OK

**403** 

Forbidden

post/\_debug/pprof/mutex

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/mutex

### Response samples 

* 403

Content type

application/json

Copy

`{
* "error": "forbidden",
* "reason": "Can only run one mutex profile at a time"
}`

## [](#tag/Profiling/operation/get%5F%5Fdebug-pprof-trace)Get trace profile 

Responds with the execution trace in binary form.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer Default: 1 |
| ------- | ------------------ |

### Responses

**200** 

OK

get/\_debug/pprof/trace

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/trace

## [](#tag/Profiling/operation/post%5F%5Fdebug-pprof-trace)Get trace profile 

Responds with the execution trace in binary form.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer Default: 1 |
| ------- | ------------------ |

### Responses

**200** 

OK

post/\_debug/pprof/trace

Admin API

{protocol}://{hostname}:4985/\_debug/pprof/trace

## [](#tag/Profiling/operation/get%5F%5Fdebug-fgprof)Get fgprof profile 

A sampling Go profiler that allows you to analyze On-CPU as well as [Off-CPU](https://www.brendangregg.com/offcpuanalysis.html) (e.g. I/O) time together.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer \>= 0 Default: 30 The amount of seconds to run the profiler for. |
| ------- | ------------------------------------------------------------------------ |

### Responses

**200** 

OK

get/\_debug/fgprof

Admin API

{protocol}://{hostname}:4985/\_debug/fgprof

## [](#tag/Profiling/operation/post%5F%5Fdebug-fgprof)Get fgprof profile 

A sampling Go profiler that allows you to analyze On-CPU as well as [Off-CPU](https://www.brendangregg.com/offcpuanalysis.html) (e.g. I/O) time together.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### query Parameters

| seconds | integer \>= 0 Default: 30 The amount of seconds to run the profiler for. |
| ------- | ------------------------------------------------------------------------ |

### Responses

**200** 

OK

post/\_debug/fgprof

Admin API

{protocol}://{hostname}:4985/\_debug/fgprof

## [](#tag/Unsupported)Unsupported

Endpoints that are not supported by Sync Gateway

## [](#tag/Unsupported/operation/get%5Fkeyspace-%5Frevtree-docid)Revision tree structure in Graphviz Dot format | Unsupported 

This returns the Dot syntax of the revision tree for the document so that it can be rendered in to a PNG image using the [Graphviz CLI tool](https://www.graphviz.org/).

To use:

1. Install the Graphviz tool. Using Brew, this can be done by calling `brew install graphviz`.
2. Save the response text from this endpoint to a file (for example, `revtree.dot`).
3. Render the PNG by calling `dot -Tpng revtree.dot > revtree.png`.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

**Note: This endpoint is useful for debugging purposes only. It is not officially supported.**

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

### Responses

**200** 

Found document

**404** 

Resource could not be found

get/{keyspace}/\_revtree/{docid}

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_revtree/{docid}

### Response samples 

* 200
* 404

Content type

application/json

Copy

`"digraph graphname{\"1-d4d949b7feafc8c31215684baa45b6cd\" -> \"2-4f3f24143ea43d85a9a340ac016fdfc4\"; }"`

## [](#tag/Unsupported/operation/post%5Fdb-%5Fflush)Flush the entire database bucket | Unsupported 

**This is unsupported**

This will purge _all_ documents.

The bucket will only be flushed if the unsupported database configuration option `enable_couchbase_bucket_flush` is set.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Successfully flushed the bucket

**404** 

Resource could not be found

**503** 

The bucket does not support flush or delete

post/{db}/\_flush

Admin API

{protocol}://{hostname}:4985/{db}/\_flush

### Response samples 

* 404
* 503

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Fdump-view)Dump a view | Unsupported 

**This is unsupported**

This queries the view and outputs it as HTML.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| viewrequired | string The view to target.                                                |

### Responses

**200** 

Retrieved view successfully

**404** 

Resource could not be found

**500** 

Internal Server Error

get/{db}/\_dump/{view}

Admin API

{protocol}://{hostname}:4985/{db}/\_dump/{view}

### Response samples 

* 404
* 500

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Fview-view)Query a view on the default design document | Unsupported 

**This is unsupported**

Query a view on the default Sync Gateway design document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| viewrequired | string The view to target.                                                |

##### query Parameters

| inclusive\_end  | boolean Indicates whether the specified end key should be included in the result.                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| descending      | boolean Return documents in descending order.                                                                                                                        |
| include\_docs   | boolean Only works when using Couchbase Server 3.0 and earlier. Indicates whether to include the full content of the documents in the response.                      |
| reduce          | boolean Whether to execute a reduce function on the response or not.                                                                                                 |
| group           | boolean Group the results using the reduce function to a group or single row.                                                                                        |
| skip            | integer Skip the specified number of documents before starting to return results.                                                                                    |
| limit           | integer Return only the specified number of documents                                                                                                                |
| group\_level    | integer Specify the group level to be used.                                                                                                                          |
| startkey\_docid | string Return documents starting with the specified document identifier.                                                                                             |
| endkey\_docid   | string Stop returning records when the specified document identifier is reached.                                                                                     |
| stale           | string Enum: "ok" "update\_after" Allow the results from a stale view to be used, without triggering a rebuild of all views within the encompassing design document. |
| startkey        | string Return records starting with the specified key.                                                                                                               |
| endkey          | string Stop returning records when this key is reached.                                                                                                              |
| key             | string Return only the document that matches the specified key.                                                                                                      |
| keys            | Array of strings An array of document ID strings to filter by.                                                                                                       |

### Responses

**200** 

Returned view successfully

**403** 

Forbidden

**404** 

Resource could not be found

get/{db}/\_view/{view}

Admin API

{protocol}://{hostname}:4985/{db}/\_view/{view}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "total_rows": 0,
* "rows": [
  * {
    * "id": "string",
    * "key": { },
    * "value": { },
    * "doc": { }  
  }  
],
* "errors": [
  * {
    * "From": "string",
    * "Reason": "string"  
  }  
]
}`

## [](#tag/Unsupported/operation/get%5Fkeyspace-%5Fdumpchannel-channel)Dump all the documents in a channel | Unsupported 

**This is unsupported**

This queries a channel and displays all the document IDs and revisions that are in that channel.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| channelrequired  | string The channel to dump all the documents from.                                                                                                                                                                                                                                                                                        |

##### query Parameters

| since | string Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully got all documents in the channel

**404** 

Resource could not be found

get/{keyspace}/\_dumpchannel/{channel}

Admin API

{protocol}://{hostname}:4985/{keyspace}/\_dumpchannel/{channel}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/post%5Fdb-%5Frepair)Disabled endpoint 

This endpoint is disabled.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**500** 

This endpoint is disabled

post/{db}/\_repair

Admin API

{protocol}://{hostname}:4985/{db}/\_repair

## [](#tag/Unsupported/operation/get%5Fdb-%5Fdesign-ddoc)Get views of a design document | Unsupported 

**This is unsupported**

Query a design document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |

### Responses

**200** 

Successfully returned design document.

**403** 

Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one.

**404** 

Resource could not be found

get/{db}/\_design/{ddoc}

Admin API

{protocol}://{hostname}:4985/{db}/\_design/{ddoc}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "language": "string",
* "views": {
  * "viewname1": {
    * "map": "string",
    * "reduce": "string"  
  },
  * "viewname2": {
    * "map": "string",
    * "reduce": "string"  
  }  
},
* "options": {
  * "local_seq": "string",
  * "include_design": "string",
  * "raw": "string",
  * "index_xattr_on_deleted_docs": "string"  
}
}`

## [](#tag/Unsupported/operation/put%5Fdb-%5Fdesign-ddoc)Update views of a design document | Unsupported 

**This is unsupported**

Update the views of a design document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |

##### Request Body schema: application/json

| language | string |
| -------- | ------ |
| views    | object |
| options  | object |

### Responses

**200** 

Design document changes successfully

**403** 

Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one.

**404** 

Resource could not be found

put/{db}/\_design/{ddoc}

Admin API

{protocol}://{hostname}:4985/{db}/\_design/{ddoc}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "language": "string",
* "views": {
  * "viewname1": {
    * "map": "string",
    * "reduce": "string"  
  },
  * "viewname2": {
    * "map": "string",
    * "reduce": "string"  
  }  
},
* "options": {
  * "local_seq": "string",
  * "include_design": "string",
  * "raw": "string",
  * "index_xattr_on_deleted_docs": "string"  
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

## [](#tag/Unsupported/operation/delete%5Fdb-%5Fdesign-ddoc)Delete a design document | Unsupported 

**This is unsupported**

Delete a design document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |

### Responses

**200** 

Design document deleted successfully

**403** 

Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one.

**404** 

Resource could not be found

delete/{db}/\_design/{ddoc}

Admin API

{protocol}://{hostname}:4985/{db}/\_design/{ddoc}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/head%5Fdb-%5Fdesign-ddoc)Check if view of design document exists | Unsupported 

**This is unsupported**

Check if a design document can be queried.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |

### Responses

**200** 

Design document exists

**403** 

Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one.

**404** 

Resource could not be found

head/{db}/\_design/{ddoc}

Admin API

{protocol}://{hostname}:4985/{db}/\_design/{ddoc}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Fdesign-ddoc-%5Fview-view)Query a view on a design document | Unsupported 

**This is unsupported**

Query a view on a design document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |
| viewrequired | string The view to target.                                                |

##### query Parameters

| inclusive\_end  | boolean Indicates whether the specified end key should be included in the result.                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| descending      | boolean Return documents in descending order.                                                                                                                        |
| include\_docs   | boolean Only works when using Couchbase Server 3.0 and earlier. Indicates whether to include the full content of the documents in the response.                      |
| reduce          | boolean Whether to execute a reduce function on the response or not.                                                                                                 |
| group           | boolean Group the results using the reduce function to a group or single row.                                                                                        |
| skip            | integer Skip the specified number of documents before starting to return results.                                                                                    |
| limit           | integer Return only the specified number of documents                                                                                                                |
| group\_level    | integer Specify the group level to be used.                                                                                                                          |
| startkey\_docid | string Return documents starting with the specified document identifier.                                                                                             |
| endkey\_docid   | string Stop returning records when the specified document identifier is reached.                                                                                     |
| stale           | string Enum: "ok" "update\_after" Allow the results from a stale view to be used, without triggering a rebuild of all views within the encompassing design document. |
| startkey        | string Return records starting with the specified key.                                                                                                               |
| endkey          | string Stop returning records when this key is reached.                                                                                                              |
| key             | string Return only the document that matches the specified key.                                                                                                      |
| keys            | Array of strings An array of document ID strings to filter by.                                                                                                       |

### Responses

**200** 

Returned view successfully

**403** 

Forbidden

**404** 

Resource could not be found

get/{db}/\_design/{ddoc}/\_view/{view}

Admin API

{protocol}://{hostname}:4985/{db}/\_design/{ddoc}/\_view/{view}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "total_rows": 0,
* "rows": [
  * {
    * "id": "string",
    * "key": { },
    * "value": { },
    * "doc": { }  
  }  
],
* "errors": [
  * {
    * "From": "string",
    * "Reason": "string"  
  }  
]
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Foidc%5Ftesting-.well-known-openid-configuration)OpenID Connect mock provider 

Mock an OpenID Connect provider response for testing purposes. This returns a response that is the same structure as what Sync Gateway expects from an OIDC provider after initiating OIDC authentication.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Successfully generated OpenID Connect provider mock response. 

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

get/{db}/\_oidc\_testing/.well-known/openid-configuration

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_testing/.well-known/openid-configuration

### Response samples 

* 200
* 404

Content type

application/json

Copy

`{
* "issuer": "string",
* "authorization_endpoint": "string",
* "token_endpoint": "string",
* "jwks_uri": "string",
* "userinfo_endpoint": "string",
* "id_token_signing_alg_values_supported": "string",
* "response_types_supported": "string",
* "subject_types_supported": "string",
* "scopes_supported": "string",
* "claims_supported": "string",
* "token_endpoint_auth_methods_supported": "string"
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Foidc%5Ftesting-authorize)OpenID Connect mock login page 

Show a mock OpenID Connect login page for the client to log in to.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| scoperequired | string The OpenID Connect authentication scope. |
| ------------- | ----------------------------------------------- |

### Responses

**200** 

OK

**400** 

A validation error occurred with the scope.

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

**500** 

An error occurred.

get/{db}/\_oidc\_testing/authorize

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_testing/authorize

### Response samples 

* 400
* 404
* 500

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Unsupported/operation/post%5Fdb-%5Foidc%5Ftesting-authorize)OpenID Connect mock login page 

Show a mock OpenID Connect login page for the client to log in to.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| scoperequired | string The OpenID Connect authentication scope. |
| ------------- | ----------------------------------------------- |

### Responses

**200** 

OK

**400** 

A validation error occurred with the scope.

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

**500** 

An error occurred.

post/{db}/\_oidc\_testing/authorize

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_testing/authorize

### Response samples 

* 400
* 404
* 500

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Unsupported/operation/post%5Fdb-%5Foidc%5Ftesting-token)OpenID Connect mock token 

Return a mock OpenID Connect token for the OIDC authentication flow.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

| grant\_typerequired | string The grant type of the token to request. Can either be an authorization\_code or refresh\_token. |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| code                | string **grant\_type=authorization\_code only**: The OpenID Connect authentication token.              |
| refresh\_token      | string **grant\_type=refresh\_token only**: The OpenID Connect refresh token.                          |

### Responses

**200** 

Properties expected back from an OpenID Connect provider after successful authentication

**400** 

Invalid token provided

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

post/{db}/\_oidc\_testing/token

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_testing/token

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "grant_type": "string",
* "code": "string",
* "refresh_token": "string"
}`

### Response samples 

* 200
* 404

Content type

application/json

Copy

`{
* "access_token": "string",
* "token_type": "string",
* "refresh_token": "string",
* "expires_in": "string",
* "id_token": "string"
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Foidc%5Ftesting-certs)OpenID Connect public certificates for signing keys 

Return a mock OpenID Connect public key to be used as signing keys.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Returned public key successfully

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

**500** 

An error occurred while getting the private RSA key

get/{db}/\_oidc\_testing/certs

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_testing/certs

### Response samples 

* 200
* 404
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "keys": [
  * {
    * "Key": { },
    * "KeyID": "string",
    * "Use": "string",
    * "Certificates": [
      * { }  
      ],
    * "Algorithm": "string"  
  }  
]
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Foidc%5Ftesting-authenticate)OpenID Connect mock login page handler 

Used to handle the login page displayed for the `GET /{db}/_oidc_testing/authorize` endpoint.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| redirect\_uri                  | string The Sync Gateway OpenID Connect callback URL. |
| ------------------------------ | ---------------------------------------------------- |
| scoperequired                  | string The OpenID Connect authentication scope.      |
| usernamerequired               | string                                               |
| tokenttlrequired               | integer                                              |
| identity-token-formatsrequired | string                                               |
| authenticatedrequired          | string                                               |

### Responses

**302** 

Redirecting to Sync Gateway OpenID Connect callback URL

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

get/{db}/\_oidc\_testing/authenticate

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_testing/authenticate

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/post%5Fdb-%5Foidc%5Ftesting-authenticate)OpenID Connect mock login page handler 

Used to handle the login page displayed for the `GET /{db}/_oidc_testing/authorize` endpoint.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| redirect\_uri | string The Sync Gateway OpenID Connect callback URL. |
| ------------- | ---------------------------------------------------- |
| scoperequired | string The OpenID Connect authentication scope.      |

##### Request Body schema: application/json

Properties passed from the OpenID Connect mock login page to the handler

| usernamerequired               | string |
| ------------------------------ | ------ |
| tokenttlrequired               | string |
| identity-token-formatsrequired | string |
| authenticatedrequired          | string |

### Responses

**302** 

Redirecting to Sync Gateway OpenID Connect callback URL

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

post/{db}/\_oidc\_testing/authenticate

Admin API

{protocol}://{hostname}:4985/{db}/\_oidc\_testing/authenticate

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "username": "string",
* "tokenttl": "string",
* "identity-token-formats": "string",
* "authenticated": "string"
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