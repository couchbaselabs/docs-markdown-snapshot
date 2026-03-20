---
title: Data Types
description: This topic describes the data types that SQL++ for Enterprise
  Analytics operates on.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/10_data_type.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:sqlpp:10_data_type.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/10_data_type.html)

# Data Types

> This topic describes the data types that SQL++ for Enterprise Analytics operates on. 

An instance of the data model can be one of the following:

* **Primitive type**: `BOOLEAN`, `STRING`, `BIGINT`, or `DOUBLE`
* **Special type**: `NULL` or `MISSING`
* **Composite type**: `OBJECT`, `ARRAY`, or `MULTISET`

The type names are case-insensitive. That is, you can use `BIGINT` or `bigint`.

## [](#PrimitiveTypes)Primitive Types

### [](#PrimitiveTypesBoolean)Boolean

The `Boolean` data type has only two values: `true` and `false`.

Examples

true
false

An expression that compares two values, such as `weight > limit`, might return a `Boolean` value or it might return one of the special values `null` or `missing`. For details, see [Comparison Operators](2%5Fexpr.md#Comparison%5Foperators).

### [](#PrimitiveTypesString)String

A `string` represents a sequence of characters. The total length of the sequence can be up to 2,147,483,648.

Syntactically, a literal string is enclosed in single or double quotes.

Examples

"This is a string."
'Have you read "War and Peace"?'
"I don't think so."

For more information about string literals, see [Literals](2%5Fexpr.md#Literals).

### [](#PrimitiveTypesInt)Bigint

A `bigint` is a 64-bit integer. The range of `bigint` is from -9223372036854775808 to 9223372036854775807.

Examples

45
-27900

In general, arithmetic operations on two `bigint` values return a `bigint` result. However, SQL++ for Enterprise Analytics provides two division operators:

* `5 / 2` returns `2.5`, a value of type `double`.
* `5 div 2` returns `2`, a value of type `bigint`, by truncating the result.

See [Arithmetic Operators](2%5Fexpr.md#Arithmetic%5Foperators).

### [](#PrimitiveTypesDouble)Double (double precision)

The `double` type represents approximate numeric data values using 8 bytes. The range of a `double` value is from (2^(-1022)) to (2-2(-52))·2(1023) for both positive and negative numbers. Expressions that compute values outside these ranges return `INF` or `-INF`. SQL++ for Enterprise Analytics also supports the special value `NaN` (not a number).

If a numeric literal contains a decimal point or an exponent, SQL++ for Enterprise Analytics treats it as a `double`.

Examples

45.
-2.79E4
2.79E-4

Enterprise Analytics parses all numbers that are not integers in incoming JSON documents as `double` values.

## [](#temporal-data-and-primitive-types)Temporal Data and Primitive Types

Applications often make use of temporal data (dates, times, and timestamps). Since JSON does not provide data types for temporal data, SQL++ for Enterprise Analytics uses the `string` and `bigint` types for this purpose. SQL++ provides a number of builtin functions, called temporal functions, that operate on `string` or `bigint` values, interpreting them as dates or times. For a list of these functions, see [Temporal Functions](8%5Fbuiltin%5Ftemp.md).

### [](#using-bigint-for-temporal-data)Using `bigint` for Temporal Data

Some of the temporal functions take `bigint` values and interpret them as representing a number of milliseconds since the beginning of the Unix Epoch at 00:00:00 UTC on January 1, 1970\. Two of these temporal functions, and some examples of their use, follow.

* `now_millis( )` returns the current point in time as a `bigint` representing Unix Epoch milliseconds.
* `date_diff_millis(t1, t2, unit)` returns the difference between two points in time--`t1` and `t2`\--in terms of the designated units: years, months, weeks, days, hours, seconds, or milliseconds.

Examples

now_millis( ) returns 1655230396621 at the start of an experiment.

now_millis( ) returns 1655231924715 at the end of the experiment.

date_diff_millis(1655231924715, 1655230396621, "minute") returns 25,
    showing that the experiment lasted for 25 minutes.

date_diff_millis(1655231924715, 1655230396621, "second") returns 1528,
    providing a finer measurement: the experiment lasted for 1528 seconds.

### [](#using-string-for-temporal-data)Using `string` for Temporal Data

A string in ISO 8601 format can represent a date, time, or timestamp. The following example shows 30.55 seconds after 15:10—​3:10pm—​on June 14, 2022 in a timezone that’s eight hours behind Coordinated Universal Time (UTC) in ISO format.

"2022-06-14T15:10:30.55-8:00"

When using a string to represent temporal data, you can omit parts of the ISO format. For example:

* `"2022-06-14"` represents the day June 14, 2022.
* `"15:10:30"` represents a time 30 seconds past 15:10 (3:10pm)

In general, you can compare two temporal values only if they have the same components, for example, two dates or two times. Violations of this rule usually give `null` results.

The following examples, which use the `date_diff_str` function to compare two temporal values and return the difference in a designated unit, demonstrate these rules.

Examples

date_diff_str("2022-06-22", "2022-06-15", "day") returns 7

date_diff_str("09:20:00", "08:00:00", "hour") returns 1

date_diff_str("09:20:00", "08:00:00", "minute") returns 80

date_diff_str("2022-06-22", "10:00:00", "hour") returns null

For more information about string formats for temporal data, see [Date String Formats](../../../server/current/n1ql/n1ql-language-reference/datefun.md#date-string).

## [](#IncompleteInformationTypes)Incomplete Information Types

### [](#IncompleteInformationTypesNull)Null

`NULL` is a special value that indicates that a value does not exist. It often represents an unknown value. For example, if a user doesn’t know what to enter for a field, they leave it blank or let it be `null`.

Example

{ "field": null };

The expected result is:

{ "field": null }

### [](#IncompleteInformationTypesMissing)Missing

`MISSING` indicates that a name-value pair is not present in an object. If you access a missing name-value pair, the query returns an empty result value.

As neither the data model nor the system enforces homogeneity for datasets or collections, items in a dataset or collection can be of heterogeneous types. A field that is present in one object might be `missing` in another.

Example

{ "field": missing };

Results in:

{  }

Since a field with value `missing` means the field is also absent, the result is an empty object.

> [!NOTE]
> When a `missing` value needs to be serialized in a query result, `missing` value is serialized as `null` (for example, a `missing` value in an array).

## [](#CompositeTypes)Composite Types

### [](#CompositeTypesObject)Object

An `object`\--that is, a JSON object—​contains a set of ﬁelds. Each ﬁeld is described by its name.

Syntactically, curly braces `{…​}` surround object constructors.

Example

  { "name": "Joe Blow", "rank": "Sergeant", "serialno": 1234567 }
  { "rank": "Private", "serialno": 9876543 }
  { "name": "Sally Forth", "rank": "Major", "serialno": 2345678, "gender": "F" }

### [](#CompositeTypesArray)Array

An `array` is a container that holds a fixed number of values. An array is an ordered collection of items.

Syntactically, brackets `[…​]` denote array constructors.

Example

["alice", 123, "bob", null]

> [!NOTE]
> An array can appear in the incoming JSON, and a query can construct an array. Each SELECT statement with an ORDER BY clause returns an array.

### [](#CompositeTypesMultiset)Multiset

A `multiset` is an unordered collection of items. A multiset allows multiple instances of its elements.

> [!NOTE]
> A multiset cannot appear in the incoming JSON. The query results convert a multiset into a JSON array with an undefined order of elements. The order of the items in the result might change from one query execution to another. Each SELECT statement without an ORDER BY clause returns a multiset.