---
title: Successful Request
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/n1ql/pages/n1ql-rest-api/exsuccessful.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:n1ql:n1ql-rest-api/exsuccessful.adoc[]
---

[View original HTML](/server/current/n1ql/n1ql-rest-api/exsuccessful.html)

# Successful Request

Request

```sh
curl -v http://localhost:8093/query/service \
     -d 'statement=SELECT name FROM `travel-sample`.inventory.hotel LIMIT 1' \
     -u Administrator:password
```

Response

```json
{
  "requestID": "615e0b26-dd61-4a1a-bda9-22333193b982",
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
    "elapsedTime": "5.232754ms",
    "executionTime": "5.160022ms",
    "resultCount": 1,
    "resultSize": 30,
    "serviceLoad": 12
  }
}
```

The same request can be run as a GET request:

Request

```sh
curl -v http://localhost:8093/query/service?statement=SELECT%20name%20FROM%20%60travel-sample%60.inventory.hotel%20LIMIT%201%3B \
     -u Administrator:password
```