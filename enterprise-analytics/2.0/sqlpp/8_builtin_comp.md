---
title: Comparison Functions
description: This topic describes the builtin SQL++ for Enterprise Analytics
  comparison functions.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/8_builtin_comp.adoc
  xref: xref:2.0@enterprise-analytics:sqlpp:8_builtin_comp.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sqlpp/8_builtin_comp.html)

# Comparison Functions

> This topic describes the builtin SQL++ for Enterprise Analytics comparison functions. 

## [](#ComparisonFunctions)Comparison Functions

## [](#greatest)greatest

* Syntax:  
greatest(numeric_value1, numeric_value2, ...)
* Computes the greatest value among arguments.
* Arguments:

  * `numeric_value1`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * `numeric_value2`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * …​.
* Return Value:

  * the greatest values among arguments. The returning type is decided by the item type with the highest order in the numeric type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among items.
  * `null` if any argument is a `missing` value or `null` value,
  * any other non-numeric input value causes a type error.
* Example:  
{ "v1": greatest(1, 2, 3), "v2": greatest(float("0.5"), double("-0.5"), 5000) };
* The expected result is:  
{ "v1": 3, "v2": 5000.0 }

## [](#least)least

* Syntax:  
least(numeric_value1, numeric_value2, ...)
* Computes the least value among arguments.
* Arguments:

  * `numeric_value1`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * `numeric_value2`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * …​.
* Return Value:

  * the least values among arguments. The returning type is decided by the item type with the highest order in the numeric type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among items.
  * `null` if any argument is a `missing` value or `null` value,
  * any other non-numeric input value causes a type error.
* Example:  
{ "v1": least(1, 2, 3), "v2": least(float("0.5"), double("-0.5"), 5000) };
* The expected result is:  
{ "v1": 1, "v2": -0.5 }