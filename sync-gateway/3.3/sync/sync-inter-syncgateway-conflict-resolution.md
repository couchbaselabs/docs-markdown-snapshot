---
title: Enhanced Conflict Resolution
description: About conflict resolution in inter-Sync Gateway replication
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/sync/pages/sync-inter-syncgateway-conflict-resolution.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.3@sync-gateway:sync:sync-inter-syncgateway-conflict-resolution.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/sync/sync-inter-syncgateway-conflict-resolution.html)

# Enhanced Conflict Resolution

> About conflict resolution in inter-Sync Gateway replication  
> Introduces inter-Sync Gateway replication conflict resolution policies and behaviors

_Related topics_: [Overview](sync-inter-syncgateway-overview.md) | [Run](sync-inter-syncgateway-run.md) | [Manage](sync-inter-syncgateway-manage.md) | [Monitor](sync-inter-syncgateway-monitor.md) | [Conflict](sync-inter-syncgateway-conflict-resolution.md)

_Other Topics_: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md) | [Admin REST API](../rest-api/rest-api-admin.md)

> [!IMPORTANT]
> Context Clarification
> 
> This content relates only to inter-Sync Gateway replication in Sync Gateway 2.8+. For documentation on pre-2.8 inter-Sync Gateway replication (also known as SG Replicate) — see the documentation for the appropriate release.

## [](#automatic-conflict-resolution)Automatic Conflict Resolution

Inter-Sync Gateway **pull** replications support automatic conflict resolution by default (no conflict mode).

In _Pull_ replications the _active_ Sync Gateway detects and resolves conflicts based on its configured [conflict\_resolution\_type](../configuration/configuration-schema-database.md#database-replications-this%5Frep-conflict%5Fresolution%5Ftype) and _conflict resolver policy_. This policy will determine the _winner_ or return an error if it cannot.

Conflicts are **not** resolved in **push** replications though. The passive end of the push simply detects and rejects any conflicting revisions (`409 Conflict` response).

Both approaches reflect the way conflicts are handled by Couchbase Lite clients. Not surprising since in both instances Couchbase Lite is acting like the active node in an inter-sync gateway exchange.

> [!NOTE]
> Conflicts are only resolved during a **pull** replication. If conflicts are likely, you should configure a `pushAndPull` replication when using Conflict Free mode.
> 
> _Alternatively_: Run the replicator from the other side; flipping the direction (to `pull`) and the resolution policy (for example `localWins` becomes `remoteWins`).
> 
> See also — our blog post: [Document Conflicts & Resolution in Couchbase Mobile](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)

For [ENTERPRISE EDITION](https://www.couchbase.com/products/editions), a custom conflict resolver policy is available, providing additional flexibility by allowing users to provide their own conflict resolution logic — see: [Inter Sync Gateway Sync - Custom Conflict Resolution](#custom-conflict-resolution-ee)

## [](#configure-conflict-resolution)Configure Conflict Resolution

Invoke automatic conflict resolution by specifying the required _conflict resolver policy_ in the [replication definition![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#replication-definition). The specified policy is applied whenever a conflict is detected.

Example 1\. Using automatic conflict resolution

* default
* localWins
* remoteWins

```json
"databases:"
  // other config as necessary
  "this_db:"
    // other config as necessary
    "sgreplicate_enabled": "true",
    "replications": [
        {
          "replication_id": "replication1",
          "direction": "push_and_pull",
          "continuous": true,
          "filter": "sync_gateway/bychannel",
          "query_params": [
              "channel1",
              "channel2"
          ],
          "conflict_resolution_type": "default",
          // other config as necessary
        }
    ]
// other config as necessary
```

```json
"databases:"
  // other config as necessary
  "this_db:"
    // other config as necessary
    "sgreplicate_enabled": "true",
    "replications": [
        {
          "replication_id": "replication1",
          "direction": "push_and_pull",
          "continuous": true,
          "filter": "sync_gateway/bychannel",
          "query_params": [
              "channel1",
              "channel2"
          ],
          "conflict_resolution_type": "localWins",
          // other config as necessary
        }
    ]
// other config as necessary
```

```json
"databases:"
  // other config as necessary
  "this_db:"
    // other config as necessary
    "sgreplicate_enabled": "true",
    "replications": [
        {
          "replication_id": "replication1",
          "direction": "push_and_pull",
          "continuous": true,
          "filter": "sync_gateway/bychannel",
          "query_params": [
              "channel1",
              "channel2"
          ],
          "conflict_resolution_type": "remoteWins",
          // other config as necessary
        }
    ]
// other config as necessary
```

## [](#custom-conflict-resolution-ee)Build a Conflict Resolution Policy \[EE\]

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Custom conflict resolution is handled by the _active_ Sync Gateway using a user-provided [custom conflict resolver![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#custom-conflict-resolver). This Javascript function is embedded in the replication configuration.

The predefined conflict resolver policies are also available as Javascript functions that you can call from within that _custom\_conflict\_resolver_ function This is useful when you want to apply greater selectivity to the automatic conflict resolution process. For example, you want to apply a 'remote wins' policy only for a specific type of document - see the 'Use Policies' tab in [Example 5](#simple-conflict-resolvers).

### [](#conflict-resolution-approaches)Conflict Resolution Approaches

There are two ways to handle conflicts in your custom\_conflict\_resolver, you can either:

* Choose a _winning_ revision from among the conflicting revisions (see [Example 5](#simple-conflict-resolvers)), or
* Merge conflicting revision to create a new _winning_ revision; losing revisions are tomb-stoned.  
> [!NOTE]  
> When creating a new revision, do not provide a `_rev` property. A new revision ID will be generated. Use `delete mergedDoc._rev` to invalidate the property.  
However, users should avoid overly-complex resolver logic that may impact performance.

### [](#approaches-to-error-handling)Approaches to Error Handling

Your custom conflict resolver function should not terminate the replication when it encounters exceptions or errors. Instead, you should log sufficient information to aid troubleshooting and recovery.

For example, your custom conflict resolver function should:

* Skip the document causing the issue
* Log a suitable warning level message. Include at least the skipped document's Id and the sequence Id of the revision in error.

Refer to log files when troubleshooting conflict resolution errors, to identify the document id and revision sequence in error.

Example 2\. Some Error Scenarios and Recommended Resolutions

Unexpected data in the remote document

You should update the remote document to fix the issue. Doing so will cause replication of the update.

Unexpected data in the local document

You should update the local document to fix the issue. This will not trigger a pull-replication. Do a no-op-update \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] of the remote document, which will trigger replication and conflict resolution.

Fault in conflict resolution javascript function

Fix the Javascript logic and then either:

* Do a _no op update_ \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] of the remote document. This triggers a pull replication and subsequent conflict resolution.
* Reset the replication (using `_replicationstatus/reset` endpoint). Not recommended as it introduces significant duplicate processing in resyncing previously synced documents.

### [](#conflict-resolver-structure)Conflict Resolver Structure

Sync Gateway supports the use of Javascript functions to customize the sync process. These functions are referenced from within the Sync Gateway Configuration and may be provided either as:

* An inline Javascript function
* An external Javascript file
* An external HTTP/HTTPS endpoint serving a JS function \[[2](#%5Ffootnotedef%5F2 "View footnote.")\].

You can provide your conflict resolver as either an inline or external Javascript function. You can learn more about the ($db.custom\_conflict\_resolver) property in the Configuration Schema Reference — see: [custom\_conflict\_resolver](../configuration/configuration-schema-database.md#database-replications-this%5Frep-custom%5Fconflict%5Fresolver).

> [!NOTE]
> Sync gateway 3.x configuration of Javascript functions is done using the [Admin REST API](../rest-api/rest-api-admin.md); specifically the [Authentication](../rest-api/rest%5Fapi%5Fadmin.md#tag/Authentication) and [/{keyspace}/\_config/import\_filter](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-import%5Ffilter) endpoints.

Prior to this, configuration was done within the database configuration file — see: [Example 3](#ex-jsfunc-opts)

* Inline Javascript functions provided within the database configuration must be enclosed by a backtick pair (\`\`).
* To use an external Javascript function for any of the eligible options, you need to specify the absolute path to the Javascript. The format and content of the external Javascript is the same as that provided inline.  
> [!NOTE]  
> You must register a CA certificate for the appropriate server if external Javascript functions are hosted on HTTPS endpoints.  
> [!TIP]  
> For testing purposes you may use the unsupported configuration option `[unsupported.remote_config_tls_skip_verify](../configuration/configuration-schema-database.md#database-unsupported-remote%5Fconfig%5Ftls%5Fskip%5Fverify     )`. Setting this `true` will side-step essential security checks. Do not use in Production deployments.

Example 3\. Configuring a Javascript Sync Function

This example shows the different ways you might provide a Javascript Sync Function. Although the example uses the Sync Function, the same approach applies wherever a Javascript function is valid (including with Import Filter, Webhook and Custom Conflict Resolver).

```json
curl -X PUT 'http://localhost:4985/db1/_config' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
         "sync": "/opt/couchbase-sync-gateway/sync.js" (1)
      },
    }
}'


  curl -X PUT 'http://localhost:4985/db2/_config' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
         "sync": "https://localhost/sync/func2" (2)
      }
   }
}


curl -X PUT 'http://localhost:4985/db3/_config' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
         "sync": `function(doc,oldDoc, meta){ if (doc.published) { channel("public");} }`
      } (3)
   }
}
```

| **1** | Here we specify an external file sync.js as containing the external function to be provisioned                |
| ----- | ------------------------------------------------------------------------------------------------------------- |
| **2** | Here we specify a HTTPS endpoint as resolving to a Javascript function to be provisioned                      |
| **3** | Here we specify inline Javascript (surrounded by a pair of backticks (\`\`) as the function to be provisioned |

The following example shows the basic structure of the conflict resolver function as it would be defined in the configuration file.

Example 4\. Conflict resolver structure

```javascript

"custom_conflict_resolver": "`function(conflict) { (1)
  //  . . .
  //  . . . application logic to determine winner
  //  . . .
  return conflict.LocalDocument;  (2)
  }`" (3)
```

| **1** | The conflict structure comprises both conflicting documents. type Conflict struct {   LocalDocument  Body \`json:"LocalDocument"\`   RemoteDocument Body \`json:"RemoteDocument"\` } LocalDocument This LocalDocument object encapsulates the body and metadata of the local conflicting document revision being replicated. Its content matches the JSON stored at the local Sync Gateway. RemoteDocument The RemoteDocument object, encapsulates the body and metadata of the remote conflicting document revision being replicated. Its content matches the JSON stored at the remote Sync Gateway. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | You should return one of: conflict.LocalDocument conflict.RemoteDocument a new document body comprising the merged local and remote documents a **nil** body, which will be resolved as a **delete**                                                                                                                                                                                                                                                                                                                                                                                                   |
| **3** | The conflict resolver function is enclosed by backticks (\`\`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### [](#sample-conflict-resolvers)Sample Conflict Resolvers

Example 5\. Simple conflict resolvers

* Use Built-in Policies
* Nominate a Winner
* Merge a Winner

This example uses the built-in resolver functions to resolve the conflict based-on the document type.

So, documents of type `a-doc-type-1` are always resolved in favor of the remote revision. All other document types are resolved in accordance with the default resolver policy.

```json
"replications": [
  {
  "replication_id": "replication1",
  // other config as required
  "conflict_resolution_type": "custom",
  "custom_conflict_resolver": `
    function(conflict) {
      if  (conflict.LocalDocument.type == "a-doctype-1") &&
          (conflict.RemoteDocument.type == "a-doctype-1")
       {
         // Invoke the built in default resolver logic
         return defaultPolicy(conflict);
       }
      else {
        // Otherwise resolve in favor of remote document
          return conflict.RemoteDocument;
        }
    }
    `
  // other config as required
  }
]
```

This example selects a winner based on relative priorities and builds a return response of its own rather than using either the localWins or remoteWins policy, although it does rely on the default resolver policy as a backstop.

```json
"replications": [
  {
    // . . . preceding replication details as required
  },
  {
    "replication_id": "replication2",
    // . . .   other config as required
    "conflict_resolution_type": "custom",
    "custom_conflict_resolver": `
      function(conflict) {
        // Custom conflict resolution policy based on priority
        if (conflict.LocalDocument.body.priority > conflict.RemoteDocument.body.priority) {
          // Choose a local winner
          // Optionally apply application logic to manipulate
          // the local object before returning it as the winner
          return conflict.LocalDocument;
        } else if (local.body.priority < remote.body.priority) {
            // Choose a remote winner
            // Optionally apply application logic to manipulate
            // the remote object before returning it as the winner
          return conflict.RemoteDocument;
          }; //end if
        } //end func()
        // Apply the default policy as a catch all
        return defaultPolicy(conflict);
    }` // end resolver property
  }, // end replication2
  {
    // . . . further replication details as required
  }
]
// . . .   other config as required
```

This example creates a winner by merging changes from the local and remote documents to create a new document object, which is returned as the winner.

If both document.types are non-null and the local document.type is `usedefault`, the merge path is overridden and the default resolver policy is applied.

```json
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
```

| **1** | Invalidate the \_rev property. A new revision ID will be generated.                                                                                                                                        |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Transcribe properties from source to target. The IF block is temporary. It circumvents the known\_issue [CBG-1335](https://issues.couchbase.com/browse/CBG-1335), which results in a revision ID mismatch. |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Inter Sync Gateway Sync - Overview](sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](sync-with-couchbase-server.md)

###### [](#-3)

Reference material …​

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)
* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Conflict Related Blogs

* [Automatic Conflict Resolution](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)
* [Demystifying Conflict Resolution](https://blog.couchbase.com/conflict-resolution-couchbase-mobile/)
* [Conflict Resolution (category)](https://blog.couchbase.com/tag/conflict-resolution/)

---

[1](#%5Ffootnoteref%5F1). No-op update — refers to a change to the document body that has no impact on the app logic but will trigger an import by the Sync Gateway. One option could be to include a property used specifically for this purpose (i.e. a counter that can be incremented in response to conflict resolver errors). 

[2](#%5Ffootnoteref%5F2). Sync Gateway 3.x