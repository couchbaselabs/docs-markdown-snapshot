---
title: Prepare Statements for Reuse
description: How to create and execute prepared statements, including
  placeholder parameters.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/prep-statements.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:server:guides:prep-statements.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/guides/prep-statements.html)

# Prepare Statements for Reuse

> How to create and execute prepared statements, including placeholder parameters. 

## [](#introduction)Introduction

If you need to execute certain SQL++ statements repeatedly, you can use placeholder parameters and prepared statements to optimize query reuse.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#placeholders)Adding Placeholder Parameters

You can add placeholder parameters to a statement, so that you can safely supply variable values when you run the statement. You can add placeholder parameters in the WHERE clause, the LIMIT clause, or the OFFSET clause.

A placeholder parameter may be a named parameter or a positional parameter.

* To add a named parameter to a query, enter a dollar sign `$` or an at sign `@` followed by the parameter name.
* To add a positional parameter to a query, enter a dollar sign `$` or an at sign `@` followed by the number of the parameter, or enter a question mark `?`.

The following example includes two named parameters.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT COUNT(*) FROM airport
WHERE country = $country AND geo.alt > @altitude;
```

To execute this query, the parameters must be supplied by name.

The following example includes two numbered positional parameters.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT COUNT(*) FROM airport
WHERE country = $1 AND geo.alt > @2;
```

To execute this query, the parameters must be supplied as a list, in order of the placeholder numbers.

The following example includes two unnumbered positional parameters.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT COUNT(*) FROM airport
WHERE country = ? AND geo.alt > ?;
```

To execute this query, the parameters must be supplied as a list, in the order in which the placeholders appear in the statement.

## [](#values)Supplying Parameter Values

To run a query containing placeholder parameters, you must supply values for the parameters.

* SQL++
* .NET
* Java
* Node.js
* Python

To supply values for placeholder parameters using the cbq shell:

* Use the `\SET` command to set the parameters before running the statement.
* Use the `-args` parameter to specify positional parameters.
* Use `-$` or `-@` followed by a parameter name to specify named parameters.

To supply values for placeholder parameters using the SQL++ REST API:

* Specify the parameters in the request body or the query URI, alongside the statement.
* Use the `args` parameter to specify positional parameters.
* Use `$` or `@` followed by a parameter name to specify named parameters.

To supply values for placeholder parameters using the Query Workbench:

* Use the cog icon  to display the Run-Time Preferences window before running the statement.
* Use the **Positional Parameters** options to specify positional parameters.
* Use the **Named Parameters** options to specify named parameters.

> [!TIP]
> When you're executing a prepared statement, the `EXECUTE` statement provides another, easier way to supply parameter values. See [Executing a Prepared Statement](#execute).

---

Context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Queries

The following query supplies positional parameter values using the cbq shell.

```sqlpp
\SET -args ["France", 500];

SELECT COUNT(*) FROM airport
WHERE country = $1 AND geo.alt > @2;
```

The following query supplies positional parameter values using the Query Workbench.

1. Click the cog icon  to display the Run-Time Preferences window.
2. Next to **Positional Parameters**, click **+**.
3. In the **$1** box, enter `"France"`.
4. Next to **Positional Parameters**, click **+** again.
5. In the **$2** box, enter `500`.
6. Choose **Save Preferences**.
7. Run the following query.

```sqlpp
SELECT COUNT(*) FROM airport
WHERE country = $1 AND geo.alt > @2;
```

The following query supplies named parameter values using the cbq shell.

```sqlpp
\SET -@country "France";
\SET -$altitude 500;

SELECT COUNT(*) FROM airport
WHERE country = $country AND geo.alt > @altitude;
```

The following query supplies named parameter values using the Query Workbench.

1. Click the cog icon  to display the Run-Time Preferences window.
2. Next to **Named Parameters**, click **+**.
3. In the first **name** box, enter `country`, and in the **value** box, enter `"France"`.
4. Next to **Named Parameters**, click **+** again.
5. In the next **name** box, enter `altitude`, and in the **value** box, enter `500`.
6. Choose **Save Preferences**.
7. Run the following query.

```sqlpp
SELECT COUNT(*) FROM airport
WHERE country = $country AND geo.alt > @altitude;
```

For more information and examples, see [Configure Queries](../n1ql/n1ql-manage/query-settings.md).

To supply values for placeholder parameters, use the `Parameter` method on the `QueryOptions` object.

> [!TIP]
> The SDK has different versions of the `Parameter` method for supplying a single named parameter, a collection of named parameters, a single positional parameter, or a list of positional parameters.

---

The following example supplies a single positional parameter.

```csharp
var result = await cluster.QueryAsync<dynamic>(
    "SELECT t.* FROM `travel-sample` t WHERE t.type=$1",
    options => options.Parameter("landmark")
);
```

The following example supplies a single named parameter.

```csharp
var result = await cluster.QueryAsync<dynamic>(
    "SELECT t.* FROM `travel-sample` t WHERE t.type=$type",
    options => options.Parameter("type", "landmark")
);
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Query.QueryOptions.html).

To supply values for placeholder parameters, use the `parameter` method on the `QueryOptions` object.

> [!TIP]
> The SDK has different versions of the `parameter` method for supplying named parameters or positional parameters.

---

The following example supplies a single positional parameter.

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airline where country = ?",
    queryOptions().parameters(JsonArray.from("France")));
```

The following example supplies a single named parameter.

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airline where country = $country",
    queryOptions().parameters(JsonObject.create().put("country", "France")));
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/query/QueryOptions.html).

To supply values for placeholder parameters, use the `parameters` property on the `QueryOptions` interface.

> [!TIP]
> The `parameters` property may be an object for supplying named parameters, or an array for supplying positional parameters.

---

The following example supplies a single positional parameter.

```javascript
async function queryPlaceholders() {
  const query = `
  SELECT airportname, city FROM \`travel-sample\`.inventory.airport
  WHERE city=$1
  `;
  const options = { parameters: ['San Jose'] }

  try {
    let result = await cluster.query(query, options)
    console.log("Result:", result)
    return result
  } catch (error) {
    console.error('Query failed: ', error)
  }
}
```

The following example supplies a single named parameter.

```javascript
async function queryNamed() {
  const query = `
    SELECT airportname, city FROM \`travel-sample\`.inventory.airport
    WHERE city=$CITY;
  `
  const options = { parameters: { CITY: 'Reno' } }

  try {
    let result = await cluster.query(query, options)
    console.log("Result:", result)
    return result
  } catch (error) {
    console.error('Query failed: ', error)
  }
}
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/QueryOptions.html).

To supply positional parameter values for a query or prepared statement, use the `positional_parameters` parameter in the `QueryOptions`.

To supply named parameter values for a query or prepared statement, use the `named_parameters` parameter in the `QueryOptions`.

> [!TIP]
> Alternatively, you can supply positional parameters or named parameters as keyword arguments for the `query()` function.

---

The following examples supply a single positional parameter.

```python
Unresolved include directive in modules/guides/pages/prep-statements.adoc - include::python-sdk:howtos:example$n1ql_ops.py[]
```

```python
Unresolved include directive in modules/guides/pages/prep-statements.adoc - include::python-sdk:howtos:example$n1ql_ops.py[]
```

The following examples supply a single named parameter.

```python
Unresolved include directive in modules/guides/pages/prep-statements.adoc - include::python-sdk:howtos:example$n1ql_ops.py[]
```

```python
Unresolved include directive in modules/guides/pages/prep-statements.adoc - include::python-sdk:howtos:example$n1ql_ops.py[]
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/options.html#queryoptions).

## [](#prepare)Creating a Prepared Statement

If you need to run a statement more than once, you can prepare the execution plan for the statement and cache it for reuse.

> [!NOTE]
> You can include placeholder parameters in the prepared statement, if necessary.

* SQL++
* .NET
* Java
* Node.js
* Python

To create a prepared statement, use the `PREPARE` statement.

1. If necessary, set the [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context) to the bucket and scope where you want to create the prepared statement.
2. Use the FROM / AS clause to specify a name for the prepared statement, if required. If you do not, a name is generated automatically.

---

Context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

The following query prepares the execution plan for the given statement, including the specified positional parameters.

```sqlpp
PREPARE NumParam AS
SELECT * FROM hotel
WHERE city=$1 AND country=$2;
```

Result

```json
"name": "[127.0.0.1:8091]NumParam", (1)
```

| **1** | The query returns the name of the prepared statement. |
| ----- | ----------------------------------------------------- |

Query

The following query prepares the execution plan for the given statement, including the specified named parameters.

```sqlpp
PREPARE NameParam AS
SELECT * FROM hotel
WHERE city=$city AND country=$country;
```

Result

```json
"name": "[127.0.0.1:8091]NameParam", (1)
```

| **1** | The query returns the name of the prepared statement. |
| ----- | ----------------------------------------------------- |

For more information and examples, see [PREPARE](../n1ql/n1ql-language-reference/prepare.md).

To create a prepared statement, use the `Cluster.QueryAsync<T>` method with the `adhoc` query option set to false.

---

The following example executes a query with the specified parameters. If this query has not been executed before, the query plan is cached for reuse.

```csharp
var result = await cluster.QueryAsync<dynamic>(
    "select count(*) from `travel-sample`.inventory.airport where country = ?",
    options =>
        options.Parameter("France")
        .AdHoc(false);
);
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/QueryOptions.html).

To create a prepared statement, use the `query()` method with the `AdHoc` query option set to false.

---

The following example executes a query with the specified parameters. If this query has not been executed before, the query plan is cached for reuse.

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airport where country = ?",
    QueryOptions.queryOptions().adhoc(false).parameters(JsonArray.from("France"))
);
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Query.QueryOptions.html).

To create a prepared statement, use the `query()` function with the `adhoc` query option set to false.

---

The following example executes a query with the specified parameters. If this query has not been executed before, the query plan is cached for reuse.

```javascript
async function queryNamed() {
  const query = `
  SELECT airportname, city FROM \`travel-sample\`.inventory.airport
  WHERE city=$1
  `;
  var options = { adhoc: false, parameters: ['London'] }

  try {
    let result = await cluster.query(query, options)
    console.log("Result:", result)
    return result
  } catch (error) {
    console.error('Query failed: ', error)
  }
}
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/QueryOptions.html).

To create a prepared statement, use the `query()` function with the `adhoc` query option set to false.

---

The following example executes a query with the specified parameters. If this query has not been executed before, the query plan is cached for reuse.

```python
result = cluster.query(
    """SELECT airportname, city
    FROM \`travel-sample\`.inventory.airport
    WHERE city=$1;""",
    'London', QueryOptions(adhoc=false))
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/options.html#queryoptions).

## [](#execute)Executing a Prepared Statement

When you execute a prepared statement, the cached execution plan is reused, so the query executes faster.

> [!NOTE]
> You can supply parameter values for a prepared statement, just as you can for a query. These can be different to the parameter values that you supplied when you created the prepared statement.

* SQL++
* .NET
* Java
* Node.js
* Python

To execute a prepared statement, use the `EXECUTE` statement.

1. If necessary, set the [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context) to the bucket and scope where you created the prepared statement.
2. Supply the name of the prepared statement, as provided when you created the prepared statement.
3. If necessary, use the USING clause to supply the values for parameters in the prepared statement.

  * Specify positional parameters using an array of values.
  * Specify named parameters using an object containing name / value properties.

---

Context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Queries

The following query executes a prepared statement, including the specified positional parameters.

```sqlpp
EXECUTE NumParam
USING ["Paris", "France"];
```

The following query executes a prepared statement, including the specified named parameters.

```sqlpp
EXECUTE NameParam
USING {"city": "Paris", "country": "France"};
```

For more information and examples, see [EXECUTE](../n1ql/n1ql-language-reference/execute.md).

To execute a prepared statement, use the `Cluster.QueryAsync<T>` method to run the prepared statement query string again, with the `adhoc` query option set to false.

Specify parameter values for the query, if necessary.

---

The following example executes a query with the specified parameters. If a prepared statement has been created from this query previously, the cached query plan is reused.

```csharp
var result = await cluster.QueryAsync<dynamic>(
    "select count(*) from `travel-sample`.inventory.airport where country = ?",
    options =>
        options.Parameter("France")
        .AdHoc(false);
);
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/QueryOptions.html).

To execute a prepared statement, use the `query()` method to run the prepared statement query string again, with the `AdHoc` query option set to false.

Specify parameter values for the query, if necessary.

---

The following example executes a query with the specified parameters. If a prepared statement has been created from this query previously, the cached query plan is reused.

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airport where country = ?",
    QueryOptions.queryOptions().adhoc(false).parameters(JsonArray.from("France"))
);
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Query.QueryOptions.html).

To execute a prepared statement, use the `query()` function to run the prepared statement query string again, with the `adhoc` query option set to false.

Specify parameter values for the query, if necessary.

---

The following example executes a query with the specified parameters. If a prepared statement has been created from this query previously, the cached query plan is reused.

```javascript
async function queryNamed() {
  const query = `
  SELECT airportname, city FROM \`travel-sample\`.inventory.airport
  WHERE city=$1
  `;
  var options = { adhoc: false, parameters: ['London'] }

  try {
    let result = await cluster.query(query, options)
    console.log("Result:", result)
    return result
  } catch (error) {
    console.error('Query failed: ', error)
  }
}
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/QueryOptions.html).

To execute a prepared statement, use the `query()` function to run the prepared statement query string again, with the `adhoc` query option set to false.

Specify parameter values for the query, if necessary.

---

The following example executes a query with the specified parameters. If a prepared statement has been created from this query previously, the cached query plan is reused.

```python
result = cluster.query(
    """SELECT airportname, city
    FROM \`travel-sample\`.inventory.airport
    WHERE city=$1;""",
    'London', QueryOptions(adhoc=false))
```

For details, see [QueryOptions](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/options.html#queryoptions).

## [](#related-links)Related Links

Overview:

* [SQL++ Queries and Results](../n1ql/n1ql-intro/queriesandresults.md)

Reference:

* [Manage and Monitor Prepared Statements](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-prepared)
* [SQL++ Admin REST API for Prepared Statements](../n1ql-rest-admin/index.md#tag-PreparedStatements)

Querying with SDKs:

* [C](../../../c-sdk/current/howtos/n1ql-queries-with-sdk.md)| [C++](../../../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [.NET](../../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Go](../../../go-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Java](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/n1ql-queries.md)| [Node.js](../../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Python](../../../python-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Rust](../../../rust-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)

Prepared statements with SDKs:

* [C](../../../c-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [C++](../../../cxx-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [.NET](../../../dotnet-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [Go](../../../go-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [Java](../../../java-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [Kotlin](../../../kotlin-sdk/current/howtos/n1ql-queries.md#prepared-statements)| [Node.js](../../../nodejs-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [PHP](../../../php-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [Python](../../../python-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [Ruby](../../../ruby-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [Rust](../../../rust-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)| [Scala](../../../scala-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization)