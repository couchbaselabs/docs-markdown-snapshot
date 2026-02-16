[View original HTML](/server/current/install/couchbase-migrations.html)

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