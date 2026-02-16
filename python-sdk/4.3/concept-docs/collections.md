[View original HTML](/python-sdk/4.3/concept-docs/collections.html)

> Fully supported in Couchbase Server 7.0\. 

The Collections feature in Couchbase Server is fully implemented in the 3.2 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#7.6@server:learn:data:scopes-and-collections.adoc).

## [](#using-collections-scope)Using Collections & Scope

Access a non-default collection, in the default scope, with:

```python
bucket.collection("flights")
```

And for a non-default scope:

```python
bucket.scope("marlowe_agency").collection("flights")
```

## [](#further-reading)Further Reading

* Please see the [Collections Overview documents](../../../server/7.6/learn/data/scopes-and-collections.md) in the Server docs.
* To see Collections in action, take a look at our [Collections-enabled Travel Sample page](../hello-world/sample-application.md).