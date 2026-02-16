[View original HTML](/server/7.6/n1ql/n1ql-rest-api/expositional.html)

Example 1\. A statement containing numbered positional parameters

This request contains the parameters described in the following table.

| Parameter Name | Value                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------- |
| statement      | SELECT airline FROM \`travel-sample\`.inventory.route WHERE sourceairport = $1 AND distance > $2; |
| $1             | "LAX"                                                                                             |
| $2             | 13000                                                                                             |

Request

```sh
curl -v http://localhost:8093/query/service \
     -d 'statement=SELECT airline FROM `travel-sample`.inventory.route
                   WHERE sourceairport = $1 AND distance > $2
       & args=["LAX", 13000]' \
     -u Administrator:password
```

Response

```json
{
  "requestID": "6e242629-ebf5-4a58-8db4-62d94974519f",
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
    "elapsedTime": "86.962678ms",
    "executionTime": "84.35715ms",
    "resultCount": 3,
    "resultSize": 48,
    "serviceLoad": 12
  }
}
```

Example 2\. A statement containing unnumbered positional parameters

Positional parameters can also be specified in a statement using the question mark (?), so the following statement is an alternative way to specify the same query.

Request

```sh
curl -v http://localhost:8093/query/service \
     -d 'statement=SELECT airline FROM `travel-sample`.inventory.route
                   WHERE sourceairport = ? AND distance > ?
       & args=["LAX", 13000]' \
     -u Administrator:password
```

Response

```json
{
  "requestID": "6d77dc41-3cab-4e00-9c54-f60fcc2e0fab",
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
    "elapsedTime": "86.226474ms",
    "executionTime": "86.072996ms",
    "resultCount": 3,
    "resultSize": 48,
    "serviceLoad": 12
  }
}
```