[View original HTML](/app-services/private-endpoints/app-services-private-endpoints.html)

> Private endpoints for App Services enable you to connect a client app directly to Couchbase App Services, assuming that they both use the same cloud service provider (CSP). 

This feature allows your mobile or IoT infrastructure to connect to the network encompassing your Capella infrastructure, so that your data does not have to flow over the internet. This can improve security whilst also lowering ingestion costs.

Currently, private endpoints for App Services are only available using Amazon Web Services (AWS).

|  | To use private endpoints for App Services, the client VPC and App Services VPC must be within the same region, for example us-east-1. |
|  | ------------------------------------------------------------------------------------------------------------------------------------- |

## [](#procedures)Procedures

* [Manage AWS Private Endpoints for App Services](app-services-private-endpoints-aws.md)