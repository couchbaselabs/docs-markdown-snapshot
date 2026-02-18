---
title: Extended Attributes
description: Extended Attributes (XATTR) are metadata that can be provided on a
  per-application basis.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.3/modules/concept-docs/pages/xattr.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

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