[View original HTML](/server/7.2/analytics/7_using_index.html)

Indexes can speed up Analytics queries if they are applied properly. The following sections describe scenarios in which indexes may be used to speed up query processing.

## [](#Standard%5Findexes)Standard Indexes

This section contains observations about standard (non-array) Analytics indexes.

|  | By default, standard indexes store NULL values. (This is to allow composite key secondary indexes to be used for prefix search.) However, when you create the index, you may specify that NULL and MISSING values should be excluded from the index. If this is the case, queries that select objects based on the existence of a NULL field will not be accelerated by the index. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#Selection%5Fqueries)Selection Queries

The query optimizer chooses to use a secondary index for query execution if both of the following conditions are met:

* The query contains a conjunctive equality or range predicate over one or more fields, or a join predicate — see [Join Queries](#Join%5Fqueries). The conjunctive predicate has a form:  
QualifiedName Operator Literal ( AND field Operator Literal )+  
where `Operator` is `=`, `>`, `>=`, `<`, `<=`, or `BETWEEN`;
* There is an index with a key, such that the corresponding fields in the predicate form a prefix of that key. For example, suppose that there is an index on collection `foo` with key fields `c_s` and `c_d`.  
CREATE INDEX idx_s_d ON foo(c_s:STRING, c_d:DOUBLE);

The following query uses the index because it has an equality predicate (`=`) on a field (`c_s`) that is a prefix of the indexed key (`c_s`, `c_d`):

SELECT f.c_x as res
FROM foo f
WHERE f.c_s = 'world';

If you would like an available index to not be used for a particular query predicate (e.g., because there will be many, many matching objects), a skip-index hint can be used:

SELECT f.c_x as res
FROM foo f
WHERE f.c_s /*+ skip-index */ = 'world';

If multiple indexes are eligible access paths, there can be two cases:

* Two or more indexes are sharing the same prefix and the predicate is on that prefix. For example: `indexA` is on (c1, c2), `indexB` is on (c1, c3) and the predicate is on c1 (c1 = 100). In this case, the query optimizer picks the first index in the order of their names, e.g., `indexA`.
* No indexes share the same prefix and the predicate refers to fields from each individual index. For example: `indexA` in on (c1) and `indexB` is on (c2), the predicate is on c1 and c2 (c1 = 100 and c2 = 200). In this case, both indexes will be used to retrieve matched primary keys and then the key sets will be intersected to further filter retrieved primary keys.

### [](#Join%5Fqueries)Join Queries

SQL++ for Analytics supports joins from standard SQL in the following forms:

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

`ds_outer` is the outer branch and `ds_inner` is the inner branch, in the order in which they appear in the FROM clause.

The query optimizer picks an index for join evaluation if the following conditions are met:

* The join predicate is an equality or range predicate that refers to fields from both branches of the join, in the form of:  
fn(expr_outer) /*+ indexnl */ op field_inner  
where `op` is `<`, `<=`, `=`, `>=`, `>`, or `BETWEEN`;
* `field_inner` is a field from the inner collection on which the index is defined;
* The index join hint, `/*+ indexnl */`, is provided for the join predicate;
* `fn()` is a function that returns the same data type as the type specified in the index for the `field_inner`. Usually, `fn()` is one of the following: to\_string(), to\_double(), or to\_bigint().

Note that the type of `expr_outer` is not known at compile time, therefore the index join cannot be selected if the join predicate is just `expr_outer /*+ indexnl */ op field_inner`.

For example, suppose there are two Analytics collections, foo1 and foo2, with an index on foo2:

CREATE index idx_f2 ON foo2(c_s2:string);

Then the following query would use this index for join evaluation:

SELECT f1.c_x1 as c1, f2.c_x2 as c2
FROM foo1 AS f1, foo2 AS f2
WHERE to_string(f1.c_s1)  /*+ indexnl */ = f2.c_s2

## [](#Array%5Findexes)Array Indexes

Array indexes are used in applications where you want to accelerate a query that involves some array-valued field. This enables fast evaluation of predicates in queries involving arrays or arrays of nested objects. For brevity, all further mentions of array-valued fields are also applicable to multiset-valued fields.

It should be noted that in Analytics, array indexes are _not_ meant to serve as covering indexes. Instead, array indexes are simply meant to accelerate queries involving multi-valued fields.

### [](#QuantificationQueries)Quantification Queries

A common use-case for array indexes involves quantifying some or all elements within an array. Quantification queries have two variants: existential and universal. Existential queries ask if _any_ element in some array satisfies a given predicate. Membership queries are a specific type of existential query, asking if any element in some array is equal to a particular value. Universal queries ask if _all_ elements in some array satisfy a particular predicate. Empty arrays are not stored in an array index, meaning that a user must additionally specify that the array is non-empty to tell Analytics that it is possible to use an array index as an access method for the given query.

The examples shown here are based on the Commerce data in [Appendix 4: Example Data](appendix%5F4%5Fexamples.md). In addition, the examples in this section suppose the existence of an Analytics collection named `products`, containing two fields: `productno` (an integer), and `categories` (an array of strings).

```json
[
  { "productno": 347, "categories": ["Food"]},
  { "productno": 193, "categories": ["Drink"]},
  { "productno": 460, "categories": ["Food", "Frozen"]},
  // ...
]
```

You can create an array index on the `categories` field of the `products` collection as follows.

CREATE INDEX pCategoriesIdx
ON products (UNNEST categories:STRING)
EXCLUDE UNKNOWN KEY;

Note that `EXCLUDE UNKNOWN KEY` is required for array indexes.

Suppose you want to find all products that have the category "Food". The following membership query will utilize the `pCategoriesIdx` index.

SELECT p
FROM products p
WHERE "Food" IN p.categories;

You can rewrite the query above as an explicit existential quantification query with an equality predicate. This will also utilize the `pCategoriesIdx` index.

SELECT p
FROM products p
WHERE SOME c IN p.categories SATISFIES c = "Food";

You can create an array index on the `qty` and `price` fields in the `items` array of the `orders` collection as follows.

CREATE INDEX oItemsQtyPriceIdx
ON orders (UNNEST items SELECT qty:BIGINT, price:DOUBLE)
EXCLUDE UNKNOWN KEY;

Now suppose you want to find all orders that only have items with large quantities and low prices. The following universal quantification query will utilize the `oItemsQtyPriceIdx` index.

SELECT o
FROM orders o
WHERE LEN(o.items) > 0 AND
      (EVERY i IN o.items SATISFIES i.qty > 100 AND i.price < 5.00);

Take note of the `LEN(o.items) > 0` conjunct. Array indexes cannot be used for queries with potentially empty arrays.

### [](#ExplicitUnnestQueries)Explicit Unnesting Queries

Array indexes can also be used to accelerate queries that involve the explicit unnesting of array fields. You can express the same membership / existential example above using an explicit `UNNEST` query. To keep the same cardinality as the query above, i.e. to undo the `UNNEST`, the query adds a `DISTINCT` clause. The `pCategoriesIdx` index will be utilized anyway.

SELECT DISTINCT p
FROM products p, p.categories c
WHERE c = "Food";

As another example, suppose that you want to find all orders that have _some_ item with a large quantity. The following query utilizes the `oItemsQtyPriceIdx` index, using only the `qty` field.

SELECT DISTINCT o
FROM orders o, o.items i
WHERE i.qty > 100 AND i.price > 0;

In this case, even though you do not want to filter the results by price, you must specify a dummy predicate on the `price` field so that the query optimizer can select the required index.

### [](#JoinQueries)Join Queries

Finally, array indexes can also be used for index nested-loop joins if the field being joined is located within an array. You can create an array index on the `itemno` field in the `items` array of the `orders` collection as follows.

CREATE INDEX oProductIDIdx
ON orders (UNNEST items SELECT itemno:BIGINT)
EXCLUDE UNKNOWN KEY;

Now suppose you want to find all products located in a specific order. You can accomplish this with the join query below. Note that you must specify the `indexnl` join hint to tell Analytics that you want to optimize this specific join, as hash join is the default join method otherwise.

SELECT DISTINCT p
FROM products p JOIN orders o
ON SOME i IN o.items SATISFIES i.itemno /*+ indexnl */ = to_bigint(p.productno)
    WHERE o.custid = "C41";

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

CREATE INDEX oItemItemQtyIdx
ON orders (UNNEST items0 UNNEST items1 SELECT qty:INT)
EXCLUDE UNKNOWN KEY;

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

CREATE INDEX oItemItemItemQtyIdx
ON orders (UNNEST items0 UNNEST items1 UNNEST items2 SELECT qty:BIGINT)
EXCLUDE UNKNOWN KEY;

The queries below will utilize the indexes above. The first query utilizes the `oItemItemQtyIdx` index through nested existential quantification. The second query utilizes the `oItemItemItemQtyIdx` index with three unnesting clauses.

SELECT o
FROM orders o
WHERE SOME o0 IN o.items0 SATISFIES (
    SOME o1 IN o0.items1 SATISFIES o1.qty = 100
);

SELECT DISTINCT o
FROM orders o, o.items0 o0, o0.items1 o1, o1.items2 o2
WHERE o2.qty = 100;