[View original HTML](/enterprise-analytics/current/sqlpp/3_query.html)

> This topic describes the syntax used by SQL++ for Enterprise Analytics queries. 

Most of the examples in this topic assume that you’re using a database called `sampleAnalytics` and a scope called `Commerce`. Refer to [Connecting to Data Sources](../intro/connecting-to-data-sources.md) to install this example data. You can set up standalone collections to access the data in Enterprise Analytics.

You can use a [USE Statements](5%5Fddl%5Fuse.md) to set the database and scope for the statement that follows it. For example:

USE sampleAnalytics.Commerce;

In the UI you can also use the query editor’s **Query Context** lists to set the database and scope.

![The Query Context lists](_images/workbench-context-set.png) 

To try the examples in this topic, select `sampleAnalytics` as the database and `Commerce` as the scope.

Enterprise Analytics uses rule-based optimization to query your collections until you run an `ANALYZE COLLECTION` statement on each collection involved in a query. The ANALYZE statement samples the data in a collection so that cost-based optimization (CBO) can be applied. As the data in a collection changes, you can run `ANALYZE COLLECTION` periodically to update the information used for CBO. See [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md).

## [](#syntax)Syntax

A query can be an [expression](2%5Fexpr.md), or you can construct it from blocks of code called query blocks. A query block can contain several clauses, including `SELECT`, `FROM`, `LET`, `WHERE`, `GROUP BY`, and `HAVING`.

### Query

![(Expr | Selection)](_images/Query.png) 

### Selection

![WithClause? QueryBlock UnionOption* OrderByClause? ( LimitClause | OffsetClause )?](_images/Selection.png) 

### QueryBlock

![SelectClause StreamGenerator? | StreamGenerator SelectClause](_images/QueryBlock.png) 

### StreamGenerator

![FromClause LetClause? WhereClause? (GroupByClause LetClause? HavingClause?)?](_images/StreamGenerator.png) 

|  | Unlike SQL, SQL++ allows the SELECT clause to appear either at the beginning or at the end of a query block. Placing the SELECT clause at the end can make some query blocks easier to understand, because the SELECT clause refers to variables defined by previous clauses. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#Select%5Fclauses)SELECT Clause

### SelectClause

![SELECT](_images/SelectClause.png) 

### Projection

![(Expr ("AS"? Identifier)?) | (VariableRef ".")? "*"](_images/Projection.png) 

Synonyms for `VALUE`: `ELEMENT`, `RAW`

In a query block, the `FROM`, `WHERE`, `GROUP BY`, and `HAVING` clauses are collectively called the **stream generator** if present. All these clauses, taken together, generate a stream of tuples of bound variables. The `SELECT` clause then uses these bound variables to generate the output of the query block.

For example, the clause `FROM customers AS c` scans over the `customers` collection, binding the variable `c` to each `customer` object in turn, and produces a stream of bindings.

Here’s a slightly more complex example of a stream generator:

```SQL++
 FROM customers AS c, orders AS o
 WHERE c.custid = o.custid
```

In this example, the `FROM` clause scans over the customers and orders collections, producing a stream of variable pairs `c` and `o`. The clause binds `c` to a `customer` object and `o` to an `orders` object. The `WHERE` clause then retains only those pairs in which the `custid` values of the two objects match.

The output of the query block is a collection containing one output item for each tuple produced by the stream generator. If the stream generator produces no tuples, the output of the query block is an empty collection. Depending on the `SELECT` clause, each output item may be an object or some other kind of value. The query result is listed as per the `SELECT` order.

```SQL++
 select field1, field2, field3, id from testCollection;
```

Result:

 [
  {
    "field1": "field1",
    "field2": 1,
    "field3": true,
    "id": 1
  },
  {
    "field1": "field1for3",
    "field2": "id3",
    "field3": false,
    "id": 3
  },
  {
    "field1": "field1for2",
    "field3": true,
    "id": 2
  }
]

In addition to using the variables bound by previous clauses, the `SELECT` clause can create and bind some additional variables. For example, the clause `SELECT salary + bonus AS pay` creates the variable `pay` and binds it to the value of `salary + bonus`. You can then use the `pay` variable in a later `ORDER BY` clause.

In SQL++, the `SELECT` clause can appear either at the beginning or at the end of a query block. Since the `SELECT` clause depends on variables bound by other clauses, the examples in this topic place `SELECT` at the end of the query blocks.

## [](#Select%5Felement)SELECT VALUE Clause

The `SELECT VALUE` clause returns an array or multiset that contains the results of evaluating the `VALUE` expression. SQL++ for Enterprise Analytics performs one evaluation per binding tuple—that is, per `FROM` clause item—satisfying the statement’s selection criteria. If there is no `FROM` clause, SQL++ evaluates the expression after `VALUE` once with no binding tuples, with the exception of those inherited from an outer environment.

### Example Q1: SELECT VALUE

```SQL++
 SELECT VALUE 1;
```

Result:

[
   1
]

### Example Q2: Include FROM and WHERE clauses

The following query returns the names of all customers who have ratings above 650.

```SQL++
 FROM customers AS c
 WHERE c.rating > 650
 SELECT VALUE name;
```

Result:

[
    "T. Cody",
    "M. Sinclair",
    "T. Henry"
]

## [](#SQL%5Fselect)SQL-style SELECT Syntax

SQL++ also supports traditional SQL-style `SELECT` syntax. The result of a query guarantees to preserve the order of expressions in the `SELECT` clause.

### Example Q3: SQL-style SELECT

The following query returns the names and customer IDs of any customers with a rating of 750.

```SQL++
 FROM customers AS c
 WHERE c.rating = 750
 SELECT c.name AS customer_name, c.custid AS customer_id;
```

Result:

[
    {
        "customer_id": "C13",
        "customer_name": "T. Cody"
    },
    {
        "customer_id": "C37",
        "customer_name": "T. Henry"
    }
]

## [](#Select%5Fstar)SELECT \*

As in SQL, the phrase `SELECT *` suggests, "select everything."

For each binding tuple in the stream, `SELECT *` produces an output object. For each variable in the binding tuple, the output object contains a field:

* The name of the field is the name of the variable
* The value of the field is the value of the variable

Essentially, `SELECT *` means, return all the bound variables, with their names and values.

This example shows the effect of `SELECT *`. It uses two collections named ages and eyes. The contents of the two collections are:

ages:

```JSON
 [
     { "name": "Bill", "age": 21 },
     { "name": "Sue", "age": 32 }
 ]
```

eyes:

```JSON
 [
     { "name": "Bill", "eyecolor": "brown" },
     { "name": "Sue", "eyecolor": "blue" }
 ]
```

To try the following examples, you can create standalone collections for this data in Enterprise Analytics. See [Create a Standalone Collection](#sources:manage-collection).

The following example applies `SELECT *` to a single collection.

### Example Q4a: SELECT \*

Return all of the information in the ages collection.

```SQL++
 FROM ages AS a
 SELECT * ;
```

Result:

[
    { "a": { "name": "Bill", "age": 21 },
    },
    { "a": { "name": "Sue", "age": 32}
    }
]

Notice that the variable-name `a` appears in the query result. If you omit `AS a` from the `FROM` clause, the variable-name in the query result is `ages`.

The next example applies `SELECT *` to a join of two collections.

### Example Q4b: Apply SELECT \* to a join

Return all of the information in a join of ages and eyes on matching name fields.

```SQL++
 FROM ages AS a, eyes AS e
 WHERE a.name = e.name
 SELECT * ;
```

Result:

[
    { "a": { "name": "Bill", "age": 21 },
      "e": { "name": "Bill", "eyecolor": "Brown" }
    },
    { "a": { "name": "Sue", "age": 32 },
      "e": { "name": "Sue", "eyecolor": "Blue" }
    }
]

Notice that the result of `SELECT *` in SQL++ is more complex than the result of `SELECT *` in SQL.

## [](#Select%5Fvariable%5Fstar)SELECT _variable_.\*

SQL++ has an alternative version of `SELECT *` in which a variable precedes the star.

While the version without a named variable means, return all the bound variables with their names **and** values, `SELECT` _variable_ `.*` means return only the named variable, and return only its value, not its name.

Compare the following example to [Q4a](#q4a) to see the difference between the two versions of `SELECT *`.

### Example Q4c: SELECT _variable_.\*

Return all information in the `ages` collection.

```SQL++
 FROM ages AS a
 SELECT a.*;
```

Result:

[
    { "name": "Bill", "age": 21 },
    { "name": "Sue", "age": 32 }
]

For queries over a single collection, `SELECT` _variable_ `.*` returns a simpler result and may be preferable to `SELECT *`.

In fact, `SELECT` _variable_ `.*`, like `SELECT *` in SQL, is equivalent to a `SELECT` clause that enumerates all of the fields of the collection, as in the next example.

### Example Q4d: Enumerate fields for SELECT

Return all of the information in the ages collection.

```SQL++
 FROM ages AS a
 SELECT a.name, a.age;
```

The result is the same as in example [Q4c](#q4c).

`SELECT` _variable_ `.*` has an additional application. You can use it to return all of the fields of a nested object. The next example uses the `customers` dataset in the [Commerce example database](../intro/connecting-to-data-sources.md) to demonstrate.

### Example Q4e: Return nested fields

In the `customers` dataset, return all of the fields of the `address` objects that have a zip code of 02340.

```SQL++
 FROM customers AS c
 WHERE c.address.zipcode = "02340"
 SELECT address.* ;
```

Result:

[
    {
        "street": "690 River St.",
        "city": "Hanover, MA",
        "zipcode": "02340"
    }
]

## [](#Select%5Fdistinct)SELECT DISTINCT

You use the `DISTINCT` keyword to eliminate duplicate items from the results of a query block.

### Example Q5a: SELECT DISTINCT

Return all of the different cities in the `customers` dataset.

```SQL++
 FROM customers AS c
 SELECT DISTINCT c.address.city;
```

Result:

[
    {
        "city": "Boston, MA"
    },
    {
        "city": "Hanover, MA"
    },
    {
        "city": "St. Louis, MO"
    },
    {
        "city": "Rome, Italy"
    }
]

## [](#select-exclude)SELECT EXCLUDE

You use the EXCLUDE keyword to remove one or more fields that the SELECT clause would otherwise return. Conceptually, the scope of the EXCLUDE clause is the output of the SELECT clause itself. A stream generator with both DISTINCT and EXCLUDE clauses applies the DISTINCT clause after the EXCLUDE clause.

### Example Q5b: SELECT EXCLUDE

For the customer with custid = C13, return their information except for the zip code field—found inside the address object—and the top-level name field.

```SQL++
  FROM customers AS c
  WHERE c.custid = "C13"
  SELECT c.* EXCLUDE address.zipcode, name;
```

Result:

[
    {
        "custid": "C13",
        "address": {
            "street": "201 Main St.",
            "city": "St. Louis, MO"
        },
        "rating": 750
    }
]

## [](#Unnamed%5Fprojections)Unnamed Projections

Similar to standard SQL, the query language supports unnamed projections—also called unnamed `SELECT` clause items—for which the system generates names rather than using names that you provide.

Name generation has these cases:

* If a projection expression is a variable reference expression, its generated name is the name of the variable.
* If a projection expression is a field access expression, its generated name is the last identifier in the expression.
* For all other cases, the query processor generates a unique name.

### Example Q6: Unnamed Projections

Return the last digit and the order date of all orders for the customer with an ID of C41.

```SQL++
 FROM orders AS o
 WHERE o.custid = "C41"
 SELECT o.orderno % 1000, o.order_date;
```

Result:

[
    {
        "$1": 1,
        "order_date": "2020-04-29"
    },
    {
        "$1": 6,
        "order_date": "2020-09-02"
    }
]

In the result, `$1` is the generated name for `o.orderno % 1000`, while `order_date` is the generated name for `o.order_date`.

Because the generated names can be confusing and non-mnemonic, it’s a good practice to use naming conventions and supply meaningful and concise names for the selected items.

## [](#Abbreviated%5Ffield%5Faccess%5Fexpressions)Abbreviated Field Access Expressions

As in standard SQL, you can abbreviate field access expressions when there is no ambiguity. In the next example, the variable `o` is the only possible variable reference for fields `orderno` and `order_date`. As a result, you can omit it from the query. This practice is not recommended, however. Queries can have fields, such as `custid`, that are present in multiple datasets. In addition, such abbreviations can make queries less readable. For more information about abbreviated field access, see [Binding Variables](appendix%5F3%5Fresolution.md#Binding%5Fvariables).

### Example Q7: Abbreviated Field Access Expressions

Same as example [Q6](#q6), omitting the variable reference for the order number and date and providing custom names for `SELECT` clause items.

```SQL++
 FROM orders AS o
 WHERE o.custid = "C41"
 SELECT orderno % 1000 AS last_digit, order_date;
```

Result:

[
    {
        "last_digit": 1,
        "order_date": "2020-04-29"
    },
    {
        "last_digit": 6,
        "order_date": "2020-09-02"
    }
]

## [](#From%5Fclauses)FROM Clause

### FromClause

![FROM](_images/FromClause.png) 

### FromTerm

![NamedExpr (JoinStep | UnnestStep)*](_images/FromTerm.png) 

### NamedExpr

![Expr ("AS"? Variable)?](_images/NamedExpr.png) 

### JoinStep

![("INNER" | ( ( "LEFT" | "RIGHT" ) "OUTER"?))? "JOIN" NamedExpr "ON" Expr](_images/JoinStep.png) 

### UnnestStep

![("INNER" | ( "LEFT" "OUTER"?))? "UNNEST" NamedExpr](_images/UnnestStep.png) 

Synonyms for `UNNEST`: `CORRELATE`, `FLATTEN`

The purpose of a `FROM` clause is to logically iterate over a collection, binding a variable to each item in turn. Here’s a query that iterates over the `customers` dataset, choosing certain customers and returning some of their attributes.

### Example Q8: FROM clause with implicit variable

List the customer IDs and names of the customers in zip code 63101, in order by their customer IDs.

```SQL++
 FROM customers
 WHERE address.zipcode = "63101"
 SELECT custid AS customer_id, name
 ORDER BY customer_id;
```

Result:

[
    {
        "customer_id": "C13",
        "name": "T. Cody"
    },
    {
        "customer_id": "C31",
        "name": "B. Pruitt"
    },
    {
        "customer_id": "C41",
        "name": "R. Dodge"
    }
]

A `FROM` clause always produces a stream of bindings, and binds an iteration variable to each item in a collection in turn. Because the [Q8](#q8) example does not provide an explicit iteration variable, the `FROM` clause defines an implicit variable named `customers`, the same name as the dataset that’s being iterated over. The implicit iteration variable serves as the object-name for all field-names in the query block that do not have explicit object-names. As a result, `address.zipcode` means `customers.address.zipcode`, `custid` means `customers.custid`, and `name` means `customers.name`.

You can also provide an explicit iteration variable, as in this version of the same query.

### Example Q9: FROM clause with explicit variable

Alternative version of [Q8](#q8) with the same result.

```SQL++
 FROM customers AS c
 WHERE c.address.zipcode = "63101"
 SELECT c.custid AS customer_id, c.name
 ORDER BY customer_id;
```

This example binds the variable `c` to each `customer` object in turn as the query iterates over the `customers` dataset. You can use an explicit iteration variable to identify the fields of the referenced object, as in `c.name` in the `SELECT` clause of Q9\. When referencing a field of an object, you can omit the iteration variable when there is no ambiguity. For example, you could replace `c.name` by `name` in the `SELECT` clause of Q9\. That’s why field-names like `name` and `custid` could stand by themselves in the [Q8](#q8) version of this query.

In the [Q8](#q8) and [Q9](#q9) examples, the `FROM` clause iterates over the objects in a dataset. However, in general, a `FROM` clause can iterate over any collection. For example, the objects in the `orders` dataset each contain a field called `items`, which is an array of nested objects. In some cases, you’ll write a `FROM` clause that iterates over a nested array like `items`.

The stream of objects, or more accurately the variable bindings, produced by the `FROM` clause does not have any particular order. The system chooses the most efficient order for the iteration. If you want your query result to have a specific order, you must use an `ORDER BY` clause.

It’s good practice to specify an explicit iteration variable for each collection in the `FROM` clause, and to use these variables to qualify the field-names in other clauses. Here are some reasons for this convention:

* Supplying different names for the collection as a whole and for an object in the collection improves readability. For example, in the clause `FROM customers AS c`, the name `customers` represents the dataset and the name `c` represents one object in the dataset.
* In some cases, a query requires iteration variables. For example, to join a dataset to itself, you must supply distinct iteration variables to distinguish the left side of the join from the right side.
* In a subquery, it’s sometimes necessary to refer to an object in an outer query block, called a correlated subquery. To avoid potential confusion in correlated subqueries, it’s best to use explicit variables.

## [](#Join%5Fclauses)Joins

A `FROM` clause gets more interesting when there is more than one collection involved. The following query iterates over two collections: `customers` and `orders`. The `FROM` clause produces a stream of binding tuples, each containing two variables, `c` and `o`. The next example binds `c` to an object from `customers` and `o` to an object from `orders`. Conceptually, at this point, the binding tuple stream contains all possible pairs of a customer and an order, called the Cartesian product of `customers` and `orders`.

The `WHERE` clause expresses a requirement to return only pairs where the `custid` fields match, along with the restriction that the order number must be 1001.

### Example Q10: Implicit join

Create a packing list for order number 1001, showing the customer name and address and all of the items in the order.

```SQL++
 FROM customers AS c, orders AS o
 WHERE c.custid = o.custid
 AND o.orderno = 1001
 SELECT o.orderno,
     c.name AS customer_name,
     c.address,
     o.items AS items_ordered;
```

Result:

[
    {
        "orderno": 1001,
        "customer_name": "R. Dodge",
        "address": {
            "street": "150 Market St.",
            "city": "St. Louis, MO",
            "zipcode": "63101"
        },
        "items_ordered": [
            {
                "itemno": 347,
                "qty": 5,
                "price": 19.99
            },
            {
                "itemno": 193,
                "qty": 2,
                "price": 28.89
            }
        ]
    }
]

This join query joins the `customers` collection and the `orders` collection, using the join condition `c.custid = o.custid`. In SQL++, as in SQL, you can also express the join explicitly by using a `JOIN` clause that includes the join condition, as in the next example.

### Example Q11: Explicit JOIN clause

Alternative to example [Q10](#q10), same result:

```SQL++
 FROM customers AS c JOIN orders AS o
     ON c.custid = o.custid
 WHERE o.orderno = 1001
 SELECT o.orderno,
     c.name AS customer_name,
     c.address,
     o.items AS items_ordered;
```

Whether you express the join condition in an explicit `JOIN` clause or in a `WHERE` clause is a matter of preference. The result is the same. This reference guide generally uses a comma-separated list of collection-names in the `FROM` clause and expresses the join condition elsewhere. More examples follow, including some with query blocks that omit the join condition entirely.

In one case, an explicit `JOIN` clause is necessary. When you need to join collection A to collection B, and you want to make sure that the query results include every item in collection A, even items that do not match any item in collection B, you must include the `JOIN` clause. This kind of query is called a left outer join, and is shown in the following example.

### Example Q12: Left outer join

List the customer ID and name, together with the order numbers and dates of their orders—if any—of customers T. Cody and M. Sinclair.

```SQL++
 FROM customers AS c LEFT OUTER JOIN orders AS o ON c.custid = o.custid
 WHERE c.name = "T. Cody"
    OR c.name = "M. Sinclair"
 SELECT c.custid, c.name, o.orderno, o.order_date
 ORDER BY c.custid, o.order_date;
```

Result:

[
    {
        "custid": "C13",
        "orderno": 1002,
        "name": "T. Cody",
        "order_date": "2020-05-01"
    },
    {
        "custid": "C13",
        "orderno": 1007,
        "name": "T. Cody",
        "order_date": "2020-09-13"
    },
    {
        "custid": "C13",
        "orderno": 1008,
        "name": "T. Cody",
        "order_date": "2020-10-13"
    },
    {
        "custid": "C13",
        "orderno": 1009,
        "name": "T. Cody",
        "order_date": "2020-10-13"
    },
    {
        "custid": "C25",
        "name": "M. Sinclair"
    }
]

As you see in these results, the data includes four orders from customer T. Cody, but no orders from customer M. Sinclair. The behavior of left outer join in SQL++ is different from that of SQL. SQL would have provided M. Sinclair with an order in which all the fields were `null`. SQL++, on the other hand, deals with schema-less data, which permits it to omit the order fields from the outer join.

The next example shows a different kind of join that was not provided or needed in original SQL. You use this join for nested JSON data. Consider the query in the next example. Notice that the query joins `orders`, which is a dataset, to `items`, which is an array nested inside each order.

### Example Q13: Join nested data

For every case in which an item order has a quantity greater than 100, show the order number, date, item number, and quantity.

```SQL++
 FROM orders AS o, o.items AS i
 WHERE i.qty > 100
 SELECT o.orderno, o.order_date, i.itemno AS item_number,
     i.qty AS quantity
 ORDER BY o.orderno, item_number;
```

Result:

[
    {
        "orderno": 1002,
        "order_date": "2020-05-01",
        "item_number": 680,
        "quantity": 150
    },
    {
        "orderno": 1005,
        "order_date": "2020-08-30",
        "item_number": 347,
        "quantity": 120
    },
    {
        "orderno": 1006,
        "order_date": "2020-09-02",
        "item_number": 460,
        "quantity": 120
    }
]

This example illustrates a feature called left-correlation in the `FROM` clause. In effect, for each order, the query unnests its `items` array and joins it to the `order` as though it were a separate collection. For this reason, this kind of query is sometimes called an unnesting query.

You can use the explicit keyword `UNNEST` whenever you use left-correlation in a `FROM` clause, as shown in the next example.

### Example Q14: Join nested data with UNNEST

Alternative statement of example [Q13](#q13), same result:

```SQL++
 FROM orders AS o UNNEST o.items AS i
 WHERE i.qty > 100
 SELECT o.orderno, o.order_date, i.itemno AS item_number,
         i.qty AS quantity
 ORDER BY o.orderno, item_number;
```

The results of [Q13](#q13) and Q14 are the same. `UNNEST` serves as a reminder that the query uses left-correlation to join an object with its nested items. The left-correlation expresses the join condition in example [Q14](#q14): it joins each order `o` to its own items, referenced as `o.items`.

The result of the `FROM` clause is a stream of binding tuples, each containing two variables, `o` and `i`. The query binds the variable `o` to an order and the variable `i` to one item inside that order.

Like `JOIN`, `UNNEST` has a `LEFT OUTER` option. Q14 could have specified:

FROM orders AS o LEFT OUTER UNNEST o.items AS i

In this case, orders that have no nested items would still appear in the query result.

## [](#Let%5Fclauses)LET Clause

### LetClause

![LET](_images/LetClause.png) 

Synonym for `LET`: `LETTING`

`LET` clauses can be useful when you use a complex expression several times within a query, allowing you to write it once to make the query more concise. You can use `LETTING` instead of `LET`. The next query shows an example.

### Example Q15: LET clause

For each item in an order, define revenue as the quantity times the price of that item. Find individual items for which the revenue is greater than 5000\. For each of these items, list the order number, item number, and revenue, in descending order by revenue.

```SQL++
 FROM orders AS o, o.items AS i
 LET revenue = i.qty * i.price
 WHERE revenue > 5000
 SELECT o.orderno, i.itemno, revenue
 ORDER by revenue desc;
```

Result:

[
    {
        "orderno": 1006,
        "itemno": 460,
        "revenue": 11997.6
    },
    {
        "orderno": 1002,
        "itemno": 460,
        "revenue": 9594.05
    },
    {
        "orderno": 1006,
        "itemno": 120,
        "revenue": 5525
    }
]

The `LET` clause defines the expression for computing `revenue` once. The remainder of the query then includes `revenue` three more times. Avoiding repetition of the `revenue` expression makes the query shorter and less prone to errors.

## [](#Where%5Fhaving%5Fclauses)WHERE Clause

### WhereClause

![WHERE](_images/WhereClause.png) 

The purpose of a `WHERE` clause is to operate on the stream of binding tuples generated by the `FROM` clause, filtering out the tuples that do not satisfy a certain condition. You specify the condition in an expression based on the variable names in the binding tuples. If the expression evaluates to true, the tuple remains in the stream. Tuples that evaluate to anything else, including `null` or `missing`, get filtered out. The surviving tuples are then passed along to the next clause for processing, often by either `GROUP BY` or `SELECT`.

Often, the expression in a `WHERE` clause is some kind of comparison like `quantity > 100`. However, a `WHERE` clause allows any kind of expression. The only thing that matters is whether the expression returns `true` or not.

## [](#Grouping)Grouping

Grouping is important when manipulating hierarchies like the ones that are often found in JSON data. For example, you might want to generate output data that includes both summary data and line items within the summaries. For this purpose, SQL++ supports several important extensions to the traditional grouping features of SQL. The familiar `GROUP BY` and `HAVING` clauses are available, along with a new clause called `GROUP AS`. A series of examples shows the use of these clauses.

### [](#Group%5FBy%5Fclauses)GROUP BY Clause

#### GroupByClause

![GROUP BY](_images/GroupByClause.png) 

#### GroupingElement

![OrdinaryGroupingSet | ( "GROUPING" "SETS" "(" GroupingElement ("](_images/GroupingElement.png) 

#### OrdinaryGroupingSet

![NamedExpr | ( "(" NamedExpr ( "](_images/OrdinaryGroupingSet.png) 

#### NamedExpr

![GROUP AS](_images/NamedExpr.png) 

To start, here’s an example of grouping from ordinary SQL.

#### Example Q16: GROUP BY clause

List the number of orders placed by each customer who has placed an order.

```SQL++
 SELECT o.custid, COUNT(o.orderno) AS `order count`
 FROM orders AS o
 GROUP BY o.custid
 ORDER BY o.custid;
```

Result:

[
    {
        "order count": 4,
        "custid": "C13"
    },
    {
        "order count": 1,
        "custid": "C31"
    },
    {
        "order count": 1,
        "custid": "C35"
    },
    {
        "order count": 1,
        "custid": "C37"
    },
    {
        "order count": 2,
        "custid": "C41"
    }
]

The input to a `GROUP BY` clause is the stream of binding tuples generated by the `FROM` and `WHERE`clauses. Before grouping, this query binds the variable `o` to each object in the `orders` collection in turn.

SQL++ evaluates the expression in the `GROUP BY` clause, called the grouping expression, once for each of the binding tuples. It then organizes the results into groups in which the grouping expression has a common value, defined by the `=` operator. In this example, the grouping expression is `o.custid`, and each of the resulting groups is a set of `orders` that have the same `custid`. If necessary, the system forms a group for `orders` in which `custid` is `null`, and another group for `orders` that have no `custid`. This query uses the aggregating function `COUNT(o.orderno)`, which counts the order numbers in each group. If you’re sure that each order object has a distinct `orderno`, you could instead count the order objects in each group by using `COUNT(*)` in place of `COUNT(o.orderno)`.

In the `GROUP BY` clause, you can optionally define an alias for the grouping expression. For example, in [Q16](#q16), you could have written `GROUP BY o.custid AS cid`. You could then use the alias `cid` in place of the grouping expression in later clauses. In cases where the grouping expression contains an operator, it’s helpful to define an alias: for example, `GROUP BY salary + bonus AS pay`.

Example [Q16](#q16) had a single grouping expression, `o.custid`. If a query has multiple grouping expressions, it evaluates the combination of grouping expressions for every binding tuple, and partitions the stream of binding tuples into groups that have values in common for all of the grouping expressions. An example of such a query follows in [Q18](#q18).

Grouping results in a reduced number of binding tuples: instead of a binding tuple for each of the input objects, there is a binding tuple for each group. The query binds the grouping expressions, identified by their aliases if any, to the results of their evaluations. However, all the non-grouping fields—that is, fields that were not named in the grouping expressions—are accessible only in a special way: as an argument of one of the aggregation pseudo-functions such as: `SUM`, `AVG`, `MAX`, `MIN`, `STDEV` and `COUNT`. The clauses that come after grouping can access only properties of groups, including the grouping expressions and aggregate properties of the groups such as `COUNT(o.orderno)` or `COUNT(*)`. The description of the new `GROUP AS` clause includes an exception.

You may notice that the results of example [Q16](#q16) do not include customers who have no `orders`. To include these `customers`, you need to use an outer join between the `customers` and `orders` collections. The following example adds the outer join and also includes the name of each customer.

#### Example Q17: Grouping with outer join

List the number of orders placed by each customer including those customers who have placed no orders.

```SQL++
 SELECT c.custid, c.name, COUNT(o.orderno) AS `order count`
 FROM customers AS c LEFT OUTER JOIN orders AS o ON c.custid = o.custid
 GROUP BY c.custid, c.name
 ORDER BY c.custid;
```

Result:

[
    {
        "custid": "C13",
        "order count": 4,
        "name": "T. Cody"
    },
    {
        "custid": "C25",
        "order count": 0,
        "name": "M. Sinclair"
    },
    {
        "custid": "C31",
        "order count": 1,
        "name": "B. Pruitt"
    },
    {
        "custid": "C35",
        "order count": 1,
        "name": "J. Roberts"
    },
    {
        "custid": "C37",
        "order count": 1,
        "name": "T. Henry"
    },
    {
        "custid": "C41",
        "order count": 2,
        "name": "R. Dodge"
    },
    {
        "custid": "C47",
        "order count": 0,
        "name": "S. Logan"
    }
]

Notice in example [Q17](#q17) what happens when you apply the special aggregation function `COUNT` to a collection that does not exist, such as the orders of M. Sinclair: it returns zero. This behavior is unlike that of the other special aggregation functions `SUM`, `AVG`, `MAX`, and `MIN`, which return `null` if their operand does not exist. This should make you cautious about the `COUNT` function: If it returns zero, that might mean that the collection you’re counting has zero members, or that it does not exist, or that you have misspelled the collection’s name.

Example [Q17](#q17) also shows how a query block can have more than one grouping expression. In general, the `GROUP BY` clause produces a binding tuple for each different combination of values for the grouping expressions. In Q17, the `c.custid` field uniquely identifies a customer, so adding `c.name` as a grouping expression does not result in any more groups. Nevertheless, you must include `c.name` as a grouping expression to reference it outside—after—the `GROUP BY` clause. If you do not include `c.name` in the `GROUP BY` clause, it’s not a group property and you cannot use it in the `SELECT` clause.

Of course, a grouping expression need not be a field-name. The [Q18](#q18) example groups orders by month, using a temporal function to extract the month component of the order dates. In cases like this, it’s helpful to define an alias for the grouping expression so that you can reference it elsewhere in the query, such as in the `SELECT` clause.

#### Example Q18: Grouping expressions

Find the months in 2020 that had the largest numbers of orders, then list the months and their numbers of orders. Return the top three.

```SQL++
 FROM orders AS o
 WHERE DATE_PART_STR(o.order_date, "year") = 2020
 GROUP BY DATE_PART_STR(o.order_date, "month") AS month
 SELECT month, COUNT(*) AS order_count
 ORDER BY order_count DESC, month DESC
 LIMIT 3;
```

Result:

[
    {
        "month": 10,
        "order_count": 2
    },
    {
        "month": 9,
        "order_count": 2
    },
    {
        "month": 8,
        "order_count": 1
    }
]

Groups are commonly formed from named collections like `customers` and `orders`. However, in some queries you need to form groups from a collection that’s nested inside another collection, such as `items` inside `orders`. In SQL++ you can do this by using left-correlation in the `FROM` clause to unnest the inner collection, joining the inner collection with the outer collection, and then performing the grouping on the join, as illustrated in example [Q19](#q19) .

Example [Q19](#q19) also shows how you can use a `LET` clause after a `GROUP BY` clause to define an expression that you can reference multiple times in later clauses.

#### Example Q19: UNNEST an inner collection

For each order, define the `total_revenue` of the order as the sum of quantity times price for all the items in that order. List the total revenue for all the orders placed by the customer with id C13, in descending order by total revenue.

```SQL++
 FROM orders as o, o.items as i
 WHERE o.custid = "C13"
 GROUP BY o.orderno
 LET total_revenue = sum(i.qty * i.price)
 SELECT o.orderno, total_revenue
 ORDER BY total_revenue desc;
```

Result:

[
    {
        "orderno": 1002,
        "total_revenue": 10906.55
    },
    {
        "orderno": 1008,
        "total_revenue": 1999.8
    },
    {
        "orderno": 1007,
        "total_revenue": 130.45
    }
]

#### [](#Rollup)ROLLUP

The `ROLLUP` sub-clause is an aggregation feature that extends the functionality of the `GROUP BY` clause. It returns extra super-aggregate items in the query results, giving subtotals and a grand total for the aggregate functions in the query.

Consider the following query.

##### [](#example-qr1-grouping-without-a-rollup-sub-clause)Example QR1: Grouping without a ROLLUP sub-clause

List the number of orders, grouped by customer region and city.

```SQL++
 SELECT customer_region AS Region,
        customer_city AS City,
        COUNT(o.orderno) AS `Order Count`
 FROM customers AS c LEFT OUTER JOIN orders AS o ON c.custid = o.custid
 LET address_line = SPLIT(c.address.city, ","),
     customer_city = TRIM(address_line[0]),
     customer_region = TRIM(address_line[1])
 GROUP BY customer_region, customer_city
 ORDER BY customer_region ASC, customer_city ASC, `Order Count` DESC;
```

Result:

[
  {
    "Region": "Italy",
    "City": "Rome",
    "Order Count": 0
  },
  {
    "Region": "MA",
    "City": "Boston",
    "Order Count": 2
  },
  {
    "Region": "MA",
    "City": "Hanover",
    "Order Count": 0
  },
  {
    "Region": "MO",
    "City": "St. Louis",
    "Order Count": 7
  }
]

This query uses string functions to split each customer’s address into city and region. The query then counts the total number of orders placed by each customer, and groups the results first by customer region, then by customer city. The aggregate results, labeled `Order Count`, are only shown by city, and there are no subtotals or grand total. To add these, you can use the `ROLLUP` sub-clause, as in the following example.

##### [](#example-qr2-grouping-with-rollup-totals)Example QR2: Grouping with ROLLUP totals

List the number of orders by customer region and city, including subtotals and a grand total.

```SQL++
 SELECT customer_region AS Region,
        customer_city AS City,
        COUNT(o.orderno) AS `Order Count`
 FROM customers AS c LEFT OUTER JOIN orders AS o ON c.custid = o.custid
 LET address_line = SPLIT(c.address.city, ","),
     customer_city = TRIM(address_line[0]),
     customer_region = TRIM(address_line[1])
 GROUP BY ROLLUP(customer_region, customer_city)
 ORDER BY customer_region ASC, customer_city ASC, `Order Count` DESC;
```

Result:

[
  {
    "Region": null,
    "City": null,
    "Order Count": 9
  },
  {
    "Region": "Italy",
    "City": null,
    "Order Count": 0
  },
  {
    "Region": "Italy",
    "City": "Rome",
    "Order Count": 0
  },
  {
    "Region": "MA",
    "City": null,
    "Order Count": 2
  },
  {
    "Region": "MA",
    "City": "Boston",
    "Order Count": 2
  },
  {
    "Region": "MA",
    "City": "Hanover",
    "Order Count": 0
  },
  {
    "Region": "MO",
    "City": null,
    "Order Count": 7
  },
  {
    "Region": "MO",
    "City": "St. Louis",
    "Order Count": 7
  }
]

With the addition of the `ROLLUP` sub-clause, notice that the results now include:

* An extra item at the start of the results, giving the grand total for all regions: `"Region": null, "City": null`.
* An extra item at the start of each region, giving the subtotal for that region: the region name followed by `"City": null`.

The order of the fields specified by the `ROLLUP` sub-clause determines the hierarchy of the super-aggregate items. This example specifies the customer region first, followed by the customer city. As a result, the results are aggregated by region first, and then by city within each region.

The grand total returns `null` as a value for the city and the region, and the subtotals return `null` as the value for the city, which may make the results hard to understand at first glance. The next example gives a workaround for this.

##### [](#example-qr3-rollup-with-ifnull-identifiers)Example QR3: ROLLUP with IFNULL identifiers

List the number of orders by customer region and city, with meaningful subtotals and grand total.

```SQL++
 SELECT IFNULL(customer_region, "All regions") AS Region,
        IFNULL(customer_city, "All cities") AS City,
        COUNT(o.orderno) AS `Order Count`
 FROM customers AS c LEFT OUTER JOIN orders AS o ON c.custid = o.custid
 LET address_line = SPLIT(c.address.city, ","),
     customer_city = TRIM(address_line[0]),
     customer_region = TRIM(address_line[1])
 GROUP BY ROLLUP(customer_region, customer_city)
 ORDER BY customer_region ASC, customer_city ASC, `Order Count` DESC;
```

Result:

[
  {
    "Region": "All regions",
    "City": "All cities",
    "Order Count": 9
  },
  {
    "Region": "Italy",
    "City": "All cities",
    "Order Count": 0
  },
  {
    "Region": "Italy",
    "City": "Rome",
    "Order Count": 0
  },
  {
    "Region": "MA",
    "City": "All cities",
    "Order Count": 2
  },
  {
    "Region": "MA",
    "City": "Boston",
    "Order Count": 2
  },
  {
    "Region": "MA",
    "City": "Hanover",
    "Order Count": 0
  },
  {
    "Region": "MO",
    "City": "All cities",
    "Order Count": 7
  },
  {
    "Region": "MO",
    "City": "St. Louis",
    "Order Count": 7
  }
]

This query uses the `IFNULL` function to populate the region and city fields with meaningful values for the super-aggregate items. This makes the results clearer and more readable.

#### [](#Cube)CUBE

The `CUBE` sub-clause is similar to the `ROLLUP` sub-clause, in that it returns extra super-aggregate items in the query results, giving subtotals and a grand total for the aggregate functions. While `ROLLUP` returns a grand total and a hierarchy of subtotals based on the specified fields, the `CUBE` sub-clause returns a grand total and subtotals for every possible combination of the specified fields.

The following example is a modification of QR3 which illustrates the `CUBE` sub-clause.

##### [](#example-qc-cube-sub-clause)Example QC: CUBE sub-clause

List the number of orders by customer region and order date, with all possible subtotals and a grand total.

```SQL++
 SELECT IFNULL(customer_region, "All regions") AS Region,
        IFNULL(order_month, "All months") AS Month,
        COUNT(o.orderno) AS `Order Count`
 FROM customers AS c INNER JOIN orders AS o ON c.custid = o.custid
 LET address_line = SPLIT(c.address.city, ","),
     customer_region = TRIM(address_line[1]),
     order_month = DATE_PART_STR(o.order_date, "month")
 GROUP BY CUBE(customer_region, order_month)
 ORDER BY customer_region ASC, order_month ASC;
```

Result:

[
  {
    "Region": "All regions",
    "Order Count": 9,
    "Month": "All months"
  },
  {
    "Region": "All regions",
    "Order Count": 1,
    "Month": 4
  },
  {
    "Region": "All regions",
    "Order Count": 1,
    "Month": 5
  },
  {
    "Region": "All regions",
    "Order Count": 1,
    "Month": 6
  },
  {
    "Region": "All regions",
    "Order Count": 1,
    "Month": 7
  },
  {
    "Region": "All regions",
    "Order Count": 1,
    "Month": 8
  },
  {
    "Region": "All regions",
    "Order Count": 2,
    "Month": 9
  },
  {
    "Region": "All regions",
    "Order Count": 2,
    "Month": 10
  },
  {
    "Region": "MA",
    "Order Count": 2,
    "Month": "All months"
  },
  {
    "Region": "MA",
    "Order Count": 1,
    "Month": 7
  },
  {
    "Region": "MA",
    "Order Count": 1,
    "Month": 8
  },
  {
    "Region": "MO",
    "Order Count": 7,
    "Month": "All months"
  },
  {
    "Region": "MO",
    "Order Count": 1,
    "Month": 4
  },
  {
    "Region": "MO",
    "Order Count": 1,
    "Month": 5
  },
  {
    "Region": "MO",
    "Order Count": 1,
    "Month": 6
  },
  {
    "Region": "MO",
    "Order Count": 2,
    "Month": 9
  },
  {
    "Region": "MO",
    "Order Count": 2,
    "Month": 10
  }
]

To simplify the results, this query uses an inner join so that customers who have not placed an order are not included in the totals. The query uses string functions to extract the region from each customer’s address, and a temporal function to extract the year from the order date.

The query uses the `CUBE` sub-clause with customer region and order month. This means that there are four possible aggregates to calculate:

* All regions, all months
* All regions, each month
* Each region, all months
* Each region, each month

The results start with the grand total, showing the total number of orders across all regions for all months. Date subtotals follow, showing the number of orders across all regions for each month. Regional subtotals, showing the total number of orders for all months in each region follow, and then the result items, giving the number of orders for each month in each region.

The query also uses the `IFNULL` function to populate the region and date fields with meaningful values for the super-aggregate items. This makes the results clearer and more readable.

### [](#Having%5Fclauses)HAVING Clause

##### HavingClause

![HAVING](_images/HavingClause.png) 

The `HAVING` clause is similar to the `WHERE` clause, except that it comes after `GROUP BY` and applies a filter to groups rather than to individual objects. Here’s an example of a `HAVING` clause that filters orders by applying a condition to their nested arrays of `items`.

By adding a `HAVING` clause to Q19, you can filter the results to include only those orders with total revenue greater than 1000, as shown in Q22.

##### Example Q20: HAVING clause

Modify example [Q19](#q19) to include only orders with total revenue greater than 5000.

```SQL++
 FROM orders AS o, o.items as i
 WHERE o.custid = "C13"
 GROUP BY o.orderno
 LET total_revenue = sum(i.qty * i.price)
 HAVING total_revenue > 5000
 SELECT o.orderno, total_revenue
 ORDER BY total_revenue desc;
```

Result:

[
    {
        "orderno": 1002,
        "total_revenue": 10906.55
    }
]

### [](#Aggregation%5FPseudoFunctions)Aggregation Pseudo-Functions

SQL provides several special functions for performing aggregations on groups including: `SUM`, `AVG`, `MAX`, `MIN`, and `COUNT`; some implementations provide more. SQL++ supports these same functions. However, it’s worth spending some time on these special functions because they do not behave like ordinary functions. They’re called pseudo-functions here because they do not evaluate their operands in the same way as ordinary functions.

To see the difference, consider these two examples, which are syntactically similar:

Example 1

SELECT LENGTH(name) FROM customers;

In Example 1, `LENGTH` is an ordinary function. It evaluates its operand `(name)` and then returns a result computed from the operand.

Example 2

SELECT AVG(rating) FROM customers;

The effect of `AVG` in Example 2 is quite different. Rather than performing a computation on an individual rating value, `AVG` has a global effect: it effectively restructures the query. As a pseudo-function, `AVG` requires its operand to be a group; therefore, it automatically collects all the rating values from the query block and forms them into a group.

The aggregation pseudo-functions always require their operand to be a group. In some queries, the group is explicitly generated by a `GROUP BY` clause, as in Q21.

#### Example Q21: Aggregation pseudo-function with GROUP BY

List the average credit rating of customers by zip code.

```SQL++
 FROM customers AS c
 GROUP BY c.address.zipcode AS zip
 SELECT zip, AVG(c.rating) AS `avg credit rating`
 ORDER BY zip;
```

Result:

[
    {
        "avg credit rating": 625
    },
    {
        "avg credit rating": 657.5,
        "zip": "02115"
    },
    {
        "avg credit rating": 690,
        "zip": "02340"
    },
    {
        "avg credit rating": 695,
        "zip": "63101"
    }
]

Note in the result of Q21 that one or more customers had no zip code. The query forms a group for these customers for whom the value of the grouping key is missing. For query results returned in JSON format, the `missing` key is not included. Notice that the group with the `missing` key appears first: SQL++ considers `missing` to be smaller than any other value. If any customers had a `null` zip code value, another group would form for those customers, and appear after the `missing` group but before the other groups.

When you use an aggregation pseudo-function without an explicit `GROUP BY` clause, it implicitly forms the entire query block into a single group, as in Q22.

#### Example Q22: Aggregation pseudo-function without GROUP BY

Find the average credit rating among all customers.

```SQL++
 FROM customers AS c
 SELECT AVG(c.rating) AS `avg credit rating`;
```

Result:

[
    {
        "avg credit rating": 670
    }
]

The aggregation pseudo-function `COUNT` has a special form in which its operand is `*` instead of an expression.

For example, `SELECT COUNT(*) FROM customers` returns the total number of customers, while `SELECT COUNT(rating) FROM customers` returns the number of customers who have known ratings—that is, their ratings are not `null` or `missing`.

Because the aggregation pseudo-functions sometimes restructure their operands, you can only use them in query blocks that do explicit or implicit grouping. Therefore, the pseudo-functions cannot operate directly on arrays or multisets. For operating directly on JSON collections, SQL++ provides a set of ordinary functions for computing aggregations. Each ordinary aggregation function, except the ones corresponding to `COUNT` and `ARRAY_AGG`, has two versions: one that ignores `null` and `missing` values and one that returns `null` if a `null` or `missing` value is encountered anywhere in the collection. The names of the aggregation functions follow:

| Aggregation pseudo-function; operates on groups only | Ordinary function: Ignores NULL or MISSING values | Ordinary function: Returns NULL if NULL or MISSING encountered |
| ---------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------- |
| SUM                                                  | ARRAY\_SUM                                        | STRICT\_SUM                                                    |
| AVG                                                  | ARRAY\_MAX                                        | STRICT\_MAX                                                    |
| MAX                                                  | ARRAY\_MIN                                        | STRICT\_MIN                                                    |
| MIN                                                  | ARRAY\_AVG                                        | STRICT\_AVG                                                    |
| COUNT                                                | ARRAY\_COUNT                                      | STRICT\_COUNT (see exception below)                            |
| STDDEV\_SAMP                                         | ARRAY\_STDDEV\_SAMP                               | STRICT\_STDDEV\_SAMP                                           |
| STDDEV\_POP                                          | ARRAY\_STDDEV\_POP                                | STRICT\_STDDEV\_POP                                            |
| VAR\_SAMP                                            | ARRAY\_VAR\_SAMP                                  | STRICT\_VAR\_SAMP                                              |
| VAR\_POP                                             | ARRAY\_VAR\_POP                                   | STRICT\_VAR\_POP                                               |
| SKEWENESS                                            | ARRAY\_SKEWNESS                                   | STRICT\_SKEWNESS                                               |
| KURTOSIS                                             | ARRAY\_KURTOSIS                                   | STRICT\_KURTOSIS                                               |
|                                                      | ARRAY\_AGG                                        |                                                                |

Exception: the ordinary aggregation function `STRICT_COUNT` operates on any collection, and returns a count of its items, including null values in the count. In this respect, `STRICT_COUNT` is more similar to `COUNT(*)` than to `COUNT(expression)`.

Notice that the ordinary aggregation functions that ignore `null` have names beginning with `ARRAY`. This naming convention has historical roots. Despite their names, the functions operate on both arrays and multisets.

Because of the special properties of the aggregation pseudo-functions, SQL, and therefore SQL++, is not a pure functional language. However, you can express every query that uses a pseudo-function as an equivalent query that uses an ordinary function. Q23 is an example of how you can express queries without pseudo-functions. A more detailed explanation of all of the functions is also available in the section on [Aggregate Functions](8%5Fbuiltin%5Fagg.md).

##### Example Q23: Ordinary function replaces aggregation pseudo-function

Alternative form of example [Q22](#q22), using the ordinary function `ARRAY_AVG` rather than the aggregating pseudo-function `AVG`.

```SQL++
 SELECT ARRAY_AVG(
     (SELECT VALUE c.rating
     FROM customers AS c) ) AS `avg credit rating`;
```

Result, same as [Q22](#q22):

[
    {
        "avg credit rating": 670
    }
]

If you use the function `STRICT_AVG` in Q23 in place of `ARRAY_AVG`, the average credit rating returned by the query is `null` because at least one customer has no credit rating.

### [](#Group%5FAs%5Fclauses)GROUP AS Clause

#### GroupAsClause

![GROUP AS](_images/GroupAsClause.png) 

JSON is a hierarchical format, and a fully featured JSON query language needs to be able to produce hierarchies of its own, with computed data at every level of the hierarchy. The key feature of SQL++ that makes this possible is the `GROUP AS` clause.

A query can have a `GROUP AS` clause only if it has a `GROUP BY` clause. The `GROUP BY` clause hides the original objects in each group, exposing only the grouping expressions and special aggregation functions on the non-grouping fields. The purpose of the `GROUP AS` clause is to make the original objects in the group visible to subsequent clauses. As a result, the query can generate output data both for the group as a whole and for the individual objects inside the group.

For each group, the `GROUP AS` clause preserves all the objects in the group, just as they were before grouping, and gives a name to this preserved group. You can then use the group name in the `FROM` clause of a subquery to process and return the individual objects in the group.

To see how this works, the next examples are of queries that investigate the customers in each zip code and their credit ratings. You can review the [Connecting to Data Sources](../intro/connecting-to-data-sources.md), or this data summary:

Customers in zip code 02115:
    C35, J. Roberts, rating 565
    C37, T. Henry, rating 750

Customers in zip code 02340:
    C25, M. Sinclair, rating 690

Customers in zip code 63101:
    C13, T. Cody, rating 750
    C31, B. Pruitt, (no rating)
    C41, R. Dodge, rating 640

Customers with no zip code:
    C47, S. Logan, rating 625

Now, consider the effect of the following clauses:

FROM customers AS c
GROUP BY c.address.zipcode
GROUP AS g

This query fragment iterates over the `customers` objects, using the iteration variable `c`. The `GROUP BY` clause forms the objects into groups, each with a common zip code, including one group for customers with no zip code. After the `GROUP BY` clause, the grouping expression `c.address.zipcode` appears, but other fields such as `c.custid` and `c.name` are visible only to special aggregation functions.

Adding the clause `GROUP AS g` makes the original objects visible again. For each group in turn, this clause binds the variable `g` to a multiset of objects, each of which has a field named `c`, which in turn contains one of the original objects. As a result, `GROUP AS g` binds the group with zip code 02115 to the following multiset:

[
    { "c":
        { "custid": "C35",
          "name": "J. Roberts",
          "address":
            { "street": "420 Green St.",
              "city": "Boston, MA",
              "zipcode": "02115"
            },
          "rating": 565
        }
    },
    { "c":
        { "custid": "C37",
          "name": "T. Henry",
          "address":
            { "street": "120 Harbor Blvd.",
              "city": "St. Louis, MO",
              "zipcode": "02115"
            },
          "rating": 750
        }
    }
]

The clauses following `GROUP AS` can see the original objects by writing subqueries that iterate over the multiset `g`.

The extra level named `c` was introduced into this multiset because the groups might have been formed from a join of two or more collections. Suppose that the `FROM` clause looked like `FROM customers AS c, orders AS o`. Then each item in the group would contain both a `customers` object and an `orders` object, and these two objects might both have a field with the same name. To avoid ambiguity, the query wraps each of the original objects in an outer object that gives it the name of its iteration variable in the `FROM` clause. Consider this fragment:

FROM customers AS c, orders AS o
WHERE c.custid = o.custid
GROUP BY c.address.zipcode
GROUP AS g

In this case, following `GROUP AS g`, the clause binds variable `g` to the following collection:

[
    { "c": { an original customers object },
      "o": { an original orders object }
    },
    { "c": { another customers object },
      "o": { another orders object }
    },
    ...
]

After using `GROUP AS` to make the content of a group accessible, you typically write a subquery to access that content. You write a subquery for this purpose in the same way as any other subquery. The name specified in the `GROUP AS` clause—\`g\` in the above example—is the name of a collection of objects. You can write a `FROM` clause to iterate over the objects in the collection, and you can specify an iteration variable to represent each object in turn. For `GROUP AS` queries, this reference uses `g` as the name of the reconstituted group, and `gi` as an iteration variable representing one object inside the group. Of course, you can use any names you like for these purposes.

Now to take a look at how you might use `GROUP AS` in a query. Suppose that you want to group customers by zip code, and for each group you want to see the average credit rating and a list of the individual customers in the group. Here’s a query that does that:

##### Example Q24: GROUP AS

For each zip code, list the average credit rating in that zip code, followed by the customer numbers and names in numeric order.

```SQL++
 FROM customers AS c
 GROUP BY c.address.zipcode AS zip
 GROUP AS g
 SELECT zip, AVG(c.rating) AS `avg credit rating`,
     (FROM g AS gi
      SELECT gi.c.custid, gi.c.name
      ORDER BY gi.c.custid) AS `local customers`
 ORDER BY zip;
```

Result:

[
    {
        "avg credit rating": 625,
        "local customers": [
            {
                "custid": "C47",
                "name": "S. Logan"
            }
        ]
    },
    {
        "avg credit rating": 657.5,
        "local customers": [
            {
                "custid": "C35",
                "name": "J. Roberts"
            },
            {
                "custid": "C37",
                "name": "T. Henry"
            }
        ],
        "zip": "02115"
    },
    {
        "avg credit rating": 690,
        "local customers": [
            {
                "custid": "C25",
                "name": "M. Sinclair"
            }
        ],
        "zip": "02340"
    },
    {
        "avg credit rating": 695,
        "local customers": [
            {
                "custid": "C13",
                "name": "T. Cody"
            },
            {
                "custid": "C31",
                "name": "B. Pruitt"
            },
            {
                "custid": "C41",
                "name": "R. Dodge"
            }
        ],
        "zip": "63101"
    }
]

Notice that this query contains two `ORDER BY` clauses: one in the outer query and one in the subquery. These two clauses govern the ordering of the outer-level list of zip codes and the inner-level lists of customers, respectively. Also, notice that the group of customers with no zip code comes first in the output list.

## [](#Union%5Fall)Selection and UNION ALL

### Selection

![WithClause? QueryBlock UnionOption* OrderByClause? ( LimitClause | OffsetClause )?](_images/Selection.png) 

### UnionOption

![UNION ALL](_images/UnionOption.png) 

In a SQL++ query, the operator `UNION ALL` can connect two or more query blocks. The result of a `UNION ALL` between two query blocks contains all the items returned by the first query block, and all the items returned by the second query block. Duplicate items are not eliminated from the query result.

As in SQL, there is no ordering guarantee on the contents of the output stream. However, unlike SQL, SQL++ does not constrain what the data looks like on the input streams; in particular, it allows heterogeneity on the input and output streams. A type error results if one of the inputs is not a collection.

When you connect two or more query blocks by `UNION ALL`, you can follow them with `ORDER BY`, `LIMIT`, and `OFFSET` clauses that apply to the `UNION` query as a whole. For these clauses to be meaningful, the field-names returned by the two query blocks should match. The following example shows a `UNION ALL` of two query blocks, with an ordering specified for the result.

In this example, a customer might be selected because he has ordered more than two different items (first query block) or because he has a high credit rating (second query block). By adding an explanatory string to each query block, you can label the output objects to distinguish these two cases.

### Example Q25a: UNION ALL with labels

Find customer IDs for customers who have placed orders for more than two different items or who have a credit rating greater than 700, with labels to distinguish these cases.

```SQL++
FROM orders AS o, o.items AS i
GROUP BY o.orderno, o.custid
HAVING COUNT(*) > 2
SELECT DISTINCT o.custid AS customer_id, "Big order" AS reason

UNION ALL

FROM customers AS c
WHERE rating > 700
SELECT c.custid AS customer_id, "High rating" AS reason
ORDER BY customer_id;
```

Result:

[
    {
        "reason": "High rating",
        "customer_id": "C13"
    },
    {
        "reason": "Big order",
        "customer_id": "C37"
    },
    {
        "reason": "High rating",
        "customer_id": "C37"
    },
    {
        "reason": "Big order",
        "customer_id": "C41"
    }
]

If, on the other hand, you only want a list of the customer ids and you do not care to preserve the reasons, you can simplify your output by using `SELECT VALUE`, as follows:

### Example Q25b: UNION ALL without labels

Simplify example [Q25a](#q25a) to return a list of unlabeled customer ids.

```SQL++
FROM orders AS o, o.items AS i
GROUP BY o.orderno, o.custid
HAVING COUNT(*) > 2
SELECT VALUE o.custid

UNION ALL

FROM customers AS c
WHERE rating > 700
SELECT VALUE c.custid;
```

Result:

[
    "C37",
    "C41",
    "C13",
    "C37"
]

## [](#With%5Fclauses)WITH Clause

### WithClause

![WITH](_images/WithClause.png) 

As in standard SQL, you can use a `WITH` clause to improve the modularity of a query. A `WITH` clause often contains a subquery that computes some result that the main query uses later. In cases like this, you can think of the `WITH` clause as computing a temporary view of the input data.

The next example uses a `WITH` clause to compute the total revenue of each order in 2020; then the main part of the query finds the minimum, maximum, and average revenue for orders in that year.

### Example Q26: WITH clause

Find the minimum, maximum, and average revenue among all orders in 2020, rounded to the nearest integer.

```SQL++
 WITH order_revenue AS
     (FROM orders AS o, o.items AS i
     WHERE DATE_PART_STR(o.order_date, "year") = 2020
     GROUP BY o.orderno
     SELECT o.orderno, SUM(i.qty * i.price) AS revenue
   )
 FROM order_revenue
 SELECT AVG(revenue) AS average,
        MIN(revenue) AS minimum,
        MAX(revenue) AS maximum;
```

Result:

[
    {
        "average": 4669.99,
        "minimum": 130.45,
        "maximum": 18847.58
    }
]

`WITH` is useful when you need to use a value several times in a query.

## [](#Order%5FBy%5Fclauses)ORDER BY, LIMIT, and OFFSET Clauses

### OrderbyClause

![ORDER BY](_images/OrderbyClause.png) 

### LimitClause

![LIMIT](_images/LimitClause.png) 

### OffsetClause

![OFFSET](_images/OffsetClause.png) 

The last three clauses that a query processes are `ORDER BY`, `LIMIT`, and `OFFSET`. These clauses are optional.

The `ORDER BY` clause globally sorts data in either ascending order, `ASC`, or descending order, `DESC`.

The `NULLS` modifier determines how the system orders `MISSING` and `NULL` relative to all other values: either first with `NULLS FIRST` or last with `NULLS LAST`.

If you do not specify the `NULLS` modifier, when the system encounters `MISSING` and `NULL` in the ordering keys it treats them as being smaller any other value. If both occur in the data, the system treats `MISSING` as smaller than `NULL`. The relative order between `MISSING` and `NULL` is not affected by the `NULLS` modifier. That is, `MISSING` is still treated as smaller than `NULL`.

The ordering of values of a given type is consistent with its type’s `<=` ordering; the ordering of values across types is implementation-defined but stable.

The `LIMIT` clause limits the result set to a specified maximum size.

The optional `OFFSET` clause specifies a number of items in the output stream to discard before the query result begins. You can use `OFFSET` as a standalone clause, without the `LIMIT`.

The following example illustrates use of the `ORDER BY` and `LIMIT` clauses.

### Example Q27: ORDER BY and LIMIT clauses

Return the top three customers by rating.

```SQL++
 FROM customers AS c
 SELECT c.custid, c.name, c.rating
 ORDER BY c.rating DESC
 LIMIT 3;
```

Result:

[
    {
        "custid": "C13",
        "name": "T. Cody",
        "rating": 750
    },
    {
        "custid": "C37",
        "name": "T. Henry",
        "rating": 750
    },
    {
        "custid": "C25",
        "name": "M. Sinclair",
        "rating": 690
    }
]

You can use the `OFFSET` and `LIMIT` clauses together to paginate results, allowing you to skip a number of records (OFFSET) and control the number of records to retrieve (LIMIT).

The following example illustrates the use of `OFFSET` and `LIMIT`:

### Example Q28: OFFSET clause

Find the customer with the third-highest credit rating.

```SQL++
 FROM customers AS c
 SELECT c.custid, c.name, c.rating
 ORDER BY c.rating DESC
 LIMIT 1 OFFSET 2;

OR

 FROM customers AS c
 SELECT c.custid, c.name, c.rating
 ORDER BY c.rating DESC
 OFFSET 2 LIMIT 1;
```

Result:

[
    {
        "custid": "C25",
        "name": "M. Sinclair",
        "rating": 690
    }
]

## [](#Subqueries)Subqueries

### Subquery

![("(" Selection ")")](_images/Subquery.png) 

A subquery is denoted by parentheses. In SQL++, a subquery can appear anywhere that an expression can appear. Like any query, a subquery always returns a collection, even if the collection contains only a single value or is empty. If the subquery has a SELECT clause, it returns a collection of objects. If the subquery has a SELECT VALUE clause, it returns a collection of scalar values. If a single scalar value is expected, you can use the indexing operator `[0]` to extract the single scalar value from the collection.

### Example Q29: Subquery in SELECT clause

For every order that includes item number 120, find the order number, customer id, and customer name.

This example uses the subquery to find a customer name, given a customer id. Since the outer query expects a scalar result, the subquery uses SELECT VALUE and includes the indexing operator `[0]`.

```SQL++
 FROM orders AS o, o.items AS i
 WHERE i.itemno = 120
 SELECT o.orderno, o.custid,
     (FROM customers AS c
      WHERE c.custid = o.custid
      SELECT VALUE c.name)[0] AS name;
```

Result:

[
    {
        "orderno": 1003,
        "custid": "C31",
        "name": "B. Pruitt"
    },
    {
        "orderno": 1006,
        "custid": "C41",
        "name": "R. Dodge"
    }
]

### Example Q30: Subquery in WHERE clause

Find the customer number, name, and rating of all customers whose rating is greater than the average rating.

This example uses the subquery to find the average rating among all customers. It includes SELECT VALUE and indexing \[0\] to get a single scalar value.

```SQL++
 FROM customers AS c1
 WHERE c1.rating >
    (FROM customers AS c2
     SELECT VALUE AVG(c2.rating))[0]
 SELECT c1.custid, c1.name, c1.rating;
```

Result:

[
    {
        "custid": "C13",
        "name": "T. Cody",
        "rating": 750
    },
    {
        "custid": "C25",
        "name": "M. Sinclair",
        "rating": 690
    },
    {
        "custid": "C37",
        "name": "T. Henry",
        "rating": 750
    }
]

### Example Q31: Subquery in FROM clause

Compute the total revenue as the sum over items of quantity time price for each order. Then, find the average, maximum, and minimum total revenue over all orders.

Here, the FROM clause expects to iterate over a collection of objects, so the subquery uses an ordinary SELECT and does not need to be indexed. You might think of a FROM clause as a natural home for a subquery.

```SQL++
 FROM
    (FROM orders AS o, o.items AS i
     GROUP BY o.orderno
     SELECT o.orderno, SUM(i.qty * i.price) AS revenue
    ) AS r
 SELECT AVG(r.revenue) AS average,
        MIN(r.revenue) AS minimum,
        MAX(r.revenue) AS maximum;
```

Result:

[
    {
        "average": 4669.99,
        "minimum": 130.45,
        "maximum": 18847.58
    }
]

Notice the similarity between examples [Q26](#q26) and Q31\. This illustrates how you can often move a subquery into a `WITH` clause to improve the modularity and readability of a query.

## [](#Over%5Fclauses)OVER Clause and Window Functions

Window functions are special functions that compute aggregate values over a window of input data. Like an ordinary function, a window function returns a value for every item in the input dataset. In the case of a window function, however, the value returned by the function can depend not only on the argument of the function, but also on other items in the same collection. For example, a window function applied to a set of employees might return the rank of each employee in the set, as measured by salary. As another example, a window function applied to a set of items, ordered by purchase date, might return the running total of the cost of the items.

An `OVER` clause identifies a window function call, which can specify three things: partitioning, ordering, and framing.

* The partitioning specification is like a `GROUP BY`: it splits the input data into partitions. For example, you might partition a set of employees by department. When applied to a given object, only other objects in the same partition influence the window function.
* The ordering specification is like an `ORDER BY`: it determines the ordering of the objects in each partition.
* The framing specification defines a frame that moves through the partition, defining how the result for each object depends on nearby objects. For example, the frame for a current object might consist of the two objects before and after the current one; or it might consist of all the objects before the current one in the same partition.

A window function call can also specify some options that control, for example, how the function handles nulls.

Here is an example of a window function call:

```SQL++
 SELECT deptno, purchase_date, item, cost,
     SUM(cost) OVER (
         PARTITION BY deptno
         ORDER BY purchase_date
         ROWS UNBOUNDED PRECEDING) AS running_total_cost
 FROM purchases
 ORDER BY deptno, purchase_date;
```

This example partitions the `purchases` dataset by department number. Within each department, it orders the `purchases` by date and computes a running total cost for each item, using the frame specification `ROWS UNBOUNDED PRECEDING`. The `ORDER BY` clause in the window function is separate and independent from the `ORDER BY` clause of the query as a whole.

This section specifies the general syntax of a window function call. SQL++ supplies a set of builtin window functions. See [Window Functions](8%5Fbuiltin%5Fwin.md) for a complete list and descriptions. In addition, you can use standard SQL aggregate functions such as `SUM` and `AVG` as window functions if you use them with an `OVER` clause.

## [](#Window%5Ffunction%5Fcall)Window Function Call

### WindowFunctionCall

![WindowFunctionType "(" WindowFunctionArguments ")" WindowFunctionOptions? "OVER" (Variable "AS")? "(" WindowDefinition")"](_images/WindowFunctionCall.png) 

### WindowFunctionType

![AggregateFunction | WindowFunction](_images/WindowFunctionType.png) 

See [Aggregate Functions](8%5Fbuiltin%5Fagg.md) for a list of aggregate functions.

See [Window Functions](8%5Fbuiltin%5Fwin.md) for a list of window functions.

### [](#Window%5Ffunction%5Farguments)Window Function Arguments

![( ("DISTINCT")? Expr | (Expr ("](_images/WindowFunctionArguments.png) 

See [Aggregate Functions](8%5Fbuiltin%5Fagg.md) or the [Window Functions](8%5Fbuiltin%5Fwin.md) for details of the arguments for individual functions.

### [](#Window%5Ffunction%5Foptions)Window Function Options

![("FROM" ( "FIRST" | "LAST" ))? (( "RESPECT" | "IGNORE" ) "NULLS")?](_images/WindowFunctionOptions.png) 

You cannot use window function options with [aggregate functions](8%5Fbuiltin%5Fagg.md).

You can only use window function options with some [window functions](8%5Fbuiltin%5Fwin.md), as described below.

The **FROM modifier** determines whether the computation begins at the first or last tuple in the window. You can use this optional modifier only with the `nth_value()` function. If you omit it, the default setting is `FROM FIRST`.

The **NULLS modifier** determines whether to include or ignore NULL values in the computation. MISSING values are treated the same way as NULL values. You can use this optional modifier only with the `first_value()`, `last_value()`, `nth_value()`, `lag()`, and `lead()` functions. If you omit it, the default setting is `RESPECT NULLS`.

### [](#Window%5Fframe%5Fvariable)Window Frame Variable

The `AS` keyword enables you to specify an alias for the window frame contents. It introduces a variable to bind to the contents of the frame. When using a built-in [aggregate function](8%5Fbuiltin%5Fagg.md) as a window function, the function’s argument must be a subquery which refers to this alias, for example:

```SQL++
 SELECT ARRAY_COUNT(DISTINCT (FROM alias SELECT VALUE alias.src.field))
 OVER alias AS (PARTITION BY … ORDER BY …)
 FROM source AS src
```

The alias is not necessary when using a [Window Functions](8%5Fbuiltin%5Fwin.md), or when using a standard SQL aggregate function with the `OVER` clause.

### [](#Window%5Fdefinition)Window Definition

![WindowPartitionClause? (WindowOrderClause (WindowFrameClause WindowFrameExclusion?)?)?](_images/WindowDefinition.png) 

The **window definition** specifies the partitioning, ordering, and framing for window functions.

#### [](#Window%5Fpartition%5Fclause)Window Partition Clause

![PARTITION](_images/WindowPartitionClause.png) 

The **window partition clause** divides the tuples into logical partitions using one or more expressions.

You can use this clause with any [window function](8%5Fbuiltin%5Fwin.md), or any [aggregate function](8%5Fbuiltin%5Fagg.md) used as a window function.

This clause is optional. If you omit it, the system unites all tuples in a single partition.

#### [](#Window%5Forder%5Fclause)Window Order Clause

![ORDER](_images/WindowOrderClause.png) 

The **window order clause** determines how to order tuples within each partition. The window function works on tuples in the order specified by this clause.

You can use this clause with any [window function](8%5Fbuiltin%5Fwin.md), or any [aggregate function](8%5Fbuiltin%5Fagg.md) used as a window function.

This clause is optional. If you omit it, the system considers all tuples peers, that is, their order is a tie. When tuples in the window partition tie, each window function behaves differently.

* The `row_number()` function returns a distinct number for each tuple. If tuples tie, the results may be unpredictable.
* The `rank()`, `dense_rank()`, `percent_rank()`, and `cume_dist()` functions return the same result for each tuple.
* For other functions, if the [window frame](#Window%5Fframe%5Fclause) is defined by `ROWS`, the results may be unpredictable.

If the window frame is defined by `RANGE` or `GROUPS`, the results are the same for each tuple.

|  | This clause does not guarantee the overall order of the query results. To guarantee the order of the final results, use the query ORDER BY clause. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#Window%5Fframe%5Fclause)Window Frame Clause

![("ROWS" | "RANGE" | "GROUPS") WindowFrameExtent](_images/WindowFrameClause.png) 

The **window frame clause** defines the window frame. You can use it with all [aggregate functions](8%5Fbuiltin%5Fagg.md) and some [window functions](8%5Fbuiltin%5Fwin.md)—refer to the descriptions of individual functions for more details. You can include this optional clause only when the [window order clause](#Window%5Forder%5Fclause) is present.

* If you omit this clause and there is no [window order clause](#Window%5Forder%5Fclause), the window frame is the entire partition.
* If you omit this clause but there is a [window order clause](#Window%5Forder%5Fclause), the window frame becomes all tuples in the partition preceding the current tuple and its peers—the same as `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.

You can define the window frame in the following ways:

* `ROWS`: Counts the exact number of tuples within the frame. If window ordering doesn’t result in unique ordering, the function may produce unpredictable results. You can add a unique expression or more window ordering expressions to produce unique ordering.
* `RANGE`: Looks for a value offset within the frame. The function produces deterministic results.
* `GROUPS`: Counts all groups of tied rows within the frame. The function produces deterministic results.

|  | If this clause uses RANGE with either _Expr_ PRECEDING or _Expr_ FOLLOWING, the [window order clause](#Window%5Forder%5Fclause) must have only a single ordering term. The ordering term expression must evaluate to a number. If these conditions are not met, the result is an empty window frame, which means the window function returns its default value. In most cases this is null, except for strict\_count() or array\_count(), whose default value is 0\. This restriction does not apply when the window frame uses ROWS or GROUPS. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | The RANGE window frame is commonly used to define window frames based on date or time. If you want to use RANGE with either _Expr_ PRECEDING or _Expr_ FOLLOWING, and you want to use an ordering expression based on date or time, the expression in _Expr_ PRECEDING or _Expr_ FOLLOWING must use a data type that can be added to the ordering expression. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#Window%5Fframe%5Fextent)Window Frame Extent

![( ( "UNBOUNDED" | Expr ) "PRECEDING" | "CURRENT" "ROW" ) |  "BETWEEN" ( "UNBOUNDED" "PRECEDING" | "CURRENT" "ROW" | Expr ( "PRECEDING" | "FOLLOWING" ) ) "AND" ( "UNBOUNDED" "FOLLOWING" | "CURRENT" "ROW" | Expr ( "PRECEDING" | "FOLLOWING" ) )](_images/WindowFrameExtent.png) 

The **window frame extent clause** specifies the start point and end point of the window frame. The expression before `AND` is the start point and the expression after `AND` is the end point. If you omit `BETWEEN`, you can only specify the start point; the end point becomes `CURRENT ROW`.

The window frame end point cannot be before the start point. If this clause violates this restriction explicitly, an error results. If it violates this restriction implicitly, the result is an empty window frame, which means the window function returns its default value. In most cases this is `null`, except for `strict_count()` or `array_count()`, whose default value is 0.

Window frame extents that result in an explicit violation are:

* `BETWEEN CURRENT ROW AND` _Expr_ `PRECEDING`
* `BETWEEN` _Expr_ `FOLLOWING AND` _Expr_ `PRECEDING`
* `BETWEEN` _Expr_ `FOLLOWING AND CURRENT ROW`

Window frame extents that result in an implicit violation are:

* `BETWEEN UNBOUNDED PRECEDING AND` _Expr_ `PRECEDING`—if _Expr_ is too high, some tuples may generate an empty window frame.
* `BETWEEN` _Expr_ `PRECEDING AND` _Expr_ `PRECEDING`—if the second _Expr_ is greater than or equal to the first _Expr_, all result sets will generate an empty window frame.
* `BETWEEN` _Expr_ `FOLLOWING AND` _Expr_ `FOLLOWING`—if the first _Expr_ is greater than or equal to the second _Expr_, all result sets will generate an empty window frame.
* `BETWEEN` _Expr_ `FOLLOWING AND UNBOUNDED FOLLOWING`—if _Expr_ is too high, some tuples may generate an empty window frame.
* If the [window frame exclusion clause](#Window%5Fframe%5Fexclusion) is present, any window frame specification may result in empty window frame.

The _Expr_ must be a positive constant or an expression that evaluates as a positive number. For `ROWS` or `GROUPS`, the _Expr_ must be an integer.

#### [](#Window%5Fframe%5Fexclusion)Window Frame Exclusion

![EXCLUDE](_images/WindowFrameExclusion.png) 

The **window frame exclusion clause** enables you to exclude specified tuples from the window frame.

You can use this clause with all [aggregate functions](8%5Fbuiltin%5Fagg.md) and some [window functions](8%5Fbuiltin%5Fwin.md)—refer to the descriptions of individual functions for more details.

The [window frame clause](#Window%5Fframe%5Fclause) must be present for you to include this clause.

This clause is optional. If you omit this clause, the default is no exclusion—the same as `EXCLUDE NO OTHERS`.

* `EXCLUDE CURRENT ROW`: If the current tuple is still part of the window frame, the system removes it from the window frame.
* `EXCLUDE GROUP`: The system removes the current tuple and any peers of the current tuple from the window frame.
* `EXCLUDE TIES`: The system removes any peers of the current tuple, but not the current tuple itself, from the window frame.
* `EXCLUDE NO OTHERS`: The system does not remove any additional tuples from the window frame.

If the current tuple is already removed from the window frame, then it remains removed from the window frame.

## [](#Vs%5FSQL-92)Differences Between SQL++ and SQL-92

SQL++ offers the following additional features beyond SQL-92:

* Fully composable and functional: A subquery can iterate over any intermediate collection and can appear anywhere in a query.
* Schema-free: The query language does not assume the existence of a static schema for any data that it processes.
* Correlated `FROM` terms: A right-side `FROM` term expression can refer to variables defined by `FROM` terms on its left.
* Powerful `GROUP BY`: In addition to a set of aggregate functions as in standard SQL, the groups created by the `GROUP BY` clause are directly usable in nested queries and to obtain nested results.
* Generalized `SELECT` clause: A `SELECT` clause can return any type of collection, while in SQL-92, a `SELECT` clause has to return a homogeneous collection of objects.

The following matrix is a quick SQL-92 compatibility cheat sheet for SQL++.

| Feature               | SQL++                                                                         | SQL-92                                                                                                                                              | Why different?                                    |
| --------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| SELECT \*             | Returns nested objects                                                        | Returns flattened concatenated objects                                                                                                              | Nested collections are first class citizens       |
| Subquery              | Returns a collection                                                          | Casts the returned collection into a scalar value if the subquery appears in a SELECT list or on one side of a comparison or as input to a function | Nested collections are first class citizens       |
| LEFT OUTER JOIN       | Fills in MISSING(s) for non-matches                                           | Fills in NULL(s) for non-matches                                                                                                                    | "Absence" is more appropriate than "unknown" here |
| UNION ALL             | Allows heterogeneous inputs and output                                        | Input streams must be UNION-compatible and output field names are drawn from the first input stream                                                 | Heterogeneity and nested collections are common   |
| IN constant\_expr     | The constant expression has to be an array or multiset, that is, \[..,..,…​\] | The constant collection can be represented as comma-separated items in a paren pair                                                                 | Nested collections are first class citizens       |
| String literal        | Double quotes or single quotes                                                | Single quotes only                                                                                                                                  | Double quoted strings are pervasive in JSON       |
| Delimited identifiers | Backticks                                                                     | Double quotes                                                                                                                                       | Double quoted strings are pervasive in JSON       |

The following SQL-92 features are not implemented yet. However, SQL++ does not conflict with these features:

* CROSS JOIN, NATURAL JOIN, UNION JOIN
* FULL OUTER JOIN
* INTERSECT, EXCEPT, UNION with set semantics
* CAST expression
* ALL and SOME predicates for linking to subqueries
* UNIQUE predicate tests a collection for duplicates
* MATCH predicate tests for referential integrity
* Row and Table constructors
* Preserved order for expressions in a SELECT list

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Connecting to Data Sources](../intro/connecting-to-data-sources.md)
* [Expressions](2%5Fexpr.md)