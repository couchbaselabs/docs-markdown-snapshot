---
title: Create a Synonym Collection and Documents
description: Create a synonym collection and documents to define synonym
  mappings for search terms in a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/synonyms/create-synonym-collection-docs.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/search/synonyms/create-synonym-collection-docs.html)

# Create a Synonym Collection and Documents

> Create a synonym collection and documents to define synonym mappings for search terms in a Search index. 

## [](#prerequisites)Prerequisites

* Your user account has the [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role) role for the project that contains your cluster.
* You have created a bucket and scope where you want to store your Search index and its synonym collections. For more information, see [Manage Buckets](../../clusters/data-service/manage-buckets.md) and [Manage Scopes and Collections](../../clusters/data-service/scopes-collections.md).

## [](#procedure)Procedure

To define the synonym mappings for a Search index, you must:

1. [Create a Synonym Collection](#create-collection)
2. [Create Synonym Documents](#create-documents)

### [](#create-collection)Create a Synonym Collection

You can create a synonym collection like any other collection in Capella. Create synonym collections to divide your synonyms based on language or other sorting criteria.

> [!NOTE]
> You must create your synonym collections in the same bucket and scope where you want to create your Search index.

For more information about how to create a new collection, see [Create a Collection](../../clusters/data-service/scopes-collections.md#create-collection).

### [](#create-documents)Create Synonym Documents

You can create the following types of synonym documents for use with the Search Service:

* [Unidirectional synonym documents](#uni)
* [Bidirectional synonym documents](#bi)

#### [](#uni)Create a Unidirectional Synonym Document

Unidirectional synonym documents define a one-way synonym relationship.

A unidirectional synonym document contains an `input` array and a `synonyms` array. Any search for a term in `input` can return any term in `synonyms`.

For example, a unidirectional synonym document for synonyms of the terms `happy`, `joyful`, and `cheerful` can be defined as:

```json
{
    "input": [
      "happy",
      "joyful",
      "cheerful"
    ],
    "synonyms": [
      "content",
      "delighted",
      "elated",
      "glad",
      "pleased"
    ]
}
```

A search for `happy` could return results for `content`, `delighted`, `elated`, `glad`, or `pleased`. A search for `cheerful` would not return results for `happy`.

> [!NOTE]
> You can only include a single `input` and `synonyms` array per unidirectional synonym document.

To insert a new document into your cluster with a command line tool or SDK, see [Create Documents](../../guides/creating-data.md).

To import multiple documents into your cluster at one time with the Couchbase Capella UI, command line tools, or an SDK, see [Import and Export Data](../../guides/load.md).

#### [](#bi)Create a Bidirectional Synonym Document

Bidirectional synonym documents define a two-way synonym relationship. All terms are contained in a single `synonyms` array. Any search for a term in the `synonyms` array can return any other term in the array.

For example, a bidirectional synonym document for synonyms of the word `happy` could be defined as:

```json
{
  "synonyms": [
    "cheerful",
    "content",
    "delighted",
    "elated",
    "glad",
    "happy",
    "joyful",
    "pleased"
  ]
}
```

A search for `cheerful`, `happy`, or 1 of the other terms in the array could return results for any other term.

> [!NOTE]
> You can only include a single `synonyms` array per bidirectional synonym document.

To insert a new document into your cluster with a command line tool or SDK, see [Create Documents](../../guides/creating-data.md).

To import multiple documents into your cluster at one time with the Couchbase Capella UI, command line tools, or an SDK, see [Import and Export Data](../../guides/load.md).

## [](#next-steps)Next Steps

To use your defined synonyms in a Search index, see [Add a Synonym Source](add-synonym-source.md).