---
title: Request with Authentication&#8201;&#8212;&#8201;Request Parameter
description: If a request requires more than one set of credentials, the creds
  parameter must be used, as in this example.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/n1ql/pages/n1ql-rest-api/exauthrequest.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/n1ql/n1ql-rest-api/exauthrequest.html)

# Request with Authentication&#8201;&#8212;&#8201;Request Parameter

If a request requires more than one set of credentials, the creds parameter must be used, as in this example.

Request

```sh
curl -v http://localhost:8093/query/service \
     -d 'statement=SELECT hotel.name, airport.airportname
                   FROM `travel-sample`.inventory.hotel
                   JOIN `travel-sample`.inventory.airport
                   ON hotel.city = airport.city LIMIT 1
        & creds=[{"user": "local:simon", "pass": "fizzbuzz"},
                 {"user": "admin:Administrator", "pass": "password"}]'
```

Response

```json
{
  "requestID": "3c6407ff-0501-475f-b922-0540c329d708",
  "signature": {
    "airportname": "json",
    "name": "json"
  },
  "results": [
    {
      "airportname": "Annapolis",
      "name": "Sea Ranch Lodge"
    }
  ],
  "status": "success",
  "metrics": {
    "elapsedTime": "73.761259ms",
    "executionTime": "73.362629ms",
    "resultCount": 1,
    "resultSize": 52,
    "serviceLoad": 12
  }
}
```