---
title: Spring Data Couchbase
description: Spring-based programming model for Couchbase Server with any of our
  JVM-based SDKs (Java, Kotlin, and Scala).
editUrl: https://github.com/couchbase/docs-sdk-extensions/edit/main/modules/ROOT/pages/spring-data-couchbase.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:sdk-extensions::spring-data-couchbase.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sdk-extensions/spring-data-couchbase.html)

# Spring Data Couchbase

> Spring-based programming model for Couchbase Server with any of our JVM-based SDKs (Java, Kotlin, and Scala). 

The primary goal of the Spring Data project is to make it easier to build Spring-powered applications that use new data access technologies such as non-relational databases, map-reduce frameworks, and Cloud-based data services.

The Spring Data Couchbase project aims to provide a familiar and consistent Spring-based programming model for Couchbase Server as a document database and cache while retaining store-specific features and capabilities. Key functional areas of Spring Data Couchbase (SDC) are a POJO centric model for interacting with a Couchbase Server Bucket or Collection, and easily writing a repository style data access layer.

From SDC 4.0, and Couchbase Server 7.0, easier migration from RDBMS is provided by Scopes and Collections. Buckets, Scopes, and Collections in Couchbase are analogous to Catalogs, Schemas, and Tables in SQL Databases.

* Scope name can be configured by overriding `config.getScopeName()`. The base method results in the use of the `_default` Scope.
* Other Scopes can potentially be used with templates and repositories.
* If Scopes require different authorization, `RepositoryOperationsMapping` is required.
* In SDC, we continue to leverage the “ `_class` property, so that data migration to/from Scopes/Collections is not required.

More information can be found in the [reference documentation](https://docs.spring.io/spring-data/couchbase/docs/current/reference/html/#reference) and [API guide](https://docs.spring.io/spring-data/couchbase/docs/current/api/) — as well as by exploring the Java-based [sample application](../java-sdk/current/hello-world/spring-data-sample-application.md).

Although hosted at [spring.io](https://spring.io/projects/spring-data-couchbase#overview), as is the norm for Spring projects, SDC is supported by Couchbase. Couchbase Server compatibility information can be found [here](../java-sdk/current/project-docs/compatibility.md#spring-compat).