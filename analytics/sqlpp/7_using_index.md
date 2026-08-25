---
title: Indexes
description: You use indexes to accelerate queries on remote and standalone collections.
pubDate: 2026-08-25T04:30:40.250Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/7_using_index.adoc
  xref: xref:analytics:sqlpp:7_using_index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sqlpp/7_using_index.html)

# Indexes

> You use indexes to accelerate queries on remote and standalone collections. 

Indexes can accelerate queries if you apply them properly. The sections in this topic describe scenarios in which you can use indexes to accelerate query processing.

> [!NOTE]
> You cannot index external collections. To make your queries on external data stores more efficient, when you create the collection you can choose to specify a location path that's as specific as possible. See [Design a Location Path](../sources/dynamic-prefixes.md).

## [](#Indexes)Indexes

An index is a materialized lookup structure for data in a collection. You can create more than one index on the same collection. Each index name must be unique within a collection. Creating an index fails if there is an existing index with the same name in the target collection and `IF NOT EXISTS` is not specified.

For each JSON document ingested into a collection, the system computes the indexed key for each index.

In the case of a secondary index, the index key is computed by extracting the target field values from the document based on the specified field path.

After the system builds the indexed key, it's inserted into the secondary index. If the system cannot build the indexed key, there is no entry made in the index for this object.

Secondary indexes are automatically maintained by the system during data ingestion — that's when a corresponding remote link is connected and starts populating its collections. In addition, they're automatically rebalanced when their shadow collections are rebalanced, scaled out or scaled in.

To accommodate varying query predicates, secondary indexes can be configured on either a single field or across multiple fields. For example, to define a standard single-field index on the `name` attribute, use the following statement:

```SQL++
CREATE INDEX idx_name ON user(name);
```

To optimize queries targeting multiple fields simultaneously, construct a composite index using the following syntax:

```SQL++
CREATE INDEX idx_age_name ON user(age, name);
```

### [](#Selection%5Fqueries)Indexing for Selection Queries

The query optimizer chooses to use a secondary index for query execution if both of the following conditions are met:

* The query contains a conjunctive equality or range predicate over one or more fields, or a join predicate: see the [next section](#Join%5Fqueries). The conjunctive predicate has a form:  
QualifiedName Operator Literal ( AND field Operator Literal )+  
where `Operator` is `=`, `>`, `>=`, `<`, `<=`, or `BETWEEN`.
* An index exists with a key, such that the corresponding fields in the predicate form a prefix of that key. For example, suppose that there is an index on collection `foo` with key fields `c_s` and `c_d`.

```SQL++
 CREATE INDEX idx_s_d ON foo(c_s, c_d);
```

The following query uses the index because it has an equality predicate `=` on a field `c_s`, which is a prefix of the indexed key `c_s, c_d`:

```SQL++
 SELECT f.c_x as res
 FROM foo f
 WHERE f.c_s = 'world';
```

As shown in the following example, to prevent an available index from being used for a particular query predicate — for example, because the query matches a large number of objects — you can include a `skip-index` hint.

> [!TIP]
> The query optimizer automatically makes these decisions for you in most cases.

```SQL++
 SELECT f.c_x as res
 FROM foo f
 WHERE f.c_s /*+ skip-index */ = 'world';
```

If multiple indexes are eligible for query execution, there can be 2 cases:

* Two or more indexes are sharing the same prefix and the predicate is on that prefix. For example: `indexA` is on (c1, c2), `indexB` is on (c1, c3) and the predicate is on c1 (c1 = 100). In this case, the query optimizer picks one of the indexes.
* No indexes share the same prefix and the predicate refers to fields from each individual index. For example: `indexA` is on (c1) and `indexB` is on (c2), the predicate is on c1 and c2 (c1 = 100 and c2 = 200). In this case, both indexes are used to retrieve matched primary keys, and the key sets are intersected to filter retrieved primary keys further.

The following queries use the index `idx_age`:

// Index
CREATE INDEX idx_age ON user(age);

// Query
SELECT * FROM user WHERE age < "30";

// Result
{ "id": 5, "age": "10" }
{ "id": 6, "age": "20" }

// Query
SELECT * FROM user WHERE age < 30;

// Result
{ "id": 1, "age": 10 }
{ "id": 2, "age": 20 }

#### [](#covering%5Findexes)Covering Indexes

A covering index is an index that contains all the information required to satisfy a query, including both the fields used in filtering conditions and the fields returned in the result set. Since all necessary data is available within the index, the optimizer creates a query plan that only scans the index. This reduces I/O operations and can significantly improve query performance.

The optimizer can be configured to generate query plans that rely exclusively on index scans by using the `compiler.index.covering` directive. This directive is enabled by default, so the optimizer prefers covering index plans whenever possible. If `compiler.index.covering` is disabled, query execution plans access both the indexes and their underlying data records.

As a practical example, consider the `idx_name` index on the `user` collection created in the previous section. For the following query:

```SQL++
SELECT u.name
FROM user u
WHERE u.name = 'name1';
```

Because the requested `name` attribute is contained entirely within `idx_name`, the query optimizer leverages this secondary index to satisfy the request directly, bypassing access to the primary records altogether.

The query optimizer evaluates and prioritizes indexes based on their filtering efficiency and selectivity. Consequently, the sequence of columns defined in a composite index is critical. Consider the following query:

```SQL++
SELECT u.age
FROM user u
WHERE u.name = 'name1';
```

If both `idx_age_name` (defined on `age`, `name`) and `idx_name` (defined on `name`) are available, the optimizer selects `idx_name`. Although `idx_age_name` contains all required attributes, the optimizer prioritizes the index whose leading column aligns with the query predicate (`u.name`). For a composite index to be considered an optimal candidate for execution plans, the filtering criteria must be positioned as the leading fields.

### [](#Join%5Fqueries)Indexing for Join Queries

SQL++ for Capella Analytics supports joins from standard SQL in the following forms:

* Inner join:  
SELECT * FROM ds_outer, ds_inner WHERE <predicate>;  
SELECT * FROM ds_outer JOIN ds_inner ON <predicate>;  
SELECT * FROM ds_outer INNER JOIN ds_inner ON <predicate>;
* Left outer join:  
SELECT * FROM ds_outer LEFT JOIN ds_inner ON <predicate>;  
SELECT * FROM ds_outer LEFT OUTER JOIN ds_inner ON <predicate>;
* Right outer join:  
SELECT * FROM ds_outer RIGHT JOIN ds_inner ON <predicate>;  
SELECT * FROM ds_outer RIGHT OUTER JOIN ds_inner ON <predicate>;

`ds_outer` is the outer collection and `ds_inner` is the inner collection, in the order in which they appear in the FROM clause.

The join predicate is an equality or range predicate that refers to fields from both branches of the join, in the form of:

expr_outer OP expr_inner

Where:

* `OP` is `<`, `⇐`, `=`, `>=`, `>`, or `BETWEEN`
* `expr_inner` is a field from the inner collection
* `expr_outer` is a field from the outer collection

## [](#Array%5Findexes)Array Indexes

Capella Analytics also provides array indexes, which enable you to index values within an array, or fields within an object nested in an array. You can create an array index by providing a sequence of `UNNEST` and `SELECT` keywords to identify the field to index.

Array indexes accelerate a query that involves some array-valued field. This enables fast evaluation of predicates in queries involving arrays or arrays of nested objects. For brevity, all further mentions of array-valued fields are also applicable to multiset-valued fields.

In Capella Analytics, array indexes are **not** meant to serve as covering indexes. Instead, array indexes are meant only to accelerate queries involving multi-valued fields.

Array indexes and standard indexes also differ in how the query optimizer uses them. See [Array Index Parameter](appendix%5F2%5Fparameters.md#ArrayIndexFlag).

> [!NOTE]
> Array indexes do not support heterogeneous indexing. This limitation exists because array indexes cannot store `NULL` or `MISSING` values. When creating an array index, you have the option to exclude `NULL` and `MISSING` values. However, excluding these values means the index does not optimize queries that rely on the presence of `NULL` fields in the documents.

### [](#QuantificationQueries)Quantification Queries

A common use case for array indexes involves quantifying some or all elements within an array. Quantification queries have two variants: existential and universal.

* **Existential** queries ask if **any** element in some array satisfies a given predicate. Membership queries are a specific type of existential query, asking if any element in some array is equal to a particular value.
* **Universal** queries ask if **all** elements in some array satisfy a particular predicate. Empty arrays are not stored in an array index, meaning that you must also specify that the array is non-empty to tell Capella Analytics that it's possible to use an array index as a retrieval method for the given query.

The examples that follow suppose the existence of a collection named `products`, containing two fields: `productno`, an integer, and `categories`, an array of strings in the Commerce dataset. You can follow the instructions for the [Commerce example dataset](../intro/examples.md) to set up a standalone collection for this data.

```json
[
  { "productno": 347, "categories": ["Food"]},
  { "productno": 193, "categories": ["Drink"]},
  { "productno": 460, "categories": ["Food", "Frozen"]}
]
```

You can create an array index on the `categories` field of the `products` collection as follows.

```SQL++
 CREATE INDEX pCategoriesIdx
 ON products (UNNEST categories:STRING)
 EXCLUDE UNKNOWN KEY;
```

> [!NOTE]
> `EXCLUDE UNKNOWN KEY` is required for array indexes.

Suppose you want to find all products that have the category `"Food"`. The following membership query uses the `pCategoriesIdx` index.

```SQL++
 SELECT p
 FROM products p
 WHERE "Food" IN p.categories;
```

You can rewrite this query as an explicit existential quantification query with an equality predicate. This also uses the `pCategoriesIdx` index:

```SQL++
 SELECT p
 FROM products p
 WHERE SOME c IN p.categories SATISFIES c = "Food";
```

You can create an array index on the `qty` and `price` fields in the `items` array of the `orders` collection as follows.

```SQL++
 CREATE INDEX oItemsQtyPriceIdx
 ON orders (UNNEST items SELECT qty:BIGINT, price:DOUBLE)
 EXCLUDE UNKNOWN KEY;
```

Now suppose you want to find all orders that only have items with large quantities and low prices. The following universal quantification query uses the `oItemsQtyPriceIdx` index:

```SQL++
 SELECT o
 FROM orders o
 WHERE LEN(o.items) > 0 AND
       (EVERY i IN o.items SATISFIES i.qty > 100 AND i.price < 5.00);
```

Take note of the `LEN(o.items) > 0` conjunct. Array indexes cannot be used for queries with potentially empty arrays.

### [](#ExplicitUnnestQueries)Explicit Unnesting Queries

You can also use array indexes to accelerate queries that involve the explicit unnesting of array fields. You can express the same membership / existential example in the preceding section using an explicit `UNNEST` query. To maintain the same cardinality as the preceding query and undo the `UNNEST`, the query adds a `DISTINCT` clause. The `pCategoriesIdx` index is still used.

```SQL++
 SELECT DISTINCT p
 FROM products p, p.categories c
 WHERE c = "Food";
```

As another example, suppose that you want to find all orders that have **some** item with a large quantity. The following query uses the `oItemsQtyPriceIdx` index, using only the `qty` field.

```SQL++
 SELECT DISTINCT o
 FROM orders o, o.items i
 WHERE i.qty > 100 AND i.price > 0;
```

In this case, even though you do not want to filter the results by price, you must specify a dummy predicate on the `price` field so that the query optimizer can select the required index.

### [](#JoinQueries)Join Queries

Array indexes can also be used for index nested-loop joins if the field being joined is located within an array. You can create an array index on the `itemno` field in the `items` array of the `orders` collection as follows.

```SQL++
 CREATE INDEX oProductIDIdx
 ON orders (UNNEST items SELECT itemno:BIGINT)
 EXCLUDE UNKNOWN KEY;
```

Now suppose you want to find all products located in a specific order. You can accomplish this with the join query that follows. If an index is possible for the join, the optimizer uses it if it's the most cost-effective option. However, if you specify a join hint like `indexnl` as in the example that follows, Capella Analytics uses the index even if it's more expensive than a hash join.

```SQL++
 SELECT DISTINCT p
 FROM products p JOIN orders o
 ON SOME i IN o.items SATISFIES i.itemno /*+ indexnl */ = p.productno
     WHERE o.custid = "C41";
```

### [](#ComplexIndexingExamples)Arrays in Arrays

Array indexes are not just limited to arrays of depth 1\. You can generalize array indexes to arbitrary depth, as long as an object encapsulates each array. For example, suppose the `orders` collection includes the `qty` field in a double-nested `items` array.

```json
{
  "orderno": 2001,
  "items0": [
    {
      "items1": [
        {
          "qty": 100,
          // ...
        }
      ]
    }
  ]
}
```

The following statement indexes the `qty` field in a double-nested `items` array.

```SQL++
 CREATE INDEX oItemItemQtyIdx
 ON orders (UNNEST items0 UNNEST items1 SELECT qty:INT)
 EXCLUDE UNKNOWN KEY;
```

Similarly, suppose the `orders` collection includes the `qty` field in a triple-nested `items` array.

```json
{
  "orderno": 3001,
  "items0": [
    {
      "items1": [
        {
          "items2": [
            {
              "qty": 100,
              // ...
            }
          ]
        }
      ]
    }
  ]
}
```

The following statement indexes the `qty` field in a triple-nested `items` array.

```SQL++
 CREATE INDEX oItemItemItemQtyIdx
 ON orders (UNNEST items0 UNNEST items1 UNNEST items2 SELECT qty:BIGINT)
 EXCLUDE UNKNOWN KEY;
```

The queries that follow use the preceding indexes. The first query uses the `oItemItemQtyIdx` index through nested existential quantification. The second query uses the `oItemItemItemQtyIdx` index with three unnesting clauses.

```SQL++
SELECT o
FROM orders o
WHERE SOME o0 IN o.items0 SATISFIES (
    SOME o1 IN o0.items1 SATISFIES o1.qty = 100
);

SELECT DISTINCT o
FROM orders o, o.items0 o0, o0.items1 o1, o1.items2 o2
WHERE o2.qty = 100;
```