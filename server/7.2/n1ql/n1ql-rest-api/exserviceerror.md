---
title: Service Error
description: "A service error means there is a problem that prevents the request
  being fulfilled:"
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/n1ql/pages/n1ql-rest-api/exserviceerror.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:n1ql:n1ql-rest-api/exserviceerror.adoc[]
---

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