---
title: Caching Example
description: A walk-through of the basics of Key-Value operations with
  Couchbase, through the lens of a REST api caching layer.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.5/modules/howtos/pages/caching-example.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.5@python-sdk:howtos:caching-example.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.5/howtos/caching-example.html)

# Caching Example

> A walk-through of the basics of Key-Value operations with Couchbase, through the lens of a REST api caching layer. 

This example uses [Flask](https://pypi.org/project/Flask/) as a web-framework for a Python REST API. Flask has no direct support for async, but another code sample is available demonstrating this whole application using the Couchbase async API [here](https://github.com/couchbase/docs-sdk-python/blob/release/3.1/modules/howtos/examples/caching%5Ffastapi.py). You can also find the [full code for _this_ example here](https://github.com/couchbase/docs-sdk-python/blob/release/3.1/modules/howtos/examples/caching%5Fflask.py).

## [](#basic-endpoint)Basic Endpoint

Our first basic endpoints will be a get and set call, using HTTP methods `GET` and `POST` and Couchbase methods `get` and `insert` respectively:

GET

```python
@app.route('/<key>', methods=['GET'])
def get(key):
    try:
        res = cb.get(key)
        return jsonify(res.content_as[dict])
    except DocumentNotFoundException:
        return 'Key not found', 404
    except CouchbaseException as e:
        return 'Unexpected error: {}'.format(e), 500
```

POST

```python
@app.route('/<key>', methods=['POST'])
def post(key):
    try:
        cb.insert(key, request.json, expiry=EXPIRY)
        return 'OK'
    except DocumentExistsException:
        return 'Key already exists', 409
    except CouchbaseException as e:
        return 'Unexpected error: {}'.format(e), 500
```

This is the simplest API we can make — allowing us to set and get arbitrary JSON from any key we specify. We also include the `expiry` parameter, which will automatically delete the document (invalidate the cache) after a set amount of time.

## [](#cache-miss)Cache Miss

There are many ways this can and could be improved upon for real world use. What happens in the case of a cache miss? With this code, we handle the `DocumentNotFoundException` and respond with a HTTP 404.

```python
@app.route('/<key>', methods=['GET'])
def get(key):
    try:
        res = cb.get(key)
        return jsonify(res.content_as[dict])
    except DocumentNotFoundException:
        return 'Key not found', 404
    except CouchbaseException as e:
        return 'Unexpected error: {}'.format(e), 500
```

## [](#error-handling)Error Handling

We can also improve the POST function to deal with some of the errors it may encounter. Even if something unexpected happens, we can still be helpful by including the error in the 500 response, and by catching any `CouchbaseException` as a fallback:

```python
@app.route('/<key>', methods=['POST'])
def post(key):
    try:
        cb.insert(key, request.json, expiry=EXPIRY)
        return 'OK'
    except DocumentExistsException:
        return 'Key already exists', 409
    except CouchbaseException as e:
        return 'Unexpected error: {}'.format(e), 500
```

The last thing we'll do is add `PUT` and `DELETE` endpoints, matching up to the Couchbase operations `upsert` and `remove`, and apply the same error handling once more:

PUT

```python
@app.route('/<key>', methods=['PUT'])
def put(key):
    try:
        cb.upsert(key, request.json, expiry=EXPIRY)
        return 'OK'
    except CouchbaseException as e:
        return 'Unexpected error: {}'.format(e), 500
```

DELETE

```python
@app.route('/<key>', methods=['DELETE'])
def delete(key):
    try:
        cb.remove(key)
        return 'OK'
    except DocumentNotFoundException:
        # Document already deleted / never existed
        return 'Key does not exist', 404
```

## [](#additional-resources)Additional Resources

* You can find the full contextualized code from this sample [here](https://github.com/couchbase/docs-sdk-python/blob/release/3.1/modules/howtos/examples/caching%5Fflask.py).
* Selecting an [ephemeral or Memcached bucket](../../../server/current/learn/buckets-memory-and-storage/buckets.md#bucket-types) for the advantages of purely in-memory storage may make sense as a design decision.
* A webinar, a whitepaper, and other high-level information on choosing Couchbase as a caching layer is [on the main Couchbase website](https://www.couchbase.com/caching-comparison).