---
title: Unsupported HTTP Method
description: For a REST method type that is not supported
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/n1ql/pages/n1ql-rest-api/exunsupportedhttp.adoc
  xref: xref:server:n1ql:n1ql-rest-api/exunsupportedhttp.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-rest-api/exunsupportedhttp.html)

# Unsupported HTTP Method

For a REST method type that is not supported

Request

```sh
curl -v http://localhost:8093/query/service -X PUT \
     -d 'statement=SELECT name FROM `travel-sample`.inventory.hotel LIMIT 1' \
     -u Administrator:password
```

Response

```console
HTTP/1.1 405 Method Not Allowed
```