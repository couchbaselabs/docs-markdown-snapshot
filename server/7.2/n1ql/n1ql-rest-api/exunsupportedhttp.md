---
title: Unsupported HTTP Method
description: For a REST method type that is not supported
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/n1ql/pages/n1ql-rest-api/exunsupportedhttp.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:n1ql:n1ql-rest-api/exunsupportedhttp.adoc[]
---

[View original HTML](/server/7.2/n1ql/n1ql-rest-api/exunsupportedhttp.html)

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