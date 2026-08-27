---
title: Service Error
description: "A service error means there is a problem that prevents the request
  being fulfilled:"
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/n1ql/pages/n1ql-rest-api/exserviceerror.adoc
  xref: xref:7.2@server:n1ql:n1ql-rest-api/exserviceerror.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-rest-api/exserviceerror.html)

# Service Error

A service error means there is a problem that prevents the request being fulfilled:

Request

```sh
curl -v http://localhost:8093/query/service \
     -d "statement=SELECT text FROM tweets LIMIT 1"
```

Response

```console
     $lt; HTTP/1.1 503 Service Unavailable
     {
     "requestID": "5c0a6a81-2fc8-4a33-a035-ed7fb1512710",
     "errors": [
     {
     "code": <int>,
     "msg": "Request queue full"
     }],
     "status": "errors",
     "metrics": {
     "elapsedTime": "134.7944us",
     "executionTime": "130.5518us",
     "resultCount": 0,
     "resultSize": 0,
     "mutationCount": 0,
     "errorCount": 1,
     "warningCount": 0
     }
     }
     $
```