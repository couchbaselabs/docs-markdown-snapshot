---
title: Migrating your Data to Couchbase
description: Couchbase offers a number of options for migrating your data from
  other platforms to Couchbase Server/Capella.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/couchbase-migrations.adoc
  xref: xref:7.6@server:install:couchbase-migrations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/install/couchbase-migrations.html)

# Migrating your Data to Couchbase

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Couchbase offers a number of options for migrating your data from other platforms to Couchbase Server/Capella. 

Data migration can take one of two forms:

## [](#data-migration-from-earlier-versions-of-couchbase)Data Migration from earlier versions of Couchbase

With the release of Couchbase Version 7.0, we added support for scopes and collections, which adds more flexible abstraction for your data.

For more information, see [Scopes and Collections](../learn/data/scopes-and-collections.md)

For more information on migrating from earlier versions of Couchbase, see [Migrating Application Data to a Collections-Based Model](migrating-application-data.md)

## [](#migrating-your-data-from-other-platforms)Migrating your data from other platforms

You have the option of migrating your data from other platforms to Couchbase Server or Couchbase Capella

We have a command line tool (`cbmigrate`) for this purpose, which currently supports migration from:

* [Mongo DB](https://www.mongodb.com)
* [Dynamo DB](https://aws.amazon.com/dynamodb/)
* [Hugging Face](https://huggingface.co)

For more information, see [cbmigrate](../cli/cbmigrate-tool.md)