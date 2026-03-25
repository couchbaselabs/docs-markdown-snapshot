---
title: Ionic
description: Using Couchbase Lite with Javascript Ionic applications
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/javascript/pages/ionic.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@couchbase-lite:javascript:ionic.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/javascript/ionic.html)

# Ionic

> Description — _Using Couchbase Lite with Javascript Ionic applications_  
> _Abstract — If you are building mobile or desktop applications using web technologies such as JavaScript/HTML/CSS, there are options for using Couchbase Lite as an embedded database within your app._  
> Related Content — [Cordova](cordova.md) | [React Native](react.md)

> [!IMPORTANT]
> Support Changes
> 
> * The Ionic plugin is now open source and community supported.
> * The Couchbase Lite API, which contains storage and sync functionality, is fully supported as normal for Enterprise customers.

## [](#introduction)Introduction

Ionic’s Couchbase Lite integration is an open source solution for web developers, enabling easy to build secure, high-performance, offline-enabled apps.

This integration supports apps built for iOS, Android, and native Windows.

> [!NOTE]
> Users can build their own native plugin on top of Couchbase Lite’s native API for iOS and Android. Ionic recommends use of [Capacitor](https://capacitorjs.com/docs/plugins), which can be used independent of the application’s UI layer, to access native functionality from within Ionic apps.

## [](#open-source-plugin)Open source Plugin

There are several benefits to be drawn from the open source Ionic integration with Couchbase Lite:

1. It is free to use.
2. You have the flexibility to customise the plugin to your needs.
3. You have more control over the functionality of the plugin and how it interacts with your applications.
4. You can contribute to and engage with a community of developers who also make use of the plugin.

Alternatively, you can build your own native application on top of [Capacitor](https://capacitorjs.com/docs/plugins).

## [](#accessing-couchbase-lite)Accessing Couchbase Lite

Using a robust JavaScript API, you can access the entirety of Couchbase Lite’s functionality with no native experience required.

As a starting point, you should follow the hotel search tutorial.  
The tutorial shows how to build an app that allows users to search and bookmark hotels. It uses data loaded from a Couchbase Lite database — see the tutorial at <https://ionic.io/docs/couchbase-lite/tutorials/hotel-search>

Resources

Docs

<https://ionic.io/docs/couchbase-lite>.

Tutorial

<https://ionic.io/docs/couchbase-lite/tutorials/hotel-search>

Demo

<https://github.com/ionic-team/demo-couchbaselite-hotels>

Download

Reach out to _Ionic_ sales to get access, either from the [docs page](https://ionic.io/docs/couchbase-lite) or this [landing page](https://ionic.io/integrations/couchbase-lite)