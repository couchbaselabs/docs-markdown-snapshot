[View original HTML](/cxx-sdk/current/project-docs/migrating-sdk-code-to-3.n.html)

> This is the first major release of the Couchbase C++ SDK — you will not have any code based upon older API versions. 

Couchbase C++ SDK 1.2 implements the Couchbase SDK 3.8 API. 1.x is the first release of the Couchbase C++ SDK, there are no releases implementing older APIs.

## [](#legacy-mapreduce-views)Legacy MapReduce Views

Note, if you are looking for information about Couchbase’s legacy MapReduce Views Service, MapReduce Views are deprecated in Couchbase Server, and will eventually be removed. Information on using MapReduce Views with the SDK can still be accessed in our [documentation archive](https://docs-archive.couchbase.com/scala-sdk/1.2/howtos/view-queries-with-sdk.html).

Views are the only service which does not benefit from [Multi-Dimensional Scaling](../../../server/current/learn/services-and-indexes/services/services.md#services-and-multi-dimensional-scaling), and is rarely the best choice over, say, [our Query service](../howtos/sqlpp-queries-with-sdk.md) if you are starting a fresh application. See our discussion document on [the best service for your use case](../concept-docs/querying-your-data.md) for querying your data.