---
title: SQL++ Error
description: A SQL++ error happens when there is an error processing the SQL++
  statement in a request.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/n1ql/pages/n1ql-rest-api/exn1qlerror.adoc
  xref: xref:7.6@server:n1ql:n1ql-rest-api/exn1qlerror.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-rest-api/exn1qlerror.html)

# SQL++ Error

A SQL++ error happens when there is an error processing the SQL++ statement in a request.

Request

```sh
curl -v http://localhost:8093/query/service \
     -d 'statement=SLECT name FROM `travel-sample`.inventory.hotel LIMIT 1' \
     -u Administrator:password
```

Response

```json
{
  "requestID": "27087759-07af-431d-a3d7-29080f870e56",
  "errors": [
    {
      "code": 3000,
      "msg": "syntax error - line 1, column 7, near 'SLECT', at: name"
    }
  ],
  "status": "fatal",
  "metrics": {
    "elapsedTime": "1.478631ms",
    "executionTime": "1.393274ms",
    "resultCount": 0,
    "resultSize": 0,
    "serviceLoad": 12,
    "errorCount": 1
  }
}
```

Request

```sh
curl -v http://localhost:8093/query/service \
     -d 'statement=SELECT name FROM `travel-sample`.inventory.motel LIMIT 1' \
     -u Administrator:password
```

Response

```json
{
  "requestID": "d30b805f-6c1e-44ec-9aec-35ff711a6e88",
  "errors": [
    {
      "code": 12003,
      "msg": "Keyspace not found in CB datastore: default:travel-sample.inventory.motel"
    }
  ],
  "status": "fatal",
  "metrics": {
    "elapsedTime": "3.096786ms",
    "executionTime": "2.468282ms",
    "resultCount": 0,
    "resultSize": 0,
    "serviceLoad": 12,
    "errorCount": 1
  }
}
```