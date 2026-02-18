---
title: Introduction
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/introduction.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/tutorials/mobile-travel-tutorial/introduction.html)

# Introduction

## [](#application-features)Application Features

This step-by-step tutorial describes a Couchbase Lite Travel application for mobile platforms, which supports the following capabilities:

* Users can search and make flight reservations using the application and-or the Python web application.  
Flight reservations made in the app are available even when the app is disconnected from the server.
* Flight reservations made using any of the client apps are automatically synced with other clients through Sync Gateway.
* Users can access Couchbase Lite’s Full Text Search features to find hotels using either the app or the Python web application.

The following functionality is also available:

* Users can fetch listing of hotels from the Python web backend via a REST endpoint.
* Users can add and remove bookmarks for 'favorite' hotels.  
The bookmarked hotels are stored locally and are available even when the app is disconnected from the server.

## [](#architecture-diagram)Architecture Diagram

This is the high level architecture of the system that we will be running.

![travelsampleapp arch](_images/travelsampleapp-arch.png) 

It includes the following components:

* Client Side  
Couchbase Lite enabled Travel app running on mobile device or desktop.  
Supports iOS, Android, UWP, Xamarin (iOS and Android) and Java Swing App.
* Backend/Server Side

  * Couchbase Server Enterprise v7.0.0
  * Sync Gateway Enterprise v3.0.0
  * Travel web app  
  The Travel Sample web app includes a Python based web backend integrated with Couchbase Python SDK 3.0.x as well as a vue.js based web frontend