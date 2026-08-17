---
title: Data API vs. Couchbase SDKs
description: This page explains when to use the Data API and when to use Couchbase SDKs.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/data-api-guide/pages/data-api-sdks.adoc
  xref: xref:cloud:data-api-guide:data-api-sdks.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/data-api-guide/data-api-sdks.html)

# Data API vs. Couchbase SDKs

> The Couchbase Capella Data API and the Couchbase SDKs have overlapping functionality. This page explains when to use the Data API and when to use Couchbase SDKs. 

## [](#when-to-use-the-data-api)When to Use the Data API

Consider using the Data API for the following use cases.

Applications in driverless mode

In some instances, it may not be practical to deploy Couchbase SDKs and related libraries. For example, code running in hosted services such as GDrive or Sharepoint which can access data through HTTP requests. The Data API may also be better suited to data access cases in Function-as-a-Service (FaaS) platforms such as AWS Lambda, Google Cloud Functions, or Azure Functions.

Integrated Platform-as-a-Service ecosystems

It's often not practical to deploy SDKs within broader Integrated Platform-as-a-Service (iPaaS) ecosystems such as Google Application Services. Integrating Capella into those third party platforms is simplified using the Data API. Developers can build connectors using off-the-shelf HTTP client libraries.

AI integrations

This is a more specific case of Integrated Platform-as-a-Service. The Data API offers a lightweight alternative to SDKs for supporting agentic workflows; for example, Google VertexAI function calling and [AWS Bedrock Agents](https://aws.amazon.com/bedrock/agents).

Automation and CI/CD pipelines

The [Management API](../management-api-guide/management-api-intro.md) makes it possible for you to configure, provision, and manage Capella deployments using Infrastructure-as-Code (IaC). The Data API enables you to extend your automation test scripts to access and manipulate data programmatically. For example, after deploying a database and creating buckets, scopes, and collections, the script can load test data, test data access, delete the test data set, or perform other related operations.

Developer prototyping and testing

The Data API enables you to develop and evaluate a new feature easily, without going through the process of integrating it into a complete application. This can also be a quick way to debug data access issues.

Where Couchbase SDKs are not (yet) available

Being language and platform agnostic, the Data API offers a fallback option in environments and platforms where there is no supported Couchbase SDK available.

Web browser applications

The Data API allows quick access to Couchbase Capella from browser applications, without the overhead which may be required by Capella App Services, in cases where scaling and security considerations are not important.

Version compatibility and dependencies

The Data API alleviates the need to deal with SDK version maintenance and compatibility issues, including framework and language version dependencies.

## [](#when-to-use-couchbase-sdks)When to Use Couchbase SDKs

Consider using the Couchbase SDKs for the following use cases.

High load and latency sensitive applications

Requests through the Data API are likely to take longer than corresponding SDK-based operations. For high load use cases and latency sensitive applications, an SDK is recommended.

Highly resilient applications

SDKs provide comprehensive retry logic for handling inevitable errors, details about Couchbase cluster status, and tracing through Open Telemetry.

Idiomatic interfaces

The SDKs support the idiomatic interface for a programming language. Use the SDKs when you want app developers building backend apps in a specific language to use patterns suitable for that language. For example, handling results as they stream in with an asynchronous or reactive interface is supported in Java, Node.js, .NET, and other SDKs.

For more information, see [SDKs & Connectors](../../home/sdk.md).

## [](#when-to-use-capella-app-services)When to Use Capella App Services

Consider using Capella App Services for the following use cases.

Web browser applications with scaling and security

Use Capella App Services for access to Couchbase Capella from browser applications where scaling and security considerations are important.

For more information, see [Manage App Services for Mobile and Edge](../../app-services/index.md).

## [](#see-also)See Also

* For an introduction to the Data API, see [Manage Data with the Data API](data-api-intro.md).
* To enable the Data API, see [Get Started with the Data API](data-api-start.md).
* To set up a private endpoint for the Data API, see [Add Private Endpoints for the Data API](data-api-private.md).
* To make an API call, see [Make an API Call with the Data API](data-api-use.md).
* For a full reference guide, see [Data API Reference](../data-api-reference/index.md).