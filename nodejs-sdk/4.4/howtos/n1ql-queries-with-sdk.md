---
title: Query
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.4/modules/howtos/pages/n1ql-queries-with-sdk.adoc
  xref: xref:4.4@nodejs-sdk:howtos:n1ql-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.4/howtos/n1ql-queries-with-sdk.html)

# Query

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. Querying can solve typical programming tasks such as finding a user profile by email address, Facebook login, or user ID. 

## [](#getting-started)Getting Started

Our query service uses SQL++ (formerly N1QL), which will be fairly familiar to anyone who's used any dialect of SQL. [Additional resources](#additional-resources) for learning about SQL++ are listed at the bottom of the page.

Before you get started you may wish to check out the [SQL++ intro page](../../../server/7.6/n1ql/n1ql-language-reference/index.md), or just dive in with a query against our travel-sample data set. Also, building indexes is covered in more detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building).

After familiarizing yourself with the basics on how the SQL++ query language works and how to query it from the UI you can use it from the Node.js SDK.

## [](#queries-placeholders)Queries & Placeholders

Placeholders allow you to specify variable constraints for an otherwise constant query. There are two variants of placeholders: positional and named parameters. Positional parameters use an ordinal placeholder for substitution and named parameters use variables. A named or positional parameter is a placeholder for a value in the WHERE, LIMIT, or OFFSET clause of a query. Note that both parameters and options are optional.

Positional parameter example:

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

Named parameter example:

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

## [](#handling-results)Handling Results

Most queries return more than one result, and you want to iterate over the results:

```javascript
async function queryResults() {
  const query = `
  SELECT airportname, city FROM \`travel-sample\`.inventory.airport
  WHERE tz LIKE '%Los_Angeles'
    AND airportname LIKE '%Intl';
  `
  try {
    let results = await cluster.query(query);
    results.rows.forEach((row) => {
      console.log('Query row: ', row)
    })
    return results
  } catch (error) {
    console.error('Query failed: ', error)
  }
}
```

## [](#cas-and-sql)CAS and SQL++

If you are performing an operation with SQL++ that requires CAS to be used, in combination with using CAS from regular KV operations for example, then you need to be aware of the [CAS type](concurrent-document-mutations.md#cas-value-format). CAS is stored as a 64-bit integer, which cannot be represented safely in javaScript — thus you must convert to a string:

```javascript
  const GET_IDS = `
    SELECT  META().id AS recordId
          , TOSTRING(META().cas) AS cas
          , id
    FROM cdb
    WHERE type = 'profile'
    LIMIT $count
    `;
```

## [](#querying-the-default-scope)Querying the default Scope

When working with earlier versions (before the Developer Preview in 6.5), or with other server versions, the `defaultcollection` is used from the SDK, by simply addressing the Bucket itself.

```javascript
async function queryNamed() {
  const query = `
    SELECT airportname, city FROM \`travel-sample\` 
    WHERE type=$TYPE 
      AND city=$CITY;
  `
  const options = { parameters: { TYPE: 'airport', CITY: 'Reno' } }

  try {
    let result = await cluster.query(query, options)
    console.log("Result:", result)
    return result
  } catch (error) {
    console.error('Query failed: ', error)
  }
}
```

## [](#additional-resources)Additional Resources

> [!NOTE]
> SQL++ is not the only query option in Couchbase. Be sure to check that your use case fits your selection of query service.

The [SQL++ Language Reference](../../../server/7.6/n1ql/n1ql-language-reference/index.md) introduces up a complete guide to the SQL++ language, including all of the latest additions.

The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.