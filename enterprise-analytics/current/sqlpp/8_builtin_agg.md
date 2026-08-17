---
title: Aggregate Functions
description: This topic contains detailed descriptions of the built-in aggregate
  functions in the query language.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/8_builtin_agg.adoc
  xref: xref:enterprise-analytics:sqlpp:8_builtin_agg.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/8_builtin_agg.html)

# Aggregate Functions

> This topic contains detailed descriptions of the built-in aggregate functions in the query language. Aggregate functions take an array—typically with a single argument—as input and produce a single, aggreagate value. 

The query language also supports standard SQL aggregate functions, for example, `MIN`, `MAX`, `SUM`, `COUNT`, and `AVG`. These are not real functions in the query language, but just syntactic sugars over corresponding builtin aggregate functions, for example, `ARRAY_MIN`, `ARRAY_MAX`, `ARRAY_SUM`, `ARRAY_COUNT`, and `ARRAY_AVG`. Refer to [Aggregation Pseudo-Functions](3%5Fquery.html#Aggregation%5FPseudoFunctions) for details.

You can use the `DISTINCT` keyword with builtin aggregate functions and standard SQL aggregate functions. You can use `DISTINCT` with aggregate functions used as window functions. It determines whether the function aggregates all values in the group, or distinct values only. Refer to [Function Calls](2%5Fexpr.html#Function%5Fcall%5Fexpressions) for details.

You can use aggregate functions as window functions when you include an OVER clause. Refer to [OVER Clauses](3%5Fquery.html#Over%5Fclauses) for details.

## [](#array%5Fcount)array\_count

* Syntax:  
array_count(collection)
* Gets the number of non-null and non-missing items in the given collection.
* Arguments:

  * `collection` could be:

    * an `array` or `multiset` to count,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `bigint` value representing the number of non-null and non-missing items in the given collection,
  * `null` if the input is `null` or `missing`,
  * any other non-array and non-multiset input value causes an error.
* Example:  
array_count( ['hello', 'world', 1, 2, 3, null, missing] );
* The expected result is:  
5

## [](#array%5Favg)array\_avg

* Syntax:  
array_avg(num_collection)
* Gets the average value of the non-null and non-missing numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the average of the non-null and non-missing numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * any other non-array and non-multiset input value causes a type error,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
array_avg( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

1.725

## [](#array%5Fsum)array\_sum

* Syntax:  
array_sum(num_collection)
* Gets the sum of non-null and non-missing items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * the sum of the non-null and non-missing numbers in the given collection. The returning type is decided by the item type with the highest order in the numeric type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among items.
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * any other non-array and non-multiset input value causes a type error,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
array_sum( [1.2, 2.3, 3.4, 0, null, missing] );
* The expected result is:

6.9

## [](#array%5Fmin)array\_min

* Syntax:  
array_min(num_collection)
* Gets the min value of non-null and non-missing comparable items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset`,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * the min value of non-null and non-missing values in the given collection. The returning type is decided by the item type with the highest order in the type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among numeric items.
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * multiple incomparable items in the input array or multiset causes a type error,
  * any other non-array and non-multiset input value causes a type error.
* Example:  
array_min( [1.2, 2.3, 3.4, 0, null, missing] );
* The expected result is:

0.0

## [](#array%5Fmax)array\_max

* Syntax:  
array_max(num_collection)
* Gets the max value of the non-null and non-missing comparable items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset`,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * the max value of non-null and non-missing numbers in the given collection. The returning type is decided by the item type with the highest order in the type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among numeric items.
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * multiple incomparable items in the input array or multiset causes a type error,
  * any other non-array and non-multiset input value causes a type error.
* Example:  
array_max( [1.2, 2.3, 3.4, 0, null, missing] );
* The expected result is:

3.4

## [](#array%5Fstddev%5Fsamp)array\_stddev\_samp

* Syntax:  
array_stddev_samp(num_collection)
* Gets the sample standard deviation value of the non-null and non-missing numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the sample standard deviation of the non-null and non-missing numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * any other non-array and non-multiset input value causes a type error,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
array_stddev_samp( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

1.4591664287073858

## [](#array%5Fstddev%5Fpop)array\_stddev\_pop

* Syntax:  
array_stddev_pop(num_collection)
* Gets the population standard deviation value of the non-null and non-missing numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the population standard deviation of the non-null and non-missing numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * any other non-array and non-multiset input value causes a type error,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
array_stddev_pop( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

1.2636751956100112

## [](#array%5Fvar%5Fsamp)array\_var\_samp

* Syntax:  
array_var_samp(num_collection)
* Gets the sample variance value of the non-null and non-missing numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the sample variance of the non-null and non-missing numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * any other non-array and non-multiset input value causes a type error,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
array_var_samp( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

2.1291666666666664

## [](#array%5Fvar%5Fpop)array\_var\_pop

* Syntax:  
array_var_pop(num_collection)
* Gets the population variance value of the non-null and non-missing numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the population variance of the non-null and non-missing numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * any other non-array and non-multiset input value causes a type error,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
array_var_pop( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

1.5968749999999998

## [](#array%5Fskewness)array\_skewness

* Syntax:  
array_skewness(num_collection)
* Gets the skewness value of the non-null and non-missing numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the skewness of the non-null and non-missing numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * any other non-array and non-multiset input value causes a type error,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
array_skewness( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

-0.04808451539164242

## [](#array%5Fkurtosis)array\_kurtosis

* Syntax:  
array_kurtosis(num_collection)
* Gets the kurtosis value from the normal distribution of the non-null and non-missing numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the kurtosis from a normal distribution of the non-null and non-missing numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if the given collection does not contain any non-null and non-missing items,
  * any other non-array and non-multiset input value causes a type error,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
array_kurtosis( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

-1.342049701096427

## [](#strict%5Fcount)strict\_count

* Syntax:  
strict_count(collection)
* Gets the number of items in the given collection.
* Arguments:

  * `collection` could be:

    * an `array` or `multiset` containing the items to count,
    * or a `null` value,
    * or a `missing` value.
* Return Value:

  * a `bigint` value representing the number of items in the given collection,
  * `null` if the input is `null` or `missing`.
* Example:  
strict_count( [1, 2, null, missing] );
* The expected result is:  
4

## [](#strict%5Favg)strict\_avg

* Syntax:  
strict_avg(num_collection)
* Gets the average value of the numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the average of the numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
strict_avg( [100, 200, 300] );
* The expected result is:

200.0

## [](#strict%5Fsum)strict\_sum

* Syntax:  
strict_sum(num_collection)
* Gets the sum of the items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * the sum of the numbers in the given collection. The returning type is decided by the item type with the highest order in the numeric type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among items.
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
strict_sum( [100, 200, 300] );
* The expected result is:  
600

## [](#strict%5Fmin)strict\_min

* Syntax:  
strict_min(num_collection)
* Gets the min value of comparable items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset`,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * the min value of the given collection. The returning type is decided by the item type with the highest order in the type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among numeric items.
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * multiple incomparable items in the input array or multiset causes a type error,
  * any other non-array and non-multiset input value causes a type error.
* Example:  
strict_min( [10.2, 100, 5] );
* The expected result is:

5.0

## [](#strict%5Fmax)strict\_max

* Syntax:  
strict_max(num_collection)
* Gets the max value of numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset`,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * The max value of the given collection. The returning type is decided by the item type with the highest order in the type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among numeric items.
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * multiple incomparable items in the input array or multiset causes a type error,
  * any other non-array and non-multiset input value causes a type error.
* Example:  
strict_max( [10.2, 100, 5] );
* The expected result is:

100.0

## [](#strict%5Fstddev%5Fsamp)strict\_stddev\_samp

* Syntax:  
strict_stddev_samp(num_collection)
* Gets the sample standard deviation value of the numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the sample standard deviation of the numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
strict_stddev_samp( [100, 200, 300] );
* The expected result is:

100.0

## [](#strict%5Fstddev%5Fpop)strict\_stddev\_pop

* Syntax:  
strict_stddev_pop(num_collection)
* Gets the population standard deviation value of the numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the population standard deviation of the numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
strict_stddev_pop( [100, 200, 300] );
* The expected result is:

81.64965809277261

## [](#strict%5Fvar%5Fsamp)strict\_var\_samp

* Syntax:  
strict_var_samp(num_collection)
* Gets the sample variance value of the numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the sample variance of the numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
strict_var_samp( [100, 200, 300] );
* The expected result is:

10000.0

## [](#strict%5Fvar%5Fpop)strict\_var\_pop

* Syntax:  
strict_var_pop(num_collection)
* Gets the population variance value of the numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the population variance of the numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
strict_var_pop( [100, 200, 300] );
* The expected result is:

6666.666666666667

## [](#strict%5Fskewness)strict\_skewness

* Syntax:  
strict_skewness(num_collection)
* Gets the skewness value of the numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the skewness of the numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
strict_skewness( [100, 200, 300] );
* The expected result is:

0.0

## [](#strict%5Fkurtosis)strict\_kurtosis

* Syntax:  
strict_kurtosis(num_collection)
* Gets the kurtosis value from the normal distribution of the numeric items in the given collection.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` containing numeric values, `null`s or `missing`s,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `double` value representing the kurtosis from a normal distribution of the numbers in the given collection,
  * `null` if the input is `null` or `missing`,
  * `null` if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection causes a type error.
* Example:  
strict_kurtosis( [100, 200, 300] );
* The expected result is:

-1.5