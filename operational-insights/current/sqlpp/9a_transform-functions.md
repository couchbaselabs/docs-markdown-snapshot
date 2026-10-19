---
title: Transform Functions
description: Operational Insights supports lightweight transformations on
  incoming data destined for remote collections, using {sqlpp}
  <code>TRANSFORM</code> User-Defined Functions (UDFs).
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/9a_transform-functions.adoc
  xref: xref:enterprise-analytics:sqlpp:9a_transform-functions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/9a_transform-functions.html)

# Transform Functions

> Operational Insights supports lightweight transformations on incoming data destined for remote collections, using {sqlpp} `TRANSFORM` User-Defined Functions (UDFs). You can use `TRANSFORM` UDFs to declaratively transform data objects before they're stored in remote collections. The supported common transformations through UDFs include: 

* Field operations and record filtering, such as:

  * Renaming fields.
  * Adding fields with static values.
  * Excluding specific fields.
  * Filtering records.
  * Flattening nested structures, using single-row nested aggregation.
* Value conversions, such as:

  * Type conversions including string to integer and timestamp formatting.
  * String manipulations including concatenation, lower/upper case, and substring.
  * Arithmetic transformations and creation of derived fields.

## [](#create-transform-function)Create TRANSFORM FUNCTION

A `TRANSFORM FUNCTION` is a specialized type of user-defined function (UDF) that's created using the `CREATE TRANSFORM FUNCTION` statement. Its purpose is to perform an automatic, on-the-fly transformation of incoming data.

For an UDF to be a valid `TRANSFORM FUNCTION`, you must have the following conditions:

* Only has a single argument: this argument is the incoming document, received from the data service/Kafka, which is passed to the function.
* Returns at most one value: the function should return at most one value for each input document. If for an input document, the function does not return any value, that document is skipped. In case the function returns a value, the value should be a valid document. The returned/transformed document is stored.
* Does not touch any collection/view: the function works only with the input document.

See the following examples:

Example

```sqlpp
CREATE TRANSFORM FUNCTION project_fields(input) {
	SELECT VALUE doc FROM (
	SELECT d.name, d.address FROM [input] d
) as doc
}
```

This function extracts only the `name` and `address` fields from each incoming document. The transformed document contains only these two fields.

Example

```sqlpp
CREATE OR REPLACE TRANSFORM FUNCTION CustomerTransform (cust)
{
SELECT VALUE doc FROM (
SELECT c.*,
         (c.address.street || ', ' || c.address.city || ', ' || c.address.zipcode) AS location
  FROM [cust] AS c ) as doc
};
```

This function transforms the customers mailing address into a single-line string. The transformed document contains all the original fields, plus a new field called `location`.

## [](#applying-transform-function-to-collections)Applying TRANSFORM FUNCTION to Collections

A `TRANSFORM FUNCTION` is applied to a remote collection to automatically process data as it is ingested from an external source. You do this by adding the `APPLY FUNCTION` clause to the `CREATE COLLECTION` statement.

See the following example:

Example

```sqlpp
CREATE COLLECTION remote_hotel ON hotel AT my_remote_link APPLY FUNCTION project_fields;
```

> [!NOTE]
> You cannot modify or drop a `TRANSFORM FUNCTION` while it's applied to any collection.

## [](#see-also)See Also

* [User-Defined Functions](9%5Fudf.md)
* [CREATE a Remote Collection](5%5Fddl%5Fremote.md)
* [Transform Data](../sources/transform-data.md)