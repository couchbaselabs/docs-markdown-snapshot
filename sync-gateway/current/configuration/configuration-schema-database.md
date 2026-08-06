---
title: Database Configuration
description: Using Sync Gateway's Admin REST API to configure and manage databases
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/configuration/pages/configuration-schema-database.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway:configuration:configuration-schema-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/configuration/configuration-schema-database.html)

# Database Configuration

> Using Sync Gateway's Admin REST API to configure and manage databases  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | [Database](configuration-schema-database.md) | [Database Security](configuration-schema-db-security.md) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

From _Sync Gateway_ 3.0 you can use the Admin REST API to provision persistent configuration changes. This content introduces the [PUT /{db}/](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/put%5Fdb-) and [POST /{db}/\_config](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig) endpoints for convenience — see [Database Configuration](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) for a full description of the endpoints available.

## [](#lbl-buckets-scopes-collections)Understanding Buckets, Scopes, and Collections

Couchbase Server, Sync Gateway, and Couchbase Lite all organize data using the same three-level hierarchy: bucket, scope, and collection. A collection holds documents. A scope groups related collections. A bucket holds all the scopes for a dataset.

[Table 1](#tbl-bucket-scope-collection) maps the terms across all three.

__Table 1\. Bucket, scope, and collection mapping across Couchbase Server, Sync Gateway, and Couchbase Lite__
| Level          | Couchbase Server                                               | Sync Gateway database config                                                                                                            | Couchbase Lite                                            |
| -------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Top container  | A bucket, created and managed on the Couchbase Server cluster. | The bucket property names one existing Couchbase Server bucket. Each Sync Gateway database maps to exactly one Couchbase Server bucket. | A database, created locally on the mobile or edge device. |
| Namespace      | A scope, created within a bucket.                              | A key under the scopes object in the database config.                                                                                   | A scope, created within a Couchbase Lite database.        |
| Data container | A collection, created within a scope.                          | A key under scopes.<scope-name>.collections in the database config.                                                                     | A collection, created within a Couchbase Lite scope.      |

### [](#defaults)Defaults

If you don't specify a custom scope and collection in your database configuration, the database will use the default scope and collection.

### [](#name-matching-across-tiers)Name matching across tiers

Scope and collection names must match exactly, character for character, across all three tiers. For example, a Couchbase Lite replicator configured to sync the `airline` collection in the `inventory` scope only succeeds against a Sync Gateway database that defines an `airline` collection inside an `inventory` scope in its `scopes` config.

The scope and collection must already exist on the Couchbase Server bucket before you reference them in the Sync Gateway database config. Sync Gateway does not create scopes or collections on Couchbase Server; you must create them there first.

If a mismatch exists at any tier, replication does not start and Couchbase Lite logs an error.

### [](#the-system-collection)The system collection

From Sync Gateway 4.1, you can opt in to using a reserved system collection, `_system._mobile`, to store Sync Gateway internal metadata separately from user application data. This collection is owned by Sync Gateway and is not a user-configurable scope or collection.

Opting in migrates Sync Gateway internal metadata from the default collection (`_default._default`) to `_system._mobile`. This isolates Sync Gateway system documents from your application data, prevents metadata from appearing in the Capella UI alongside user documents, and reduces the risk of metadata being processed by eventing functions or SQL++ queries.

See [Migrate Metadata to System Collection](../migrate-metadata-system-collection.md) for details.

### [](#scope-and-collection-limits)Scope and collection limits

You can define:

* 1 custom scope per database
* 1000 custom collections across the cluster

For the full set of configuration options, including default-scope and default-collection variants, worked JSON examples, and sync/import filter functions, see [Scopes and Collections Configuration for Sync Gateway](scopes-and-collections-config.md).

## [](#lbl-create-db)Create a new Sync Gateway database

For complete endpoint details, see [PUT /{db}/](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/put%5Fdb-).

### [](#example)Example

Example 1\. Create database

This example creates a new Sync Gateway database.

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/traveldb/' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \ (2)
--header 'Content-Type: application/json' \
--data '{
"bucket": "todo", (3)
"index": {"num_replicas": 0}
}'
```

```http
PUT /traveldb/ HTTP/1.1 (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk (2)
Content-Type: application/json
Content-Length: 44

{
"bucket": "todo", (3)
"index": {"num_replicas": 0}
}
```

| **1** | Create a Sync Gateway database called traveldb                                          |
| ----- | --------------------------------------------------------------------------------------- |
| **2** | Use Basic Authentication to authenticate against an existing Couchbase Server RBAC user |
| **3** | Point to the Couchbase Server bucket called todo                                        |

## [](#lbl-configure-db)Update database configuration

For complete endpoint details, see [POST /{db}/\_config](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig).

### [](#example-2)Example

Example 2\. Configure database

This example configures an existing Sync Gateway database.

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/traveldb/_config' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \ (2)
--header 'Content-Type: application/json' \
--data '{
  "enable_shared_bucket_access": true,
  "import_docs": true
}' (3)
```

```http
PUT /traveldb/_config HTTP/1.1  (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk  (2)
Content-Type: application/json
Content-Length: 120

{
"enable_shared_bucket_access": true,
"import_docs": true
} (3)
```

| **1** | Configure (\_config) a Sync Gateway database called traveldb                            |
| ----- | --------------------------------------------------------------------------------------- |
| **2** | Use Basic Authentication to authenticate against an existing Couchbase Server RBAC user |
| **3** | Toggle a couple of database properties                                                  |

## [](#DatabaseConfig)Schema

This section shows Sync Gateway's database configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through the [Database Configuration](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) endpoints.


{
   [allow_empty_password](#allow%5Fempty%5Fpassword): false,
   [bucket](#bucket): "The database name",
   [bucket_op_timeout_ms](#bucket%5Fop%5Ftimeout%5Fms): 0,
   [cacertpath](#cacertpath): "string",
   cache: {
      [channel_cache](#cache-channel%5Fcache): {
         [compact_high_watermark_pct](#cache-channel%5Fcache-compact%5Fhigh%5Fwatermark%5Fpct): 80,
         [compact_low_watermark_pct](#cache-channel%5Fcache-compact%5Flow%5Fwatermark%5Fpct): 60,
         [expiry_seconds](#cache-channel%5Fcache-expiry%5Fseconds): 60,
         [max_length](#cache-channel%5Fcache-max%5Flength): 500,
         [max_num_pending](#cache-channel%5Fcache-max%5Fnum%5Fpending): 10000,
         [max_number](#cache-channel%5Fcache-max%5Fnumber): 50000,
         [max_wait_pending](#cache-channel%5Fcache-max%5Fwait%5Fpending): 5000,
         [max_wait_skipped](#cache-channel%5Fcache-max%5Fwait%5Fskipped): 3600000,
         [min_length](#cache-channel%5Fcache-min%5Flength): 50
      },
      [rev_cache](#cache-rev%5Fcache): {
         [insert_on_write](#cache-rev%5Fcache-insert%5Fon%5Fwrite): false,
         [max_memory_count_mb](#cache-rev%5Fcache-max%5Fmemory%5Fcount%5Fmb): 0,
         [shard_count](#cache-rev%5Fcache-shard%5Fcount): 16,
         [size](#cache-rev%5Fcache-size): 5000
      }
   },
   [certpath](#certpath): "string",
   [changes_request_plus](#changes%5Frequest%5Fplus): false,
   [client_partition_window_secs](#client%5Fpartition%5Fwindow%5Fsecs): 2592000,
   [compact_interval_days](#compact%5Finterval%5Fdays): 1,
   cors: {
      [headers](#cors-headers): ["string"...],
      [login_origin](#cors-login%5Forigin): ["string"...],
      [max_age](#cors-max%5Fage): 0,
      [origin](#cors-origin): ["string"...]
   },
   [delta_sync](#delta%5Fsync): {
      [enabled](#delta%5Fsync-enabled): false,
      [rev_max_age_seconds](#delta%5Fsync-rev%5Fmax%5Fage%5Fseconds): 86400
   },
   [disable_password_auth](#disable%5Fpassword%5Fauth): false,
   [disable_public_all_docs](#disable%5Fpublic%5Fall%5Fdocs): false,
   [event_handlers](#event%5Fhandlers): {
      [db_state_changed](#event%5Fhandlers-db%5Fstate%5Fchanged): {
         [filter](#event%5Fhandlers-db%5Fstate%5Fchanged-filter): "string",
         [handler](#event%5Fhandlers-db%5Fstate%5Fchanged-handler): "string",
         [timeout](#event%5Fhandlers-db%5Fstate%5Fchanged-timeout): 0,
         [url](#event%5Fhandlers-db%5Fstate%5Fchanged-url): "string"
      },
      document_changed: {
         [filter](#event%5Fhandlers-document%5Fchanged-filter): "string",
         [handler](#event%5Fhandlers-document%5Fchanged-handler): "string",
         [options](#event%5Fhandlers-document%5Fchanged-options): {
            [winning_rev_only](#event%5Fhandlers-document%5Fchanged-options-winning%5Frev%5Fonly): false
         },
         [timeout](#event%5Fhandlers-document%5Fchanged-timeout): 0,
         [url](#event%5Fhandlers-document%5Fchanged-url): "string"
      },
      [max_processes](#event%5Fhandlers-max%5Fprocesses): "string",
      [wait_for_process](#event%5Fhandlers-wait%5Ffor%5Fprocess): "string"
   },
   [guest](#guest): {
      [admin_channels](#guest-admin%5Fchannels): ["string"...],
      [admin_roles](#guest-admin%5Froles): ["string"...],
      [all_channels](#guest-all%5Fchannels): ["string"...],
      [collection_access](#guest-collection%5Faccess): {
         [{scopename...}](#guest-collection%5Faccess-{scopename}): {
            [{collectionname...}](#guest-collection%5Faccess-{scopename}-{collectionname}): {
               [admin_channels](#guest-collection%5Faccess-{scopename}-{collectionname}-admin%5Fchannels): ["string"...],
               [all_channels](#guest-collection%5Faccess-{scopename}-{collectionname}-all%5Fchannels): ["string"...],
               [jwt_channels](#guest-collection%5Faccess-{scopename}-{collectionname}-jwt%5Fchannels): ["string"...],
               [jwt_last_updated](#guest-collection%5Faccess-{scopename}-{collectionname}-jwt%5Flast%5Fupdated): "string"
            }
         }
      },
      [disabled](#guest-disabled): false,
      [email](#guest-email): "string",
      [jwt_channels](#guest-jwt%5Fchannels): ["string"...],
      [jwt_issuer](#guest-jwt%5Fissuer): "string",
      [jwt_last_updated](#guest-jwt%5Flast%5Fupdated): "string",
      [jwt_roles](#guest-jwt%5Froles): ["string"...],
      [name](#guest-name): "string",
      [password](#guest-password): "string",
      [roles](#guest-roles): ["string"...]
   },
   [import_backup_old_rev](#import%5Fbackup%5Fold%5Frev): false,
   [import_docs](#import%5Fdocs): true,
   [import_filter](#import%5Ffilter): "function(doc) { if (doc.type != 'mobile') { return false; } return true; }",
   [import_partitions](#import%5Fpartitions): 16,
   [index](#index): {
      [num_partitions](#index-num%5Fpartitions): 1,
      [num_replicas](#index-num%5Freplicas): 1
   },
   [javascript_timeout_secs](#javascript%5Ftimeout%5Fsecs): 60,
   [keypath](#keypath): "string",
   [kv_tls_port](#kv%5Ftls%5Fport): 11207,
   [local_doc_expiry_secs](#local%5Fdoc%5Fexpiry%5Fsecs): 7776000,
   [local_jwt](#local%5Fjwt): {
      [{providername...}](#local%5Fjwt-{providername}): {
         [algorithms](#local%5Fjwt-{providername}-algorithms): ["string"...],
         [channels_claim](#local%5Fjwt-{providername}-channels%5Fclaim): "string",
         [client_id](#local%5Fjwt-{providername}-client%5Fid): "string",
         [disable_session](#local%5Fjwt-{providername}-disable%5Fsession): true,
         [issuer](#local%5Fjwt-{providername}-issuer): "string",
         [keys](#local%5Fjwt-{providername}-keys): [
            [alg](#local%5Fjwt-{providername}-keys-alg): "string",
            [crv](#local%5Fjwt-{providername}-keys-crv): "string",
            [e](#local%5Fjwt-{providername}-keys-e): "string",
            [kid](#local%5Fjwt-{providername}-keys-kid): "string",
            [kty](#local%5Fjwt-{providername}-keys-kty): "string",
            [n](#local%5Fjwt-{providername}-keys-n): "string",
            [use](#local%5Fjwt-{providername}-keys-use): "string",
            [x](#local%5Fjwt-{providername}-keys-x): "string",
            [y](#local%5Fjwt-{providername}-keys-y): "string"
         ],
         [register](#local%5Fjwt-{providername}-register): true,
         [roles_claim](#local%5Fjwt-{providername}-roles%5Fclaim): "string",
         [user_prefix](#local%5Fjwt-{providername}-user%5Fprefix): "string",
         [username_claim](#local%5Fjwt-{providername}-username%5Fclaim): "string"
      }
   },
   [logging](#logging): {
      [audit](#logging-audit): {
         [disabled_roles](#logging-audit-disabled%5Froles): [
            [domain](#logging-audit-disabled%5Froles-domain): "string",
            [name](#logging-audit-disabled%5Froles-name): "string"
         ],
         [disabled_users](#logging-audit-disabled%5Fusers): [
            [domain](#logging-audit-disabled%5Fusers-domain): "string",
            [name](#logging-audit-disabled%5Fusers-name): "string"
         ],
         [enabled](#logging-audit-enabled): false,
         [enabled_events](#logging-audit-enabled%5Fevents): [0...]
      },
      [console](#logging-console): {
         [log_keys](#logging-console-log%5Fkeys): ["string"...],
         [log_level](#logging-console-log%5Flevel): "debug"
      }
   },
   [max_concurrent_query_ops](#max%5Fconcurrent%5Fquery%5Fops): 1000,
   [name](#name): "string",
   [offline](#offline): false,
   [oidc](#oidc): {
      [default_provider](#oidc-default%5Fprovider): "string",
      [providers](#oidc-providers): {
         [{providername...}](#oidc-providers-{providername}): {
            [InsecureSkipVerify](#oidc-providers-{providername}-InsecureSkipVerify): false,
            [IsDefault](#oidc-providers-{providername}-IsDefault): true,
            [Name](#oidc-providers-{providername}-Name): "string",
            [allow_unsigned_provider_tokens](#oidc-providers-{providername}-allow%5Funsigned%5Fprovider%5Ftokens): true,
            [callback_url](#oidc-providers-{providername}-callback%5Furl): "string",
            [channels_claim](#oidc-providers-{providername}-channels%5Fclaim): "string",
            [client_id](#oidc-providers-{providername}-client%5Fid): "string",
            [disable_callback_state](#oidc-providers-{providername}-disable%5Fcallback%5Fstate): false,
            [disable_cfg_validation](#oidc-providers-{providername}-disable%5Fcfg%5Fvalidation): false,
            [disable_session](#oidc-providers-{providername}-disable%5Fsession): true,
            [discovery_url](#oidc-providers-{providername}-discovery%5Furl): "string",
            [include_access](#oidc-providers-{providername}-include%5Faccess): true,
            [issuer](#oidc-providers-{providername}-issuer): "string",
            [register](#oidc-providers-{providername}-register): true,
            [roles_claim](#oidc-providers-{providername}-roles%5Fclaim): "string",
            [scope](#oidc-providers-{providername}-scope): ["string"...],
            [user_prefix](#oidc-providers-{providername}-user%5Fprefix): "string",
            [username_claim](#oidc-providers-{providername}-username%5Fclaim): "string",
            [validation_key](#oidc-providers-{providername}-validation%5Fkey): "string"
         }
      }
   },
   [old_rev_expiry_seconds](#old%5Frev%5Fexpiry%5Fseconds): 300,
   [password](#password): "string",
   [query_pagination_limit](#query%5Fpagination%5Flimit): 5000,
   replications: {
      [replication_id](#replications-replication%5Fid): {
         [adhoc](#replications-replication%5Fid-adhoc): false,
         [batch_size](#replications-replication%5Fid-batch%5Fsize): 200,
         [collections_enabled](#replications-replication%5Fid-collections%5Fenabled): false,
         [collections_local](#replications-replication%5Fid-collections%5Flocal): ["string"...],
         [collections_remote](#replications-replication%5Fid-collections%5Fremote): ["string"...],
         [conflict_resolution_type](#replications-replication%5Fid-conflict%5Fresolution%5Ftype): "default",
         [continuous](#replications-replication%5Fid-continuous): false,
         [custom_conflict_resolver](#replications-replication%5Fid-custom%5Fconflict%5Fresolver): "",
         [direction](#replications-replication%5Fid-direction): "string",
         [enable_delta_sync](#replications-replication%5Fid-enable%5Fdelta%5Fsync): false,
         [filter](#replications-replication%5Fid-filter): "string",
         [initial_state](#replications-replication%5Fid-initial%5Fstate): "running",
         [max_backoff_time](#replications-replication%5Fid-max%5Fbackoff%5Ftime): 5,
         [purge_on_removal](#replications-replication%5Fid-purge%5Fon%5Fremoval): false,
         [query_params](#replications-replication%5Fid-query%5Fparams): ["string"...],
         [remote](#replications-replication%5Fid-remote): "string",
         [remote_password](#replications-replication%5Fid-remote%5Fpassword): "string",
         [remote_username](#replications-replication%5Fid-remote%5Fusername): "string",
         [replication_id](#replications-replication%5Fid-replication%5Fid): "string",
         [run_as](#replications-replication%5Fid-run%5Fas): "string"
      }
   },
   [revs_limit](#revs%5Flimit): 50,
   roles: {
      [{rolename...}](#roles-{rolename}): {
         [admin_channels](#roles-{rolename}-admin%5Fchannels): ["string"...],
         [all_channels](#roles-{rolename}-all%5Fchannels): ["string"...],
         [collection_access](#roles-{rolename}-collection%5Faccess): {
            [{scopename...}](#roles-{rolename}-collection%5Faccess-{scopename}): {
               [{collectionname...}](#roles-{rolename}-collection%5Faccess-{scopename}-{collectionname}): {
                  [admin_channels](#roles-{rolename}-collection%5Faccess-{scopename}-{collectionname}-admin%5Fchannels): ["string"...],
                  [all_channels](#roles-{rolename}-collection%5Faccess-{scopename}-{collectionname}-all%5Fchannels): ["string"...],
                  [jwt_channels](#roles-{rolename}-collection%5Faccess-{scopename}-{collectionname}-jwt%5Fchannels): ["string"...],
                  [jwt_last_updated](#roles-{rolename}-collection%5Faccess-{scopename}-{collectionname}-jwt%5Flast%5Fupdated): "string"
               }
            }
         },
         [name](#roles-{rolename}-name): "string"
      }
   },
   [scopes](#scopes): {
      [{scopename...}](#scopes-{scopename}): {
         [collections](#scopes-{scopename}-collections): {
            [{collectionname...}](#scopes-{scopename}-collections-{collectionname}): {
               [import_filter](#scopes-{scopename}-collections-{collectionname}-import%5Ffilter): "function(doc) { if (doc.type != 'mobile') { return false; } return true; }",
               [sync](#scopes-{scopename}-collections-{collectionname}-sync): "function(doc){channel("collection name");}"
            }
         }
      }
   },
   [send_www_authenticate_header](#send%5Fwww%5Fauthenticate%5Fheader): true,
   [serve_insecure_attachment_types](#serve%5Finsecure%5Fattachment%5Ftypes): false,
   [server](#server): "string",
   [session_cookie_http_only](#session%5Fcookie%5Fhttp%5Fonly): false,
   [session_cookie_name](#session%5Fcookie%5Fname): "string",
   [session_cookie_secure](#session%5Fcookie%5Fsecure): true,
   [sgreplicate_enabled](#sgreplicate%5Fenabled): true,
   [sgreplicate_websocket_heartbeat_secs](#sgreplicate%5Fwebsocket%5Fheartbeat%5Fsecs): 300,
   [slow_query_warning_threshold](#slow%5Fquery%5Fwarning%5Fthreshold): 500,
   [store_legacy_revtree_data](#store%5Flegacy%5Frevtree%5Fdata): true,
   [suspendable](#suspendable): false,
   [sync](#sync): "function(doc){channel(doc.channels);}",
   [unsupported](#unsupported): {
      api_endpoints: {
         [enable_couchbase_bucket_flush](#unsupported-api%5Fendpoints-enable%5Fcouchbase%5Fbucket%5Fflush): true
      },
      [dcp_read_buffer](#unsupported-dcp%5Fread%5Fbuffer): 0,
      [force_api_forbidden_errors](#unsupported-force%5Fapi%5Fforbidden%5Ferrors): true,
      [guest_read_only](#unsupported-guest%5Fread%5Fonly): true,
      [kv_buffer](#unsupported-kv%5Fbuffer): 0,
      oidc_test_provider: {
         [enabled](#unsupported-oidc%5Ftest%5Fprovider-enabled): true
      },
      [oidc_tls_skip_verify](#unsupported-oidc%5Ftls%5Fskip%5Fverify): true,
      [remote_config_tls_skip_verify](#unsupported-remote%5Fconfig%5Ftls%5Fskip%5Fverify): true,
      [resync_partitions](#unsupported-resync%5Fpartitions): 0,
      [same_site_cookie](#unsupported-same%5Fsite%5Fcookie): "string",
      [sgr_tls_skip_verify](#unsupported-sgr%5Ftls%5Fskip%5Fverify): true,
      user_views: {
         [enabled](#unsupported-user%5Fviews-enabled): true
      },
      warning_thresholds: {
         [access_and_role_grants_per_doc](#unsupported-warning%5Fthresholds-access%5Fand%5Frole%5Fgrants%5Fper%5Fdoc): 0,
         [channel_name_size](#unsupported-warning%5Fthresholds-channel%5Fname%5Fsize): 0,
         [channels_per_doc](#unsupported-warning%5Fthresholds-channels%5Fper%5Fdoc): 0,
         [channels_per_user](#unsupported-warning%5Fthresholds-channels%5Fper%5Fuser): 0,
         [xattr_size_bytes](#unsupported-warning%5Fthresholds-xattr%5Fsize%5Fbytes): 0
      }
   },
   [use_views](#use%5Fviews): false,
   [user_xattr_key](#user%5Fxattr%5Fkey): "string",
   [username](#username): "string",
   users: {
      [{username...}](#users-{username}): {
         [admin_channels](#users-{username}-admin%5Fchannels): ["string"...],
         [admin_roles](#users-{username}-admin%5Froles): ["string"...],
         [all_channels](#users-{username}-all%5Fchannels): ["string"...],
         [collection_access](#users-{username}-collection%5Faccess): {
            [{scopename...}](#users-{username}-collection%5Faccess-{scopename}): {
               [{collectionname...}](#users-{username}-collection%5Faccess-{scopename}-{collectionname}): {
                  [admin_channels](#users-{username}-collection%5Faccess-{scopename}-{collectionname}-admin%5Fchannels): ["string"...],
                  [all_channels](#users-{username}-collection%5Faccess-{scopename}-{collectionname}-all%5Fchannels): ["string"...],
                  [jwt_channels](#users-{username}-collection%5Faccess-{scopename}-{collectionname}-jwt%5Fchannels): ["string"...],
                  [jwt_last_updated](#users-{username}-collection%5Faccess-{scopename}-{collectionname}-jwt%5Flast%5Fupdated): "string"
               }
            }
         },
         [disabled](#users-{username}-disabled): false,
         [email](#users-{username}-email): "string",
         [jwt_channels](#users-{username}-jwt%5Fchannels): ["string"...],
         [jwt_issuer](#users-{username}-jwt%5Fissuer): "string",
         [jwt_last_updated](#users-{username}-jwt%5Flast%5Fupdated): "string",
         [jwt_roles](#users-{username}-jwt%5Froles): ["string"...],
         [name](#users-{username}-name): "string",
         [password](#users-{username}-password): "string",
         [roles](#users-{username}-roles): ["string"...]
      }
   },
   [view_query_timeout_secs](#view%5Fquery%5Ftimeout%5Fsecs): 75
}

#### `allow_empty_password`

Type

boolean

Description

This controls whether users that are created can have an empty password or not.

#### `bucket`

Type

string

Default

The database name

Description

The Couchbase Server backing bucket for the database.

#### `bucket_op_timeout_ms`

Type

number

Description

This is the amount of milliseconds should pass before a bucket operation times out. An error will be returned if the bucket operation times out saying: `operation timed out`.

#### `cacertpath`

Type

string

Description

The root CA cert path for X.509 bucket authentication.

#### `cache.channel_cache`

Type

object

Description

The channel cache config settings.

#### `cache.channel_cache.compact_high_watermark_pct`

Type

integer

Default

80

Description

The trigger value for starting the channel cache eviction process.

Specify this as a percentage which will be the percentage used on \`max\_number).

When the cache size, determined by `max_number`, reaches the high watermark, the eviction process iterates through the cache, removing inactive channels.

#### `cache.channel_cache.compact_low_watermark_pct`

Type

integer

Default

60

Description

The trigger value for stopping the channel cache eviction process.

Specify this as a percentage which will be the percentage used on \`max\_number).

When the cache size, determined by `max_number` returns to a value lower than the percentage of it set here, the cache eviction process is stopped.

#### `cache.channel_cache.expiry_seconds`

Type

integer

Default

60

Description

The amount of time (in seconds) to keep entries in the cache beyond the minimum retained.

#### `cache.channel_cache.max_length`

Type

integer

Default

500

Description

The maximum number of entries to maintain in the cache per channel.

#### `cache.channel_cache.max_num_pending`

Type

integer

Default

10000

Description

The maximum number of pending sequences before skipping sequences.

#### `cache.channel_cache.max_number`

Type

integer

Default

50000

Description

The maximum number of channel caches which can exist at any one point.

#### `cache.channel_cache.max_wait_pending`

Type

number

Default

5000

Description

The maximum time (in milliseconds) for waiting for a pending sequence before skipping it.

#### `cache.channel_cache.max_wait_skipped`

Type

number

Default

3600000

Description

The maximum amount of time (in milliseconds) to wait for a skipped sequence before abandoning it.

#### `cache.channel_cache.min_length`

Type

integer

Default

50

Description

The minimum number of entries to maintain in the cache per channel.

#### `cache.rev_cache`

Type

object

Description

The revision cache config settings.

#### `cache.rev_cache.insert_on_write`

Type

boolean

Description

Whether to insert revisions into the revision cache when documents are written to the database. If false, only revisions read from the database will be cached.

#### `cache.rev_cache.max_memory_count_mb`

Type

integer

Default

0

Description

The maximum amount of memory the revision cache should take up in MB, setting to 0 will disable any eviction based on memory at rev cache. There is a minimum value of 50 (50MB) for this config option. When set this memory limit will work in in hand with revision cache size parameter. So you will potentially get eviction at revision cache both based off memory footprint and number of items in the cache. **This is an Enterprise Edition feature only**

#### `cache.rev_cache.shard_count`

Type

integer

Default

16

Description

The number of shards the revision cache should be split into.

#### `cache.rev_cache.size`

Type

integer

Default

5000

Description

The maximum number of revisions that can be stored in the revision cache. Note when running with greater than 1 shard count we add 10% capacity overall to avoid early eviction when some shards fill up before others, so you may find that the capacity stat (revision\_cache\_num\_items) will climb to the defined rev cache size + 10%.

#### `certpath`

Type

string

Description

The cert path (public key) for X.509 bucket auth.

#### `changes_request_plus`

Type

boolean

Description

Sets the default value of `request_plus` for one-shot/non-continuous changes feeds, which when true, ensures all valid documents written prior to the request being issued are included in the response. Setting this option at the database level is required to ensure Couchbase Lite utilizes this changes feed mode.

This also sets the default value of query param `request_plus` for [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or `request_plus` for [POST /{keyspace}/\_changes](#operation/post%5Fkeyspace-%5Fchanges).

#### `client_partition_window_secs`

Type

integer

Default

2592000

Description

How long (in seconds) clients can remain offline for without losing replication metadata.

Defaults to 30 days (in seconds)

#### `compact_interval_days`

Type

number

Default

1

Description

The interval between scheduled tombstone compaction runs (in days). This can be a floating point number.

If set to 0, compaction will not run automatically.

#### `cors.headers`

Type

array

Description

List of allowed headers. These headers will be added the `Access-Control-Allow-Headers` response to a valid CORS request.

A recommended minimum set of values should be `["Accept-Encoding", "Authorization", "Content-Type", "If-Match"]`.

#### `cors.login_origin`

Type

array

Description

List of allowed origins to apply to public `/{db}/_session` API.

To use cors on `/{db}/_session`, the domain must be present in both `login_origin` and `origin`.

If configured, `Authorization` must be included in headers.

#### `cors.max_age`

Type

integer

Default

0

Description

Value for `Access-Control-Maximum-Age`. Uses 0 by default.

#### `cors.origin`

Type

array

Description

List of allowed origins for the public API. The request `Origin` header is checked against these values. If successful the `Origin` header is returned in the HTTP response header as `Access-Control-Allow-Origin`.

#### `delta_sync`

Type

object

Description

Delta sync configuration settings.

**This is an Enterprise Edition feature only**

#### `delta_sync.enabled`

Type

boolean

Description

Whether delta sync is enabled.

**This is an Enterprise Edition feature only**

#### `delta_sync.rev_max_age_seconds`

Type

number

Default

86400

Description

The number of seconds deltas for old revisions are available for.

This defaults to 24 hours (in seconds).

#### `disable_password_auth`

Type

boolean

Description

Whether to disable username/password authentication and only allow OIDC and guest access.

#### `disable_public_all_docs`

Type

boolean

Description

This controls whether the [GET /{keyspace}/\_all\_docs](#operation/get%5Fkeyspace-%5Fall%5Fdocs) REST API endpoint is publicly accessible or not. Disabling this endpoint is recommended for larger datasets or production workloads. [GET /{keyspace}/\_changes](#operation/get%5Fkeyspace-%5Fchanges) or [POST /{keyspace}/\_bulk\_get](#operation/post%5Fkeyspace-%5Fbulk%5Fget) have more efficient implementations and should be used instead.

If set to `true`, the endpoint will not be publicly accessible, and will only be available on the Admin API. Setting this to `false`, or leaving it as the default value is deprecated, and may default to `true` in a future release.

#### `event_handlers`

Type

object

Description

These are the settings for webhooks.

#### `event_handlers.db_state_changed.filter`

Type

string

Description

The Javascript function to use to filter the webhook events.

#### `event_handlers.db_state_changed.handler`

Type

string

Description

The handler type.

#### `event_handlers.db_state_changed.timeout`

Type

number

Description

The amount of time (in seconds) to attempt connect to the webhook before giving up.

#### `event_handlers.db_state_changed.url`

Type

string

Description

The URL of the webhook.

#### `event_handlers.document_changed.filter`

Type

string

Description

The Javascript function to use to filter the webhook events.

#### `event_handlers.document_changed.handler`

Type

string

Description

The handler type.

#### `event_handlers.document_changed.options`

Type

object

Description

Options for the document changed event.

#### `event_handlers.document_changed.options.winning_rev_only`

Type

boolean

Description

If true, only the winning revision of the document will be sent to the webhook.

#### `event_handlers.document_changed.timeout`

Type

number

Description

The amount of time (in seconds) to attempt connect to the webhook before giving up.

#### `event_handlers.document_changed.url`

Type

string

Description

The URL of the webhook.

#### `event_handlers.max_processes`

Type

string

Description

The maximum amount of concurrent event handling independent functions that can be running at the same time.

#### `event_handlers.wait_for_process`

Type

string

Description

The maximum amount of time (in milliseconds) to wait when the even queue is full.

#### `guest`

Type

object

Description

Properties associated with a user

#### `guest.admin_channels`

Type

array

Description

A list of channels to explicitly grant to the user for the default collection. See `collection_access` for channels in named collections.

#### `guest.admin_roles`

Type

array

Description

A list of roles to explicitly grant to the user.

#### `guest.all_channels`

Type

array (readOnly)

Description

All the channels that the user has been granted access to for the default collection. See `collection_access` for channels in named collections.

Access could have been granted through the sync function, roles, or explicitly on the user under the `admin_channels` property.

#### `guest.collection_access`

Type

object

Description

A set of access grants by scope and collection for a specific collection.

#### `guest.collection_access.{scopename…​}`

Type

object

Description

An object keyed by scope, containing a set of collections.

#### `guest.collection_access.{scopename…​}.{collectionname…​}`

Type

object

Description

An object keyed by collection name, defines access collections in this scope.

#### `guest.collection_access.{scopename…​}.{collectionname…​}.admin_channels`

Type

array

Description

A list of channels to explicitly grant to the user in this collection.

#### `guest.collection_access.{scopename…​}.{collectionname…​}.all_channels`

Type

array (readOnly)

Description

All the channels that the user has been granted access to in this collection.

Access could have been granted through the sync function, roles, or explicitly on the user under the `admin_channels` property.

#### `guest.collection_access.{scopename…​}.{collectionname…​}.jwt_channels`

Type

array (readOnly)

Description

The channels that the user has been granted access to through channels\_claim for this collection.

#### `guest.collection_access.{scopename…​}.{collectionname…​}.jwt_last_updated`

Type

string (readOnly)

Description

The last time that the user's JWT channels were updated for this collection.

#### `guest.disabled`

Type

boolean

Description

If true, the user will not be able to login to the account as it is disabled.

#### `guest.email`

Type

string

Description

The email address of the user.

#### `guest.jwt_channels`

Type

array (readOnly)

Description

The channels that the user has been granted access to through channels\_claim for the default collection.

#### `guest.jwt_issuer`

Type

string (readOnly)

Description

The issuer of the last JSON Web Token that the user last used to sign in.

#### `guest.jwt_last_updated`

Type

string (readOnly)

Description

The last time that the user's JWT roles/channels were updated.

#### `guest.jwt_roles`

Type

array (readOnly)

Description

The roles that the user has been added to through roles\_claim.

#### `guest.name`

Type

string

Description

The name of the user.

User names can only have alphanumeric ASCII characters and underscores.

#### `guest.password`

Type

string

Description

The password of the user.

Mandatory. unless `allow_empty_password` is `true` in the database configs.

#### `guest.roles`

Type

array (readOnly)

Description

All the roles that the user has been granted access to.

Access could have been granted through the sync function, roles\_claim, or explicitly on the user under the `admin_roles` property.

#### `import_backup_old_rev`

Type

boolean

Description

This controls whether import should attempt to create a temporary backup of the previous revision body (if available) when the document is modified in the bucket.

#### `import_docs`

Type

boolean

Description

If true, documents will be imported in to Sync Gateway from the bucket in the background. Documents will be ran through the set `import_filter` if any is set.

The default value depends on the edition of Sync Gateway being used. If the edition is the Community Edition, then this will default to `false` or else in the Enterprise Edition, it will default to `true`. This value requires `enable_shared_bucket_access=true`.

This can also be set to the string `continuous` which maps to true.

#### `import_filter`

Type

string

Description

This is the function that all imported documents in the default scope and collection are ran through in order to filter out what to import and what not to import. This allows you to control what is made available to Couchbase Mobile clients. If it is not set, then no documents are filtered when imported.

`import_docs` must be true to make this field applicable.

If `scopes` parameter is set, this is ignored.

#### `import_partitions`

Type

number

Default

16

Description

\*\* This is an Enterprise Edition feature only\*\*

This is how many import partitions should be used for import sharding.

Partitions are distributed among all Sync Gateway nodes participating in import processing (`import_docs=true`), and each process a subset of the server's vbuckets.

Each partition is processed by an independent function that runs simultaneously to others, so `import_partitions` can be used to tune concurrency based on the number of Sync Gateway nodes, and the number of cores per node.

#### `index`

Type

object

Description

Global Secondary Index Settings

#### `index.num_partitions`

Type

number

Default

1

Description

The number of partitions to use for the large indexes created by Sync Gateway. It is not recommended to set this unless you require additional horizontal scalability for individual indexes and have appropriately scaled your Query nodes to handle the increased query parallelism. If set, the recommended number is 8 and does not need to be directly related to the number of your Query nodes. Ensure documentation is read to understand the performance tradeoffs and instructions for migration if you have previously run with only one partition. See [/{db}/\_index\_init](#operation/post%5Fdb-%5Findex%5Finit) for more information.

If not specified or 1, all indexes will be non partitioned.

#### `index.num_replicas`

Type

number

Default

1

Description

This is the number of Global Secondary Indexes (GSI) to use for core indexes.

#### `javascript_timeout_secs`

Type

number

Default

60

Description

The maximum number of seconds the sync, import filter, and custom conflict resolver JavaScript functions are allowed to run for before timing out. Set to 0 to allow the JS functions to run uncapped.

#### `keypath`

Type

string

Description

The key path (private key) for X.509 bucket auth

#### `kv_tls_port`

Type

integer

Default

11207

Description

The Memcached TLS port.

#### `local_doc_expiry_secs`

Type

integer

Default

7776000

Description

The number of seconds before a `_local` document should expire.

#### `local_jwt`

Type

object

Description

Configuration for Local JWT authentication.

#### `local_jwt.{providername…​}`

Type

object

Description

The providers name.

#### `local_jwt.{providername…​}.algorithms`

Type

array

Description

The JWT signing algorithms to accept for authentication.

#### `local_jwt.{providername…​}.channels_claim`

Type

string

Description

If set, the value(s) of the given JSON Web Token claim will be added to the user's channels.

The value of this claim must be either a string or an array of strings, any other type will result in an error.

#### `local_jwt.{providername…​}.client_id`

Type

string

Description

The value to match against the "aud" claim of JWTs. Set to an empty string to disable audience validation.

#### `local_jwt.{providername…​}.disable_session`

Type

boolean

Description

Disable Sync Gateway session creation on successful JWT authentication.

#### `local_jwt.{providername…​}.issuer`

Type

string

Description

The value to match against the "iss" claim of JWTs.

#### `local_jwt.{providername…​}.keys`

Type

array

Description

The JSON Web Keys to use to validate JWTs.

#### `local_jwt.{providername…​}.keys.alg`

Type

string

Description

The algorithm intended for use with the key.

#### `local_jwt.{providername…​}.keys.crv`

Type

string

Description

For Elliptic Curve keys, the name of the curve to use.

#### `local_jwt.{providername…​}.keys.e`

Type

string

Description

For RSA keys, the exponent of the public key, as a Base64urlUInt-encoded value.

#### `local_jwt.{providername…​}.keys.kid`

Type

string

Description

The Key ID, used to identify the key to use.

#### `local_jwt.{providername…​}.keys.kty`

Type

string

Description

The cryptographic algorithm family used with the key, such as "RSA" or "EC"

#### `local_jwt.{providername…​}.keys.n`

Type

string

Description

For RSA keys, the modulus value of the key, as a Base64urlUInt-encoded value.

#### `local_jwt.{providername…​}.keys.use`

Type

string

Description

The intended use of the public key. Only 'sig' is accepted.

#### `local_jwt.{providername…​}.keys.x`

Type

string

Description

For Elliptic Curve keys, the X coordinate of the point, as a base64url string.

#### `local_jwt.{providername…​}.keys.y`

Type

string

Description

For Elliptic Curve keys, the Y coordinate of the point, as a base64url string.

#### `local_jwt.{providername…​}.register`

Type

boolean

Description

If to register a new Sync Gateway user account when a user logs in with a JWT.

#### `local_jwt.{providername…​}.roles_claim`

Type

string

Description

If set, the value(s) of the given JSON Web Token claim will be added to the user's roles.

The value of this claim must be either a string or an array of strings, any other type will result in an error.

#### `local_jwt.{providername…​}.user_prefix`

Type

string

Description

This is the username prefix for all users created through this provider.

#### `local_jwt.{providername…​}.username_claim`

Type

string

Description

Allows a different OpenID Connect field to be specified instead of the Subject (`sub`).

The field name to use can be specified here.

#### `logging`

Type

object

Description

Per-database logging configuration.

#### `logging.audit`

Type

object

Description

Audit logging configuration.

#### `logging.audit.disabled_roles`

Type

array

Description

List of roles for which audit logging is disabled. Either cbs or sgw.

#### `logging.audit.disabled_roles.domain`

Type

string

Description

The domain of the role for which audit logging is disabled.

#### `logging.audit.disabled_roles.name`

Type

string

Description

The name of the role for which audit logging is disabled.

#### `logging.audit.disabled_users`

Type

array

Description

List of users for which audit logging is disabled.

#### `logging.audit.disabled_users.domain`

Type

string

Description

The domain of the user for which audit logging is disabled.

#### `logging.audit.disabled_users.name`

Type

string

Description

The name of the user for which audit logging is disabled.

#### `logging.audit.enabled`

Type

boolean

Description

Whether audit logging is enabled.

#### `logging.audit.enabled_events`

Type

array

Description

List of enabled audit events for this database.

#### `logging.console`

Type

object

Description

Console logging configuration.

#### `logging.console.log_keys`

Type

array

Description

Log Keys for the console output

#### `logging.console.log_level`

Type

string

Description

Log Level for the console output

#### `max_concurrent_query_ops`

Type

integer

Default

1000

Description

The maximum amount of query operations that can be running at any one point.

#### `name`

Type

string

Description

The name of the database.

#### `offline`

Type

boolean

Description

Start the database in an offline state.

#### `oidc`

Type

object

Description

Configuration for OpenID Connect authentication.

#### `oidc.default_provider`

Type

string

Description

The default provider to use when the provider is not specified in the client.

#### `oidc.providers`

Type

object

Description

List of OpenID Connect issuers.

#### `oidc.providers.{providername…​}`

Type

object

Description

The providers name.

#### `oidc.providers.{providername…​}.InsecureSkipVerify`

Type

boolean

Description

Determines whether the TLS certificate verification should be disabled for this provider.

#### `oidc.providers.{providername…​}.IsDefault`

Type

boolean

Description

Indicates if this is the default OpenID Connect provider.

#### `oidc.providers.{providername…​}.Name`

Type

string

Description

The name of the OpenID Connect Provider.

#### `oidc.providers.{providername…​}.allow_unsigned_provider_tokens`

Type

boolean

Description

Allows users accept unsigned tokens from providers.

#### `oidc.providers.{providername…​}.callback_url`

Type

string

Description

The URL that the OpenID Connect will redirect to after authentication.

If not provided, a callback URL will be generated.

#### `oidc.providers.{providername…​}.channels_claim`

Type

string

Description

If set, the value(s) of the given OpenID Connect authentication token claim will be added to the user's channels.

The value of this claim must be either a string or an array of strings, any other type will result in an error.

#### `oidc.providers.{providername…​}.client_id`

Type

string

Description

The OpenID Connect provider client ID.

#### `oidc.providers.{providername…​}.disable_callback_state`

Type

boolean

Description

Controls whether to maintain state between the auth request and callback endpoints (`/_oidc` and `/_oidc_callback`).

**This is not recommended as it would cause OpenID Connect authentication to be vulnerable to Cross-Site Request Forgery (CSRF, XSRF).**

#### `oidc.providers.{providername…​}.disable_cfg_validation`

Type

boolean

Description

This bypasses the configuration validation based on the OpenID Connect specifications. This may be required for some OpenID providers that don't strictly adhere to the specifications.

#### `oidc.providers.{providername…​}.disable_session`

Type

boolean

Description

Disable Sync Gateway session creation on successful OpenID Connect authentication.

#### `oidc.providers.{providername…​}.discovery_url`

Type

string

Description

The non-standard discovery endpoint.

#### `oidc.providers.{providername…​}.include_access`

Type

boolean

Description

This is whether the `_oidc_callback` response should include the OpenID Connect access token and associated fields (such as `token_type`, and `expires_in`).

#### `oidc.providers.{providername…​}.issuer`

Type

string

Description

The URL for the OpenID Connect issuer.

#### `oidc.providers.{providername…​}.register`

Type

boolean

Description

If to register a new Sync Gateway user account when a user logs in with OpenID Connect.

#### `oidc.providers.{providername…​}.roles_claim`

Type

string

Description

If set, the value(s) of the given OpenID Connect authentication token claim will be added to the user's roles.

The value of this claim must be either a string or an array of strings, any other type will result in an error.

#### `oidc.providers.{providername…​}.scope`

Type

array

Description

The scope sent for the OpenID Connect request.

#### `oidc.providers.{providername…​}.user_prefix`

Type

string

Description

This is the username prefix for all users created through this provider.

#### `oidc.providers.{providername…​}.username_claim`

Type

string

Description

Allows a different OpenID Connect field to be specified instead of the Subject (`sub`).

The field name to use can be specified here.

#### `oidc.providers.{providername…​}.validation_key`

Type

string

Description

The OpenID Connect provider client secret.

#### `old_rev_expiry_seconds`

Type

number

Default

300

Description

The number of seconds before old revisions are removed from the Couchbase Server bucket.

#### `password`

Type

string

Description

The password for authenticating to the server.

#### `query_pagination_limit`

Type

integer

Default

5000

Description

The query limit to be used during pagination of large queries.

#### `replications.replication_id`

Type

object

Description

Properties of a replication

#### `replications.replication_id.adhoc`

Type

boolean

Description

Set to true to run the replication as an adhoc replication instead of a persistent one.

This means that the replication will only last the period of the replication until the status is changed to `stopped` and then it will be removed automatically. It will also be removed if Sync Gateway restarts or if removed due to user action.

#### `replications.replication_id.batch_size`

Type

integer

Default

200

Description

The amount of changes to be sent in one batch of replications. Changing this is an Enterprise Edition only feature.

#### `replications.replication_id.collections_enabled`

Type

boolean

Description

If true, the replicator will run with collections, and will replicate all collections, unless otherwise limited by `collections_local`.

If false, the replicator will only replicate the default collection.

#### `replications.replication_id.collections_local`

Type

array

Description

Limits the set of collections replicated to those listed in this array.

The replication will use all collections defined on the database if this list is empty.

#### `replications.replication_id.collections_remote`

Type

array

Description

Remaps the local collection name to the one specified in this array when replicating with the remote.

If only a subset of collections need remapping, elements in this array can be specified as `null` to preserve the local collection name.

The same index is used for both `collections_remote` and `collections_local`, and both arrays must be the same length.

#### `replications.replication_id.conflict_resolution_type`

Type

string

Default

default

Description

This defines what conflict resolution policy Sync Gateway should use to apply when resolving conflicting revisions.

Changing this is an Enterprise Edition only feature.

#### `replications.replication_id.continuous`

Type

boolean

Description

If true, changes will be immediately synced when they happen. This is known as a continuous replication.

If false, all changes will be synced until they have been processed. The replication will then cease and not process any future changes (unless started again by the user). This is known as a one-shot replication.

#### `replications.replication_id.custom_conflict_resolver`

Type

string

Description

This specifies the Javascript function to use to resolve conflicts between conflicting revisions.

This **must** be used when `conflict_resolution_type=custom`. This property will be ignored when `conflict_resolution_type` is not `custom`.

The Javascript function to provide this property should be in backticks (like the sync function). The function takes 1 parameter which is a struct that represents the conflict. This struct has 2 properties:

* `LocalDocument` \- The local document. This contains the document ID under the `_id` key.
* `RemoteDocument` \- The remote document The function should return the new document's body. This can be the winning revision (for example, `return conflict.LocalDocument`), a new body, or `nil` to resolve as a delete.

Example:

```javascript
function(conflict) {
  console.log("Doc ID: "+conflict.LocalDocument._id);
  console.log("Full remote doc: "+JSON.stringify(conflict.RemoteDocument));
  return conflict.RemoteDocument;
}

```

Using complex `custom_conflict_resolver` functions can noticeably degrade performance. Use a built-in resolver whenever possible.

If a document merge is being done, the `_rev` and `_cv` properties should not be included in the returned document body as Sync Gateway will generate new values for these.

This is an Enterprise Edition only feature.

#### `replications.replication_id.direction`

Type

string

Description

This specifies which direction the replication will be replicating with the `remote` replicator.

#### `replications.replication_id.enable_delta_sync`

Type

boolean

Description

This will turn on delta-sync for the replication. In order to enable delta-sync for a replication, the database level setting `delta_sync.enabled` must also be set to true.

Using delta-sync is an Enterprise Edition only feature.

#### `replications.replication_id.filter`

Type

string

Description

This defines whether to filter documents.

#### `replications.replication_id.initial_state`

Type

string

Default

running

Description

This is what state to start the replication in when creating a new replication.

This allows you to control if the replication starts in a `stopped` start or `running` state.

Replications prior to Sync Gateway 2.8 will run in the default state `running`.

#### `replications.replication_id.max_backoff_time`

Type

integer

Default

5

Description

Specifies the maximum time-period (in minutes) that Sync Gateway will attempt to reconnect to a lost or unreachable remote.

When a disconnection happens, Sync Gateway will do an exponential backoff up to this specified value. When this value is met, it will attempt to reconnect indefinitely every `max_backoff_time` minutes.

If this is set to 0, Sync Gateway will do the normal exponential backoff after the disconnect happens but then attempting 10 minutes and stop the replication.

Note: this defaults to 5 minutes for replications created prior to Sync Gateway 2.8.

#### `replications.replication_id.purge_on_removal`

Type

boolean

Description

Specifies whether to purge a document if the remote user loses access to all of the channels on the document when attempting to pull it from the remote.

If false, documents will not be replicated and not be purged when the user loses access.

#### `replications.replication_id.query_params`

Type

array

Description

This is a set of key/value pairs used in the query string of the replication.

If `filters=sync_gateway/bychannel` then this can be used to set the channels to filter by in a pull replication. To do this, set the `channels` key to a string array of the channels to filter by. For example:

```json
"filter":"sync_gateway/bychannel",
"query_params": {
  "channels":["chanUser1"]
},

```

#### `replications.replication_id.remote`

Type

string

Description

This is the endpoint of the database for the remote Sync Gateway that is the subject of this replication's `push`, `pull`, or `pushAndPull` action. Typically this would include the URI, port, and database name. For example, `https://localhost:4985/db`.

#### `replications.replication_id.remote_password`

Type

string

Description

The password to use to authenticate with the remote. This password will be redacted in the replication config.

#### `replications.replication_id.remote_username`

Type

string

Description

The username to use to authenticate with the remote.

#### `replications.replication_id.replication_id`

Type

string

Description

This is the ID of the replication.

When creating a new replication using a POST request, this will be set to a random UUID if not explicitly set.

When the replication ID is specified in the URL, this must be set to the same replication ID if specifying it at all.

#### `replications.replication_id.run_as`

Type

string

Description

This is used if you want to specify a user to run the replication as. This means that the replication will only be able to replicate what the user access to what the user has access to.

#### `revs_limit`

Type

number

Default

50

Description

The maximum depth a document's revision tree can grow to.

#### `roles.{rolename…​}`

Type

object

Description

Properties associated with a role

#### `roles.{rolename…​}.admin_channels`

Type

array

Description

A list of channels to explicitly grant to the role for the default collection. See `collection_access` for channels in named collections.

#### `roles.{rolename…​}.all_channels`

Type

array (readOnly)

Description

All the channels that the role has been granted access to for the default collection.

These channels could have been assigned by the Sync function or using the `admin_channels` property.

#### `roles.{rolename…​}.collection_access`

Type

object

Description

A set of access grants by scope and collection for a specific collection.

#### `roles.{rolename…​}.collection_access.{scopename…​}`

Type

object

Description

An object keyed by scope, containing a set of collections.

#### `roles.{rolename…​}.collection_access.{scopename…​}.{collectionname…​}`

Type

object

Description

An object keyed by collection name, defines access collections in this scope.

#### `roles.{rolename…​}.collection_access.{scopename…​}.{collectionname…​}.admin_channels`

Type

array

Description

A list of channels to explicitly grant to the user in this collection.

#### `roles.{rolename…​}.collection_access.{scopename…​}.{collectionname…​}.all_channels`

Type

array (readOnly)

Description

All the channels that the user has been granted access to in this collection.

Access could have been granted through the sync function, roles, or explicitly on the user under the `admin_channels` property.

#### `roles.{rolename…​}.collection_access.{scopename…​}.{collectionname…​}.jwt_channels`

Type

array (readOnly)

Description

The channels that the user has been granted access to through channels\_claim for this collection.

#### `roles.{rolename…​}.collection_access.{scopename…​}.{collectionname…​}.jwt_last_updated`

Type

string (readOnly)

Description

The last time that the user's JWT channels were updated for this collection.

#### `roles.{rolename…​}.name`

Type

string

Description

The name of the role.

Role names can only have alphanumeric ASCII characters and underscores.

#### `scopes`

Type

object

Description

An object keyed by scope name containing config for the specific collection.

#### `scopes.{scopename…​}`

Type

object

Description

Scope-specific configuration.

#### `scopes.{scopename…​}.collections`

Type

object

Description

An object keyed by collection name containing config for the specific collection.

#### `scopes.{scopename…​}.collections.{collectionname…​}`

Type

object

Description

Collection-specific configuration.

#### `scopes.{scopename…​}.collections.{collectionname…​}.import_filter`

Type

string

Description

This is the function that all imported documents in this collection are ran through in order to filter out what to import and what not to import. This allows you to control what is made available to Couchbase Mobile clients. If it is not set, then no documents are filtered when imported.

`import_docs` in the database config must be true to make this field applicable.

#### `scopes.{scopename…​}.collections.{collectionname…​}.sync`

Type

string

Description

The Javascript function that newly created documents in this collection are ran through.

#### `send_www_authenticate_header`

Type

boolean

Default

true

Description

Controls whether to send a `WWW-Authenticate` header in `401 Unauthorized` HTTP responses.

#### `serve_insecure_attachment_types`

Type

boolean

Description

If set, always serve attachments with the `Content-Type` header set to the type of the attachment.

When serving an attachment, usually the `Content-Type` header is set to the type of the attachment but the `Content-Disposition` response header will be set instead if the content type is vulnerable to a phishing attack, causing the browser to download the file instead of display it. This option will override that behaviour and always set the `Content-Type` header.

#### `server`

Type

string

Description

This is the Couchbase Server address or addresses that the database connect to.

#### `session_cookie_http_only`

Type

boolean

Description

Make all session cookies for the database set the `HttpOnly` flag so they are inaccessible to JavaScript.

#### `session_cookie_name`

Type

string

Description

This can be used to define a custom per-database session cookie name.

#### `session_cookie_secure`

Type

boolean

Description

Override the session cookie `secure` flag. If set, the cookie will have the `secure` flag.

This will default to `true` if startup config `api.https.tls_cert_path` is set otherwise it will default to `false`.

#### `sgreplicate_enabled`

Type

boolean

Default

true

Description

Whether the node should accept assign replications (`true`) or not (`false`).

#### `sgreplicate_websocket_heartbeat_secs`

Type

integer

Default

300

Description

Use a custom heartbeat interval (in seconds) for websocket ping frames.

#### `slow_query_warning_threshold`

Type

number

Default

500

Description

The amount of milliseconds a N1QL query should run before logging a warning.

#### `store_legacy_revtree_data`

Type

boolean

Default

true

Description

Controls whether Sync Gateway stores additional legacy revision tree pointer data to support 3.x/early 4.x clients that still use RevTree IDs (for example when used as delta sources).

Disable this when you are confident all clients use newer CV-based revisions and no longer require legacy RevTree ID lookups.

#### `suspendable`

Type

boolean

Description

Set to true to allow the database to be suspended.

Defaults to true when running in serverless mode otherwise defaults to false.

#### `sync`

Type

string

Default

function(doc){channel(doc.channels);}

Description

The Javascript function that newly created documents are ran through for the default scope and collection.

If `scopes` parameter is set, this is ignored.

#### `unsupported`

Type

object

Description

These are unsupported options and therefore it is not recommended to use them.

#### `unsupported.api_endpoints.enable_couchbase_bucket_flush`

Type

boolean

Description

**Setting for test purposes only**

Whether Couchbase buckets can be flushed via Admin REST API.

#### `unsupported.dcp_read_buffer`

Type

number

Description

Set the dcp feed to use a different read buffer size.

#### `unsupported.force_api_forbidden_errors`

Type

boolean

Description

Force REST API errors to return forbidden

#### `unsupported.guest_read_only`

Type

boolean

Description

Restrict GUEST document access to read-only.

#### `unsupported.kv_buffer`

Type

number

Description

Set the kv pool to use a different buffer size.

#### `unsupported.oidc_test_provider.enabled`

Type

boolean

Description

Whether the `oidc_test_provider` endpoints should be exposed on the public API.

#### `unsupported.oidc_tls_skip_verify`

Type

boolean

Description

Enable self-signed certificates for OIDC testing.

#### `unsupported.remote_config_tls_skip_verify`

Type

boolean

Description

Enable self-signed certificates for external JavaScript load.

#### `unsupported.resync_partitions`

Type

integer

Description

Number of partitions to use for distributed DCP resync. Maximum number is the number of vBuckets for the backing bucket.

#### `unsupported.same_site_cookie`

Type

string

Description

Override the session cookie SameSite behavior. By default, a session cookie will have SameSite:None if CORS is enabled, and will have no SameSite attribute if CORS is not enabled. Setting this property to`Default` will omit the SameSite attribute from the cookie.

#### `unsupported.sgr_tls_skip_verify`

Type

boolean

Description

Enable self-signed certificates for SG-replicate testing.

#### `unsupported.user_views.enabled`

Type

boolean

Description

Whether pass-through view query is supported through public API.

#### `unsupported.warning_thresholds.access_and_role_grants_per_doc`

Type

number

Description

The number of access and role grants per document to be used as a threshold for grant count warnings.

#### `unsupported.warning_thresholds.channel_name_size`

Type

number

Description

The number of channel name characters to be used as a threshold for channel name warnings.

#### `unsupported.warning_thresholds.channels_per_doc`

Type

number

Description

The number of channels per document to be used as a threshold for the channel count warnings.

#### `unsupported.warning_thresholds.channels_per_user`

Type

number

Description

The number of channels per user to be used as a threshold for channel count warnings.

#### `unsupported.warning_thresholds.xattr_size_bytes`

Type

number

Description

The number of bytes to be used as a threshold for xattr size limit warnings.

#### `use_views`

Type

boolean

Description

Force the use of views instead of GSI.

#### `user_xattr_key`

Type

string

Description

The key to use for the user xattr that will be accessible from the sync function. If empty, the feature will be disabled.

This is an Enterprise Edition feature only.

#### `username`

Type

string

Description

The username for authenticating to the server.

#### `users.{username…​}`

Type

object

Description

Properties associated with a user

#### `users.{username…​}.admin_channels`

Type

array

Description

A list of channels to explicitly grant to the user for the default collection. See `collection_access` for channels in named collections.

#### `users.{username…​}.admin_roles`

Type

array

Description

A list of roles to explicitly grant to the user.

#### `users.{username…​}.all_channels`

Type

array (readOnly)

Description

All the channels that the user has been granted access to for the default collection. See `collection_access` for channels in named collections.

Access could have been granted through the sync function, roles, or explicitly on the user under the `admin_channels` property.

#### `users.{username…​}.collection_access`

Type

object

Description

A set of access grants by scope and collection for a specific collection.

#### `users.{username…​}.collection_access.{scopename…​}`

Type

object

Description

An object keyed by scope, containing a set of collections.

#### `users.{username…​}.collection_access.{scopename…​}.{collectionname…​}`

Type

object

Description

An object keyed by collection name, defines access collections in this scope.

#### `users.{username…​}.collection_access.{scopename…​}.{collectionname…​}.admin_channels`

Type

array

Description

A list of channels to explicitly grant to the user in this collection.

#### `users.{username…​}.collection_access.{scopename…​}.{collectionname…​}.all_channels`

Type

array (readOnly)

Description

All the channels that the user has been granted access to in this collection.

Access could have been granted through the sync function, roles, or explicitly on the user under the `admin_channels` property.

#### `users.{username…​}.collection_access.{scopename…​}.{collectionname…​}.jwt_channels`

Type

array (readOnly)

Description

The channels that the user has been granted access to through channels\_claim for this collection.

#### `users.{username…​}.collection_access.{scopename…​}.{collectionname…​}.jwt_last_updated`

Type

string (readOnly)

Description

The last time that the user's JWT channels were updated for this collection.

#### `users.{username…​}.disabled`

Type

boolean

Description

If true, the user will not be able to login to the account as it is disabled.

#### `users.{username…​}.email`

Type

string

Description

The email address of the user.

#### `users.{username…​}.jwt_channels`

Type

array (readOnly)

Description

The channels that the user has been granted access to through channels\_claim for the default collection.

#### `users.{username…​}.jwt_issuer`

Type

string (readOnly)

Description

The issuer of the last JSON Web Token that the user last used to sign in.

#### `users.{username…​}.jwt_last_updated`

Type

string (readOnly)

Description

The last time that the user's JWT roles/channels were updated.

#### `users.{username…​}.jwt_roles`

Type

array (readOnly)

Description

The roles that the user has been added to through roles\_claim.

#### `users.{username…​}.name`

Type

string

Description

The name of the user.

User names can only have alphanumeric ASCII characters and underscores.

#### `users.{username…​}.password`

Type

string

Description

The password of the user.

Mandatory. unless `allow_empty_password` is `true` in the database configs.

#### `users.{username…​}.roles`

Type

array (readOnly)

Description

All the roles that the user has been granted access to.

Access could have been granted through the sync function, roles\_claim, or explicitly on the user under the `admin_roles` property.

#### `view_query_timeout_secs`

Type

integer

Default

75

Description

The number of seconds before a view query should timeout.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)