[View original HTML](/cloud/data-api-guide/data-api-intro.html)

> The Couchbase Capella Data API is a secure REST API that enables you to create, read, update, and delete data. It also provides passthrough access to the Query Service and the Search Service, so that you can run SQL++ queries and full-text searches. 

Clients do not need any special tools, SDKs, or libraries to access the Data API. The Data API supports off-the-shelf HTTP clients, such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com).

To get started quickly, [enable the Data API and make an API call](#see-also).

## [](#versioning)Versioning

The Data API uses [semantic versioning](https://semver.org). The full version number consists of 3 parts: `major.minor.patch`.

An update to the Data API may be a non-versioned bug fix, a patch update, a minor update, or a major update. When a non-versioned bug fix is released, the version number is not updated. When a patch update, a minor update, or a major update is released, the version number is updated also.

With few exceptions, new versions of Data API are backward compatible, minimizing the effect on existing deployments. In most cases, you do not have to update your existing infrastructure when a new version of the Data API is released. Features added in a new version of the Data API will not break existing deployments.

Exceptions to backward compatibility are as follows:

* Critical security fixes. A vulnerable version is marked as unsupported when a fixed version is released. In this case, you must plan to upgrade as soon as possible.
* Fundamental architectural changes, when unavoidable.

|  | Beta Features From time to time, beta features may be added to the Data API. Beta features are early previews that are added to the Data API for evaluation only. They’re subject to change, and should not be used in production. Beta features are clearly labelled in the Data API reference. They will be promoted to regular features in a future version. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#private-networking)Private Networking

If your client app and your Capella cluster use the same cloud service provider (CSP), you can connect your client app to the Data API privately through the cloud, using either a VPC Peering connection or a private endpoint.

VPC Peering (virtual private cloud) provides a connection between your client app and the whole Capella cluster. A private endpoint provides a connection between your client app and the Data API in particular.

Both of these solutions add security by avoiding communication over the Internet, and may lead to a reduction in latency and egress costs.

## [](#authentication-and-authorization)Authentication and Authorization

The Data API uses cluster access credentials for authentication and authorization.

The access privileges specified for the cluster access credential determine the buckets, scopes, and collections that a client can access via the Data API.

You must permit access to the cluster from the IP address of the Data API client. (If you’re accessing the Data API via a VPC Peering connection or a private endpoint, you do not need to permit access from the peered range of private IP addresses.)

To authenticate a Data API call, you must pass the cluster access credentials as the username and password, using HTTP Basic authentication.

## [](#concurrent-access)Concurrent Access

To support concurrent requests, PUT and DELETE requests support optimistic concurrency control, using `If-Match` headers in combination with HTTP ETags (entity tags). Exceptions are noted in the endpoint descriptions. A typical pattern is to do a GET request on a specified resource, which returns an ETag value. You can then include the ETag value in a PUT request to update the resource.

The ETag value for a document is equivalent to the document’s CAS (Compare and Swap) value.

## [](#passthrough-proxy-requests)Passthrough Proxy Requests

The Data API provides passthrough access to the Query Service and the Search Service.

The passthrough Query Service endpoints enable you to run SQL++ queries and set request-level parameters. Managing and administrating the Query Service is not supported.

The passthrough Search Service endpoints enable you to run Full-Text Search queries and Vector Search queries using a Search index. Other search requests are not supported.

You can access the passthrough Query Service and Search Service endpoints via the Data API, in the same way as the other Data API endpoints.

|  | Versioning of Passthrough Endpoints The version of the passthrough endpoints depends on the version of Couchbase Server installed on the cluster. Clusters running different versions of Couchbase Server may expose slightly different functionality via the passthrough endpoints. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#billing)Billing

You’ll incur charges when you enable the Data API for a cluster. You’ll incur an extra charge when both Data API and VPC Peering connections are enabled. Enabling private endpoint support with the Data API has no additional cost. For details of the charges associated with the Data API, see [Manage Your Billing](../billing/billing.md).

## [](#service-limits)Service Limits

Long-Running Requests

Key-value requests taking longer than 120 seconds to process are rejected with error 504, Gateway Timeout. This limit does not apply to passthrough REST API requests.

Rate Limiting

Requests are limited to 10,000 requests per second per node. If the rate limit is exceeded, the request returns error 429, too many requests.

Payload Size

Requests and response payloads are restricted to 100 MB. If a response is a list of items, then the maximum number of items returned in a response must not exceed the maximum permitted size. This also restricts the number of items that can be included in bulk requests.

## [](#see-also)See Also

* To enable the Data API, see [Get Started with the Data API](data-api-start.md).
* To set up a private endpoint for the Data API, see [Add Private Endpoints for the Data API](data-api-private.md).
* To make an API call, see [Make an API Call with the Data API](data-api-use.md).
* To understand when to use the Data API, see [Data API vs. Couchbase SDKs](data-api-sdks.md).
* For a full reference guide, see [Data API Reference](../data-api-reference/index.md).