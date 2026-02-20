---
title: Couchbase Server Editions
description: "Couchbase Server is available in two editions: Enterprise and Community."
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/introduction/pages/editions.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:introduction:editions.adoc[]
---

[View original HTML](/server/current/introduction/editions.html)

# Couchbase Server Editions

> Couchbase Server is available in two editions: Enterprise and Community. 

Each edition offers different features and levels of support.

## [](#enterprise-edition)Enterprise Edition

The Enterprise Edition (EE) represents the latest, most stable, production-ready release of Couchbase Server. We recommend the Enterprise Edition binaries for commercial production systems running Couchbase Server. The Enterprise Edition contains some unique features that make it the best fit for production deployments running in data centers or public cloud infrastructure.

A subscription to the Enterprise Edition includes a commercial license, better availability capabilities, enhanced security features, advanced tooling, and higher performance and scale. It also includes technical support with service level commitments via our 24/7 support organization and hot fixes for releases.

Refer to the [pricing](https://www.couchbase.com/pricing) page for details on Couchbase’s Enterprise Edition.

## [](#community-edition)Community Edition

The Community Edition (CE) is best for noncommercial developers where basic availability, performance, scale, tooling, security capabilities and community support is sufficient.

One important principle for Community Edition and Enterprise Edition is to ensure full portability of applications between the two editions. The capabilities ensure that an application running on Enterprise Edition should transition to Community Edition without code changes and vice versa.

The Community Edition license provides the free deployment of Couchbase Community Edition for departmental-scale deployments of up to five node clusters. The Community Edition license has recently been updated to disallow the use of Cross Data Center Replication (XDCR), which is now an exclusive Enterprise Edition feature. The Community Edition is not subjected to the iterative "test, fix, and verify" quality assurance cycle that is an integral part of the Enterprise Edition release process. The Community Edition does not include the latest bug fixes.

The Community Edition comes with limited concurrency and parallelism and supports a maximum of 4 cores per node.

Documentation, mailing lists, and forums support the Couchbase user community to help troubleshoot issues and answer questions.

## [](#open-source-project)Open Source Project

The Couchbase Server open source project is a platform for innovation. Couchbase is committed to open source development, and the open source project continues to serve as the foundation for both the Community Edition and the Enterprise Edition.

There are many ways to contribute to the open source project:

* Contribute code to our core engine, our SDKs, connectors and other integration components that help us connect to other products through [github.com/couchbase](https://github.com/couchbase). Find more details on the [Open Source Projects](https://developer.couchbase.com/open-source-projects/) page.
* Report issues on our tracking system: [JIRA](https://issues.couchbase.com/projects/MB?selectedItem=com.atlassian.jira.jira-projects-plugin:release-page).
* [Contribute to the documentation](#home:contribute:index.adoc) either by submitting changes on GitHub or by simply clicking the "Feedback" link in our online documentation.

For a feature by feature comparison between editions, take a look at <https://www.couchbase.com/products/editions>.