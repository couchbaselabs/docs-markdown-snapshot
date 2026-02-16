[View original HTML](/server/7.6/n1ql/n1ql-rest-api/exauthhttp.html)

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