---
title: Analytics Views
description: A description of Analytics views and Tabular Analytics views.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/8.0/modules/analytics/pages/5a_views.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:analytics:5a_views.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/analytics/5a_views.html)

# Analytics Views

Analytics views are virtual Analytics collections that are derived from actual stored Analytics collections. Analytics views might be used to present a subset of the stored data, or to present a join or other transformation of stored data for some particular purpose. Queries may operate on Analytics views in exactly the same way as they do on real stored data — in fact, a query might refer to both a stored Analytics collection and an Analytics view, perhaps joining them together. Analytics views are not materialized. When a query refers to an Analytics view, the definition of the view is merged with the query to produce the desired result.

Most of the examples in this section assume that you are using an Analytics scope called `Commerce`. Refer to [Appendix 4: Example Data](appendix%5F4%5Fexamples.md) to install this example data.

You can use the [USE statement](5%5Fddl.md#Use%5Fstatements)to set the default scope for the statement immediately following.

Example

USE Commerce;

Alternatively, use the **query context** drop-down list at the top right of the Query Editor to select `Commerce` as the default scope for the following examples.

![The query context drop-down menu with 'Commerce' selected](_images/workbench-context-set.png) 

## [](#creating-an-analytics-view)Creating an Analytics View

An Analytics view is created by a CREATE statement with the following syntax:

##### CreateView

!["CREATE" ("OR" "REPLACE")? "ANALYTICS" "VIEW" ViewName ("IF" "NOT" "EXISTS")? "AS" ViewDefn](_images/diagrams/CreateView.png) 

##### ViewName

![QualifiedName](_images/diagrams/ViewName.png) 

##### ViewDefn

![QualifiedName | Selection](_images/diagrams/ViewDefn.png) 

The CREATE ANALYTICS VIEW statement simply specifies the name of the view (`QualifiedName`) and the definition of the view. The view definition may be the `QualifiedName` of an Analytics collection or another Analytics view, or (more likely) it may be a query that defines the content of the view. The view-defining query must conform to the syntax of a `Selection` — in other words, it is a query that may include optional features such as WITH, UNION, and SELECT VALUE.

The `QualifiedName` of the view to be created consists of an optional Analytics scope name followed by an identifier. If the `QualifiedName` contains a scope name, the view is created within the specified Analytics scope. Otherwise, the view is created in the scope defined by the immediately preceding USE statement, or the scope defined by the `query_context` parameter, or the `Default` Analytics scope, according to the rules for [Resolving Database Entities](appendix%5F3%5Fresolution.md#Resolving%5Fdatabase%5Fentities).

The scope where the view is created becomes the default scope for resolving names in the `ViewDefn` expression or query (the "body" of the view definition).

Analytics views share the same namespace as Analytics collections. This means that a view cannot be created with the same name as another view or collection in the same Analytics scope. However, views and collections do not share the same namespace as synonyms; a synonym can coexist with a view or collection with the same name in the same Analytics scope. In this case, the view or collection takes precedence over the synonym.

The OR REPLACE and IF NOT EXISTS clauses specify the action to take if an Analytics view already exists with the specified name, as follows:

* If neither OR REPLACE nor IF NOT EXISTS is specified, an error is raised.
* If only OR REPLACE is specified, the existing view definition is replaced with the new one.
* If only IF NOT EXISTS is specified, the statement is ignored and the existing view definition is retained.
* If both of these clauses are specified, an error is raised because the clauses contradict each other.

##### Examples

The examples shown here are based on the Commerce data in [Appendix 4: Example Data](appendix%5F4%5Fexamples.md).

The following Analytics view operates on the `customers` Analytics collection, showing the `custid`, `name`, and `rating` of each customer whose rating is greater than 700, omitting the customer’s address.

CREATE ANALYTICS VIEW good_customers AS
    SELECT custid, name, rating
    FROM customers
    WHERE rating > 700;

The following Analytics view unnests ("flattens") the items in each order and aggregates them to compute the total revenue for each order.

CREATE ANALYTICS VIEW orders_summary AS
   SELECT o.orderno, o.order_date, o.custid, sum(i.qty * i.price) AS revenue
   FROM orders AS o UNNEST o.items AS i
   GROUP BY o.orderno, o.order_date, o.custid;

The Analytics view in the previous example might be used in the following query, which lists orders in the year 2020 that had more than 1000 in total revenue, in descending order by revenue.

SELECT s.orderno, s.order_date, s.revenue
FROM orders_summary AS s
WHERE date_part_str(s.order_date, "year") = 2020
AND s.revenue > 1000
ORDER BY revenue DESC;

Metadata for Analytics views can be found in the `` Metadata.`Dataset` `` collection, identified by `DatasetType = "VIEW"`. Analytics views and Analytics tabular views are also displayed in the insights sidebar to the right of the Analytics Workbench.

## [](#tabular-analytics-views)Tabular Analytics Views

A Tabular Analytics view (abbreviated here as TAV) is a special kind of Analytics view that enables Couchbase Analytics to interact with software tools that are designed for relational databases. A TAV always presents data in the form of a table with uniform rows and columns and with a well-defined schema. Like any Analytics view, a TAV can be queried by an ordinary SQL++ for Analytics query. But, because its data is presented in the form of tables, a TAV is also accessible to relational tools.

Currently, Couchbase Analytics provides a [Connector for the Tableau tool](../../../tableau-connector/current/index.md)that is used to visualize relational data. The Connector enables Tableau to execute SQL queries against TAVs. In the future, additional Connectors may be provided to make TAVs accessible to other relational tools.

A TAV is created by a CREATE ANALYTICS VIEW statement with certain additional clauses, using the following syntax:

##### CreateTabularView

!["CREATE" ("OR" "REPLACE")? "ANALYTICS" "VIEW" ViewName "(" ViewSchema ")""( "IF" "NOT" "EXISTS")? "DEFAULT" "NULL" (DateTimeFormatSpecification)? (PrimaryKeyDefn)? (ForeignKeyDefn)? "AS" ViewDefn](_images/diagrams/CreateTabularView.png) 

##### ViewSchema

![ColumnName ViewTypeRef ("NOT" "UNKNOWN")? ( "," ColumnName ViewTypeRef ("NOT" "UNKNOWN")? )*](_images/diagrams/ViewSchema.png) 

##### ColumnName

![Identifier](_images/diagrams/ColumnName.png) 

##### ViewTypeRef

!["BOOLEAN" | "BIGINT" | "INT" | "DOUBLE" | "STRING" | "DATE" | "TIME" | "DATETIME"](_images/diagrams/ViewTypeRef.png) 

##### DateTimeFormatSpec

![("DATE" StringLiteral)? ("TIME" StringLiteral)? ("DATETIME" StringLiteral)?](_images/diagrams/DateTimeFormatSpec.png) 

##### PrimaryKeyDefn

!["PRIMARY" "KEY" "(" ColumnName ( "," ColumnName )* ")" "NOT" "ENFORCED"](_images/diagrams/PrimaryKeyDefn.png) 

##### ForeignKeyDefn

!["FOREIGN" "KEY" "(" ColumnName ( "," ColumnName )* ")" "REFERENCES" QualifiedName "NOT" "ENFORCED"](_images/diagrams/ForeignKeyDefn.png) 

The clauses that are in common with an ordinary CREATE ANALYTICS VIEW statement are handled in the usual way. The additional clauses are handled as follows.

**ViewSchema**

This clause identifies the view as a TAV and specifies the column names of the resulting table and their datatypes. The following datatypes are supported in TAVs:

`BOOLEAN`  
`STRING`  
`BIGINT` (synonym `INT`)  
`DOUBLE`  
`DATE` (includes date only, no timezone)  
`TIME` (includes time only, no timezone)  
`DATETIME` (includes date and time, no timezone)

The data values returned by the view definition query are cast into the datatypes specified in the `ViewSchema`. Whenever this casting process fails, a NULL value is returned and a warning is raised. However, columns that are designated NOT UNKNOWN in the `ViewSchema` may not contain NULL or MISSING values. Any row in which a NULL or MISSING value would appear in a NOT UNKNOWN column is excluded from the view.

Columns that are included in the PRIMARY KEY clause are automatically treated as NOT UNKNOWN columns.

**DEFAULT NULL**

This required clause documents the fact that missing data values are replaced by NULL, unless NOT UNKNOWN is specified. This convention is required because relational databases use NULL to represent missing values.

**DateTimeFormatSpec**

This clause specifies the format in which values are represented in columns of type DATE, TIME, and/or DATETIME. Permissible formats, based on the ISO 8601 Standard, are described in [Temporal Formats](../n1ql/n1ql-language-reference/datefun.md#date-formats). If no explicit formats are specified, the default formats are as follows:

For DATE columns: `"YYYY-MM-DD"`  
For TIME columns: `"hh:mm:ss.s"`  
For DATETIME columns: `"YYYY-MM-DDThh:mm:ss.s"`

Timezones appearing in TIME or DATETIME values are ignored.

**PRIMARY KEY** and **FOREIGN KEY**

These optional clauses allow the view definer to specify which columns in the TAV serve as primary or foreign keys. This information can be accessed and exploited by tools like the Tableau Connector. However, the primary and foreign key relationships are not enforced by Couchbase Analytics. The clause NOT ENFORCED is required in primary and foreign key specifications. The `QualifiedName` following REFERENCES in a FOREIGN KEY clause must be the name of a TAV. Self-references are allowed — for example, the `manager` field in an `employee` view might be a foreign key referencing another row in the `employee` view.

**ViewDefn**

The view definition body (usually a query) is handled in the same way as in an ordinary CREATE ANALYTICS VIEW statement. However, the view definition must generate tabular data with column names that match the column names in the `ViewSchema`, and the values in these columns must be castable into the types specified in the `ViewSchema`. (If the casting process fails, a NULL value is returned, or the row is excluded if NOT UNKNOWN is specified.) The correspondence between the column names in the `ViewSchema` and the column names generated by the `ViewDefn` is based on name-matching, not on relative position. In other words, each column in the `ViewSchema` must have a column in the `ViewDefn` with the same name and a compatible (castable) type, but the columns need not be in the same order.

##### Examples

The simplest form of a TAV simply makes an existing Analytics collection available to be queried by relational tools. This is possible if the existing collection already has a tabular form — that is, it consists of an array of objects with no nested arrays or nested objects.

Suppose that an Analytics collection named `staff` contains the following data:

```json
[
  { "empno": 105, "name": "B. Happy", "hiredate": "03/15/2021"},
  { "empno": 107, "name": "Y. Knott", "hiredate": "06/30/2021"}
]
```

This collection could be made available to SQL queries by creating the following TAV. In this view definition, the `DATE` clause is necessary because dates are stored in the nonstandard format `MM/DD/YYYY`instead of the standard ISO 8601 format. Note how the view definition provides the schema information that is expected by relational tools.

CREATE OR REPLACE ANALYTICS VIEW staff_table (
   empno BIGINT,
   name STRING,
   hiredate DATE
)
DEFAULT NULL
DATE "MM/DD/YYYY"
AS staff;

Data that includes nested objects can be made accessible to relational tools by TAVs that convert the nested data into tabular form, using a process called _normalization_. The following examples illustrate normalization techniques, using the Commerce data in [Appendix 4: Example Data](appendix%5F4%5Fexamples.md).

If each object in a collection directly contains a nested object, that nested object can easily be "flattened", as illustrated in the definition of `customers_view`, which flattens the `address` object into three fields named `addr_street`, `addr_city`, and `addr_zipcode`.

CREATE OR REPLACE ANALYTICS VIEW customers_view (
   custid STRING, name STRING, rating BIGINT,
   adr_street STRING, adr_city STRING, adr_zipcode STRING)
DEFAULT NULL
PRIMARY KEY (custid) NOT ENFORCED
AS
   SELECT custid, name, rating, address.street AS adr_street,
      address.city AS adr_city, address.zipcode AS adr_zipcode
   FROM customers;

If each object in a collection contains a nested array of objects, the nested array can be removed from the main view table and put into a side view table that is linked to the main table by a foreign key. This technique — common in traditional relational schema design — is illustrated by the following view definitions in which the `items` array is moved from `orders` into a separate table.

CREATE OR REPLACE ANALYTICS VIEW orders_view (
   orderno BIGINT, custid STRING, order_date DATE, ship_date DATE)
DEFAULT NULL
PRIMARY KEY (orderno) NOT ENFORCED
FOREIGN KEY (custid) REFERENCES customers_view NOT ENFORCED
AS
  SELECT orderno, custid, order_date, ship_date
  FROM orders;

CREATE OR REPLACE ANALYTICS VIEW items_view (
   orderno BIGINT, itemno BIGINT, qty BIGINT, price DOUBLE)
DEFAULT NULL
PRIMARY KEY (orderno, itemno) NOT ENFORCED
FOREIGN KEY (orderno) REFERENCES orders_view NOT ENFORCED
AS
  SELECT o.orderno, i.itemno, i.qty, i.price
  FROM orders AS o UNNEST o.items AS i;

The resulting normalized tabular view schema can then be used by Tableau as if it were stored relational data. This includes, of course, the possibility of referencing TAVs in queries produced by user actions in Tableau.

## [](#using-indexes-with-analytics-views)Using Indexes with Analytics Views

Indexes can be used to improve performance of queries on Analytics views, including TAVs. The index must be created on the underlying Analytics collection rather than on the view itself. More details about the creation and use of indexes in Analytics can be found in [Using Indexes](7%5Fusing%5Findex.md).

When creating an index to support a TAV, an additional CAST clause should be specified in the CREATE INDEX statement. This clause specifies that data values are to be cast into the specified type before indexing them, and that, if the cast fails, the data value is indexed as NULL. The CAST clause may also specify the format in which a DATE, TIME, or TIMESTAMP is represented if it is other than the standard ISO 8601.

##### IndexCastDefault

!["CAST" "(" "DEFAULT" "NULL" DateTimeFormatSpecification? ")"](_images/diagrams/IndexCastDefault.png) 

##### Examples

The `orders_summary` Analytics view, defined above, is based on the `orders` collection and contains a `custid` field. The following statement creates an index on the `custid` field of the underlying collection. This index might improve performance of queries that search for the orders of a particular customer, either through the `orders` table or through the `orders_summary` view. This example does not require a CAST clause because `orders_summary` is not a Tabular Analytics view (TAV).

CREATE INDEX idx1 ON orders(custid:STRING);

The index created in the following example might improve the performance of queries against either the `staff`collection or the Tabular Analytics view named `staff_table` (defined above), when searching for staff members hired on a particular date. The `DATE` clause in this statement is needed because `hiredate` values are stored in a nonstandard format.

CREATE INDEX idx2 ON staff(hiredate:DATE) CAST(DEFAULT NULL DATE "MM/DD/YYYY");

## [](#dropping-an-analytics-view)Dropping an Analytics View

Any Analytics view (including a TAV) can be dropped using the following statement:

##### DropView

!["DROP" "ANALYTICS" "VIEW" QualifiedName ("IF" "EXISTS")?](_images/diagrams/DropView.png) 

The `QualifiedName` identifies the Analytics view to be dropped.

The target scope (Analytics scope containing the view to be dropped) is identified as follows:

1. The scope specified in the `QualifiedName`, if any;
2. The scope named in the immediately preceding USE statement, if any;
3. The scope defined by the `query_context` parameter, or the `Default` Analytics scope, according to the rules for [Resolving Database Entities](appendix%5F3%5Fresolution.md#Resolving%5Fdatabase%5Fentities).

If the target scope does not exist, the DROP statement fails.

If the target scope exists but does not contain a view with the specified name, the DROP statement fails unless IF EXISTS is specified.

If an Analytics collection with the same name exists in the target scope, the DROP statement fails.

If an existing view or user-defined function depends on the view to be dropped, the DROP statement fails.

When an Analytics view is dropped, its descriptive metadata is deleted from the `` Metadata.`Dataset` ``collection, and the Analytics view is removed from the insights sidebar to the right of the Analytics Workbench.