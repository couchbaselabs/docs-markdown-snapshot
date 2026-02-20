---
title: Request Timeout
description: The request timed out because it could not be completed in the time
  given in the request (or the query engine timeout, if one was specified when
  starting the query engine).
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/n1ql/pages/n1ql-rest-api/extimeout.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:n1ql:n1ql-rest-api/extimeout.adoc[]
---

[View original HTML](/server/7.6/n1ql/n1ql-rest-api/extimeout.html)

# Request Timeout

The request timed out because it could not be completed in the time given in the request (or the query engine timeout, if one was specified when starting the query engine).

Request

```sh
curl -v http://localhost:8093/query/service \
     -d 'statement=SELECT name FROM `travel-sample`.inventory.hotel LIMIT 1
       & timeout=1ms' \
     -u Administrator:password
```

Response

```json
{
  "requestID": "f8f222ee-e402-4031-acf6-1f96612558c7",
  "signature": {
    "name": "json"
  },
  "results": [],
  "errors": [
    {
      "code": 1080,
      "msg": "Timeout 1ms exceeded",
      "retry": true
    }
  ],
  "status": "timeout",
  "metrics": {
    "elapsedTime": "18.472145ms",
    "executionTime": "18.283746ms",
    "resultCount": 0,
    "resultSize": 0,
    "serviceLoad": 12,
    "errorCount": 1
  }
}
```