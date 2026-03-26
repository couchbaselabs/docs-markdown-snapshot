---
title: React Native
description: Using Couchbase Lite with Javascript applications
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/javascript/pages/react.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.1@couchbase-lite:javascript:react.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/javascript/react.html)

# React Native

> Description — _Using Couchbase Lite with Javascript applications_  
> _Abstract — If you are building mobile or desktop applications using web technologies such as JavaScript/HTML/CSS, there are options for using Couchbase Lite as an embedded database within your app._  
> Related Content — [Ionic](ionic.md) | [Cordova](cordova.md)

> [!NOTE]
> Couchbase Lite for React Native is a community-driven project without official support from Couchbase.

To use Couchbase Lite as an embedded database within your React Native app, you need a way to access Couchbase Lite's iOS and Android native APIs from within it.

React Native's _NativeModule_ system provides an answer, exposing instances of native classes to JavaScript (JS) as JS objects.

[React Native Modules](https://reactnative.dev/docs/native-modules-intro)allow mobile apps written in React Native to access native platform APIs. So in order to use Couchbase Lite within your React Native apps, you should implement a React Native plugin that exports the Couchbase Lite Android and iOS APIs to Javascript. It is typical to start with exporting the minimal subset of APIs that your app needs.

Resources

Docs

**[Docs:](https://reactnative.dev/docs/native-modules-intro)** (<https://reactnative.dev/docs/native-modules-intro>)

Tutorial

This tutorial is based on our series of _Getting Started_ User Profile app tutorials.  
**[Get Started:](https://github.com/couchbaselabs/userprofile-couchbase-mobile-reactnative/blob/main/README.md)** (<https://github.com/couchbaselabs/userprofile-couchbase-mobile-reactnative/blob/main/README.md>)

Reference Implementation

[Reference Implementation](https://github.com/couchbaselabs/couchbase-lite-react-native-module/) (<https://github.com/couchbaselabs/couchbase-lite-react-native-module/>)