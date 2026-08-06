---
title: Configure Named Query Access Control
description: Restrict which named queries edge client users can execute in
  Couchbase Edge Server based on their collection-level access permissions.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/access-control/pages/configure-query-access.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-edge-server:access-control:configure-query-access.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/access-control/configure-query-access.html)

# Configure Named Query Access Control

Configure named query access control to restrict which queries each edge client user can execute, based on their collection-level permissions.

## [](#prerequisites)Prerequisites

* Couchbase Edge Server {version} or later.
* `enable_user_access_control` set to `true` at the server level. See [configuration:configure-access-control.adoc](#configuration:configure-access-control.adoc).
* Named queries defined in the database configuration.

> [!NOTE]
> Ad hoc query execution is disabled by default. Couchbase recommends keeping ad hoc queries disabled in production deployments. Access control policies apply to named queries only.

## [](#how-named-query-access-works)How Named Query Access Works

When `enable_user_access_control` is enabled, Couchbase Edge Server evaluates a user's collection-level permissions to determine which named queries that user can execute.

There are two ways to configure a named query:

* **Database-level query** — A query defined without an `allow` property. Any authenticated user with read access to at least one collection in the database can execute this query.
* **Collection-restricted query** — A query with an `allow.collections` property. Only users with read access to at least one of the listed collections can execute this query.

## [](#configure-a-database-level-named-query)Configure a Database-Level Named Query

Define the query in the `queries` object without an `allow` property.

```json
{
  "enable_user_access_control": true,
  "databases": {
    "mydb": {
      "queries": {
        "all_airlines": {
          "statement": "SELECT * FROM travel.inventory.airlines"
        }
      }
    }
  }
}
```

Any user with read access to the `mydb` database can execute the `all_airlines` query.

## [](#configure-a-collection-restricted-named-query)Configure a Collection-Restricted Named Query

Add an `allow.collections` property to the query definition. List the collections a user must have read access to in order to execute the query. A user needs read access to at least one of the listed collections.

```json
{
  "enable_user_access_control": true,
  "databases": {
    "mydb": {
      "queries": {
        "all_airlines": {
          "statement": "SELECT * FROM travel.inventory.airlines"
        },
        "best_hotels": {
          "statement": "SELECT id, name, rating FROM travel.inventory.hotels",
          "allow": {
            "collections": ["inventory.hotels", "inventory.landmarks"]
          }
        }
      }
    }
  }
}
```

In this example:

* Any user with read access to `mydb` can execute `all_airlines`.
* Only users with read access to `inventory.hotels` or `inventory.landmarks` can execute `best_hotels`.

The following users file illustrates which queries each user can run:

```json
{
  "foo": {
    "access": {
      "mydb.inventory.landmarks": ["read"]
    }
  },
  "bar": {
    "access": {
      "mydb.inventory.airlines": ["read", "write"]
    }
  }
}
```

* `foo` has read access to `inventory.landmarks` and can execute `best_hotels`.
* `bar` has read access to `inventory.airlines` and can execute `all_airlines`. `bar` cannot execute `best_hotels` because `bar` does not have access to `inventory.hotels` or `inventory.landmarks`.

## [](#next-steps)Next Steps

* To review how Couchbase Edge Server enforces access control across REST operations, see [configuration:fine-grained-access-control.adoc](#configuration:fine-grained-access-control.adoc).
* To configure user access permissions, see [configuration:configure-access-control.adoc](#configuration:configure-access-control.adoc).