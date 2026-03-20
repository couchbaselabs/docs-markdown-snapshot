---
title: Concurrent Document Mutations
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/concurrent-document-mutations.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:c-sdk:howtos:concurrent-document-mutations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/c-sdk/current/howtos/concurrent-document-mutations.html)

# Concurrent Document Mutations

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::6.6@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::6.6@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::6.6@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::6.6@sdk:shared:partial$cas.adoc\[\]

```c
{
    lcb_CMDGET *cmd = nullptr;
    check(lcb_cmdget_create(&cmd), "create GET command");
    check(lcb_cmdget_key(cmd, document_id.c_str(), document_id.size()),
            "assign ID for GET command");
    /**
     * Time in seconds, note that the server might reset time to default, if it larger than
     * maximum time (both durations are configurable). The following command will help to
     * discover effective values for the feature.
     *
     * $ cbstats -u Administrator -p password  localhost all | grep ep_getl
     * ep_getl_default_timeout:                               15
     * ep_getl_max_timeout:                                   30
     */
    check(lcb_cmdget_locktime(cmd, 5), "lock for 5 seconds");
    check(lcb_get(local_instance, &result, cmd), "schedule GET command");
    check(lcb_cmdget_destroy(cmd), "destroy GET command");
    lcb_wait(local_instance, LCB_WAIT_DEFAULT);

    if (result.rc == LCB_ERR_DOCUMENT_LOCKED
            || result.rc == LCB_ERR_TEMPORARY_FAILURE) {
        std::stringstream msg;
        msg << "Document is locked for " << item_value
            << ". Retrying in 100 milliseconds...\n";
        std::cout << msg.str();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        continue;
    } else {
        check(result.rc, "could not find list document");
    }
    cas = result.cas;
}
```

Sometimes more logic is needed when performing updates, for example, if a property is mutually exclusive with another property; only one or the other can exist, but not both.

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::6.6@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::6.6@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::6.6@sdk:shared:partial$cas.adoc\[\]

```c
    check(lcb_cmdstore_cas(cmd, cas), "assign CAS value for REPLACE command");
```

The handler will unlock the item implicitly via modifying the item with the correct CAS.

If the item has already been locked, the server will respond with CasMismatch which means that the operation could not be executed temporarily, but may succeed later on.

## [](#apis-and-additional-information)APIs and Additional Information

API information for working with CAS can be found [in our API docs](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/group%5F%5Flcb-kv-api.html).

A fully worked example can be found [here](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/cas.cc) and [here](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/pessimistic-lock.cc).