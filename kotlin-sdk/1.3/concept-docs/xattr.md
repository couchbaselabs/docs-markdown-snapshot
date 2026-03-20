---
title: Extended Attributes
description: Extended Attributes (XATTR) are metadata that can be provided on a
  per-application basis.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.3/modules/concept-docs/pages/xattr.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.3@kotlin-sdk:concept-docs:xattr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/1.3/concept-docs/xattr.html)

# Extended Attributes

> Extended Attributes (XATTR) are metadata that can be provided on a per-application basis. 

Unresolved include directive in modules/concept-docs/pages/xattr.adoc - include::7.5@sdk:shared:partial$sdk-xattr-overview.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/xattr.adoc - include::7.5@sdk:shared:partial$sdk-xattr-overview.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/xattr.adoc - include::7.5@sdk:shared:partial$sdk-xattr-overview.adoc\[\]

```java
collection.lookupIn(
    "airport_1254",
    Collections.singletonList(
        LookupInSpec.get(LookupInMacro.EXPIRY_TIME).xattr())
);
```