[View original HTML](/cloud/data-api-guide/data-api-use.html)

> How to make an API call with the Couchbase Capella Data API. 

## [](#prerequisites)Prerequisites

The procedures on this page assume the following:

* The Data API is enabled for the cluster. You must have the base URL for the Data API.
* You have a cluster access credential that has access to the required buckets, scopes, and collections. You must have saved the cluster access username and cluster access secret when you created the cluster access credential.
* If you’re accessing the Data API from a public network, you have access to the Data API from your client’s IP address. Alternatively, you have enabled a VPC peering connection or a private endpoint to access the Data API.

To enable the Data API for the cluster, see [Get Started with the Data API](data-api-start.md).

## [](#make-an-api-call)Make an API Call

To make an API call with the Data API, you can use a client such as [curl](https://curl.se), or a native HTTP request.

When you make an API call:

1. Use the base URL that you obtained when you enabled the Data API.
2. Pass the cluster access username as the username and the cluster access secret as the password, using HTTP Basic authentication.
3. If a request body is required, pass it in the format required by the operation. For more information, see the [Data API Reference](../data-api-reference/index.md). If the request body is in JSON format, set the `Accept: application/json` header.

Alternatively, you can use a client such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com) to explore the details of the REST API, generate code samples, and so on. The Data API uses an [OpenAPI](https://swagger.io/resources/open-api) v3 specification. To download the Data API specification, go to the [Data API Reference](../data-api-reference/index.md) and click **Download**.

## [](#examples)Examples

### [](#ex-get-caller)Get Caller Identity

The following request retrieves the identity of the user making the current request. This provides a quick way to check that the connection to the Data API is working correctly.

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.

HTTP Request

```sh
curl "$BASEURL/v1/callerIdentity" \
  -u $USER:$PASSWORD
```

The response is a JSON object similar to the following.

HTTP Response

```json
{"user": "<USER>"}
```

The response includes the cluster access username.

### [](#ex-get-doc)Get a Document

The following request gets the document with the specified ID from the specified bucket, scope, and collection.

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.

HTTP Request

```sh
curl "$BASEURL/v1/buckets/travel-sample/scopes/inventory/collections/airline/documents/airline_10" \
  -u $USER:$PASSWORD
```

The response is a JSON object similar to the following.

HTTP Response

```json
{
  "id": 10,
  "type": "airline",
  "name": "40-Mile Air",
  "iata": "Q5",
  "icao": "MLA",
  "callsign": "MILE-AIR",
  "country": "United States"
}
```

### [](#ex-create-doc)Create a Document

The following request creates the specified document in the specified bucket, scope, and collection.

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.

HTTP Request

```sh
curl -X POST "$BASEURL/v1/buckets/travel-sample/scopes/inventory/collections/hotel/documents/hotel-123" \
  -u $USER:$PASSWORD \
  -H "Accept: application/json" \
  -d '{
  "id": 123,
  "name": "Medway Youth Hostel",
  "address": "Capstone Road, ME7 3JE",
  "url": "http://www.yha.org.uk",
  "country": "United Kingdom",
  "city": "Medway",
  "state": null,
  "vacancy": true,
  "description": "40 bed summer hostel about 3 miles from Gillingham."
}'
```

### [](#ex-get-etag)Get the CAS for a Document

The following request gets the CAS (Compare and Swap) value of the specified document within the specified bucket, scope, and collection.

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.

HTTP Request

```sh
curl "$BASEURL/v1/buckets/travel-sample/scopes/inventory/collections/hotel/documents/hotel-123" \
  -u $USER:$PASSWORD \
  -i | grep etag
```

curl also has an `--etag-save` option, which provides a convenient way of saving the CAS value. This example requests the protocol response headers instead, for clarity.

The response is an ETag similar to the following. The ETag is the document’s CAS value.

HTTP Response

```text
etag: 184ed623be9d0000
```

You can use the CAS in a PUT or DELETE request for concurrency control.

### [](#ex-put-etag)Update a Document with Concurrency Control

The following request checks whether the specified document within the specified bucket, scope, and collection has the expected CAS value. If so, it updates the document.

This enables you to make sure that you’re applying your update to the correct revision of the document, in cases where the document may be updated by other processes concurrently.

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.
* `$ETAG` is the expected CAS value, such as `184ed623be9d0000`.

HTTP Request

```sh
curl -X PUT "$BASEURL/v1/buckets/travel-sample/scopes/inventory/collections/hotel/documents/hotel-123" \
  -u $USER:$PASSWORD \
  -H "Accept: application/json" \
  -H "If-Match: $ETAG" \
  -d '{
  "id": 123,
  "name": "Medway Youth Hostel",
  "address": "Capstone Road, ME7 3JE",
  "url": "http://www.yha.org.uk",
  "geo": {
    "lat": 51.35785,
    "lon": 0.55818,
    "accuracy": "RANGE_INTERPOLATED"
  },
  "country": "United Kingdom",
  "city": "Medway",
  "state": null,
  "reviews": [
    {
      "content": "This was our 2nd trip here and we enjoyed it more than last year.",
      "author": "Ozella Sipes",
      "date": "2021-12-13T17:38:02.935Z"
    },
    {
      "content": "This hotel was cozy, conveniently located and clean.",
      "author": "Carmella O’Keefe",
      "date": "2021-12-13T17:38:02.974Z"
    }
  ],
  "vacancy": true,
  "description": "40 bed summer hostel about 3 miles from Gillingham."
}'
```

curl also has an `--etag-compare` option, which provides a convenient way of checking the CAS value. This example specifies the `If-Match` request header instead, for clarity.

If the CAS of the document matches, the document is updated. If the CAS does not match, the request returns an error message similar to the following.

HTTP Response

```json
{
  "code": "CasMismatch",
  "message": "The specified CAS for 'hotel-123' in 'travel-sample/inventory/hotel' did not match.",
  "resource": "/buckets/travel-sample/scopes/inventory/collections/hotel/documents/hotel-123"
}
```

### [](#ex-delete-doc)Delete a Document

The following request deletes the specified document within the specified bucket, scope, and collection.

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.

HTTP Request

```sh
curl -X DELETE "$BASEURL/v1/buckets/travel-sample/scopes/inventory/collections/hotel/documents/hotel-123" \
  -u $USER:$PASSWORD
```

### [](#ex-pass-query)Run a SQL++ Query

The following request uses the Query Service passthrough to run the specified SQL++ query.

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.

HTTP Request

```sh
curl -X POST "$BASEURL/_p/query/query/service" \
   -u $USER:$PASSWORD \
   -H "Accept: application/json" \
   -d '{ "statement": "SELECT name
          FROM `travel-sample`.inventory.hotel
          LIMIT 1;" }'
```

The response is a JSON object similar to the following.

HTTP Response

```json
{
  "requestID": "6d4c5569-609e-4380-b4cc-f51ba5dc8b72",
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
    "elapsedTime": "1.662561ms",
    "executionTime": "1.588577ms",
    "resultCount": 1,
    "resultSize": 30,
    "serviceLoad": 6,
    "usedMemory": 2298
  }
}
```

For more examples showing how to specify query parameters, see [Named Parameters and Positional Parameters](../n1ql/n1ql-manage/query-settings.md#section%5Fsrh%5Ftlm%5Fn1b).

## [](#next-steps)Next Steps

* For a full reference guide, see [Data API Reference](../data-api-reference/index.md).
* For information about SQL++ queries, see [Query Data with SQL++](../n1ql/query.md).
* For information about Vector Search queries, see [Vector Search Using Search Vector Indexes](../vector-search/vector-search.md).
* For information about Search queries, see [Add Search to Your Application](../search/search.md).