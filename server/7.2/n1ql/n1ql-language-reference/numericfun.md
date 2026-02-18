---
title: Number Functions
description: Number functions are functions that are performed on a numeric field.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/numericfun.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/n1ql/n1ql-language-reference/numericfun.html)

# Number Functions

Number functions are functions that are performed on a numeric field.

## [](#absexpression)ABS(expression)

### [](#description)Description

Returns absolute value of the number.

## [](#acosexpression)ACOS(expression)

### [](#description-2)Description

Returns arc cosine in radians.

## [](#asinexpression)ASIN(expression)

### [](#description-3)Description

Returns arc sine in radians.

## [](#atanexpression)ATAN(expression)

### [](#description-4)Description

Returns arc tangent in radians.

## [](#atan2expression1-expression2)ATAN2(expression1, expression2)

### [](#description-5)Description

Returns arc tangent of expression2/expression1.

## [](#ceilexpression)CEIL(expression)

### [](#description-6)Description

Returns smallest integer not less than the number.

## [](#cosexpression)COS(expression)

### [](#description-7)Description

Returns cosine.

## [](#degreesexpression)DEGREES(expression)

### [](#description-8)Description

Returns radians to degrees.

## [](#e)E()

### [](#description-9)Description

Base of natural logarithms.

## [](#expexpression)EXP(expression)

### [](#description-10)Description

Returns eexpression.

## [](#lnexpression)LN(expression)

### [](#description-11)Description

Returns log base e.

## [](#logexpression)LOG(expression)

### [](#description-12)Description

Returns log base 10.

## [](#floorexpression)FLOOR(expression)

### [](#description-13)Description

Largest integer that is not greater than the number.

## [](#pi)PI()

Returns PI.

## [](#powerexpression1-expression2)POWER(expression1, expression2)

### [](#description-14)Description

Returns expression1expression2.

## [](#radiansexpression)RADIANS(expression)

### [](#description-15)Description

Returns degrees to radians.

## [](#random-expression)RANDOM(\[ expression \])

### [](#description-16)Description

Returns pseudo-random number with optional seed.

## [](#roundexpression-digits)ROUND(expression \[, digits \])

### [](#description-17)Description

Rounds the value to the given number of integer digits to the right of the decimal point (left if `digits` is negative). `Digits` is zero if not given.

## [](#signexpression)SIGN(expression)

### [](#description-18)Description

Valid values: -1, 0, or 1 for negative, zero, or positive numbers respectively.

## [](#sinexpression)SIN(expression)

### [](#description-19)Description

Returns sine.

## [](#sqrtexpression)SQRT(expression)

### [](#description-20)Description

Returns square root.

## [](#tanexpression)TAN(expression)

### [](#description-21)Description

Returns tangent.

## [](#truncexpression-digits)TRUNC(expression \[, digits \])

### [](#description-22)Description

Truncates the number to the given number of integer digits to the right of the decimal point (left if `digits` is negative). `Digits` is zero if not given.

### [](#example)Example

Query

```sqlpp
SELECT
    AVG(reviews.rating) / 5 AS normalizedRating,
    ROUND((avg(reviews.rating) / 5), 2) AS roundedRating,
    TRUNC((avg(reviews.rating) / 5), 3) AS truncRating
    FROM reviews AS reviews
    WHERE reviews.customerId = "customer62"
```

Returns

Result

```json
{
   "results": [
     {
       "normalizedRating": 0.42000000000000004,
       "roundedRating": 0.42,
       "truncRating": 0.42
     }
   ]
 }
```