---
title: Choosing an API
description: Async &amp; batching
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/concurrent-async-apis.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:c-sdk:howtos:concurrent-async-apis.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/c-sdk/current/howtos/concurrent-async-apis.html)

# Choosing an API

> Async & batching 

Libcouchbase is an asynchronous client that may also be used in blocking mode. The library contains I/O plugins for common libraries such as _libevent_, _libev_, and _libuv_, and a libevent-based example can be found [here](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/example%5F2libeventdirect%5F2main%5F8c-example.html).

Batching examples are given for [bulk store](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/bulk-store.cc) and for [bulk get](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/bulk-get.cc).

## [](#usage-differences-in-non-blocking-mode)Usage Differences in Non-Blocking Mode

For the most part, programming with libcouchbase is the same regardless of whether you're using it in a blocking or non-blocking application. There are some key differences to note, however:

* `lcb_wait()` should not be called in non-blocking mode. By definition, the `lcb_wait()` routine will block the application until all pending I/O completes. In non-blocking mode the pending I/O is completed when control is returned back to the event loop.
* You must not schedule operations until the bootstrap callback, `lcb_set_bootstrap_callback()`, has been invoked. This is because operations must be forwarded to a destination node in the cluster depending on the key specified within the operation. Until the client has been bootstrapped it does not know how to forward keys to any nodes.  
Unlike blocking mode where you may simply do:  
```c  
lcb_connect(instance);  
lcb_wait(instance);  
if (lcb_get_bootstrap_status(instance) == LCB_SUCCESS)) {  
  // Start operations  
}  
```  
You need to use the callback variant that notifies your application when the library is ready.
* You are responsible for ensuring that the `iops` structure passed to the library remains valid until `lcb_destroy` is invoked. Likewise, you are responsible for freeing the `iops` structure via `lcb_destroy_io_opts()` when it is no longer required.
* Currently the library does blocking DNS look-ups via the standard `getaddrinfo()` call. Typically this should not take a long time but may potentially block your application if an invalid host name is detected or the DNS server in use is slow to respond.

## [](#batching)Batching

The most simplistic bulk fetch looks like this:

```c
    // Make a list of keys to store initially
    std::vector<std::string> keys_to_get{"foo", "bar", "baz"};

    std::vector<Result> results;
    results.reserve(keys_to_get.size());

    lcb_sched_enter(instance);
    for (const auto &key : keys_to_get) {
        lcb_CMDGET *cmd = nullptr;
        check(lcb_cmdget_create(&cmd), "create GET command");
        check(lcb_cmdget_key(cmd, key.c_str(), key.size()), "assign ID for GET command");
        lcb_STATUS rc = lcb_get(instance, &results, cmd);
        check(lcb_cmdget_destroy(cmd), "destroy GET command");
        if (rc != LCB_SUCCESS) {
            std::cerr << "[ERROR] could not schedule GET for " << key << ": "
                      << lcb_strerror_short(rc) << "\n";
            // Discards all operations since the last scheduling context (created by lcb_sched_enter)
            lcb_sched_fail(instance);
            break;
        }
    }
    lcb_sched_leave(instance);
    check(lcb_wait(instance, LCB_WAIT_DEFAULT), "wait for batch to complete");
```