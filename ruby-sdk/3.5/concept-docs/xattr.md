---
title: XATTR and Virtual XATTR
description: Extended Attributes (XATTR) are metadata that can be provided on a
  per-application basis.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/concept-docs/pages/xattr.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.5@ruby-sdk:concept-docs:xattr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.5/concept-docs/xattr.html)

# XATTR and Virtual XATTR

> Extended Attributes (XATTR) are metadata that can be provided on a per-application basis. 

Unresolved include directive in modules/concept-docs/pages/xattr.adoc - include::7.5@sdk:shared:partial$sdk-xattr-overview.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/xattr.adoc - include::7.5@sdk:shared:partial$sdk-xattr-overview.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/xattr.adoc - include::7.5@sdk:shared:partial$sdk-xattr-overview.adoc\[\]

```ruby
res = @collection.lookup_in(doc_id, [
    LookupInSpec.get(:expiry_time).xattr,
])
res.content(0) #=> 1599488554
Time.now.to_i  #=> 1599488525
```