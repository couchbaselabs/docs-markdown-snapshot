---
title: New in 3.0
description: Couchbase Sync Gateway -- What's new in the latest release
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/whatsnew.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@sync-gateway::whatsnew.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/whatsnew.html)

# New in 3.0

> Couchbase Sync Gateway — What's new in the latest release  
> This content covers the new features introduced in Sync Gateway 3.0

> [!CAUTION]
> Sync Gateway 3.0 introduces some breaking changes.  
> If you are upgrading from 2.x, please refer to the [Upgrading](upgrading.md) page.

## [](#overview-of-syncgateway-3-0)Overview of Sync Gateway 3.0

_This release of Sync Gateway introduces significant strategic new features and enhancements aimed at boosting the functionality supporting mobile and edge computing solutions._

Most significant are the major architectural enhancements to make sync gateway node configuration simpler, more modular and cluster-aware. The secure, encrypted, REST API endpoints now support persistent configuration changes to simplify management and administration.

## [](#centralized-persistent-modular-configuration)Centralized Persistent Modular Configuration

_Centralized Persistent Modular Configuration is a core enhancement that makes it simpler for administrators to configure and manage the Sync Gateway._

This enhancement removes reliance on monolithic JSON configuration files whilst providing a modular and _cluster-aware_ approach to Sync Gateway node configuration.

Basic startup configuration settings bootstrap your Sync Gateway nodes and securely connect them to a Couchbase Server. Configuration of cluster-wide Sync Gateway databases, access control policies and inter-Sync Gateway replications is then provided using the Admin REST API.

Persistent configuration changes made to any node in a sync gateway cluster are automatically propagated throughout the cluster or — by using Sync gateway groups — a defined cluster subset. These changes persist across sync gateway restarts.

Your existing JSON configurations can be automatically converted to the new centralized persistent modular configuration format on start-up; there is an opt-out for user wishing to temporarily continue working in legacy mode.

More

[Configuration Overview](configuration-overview.md)

## [](#secure-administration)Secure Administration

_This major enhancement complements the introduction of the centralized persistent configuration by introducing secure administration of a cluster through the Admin REST API._

The Admin REST API now enforces authentication and role-based access control by default.

All Admin API traffic must be conducted using existing, valid, Couchbase Server RBAC user credentials. These users must be set-up with specific sync gateway roles.

A similar approach is also adopted for users of the Metrics API. Public API users are not impacted by the change.

More

[REST API Access](rest-api-access.md)

## [](#tls-encryption-enabled-by-default)TLS Encryption Enabled by Default

_The default enabling of secure TLS connections for all Couchbase Server,side communication ensures that all such communication is encrypted; enforcing and encouraging security best practices._

Sync Gateway supports v1.3 of TLS. No un-encrypted access using non-TLS schemes (for example, `couchbase://` or `http://`) is permitted for server side network through Couchbase Server.

While we strongly recommend always having TLS enabled, we recognize that users may want to disable it for development and testing environments; there is an opt-out option to do this.

More

[Secure Sync Gateway Access](secure-sgw-access.md)

## [](#user-defined-extended-attributesxattrs-for-access-control)User Defined Extended Attributes(XAttrs) for Access Control

_Use extended attributes (metadata) to avoid the need to embed sensitive access grant information such as channels and roles within document bodies._

This key architectural enhancement enforces separation of concerns by providing you the option to use Extended Attributes (XATTRs) to specify channel access grants outside of your document bodies.

In addition to addressing privacy concerns, this feature can result in bandwidth savings as it ensures that changes to access grants do not impact document body content and so are no longer propagated to clients.

More

[Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md)

## [](#auto-purge-on-channel-access-revocation-in-inter-sync-gateway-replication)Auto-Purge on Channel Access Revocation in Inter-Sync Gateway Replication

_This enhancement to inter-Sync Gateway replication technology helps with the enforcement of data privacy and governance in complex workflows._

Sync gateway nodes can replicate data with each other using [inter-Sync Gateway replication](sync-inter-syncgateway-overview.md) technology.

When a user loses access to a channel (and therefore the documents in it) you can opt to enable the initiating sync gateway cluster to auto-purge those documents in the revoked channel.

More

[Auto-purge on Channel Access Revocation](auto-purge-channel-access-revocation.md)

## [](#use-environment-variables-in-configuration-file)Use Environment Variables in Configuration File

Sync Gateway configuration is extended to allow the use of defined _environment variables_ as substitution values inside the configuration file. This allows users to determine, pick-up and substitute appropriate values during Sync Gateway start-up.

The use of environment variables within the configuration file increases the flexibility of the configuration process. It makes the switching of the runtime behavior — for example during development, experimentation or testing — much easier.

More

[Configuration Environment Variables](configuration-environment-variables.md)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function-overview.md)
* [Import filter](import-filter.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)