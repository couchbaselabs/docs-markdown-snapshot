---
title: Error Handling
description: Errors are inevitable. The developer's job is to be prepared for
  whatever is likely to come up -- and to try and be prepared for anything that
  conceivably could come up.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.4/modules/howtos/pages/error-handling.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:4.4@python-sdk:howtos:error-handling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.4/howtos/error-handling.html)

# Error Handling

> Errors are inevitable. The developer's job is to be prepared for whatever is likely to come up — and to try and be prepared for anything that conceivably could come up. 

Couchbase gives you a lot of flexibility, but it is recommended that you equip yourself with an understanding of the possibilities.

## [](#how-the-sdk-handles-exceptions)How the SDK Handles Exceptions

Couchbase-specific exceptions are all derived from `CouchbaseException`. Errors that cannot be recovered by the SDK will be returned to the application. These unrecoverable errors are left to the application developer to handle — this section covers handling many of the common error scenarios.

## [](#handling-exceptions)Handling Exceptions

The Python SDK works directly with the built in exception handling available in Python. This enables you to catch, interrogate, and handle or log them and continue. Depending on the type of the exception you catch, there are a number of properties which will be available to you. Couchbase-specific exceptions are all derived from `CouchbaseException`.

How you handle exceptions in your application will depend upon the type of exception thrown. Is it transient? Is it even recoverable? Below we examine error handling strategies in relation to the Couchbase SDKs, then take a practical walk through some common error scenarios you are likely to have to handle when working with a Couchbase cluster.

### [](#failing)Failing

While most of the time you want more sophisticated exception handling strategies, sometimes you just need to fail. It makes no sense for some exceptions to be retried, either because they are not transient, or because you already tried everything to make it work and it still keeps failing. If containment is not able to handle the exception, then it needs to propagate up to a parent component that can handle it.

For synchronous programs, every error is converted into an Exception and thrown so that you can use regular `try`/`except` semantics.

```python
try:
    res = collection.get("not-a-key")
except CouchbaseException:
    # we can handle any exceptions thrown here.
    pass
```

If you do not catch the Exception, it will bubble up:

```python
Traceback (most recent call last):
  File "../sample_code/3x/docs/error_handling.py", line 21, in <module>
    res = collection.get("not-a-key")
  File "../.virtualenvs/cb-sample-py3.9.5/lib/python3.9/site-packages/couchbase/collection.py", line 293, in wrapped
    return func(self, *args, **kwargs)
  File "../.virtualenvs/cb-sample-py3.9.5/lib/python3.9/site-packages/couchbase/result.py", line 507, in wrapped
    x, options = func(*args, **kwargs)
  File "../.virtualenvs/cb-sample-py3.9.5/lib/python3.9/site-packages/couchbase/collection.py", line 521, in get
    return self._get_generic(key, kwargs, options)
  File "../.virtualenvs/cb-sample-py3.9.5/lib/python3.9/site-packages/couchbase/collection.py", line 484, in _get_generic
    x = CoreClient.get(self.bucket, key, **opts)
  File "../.virtualenvs/cb-sample-py3.9.5/lib/python3.9/site-packages/couchbase_core/client.py", line 409, in get
    return super(Client, self).get(*args, **kwargs)
couchbase.exceptions.DocumentNotFoundException: <Key='not-a-key', RC=0x12D[LCB_ERR_DOCUMENT_NOT_FOUND (301)], Operational Error, Results=1, C Source=(src/multiresult.c,332), Context={'status_code': 1, 'opaque': 1, 'cas': 0, 'key': 'not-a-key', 'bucket': 'travel-sample', 'collection': 'hotel', 'scope': 'inventory', 'context': '', 'ref': '', 'endpoint': '172.23.111.139:11210', 'type': 'KVErrorContext'}, Tracing Output={"not-a-key": {"debug_info": {"FILE": "src/callbacks.c", "FUNC": "value_callback", "LINE": 848}}}>
```

### [](#logging)Logging

It is always important to log errors, but even more so in the case of reactive applications. Because of the event driven nature, stack traces get harder to look at, and caller context is sometimes lost.

### [](#retry)Retry

Transient errors — such as those caused by resource starvation — are best tackled with one of the following retry strategies:

* Retry with an exponentially increasing delay and a delay ceiling.
* Retry with a linearly increasing delay and a delay ceiling.
* Retry with a fixed delay.
* Retry with a random delay.
* Retry immediately (not preferred) with a limit of retries.

Retrying immediately may be appropriate in some situations, but is not as preferred as it can lead to pathological failure type situations where an exhausted resource is put under further load and never has a chance to recover.

Consider a decorator that provides flexibility to determine which Exceptions to retry and how to retry (fixed, linear or exponential delay).

```python
def allow_retries(retry_limit=3,                # type: int
                  backoff=1.0,                  # type: float
                  exponential_backoff=False,    # type: bool
                  linear_backoff=False,         # type: bool
                  allowed_exceptions=None       # type: Optional[Tuple]
                  ) -> Callable:
    def handle_retries(func):
        @functools.wraps(func)
        def func_wrapper(*args, **kwargs):
            for retry_num in reversed(range(retry_limit)):
                try:
                    return func(*args, **kwargs)
                except Exception as ex:
                    if allowed_exceptions is None or not isinstance(ex, allowed_exceptions):
                        raise

                    if retry_num == 0:
                        raise

                    delay = backoff
                    if exponential_backoff is True:
                        delay *= (2**retry_num)
                    elif linear_backoff is True:
                        delay *= (retry_num+1)

                    print(f"Retries left: {retry_num}")
                    print(f"Backing Off: {delay} seconds")
                    time.sleep(delay)

        return func_wrapper
    return handle_retries


@allow_retries(retry_limit=5,
               backoff=0.5,
               allowed_exceptions=(CASMismatchException))
def update_with_cas(collection,    # type: str
                    doc_key       # type: str
                    ) -> bool:

    result = collection.get(doc_key)
    content = result.content_as[dict]
    reviews = content.get("reviews", 0)
    content["total_reviews"] = reviews if reviews == 0 else len(reviews)
    collection.replace(doc_key, content, ReplaceOptions(cas=result.cas))


key = "hotel_10026"
update_with_cas(collection, key)
```

## [](#key-value-exceptions)Key-Value Exceptions

The KV Service exposes several common errors that can be encountered - both during development, and to be handled by the production app. Here we will cover some of the most common errors.

If a particular key cannot be found a `DocumentNotFoundException` is raised:

```python
try:
    key = "not-a-key"
    res = collection.get(key)
except DocumentNotFoundException:
    print("doc with key: {} does not exist".format(key))
```

On the other hand if the key already exists and should not (e.g. on an insert) then a `DocumentExistsException` is raised:

```python
try:
    key = "hotel_10026"
    res = collection.insert(
        key, {"title": "New Hotel", "name": "The New Hotel"})
except DocumentExistsException:
    print("doc with key: {} already exists".format(key))
```

### [](#cas-mismatch)CAS Mismatch

Couchbase provides optimistic concurrency using CAS. Each document gets a CAS value on the server, which is changed on each mutation. When you get a document you automatically receive its CAS value, and when replacing the document, if you provide that CAS the server can check that the document has not been concurrently modified by another agent in-between. If it has, it returns `CASMismatchException`. See the [Retry](#retry) section for an approach to retry in this scenario.

```python
try:
    result = collection.get("hotel_10026")
    collection.replace("hotel_10026", {}, cas=result.cas)
except CASMismatchException:
    # the CAS value has changed
    pass
```

### [](#ambiguity)Ambiguity

There are situations with any distributed system in which it is simply impossible to know for sure if the operation completed successfully or not. Take this as an example: your application requests that a new document be created on Couchbase Server. This completes, but, just before the server can notify the client that it was successful, a network switch dies and the application's connection to the server is lost. The client will timeout waiting for a response and will raise a `TimeoutException`, but it's ambiguous to the app whether the operation succeeded or not.

Another ambiguous exception is `DurabilitySyncWriteAmbiguousException`, which can returned when performing a durable operation. This also indicates that the operation may or may not have succeeded: though when using durability you are guaranteed that the operation will either have been applied to all replicas, or none.

Given the inevitability of ambiguity, how is the application supposed to handle this?

This needs to be considered case-by-case, but the general strategy is to become certain if the operation succeeded or not, and to retry it if required.

For instance, consider inserts: on an ambiguous Exception, you can simply **retry** the insert. If it now fails with a `DocumentExistsException`, we know that the previous operation was in fact successful:

```python
for i in range(5):
    try:
        durability = ServerDurability(level=Durability.PERSIST_TO_MAJORITY)
        collection.insert(
            "my-key", {"title": "New Hotel"}, InsertOptions(durability=durability))
    except (DocumentExistsException, DurabilitySyncWriteAmbiguousException,) as ex:
        # if previously retried and the document now exists,
        # we can assume it was written successfully by a previous ambiguous exception
        if isinstance(ex, DocumentExistsException) and i > 0:
            continue

        # simply retry the durable operation again
        if isinstance(ex, DurabilitySyncWriteAmbiguousException):
            continue

        # raise the exception if not DocumentExistsException, DurabilitySyncWriteAmbiguousException
        raise
```

### [](#non-idempotent-operations)Non-Idempotent Operations

An "Idempotent operation" is one that can be applied multiple times yet still have the same effect, exactly once.

* Repeatedly setting an email field is Idempotent. (If you do it twice, the email field will have the same, expected value.)
* Increasing a counter by one is Non-Idempotent. (If you do it twice, the result will now have increased by **2**.)

We can view some operations as idempotent because they will fail with no effect after the first success. This was the case for inserts, as we saw above.

Idempotent operations are much easier to handle, as on ambiguous error results (`DurabilitySyncWriteAmbiguousException` and `TimeoutException`) the operation can simply be retried.

Most key-value operations are idempotent. Non-Idempotent operations include a Sub-Document arrayAppend call, or a counter increment. After an ambiguous exception on a Non-Idempotent operation, you should first read the document to check for yourself whether or not that change was applied.

## [](#query-and-analytics-errors)Query and Analytics Errors

A SQL++ (formerly N1QL) query either returns results or will throw an error with a `QueryErrorContext`, like so:

```python
try:
    cluster.query("SELECT * FROM no_such_bucket").rows()
except CouchbaseException as ex:
    if isinstance(ex.context, QueryErrorContext):
        # We have a Query error context, we can print out some useful information:
        print(ex.context.statement)
        print(ex.context.first_error_code)
        print(ex.context.first_error_message)
        print(ex.context.client_context_id)
        print(ex.context.endpoint)
```

Analytics works in an identical fashion, potentially raising an analytics specific error and having an `AnalyticsErrorContext`.

## [](#additional-resources)Additional Resources

Errors & Exception handling is an expansive topic. Here, we have covered examples of the kinds of exception scenarios that you are most likely to face. More fundamentally, you also need to weigh up [concepts of durability](../concept-docs/durability-replication-failure-considerations.md).

Diagnostic methods are available to check on the [health if the cluster](health-check.md), and the [health of the network](#tracing-from-the-sdk.adoc).

Logging methods are dependent upon the platform and SDK used. We offer [recommendations and practical examples](collecting-information-and-logging.md).