---
title: Run a Function on Data Change
description: The Eventing Service lets you handle data changes in real time.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/eventing/pages/eventing-overview.adoc
  xref: xref:7.6@server:eventing:eventing-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/eventing/eventing-overview.html)

# Run a Function on Data Change

> The Eventing Service lets you handle data changes in real time. 

## [](#eventing-service)Eventing Service

The Eventing Service handles data changes that happen when applications interact. These changes in data are known as document mutations, and include operations such as insert, delete, update, and expiration.

You can use the Eventing Service to:

* Monitor specific parameters in a document
* Set alerts in a document for when a preconfigured threshold is breached
* Propagate data changes inside a database
* Enrich documents in real time
* Cascade delete to avoid orphaned documents

You can also use the Eventing Service to scale your business logic and streamline your business workflows. The Eventing Service lets you:

* Integrate with other Couchbase services such as Data, Query, GSI, FTS, and Analytics
* Handle inconsistencies in business logic across multiple applications
* Increase customer engagement by managing business logic across different applications in a timely manner
* Scale your throughput without making changes to your data configuration and infrastructure
* Create specialized tools to clean, enhance, and transform your data
* Maximize your return on investment (ROI) by minimizing your total cost of ownership (TCO)
* Test, debug, and troubleshoot on a single platform instead of on multiple applications

## [](#eventing-functions)Eventing Functions

The Eventing Service can run one or more Eventing Functions in your database to handle data changes according to a real-time Event-Condition-Action model. Eventing Functions are standalone JavaScript fragments that trigger in real time as a response to document mutations. When you create, update, or delete documents, or when these documents expire, your Functions handle and process these events.

You can use Eventing Functions to:

* Integrate with the Data Service to read, write, and delete documents
* Integrate with the Query Service to use inline SQL++ queries and statements
* Enable Timers to schedule functions to run in the future
* Interact with external REST endpoints through cURL functionality

## [](#eventing-service-vs-other-implementations)Eventing Service vs Other Implementations

Unlike Message Queue or Polling-based external systems, the Eventing Service is native to Couchbase Server. This means you do not need to use multiple applications to track data mutations.

The following table compares the implementation of the Eventing Service with the Message Queue method.

| Eventing Service                                                                                              | Message Queue                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Native to Couchbase Server. Does not need a new layer to propagate data changes.                              | Needs an additional layer to propagate data changes.                                                                             |
| Eliminates the dual-write problem. Multiple application servers can perform simultaneous write operations.    | Has a dual-write problem. Every write operation gets pushed twice, once to the message queue and the second time to the cluster. |
| Eliminates the write-failure condition.                                                                       | A write-failure condition can happen at any point.                                                                               |
| Integrates with native debugger support.                                                                      | No easy debug option during troubleshooting.                                                                                     |
| Provides a centralized control for aspects such as data auditing and data governance, reducing data leakages. | Leads to inefficient data governance and data leakages.                                                                          |
| No additional expenses, so TCO is reduced.                                                                    | Has added license, infrastructure, and deployment expenses, which increases TCO.                                                 |

The following table compares the implementation of the Eventing Service with the Polling method.

| Eventing Service                                                                                                                  | Polling                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Can record and propagate data changes to a database, message queue, end-point, or to another bucket inside the Couchbase cluster. | Needs multiple applications to record and propagate data changes.                          |
| Handles data mutations in real-time.                                                                                              | Batch systems are highly inefficient and are not reactive.                                 |
| Implements as a state-less compute operation and utilizes latest trends in compute (multi-core CPU).                              | Consumes a lot of CPU resources.                                                           |
| No code duplication.                                                                                                              | Leads to code duplication across multiple infrastructure applications.                     |
| Provides easy horizontal and vertical scaling options with built-in support.                                                      | Difficult to scale as you need to scale for applications and transport layer requirements. |

## [](#eventing-service-use-cases)Eventing Service Use Cases

You can use the Eventing Service to track data changes in many different domains. For example, you can design a custom workflow to track a user's credit limit, usage currency, and risk propositions when that user makes a credit card transaction. You can also create a workflow that automatically maintains a set stock threshold and triggers new stock replacements when that stock runs out.

The following table provides use cases for the Eventing Service.

| Domain                         | Eventing trigger  | Condition check                                    | Sample workflow                                                                     |
| ------------------------------ | ----------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Banking and financial services | Card transaction  | Transaction threshold                              | Generates risk alerts and quarantines user when they hit the transaction threshold. |
| Inventory and warehousing      | New sales voucher | Stock availability                                 | Generates invoice to replenish stock.                                               |
| New purchase order             | Saved wishlist    | Alerts user about price drops for wishlist items.  |                                                                                     |
| Airline                        | New booking       | Booking history                                    | Enrolls user in frequent flyer programs and notifies them about special promotions. |
| Enquiry                        | User profile      | Alerts user about price drops for airline tickets. |                                                                                     |
| Healthcare                     | New report        | Check for vitals                                   | Schedules an appointment for the user.                                              |
| Sports and gaming              | New user creation | User profile                                       | Generates notifications about leaderboard and other statistics.                     |
| Media and entertainment        | Breaking news     | Query archives                                     | Enriches existing news with archival information.                                   |