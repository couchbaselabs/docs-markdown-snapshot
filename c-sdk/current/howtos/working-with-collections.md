---
title: Working with Collections
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/working-with-collections.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:c-sdk:howtos:working-with-collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/c-sdk/current/howtos/working-with-collections.html)

# Working with Collections

> The 3.x API SDKs all work with all features of Collections and Scopes. 

The [Collections feature](../../../server/current/learn/data/scopes-and-collections.md) in Couchbase Server 7.x is fully implemented in the 3.x API versions of the Couchbase SDKs.

> [!NOTE]
> When working with versions earlier than 7.0, the `defaultcollection` is used from the SDK.

Read more about [Collections and Scopes](../concept-docs/collections.md).

## [](#sample-application)Sample Application

The [Travel Sample Application](../hello-world/sample-application.md) has been updated with a motivating example for Collections - a multi-tenanted travel application. Imagine that we are providing a white-label Flight and Hotel booking service to multiple travel agents. Each tenant agent will get the same underlying service, but interact only with their own data.

The `travel-sample` bucket has been split into _Scopes_ for multiple tenant travel agents (for example `tenant_agent_00`, `tenant_agent_01`, …​) and a shared `inventory` which is further subdivided into _Collections_ such as `hotels` and `airports`.

Read more about the new travel-sample [Data Model](../ref/travel-app-data-model.md).

The app is currently implemented for the following SDKs:

* [Go](#2.3@go-sdk:hello-world:sample-application.adoc)
* [Java](#3.2@java-sdk:hello-world:sample-application.adoc)
* [Java Spring Data](#3.2@java-sdk:hello-world:spring-data-sample-application.adoc)
* [.NET](#3.2@dotnet-sdk:hello-world:sample-application.adoc)
* [Node.js](#3.2@nodejs-sdk:hello-world:sample-application.adoc)
* [PHP](#3.2@php-sdk:hello-world:sample-application.adoc)
* [Python](#3.2@python-sdk:hello-world:sample-application.adoc)
* [Scala](#1.2@scala-sdk:hello-world:sample-application.adoc)
* [Ruby](#3.2@ruby-sdk:hello-world:sample-application.adoc)

## [](#example-code)Example code

In the following example, we will use `NULL` for default collection, which covers the whole Bucket. To use named Collections (and Scopes), just substitute the Collection (and Scope) name for `NULL`.

```c
static void store_callback(lcb_INSTANCE *instance, int cbtype, const lcb_RESPSTORE *resp)
{
    const char *key;
    size_t nkey;
    uint64_t cas;
    lcb_respstore_key(resp, &key, &nkey);
    lcb_respstore_cas(resp, &cas);
    printf("status: %s, key: %.*s, CAS: 0x%" PRIx64 "\n",
       lcb_strerror_short(lcb_respstore_status(resp)), (int)nkey, key, cas);
}

lcb_install_callback3(instance, LCB_CALLBACK_STORE, (lcb_RESPCALLBACK)store_callback);

lcb_STATUS rc;
lcb_CMDSTORE *cmd;
const char *collection = NULL, *scope = NULL;
size_t collection_len = 0, scope_len = 0;
const char *key = "my-document";
const char *value = "{\"name\": \"mike\"}";
rc = lcb_cmdstore_create(&cmd, LCB_STORE_UPSERT);
rc = lcb_cmdstore_collection(cmd, scope, scope_len, collection, collection_len);
rc = lcb_cmdstore_key(cmd, key, strlen(key));
rc = lcb_cmdstore_value(cmd, value, strlen(value));
rc = lcb_store(instance, NULL, cmd);
rc = lcb_cmdstore_destroy(cmd);
rc = lcb_wait(instance);
```

```c
static void get_callback(lcb_INSTANCE *instance, int cbtype, const lcb_RESPGET *resp)
{
    const char *key, *value;
    size_t nkey, nvalue;
    uint64_t cas;
    lcb_respget_key(resp, &key, &nkey);
    lcb_respget_value(resp, &value, &nvalue);
    lcb_respget_cas(resp, &cas);
    printf("status: %s, key: %.*s, CAS: 0x%" PRIx64 "\n",
       lcb_strerror_short(lcb_respget_status(resp)), (int)nkey, key, cas);
    printf("value:\n%s\n", (int)nvalue, value);
}

lcb_install_callback3(instance, LCB_CALLBACK_GET, (lcb_RESPCALLBACK)get_callback);

lcb_STATUS rc;
lcb_CMDGET *cmd;
const char *collection = NULL, *scope = NULL;
size_t collection_len = 0, scope_len = 0;
const char *key = "my-document";
rc = lcb_cmdget_create(&cmd);
rc = lcb_cmdget_collection(cmd, scope, scope_len, collection, collection_len);
rc = lcb_cmdget_key(cmd, key, strlen(key));
rc = lcb_get(instance, NULL, cmd);
rc = lcb_cmdget_destroy(cmd);
rc = lcb_wait(instance);
```