---
title: Couchbase Ruby SDK 3.7
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.7/modules/hello-world/pages/overview.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:ruby-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/hello-world/overview.html)

# Couchbase Ruby SDK 3.7

# Couchbase Ruby SDK 3.7

```ruby
agent_scope = bucket.scope("tenant_agent_00")
users_collection = agent_scope.collection("users")
document = {"name" => "John Doe", "preferred_email" => "johndoe111@test123.test"}

result = users_collection.upsert("user-key", document)
```

The Couchbase Ruby SDK allows you to connect to a Couchbase cluster from Ruby. The Ruby SDK includes high-performance native Ruby extensions to handle communicating to the cluster over Couchbase’s binary protocols.

  
##  Use Your Database

How-to guides to help you start your development journey with Couchbase and the Ruby SDK.

Get Started

* [Start Using the Ruby SDK](start-using-sdk.md)
* [Data Operations](../howtos/kv-operations.md)
* [Query](../howtos/n1ql-queries-with-sdk.md)
* [Search](../howtos/full-text-searching-with-sdk.md)
* [Sample Application](sample-application.md)

Work with Data

* [Sub-Document Operations](../howtos/subdocument-operations.md)
* [Analytics](../howtos/analytics-using-sdk.md)
* [Organize Data with Collections](../howtos/working-with-collections.md)

Manage Couchbase

* [Managing Connections](../howtos/managing-connections.md)
* [Authentication](../howtos/sdk-authentication.md)
* [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md)
* [User Management](../howtos/sdk-user-management-example.md)

Explore Errors & Diagnostics

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)

##  Learn

Take a deep-dive into the SDK concept material and learn more about Couchbase.

Data Concepts

* [Data Model](../concept-docs/data-model.md)
* [Service Selection](../concept-docs/data-services.md)

Errors & Diagnostics Concepts

* [Errors and Diagnostics](../concept-docs/errors.md)
* [Tracing](../concept-docs/response-time-observability.md)
* [Failure Considerations](../concept-docs/durability-replication-failure-considerations.md)

##  Resources

Useful resources to help support your development experience with Couchbase and the Ruby SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [Glossary](../ref/glossary.md)
* [Travel Sample Data Model](../ref/travel-app-data-model.md)

Project Docs

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating from SDK2 to SDK3 API](../project-docs/migrating-sdk-code-to-3.n.md)
* [3rd Party Integrations](../project-docs/third-party-integrations.md)