---
title: Configuration File
description: How to configure <em>Sync Gateway</em> to provide secure
  cloud-to-edge synchronization of enterprise data.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/configuration-properties.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::configuration-properties.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/configuration-properties.html)

# Configuration File

> How to configure _Sync Gateway_ to provide secure cloud-to-edge synchronization of enterprise data.  
> This content describes Sync Gateway’s configuration schema providing parameter explanations and examples of use

## [](#about-the-schema)About the Schema

Sync Gateway uses a JSON-like configuration file to define its runtime behavior. The file’s contents include, for example:

* Details of the connected Couchbase databases
* How replications are conducted
* What security is to be used
* What logging options are to be applied, and
* Any customization of import filtering and synchronization.

The majority of the configuration is achieved using standard JSON syntax — see [Configuration Reference](#configuration-reference) for more.

> [!NOTE]
> The `sync-gateway-config.json` file relies on the use of one _relaxed_ JSON feature; the use of back ticks (`` ` ``). Text between back ticks is treated as a string. It can span multiple lines and contain double-quotes. Those features make it ideal for the JavaScript used in `sync` and `import_filter` functions.

Use the following command to run Sync Gateway with a configuration file:

```bashrc
sync_gateway sync-gateway-config.json
```

## [](#configuration-reference)Configuration Reference

## [](#example-sync-gateway-configuration)Example Sync Gateway Configuration

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

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)