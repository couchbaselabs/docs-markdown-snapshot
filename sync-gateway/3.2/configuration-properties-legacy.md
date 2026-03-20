---
title: Legacy Pre-3.0 Configuration
description: Configuring <em>Sync Gateway</em> Pre-3.0 to provide secure
  cloud-to-edge synchronization of enterprise data using the standard, static,
  configuration file.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/configuration-properties-legacy.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.2@sync-gateway::configuration-properties-legacy.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.2/configuration-properties-legacy.html)

# Legacy Pre-3.0 Configuration

> Configuring _Sync Gateway_ Pre-3.0 to provide secure cloud-to-edge synchronization of enterprise data using the standard, static, configuration file.  

Topic Group

Configuration Schema | [Javascript Functions](configuration-javascript-functions.md)| [Environment Variables](configuration-environment-variables.md)| [REST API](configuration-rest-api.md)| [Persistent Configuration](configuration-overview.md)

> [!IMPORTANT]
> Legacy Configuration
> 
> You cannot use `collections` in Sync Gateway’s legacy Pre-3.0 configuration method. For current configuration details, see: [Configuration Overview](configuration-overview.md) and-or [Bootstrap Configuration](configuration-schema-bootstrap.md).

## [](#introduction)Introduction

This page describes Sync Gateway’s legacy Pre-3.0 configuration method. It uses a centralized configuration file to hold all configuration settings in JSON form — see:[the schema](#lbl-schema) for the file contents.

> [!IMPORTANT]
> Persistent Configuration is enabled by default from 3.0.
> 
> To continue using legacy Pre-3.0 configuration you should start Sync Gateway with [disable-persistent-config](#disable%5Fpersistent%5Fconfig) set `true` either in the configuration file or in [Command Line Options](command-line-options.md).

Many configuration settings can be changed using the [Admin REST API](rest-api-admin.md) **but these are not persisted beyond a Sync Gateway restart**. To make persistent changes you must edit the central Configuration Properties file — or switch to the 3.x persistent configuration — see: [Configuration Overview](configuration-overview.md)

## [](#lbl-format)File Format

The Configuration Properties file defines sync gateway’s runtime behavior. Its contents include, for example:

* Details of the connected Couchbase databases
* How replications are conducted
* What security is to be used
* What logging options are to be applied, and
* Any customization of import filtering and synchronization.

The majority of the configuration is achieved using standard JSON syntax — see [the schema](#lbl-schema) for more.

> [!NOTE]
> The `sync-gateway-config.json` file relies on the use of one _relaxed_ JSON feature; the use of back ticks (`` ` ``). Text between back ticks is treated as a string. It can span multiple lines and contain double-quotes. Those features make it ideal for the incorporation of inline JavaScript, which can be used to provision, for example, `sync` and `import_filter` functions.

## [](#lbl-running)Running

Use the following command to run Sync Gateway with a configuration file:

Run Sync Gateway

```bash
sync_gateway -disable_persistent_config sync-gateway-config.json
```

See also — [Command Line Options](command-line-options.md)

## [](#lbl-schema)Schema

## [](#lbl-example)Example

```json
{
  "interface":":5984",
  "adminInterface":":5985",
  "logging": {
    "log_file_path": "/var/tmp/sglogs",
    "console": {
      "log_level": "debug",
      "log_keys": ["*"]
    },
    "error": {
      "enabled": true,
      "rotation": {
        "max_size": 20,
        "max_age": 180
      }
    },
    "warn": {
      "enabled": true,
      "rotation": {
        "max_size": 20,
        "max_age": 90
      }
    },
    "info": {
      "enabled": false
    },
    "debug": {
      "enabled": false
    }
  },
  "databases": {
       "db1-local": {
            "import_docs": true,
            "bucket":"db1-local",
            "server": "couchbase://cb-server",
            "enable_shared_bucket_access":true,
            "delta_sync": {
              "enabled": true
            },
            "import_filter": `
              function(doc) {
                return true;
              }
              `,
            "username": "admin",
            "password": "password",
            "users":{
                "admin": {"password": "password", "admin_channels": ["*"]},
                "user1": {"password": "password", "admin_channels":["channel.user1"]}
            },
           "num_index_replicas":0,
           "sgreplicate_enabled":false,
           "replications":{
               "db1-rep-id1" : {
                   "direction": "pushAndPull",
                   "conflict_resolution_type":"custom",
                    "custom_conflict_resolver":`
                      function(conflict) {
                          if (  (conflict.LocalDocument.type != null) &&
                                (conflict.RemoteDocument.type != null) &&
                                (conflict.LocalDocument.type == "usedefault"))
                          {
                              console.log("Will use default policy");
                              // Resolve using built-in policy
                              return defaultPolicy(conflict);
                          }
                          else
                          {
                            // Merge local and remote docs
                            var remoteDoc = conflict.RemoteDocument;
                            console.log("full remoteDoc doc: "+JSON.stringify(remoteDoc));
                            var localDoc = conflict.LocalDocument;
                            console.log("full localDoc doc: "+JSON.stringify(localDoc));
                            var mergedDoc = extend({}, localDoc, remoteDoc);
                            delete mergedDoc._rev (1)

                            console.log("full mergedDoc doc: "+JSON.stringify(mergedDoc));
                            // Resolve using this merged doc as the winner
                            return mergedDoc;

                            function extend(target) {
                                var sources = [].slice.call(arguments, 1);
                                sources.forEach(function (source) {
                                    for (var prop in source) {
                                      if (prop.indexOf('_') != 0) { (2)
                                        target[prop] = source[prop];
                                      }
                                    }
                                });
                                return target;
                            } // end function extend()
                          } // end if
                      }` // end function()
                    , // end custom_conflict_resolver
                   "purge_on_removal":true,
                   "remote": "http://user1:password@example.com:4984/db1-remote",
                   "filter":"sync_gateway/bychannel",
                   "query_params": {
                       "channels":["channel.user1"]
                   },
                   "enable_delta_sync":  true,
                    "batch_size" :1000,
                    "continuous": true,
                    "state": "running"
               }
           },
          "sync": `
      function sync(doc, oldDoc) {
        /* sanity check */
        // check if document was removed from server or via SDK
        // In this case, just return
        if (isRemoved()) {
          return;
        }

        /* Routing */
        // Add doc to the user's channel.
        channel("channel.user1");

        // This is when document is removed via SDK or directly on server
        function isRemoved() {
          return( isDelete() && oldDoc == null);
        }

        function isDelete() {
          return (doc._deleted == true);
        }

      }
            `
          },
    "db2-local": {
      "import_docs": true,
      "bucket":"db2-local",
      "server": "couchbase://cb-server",
      "enable_shared_bucket_access":true,
      "delta_sync": {
        "enabled": true
      },
      "import_filter": `
        function(doc) {
          return true;
        }
        `,
      "username": "admin",
      "password": "password",
      "users":{
        "admin": {"password": "password", "admin_channels": ["*"]},
        "user1": {"password": "password", "admin_channels":["channel.user1"]}
      },
      "num_index_replicas":0,
      "sgreplicate_enabled":true,
      "replications":{
        "db2-rep-id1-pull" : {
          "direction": "pull",
          "purge_on_removal":true,
          "remote": "http://user1:password@example2.com:4984/db2-remote",
          "conflict_resolution_type":"remoteWins",
          "filter":"sync_gateway/bychannel",
          "query_params": {
            "channels":["channel.user1"]
          },
          "enable_delta_sync":  true,
          "batch_size" :1000,
          "continuous": true,
          "state": "stopped"
            }
          },
          "sync": `
          function sync(doc, oldDoc) {
            // . . . code as required
          `
        }
      }
    }
```

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](#)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)