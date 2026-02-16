[View original HTML](/dotnet-sdk/3.6/project-docs/third-party-integrations.html)

> The Couchbase .NET SDK is often used with unofficial and third party tools and applications to integrate into broader language and platform ecosystems, and across data lakes in heterogeneous environments. 

Couchbase SDKs are often used with unofficial and third party tools and applications to integrate into broader language and platform ecosystems, and across data lakes in heterogeneous environments. These are some of the applications that you need to be aware of.

## [](#across-the-ecosystem)Across the Ecosystem

Although unsupported, and not maintained by Couchbase, several projects are worth a look at. We offer brief notes on what you should consider if integrating with them:

Linq2Couchbase creates a lightweight ORM/ODM for querying Couchbase buckets using LINQ as the lingua-franca between your application and Couchbase Server using Couchbase’s SQL++ for JSON documents. It also provides a write API for performing CRUD operations on JSON documents.

* <https://www.nuget.org/packages/Linq2Couchbase>