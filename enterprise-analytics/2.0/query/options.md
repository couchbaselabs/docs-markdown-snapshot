---
title: Set Query Options
description: You can use the <strong>query options</strong> to change the query
  timeout period, define request-level parameters, and so on.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/query/pages/options.adoc
  xref: xref:2.0@enterprise-analytics:query:options.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/query/options.html)

# Set Query Options

> You can use the **query options** to change the query timeout period, define request-level parameters, and so on. 

## [](#prerequisites)Prerequisites

To use the Enterprise Analytics UI, you need the `**Enterprise Analytics Access**` role along with specific privileges.

## [](#access-query-settings)Access Query Settings

You can specify various query options by clicking the Settings icon at the top right corner. This opens the Run-Time Preferences menu.

## [](#available-query-options)Available Query Options

When you select **query options**, you can define the following settings and request-level parameters and click **Save Preferences** to save the configuration.

* Query Timeout
* Collect query timings
* Scan Consistency
* Positional Parameters
* Named Parameters

Descriptions of these settings follow.

### [](#query-timeout-setting)Query Timeout Setting

You define a query timeout to specify the maximum time, in seconds, for the system to spend on a query before timing out.

This setting has a default value of 1800 with 1 being the lowest value.

### [](#collect-query-timings)Collect Query Timings

To collect per-operator query timings during query execution and display them in the query plan, click **Collect query timings**. By default, this option is not selected.

### [](#scan-consistency-setting)Scan Consistency Setting

The scan consistency setting specifies the consistency guarantee for scanning. You can select 1 of the following options:

* **not\_bounded**: The scan does not use a timestamp vector. This is the fastest mode, because it avoids the costs of obtaining the vector.
* **request\_plus**: This option implements bounded consistency. Before processing the request, a current vector is obtained. The vector is used as a lower bound for the statements in the request.

### [](#positional-parameters)Positional Parameters

Positional parameters use numeric identifiers to represent values to supply in a query. Enterprise Analytics automatically supplies numbered identifiers for these parameters as you add them: $1, $2, and so on. The value you enter must use JSON formatting, such as enclosing strings in quotation marks.

To add positional parameters, click the + button. To remove parameters from last to first, click the - button.

Example

You define the following positional parameters:

$1 "Paris"
$2 "Gare du Nord"

When you run the following query:

```SQL++
SELECT * FROM travel-sample.inventory.airport
WHERE airportname <> $2 AND city = $1;
```

The result returns the 8 documents that have `"Paris"` as the city but that do not have `"Gare du Nord"` as the airport name.

You can then reuse these parameters in other queries as is, change their values, or delete them.

### [](#named-parameters)Named Parameters

Named parameters store an identifying variable name in addition to the value. The name must start with $, and the value must use JSON formatting, such as enclosing strings in quotation marks.

To add named parameters, click the + button. To remove parameters from last to first, click the - button.

Example

You define a parameter, $n, and specify a value of `"Orbit Airlines"` for it.

When you run the following query:

```SQL++
SELECT * FROM travel-sample.inventory.airport
WHERE name = $n;
```

The result returns the single document that has an airline name of `"Orbit Airlines"`.

You can then reuse `$n` in other queries as is, change its value, update its name, or delete it.

## [](#see-also)See Also

* [Query and Explore with the Workbench](workbench.md)
* [Write and Run Queries](editor.md)
* [Work with Query Results](results.md)
* [Connecting to Data Sources](../intro/connecting-to-data-sources.md)
* [SELECT Statements](../sqlpp/3%5Fquery.md)