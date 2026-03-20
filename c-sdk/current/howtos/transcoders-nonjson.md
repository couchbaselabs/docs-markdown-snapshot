---
title: Transcoders &amp; Non-JSON Documents
description: Libcouchbase operates on bare memory, and does not have a transcoders API.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/transcoders-nonjson.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:c-sdk:howtos:transcoders-nonjson.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/c-sdk/current/howtos/transcoders-nonjson.html)

# Transcoders &amp; Non-JSON Documents

> Libcouchbase operates on bare memory, and does not have a transcoders API. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data, and are available in the other SDKs, including those that sit on top of LCB. 

Libcouchbase operates on bare memory, and does not have a transcoders API. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data, and are available in the other SDKs, including those that sit on top of LCB.

See the _Transcoders & Non-JSON Documents_ pages for [Node.js](#3.0@nodejs-sdk:howtos:transcoders-nonjson.adoc).