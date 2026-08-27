---
title: Cordova
description: Using Couchbase Lite with Javascript applications
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/javascript/pages/cordova.adoc
  xref: xref:3.0@couchbase-lite:javascript:cordova.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/javascript/cordova.html)

# Cordova

> Description — _Using Couchbase Lite with Javascript applications_  
> _Abstract — If you are building mobile or desktop applications using web technologies such as JavaScript/HTML/CSS, there are options for using Couchbase Lite as an embedded database within your app._  
> Related Content — [Ionic](ionic.md) | [React Native](react.md)

> [!NOTE]
> Enterprise-only
> 
> Ionic supports both [Capacitor](https://capacitorjs.com/docs/plugins) and Cordova, with Ionic recommending use of Capacitor.

## [](#introduction)Introduction

To use Couchbase Lite as an embedded database within your Cordova-based app, you need a way to access Couchbase Lite's iOS and Android native APIs from within your Cordova web application.

## [](#native-functionality)Native Functionality

[Cordova Native Plugins](https://cordova.apache.org/docs/en/10.x/guide/hybrid/plugins/index.html)allow web-based apps running in a Cordova webview to access native platform functionality through a Javascript interface.

To use Couchbase Lite within your Cordova apps, you should implement a Cordova native plugin, which exports the Couchbase Lite Android and iOS APIs to Javascript. It is typical to start with exporting the minimal subset of APIs that your app needs and extend as needed.

**A reference implementation of a Cordova plugin will be available shortly.**