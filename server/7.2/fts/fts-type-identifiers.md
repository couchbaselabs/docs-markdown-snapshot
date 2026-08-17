---
title: Specifying Type Identifiers
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-type-identifiers.adoc
  xref: xref:7.2@server:fts:fts-type-identifiers.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-type-identifiers.html)

# Specifying Type Identifiers

A _type identifier_ allows the documents in a bucket to be identified filtered for inclusion into the index according to their _type_. When the **Add Index, Edit Index**, or **Clone Index** screen is accessed, a **Type Identifier** panel is displayed:

![fts type identifier ui](_images/fts-type-identifier-ui.png) 

There are three options, each of which gives the index a particular way of determining the type of each document in the bucket. This document filtering via the **Type Identifier** is only active is you append a `.` and then a `substring` to the end of the `scope.collection` in the Type Mapping.

## [](#json-type-field)JSON type field

It is the name of a document field. The value specified for this field is used by the index to determine the type of document.

> [!NOTE]
> FTS Indexing does not work for fields having a dot (. or period) in the field name. Users must avoid adding a dot (. or period) in the field name.  
> **Unsupported field names**: `field.name` or `country.name`. For example, `{ "database.name": "couchbase"}`  
> **Supported field names**: `fieldname` or `countryname`. For example, `{ "databasename": "couchbase"}`

The default value is type: meaning that the index searches for a field in each document whose name is type.

Each document that contains a field with that name is duly included in the index, with the value of the field specifying the type of the document.

> [!NOTE]
> The value of the field should be of text type and cannot be an array or JSON object.

## [](#doc-id-up-to-separator)Doc ID up to separator

The characters in the ID of each document, up to but not including the separator. For example, if the document's ID is `hotel_10123`, the value `hotel` is determined by the index to be the type of document. The value entered into the field should be the separator-character used in the ID: for example, `_`, if that character is the underscore

## [](#doc-id-with-regex)Doc ID with regex

A **[RE2](https://github.com/google/re2/wiki/Syntax)** regular expression that is applied by the index to the ID of each document. The resulting value is determined to be the type of the document. (This option may be used when the targeted document-subset contains neither a suitable **JSON type field** nor an ID that follows a naming convention suitable for **Doc ID up to separator**.) The value entered into the field should be the regular expression to be used.