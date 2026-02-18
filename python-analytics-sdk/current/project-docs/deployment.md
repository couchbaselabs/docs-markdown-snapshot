---
title: Deployment
description: Transition from dev environment to prod, and keep up with the latest fixes.
editUrl: https://github.com/couchbase/docs-analytics-sdk-python/edit/release/1.0/modules/project-docs/pages/deployment.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/python-analytics-sdk/current/project-docs/deployment.html)

# Deployment

> Transition from dev environment to prod, and keep up with the latest fixes. 

One of Couchbase’s strengths is speedy response, so deployment of apps should be in the same region as the Server.

We always recommend the [latest version](analytics-sdk-release-notes.md#latest-release) of the SDK. This not only contains the latest security updates and bug fixes, but will be compatible with the latest Enterprise Analytics release.

Before deploying, take note of any [compatibility](compatibility.md) issues for the language platform and underlying OS. The [full installation guide](sdk-full-installation.md) should cover any special cases for all supported environments.

## [](#development-testing-environments)Development & Testing Environments

During development, some shortcuts are taken to get up and running which would not be acceptable during deployment. These include use of administrator permissions, connecting from your laptop instead of a secure app server, and even disabling certificate verification for TLS. Testing environments may also differ from deployment.

The Python Analytics SDK docs note whenever a shortcut is being taken, but here is a non-exhaustive list of those development practices which should not be carried over to production deployments:

* Over-privileged access
* Geographical separation of app server and database
* Skipping certificate verification

The best way to accommodate developing an application that is to be deployed to production is to use the platform’s default approach for configuration files.