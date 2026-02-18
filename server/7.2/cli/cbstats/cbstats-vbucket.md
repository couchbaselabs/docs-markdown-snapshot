---
title: vbucket
description: Provides detailed statistics on a per vbucket granularity.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbstats/cbstats-vbucket.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/cli/cbstats/cbstats-vbucket.html)

# vbucket

> Provides detailed statistics on a per vbucket granularity. 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] vbucket

## [](#description)Description

This command lists all available vBuckets and provides information about their type: active, replica, pending or dead.

## [](#options)Options

There are no options for this command. For common `cbstats` options, see [cbstats](../cbstats-intro.md).

## [](#example)Example

**Request**

cbstats -u Administrator -p password -b beer-sample localhost:11210 vbucket

**Response**

 vb_0:    replica
 vb_1:    replica
 vb_10:   replica
 vb_100:  active
 vb_1000: replica
 vb_1001: replica
 vb_1002: replica
 vb_1003: replica
 vb_1004: replica
 vb_1005: replica
 ...