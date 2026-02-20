---
title: Request with Authentication&#8201;&#8212;&#8201;HTTP Header
description: In this example, the credentials (user="simon", pass="fizzbuzz")
  are given in the request header using basic authentication.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/n1ql/pages/n1ql-rest-api/exauthhttp.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:n1ql:n1ql-rest-api/exauthhttp.adoc[]
---

[View original HTML](/server/current/n1ql/n1ql-rest-api/exauthhttp.html)

# Request with Authentication&#8201;&#8212;&#8201;HTTP Header

In this example, the credentials (user="simon", pass="fizzbuzz") are given in the request header using basic authentication.

Request

```sh
curl -v http://localhost:8093/query/service \
     -d 'statement=SELECT name FROM `travel-sample`.inventory.hotel LIMIT 1' \
     -u simon:fizzbuzz
```

Response

```json
{
  "requestID": "d8b27115-a2a3-419d-a802-de0746c6497c",
  "signature": {
    "name": "json"
  },
  "results": [
    {
      "name": "Medway Youth Hostel"
    }
  ],
  "status": "success",
  "metrics": {
    "elapsedTime": "6.737428ms",
    "executionTime": "6.55678ms",
    "resultCount": 1,
    "resultSize": 30,
    "serviceLoad": 12
  }
}
```