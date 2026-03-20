---
title: Handling Errors with the C SDK
description: How to handle errors when programming with the C SDK.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/error-handling.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:c-sdk:howtos:error-handling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/c-sdk/current/howtos/error-handling.html)

# Handling Errors with the C SDK

> How to handle errors when programming with the C SDK. 

Errors are inevitable. The developer’s job is to be prepared for whatever is likely to come up — and to try and be prepared for anything that conceivably could come up. Couchbase gives you a lot of flexibility, but it is recommended that you equip yourself with an understanding of the possibilities.

## [](#how-the-sdk-handles-errors)How the SDK Handles Errors

Couchbase-specific errors in the C SDK have a common underlying implementation. Errors that cannot be recovered by the SDK will be returned to the application. These unrecoverable errors are left to the application developer to handle.

## [](#error-handling-strategies)Error Handling Strategies

The specific error handling strategy required will depend upon the type of error thrown and how it affects the application. Is it transient? Is it even recoverable? Below we examine some general error handling strategies in relation to the Couchbase SDKs.

### [](#failing)Failing

While most of the time you want more sophisticated error handling strategies, sometimes you just need to fail gracefully. It makes no sense for some errors to be retried, either because they are not transient, or because you already tried everything to make it work and it still keeps failing. If containment is not able to handle the error, then it needs to propagate up to a parent component that can handle it, or perhaps made visible via monitoring or alerting systems.

### [](#logging)Logging

It is always important to log errors, but even more so in the case of reactive or event driven applications. The specific context of an operation can be lost and stack traces get harder to look at. This SDK has several ways to obtain additional context from the errors that are reported which are helpful when logging.

We have also documented how to [collect information and logging](collecting-information-and-logging.md) that is useful when using this SDK.

### [](#retry)Retry

Transient errors — such as those caused by resource starvation — are best addressed with application logic that implements one of the following retry strategies:

* Retry immediately.
* Retry with a fixed delay.
* Retry with a linearly increasing delay.
* Retry with an exponentially increasing delay.
* Retry with a random delay.

In addition to application specific retry logic, a **global retry strategy** can also be configured. See the [lcb\_retry\_strategy()](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/group%5F%5Flcb-error-codes.html#gae5e21e2fe95c1e8ef890719bbb582e89) function in the API reference.

## [](#error-handling-constructs)Error Handling Constructs

There are several error handling constructs to be aware of when working with the C SDK.

### [](#error-codes-metadata)Error Codes & Metadata

The `lcb_STATUS` enum is returned by most functions in this SDK and it contains all of the error codes that could be returned (e.g., `LCB_SUCCESS`, `LCB_ERR_TIMEOUT`, `LCB_ERR_DOCUMENT_NOT_FOUND`). Each error code has an associated text description and a specific `lcb_ERROR_TYPE` and some also have additional `lcb_ERROR_FLAGS` that can be used with macros (e.g., `lcb_error_flags()` and `LCB_ERROR_IS_TRANSIENT`). The response callbacks also have error codes that indicate the result of the scheduled command.

### [](#utility-functions-and-macros)Utility Functions and Macros

In addition to the error codes themselves, there are several utility functions and macros that can be useful when handling errors. The most obvious are `lcb_strerror_short()` and `lcb_strerror_long()` which provide a textual description of the error that can be used for logging and similar purposes. There are also a series of macros (e.g, `LCB_ERROR_IS_TRANSIENT`, `LCB_ERROR_IS_FATAL`) that can test for special flags that indicate special cases.

### [](#additional-error-context)Additional Error Context

As previously stated, response callbacks have error codes that indicate the result of the scheduled command. However, when an error is present, they also have additional error context that can may be useful for error handling or logging. The general form of those functions are `lcb_XXXX_error_context()` and then their associated helpers are in the form of `lcb_errctx_XXXX_DATA()`. Some examples are shown below, but review the references in [Error Code API Reference](#error-code-api-reference) for more.

A few examples:

* **KV Store Response Error Context:** `lcb_respstore_error_context()` returns a `lcb_KEY_VALUE_ERROR_CONTEXT` that can be passed to the `lcb_errctx_kv_` series of functions for more info (e.g., `lcb_errctx_kv_key()` gets the key).
* **Query Response Error Context:** `lcb_respquery_error_context()` returns a `lcb_QUERY_ERROR_CONTEXT` that can be passed to the `lcb_errctx_query_` series of functions for more info (e.g., `lcb_errctx_query_first_error_message()` gets the first error message).
* **Search Response Error Context:** `lcb_respsearch_error_context()` returns a `lcb_SEARCH_ERROR_CONTEXT` that can be passed to the `lcb_errctx_search_` series of functions for more info (e.g., `lcb_errctx_search_http_response_body()` gets the underlying HTTP response body).

## [](#additional-resources)Additional Resources

Error handling can be an expansive topic. We have provided some general guidance and references that can be useful for error handling, but each application must carefully consider strategies that are most appropriate for their requirements. More fundamentally, you should also review the related topics and references listed below.

### [](#related-topics)Related Topics

Consider the [concepts of durability](../concept-docs/durability-replication-failure-considerations.md) that may have a role in your overall error handling strategy as well as any [client settings](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/group%5F%5Flcb-cntl-settings.html) that can control timeouts and retry logic.

Diagnostic methods are available to check on the [health of the cluster](health-check.md), and the [health of the network](tracing-from-the-sdk.md).

Logging methods are dependent upon the platform and SDK used. We offer [recommendations and practical examples](collecting-information-and-logging.md).

### [](#error-code-api-reference)Error Code API Reference

The [Error Codes](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/group%5F%5Flcb-error-codes.html) section of the API reference documentation is a good starting point to read about the various error codes and related functions.

However, the [libcouchbase error header file](https://github.com/couchbase/libcouchbase/blob/3.3.18/include/libcouchbase/error.h) is the definitive source which declares all error codes that can be returned and all related utility functions that can be used to obtain additional context.