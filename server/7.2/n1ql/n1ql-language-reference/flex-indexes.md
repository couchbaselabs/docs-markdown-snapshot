---
title: Flex Indexes
description: The Flex Index feature enables you run a SQL++ query as a full-text
  search query, using a full-text index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/flex-indexes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:n1ql:n1ql-language-reference/flex-indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/flex-indexes.html)

# Flex Indexes

> The Flex Index feature enables you run a SQL++ query as a full-text search query, using a full-text index. This means that you can write queries in SQL++ to leverage the Search service's keyword search capabilities. 

In Couchbase Server, a global secondary index (GSI) uses a B-tree structure for fast exact search, whereas full-text search (FTS) uses an inverted index to provide efficient term search. In Couchbase Server 6.5 and later, it is possible to perform a full-text search within a SQL++ query using [search functions](searchfun.md). However this requires you to write the full-text search using the FTS syntax.

Starting with Couchbase Server 6.6, the _Flex Index_ feature provides the ability for a SQL++ query to leverage either a global secondary index or full-text index transparently with standard SQL++ syntax, simplifying the application development process.

The full-text index must be defined in a certain way to be usable by a SQL++ query; similarly, the SQL++ query must have certain characteristics to be able to use the full-text index. If these requirements are met, the query is transformed into an FTS query, and run against the full-text index.

Using a Flex Index query may offer advantages in the following situations:

* When the search conditions are not predetermined.
* When the search predicate involves a large number of fields combined using AND or OR.
* When the search predicate involves multiple arrays.
* When an application requires a full-text search combined with SQL++ aggregation or joins.

For a general introduction to creating full-text indexes, refer to [Creating Indexes](../../fts/fts-creating-indexes.md).

## [](#overview)Overview

To understand how a SQL++ query can make use of a full-text index, it's important to understand the differences between the semantics of SQL++ queries and full-text indexes, and the restrictions that arise from these differences.

### [](#semantic-differences)Semantic Differences

Full-text indexes have different semantics to SQL++ queries. Some of the main differences are described here.

* SQL++ uses escaped path names, whereas full-text indexes flatten the field names.
* SQL++ uses array subscripts to identify array objects, for example `f1.arr1[0].b`; whereas full-text indexes ignore subscripts, for example `f1.arr1.b`. This means full-text indexes cannot uniquely identify the path.
* In SQL++, data can be compared across data types. This is not possible with a full-text index.
* SQL++ handles MISSING fields, whereas these are not handled by a full-text index.

### [](#restrictions)Restrictions

Because of the semantic differences described above, there are several restrictions to the way a Flex Index query can use a full-text index.

* A Flex Index query cannot use a full-text index as a [covering index](covering-indexes.md).
* A Flex Index query cannot use a full-text index with a query on fields whose names contain special characters.
* A Flex Index query may include LIMIT and OFFSET clauses, but they cannot be [pushed down to the full-text index](../../learn/services-and-indexes/indexes/index%5Fpushdowns.md).
* A Flex Index query may include Aggregate functions and Window functions, but they cannot be [pushed down to the full-text index](../../learn/services-and-indexes/indexes/index%5Fpushdowns.md).

Flex Index queries only make use of full-text indexes to find the access path to the required data. The query engine then fetches the data from the data service.

Flex Index queries may use full-text indexes to do an intersect scan with other indexes. For further details, refer to [Usage](#usage) below.

### [](#index-availability)Index Availability

Full-text indexes are online and searchable as soon as they are created. GSI indexes are online and searchable after they have been built. For further details, refer to [BUILD INDEX](build-index.md).

## [](#usage)Usage

Assuming that there is no search function in the query predicate, there are two ways to specify that you would like to use a full-text index with a SQL++ query:

* Use the `USING FTS` hint in the SQL++ query. For full details, refer to [USE Clause](hints.md#index-type).
* Set the `use_fts` request-level parameter to `true`. For full details, refer to [Settings and Parameters](../../settings/query-settings.md).

When using an index hint, you may specify preferred indexes by name, or simply specify the preferred index type — `FTS` or `GSI`. It is possible to specify mixed index types.

Example 1\. Use FTS, no index specified

```sqlpp
SELECT META(d).id
FROM default AS d
USE INDEX (USING FTS)
WHERE d.f1 = "xyz" AND d.f2 = 100;
```

In this case:

1. The query engine considers all available full-text indexes.
2. If any full-text index qualifies, the full-text index is used.
3. If none of the full-text indexes qualify, the query engine considers other available GSI and primary indexes, following existing rules.

Example 2\. Use FTS or GSI, no index specified

```sqlpp
SELECT META(d).id
FROM default AS d
USE INDEX (USING FTS, USING GSI)
WHERE d.f1 = "xyz" AND d.f2 = 100;
```

In this case:

1. If any GSI index covers the query, the covering index is used and all other indexes are ignored.
2. If the query is not covered, the query engine considers all available full-text indexes and GSI indexes.
3. If any full-text indexes qualify, the query engine does an intersect scan of all the qualified full-text indexes and GSI indexes.
4. If none of the full-text indexes qualify, the query engine considers other available GSI and primary indexes, following existing rules.

Example 3\. Prefer the specified FTS and GSI indexes

```sqlpp
SELECT META(d).id
FROM default AS d
USE INDEX (fix1 USING FTS, gix1 USING GSI)
WHERE d.f1 = "xyz" AND d.f2 = 100;
```

In this case:

1. If the specified GSI index covers the query, the covering index is used and all other indexes are ignored.
2. If the query is not covered, the query engine considers the specified full-text indexes and all available GSI indexes.
3. If the specified full-text index qualifies, the query engine does an intersect scan of the full-text index and all qualified GSI indexes.
4. If the specified full-text index does not qualify, the query engine considers other available GSI and primary indexes, following existing rules.

In all cases, if the query meets the requirements to use a full-text index, and a qualified full-text index is selected, the query is transformed into an FTS [simple query](#fts:fts-query-types.adoc#simple-queries) (_not_ a query string query), and the simple query is run against the qualified full-text index.

> [!IMPORTANT]
> If the query predicate contains a search function, none of this applies — instead, an index is selected for the query according to the method described on the [Search Functions](searchfun.md) page.

## [](#fts-requirements)Full-Text Index Requirements

In order to use a full-text index with a SQL++ query, the full-text index must meet certain requirements.

### [](#analyzer)Analyzer

The full-text index _must_ use the [keyword analyzer](../../fts/fts-index-analyzers.md#pre-constructed-analyzers).

To specify that a full-text index should use the keyword analyzer:

1. In the **Add Index**, **Edit Index**, or **Clone Index** screen, click the **Advanced** heading to display the Advanced settings panel.
2. Open the **Default Analyzer** pull-down menu and select `keyword`.  
![FTS Settings Advanced Panel with Default Analyzer set to keyword](../_images/flex-fts-keyword-analyzer.png)

### [](#type-mappings)Type Mappings

The full-text index _must_ use one of the following type mappings:

* The default type mapping
* A single custom type mapping
* Multiple custom type mappings

The full-text index may _not_ use the default type mapping along with one or more custom type mappings.

### [](#indexed-fields)Indexed Fields

If the full-text index uses the default type mapping, only child mappings and fields mapped under the default type mapping can be used in a query. In case of dynamic mapping or dynamic child mappings, any field within the mapping can be used within a query.

If the full-text index has multiple custom type mappings, all the fields that you want to query must be indexed within all the requested type mappings.

Child mappings and fields mapped under top level type mappings can all be used within a query, provided they are enabled.

When [creating a full-text definition in the Couchbase Web Console](../../fts/fts-creating-indexes.md#inserting-a-child-field), the child fields listed by field name or by **searchable as** may be used within a SQL++ query.

> [!NOTE]
> The type field in a custom type mapped index is _not_ searchable.

Example 4\. Child fields that may be used in a query

A full-text index definition contains the following child fields:

```json
{
  "reviews": {
    "enabled": true,
    "dynamic": false,
    "properties": {
      "review": {
        "enabled": true,
        "dynamic": false,
        "properties": {
          "author": {
            "enabled": true,
            "dynamic": false,
            "fields": [{
                "name": "author", (1)
                "type": "text",
                "index": true,
                "analyzer": "keyword"
              }]
          }
        }
      }
    }
  },
  "id": {
    "enabled": true,
    "dynamic": false,
    "fields": [{
        "name": "id", (2)
        "type": "number",
        "index": true
      }]
  }
}
```

A query may search the following fields with this full-text index:

| **1** | The reviews.review.author field |
| ----- | ------------------------------- |
| **2** | The id field                    |

## [](#query-requirements)Query Requirements

In order to use a full-text index with a SQL++ query, the query must also meet certain requirements.

### [](#conditional-expression)Conditional Expression for Custom Type Mappings

If the full-text index has a single custom type mapping, the query predicate _must_ contain an expression matching the type, independent of the rest of the predicate.

Example 5\. Conditional expression for a custom type mapping with a simple predicate

A full-text index definition contains the following custom type mapping:

```json
"doc_config.mode": "type_field",
"doc_config.type_field": "type"
```

The following query can be used with this full-text index:

```sqlpp
SELECT meta().id
FROM `keyspace` USE INDEX (USING FTS)
WHERE type = "hotel" (1)
AND country = "US";
```

| **1** | Conditional expression matching the type mapping |
| ----- | ------------------------------------------------ |

If you have several expressions within the WHERE clause, the query engine needs to be able to resolve the conditional expression without any ambiguity, to avoid the possibility of false negatives.

Example 6\. Conditional expression for a custom type mapping with a complex predicate

The following query is ambiguous, and cannot be used with the full-text index defined in [Example 5](#ex-conditional-1):

```sqlpp
SELECT meta().id
FROM `keyspace` USE INDEX (USING FTS)
WHERE type = "hotel" AND country = "US" OR country = "CAN";
```

With brackets setting the priority of the AND and OR operators, the following queries are unambiguous, and can be used with the full-text index defined in [Example 5](#ex-conditional-1):

```sqlpp
SELECT meta().id
FROM `keyspace` USE INDEX (USING FTS)
WHERE type = "hotel" AND (country = "US" OR country = "CAN");
```

```sqlpp
SELECT meta().id
FROM default USE INDEX (USING FTS)
WHERE type = "hotel"
AND (
    country = "US" OR country = "CAN"
    AND id >= 0 AND id <= 10
    OR id >= 20 AND id <= 30
);
```

```sqlpp
SELECT meta().id
FROM default USE INDEX (USING FTS)
WHERE type = "hotel"
AND (country = "US" OR country = "CAN")
AND (id >= 0 AND id <= 10 OR id >= 20 AND id <= 30);
```

Similarly, if the full-text index contains multiple custom type mappings, the query engine needs to be able to resolve the conditional expression without any ambiguity, to avoid the possibility of false negatives.

Example 7\. Conditional expression for multiple custom type mappings

The following predicates can be used with a full-text index with multiple custom type mappings:

```sqlpp
WHERE type = "xyz"
WHERE (type = "xyz" OR type = "abc")
```

The following predicate cannot be used with a full-text index with multiple custom type mappings:

```sqlpp
WHERE type = "xyz" OR type = "abc"
```

### [](#n1ql-predicates)SQL++ Predicates

SQL++ predicates can be used with a Flex Index query, as long as they meet certain requirements, as detailed below.

#### [](#equality)Equality Expressions

You can use an equality expression with a full-text index, as long as the field is either explicitly indexed, or if the indexing is dynamic within the keyword analyzer.

Example 8\. Equality expressions with a dynamic keyword index

The following predicates can be used with a dynamic keyword index:

```sqlpp
WHERE a = "12"
WHERE b = true
WHERE c = 13
```

Example 9\. Equality expressions with explicitly indexed fields

A full-text index has the following explicitly indexed fields: `a` (text), `b` (boolean), `c` (numeric).

The following predicates can be used with this full-text index:

```sqlpp
WHERE a = "12"
WHERE b = true
```

The following predicates cannot be used with this full-text index:

```sqlpp
WHERE c = "13" (1)
WHERE d = "N/A" (2)
```

| **1** | c is indexed as numeric |
| ----- | ----------------------- |
| **2** | d is not indexed        |

The left-hand side of an equality expression must be a field name or a fully-qualified path. It may not be an expression. Conversely, the right-hand side of an equality expression may not depend on the keyspace.

Example 10\. Equality expression with field name

The following predicate can be used with a full-text index:

```sqlpp
WHERE state = LOWER("CALIFORNIA")
```

The following predicate cannot be used with a full-text index:

```sqlpp
WHERE LOWER(state) = "california" (1)
```

| **1** | Left-hand side is an expression |
| ----- | ------------------------------- |

#### [](#and)AND Expressions

You can use an `AND` expression with a full-text index. Partial sargability is supported: this means that one or both of the requested child expressions must be indexed for the query to use a full-text index. If there's a possibility of false positives, the query engine filters the results using KV fetches.

Example 11\. AND expressions

In a full-text index, the fields `a` and `b` are indexed.

The following expressions can be used with this full-text index:

```sqlpp
WHERE a = "12" AND b = "34" (1)
WHERE a = "12" AND d = "56" (2)
```

| **1** | Searches for a and b using the full-text index                                      |
| ----- | ----------------------------------------------------------------------------------- |
| **2** | Searches for a using the full-text index, and uses KV fetch to filter results for d |

The following expressions cannot be used with this full-text index:

```sqlpp
WHERE d = "56" AND e = "78" (1)
```

| **1** | Neither d nor e are indexed |
| ----- | --------------------------- |

#### [](#or)OR Expressions

You can use an `OR` expression with a full-text index. Partial sargability is not supported: all the requested child expressions must be indexed. This is to avoid false negatives.

Example 12\. OR expressions

In a full-text index, the fields `a` and `b` are indexed.

The following expressions can be used with this full-text index:

```sqlpp
WHERE a = "12" OR b = "34" (1)
WHERE a = "12" OR a = "98" (2)
```

| **1** | Searches for a and b using the full-text index |
| ----- | ---------------------------------------------- |
| **2** | Searches for a using the full-text index       |

The following expressions cannot be used with this full-text index:

```sqlpp
WHERE a = "12" OR d = "56" (1)
```

| **1** | d is not indexed (false negatives) |
| ----- | ---------------------------------- |

#### [](#compound-expressions)Compound Expressions

You can use compound expressions with a full-text index, as long as they respect the rules of [AND Expressions](#and) and [OR Expressions](#or) expressions described above, and do not return false negatives.

Example 13\. Compound expressions

A full-text index definition has a type mapping `X` with 2 child fields — `name` (text), `age` (numeric).

The following predicate can be used with this full-text index:

```sqlpp
WHERE type = "X" AND name = "abc" AND age = 10 (1)
```

| **1** | No chance of false negatives, all fields are sargable |
| ----- | ----------------------------------------------------- |

The following predicates cannot be used with this full-text index:

```sqlpp
WHERE type = "X" OR name = "abc" AND age = 10 (1)
WHERE type = "X" AND name = "abc" OR age = 10 (2)
```

| **1** | This is treated as an OR expression: (type = "X") OR (name = "abc" AND age = 10) |
| ----- | -------------------------------------------------------------------------------- |
| **2** | This is treated as an OR expression: (type = "X" AND name = "abc") OR (age = 10) |

AND takes precedence over OR, so these predicates are treated as OR expressions. Both child expressions of an OR expression must be indexed. Therefore these predicates cannot be used with a full-text index.

However, the following predicate can be used with this full-text index:

```sqlpp
WHERE type = "X" AND (name = "abc" OR age = 10) (1)
```

| **1** | Brackets alter the order of precedence so there is no chance of false negatives |
| ----- | ------------------------------------------------------------------------------- |

#### [](#ranges)Range Expressions

You can use range expressions with a full-text index, as long as the range expressions meet the following criteria:

1. Ranges must be deterministic: that is, they should have a clear start and finish.
2. Range boundaries must be of the same data type.
3. The maximum range boundary expression must always come after the minimum range boundary expression.
4. If there are several range expressions, or there is a mixture of range expressions and other expressions, the range expressions need to be contiguous.

Example 14\. Range expressions

The following range expressions can be used with a full-text index:

```sqlpp
WHERE a >= 10 AND a <= 20
WHERE b >= "hot" AND b <= "hotel"
WHERE c >= "2020-03-01" AND c <= "2020-04-01" (1)

WHERE type = "xyz" AND a >= 10 AND a <= 20
WHERE a >= 10 AND a <= 20 AND type = "xyz"
WHERE type = "xyz" AND (a >= 10 AND a <= 20) (2)
```

| **1** | Ranges are deterministic, range boundaries are of similar type, and maximum range boundary comes after minimum range boundary |
| ----- | ----------------------------------------------------------------------------------------------------------------------------- |
| **2** | Range expressions are contiguous                                                                                              |

The following range expressions cannot be used with a full-text index:

```sqlpp
WHERE a >= 10
WHERE b < "hotel"
WHERE c > "2020-03-01"
WHERE a >= 10 OR a <= 20 (1)

WHERE a <= 20 AND a >= 10
WHERE a >= 20 AND a <= 10 (2)

WHERE a >= 10 AND a <= "hot" (3)

WHERE a >= 10 AND type = "xyz" AND a <= 20 (4)
```

| **1** | Ranges are open-ended (non-deterministic)                  |
| ----- | ---------------------------------------------------------- |
| **2** | Maximum range boundary comes before minimum range boundary |
| **3** | Range boundaries are of different data types               |
| **4** | Range expression is not contiguous                         |

#### [](#isstring-and-issnumber)ISSTRING() and ISNUMBER()

You can use the [ISSTRING()](typefun.md#isstring) and [ISNUMBER()](typefun.md#isnumber) functions as a workaround to support open-ended ranges with a full-text index.

* The query engine translates `ISSTRING(x)` to a range establishing the data type of the object as a string, i.e. greater than or equal to an empty string, and less than an empty array: `"" <= x AND x < []`.
* The query engine translates `ISNUMBER(y)` to a range establishing the data type of the object as numeric, i.e. greater than the boolean value `true`, and less than an empty string: `true < y AND y < ""`.

Refer to [Collation](datatypes.md#collation) for more information.

Example 15\. Workarounds for open-ended ranges

The following open-ended ranges can be used with a full-text index:

```sqlpp
WHERE ISSTRING(name) AND name >= "abhi" (1)
WHERE ISNUMBER(age) AND age > 30 (2)
```

| **1** | An open-ended range specifying any string later than "abhi". |
| ----- | ------------------------------------------------------------ |
| **2** | An open-ended range specifying any number greater than 30.   |

#### [](#like)LIKE Expressions

You can use a `LIKE` expression with a full-text index, as long as the `LIKE` expression contains a simple string, or a string followed by the `%` wildcard.

If the `LIKE` expression contains a simple string, it must respect the rules outlined in the [Equality Expressions](#equality) section above. A string followed by the `%` wildcard, such as `a LIKE bc%`, will be treated as a range expression. Other `LIKE` expressions cannot be used with a full-text index.

Example 16\. LIKE expressions

The following predicates may be used with a full-text index:

```sqlpp
WHERE a LIKE "hotel" (1)
WHERE a LIKE "hote%" (2)
```

| **1** | The query engine treats this expression as the equality expression a = "hotel"   |
| ----- | -------------------------------------------------------------------------------- |
| **2** | The query engine treats this expression as the range a >= "hote" AND a <= "hotf" |

#### [](#between)BETWEEN Expressions

You can use a `BETWEEN` expression with a full-text index. The range specified by the `BETWEEN` expression must respect the rules outlined in the [Range Expressions](#ranges) section above. `BETWEEN` expressions that mix data type boundaries cannot be used with a full-text index.

Example 17\. BETWEEN expressions

The following predicate may be used with a full-text index:

```sqlpp
WHERE a BETWEEN 10 AND 20 (1)
```

| **1** | The query engine treats this expression as the range a >= 10 AND a <= 20 |
| ----- | ------------------------------------------------------------------------ |

#### [](#any-in-satisfies)ANY …​ IN …​ SATISFIES Expressions

You can use an `ANY` …​ `IN` …​ `SATISFIES` expression with a full-text index. The `ANY` …​ `IN` …​ `SATISFIES` expression must operate over an array, which may be an array of objects or any supported data types.

Example 18\. ANY …​ IN …​ SATISFIES expressions

A full-text index definition contains the following type mapping over documents of type `"hotel"`.

```json
{
  "hotel": {
    "default_analyzer": "keyword",
    "enabled": true,
    "properties": {
      "reviews": {
        "enabled": true,
        "properties": {
          "ratings": {
            "enabled": true,
            "properties": {
              "Cleanliness": {
                "enabled": true,
                "fields": [
                  {
                    "index": true,
                    "name": "Cleanliness",
                    "type": "number"
                  }
                ]
              },
              "Overall": {
                "enabled": true,
                "fields": [
                  {
                    "index": true,
                    "name": "Overall",
                    "type": "number"
                  }
                ]
              }
            }
          },
          "author": {
            "enabled": true,
            "fields": [
              {
                "index": true,
                "name": "author",
                "type": "text"
              }
            ]
          }
        }
      },
      "public_likes": {
        "enabled": true,
        "fields": [
          {
            "index": true,
            "name": "public_likes",
            "type": "text"
          }
        ]
      }
    }
  }
}
```

The following predicates may be used with this full-text index:

WHERE type = "hotel" AND ANY r in reviews SATISFIES r.author = "xyz" END

WHERE type = "hotel" AND ANY r in reviews SATISFIES r.ratings.Cleanliness = 5 OR r.ratings.Overall = 4 END

WHERE type = "hotel" AND ANY r in reviews SATISFIES r.ratings.Cleanliness = 5 OR r.ratings.Overall = 4 END AND ANY p in public_likes SATISFIES p LIKE "xyz" END

#### [](#every-in-satisfies)EVERY …​ IN …​ SATISFIES Expressions

You can use an `EVERY` …​ `IN` …​ `SATISFIES` expression with a full-text index. The `EVERY` …​ `IN` …​ `SATISFIES` expression must operate over an array, which may be an array of objects or any supported data types.

Example 19\. EVERY …​ IN …​ SATISFIES expressions

The following predicate may be used with the full-text index defined in [Example 18](#ex-any-in-satisfies):

WHERE EVERY r IN reviews SATISFIES r.ratings.Cleanliness = 5 END

#### [](#any-and-every-in-satisfies)ANY AND EVERY …​ IN …​ SATISFIES Expressions

You can use an `ANY AND EVERY` …​ `IN` …​ `SATISFIES` expression with a full-text index. The `ANY AND EVERY` …​ `IN` …​ `SATISFIES` expression must operate over an array, which may be an array of objects or any supported data types.

Example 20\. ANY AND EVERY …​ IN …​ SATISFIES expressions

The following predicate may be used with the full-text index defined in [Example 18](#ex-any-in-satisfies):

WHERE ANY AND EVERY r IN reviews SATISFIES r.ratings.Cleanliness = 5 END

#### [](#not)NOT Expressions

You cannot use a complex `NOT` expression with a full-text index.

### [](#joins)JOINs

JOINs may be used with a full-text index, as long as the JOIN predicate meets the requirements to be used with a full-text index. Refer to [SQL++ Predicates](#n1ql-predicates) above.

### [](#pagination)ORDER, LIMIT, and OFFSET

The LIMIT, OFFSET, and ORDER clauses can be used with a full-text index when the index uses the default type mapping or a single custom type mapping.