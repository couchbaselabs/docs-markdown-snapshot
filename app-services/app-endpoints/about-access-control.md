---
title: About Access Control
description: Learn about Access Control in App Services, how Users, Roles, and
  Channels work together, and how to secure your data.
pubDate: 2026-09-25T04:30:57.829Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/about-access-control.adoc
  xref: xref:app-services::app-endpoints/about-access-control.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/about-access-control.html)

# About Access Control

> Learn about Access Control in App Services, how Users, Roles, and Channels work together, and how to secure your data. 

Access Control in App Services has two parts:

* Channels: Determines which clients receive a document when they sync.
* [Access Control and Data Validation Function](access-control-data-validation.md): Determines whether a client can write or delete a document.

This page covers the first part: how documents reach the right users through channels.

## [](#key-concepts)Key Concepts

* App Services builds Access Control from 3 entities: Users, Roles, and Channels.
* Channels tag documents and act as the conduit between a document and a user.
* Users gain channel access directly, or by inheriting it from a role.
* Your [Access Control and Data Validation Function](access-control-data-validation.md) assigns documents to channels on every write.
* A client can sync at most the documents in the channels its user has access to.

## [](#why-access-control-matters)Why Access Control Matters

Every document synced through an App Endpoint passes through your [Access Control and Data Validation Function](access-control-data-validation.md). The function assigns the document to channels, which determines which clients receive it. The function can also reject the write, which determines who may create, update, or delete documents.

An incorrectly configured function can lock authorized users out of needed data. It can also expose data to unauthorized users. Review your function as part of any security review of your application.

## [](#the-three-entities)Entities

### [](#channels)Channels

A channel is a tag attached to a document. Your Access Control and Data Validation Function assigns documents to channels. A user gains access to 1 or more channels, either directly or through a role. Channels control which documents a client receives. A channel name only has meaning within the collection it belongs to, so `orders` in the `sales.invoices` collection and `orders` in the `hr.employees` collection are two separate channels. Granting a user access to `orders` in one collection grants them no access in the other. For more information, see [Add Security with Channels](../security/channels.md).

### [](#users)Users

Users are one of the cornerstone concepts of access control. You can restrict document access to specific users and-or to users with specific [roles](../security/create-app-role.md#app-roles).

For more information, see [Create App Users](../security/create-user.md).

### [](#roles)Roles

Roles are named collections of [Channels](../security/channels.md), where channels are organised within a linked Collection to a given Scope within your App Endpoint. They enable the grouping together of [Users](../security/create-user.md) with similar characteristics, which makes the management of large user populations easier.

For more information, see [Create App Roles](../security/create-app-role.md).

## [](#assign-channels)Assign Channels

You can grant channels to a user or role in 2 ways. Most applications use a mix of both.

Admin Channels

You assign these channels statically. Assign them in the Capella UI on the [Create App User](../security/create-user.md) page, or through the [Admin REST API](../references/rest%5Fapi%5Fadmin.md).

Use this method when access does not change based on document content. For example, grant a support team access to a fixed set of channels.

Channels from the Access Control and Data Validation Function

This function assigns channels dynamically, based on the content of each document.

Use this method when access depends on document data. For example, route a document to a channel named after its owner or team.

> [!IMPORTANT]
> You cannot edit or delete channels created by the Access Control and Data Validation Function in the Capella UI or the Admin REST API. Edit the function itself to apply any changes.

The function only runs on a write, so existing documents keep their current channel assignments until you [resync](resync.md) the collection to re-run the function over them.

## [](#see-also)See Also

* [Create App Users](../security/create-user.md)
* [Create App Roles](../security/create-app-role.md)
* [Add Security with Channels](../security/channels.md)
* [Access Control and Data Validation](access-control-data-validation.md)
* [About App Endpoints](about-app-endpoints.md)