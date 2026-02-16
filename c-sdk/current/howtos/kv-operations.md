[View original HTML](/c-sdk/current/howtos/kv-operations.html)

## [](#documents)Documents

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform. Or read on, for a hands-on introduction to working with documents from the .NET SDK.

## [](#crud-operations)CRUD Operations

The core interface to Couchbase Server is simple KV operations on full documents. Make sure you’re familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK section](../hello-world/start-using-sdk.md).

See the [code sample](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/retrieving.cc) for use in context.

## [](#upsert)Upsert

|  | Sub-Document Operations All of these operations involve fetching the complete document from the Cluster. Where the number of operations or other circumstances make bandwidth a significant issue, the SDK can work on just a specific _path_ of the document with [Sub-Document Operations](subdocument-operations.md). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Here is a simple upsert operation, which will insert the document if it does not exist, or replace it if it does.

We use `lcb_cmdstore_create` for storing an item in Couchbase as it is only one operation with different set of attributes/constraints for storage modes.

```c
        lcb_cmdstore_create(&scmd, LCB_STORE_UPSERT);
        lcb_cmdstore_key(scmd, key.data(), key.size());
        lcb_cmdstore_value(scmd, value.data(), value.size());

        err = lcb_store(instance, nullptr, scmd);
        lcb_cmdstore_destroy(scmd);
        if (err != LCB_SUCCESS) {
            die("Couldn't schedule storage operation", err);
        }
        lcb_wait(instance, LCB_WAIT_DEFAULT);
```

## [](#insert)Insert

Insert works very similarly to upsert , but will fail if the document already exists.

```c
        lcb_cmdstore_create(&scmd, LCB_STORE_INSERT);
        lcb_cmdstore_key(scmd, key.data(), key.size());
        lcb_cmdstore_value(scmd, value.data(), value.size());

        err = lcb_store(instance, nullptr, scmd);
        lcb_cmdstore_destroy(scmd);
        if (err != LCB_SUCCESS) {
            die("Couldn't schedule storage operation", err);
        }
        lcb_wait(instance, LCB_WAIT_DEFAULT);
```

## [](#retrieving-documents)Retrieving documents

We’ve tried upserting and inserting documents into the Couchbase Server, let’s get them back:

```c
static void get_callback(lcb_INSTANCE *instance, int cbtype, const lcb_RESPGET *resp)
{
    lcb_STATUS rc = lcb_respget_status(resp);
    std::cerr << "=== " << lcb_strcbtype(cbtype) << " ===\n";
    if (rc == LCB_SUCCESS) {
        const char *key, *value;
        size_t nkey, nvalue;
        uint64_t cas;
        uint32_t flags;
        lcb_respget_key(resp, &key, &nkey);
        std::cerr << "KEY: " << std::string(key, nkey) << "\n";
        lcb_respget_cas(resp, &cas);
        std::cerr << "CAS: 0x" << std::hex << cas << "\n";
        lcb_respget_value(resp, &value, &nvalue);
        std::cerr << "VALUE: " << std::string(value, nvalue) << "\n";
        lcb_respget_flags(resp, &flags);
        std::cerr << "FLAGS: 0x" << std::hex << flags << "\n";

        {
            // This snippet lives inside the callback, so it is not necessary to call lcb_wait here
            lcb_CMDSTORE *cmd;
            lcb_cmdstore_create(&cmd, LCB_STORE_INSERT);
            lcb_cmdstore_key(cmd, key, nkey);
            lcb_cmdstore_value(cmd, value, nvalue);

            lcb_STATUS err = lcb_store(instance, nullptr, cmd);
            lcb_cmdstore_destroy(cmd);
            if (err != LCB_SUCCESS) {
                die("Couldn't schedule storage operation", err);
            }
        }
    } else {
        die(lcb_strcbtype(cbtype), rc);
    }
}
```

## [](#replace)Replace

A very common sequence of operations is to `get` a document, modify its contents, and `replace` it. So what is CAS?

CAS, or Compare and Swap, is a form of optimistic locking. Every document is Couchbase has a CAS value, and it’s changed on every mutation. When you get a document you also get the document’s CAS, and then when it is time to write the document, you send the same CAS back. If another thread or program has modified that document in the meantime, the Couchbase Server can detect you’ve provided a now-outdated CAS, and return an error. This provides cheap and safe concurrency. See this [this detailed description of CAS](concurrent-document-mutations.md) for further details.

In general, you’ll want to provide a CAS value whenever you `replace` a document, to prevent overwriting another agent’s mutations.

Setting a Compare and Swap (CAS) value is a form of optimistic locking - dealt with in depth in the [CAS page](concurrent-document-mutations.md). Here we just note that the CAS is a value representing the current state of an item; each time the item is modified, its CAS changes. The CAS value is returned as part of a document’s metadata whenever a document is accessed. Without explicitly setting it, a newly-created document would have a CAS value of _0_.

```c
            result = {}; // reset result object
            {
                lcb_CMDSTORE *cmd = nullptr;
                check(lcb_cmdstore_create(&cmd, LCB_STORE_REPLACE),
                        "create REPLACE command");
                check(lcb_cmdstore_key(cmd,
                                document_id.c_str(),
                                document_id.size()),
                        "assign ID for REPLACE command");
                check(lcb_cmdstore_value(cmd,
                                new_value.c_str(),
                                new_value.size()),
                        "assign value for REPLACE command");
                check(lcb_store(local_instance, &result, cmd),
                        "schedule REPLACE command");
                check(lcb_cmdstore_destroy(cmd), "destroy UPSERT command");
                lcb_wait(local_instance, LCB_WAIT_DEFAULT);

                if (result.rc != LCB_SUCCESS) {
                    std::stringstream msg;
                    msg << "failed to append " << item_value << ": "
                        << lcb_strerror_short(result.rc) << "\n";
                    std::cout << msg.str();
                }
            }
```

See the [code sample](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/cas.cc) for use in context.

## [](#durability)Durability

Writes in Couchbase are written to a single node, and from there the Couchbase Server will take care of sending that mutation to any configured replicas.

The optional `durability` parameter, which all mutating operations accept, allows the application to wait until this replication (or persistence) is successful before proceeding.

See the [code sample](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/expiration.cc) for use in context.

### [](#preferred-server-group-replica-reads)Preferred Server Group Replica Reads

|  | Preferred Server Group Replica Reads are only accessible with the C SDK working with Couchbase Server 7.6.2 or newer (Capella or self-managed), from SDK version 3.3.14\. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

[Server Groups](../../../server/current/learn/clusters-and-availability/groups.md#understanding-server-group-awareness)can be used to define subsets of nodes within a Couchbase cluster, which contain a complete set of vbuckets (active or replica). As well as high availability use cases, Servre Groups can also be used to keep much traffic within the same cloud Availability Zone.

For Capella users with high data volumes, egress charges for reads from other Availability Zones (AZ) in AWS can be a significant cost. The C SDK, when making read replica requests, can make a request to a preferred Server Group — in this case the local AZ — and set to always read from a copy of the document in this local zone. This is done by putting cluster nodes in the same AZ into the same [Server Group](../../../server/current/learn/clusters-and-availability/groups.md#server-groups-and-vbuckets), too.

This may mean the application has to be tolerant of slight inconsistencies, until the local replica catches up. Alternatively, it may demand a stronger level of durability, to ensure that all copies of a document are consistent before they are accessible — provided that this is `persistToMajority` with [no more than one replica](../../../server/current/learn/data/durability.md#majority).

Couchbase does not recommend this feature where read consistency is critical, but with the appropriate durability settings consistency can be favored ahead of availability.

|  | Replicas, Nodes, and Server Groups Implicit in the rules for durability, and the process of setting up Server Groups, is the following information — which we mention here explicitly to ensure it is all noted: Moving servers between Server Groups updates the clustermap immediately, but to move the data, an administrator **must** perform rebalance. Until the rebalance is complete, the SDK will see and be able to 'use' the new server groups, but the vBucketMap may still refer to data in the previous locations. The cluster should have enough nodes and group to make sure that copies of the same document are not stored on the same node, and each group has nodes that cover all 1024 vbuckets (in other words, the number of the groups does not exceeds number of the copies: active+num\_replicas). The Admin UI should emit small yellow warning if the configuration is considered unbalanced. Setting **three** replicas for the bucket [disables durability for sync writes](../../../server/current/learn/data/durability.md#majority), also precluding the use of [multi-document ACID transactions](#concept-docs:transactions.adoc). |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#atomic-counters)Atomic Counters

The numeric content of a document can be manipulated using [lcb\_RESPCOUNTER](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/group%5F%5Flcb-counter.html).

|  | Increment & Decrement are considered part of the ‘binary’ API and as such may still be subject to change. |
|  | --------------------------------------------------------------------------------------------------------- |

Counter opeations treat the document as a numeric value (the document must contain a parseable integer as its content). This value may then be incremented or decremented.

```c
        check(lcb_cmdcounter_create(&cmd), "create COUNTER command");
        check(lcb_cmdcounter_key(cmd, document_id.c_str(), document_id.size()),
                "assign ID for COUNTER command");
        check(lcb_cmdcounter_initial(cmd, 100), "assign initial value for COUNTER command");
        check(lcb_cmdcounter_delta(cmd, 20), "assign delta value for COUNTER command");
        check(lcb_counter(instance, nullptr, cmd), "schedule COUNTER command");
        check(lcb_cmdcounter_destroy(cmd), "destroy COUNTER command");
        lcb_wait(instance, LCB_WAIT_DEFAULT);
```

See the [code sample](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/counter.cc) for use in context.

|  | Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the Touch() method. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#atomicity-across-data-centers)Atomicity Across Data Centers

If you are using [Cross Data Center Replication](../../../server/current/manage/manage-xdcr/xdcr-management-overview.md) (XDCR), be sure to avoid modifying the same counter in more than one datacenter. If the same counter is modified in multiple datacenters between replications, the counter will no longer be atomic, and its value can change in unspecified ways.

A counter must be incremented or decremented by only a single datacenter. Each datacenter must have its own set of counters that it uses — a possible implementation would be including a datacenter name in the counter document ID.

## [](#additional-resources)Additional Resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements - see the [Sub-Document](subdocument-operations.md) pages. For working with metadata on a document, reference our [Extended Attributes](#sdk-xattr-example.adoc) pages.

Our [Query Engine](n1ql-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of SQL++ (formerly N1QL).