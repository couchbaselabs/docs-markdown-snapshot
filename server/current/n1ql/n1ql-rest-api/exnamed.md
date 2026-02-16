[View original HTML](/server/current/n1ql/n1ql-rest-api/exnamed.html)

Example 1\. A statement containing named parameters

This request contains the parameters described in the following table.

| Parameter Name | Value                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------- |
| statement      | SELECT airline FROM \`travel-sample\`.inventory.route WHERE sourceairport = $aval AND distance > $dval; |
| $aval          | "LAX"                                                                                                   |
| $davl          | 13000                                                                                                   |

Request

```sh
curl -v http://localhost:8093/query/service \
     -d 'statement=SELECT airline FROM `travel-sample`.inventory.route
                   WHERE sourceairport = $aval AND distance > $dval
       & $aval="LAX" & $dval=13000' \
     -u Administrator:password
```

Response

```json
{
  "requestID": "81aceab8-7f7a-4d00-b741-00385740329a",
  "signature": {
    "airline": "json"
  },
  "results": [
    {
      "airline": "B6"
    },
    {
      "airline": "EK"
    },
    {
      "airline": "SV"
    }
  ],
  "status": "success",
  "metrics": {
    "elapsedTime": "72.886709ms",
    "executionTime": "72.765333ms",
    "resultCount": 3,
    "resultSize": 48,
    "serviceLoad": 12
  }
}
```

Example 2\. A statement containing a wildcard parameter

The **%** symbol is the escape character in URIs, so when using **%** as a wildcard in a query, we need to escape that by replacing it with its corresponding ASCII code **%25**.

Request

```sh
curl -v http://localhost:8093/query/service \
     -u Administrator:password \
     -d 'statement=SELECT meta().id
                   FROM `travel-sample`.inventory.hotel
                   WHERE meta().id LIKE $pattern
       & $pattern="hotel_1002%25"'
```

Response

```json
{
  "requestID": "716f5e7b-557a-44a6-a372-9a98611c5b5e",
  "signature": {
    "id": "json"
  },
  "results": [
    {
      "id": "hotel_10025"
    },
    {
      "id": "hotel_10026"
    }
  ],
  "status": "success",
  "metrics": {
    "elapsedTime": "64.11756ms",
    "executionTime": "63.993854ms",
    "resultCount": 2,
    "resultSize": 40,
    "serviceLoad": 12
  }
}
```