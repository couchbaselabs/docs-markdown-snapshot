---
title: Extended Attributes
description: Extended Attributes (XATTR) are metadata that can be provided on a
  per-application basis.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.4/modules/concept-docs/pages/xattr.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.4@kotlin-sdk:concept-docs:xattr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/1.4/concept-docs/xattr.html)

# Extended Attributes

> Extended Attributes (XATTR) are metadata that can be provided on a per-application basis. 

Couchbase Server permits the addition of _extended attributes_ (XATTRs).

These allow developers to define application-specific metadata that will only be visible to those applications that request it or attempt to modify it. This might be, for example, meta-data specific to a programming framework that should be hidden by default from other frameworks, or possibly from other versions of the same framework. They are not intended for use in general applications, only libraries and frameworks, and data stored there cannot be accessed easily by some Couchbase services, such as Search.

## [](#using-extended-attributes)Using Extended Attributes

The SDK supports extended attributes by means of extensions to the _Sub-Document API_: so that extended attributes can be defined, searched for, edited, removed, and more. In order to specify that a subdocument operation should be performed on an extended rather than a regular attribute, an `xattr` flag should be set to `true`, by the calling application. For detailed information on the Subdocument API, see [Subdocument Operations](subdocument-operations.md), and the accompanying [practical doc](#howtos:subdocument-operations.adoc).

For more information, see [Extended Attributes](#7.1@server:learn:data/extended-attributes-fundamentals.adoc).

> [!NOTE]
> The maximum content size for a document stored in Couchbase Server is 20MB. XATTRs — including Virtual XATTRs — will reduce the space available for the remainder of the document.

## [](#virtual-extended-attributes)Virtual Extended Attributes

_Virtual_ extended attributes consist of metadata on an individual document: this can be retrieved by specifying `$document` as a search-path — see below. See [the Virtual XATTR Section](#7.1@server:learn:data/extended-attributes-fundamentals.adoc#virtual-extended-attributes) for more information on the metadata that they expose.

These attributes are generated on-demand to expose storage-level document metadata, such as expiry to expose document expiration. For expiry using Virtual XATTR, use the following:

```java
collection.lookupIn(
    "airport_1254",
    Collections.singletonList(
        LookupInSpec.get(LookupInMacro.EXPIRY_TIME).xattr())
);
```