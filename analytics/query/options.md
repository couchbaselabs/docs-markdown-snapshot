---
title: Set Query Options
description: You can use the <strong>query options</strong> to change the query
  timeout period, define request-level parameters, and so on.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/query/pages/options.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/analytics/query/options.html)

# Set Query Options

> You can use the **query options** to change the query timeout period, define request-level parameters, and so on. 

## [](#prerequisites)Prerequisites

To use the workbench for Capella Analytics:

* You must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your cluster:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) (Allows queries that read and write data)
  * [Database Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader) (Allows read-only queries)

## [](#available-query-options)Available Query Options

When you select **query options**, you can define the following settings and request-level parameters:

* Collect Query Timings
* Query Timeout
* Scan Consistency
* Positional Parameters
* Named Parameters

Descriptions of these settings follow.

### [](#collect-query-timings)Collect Query Timings

Collects per-operator query timings during query executions and displays them in the query plan. Enable only when performance monitoring is required to avoid additional processing overhead.

### [](#query-timeout-setting)Query Timeout Setting

You define a query timeout to specify the maximum time, in seconds, for the system to spend on a query before timing out.

This setting accepts a value from 1 to 1800, with a default of 1800.

### [](#scan-consistency-setting)Scan Consistency Setting

The scan consistency setting specifies the consistency guarantee for index scanning. You can select one of the following options:

* **not\_bounded**: The index scan does not use a timestamp vector. This is the fastest mode, because it avoids the costs of obtaining the vector and waiting for the index to catch up to the vector.
* **request\_plus**: This option implements bounded consistency. The request includes a scan\_vector parameter and value, which is used as a lower bound. You can use this setting to implement read-your-own-writes (RYOW).

### [](#positional-parameters)Positional Parameters

Positional parameters use numeric identifiers to represent values to supply in a query. Capella Analytics automatically supplies numbered identifiers for these parameters as you add them: $1, $2, and so on. The value you enter must use JSON formatting, such as enclosing strings in quotation marks.

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

The result returns the eight documents that have `"Paris"` as the city but that do not have `"Gare du Nord"` as the airportname.

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
* [Access Data](../intro/examples.md)
* [SELECT Statements](../sqlpp/3%5Fquery.md)