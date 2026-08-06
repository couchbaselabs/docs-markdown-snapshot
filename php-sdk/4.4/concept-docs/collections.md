---
title: Collections and Scopes
description: Fully supported from Couchbase Server 7.0.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.4/modules/concept-docs/pages/collections.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.4@php-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.4/concept-docs/collections.html)

# Collections and Scopes

> Fully supported from Couchbase Server 7.0\. 

The Collections feature in Couchbase Server is fully implemented in the 3.x API versions of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#8.0@server:learn:data:scopes-and-collections.adoc).

## [](#using-collections-scopes)Using Collections & Scopes

Access a non-default collection, in the default scope, with:

```php
$bucket->scope('_default')->collection('bookings');
```

And for a non-default scope:

```php
$bucket->scope('tenant_agent_00')->collection('bookings');
```

## [](#further-reading)Further Reading

To see Collections in action, take a look at our [Collections-enabled Travel Sample page](../howtos/working-with-collections.md).