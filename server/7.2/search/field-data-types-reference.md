---
title: Field Data Types
description: You can assign a data type to a field to tell the Search Service
  how to analyze its data.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/field-data-types-reference.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/search/field-data-types-reference.html)

# Field Data Types

> You can assign a data type to a field to tell the Search Service how to analyze its data. 

When you [create a child field](create-child-field.md) on a type mapping or [Create a Search Index with the Quick Editor](create-quick-index.md), you need to set a field’s data type.

When you create a Search index and don’t set a data type for a field, the Search Service automatically assigns a field data type.

The following field data types are available:

| Field Data Type | Description                                                                                                                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| text            | The field contains a string. The string can contain numbers and special characters.                                                                                                                                                                                 |
| number          | The field contains a number. It doesn’t contain any alphabetic characters.                                                                                                                                                                                          |
| datetime        | The field contains a date/time value that matches the format of a [Date/Time Parser](customize-index.md#date-time) in the index.                                                                                                                                    |
| boolean         | The field contains a true or false value.                                                                                                                                                                                                                           |
| disabled        | This field data type is deprecated. It’s included for compatibility only.                                                                                                                                                                                           |
| geopoint        | The field contains geopoint (latitude and longitude) data, represented as either: A string, as two numeric values separated by a comma. A string, as a geohash point. An array, as two floating point integers. A JSON object, with the properties lon/lng and lat. |
| geoshape        | The field contains a GeoJSON object. For more information about GeoJSON objects, see [Search Request JSON Properties](../../current/search/search-request-params.md).                                                                                               |
| ip              | The field contains an IP address, formatted in IPv4 or IPv6 CIDR syntax. For example: {     "ipv4": "4.7.44.162",     "ipv6": "2001:4800:0000:0000:0000:0000:0000:0000" }                                                                                           |