---
title: Builtin Functions
description: A description of Couchbase SQL++ for Analytics builtin functions.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/8_builtin.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:analytics:8_builtin.adoc[]
---

[View original HTML](/server/7.2/analytics/8_builtin.html)

# Builtin Functions

Some of the examples in this section assume that you are using an Analytics scope called `Commerce`. Refer to [Appendix 4: Example Data](appendix%5F4%5Fexamples.md) to install this example data.

You can use the [USE statement](5%5Fddl.md#Use%5Fstatements)to set the default scope for the statement immediately following.

Example

USE Commerce;

Alternatively, use the **query context** drop-down list at the top right of the Query Editor to select `Commerce` as the default scope for the following examples.

![The query context drop-down menu with 'Commerce' selected](_images/workbench-context-set.png) 

## [](#NumericFunctions)Numeric Functions

### [](#abs)abs

* Syntax:  
abs(numeric_value)
* Computes the absolute value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * The absolute value of the argument with the same type as the input argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": abs(2013), "v2": abs(-4036), "v3": abs(0), "v4": abs(float("-2013.5")), "v5": abs(double("-2013.593823748327284")) };
* The expected result is:  
{ "v1": 2013, "v2": 4036, "v3": 0, "v4": 2013.5, "v5": 2013.5938237483274 }

### [](#acos)acos

* Syntax:  
acos(numeric_value)
* Computes the arc cosine value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` arc cosine in radians for the argument, if the argument is in the range of -1 (inclusive) to 1 (inclusive),
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error,
  * "NaN" for other legitimate numeric values.
* Example:  
{ "v1": acos(1), "v2": acos(2), "v3": acos(0), "v4": acos(float("0.5")), "v5": acos(double("-0.5")) };
* The expected result is:  
{ "v1": 0.0, "v2": "NaN", "v3": 1.5707963267948966, "v4": 1.0471975511965979, "v5": 2.0943951023931957 }

### [](#asin)asin

* Syntax:  
asin(numeric_value)
* Computes the arc sine value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` arc sin in radians for the argument, if the argument is in the range of -1 (inclusive) to 1 (inclusive),
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error,
  * "NaN" for other legitimate numeric values.
* Example:  
{ "v1": asin(1), "v2": asin(2), "v3": asin(0), "v4": asin(float("0.5")), "v5": asin(double("-0.5")) };
* The expected result is:  
{ "v1": 1.5707963267948966, "v2": "NaN", "v3": 0.0, "v4": 0.5235987755982989, "v5": -0.5235987755982989 }

### [](#atan)atan

* Syntax:  
atan(numeric_value)
* Computes the arc tangent value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` arc tangent in radians for the argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": atan(1), "v2": atan(2), "v3": atan(0), "v4": atan(float("0.5")), "v5": atan(double("1000")) };
* The expected result is:  
{ "v1": 0.7853981633974483, "v2": 1.1071487177940904, "v3": 0.0, "v4": 0.4636476090008061, "v5": 1.5697963271282298 }

### [](#atan2)atan2

* Syntax:  
atan2(numeric_value1, numeric_value2)
* Computes the arc tangent value of numeric\_value2/numeric\_value1.
* Arguments:

  * `numeric_value1`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * `numeric_value2`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` arc tangent in radians for `numeric_value1` and `numeric_value2`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": atan2(1, 2), "v2": atan2(0, 4), "v3": atan2(float("0.5"), double("-0.5")) };
* The expected result is:  
{ "v1": 0.4636476090008061, "v2": 0.0, "v3": 2.356194490192345 }

### [](#ceil)ceil

* Syntax:  
ceil(numeric_value)
* Computes the smallest (closest to negative infinity) number with no fractional part that is not less than the value of the argument. If the argument is already equal to mathematical integer, then the result is the same as the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * The ceiling value for the given number in the same type as the input argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{  
  "v1": ceil(2013),  
  "v2": ceil(-4036),  
  "v3": ceil(0.3),  
  "v4": ceil(float("-2013.2")),  
  "v5": ceil(double("-2013.893823748327284"))  
};
* The expected result is:  
{ "v1": 2013, "v2": -4036, "v3": 1.0, "v4": -2013.0, "v5": -2013.0 }

### [](#cos)cos

* Syntax:  
cos(numeric_value)
* Computes the cosine value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` cosine value for the argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": cos(1), "v2": cos(2), "v3": cos(0), "v4": cos(float("0.5")), "v5": cos(double("1000")) };
* The expected result is:  
{ "v1": 0.5403023058681398, "v2": -0.4161468365471424, "v3": 1.0, "v4": 0.8775825618903728, "v5": 0.562379076290703 }

### [](#cosh)cosh

* Syntax:  
cosh(numeric_value)
* Computes the hyperbolic cosine value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` hyperbolic cosine value for the argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": cosh(1), "v2": cosh(2), "v3": cosh(0), "v4": cosh(float("0.5")), "v5": cosh(double("8")) };
* The expected result is:  
{ "v1": 1.5430806348152437, "v2": 3.7621956910836314, "v3": 1.0, "v4": 1.1276259652063807, "v5": 1490.479161252178 }

### [](#degrees)degrees

* Syntax:  
degrees(numeric_value)
* Converts radians to degrees
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * The degrees value for the given radians value. The returned value has type `double`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": degrees(pi()) };
* The expected result is:  
{ "v1": 180.0 }

### [](#e)e

* Syntax:  
e()
* Return Value:

  * e (base of the natural logarithm)
* Example:  
{ "v1": e() };
* The expected result is:  
{ "v1": 2.718281828459045 }

### [](#exp)exp

* Syntax:  
exp(numeric_value)
* Computes enumeric\_value.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * enumeric\_value,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": exp(1), "v2": exp(2), "v3": exp(0), "v4": exp(float("0.5")), "v5": exp(double("1000")) };
* The expected result is:  
{ "v1": 2.718281828459045, "v2": 7.38905609893065, "v3": 1.0, "v4": 1.6487212707001282, "v5": "Infinity" }

### [](#floor)floor

* Syntax:  
floor(numeric_value)
* Computes the largest (closest to positive infinity) number with no fractional part that is not greater than the value. If the argument is already equal to mathematical integer, then the result is the same as the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * The floor value for the given number in the same type as the input argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{  
  "v1": floor(2013),  
  "v2": floor(-4036),  
  "v3": floor(0.8),  
  "v4": floor(float("-2013.2")),  
  "v5": floor(double("-2013.893823748327284"))  
};
* The expected result is:  
{ "v1": 2013, "v2": -4036, "v3": 0.0, "v4": -2014.0, "v5": -2014.0 }

### [](#ln)ln

* Syntax:  
ln(numeric_value)
* Computes logenumeric\_value.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * logenumeric\_value,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": ln(1), "v2": ln(2), "v3": ln(0), "v4": ln(float("0.5")), "v5": ln(double("1000")) };
* The expected result is:  
{ "v1": 0.0, "v2": 0.6931471805599453, "v3": "-Infinity", "v4": -0.6931471805599453, "v5": 6.907755278982137 }

### [](#log)log

* Syntax:  
log(numeric_value)
* Computes log10numeric\_value.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * log10numeric\_value,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": log(1), "v2": log(2), "v3": log(0), "v4": log(float("0.5")), "v5": log(double("1000")) };
* The expected result is:  
{ "v1": 0.0, "v2": 0.3010299956639812, "v3": "-Infinity", "v4": -0.3010299956639812, "v5": 3.0 }

### [](#pi)pi

* Syntax:  
pi()
* Return Value:

  * Pi
* Example:  
{ "v1": pi() };
* The expected result is:  
{ "v1": 3.141592653589793 }

### [](#power)power

* Syntax:  
power(numeric_value1, numeric_value2)
* Computes numeric\_value1numeric\_value2.
* Arguments:

  * `numeric_value1`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * `numeric_value2`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * numeric\_value1numeric\_value2,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": power(1, 2), "v3": power(0, 4), "v4": power(float("0.5"), double("-0.5")) };
* The expected result is:  
{ "v1": 1, "v3": 0, "v4": 1.4142135623730951 }

### [](#radians)radians

* Syntax:  
radians(numeric_value)
* Converts degrees to radians
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * The radians value for the given degrees value. The returned value has type `double`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": radians(180) };
* The expected result is:  
{ "v1": 3.141592653589793 }

### [](#round)round

* Syntax:  
round(numeric_value[, round_digit])
* Rounds the value to the given number of integer digits to the right of the decimal point, or to the left of the decimal point if the number of digits is negative.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value that represents the numeric value to be rounded.
  * `round_digit`: (Optional) a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value that specifies the digit to round to. This argument may be positive or negative; positive indicating that rounding needs to be to the right of the decimal point, and negative indicating that rounding needs to be to the left of the decimal point. Values such as 1.0 and 2.0 are acceptable, but values such as 1.3 and 1.5 result in a `null`. If omitted, the default is 0.
* Return Value:

  * The rounded value for the given number. The returned value has the following type:

    * `bigint` if the input value has type `tinyint`, `smallint`, `integer` or `bigint`,
    * `float` if the input value has type `float`,
    * `double` if the input value has type `double`;
  * `missing` if the input value is a `missing` value,
  * `null` if the input value is a `null` value,
  * any other non-numeric input value will return a `null` value.
* Example:  
{  
  "v1": round(2013),  
  "v2": round(-4036),  
  "v3": round(0.8),  
  "v4": round(float("-2013.256")),  
  "v5": round(double("-2013.893823748327284"))  
  "v6": round(123456, -1),  
  "v7": round(456.456, 2),  
  "v8": round(456.456, -1),  
  "v9": round(-456.456, -2)  
};
* The expected result is:  
{ "v1": 2013, "v2": -4036, "v3": 1.0, "v4": -2013.0, "v5": -2014.0, "v6": 123460, "v7": 456.46, "v8": 460, "v9": -500 }

### [](#sign)sign

* Syntax:  
sign(numeric_value)
* Computes the sign of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the sign (a `tinyint`) of the argument, -1 for negative values, 0 for 0, and 1 for positive values,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": sign(1), "v2": sign(2), "v3": sign(0), "v4": sign(float("0.5")), "v5": sign(double("-1000")) };
* The expected result is:  
{ "v1": 1, "v2": 1, "v3": 0, "v4": 1, "v5": -1 }

### [](#sin)sin

* Syntax:  
sin(numeric_value)
* Computes the sine value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` sine value for the argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": sin(1), "v2": sin(2), "v3": sin(0), "v4": sin(float("0.5")), "v5": sin(double("1000")) };
* The expected result is:  
{ "v1": 0.8414709848078965, "v2": 0.9092974268256817, "v3": 0.0, "v4": 0.479425538604203, "v5": 0.8268795405320025 }

### [](#sinh)sinh

* Syntax:  
sinh(numeric_value)
* Computes the hyperbolic sine value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` hyperbolic sine value for the argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": sinh(1), "v2": sinh(2), "v3": sinh(0), "v4": sinh(float("0.5")), "v5": sinh(double("8")) };
* The expected result is:  
{ "v1": 1.1752011936438014, "v2": 3.626860407847019, "v3": 0.0, "v4": 0.5210953054937474, "v5": 1490.4788257895502 }

### [](#sqrt)sqrt

* Syntax:  
sqrt(numeric_value)
* Computes the square root of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` square root value for the argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": sqrt(1), "v2": sqrt(2), "v3": sqrt(0), "v4": sqrt(float("0.5")), "v5": sqrt(double("1000")) };
* The expected result is:  
{ "v1": 1.0, "v2": 1.4142135623730951, "v3": 0.0, "v4": 0.7071067811865476, "v5": 31.622776601683793 }

### [](#tan)tan

* Syntax:  
tan(numeric_value)
* Computes the tangent value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` tangent value for the argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": tan(1), "v2": tan(2), "v3": tan(0), "v4": tan(float("0.5")), "v5": tan(double("1000")) };
* The expected result is:  
{ "v1": 1.5574077246549023, "v2": -2.185039863261519, "v3": 0.0, "v4": 0.5463024898437905, "v5": 1.4703241557027185 }

### [](#tanh)tanh

* Syntax:  
tanh(numeric_value)
* Computes the hyperbolic tangent value of the argument.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value.
* Return Value:

  * the `double` hyperbolic tangent value for the argument,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": tanh(1), "v2": tanh(2), "v3": tanh(0), "v4": tanh(float("0.5")), "v5": tanh(double("8")) };
* The expected result is:  
{ "v1": 0.7615941559557649, "v2": 0.964027580075817, "v3": 0.0, "v4": 0.4621171572600098, "v5": 0.999999774929676 }

### [](#trunc)trunc

* Syntax:  
trunc(numeric_value, number_digits)
* Truncates the number to the given number of integer digits to the right of the decimal point (left if digits is negative). Digits is 0 if not given.
* Arguments:

  * `numeric_value`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * `number_digits`: a `tinyint`/`smallint`/`integer`/`bigint` value.
* Return Value:

  * the `double` tangent value for the argument,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is `missing`,
  * a type error will be raised if:

    * the first argument is any other non-numeric value,
    * the second argument is any other non-tinyint, non-smallint, non-integer, and non-bigint value.
* Example:  
{ "v1": trunc(1, 1), "v2": trunc(2, -2), "v3": trunc(0.122, 2), "v4": trunc(float("11.52"), -1), "v5": trunc(double("1000.5252"), 3) };
* The expected result is:  
{ "v1": 1, "v2": 2, "v3": 0.12, "v4": 10.0, "v5": 1000.525 }

### [](#random)random

* Syntax:  
random([expr])
* Returns a pseudo-random number with optional seed.
* Arguments:

  * `expr`: A number, or an expression that evaluates to a number.
* Return Value:

  * Returns a number between 0 and 1.
  * Returns NULL if `expr` is not a number.
* Example:  
random(123);
* A possible result is:

0.029199439979853525

## [](#StringFunctions)String Functions

### [](#concat)concat

* Syntax:  
concat(string1, string2, ...)
* Returns a concatenated string from arguments.
* Arguments:

  * `string1`: a string value,
  * `string2`: a string value,
  * …​.
* Return Value:

  * a concatenated string from arguments,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value will cause a type error.
* Example:  
concat("test ", "driven ", "development");
* The expected result is:  
"test driven development"

### [](#contains)contains

* Syntax:  
contains(string, substring_to_contain)
* Checks whether the string `string` contains the string `substring_to_contain`
* Arguments:

  * `string` : a `string` that might contain the given substring,
  * `substring_to_contain` : a target `string` that might be contained.
* Return Value:

  * a `boolean` value, `true` if `string` contains `substring_to_contain`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value will cause a type error,
  * `false` otherwise.
* Example:  
{ "v1": contains("I like x-phone", "phone"), "v2": contains("one", "phone") };
* The expected result is:  
{ "v1": true, "v2": false }

### [](#ends%5Fwith)ends\_with

* Syntax:  
ends_with(string, substring_to_end_with)
* Checks whether the string `string` ends with the string `substring_to_end_with`.
* Arguments:

  * `string` : a `string` that might end with the given string,
  * `substring_to_end_with` : a `string` that might be contained as the ending substring.
* Return Value:

  * a `boolean` value, `true` if `string` contains `substring_to_contain`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value will cause a type error,
  * `false` otherwise.
* Example:  
{  
  "v1": ends_with(" love product-b its shortcut_menu is awesome:)", ":)"),  
  "v2": ends_with(" awsome:)", ":-)")  
};
* The expected result is:  
{ "v1": true, "v2": false }

### [](#initcap-or-title)initcap (or title)

* Syntax:  
initcap(string)
* Converts a given string `string` so that the first letter of each word is uppercase and every other letter is lowercase. The function has an alias called "title".
* Arguments:

  * `string` : a `string` to be converted.
* Return Value:

  * a `string` as the title form of the given `string`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value will cause a type error.
* Example:  
{ "v1": initcap("ANALYTICS is here!"), "v2": title("ANALYTICS is here!") };
* The expected result is:  
{ "v1": "Analytics Is Here!", "v2": "Analytics Is Here!" }

### [](#length)length

* Syntax:  
length(string)
* Returns the length of the string `string`. Note that the length is in the unit of code point. See the following examples for more details.
* Arguments:

  * `string` : a `string` or `null` that represents the string to be checked.
* Return Value:

  * an `bigint` that represents the length of `string`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value will cause a type error.
* Example:  
length("test string");
* The expected result is:  
11
* Example:  
length("👩‍👩‍👧‍👦");
* The expected result is (the emoji character 👩‍👩‍👧‍👦 has 7 code points):  
7

### [](#lower)lower

* Syntax:  
lower(string)
* Converts a given string `string` to its lowercase form.
* Arguments:

  * `string` : a `string` to be converted.
* Return Value:

  * a `string` as the lowercase form of the given `string`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value will cause a type error.
* Example:  
lower("ANALYTICS");
* The expected result is:  
"analytics"

### [](#ltrim)ltrim

* Syntax:  
ltrim(string[, chars]);
* Returns a new string with all leading characters that appear in `chars` removed. By default, white space is the character to trim. Note that here one character means one code point. For example, the emoji 4-people-family notation "👩‍👩‍👧‍👦" contains 7 code points, and it is possible to trim a few code points (such as a 2-people-family "👨‍👦") from it. See the following example for more details.
* Arguments:

  * `string` : a `string` to be trimmed,
  * `chars` : a `string` that contains characters that are used to trim.
* Return Value:

  * a trimmed, new `string`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value will cause a type error.
* Related functions: see `trim()`, `rtrim()`
* Example:  
ltrim("me like x-phone", "eml");
* The expected result is:  
" like x-phone"
* Example with multi-codepoint notation (trim the man and boy from the family of man, woman, girl and boy):  
ltrim("👨‍👩‍👧‍👦", "👨‍👦")
* The expected result is (only woman, girl and boy are left in the family):  
"👩‍👧‍👦"

### [](#position)position

* Syntax:  
position(string, string_pattern)
* Returns the first position of `string_pattern` within `string`. The result is counted in the unit of code points. See the following example for more details.
* The function returns the 0-based position. Another version of the function returns the 1-based position. Below are the aliases for each version:

  * 0-based: `position`, `pos`, `position0`, `pos0`.
  * 1-based: `position1`, `pos1`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` to be matched.
* Return Value:

  * the first position that `string_pattern` appears within `string`(starting at 0), or -1 if it does not appear,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value will return a `null`.
* Example:  
{  
  "v1": position("ppphonepp", "phone"),  
  "v2": position("hone", "phone"),  
  "v3": position1("ppphonepp", "phone"),  
  "v4": position1("hone", "phone")  
};
* The expected result is:  
{ "v1": 2, "v2": -1, v3": 3, "v4": -1 }
* Example of multi-code-point character:  
position("👩‍👩‍👧‍👦🏀", "🏀");
* The expected result is (the emoji family character has 7 code points):  
7

### [](#regexp%5Fcontains)regexp\_contains

* Syntax:  
regexp_contains(string, string_pattern[, string_flags])
* Checks whether the strings `string` contains the regular expression pattern `string_pattern` (a Java regular expression pattern).
* Aliases:

  * `regexp_contains`, `regex_contains`, `contains_regexp`, `contains_regex`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` to be matched.
  * `string_flag` : (Optional) a `string` with flags to be used during regular expression matching.

    * The following modes are enabled with these flags: dotall (s), multiline (m), case\_insensitive (i), and comments and whitespace (x).
* Return Value:

  * a `boolean`, returns `true` if `string` contains the pattern `string_pattern`, `false` otherwise.
  * `missing` if any argument is a `missing` value.
  * `null` if any argument is a `null` value but no argument is a `missing` value.
  * any other non-string input value will return a `null`.
* Example:  
{  
  "v1": regexp_contains("pphonepp", "p*hone"),  
  "v2": regexp_contains("hone", "p+hone")  
};
* The expected result is:  
{ "v1": true, "v2": false }

### [](#regexp%5Flike)regexp\_like

* Syntax:  
regexp_like(string, string_pattern[, string_flags])
* Checks whether the string `string` exactly matches the regular expression pattern `string_pattern`(a Java regular expression pattern).
* Aliases:

  * `regexp_like`, `regex_like`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` that might be contained.
  * `string_flag` : (Optional) a `string` with flags to be used during regular expression matching.

    * The following modes are enabled with these flags: dotall (s), multiline (m), case\_insensitive (i), and comments and whitespace (x).
* Return Value:

  * a `boolean` value, `true` if `string` contains the pattern `string_pattern`, `false` otherwise.
  * `missing` if any argument is a `missing` value.
  * `null` if any argument is a `null` value but no argument is a `missing` value.
  * any other non-string input value will return a `null`.
* Example:  
{  
  "v1": regexp_like(" can't stand acast the network is horrible:(", ".*acast.*"),  
  "v2": regexp_like("acast", ".*acst.*")  
};
* The expected result is:  
{ "v1": true, "v2": false }

### [](#regexp%5Fposition)regexp\_position

* Syntax:  
regexp_position(string, string_pattern[, string_flags])
* Returns first position of the regular expression `string_pattern` (a Java regular expression pattern) within `string`. The function returns the 0-based position. Another version of the function returns the 1-based position. Below are the aliases for each version:
* Aliases:

  * 0-Based: `regexp_position`, `regexp_pos`, `regexp_position0`, `regexp_pos0`, `regex_position`, `regex_pos`, `regex_position0`, `regex_pos0`.
  * 1-Based: `regexp_position1`, `regexp_pos1`, `regex_position1` `regex_pos1`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` to be matched.
  * `string_flag` : (Optional) a `string` with flags to be used during regular expression matching.

    * The following modes are enabled with these flags: dotall (s), multiline (m), case\_insensitive (i), and comments and whitespace (x).
* Return Value:

  * the first position that the regular expression `string_pattern` appears in `string`(starting at 0), or -1 if it does not appear.
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value will return a `null`.
* Example:  
{  
  "v1": regexp_position("pphonepp", "p*hone"),  
  "v2": regexp_position("hone", "p+hone"),  
  "v3": regexp_position1("pphonepp", "p*hone"),  
  "v4": regexp_position1("hone", "p+hone")  
};
* The expected result is:  
{ "v1": 0, "v2": -1, "v3": 1, "v4": -1 }

### [](#regexp%5Freplace)regexp\_replace

* Syntax:  
regexp_replace(string, string_pattern, string_replacement[, string_flags])  
regexp_replace(string, string_pattern, string_replacement[, replacement_limit])
* Checks whether the string `string` matches the given regular expression pattern `string_pattern` (a Java regular expression pattern), and replaces the matched pattern `string_pattern` with the new pattern `string_replacement`.
* Aliases:

  * `regexp_replace`, `regex_replace`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` to be matched.
  * `string_replacement` : a pattern `string` to be used as the replacement.
  * `string_flag` : (Optional) a `string` with flags to be used during replace.

    * The following modes are enabled with these flags: dotall (s), multiline (m), case\_insensitive (i), and comments and whitespace (x).
  * `replacement_limit`: (Optional) an `integer` specifying the maximum number of replacements to make (if negative then all occurrences will be replaced)
* Return Value:

  * Returns a `string` that is obtained after the replacements.
  * `missing` if any argument is a `missing` value.
  * `null` if any argument is a `null` value but no argument is a `missing` value.
  * any other non-string input value will return a `null`.
* Example:  
regexp_replace(" like x-phone the voicemail_service is awesome", " like x-phone", "like product-a");
* The expected result is:  
"like product-a the voicemail_service is awesome"

### [](#repeat)repeat

* Syntax:  
repeat(string, n)
* Returns a string formed by repeating the input `string` `n` times.
* Arguments:

  * `string` : a `string` to be repeated,
  * `n` : an `tinyint`/`smallint`/`integer`/`bigint` value - how many times the string should be repeated.
* Return Value:

  * a string that repeats the input `string` `n` times,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * a type error will be raised if:

    * the first argument is any other non-string value,
    * or, the second argument is not a `tinyint`, `smallint`, `integer`, or `bigint`.
* Example:  
repeat("test", 3);
* The expected result is:  
"testtesttest"

### [](#replace)replace

* Syntax:  
replace(string, search_string, replacement_string[, limit])
* Finds occurrences of the given substring `search_string` in the input string `string`and replaces them with the new substring `replacement_string`.
* Arguments:

  * `string` : an input `string`,
  * `search_string` : a `string` substring to be searched for,
  * `replacement_string` : a `string` to be used as the replacement,
  * `limit` : (Optional) an `integer` \- maximum number of occurrences to be replaced. If not specified or negative then all occurrences will be replaced
* Return Value:

  * Returns a `string` that is obtained after the replacements,
  * `missing` if any argument is a `missing` value,
  * any other non-string input value or non-integer `limit` will cause a type error,
  * `null` if any argument is a `null` value but no argument is a `missing` value.
* Example:  
{  
  "v1": replace(" like x-phone the voicemail_service is awesome", " like x-phone", "like product-a"),  
  "v2": replace("x-phone and x-phone", "x-phone", "product-a", 1)  
};
* The expected result is:  
{  
  "v1": "like product-a the voicemail_service is awesome",  
  "v2": "product-a and x-phone"  
}

### [](#reverse)reverse

* Syntax:  
reverse(string)
* Returns a string formed by reversing characters in the input `string`. For characters of multiple code points, code point is the minimal unit to reverse. See the following examples for more details.
* Arguments:

  * `string` : a `string` to be reversed
* Return Value:

  * a string containing characters from the the input `string` in the reverse order,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * a type error will be raised if:

    * the first argument is any other non-string value
* Example:  
reverse("hello");
* The expected result is:  
"olleh"
* Example of multi-code-point character (Korean):  
reverse("한글");
* The expected result is (the Korean characters are splitted into code points and then the code points are reversed):  
"ᆯᅳᄀᆫᅡᄒ"

### [](#rtrim)rtrim

* Syntax:  
rtrim(string[, chars]);
* Returns a new string with all trailing characters that appear in `chars` removed. By default, white space is the character to trim. Note that here one character means one code point. For example, the emoji 4-people-family notation "👩‍👩‍👧‍👦" contains 7 code points, and it is possible to trim a few code points (such as a 2-people-family "👨‍👦") from it. See the following example for more details.
* Arguments:

  * `string` : a `string` to be trimmed,
  * `chars` : a `string` that contains characters that are used to trim.
* Return Value:

  * a trimmed, new `string`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value will cause a type error.
* Related functions: see `trim()`, `ltrim()`
* Example:  
{  
  "v1": rtrim("i like x-phone", "x-phone"),  
  "v2": rtrim("i like x-phone", "onexph")  
};
* The expected result is:  
{ "v1": "i like ", "v2": "i like x-" }
* Example with multi-codepoint notation (trim the man and boy from the family of man, woman, girl and boy):  
rtrim("👨‍👩‍👧‍👦", "👨‍👦")
* The expected result is (only man, woman and girl are left in the family):  
"👨‍👩‍👧"

### [](#split)split

* Syntax:  
split(string, sep)
* Splits the input `string` into an array of substrings separated by the string `sep`.
* Arguments:

  * `string` : a `string` to be split.
* Return Value:

  * an array of substrings by splitting the input `string` by `sep`,
  * in case of two consecutive `sep`s in the `string`, the result of splitting the two consecutive `sep`s will be the empty string `""`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value will cause a type error.
* Example:  
split("test driven development", " ");
* The expected result is:  
[ "test", "driven", "development" ]
* Example with two consecutive `sep`s in the `string`:  
split("123//456", "/");
* The expected result is:  
[ "123", "", "456" ]

### [](#starts%5Fwith)starts\_with

* Syntax:  
starts_with(string, substring_to_start_with)
* Checks whether the string `string` starts with the string `substring_to_start_with`.
* Arguments:

  * `string` : a `string` that might start with the given string.
  * `substring_to_start_with` : a `string` that might be contained as the starting substring.
* Return Value:

  * a `boolean`, returns `true` if `string` starts with the string `substring_to_start_with`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value will cause a type error,
  * `false` otherwise.
* Example:  
{  
  "v1" : starts_with(" like the plan, amazing", " like"),  
  "v2" : starts_with("I like the plan, amazing", " like")  
};
* The expected result is:  
{ "v1": true, "v2": false }

### [](#substr)substr

* Syntax:  
substr(string, offset[, length])
* Returns the substring from the given string `string` based on the given start offset `offset` with the optional `length`. Note that both of the `offset` and `length` are in the unit of code point (e.g. the emoji family 👨‍👩‍👧‍👦 has 7 code points). The function uses the 0-based position. Another version of the function uses the 1-based position. Below are the aliases for each version:
* Aliases:

  * 0-Based: `substring`, `substr`, `substring0`, `substr0`.
  * 1-Based: `substring1`, `substr1`.
* Arguments:

  * `string` : a `string` to be extracted.
  * `offset` : an `tinyint`/`smallint`/`integer`/`bigint` value as the starting offset of the substring in `string`(starting at 0). If negative then counted from the end of the string.
  * `length` : (Optional) an an `tinyint`/`smallint`/`integer`/`bigint` value as the length of the substring.
* Return Value:

  * a `string` that represents the substring,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value, or if the substring could not be obtained because the starting offset is not within string bounds or `length` is negative.
  * a `null` will be returned if:

    * the first argument is any other non-string value.
    * the second argument is not a `tinyint`, `smallint`, `integer`, or `bigint`.
    * the third argument is not a `tinyint`, `smallint`, `integer`, or `bigint` if the argument is present.
* Example:  
{ "v1": substr("test string", 6, 3), "v2": substr1("test string", 6, 3) };
* The expected result is:  
{ "v1": "tri", "v2": "str" }

The function has an alias `substring`.

### [](#trim)trim

* Syntax:  
trim(string[, chars]);
* Returns a new string with all leading and trailing characters that appear in `chars` removed. By default, white space is the character to trim. Note that here one character means one code point. For example, the emoji 4-people-family notation "👩‍👩‍👧‍👦" contains 7 code points, and it is possible to trim a few code points (such as a 2-people-family "👨‍👦") from it. See the following example for more details.
* Arguments:

  * `string` : a `string` to be trimmed,
  * `chars` : a `string` that contains characters that are used to trim.
* Return Value:

  * a trimmed, new `string`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value will cause a type error.
* Related functions: see `ltrim()`, `rtrim()`
* Example:  
trim("i like x-phone", "xphoen");
* The expected result is:  
" like "
* Example with multi-codepoint notation (trim the man and boy from the family of man, woman, girl and boy):  
trim("👨‍👩‍👧‍👦", "👨‍👦")
* The expected result is (only woman and girl are left in the family):  
"👩‍👧"

### [](#upper)upper

* Syntax:  
upper(string)
* Converts a given string `string` to its uppercase form.
* Arguments:

  * `string` : a `string` to be converted.
* Return Value:

  * a `string` as the uppercase form of the given `string`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value will cause a type error.
* Example:  
upper("hello")
* The expected result is:  
"HELLO"

### [](#concat2)concat2

* Syntax:  
concat2(string_separator, string_or_array_of_strings1, string_or_array_of_strings2, ...)
* This function takes the input strings, or arrays of strings, and concatenates them with the specified separator between each input string. Arrays of strings are flattened and concatenated in the same order. If there is only a single string argument, the separator is not used.
* Arguments:

  * `string_separator`: a string value representing the separator to use between the concatenated strings.
  * `string_or_array_of_strings1`: a string or an array of strings to be concatenated.
  * …​.
* Return Value:

  * a concatenated string from arguments with separator between each argument.
  * `missing` if any argument is a `missing` value.
  * `missing` if an array is provided, and any element in the array is `missing`.
  * `null` if any argument (or any array element) is a `null` but no argument (or any array element) is a `missing`value.
  * any other non-string input value will return a `null`.
* Example:  
concat2("-", "ab", "cd", ["e", "f", "g"]);
* The expected result is:  
"ab-cd-e-f-g"

## [](#TemporalFunctions)Temporal Functions

Note that in SQL++ for Analytics, temporal functions only support ISO-8601 example date formats. They do not support date string codes, Go reference dates, or percent-style dates, which are supported by SQL++ for Query.

### [](#datefun%5F%5Ffn-date-now-local)now\_local (clock\_local)

* Syntax:  
now_local([fmt])
* The current time (at query compilation time) on the node that compiled the query, in the specified string format.
* Arguments:

  * `fmt`: A string, or an expression which evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string) to use for the result.  
  This argument is optional. If no format or an incorrect format is specified, it defaults to the combined full date and time.
* Return Value:

  * A date string in the format specified representing the local system time.
* Example:  
{"full_date":    now_local(),  
 "invalid_date": now_local('invalid date'),  
 "short_date":   now_local('1111-11-11')};
* The expected result is:  
{  
  "full_date": "2018-09-07T14:16:35.233+01:00",  
  "invalid_date": "2018-09-07T14:16:35.233+01:00",  
  "short_date": "2018-09-07"  
}

The function has an alias `clock_local`.

### [](#datefun%5F%5Ffn-date-now-millis)now\_millis (clock\_millis)

* Syntax:  
now_millis()
* The current time (at query compilation time) on the node that compiled the query, as an Epoch/UNIX timestamp.
* Arguments:  
None.
* Return Value:

  * An integer representing the system time as Epoch/UNIX time in milliseconds.
* Example:  
{"CurrentTime": now_millis()};
* The expected result is:  
{  
  "CurrentTime": 1536326726276  
}

The function has an alias `clock_millis`.

### [](#datefun%5F%5Ffn-date-now-str)now\_str (clock\_str)

* Syntax:  
now_str([fmt])
* The current time (at query compilation time) on the node that compiled the query, in the specified string format.
* Arguments:

  * `fmt`: A string, or an expression which evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string) to use the result.  
  This argument is optional. If no format or an incorrect format is specified, it defaults to the combined full date and time.
* Return Value:

  * A date string in the format specified representing the system time.
* Example:  
{"full_date":    now_str(),  
 "invalid_date": now_str('invalid date'),  
 "short_date":   now_str('1111-11-11')};
* The expected result is:  
{  
  "full_date": "2018-09-07T14:26:01.115+01:00",  
  "invalid_date": "2018-09-07T14:26:01.115+01:00",  
  "short_date": "2018-09-07"  
}

The function has an alias `clock_str`.

### [](#datefun%5F%5Ffn-date-now-tz)now\_tz (clock\_tz)

* Syntax:  
now_tz(tz [, fmt])
* The current time (at query compilation time) in the timezone given by the timezone argument passed to the function. This time is the local system time converted to the specified timezone.  
As this function converts the local time, it may not accurately represent the true time in that timezone.
* Arguments:

  * `tz`: A string, or an expression which evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.md#date-timezone) to convert the local time to.  
  If this argument is not a valid timezone then `null` is returned as the result.
  * `fmt`: A string, or an expression which evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string) to use for the result.  
  This argument is optional. If no format or an incorrect format is specified, it defaults to the combined full date and time.
* Return Value:

  * An date string in the format specified representing the system time in the specified timezone.
* Example:  
{"UTC_full_date":    now_tz('UTC'),  
 "UTC_short_date":   now_tz('UTC', '1111-11-11'),  
 "invalid_timezone": now_tz('invalid timezone'),  
 "us_east":          now_tz('US/Eastern'),  
 "us_west":          now_tz('US/Pacific')};
* The expected result is:  
{  
  "UTC_full_date": "2018-09-07T13:26:47.956Z",  
  "UTC_short_date": "2018-09-07",  
  "invalid_timezone": null,  
  "us_east": "2018-09-07T09:26:47.956-04:00",  
  "us_west": "2018-09-07T06:26:47.956-07:00"  
}

The function has an alias `clock_tz`.

### [](#datefun%5F%5Ffn-date-now-utc)now\_utc (clock\_utc)

* Syntax:  
now_utc([fmt])
* The current time in UTC. This time is the local system time converted to UTC. This function is provided for convenience and is the same as `now_tz('UTC')`.
* Arguments:

  * `fmt`: A string, or an expression which evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string) to use for the result.  
  This argument is optional. If no format or an incorrect format is specified, it defaults to the combined full date and time.
* Return Value:

  * An date string in the format specified representing the system time in UTC.
* Example:  
{"full_date":  now_utc(),  
 "short_date": now_utc('1111-11-11')};
* The expected result is:  
{  
  "full_date": "2018-09-07T13:27:40.693Z",  
  "short_date": "2018-09-07"  
}

The function has an alias `clock_utc`.

### [](#datefun%5F%5Ffn-date-add-millis)date\_add\_millis

* Syntax:  
date_add_millis(date1, n, part)
* Performs date arithmetic on a particular component of an Epoch/UNIX timestamp value. This calculation is specified by the arguments `n` and `part`. For example, a value of 3 for `n` and a value of `day` for `part` would add 3 days to the date specified by `date1`.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds.  
  If this argument is not an integer then `null` is returned.
  * `n`: The value to increment the date component by. This value must be an integer, or an expression which evaluates to an integer, and may be negative to perform date subtraction.  
  If a non-integer is passed to the function then `null` is returned.
  * `part`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function then `null` is returned.
* Return Value:

  * An integer, representing the result of the calculation as an Epoch/UNIX timestamp in milliseconds.
* Example:  
{"add_3_days":  date_add_millis(1463284740000,  3, 'day'),  
 "add_3_years": date_add_millis(1463284740000,  3, 'year'),  
 "sub_3_days":  date_add_millis(1463284740000, -3, 'day'),  
 "sub_3_years": date_add_millis(1463284740000, -3, 'year')};
* The expected result is:  
{  
  "add_3_days": 1463543940000,  
  "add_3_years": 1557892740000,  
  "sub_3_days": 1463025540000,  
  "sub_3_years": 1368590340000  
}

### [](#datefun%5F%5Ffn-date-add-str)date\_add\_str

* Syntax:  
date_add_str(date1, n, part)
* Performs date arithmetic on a date string. This calculation is specified by the arguments `n` and `part`. For example a value of 3 for `n` and a value of `day` for `part` would add 3 days to the date specified by `date1`.
* Arguments:

  * `date1`: A string, or an expression which evaluates to a string, representing the date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string).
  * `n`: The value to increment the date component by. This value must be an integer, or an expression which evaluates to an integer, and may be negative to perform date subtraction.  
  If a non-integer is passed to the function then `null` is returned.
  * `part`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function then `null` is returned.
* Return Value:

  * An integer representing the result of the calculation as an Epoch/UNIX timestamp in milliseconds.
* Example:  
{"add_3_days":  date_add_str('2016-05-15 03:59:00Z',  3, 'day'),  
 "add_3_years": date_add_str('2016-05-15 03:59:00Z',  3, 'year'),  
 "sub_3_days":  date_add_str('2016-05-15 03:59:00Z', -3, 'day'),  
 "sub_3_years": date_add_str('2016-05-15 03:59:00Z', -3, 'year')};
* The expected result is:  
{  
  "add_3_days": "2016-05-18T03:59:00Z",  
  "add_3_years": "2019-05-15T03:59:00Z",  
  "sub_3_days": "2016-05-12T03:59:00Z",  
  "sub_3_years": "2013-05-15T03:59:00Z"  
}

### [](#datefun%5F%5Ffn-date-diff-millis)date\_diff\_millis

* Syntax:  
date_diff_millis(date1, date2, part)
* Finds the elapsed time between two Epoch/UNIX timestamps. This elapsed time is measured from the date specified by `date2` to the date specified by `date1`. If `date1` is greater than `date2`, then the value returned is positive, otherwise the value returned is negative.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds.  
  If this argument is not an integer, then `null` is returned.
  * `date2`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value that is subtracted from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function, then `null` is returned.
* Return Value:

  * An integer representing the elapsed time (based on the specified `part`) between both dates.
* Example:  
{"add_3_days":  date_diff_millis(1463543940000, 1463284740000, 'day'),  
 "add_3_years": date_diff_millis(1557892740000, 1463284740000, 'year'),  
 "sub_3_days":  date_diff_millis(1463025540000, 1463284740000, 'day'),  
 "sub_3_years": date_diff_millis(1368590340000, 1463284740000, 'year')};
* The expected result is:  
{  
  "add_3_days": 3,  
  "add_3_years": 3,  
  "sub_3_days": -3,  
  "sub_3_years": -3  
}

### [](#datefun%5F%5Ffn-date-diff-str)date\_diff\_str

* Syntax:  
date_diff_str(date1, date2, part)
* Finds the elapsed time between two dates specified as formatted strings. This elapsed time is measured from the date specified by `date2` to the date specified by `date1`. If `date1` is greater than `date2` then the value returned is positive, otherwise the value returned is negative.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value that is subtracted from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `date2`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value that is subtracted from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function, then `null` is returned.
* Return Value:

  * An integer representing the elapsed time (based on the specified `part`) between both dates.
* Example:  
{"add_3_days":  date_diff_str('2016-05-18T03:59:00Z', '2016-05-15 03:59:00Z', 'day'),  
 "add_3_years": date_diff_str('2019-05-15T03:59:00Z', '2016-05-15 03:59:00Z', 'year'),  
 "sub_3_days":  date_diff_str('2016-05-12T03:59:00Z', '2016-05-15 03:59:00Z', 'day'),  
 "sub_3_years": date_diff_str('2013-05-15T03:59:00Z', '2016-05-15 03:59:00Z', 'year')};
* The expected result is:  
{  
  "add_3_days": 3,  
  "add_3_years": 3,  
  "sub_3_days": -3,  
  "sub_3_years": -3  
}

### [](#datefun%5F%5Ffn-date-format-str)date\_format\_str

* Syntax:  
date_format_str(date1, fmt)
* Converts datetime strings from one supported date string format to a different supported date string format.
* Arguments:

  * `date1`: A string, or an expression which evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string).  
  If this argument is not a valid date string then `null` is returned.
  * `fmt`: A string, or an expression which evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string) to use for the result.  
  If an incorrect format is specified, it defaults to the combined full date and time.
* Return Value:

  * A date string in the format specified.
* Example:  
{"full_to_short": date_format_str('2016-05-15T00:00:23+00:00', '1111-11-11'),  
 "short_to_full": date_format_str('2016-05-15', '1111-11-11T00:00:00+00:00'),  
 "time_to_full":  date_format_str('01:10:05', '1111-11-11T01:01:01Z')};
* The expected result is:  
{  
  "full_to_short": "2016-05-15",  
  "short_to_full": "2016-05-15T00:00:00+01:00",  
  "time_to_full": "0000-01-01T01:10:05Z"  
}

### [](#datefun%5F%5Ffn-date-part-millis)date\_part\_millis

* Syntax:  
date_part_millis(date1, part [, tz])
* Extracts the value of a given date component from an Epoch/UNIX timestamp value.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value that is subtracted from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function, then `null` is returned.
  * `tz`: A string, or an expression which evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.md#date-timezone) to convert the local time to.  
  This argument is optional. If not specified, it defaults to the system timezone. If an incorrect time zone is provided, then `null` is returned.
* Return Value:

  * An integer representing the value of the component extracted from the timestamp.
* Example:  
{"day_local": date_part_millis(1463284740000, 'day'),  
 "day_pst":   date_part_millis(1463284740000, 'day', 'America/Tijuana'),  
 "day_utc":   date_part_millis(1463284740000, 'day', 'UTC'),  
 "month":     date_part_millis(1463284740000, 'month'),  
 "week":      date_part_millis(1463284740000, 'week'),  
 "year":      date_part_millis(1463284740000, 'year')};
* The expected result is:  
{  
  "day_local": 15,  
  "day_pst": 14,  
  "day_utc": 15,  
  "month": 5,  
  "week": 20,  
  "year": 2016  
}

### [](#datefun%5F%5Ffn-date-part-str)date\_part\_str

* Syntax:  
date_part_str(date1, part)
* Extracts the value of a given date component from a date string.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value that is subtracted from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function, then `null` is returned.
* Return Value:

  * An integer representing the value of the component extracted from the timestamp.
* Example:  
{"day":         date_part_str('2016-05-15T03:59:00Z', 'day'),  
 "millisecond": date_part_str('2016-05-15T03:59:00Z', 'millisecond'),  
 "month":       date_part_str('2016-05-15T03:59:00Z', 'month'),  
 "week":        date_part_str('2016-05-15T03:59:00Z', 'week'),  
 "year":        date_part_str('2016-05-15T03:59:00Z', 'year')};
* The expected result is:  
{  
  "day": 15,  
  "millisecond": 0,  
  "month": 5,  
  "week": 20,  
  "year": 2016  
}

### [](#datefun%5F%5Ffn-date-range-millis)date\_range\_millis

* Syntax:  
date_range_millis(date1, date2, part [,n])
* Generates an array of dates from the start date specified by `date1` and the end date specified by `date2`, as Epoch/UNIX timestamps. The difference between each subsequent generated date can be adjusted.  
It is possible to generate very large arrays using this function. In some cases the query engine may be unable to process all of these and cause excessive resource consumption. It is therefore recommended that you first validate the inputs to this function to ensure that the generated result is a reasonable size.  
If the start date is greater than the end date passed to the function then an error is not thrown, but the result array is empty. An array of descending dates can be generated by setting the start date greater than the end date and specifying a negative value for `n`.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value that is subtracted from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `date2`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value that is subtracted from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function, then `null` is returned.
  * `n`: An integer, or an expression which evaluates to an integer, representing the value by which to increment the part component for each generated date.  
  This argument is optional. If not specified, it defaults to 1\. If a value which is not an integer is specified, then `null` is returned.
* Return Value:

  * An array of integers representing the generated dates, as Epoch/UNIX timestamps, between `date1` and `date2`.
* Example:  
{"range_of_milliseconds_by_month":          date_range_millis(1480752000000, 1475478000000, 'month', -1),  
 "range_of_milliseconds_by_previous_month": date_range_millis(1480752000000, 1449129600000, 'month', -1)};
* The expected result is:  
{  
  "range_of_milliseconds_by_month": [  
    1480752000000,  
    1478160000000  
  ],  
  "range_of_milliseconds_by_previous_month": [  
    1480752000000,  
    1478160000000,  
    1475478000000,  
    1472886000000,  
    1470207600000,  
    1467529200000,  
    1464937200000,  
    1462258800000,  
    1459666800000,  
    1456992000000,  
    1454486400000,  
    1451808000000  
  ]  
}

### [](#datefun%5F%5Ffn-date-range-str)date\_range\_str

* Syntax:  
date_range_str(start_date, end_date, date_interval [, quantity_int ])
* Generates an array of date strings between the start date and end date, calculated by the interval and quantity values. The input dates can be in any of the [supported date formats](../n1ql/n1ql-language-reference/datefun.md#date-formats).  
It is possible to generate very large arrays using this function. In some cases the query engine may be unable to process all of these and cause excessive resource consumption. It is therefore recommended that you first validate the inputs of this function to ensure that the generated result is a reasonable size.  
If the `start_date` is greater than the `end_date`, an error is not thrown, but the result array is empty. An array of descending dates can be generated by setting the `start_date` greater than the `end_date` and specifying a negative value for `quantity_number`.  
Both specified dates must have the same string format, otherwise `null` is returned. To ensure that both dates have the same format, you should use [date\_format\_str()](#datefun%5F%5Ffn-date-format-str).
* Arguments:

  * `start_date`: A string, or an expression which evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string). This is the date used as the start date of the array generation.  
  If this argument is not an integer, then `null` is returned.
  * `end_date`: A string, or an expression which evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string). This is the date used as the end date of the array generation. This value is exclusive, that is, the end date is not included in the result.  
  If this argument is not an integer, then `null` is returned.
  * `date_interval`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function, then `null` is returned.
  * `quantity_int`: An integer, or an expression which evaluates to an integer, representing the value by which to increment the interval component for each generated date.  
  This argument is optional. If not specified, it defaults to 1\. If a value which is not an integer is specified, then `null` is returned.
* Return Value:

  * An array of strings representing the generated dates, as date strings, between `start_date` and `end_date`.
* Example:  
{"ranges_by_quarters":      date_range_str('2015-11-30T15:04:05.999', '2017-04-14T15:04:06.998', 'quarter'),  
 "ranges_by_single_day":    date_range_str('2016-01-01T15:04:05.999', '2016-01-05T15:04:05.998', 'day', 1),  
 "ranges_by_four_months":   date_range_str('2018-01-01','2019-01-01', 'month', 4),  
 "ranges_by_previous_days": date_range_str('2016-01-05T15:04:05.999', '2016-01-01T15:04:06.998', 'day', -1),  
 "ranges_by_month":         date_range_str('2015-01-01T01:01:01', '2015-12-11T00:00:00', 'month', 1)};
* The expected result is:  
{  
  "ranges_by_quarters": [  
    "2015-11-30T15:04:05.999",  
    "2016-02-29T15:04:05.999",  
    "2016-05-29T15:04:05.999",  
    "2016-08-29T15:04:05.999",  
    "2016-11-29T15:04:05.999",  
    "2017-02-28T15:04:05.999"  
  ],  
  "ranges_by_single_day": [  
    "2016-01-01T15:04:05.999",  
    "2016-01-02T15:04:05.999",  
    "2016-01-03T15:04:05.999",  
    "2016-01-04T15:04:05.999"  
  ],  
  "ranges_by_four_months": [  
    "2018-01-01",  
    "2018-05-01",  
    "2018-09-01"  
  ],  
  "ranges_by_previous_days": [  
    "2016-01-05T15:04:05.999",  
    "2016-01-04T15:04:05.999",  
    "2016-01-03T15:04:05.999",  
    "2016-01-02T15:04:05.999"  
  ],  
  "ranges_by_month": [  
    "2015-01-01T01:01:01",  
    "2015-02-01T01:01:01",  
    "2015-03-01T01:01:01",  
    "2015-04-01T01:01:01",  
    "2015-05-01T01:01:01",  
    "2015-06-01T01:01:01",  
    "2015-07-01T01:01:01",  
    "2015-08-01T01:01:01",  
    "2015-09-01T01:01:01",  
    "2015-10-01T01:01:01",  
    "2015-11-01T01:01:01",  
    "2015-12-01T01:01:01"  
  ]  
}

### [](#datefun%5F%5Ffn-date-trunc-millis)date\_trunc\_millis

* Syntax:  
date_trunc_millis(date1, part)
* Truncates an Epoch/UNIX timestamp up to the specified date component.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the date used as the date to truncate.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) to truncate to.  
  If an invalid part is specified, then `null` is returned.
* Return Value:

  * An integer representing the truncated timestamp in Epoch/UNIX time.
* Example:  
{"day":   date_trunc_millis(1463284740000, 'day'),  
 "month": date_trunc_millis(1463284740000, 'month'),  
 "year":  date_trunc_millis(1463284740000, 'year')};
* The expected result is:  
{  
  "day": 1463270400000,  
  "month": 1462060800000,  
  "year": 1451606400000  
}

### [](#datefun%5F%5Ffn-date-trunc-str)date\_trunc\_str

* Syntax:  
date_trunc_str(date1, part)
* Truncates a date string up to the specified date component.
* Arguments:

  * `date1`: A string, or an expression which evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string). This is the date that is truncated.  
  If this argument is not a valid date format, then `null` is returned.
  * `part`: A string, or an expression which evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.md#manipulating-components) to truncate to.  
  If an invalid part is specified, then `null` is returned.
* Return Value:

  * A date string representing the truncated date.
* Example:  
{"day":   date_trunc_str('2016-05-18T03:59:00Z', 'day'),  
 "month": date_trunc_str('2016-05-18T03:59:00Z', 'month'),  
 "year":  date_trunc_str('2016-05-18T03:59:00Z', 'year')};
* The expected result is:  
{  
  "day": "2016-05-18T00:00:00Z",  
  "month": "2016-05-01T00:00:00Z",  
  "year": "2016-01-01T00:00:00Z"  
}

### [](#datefun%5F%5Ffn-date-duration-to-str)duration\_to\_str

* Syntax:  
duration_to_str(duration)
* Converts a number into a human-readable time duration with units.
* Arguments:

  * `duration`: A number, or an expression which evaluates to a number, which represents the duration to convert to a string. This value is specified in nanoseconds (1×10\-9 seconds).  
  If a value which is not a number is specified, then `null` is returned.
* Return Value:

  * A string representing the human-readable duration.
* Example:  
{"microsecs": duration_to_str(2000),  
 "millisecs": duration_to_str(2000000),  
 "secs":      duration_to_str(2000000000)};
* The expected result is:  
{  
  "microsecs": "2µs",  
  "millisecs": "2ms",  
  "secs": "2s"  
}

### [](#datefun%5F%5Ffn-date-millis)millis

* Syntax:  
millis(date1)
* Converts a date string to Epoch/UNIX milliseconds.
* Arguments:

  * `date1`: A string, or an expression which evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string). This is the date to convert to Epoch/UNIX milliseconds.  
  If this argument is not a valid date format. then `null` is returned.
* Return Value:

  * An integer representing the date string converted to Epoch/UNIX milliseconds.
* Example:  
{"DateStringInMilliseconds": millis("2016-05-15T03:59:00Z")};
* The expected result is:  
{  
  "DateStringInMilliseconds": 1463284740000  
}

### [](#datefun%5F%5Ffn-date-millis-to-str)millis\_to\_str (millis\_to\_local)

* Syntax:  
millis_to_str(date1 [, fmt ])
* Converts an Epoch/UNIX timestamp into the specified date string format.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the date to convert.  
  If this argument is not an integer, then `null` is returned.
  * `fmt`: A string, or an expression which evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string) to use for the result.  
  This argument is optional. If no format or an incorrect format is specified, it defaults to the combined full date and time.
* Return Value:

  * A date string representing the local date in the specified format.
* Example:  
{"full_date":      millis_to_str(1463284740000),  
 "invalid_format": millis_to_str(1463284740000, 'invalid format'),  
 "short_date":     millis_to_str(1463284740000, '1111-11-11')};
* The expected result is:  
{  
  "full_date": "2016-05-15T04:59:00+01:00",  
  "invalid_format": "2016-05-15T04:59:00+01:00",  
  "short_date": "2016-05-15"  
}

The function has an alias `millis_to_local`.

### [](#datefun%5F%5Ffn-date-millis-to-tz)millis\_to\_tz (millis\_to\_zone\_name)

* Syntax:  
millis_to_tz(date1, tz [, fmt])
* Converts an Epoch/UNIX timestamp into the specified time zone in the specified date string format.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the date to convert.  
  If this argument is not an integer, then `null` is returned.
  * `tz`: A string, or an expression which evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.md#date-timezone) to convert the local time to.  
  This argument is optional. If not specified, it defaults to the system timezone.  
  If an incorrect time zone is provided, then `null` is returned.
  * `fmt`: A string, or an expression which evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string) to use for the result.  
  This argument is optional. If no format or an incorrect format is specified, it defaults to the combined full date and time.
* Return Value:

  * A date string representing the date in the specified timezone in the specified format.
* Example:  
{"est": millis_to_tz(1463284740000, 'America/New_York'),  
 "ist": millis_to_tz(1463284740000, 'Asia/Kolkata'),  
 "utc": millis_to_tz(1463284740000, 'UTC')};
* The expected result is:  
{  
  "est": "2016-05-14T23:59:00-04:00",  
  "ist": "2016-05-15T09:29:00+05:30",  
  "utc": "2016-05-15T03:59:00Z"  
}

The function has an alias `millis_to_zone_name`.

### [](#datefun%5F%5Ffn-date-millis-to-utc)millis\_to\_utc

* Syntax:  
millis_to_utc(date1 [, fmt])
* Converts an Epoch/UNIX timestamp into local time in the specified date string format.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the date to convert to UTC.  
  If this argument is not an integer, then `null` is returned.
  * `fmt`: A string, or an expression which evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string) to use for the result.  
  This argument is optional. If no format or an incorrect format is specified, it defaults to the combined full date and time.
* Return Value:

  * A date string representing the date in UTC in the specified format.
* Example:  
{"full_date":      millis_to_utc(1463284740000),  
 "invalid_format": millis_to_utc(1463284740000, 'invalid format'),  
 "short_date":     millis_to_utc(1463284740000, '1111-11-11')};
* The expected result is:  
{  
  "full_date": "2016-05-15T03:59:00Z",  
  "invalid_format": "2016-05-15T03:59:00Z",  
  "short_date": "2016-05-15"  
}

### [](#datefun%5F%5Ffn-date-str-to-duration)str\_to\_duration

* Syntax:  
str_to_duration(duration)
* Converts a string representation of a time duration into nanoseconds. This accepts the following units:

  * nanoseconds (`ns`)
  * microseconds (`us` or `µs`)
  * milliseconds (`ms`)
  * seconds (`s`)
  * minutes (`m`)
  * hours (`h`)
* Arguments:

  * `duration`: A string, or an expression which evaluates to a string, representing the duration to convert.  
  If an invalid duration string is specified, then `null` is returned.
* Return Value:

  * A single integer representing the duration in nanoseconds.
* Example:  
{"hour":        str_to_duration('1h'),  
 "microsecond": str_to_duration('1us'),  
 "millisecond": str_to_duration('1ms'),  
 "minute":      str_to_duration('1m'),  
 "nanosecond":  str_to_duration('1ns'),  
 "second":      str_to_duration('1s')};
* The expected result is:  
{  
  "hour": 3600000000000,  
  "microsecond": 1000,  
  "millisecond": 1000000,  
  "minute": 60000000000,  
  "nanosecond": 1,  
  "second": 1000000000  
}

### [](#datefun%5F%5Ffn-date-str-to-millis)str\_to\_millis

* Syntax:  
str_to_millis(date1)
* Converts a date string to Epoch/UNIX milliseconds.
* Arguments:

  * `date1`: A string, or an expression which evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string). This is the date to convert to Epoch/UNIX milliseconds.  
  If this argument is not a valid date format, then `null` is returned.
* Return Value:

  * An integer representing the date string converted to Epoch/UNIX milliseconds.
* Example:  
{"Milliseconds": str_to_millis("2016-05-15T03:59:00Z")};
* The expected result is:  
{  
  "Milliseconds": 1463284740000  
}

### [](#datefun%5F%5Ffn-date-str-to-utc)str\_to\_utc

* Syntax:  
str_to_utc(date1)
* Converts a date string into the equivalent date in UTC. The output date format follows the date format of the date passed as input.
* Arguments:

  * `date1`: A string, or an expression which evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string). This is the date to convert to UTC.  
  If this argument is not a valid date format, then `null` is returned.
* Return Value:

  * A single date string representing the date string converted to UTC.
* Example:  
{"full_date":  str_to_utc('1111-11-11T00:00:00+08:00'),  
 "short_date": str_to_utc('1111-11-11')};
* The expected result is:  
{  
  "full_date": "1111-11-10T16:00:00Z",  
  "short_date": "1111-11-11"  
}

### [](#datefun%5F%5Ffn-date-str-to-tz)str\_to\_tz (str\_to\_zone\_name)

* Syntax:  
str_to_tz(date1, tz)
* Converts a date string to its equivalent in the specified timezone. The output date format follows the date format of the date passed as input.
* Arguments:

  * `date1`: A string, or an expression which evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string). This is the date to convert to UTC.  
  If this argument is not a valid date format then `null` is returned.
  * `tz`: A string, or an expression which evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.md#date-timezone) to convert the local time to.  
  If this argument is not a valid timezone, then `null` is returned.
* Return Value:

  * A single date string representing the date string converted to the specified timezone.
* Example:  
{"est":       str_to_tz('1111-11-11T00:00:00+08:00', 'America/New_York'),  
 "utc":       str_to_tz('1111-11-11T00:00:00+08:00', 'UTC'),  
 "utc_short": str_to_tz('1111-11-11', 'UTC')};
* The expected result is:  
{  
  "est": "1111-11-10T11:00:00-05:00",  
  "utc": "1111-11-10T16:00:00Z",  
  "utc_short": "1111-11-11"  
}

The function has an alias `str_to_zone_name`.

### [](#datefun%5F%5Ffn-date-weekday-millis)weekday\_millis

* Syntax:  
weekday_millis(expr [, tz ])
* Converts a date string to its equivalent in the specified timezone. The output date format follows the date format of the date passed as input.
* Arguments:

  * `expr`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds.
  * `tz`: A string, or an expression which evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.md#date-timezone) for the `expr` argument.  
  This argument is optional. If not specified, it defaults to the system timezone. If an incorrect time zone is provided then `null` is returned.
* Return Value:

  * A single date string representing the date string converted to the specified timezone.
* Example:  
{"Day": weekday_millis(1486237655742, 'America/Tijuana')};
* The expected result is:  
{  
  "Day": "Saturday"  
}

### [](#datefun%5F%5Ffn-date-weekday-str)weekday\_str

* Syntax:  
weekday_str(date)
* Returns the day of the week string value from the input date string. Returns the weekday name from the input date in Unix timestamp. Note that his function returns the string value of the day of the week, whereas [date\_part\_str()](#datefun%5F%5Ffn-date-part-str) with `part` \= "dow" returns an integer value of the weekday (0-6).
* Arguments:

  * `date`: A string, or an expression which evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.md#date-string). This is the date to convert to UTC.  
  If this argument is not a valid date format then `null` is returned.
* Return Value:

  * The text string name of the day of the week, such as "Monday" or "Friday".
* Example:  
{"Day": weekday_str('2017-02-05')};
* The expected result is:  
{  
  "Day": "Sunday"  
}

## [](#ObjectFunctions)Object Functions

### [](#object%5Fadd)object\_add

* Syntax:  
object_add(object, new_attr_key, new_attr_value)
* Adds a new field (name-value pair) to a given object. Note that this function does not update an existing field in a given object.
* Arguments:

  * `object`: An object, or an expression that evaluates to an object.
  * `new_attr_key`: A string, or an expression which evaluates to a string, representing a field name.
  * `new_attr_value`: A value, or any expression which evaluates to a value.
* Return Value:

  * The original JSON object, also including the added field.
  * If you add a duplicate field (that is, if the name is found), this function returns the object unmodified.
  * If `new_attr_key` is NULL, it returns a NULL value.
  * If `new_attr_key` is MISSING, it returns a MISSING value.
  * If `new_attr_value` is MISSING, it returns the object unmodified.
  * If `object` is not an object, or NULL, it returns a NULL value object.
* Example:  
object_add({"a": 1}, "b", 2);
* The expected result is:  
{  
  "a": 1,  
  "b": 2  
}

### [](#object%5Fconcat)object\_concat

* Syntax:  
object_concat(obj1, obj2 ...)  
object_concat(array)
* Concatenates the input objects. This function has two possible syntaxes. The first requires any number of object arguments. The second requires a single array argument, containing any number of objects.  
You can use the array syntax in situations where you don’t know ahead of time how many input objects there are to concatenate; or where you want to concatenate objects which are generated dynamically, for example by a subquery.
* Arguments:

  * `obj1`, `obj2` …​: Objects, or expressions that evaluate to objects.
  * `array`: An array of objects, or an expression that evaluates to an array of objects.
* Return Value:

  * An object constructed by concatenating all the input objects. If there is only one input object, it is returned unchanged. If any of the input objects contain the same attribute name, the attribute from the last relevant object in the input list is copied to the output; similarly-named attributes from earlier objects in the input list are ignored.
  * `null` if the function contains more than one array argument; if the function contains a mixture of array and object arguments; if the function has an array argument which is empty; if the function has no arguments; or if the function contains any argument that is not an array or object.
* Example — using object syntax:  
object_concat({"abc": 0}, {"abc": 1}, {"def": 2}, {"ghi": 3});
* The expected result is:  
{  
  "ghi": 3,  
  "def": 2,  
  "abc": 1  
}
* Example — using array syntax:  
object_concat([{"abc": 0}, {"abc": 1}, {"def": 2}, {"ghi": 3}]);
* The expected result is:  
{  
  "ghi": 3,  
  "def": 2,  
  "abc": 1  
}
* Example — using subquery:  
object_concat((SELECT VALUE {custid: name} FROM customers));
* The expected result is:  
{  
  "C41": "R. Dodge",  
  "C25": "M. Sinclair",  
  "C31": "B. Pruitt",  
  "C47": "S. Logan",  
  "C37": "T. Henry",  
  "C13": "T. Cody",  
  "C35": "J. Roberts"  
}

### [](#object%5Flength)object\_length

* Syntax:  
object_length(object)
* Counts the number of fields (name-value pairs) in an object.
* Arguments:

  * `object`: An object, or an expression that evaluates to an object.
* Return Value:

  * The number of fields in the object.
* Example:  
object_length({"abc":1, "def":2, "ghi":3});
* The expected result is:  
3

### [](#object%5Fnames)object\_names

* Syntax:  
object_names(object)
* Returns the names of all fields (name-value pairs) in an object.
* Arguments:

  * `object`: An object, or an expression that evaluates to an object.
* Return Value:

  * An array containing the field names of the object.
* Example:  
object_names({"a":1, "b":2, "c":3});
* The expected result is:  
[  
  "a",  
  "b",  
  "c"  
]

### [](#object%5Fpairs)object\_pairs

* Syntax:  
object_pairs(object)
* Returns the names and values of all fields (name-value pairs) in an object.
* Arguments:

  * `object`: An object, or an expression that evaluates to an object.
* Return Value:

  * An array of objects, each of which contains the name and value of one field in the original object.
* Example:  
object_pairs({"abc":1, "def":2, "ghi":3});
* The expected result is:  
[  
  {  
    "name": "abc",  
    "value": 1  
  },  
  {  
    "name": "def",  
    "value": 2  
  },  
  {  
    "name": "ghi",  
    "value": 3  
  }  
]

### [](#object%5Fput)object\_put

* Syntax:  
object_put(object, attr_key, attr_value)
* Adds a new field (name-value pair), or updates an existing field in a given object.
* Arguments:

  * `object`: An object, or an expression that evaluates to an object.
  * `attr_key`: A string, or an expression which evaluates to a string, representing a field name.
  * `attr_value`: A value, or any expression which evaluates to a value.
* Return Value:

  * The original JSON object, also including the field.
  * If `attr_key` is found in the object, this function replaces the corresponding field value by `attr_value`.
  * If `attr_key` is MISSING, it returns a MISSING value.
  * If `attr_key` is not a string, it returns a NULL value.
  * If `attr_value` is MISSING, it deletes the corresponding existing field (if any), like `object_remove()`.
* Example:  
object_put({"a": 1, "b": 2}, "a", 3);
* The expected result is:  
{  
  "a": 3,  
  "b": 2  
}

### [](#object%5Frename)object\_rename

* Syntax:  
object_rename(object, old_attr_key, new_attr_key)
* Renames a field (name-value pair) in the JSON input object.
* Arguments:

  * `object`: Any JSON object, or SQL++ expression that can evaluate to a JSON object.
  * `old_attr_key`: A string, or an expression which evaluates to a string, representing the old (original) field name inside the JSON object.
  * `new_attr_key`: A string, or an expression which evaluates to a string, representing the new field name to replace `old_attr_key` inside the JSON object.
* Return Value:

  * The JSON object `object` with the updated field name.
  * If `object` is not an object, or is NULL, the function returns a NULL value.
  * If `old_attr_key` or `new_attr_key` is not a string, or is NULL, the function returns a NULL value.
  * If any argument is MISSING, the function returns a MISSING value.
* Example:  
object_rename({"name": 1}, "name", "new_name");
* The expected result is:  
{  
  "new_name": 1  
}

### [](#object%5Fremove)object\_remove

* Syntax:  
object_remove(object, attr_key)
* Removes the specified field (name-value pair) from the given object.
* Arguments:

  * `object`: An object, or an expression that evaluates to an object.
  * `attr_key`: A string, or an expression which evaluates to a string, representing the name of the field to remove.
* Return Value:

  * The updated object.
  * If `object` is NULL, or is not an object, the function returns a NULL value.
  * If `attr_key` is NULL, or is not a string, the function returns a NULL value.
  * If any argument is MISSING, the function returns a MISSING value.

Example:

object_remove({"abc": 1, "def": 2, "ghi": 3}, "def");

* The expected result is:  
{  
  "abc": 1,  
  "ghi": 3  
}

### [](#object%5Freplace)object\_replace

* Syntax:  
object_replace(object, old_attr_value, new_attr_value)
* Replaces all occurrences of a value in the JSON input object.
* Arguments:

  * `object`: Any JSON object, or SQL++ expression that can evaluate to a JSON object.
  * `old_attr_value`: A value, or any expression which evaluates to a value, representing the old (original) value inside the JSON object.
  * `new_attr_value`: A value, or any expression which evaluates to a value, representing the new value to replace `old_attr_value` inside the JSON object.
* Return Value:

  * The JSON object `object` with the new value.
  * If `object` is not an object, the function returns a NULL value.
  * If `object` or `old_attr_value` is NULL, the function returns a NULL value.
  * If any argument is MISSING, the function returns a MISSING value.
* Example:  
object_replace({"abc": 1, "def": 2, "ghi": 3}, 3, "xyz");
* The expected result is:  
{  
  "abc": 1,  
  "def": 2,  
  "ghi": "xyz"  
}

### [](#object%5Funwrap)object\_unwrap

* Syntax:  
object_unwrap(object)
* Enables you to unwrap the value from an object containing a single field (name-value pair).
* Arguments:

  * `object`: An object, or an expression that evaluates to an object, containing exactly one field.
* Return Value:

  * The value from the field.
  * If the `object` is MISSING, this function returns MISSING.
  * For all other cases, or if the `object` contains more than one field, it returns NULL.
* Example:  
{ "v1": object_unwrap({"name": "value"}),  
  "v2": object_unwrap(MISSING),  
  "v3": object_unwrap({"name": "value", "name2": "value2"}),  
  "v4": object_unwrap("some_string") };
* The expected result is:  
{  
  "v1": "value",  
  "v3": null,  
  "v4": null  
}

### [](#object%5Fvalues)object\_values

* Syntax:  
object_values(object)
* Returns the values from all the fields (name-value pairs) in the object.
* Arguments:

  * `object`: An object, or an expression that evaluates to an object.
* Return Value:

  * An array which contains the values from all the fields in the object.
  * If the `object` is MISSING, this function returns MISSING.
  * If the `object` is NULL or not an object, it returns NULL.
* Example:  
object_values({"abc":1, "def":2, "ghi":3});
* The expected result is:  
[  
  1,  
  2,  
  3  
]

## [](#AggregateFunctions)Aggregate Functions

This section contains detailed descriptions of the built-in aggregate functions in the query language.

The query language also supports standard SQL aggregate functions (e.g., `MIN`, `MAX`, `SUM`, `COUNT`, and `AVG`). Note that these are not real functions in the query language, but just syntactic sugars over corresponding builtin aggregate functions (e.g., `ARRAY_MIN`, `ARRAY_MAX`, `ARRAY_SUM`, `ARRAY_COUNT`, and `ARRAY_AVG`). Refer to [Aggregation Pseudo-Functions](3%5Fquery.html#Aggregation%5FPseudoFunctions) for details.

The `DISTINCT` keyword may be used with built-in aggregate functions and standard SQL aggregate functions. It may also be used with aggregate functions used as window functions. It determines whether the function aggregates all values in the group, or distinct values only. Refer to [Function Calls](2%5Fexpr.html#Function%5Fcall%5Fexpressions) for details.

Couchbase Server 7.2.5

The [ARRAY\_MEDIAN](#array%5Fmedian) function, and the corresponding [MEDIAN](3%5Fquery.md#Aggregation%5FPseudoFunctions) aggregation pseudo-function, are available in Couchbase Server 7.2.5 and later.

Refer to [OVER Clauses](3%5Fquery.html#Over%5Fclauses) for details.

### [](#array%5Fcount)array\_count

* Syntax:  
array_count(collection)
* Gets the number of non-null and non-missing items in the given collection.
* Arguments:

  * `collection` could be:

    * an `array` or `multiset` to be counted,
    * or, a `null` value,
    * or, a `missing` value.
* Return Value:

  * a `bigint` value representing the number of non-null and non-missing items in the given collection,
  * `0` is returned if the input is `null` or `missing`,
  * `0` is returned if the input is not an array or a multiset.
* Example:  
array_count( ['hello', 'world', 1, 2, 3, null, missing] );
* The expected result is:  
5

### [](#array%5Favg)array\_avg

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will be ignored.
* Example:  
array_avg( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

1.725

### [](#array%5Fsum)array\_sum

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will be ignored.
* Example:  
array_sum( [1.2, 2.3, 3.4, 0, null, missing] );
* The expected result is:

6.9

### [](#array%5Fmin)array\_min

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if there are non-comparable items in the input array or multiset,
  * `null` is returned if the input is not an array or a multiset.
* Example:  
array_min( [1.2, 2.3, 3.4, 0, null, missing] );
* The expected result is:

0.0

### [](#array%5Fmax)array\_max

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if there are non-comparable items in the input array or multiset,
  * `null` is returned if the input is not an array or a multiset.
* Example:  
array_max( [1.2, 2.3, 3.4, 0, null, missing] );
* The expected result is:

3.4

### [](#array%5Fmedian)array\_median

* Syntax:  
array_median(num_collection)
* Gets the median value of the numeric items in the given collection, ignoring null, missing, and non-numeric items.  
The function starts by sorting the numeric items.

  * If there is an odd number of numeric items, the function returns the item that is exactly in the middle of the range: that is, it has the same number of items before and after.
  * If there is an even number of numeric items, the function returns the mean of the two items that are exactly in the middle of the range.
* NOTE: You cannot use the `DISTINCT` keyword with this function, or with the `median` aggregation pseudo-function. The `median` aggregation pseudo-function does support the `FILTER` clause. There is no `strict_median` function corresponding to this function.
* Arguments:

  * `num_collection` could be:

    * an `array` or `multiset` of numbers,
    * or, a `null` value,
    * or, a `missing` value.
* Clauses: When used as a window function, this function supports the [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause), but not the [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause) or the [Window Frame Clause](3%5Fquery.html#Window%5Fframe%5Fclause).
* Return Value:

  * a `double` value representing the median of the numeric items in the given collection,
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any numeric items,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will be ignored.
* Example:  
{ "v1": array_median( [1.2, 2.3, 3.4, 0, null, missing],  
  "v2": array_median( [1.2, 2.3, 3.4, 4.5, 0, null, missing] ) };
* The expected result is:  
{ "v1": 1.75,  
  "v2": 2.3 }

### [](#array%5Fstddev%5Fsamp)array\_stddev\_samp

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
array_stddev_samp( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

1.4591664287073858

### [](#array%5Fstddev%5Fpop)array\_stddev\_pop

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
array_stddev_pop( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

1.2636751956100112

### [](#array%5Fvar%5Fsamp)array\_var\_samp

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
array_var_samp( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

2.1291666666666664

### [](#array%5Fvar%5Fpop)array\_var\_pop

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
array_var_pop( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

1.5968749999999998

### [](#array%5Fskewness)array\_skewness

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
array_skewness( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

-0.04808451539164242

### [](#array%5Fkurtosis)array\_kurtosis

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if the given collection does not contain any non-null and non-missing items,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
array_kurtosis( [1.2, 2.3, 3.4, 0, null] );
* The expected result is:

-1.342049701096427

### [](#strict%5Fcount)strict\_count

* Syntax:  
strict_count(collection)
* Gets the number of items in the given collection.
* Arguments:

  * `collection` could be:

    * an `array` or `multiset` containing the items to be counted,
    * or a `null` value,
    * or a `missing` value.
* Return Value:

  * a `bigint` value representing the number of items in the given collection,
  * `0` is returned if the input is `null` or `missing`,
  * `0` is returned if the input is not an array or a multiset.
* Example:  
strict_count( [1, 2, null, missing] );
* The expected result is:  
4

### [](#strict%5Favg)strict\_avg

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * `null` is returned if the input is not an array or a multiset,
  * `null` is returned if there are any other non-numeric values in the input collection.
* Example:  
strict_avg( [100, 200, 300] );
* The expected result is:

200.0

### [](#strict%5Fsum)strict\_sum

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * `null` is returned if the input is not an array or a multiset,
  * `null` is returned if there are any other non-numeric values in the input collection.
* Example:  
strict_sum( [100, 200, 300] );
* The expected result is:  
600

### [](#strict%5Fmin)strict\_min

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * `null` is returned if there are non-comparable items in the input array or multiset,
  * `null` is returned if the input is not an array or a multiset.
* Example:  
strict_min( [10.2, 100, 5] );
* The expected result is:

5.0

### [](#strict%5Fmax)strict\_max

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * `null` is returned if there are non-comparable items in the input array or multiset,
  * `null` is returned if the input is not an array or a multiset.
* Example:  
strict_max( [10.2, 100, 5] );
* The expected result is:

100.0

### [](#strict%5Fstddev%5Fsamp)strict\_stddev\_samp

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
strict_stddev_samp( [100, 200, 300] );
* The expected result is:

100.0

### [](#strict%5Fstddev%5Fpop)strict\_stddev\_pop

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
strict_stddev_pop( [100, 200, 300] );
* The expected result is:

81.64965809277261

### [](#strict%5Fvar%5Fsamp)strict\_var\_samp

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
strict_var_samp( [100, 200, 300] );
* The expected result is:

10000.0

### [](#strict%5Fvar%5Fpop)strict\_var\_pop

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
strict_var_pop( [100, 200, 300] );
* The expected result is:

6666.666666666667

### [](#strict%5Fskewness)strict\_skewness

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
strict_skewness( [100, 200, 300] );
* The expected result is:

0.0

### [](#strict%5Fkurtosis)strict\_kurtosis

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
  * `null` is returned if the input is `null` or `missing`,
  * `null` is returned if there is a `null` or `missing` in the input collection,
  * `null` is returned if the input is not an array or a multiset,
  * any other non-numeric value in the input collection will cause a type error.
* Example:  
strict_kurtosis( [100, 200, 300] );
* The expected result is:

-1.5

## [](#ArrayFunctions)Array Functions

### [](#array%5Fappend)array\_append

* Syntax:  
array_append(list, val1, val2, ...)
* Appends the supplied values to the input array or multiset. Values can be NULL, meaning you can append NULLs.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
  * `val1`, `val2` …​: Values, or expressions that evaluate to values.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if `list` is NULL, or is not an array or multiset.
* Example:  
array_append([1, 2, 3], "a", "z");
* The expected result is:  
[  
  1,  
  2,  
  3,  
  "a",  
  "z"  
]

### [](#array%5Fconcat)array\_concat

* Syntax:  
array_concat(list1, list2, ...)
* Concatenates all the values from all the supplied arrays or multisets, in order, into a new array or multiset.
* Arguments:

  * `list1`, `list2` …​: Arrays or multisets, or expressions that evaluate to arrays or multisets.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL, or is not an array or multiset.
  * Returns an error if the input arguments are not all the same type — they must be all multisets or all arrays.
* Example:  
array_concat([1, 2, 3], ["a", "b", "c"]);
* The expected result is:  
[  
  1,  
  2,  
  3,  
  "a",  
  "b",  
  "c"  
]

### [](#array%5Fcontains)array\_contains

* Syntax:  
array_contains(list, val)
* Checks whether the the input array or multiset contains the value argument. A string value argument is case-sensitive.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
  * `val`: A value, or an expression that evaluates to a value.
* Return Value:

  * Returns true or false.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL.
  * Returns an error if `val` is an array, multiset, or object.
  * Returns NULL if `list` is not an array.
* Example:  
{"v1": array_contains([1, 2, 3], 1),  
 "v2": array_contains([1, 2, 3], "a")};
* The expected result is:  
{  
  "v1": true,  
  "v2": false  
}

### [](#array%5Fdistinct)array\_distinct

* Syntax:  
array_distinct(list)
* Returns all distinct items from the input array or multiset. The `list` can contain NULL and MISSING items. NULL and MISSING are considered to be the same. String items are case-sensitive.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
* Return Value:

  * Returns a new array if `list` is an array; returns a new multiset if `list` is a multiset.
  * Returns MISSING if `list` is MISSING.
  * Returns NULL if `list` is NULL, or is not an array or multiset.
  * Returns an error if any item in `list` is itself an array, multiset, or object.
* Example:  
array_distinct([1, 2, null, 4, missing, 2, 1]);
* The expected result is:  
[  
  1,  
  2,  
  null,  
  4  
]

### [](#array%5Fflatten)array\_flatten

* Syntax:  
array_flatten(list, depth)
* Flattens any nested arrays or multisets up to the specified depth. If `list` is an array, the function returns an array; if `list` is a multiset, it returns a multiset. NULL and MISSING items are preserved. If `depth` is less than 0, the function flattens all nested arrays and multisets, no matter how deeply nested.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
  * `depth`: A number, or an expression that evaluates to a number.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL.
  * Returns NULL if `list` is not an array or multiset.
  * Returns NULL if `depth` is not numeric, or if it is not an integer value. (For example, 1.2 will produce NULL; 1.0 is OK.)
* Example:  
{"v1": array_flatten([2, null, [5, 6], 3, missing], 1),  
 "v2": array_flatten([2, [5, 6], 3], 0)};
* The expected result is:  
{  
  "v1": [  
    2,  
    null,  
    5,  
    6,  
    3,  
    null  
  ],  
  "v2": [  
    2,  
    [  
      5,  
      6  
    ],  
    3  
  ]  
}  
where 0 depth does nothing.

### [](#array%5Fifnull)array\_ifnull

* Syntax:  
array_ifnull(list)
* In an array, finds the first item that is not a NULL or MISSING. In a multiset, finds an item that is not a NULL or MISSING — which item is undefined.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
* Return Value:

  * Returns the first non-NULL, non-MISSING item in an array, or any non-NULL, non-MISSING item in a multiset. If all items are NULL or MISSING, it returns NULL.
  * Returns MISSING if the input array or multiset is MISSING.
  * Returns NULL if `list` is NULL, or is not an array or multiset.
* Example:  
array_ifnull([null, 1, 2]);
* The expected result is:  
1

### [](#array%5Finsert)array\_insert

* Syntax:  
array_insert(list, pos, val1, val2, ...)
* Inserts the supplied values into the original array or multiset. Values can be NULL, meaning you can insert NULLs.  
When the input is an array, the supplied values are inserted at the specified position. If the position is positive, the position before the first item is 0, the position before the second item is 1, and so on. If the position is negative, the position before the last item is -1, the position before the second-last item is -2, and so on. So for example, in the array \[5,6\], the valid positions are 0, 1, 2, -1, -2\. If the input array or multiset is empty, the only valid position is 0\. If the position is a floating-point number, it’s cast to integer.  
When the input is a multiset, the location of the inserted values is undefined. The position must be less than the size of the multiset.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
  * `pos`: A number, or an expression that evaluates to a number.
  * `val1`, `val2` …​: Values, or expressions that evaluate to values.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if `list` is NULL, or is not an array or multiset.
  * Returns NULL if `pos` is not numeric, or the position is out of bound, or if it is NaN or ±INF, or if it is not an integer value. (For example, 1.2 will produce NULL; 1.0 is OK.)
* Example:  
{"v1": array_insert([5, 6], 0, 7, 8),  
 "v2": array_insert([5, 6], 1, 7, 8),  
 "v3": array_insert([5, 6], 2, 7, 8),  
 "v4": array_insert([5, 6], -1, 7, 8),  
 "v5": array_insert([5, 6], -2, 7, 8)};
* The expected result is:  
{  
  "v1": [  
    7,  
    8,  
    5,  
    6  
  ],  
  "v2": [  
    5,  
    7,  
    8,  
    6  
  ],  
  "v3": [  
    5,  
    6,  
    7,  
    8  
  ],  
  "v4": [  
    5,  
    7,  
    8,  
    6  
  ],  
  "v5": [  
    7,  
    8,  
    5,  
    6  
  ]  
}

### [](#array%5Fintersect)array\_intersect

* Syntax:  
array_intersect(list1, list2, ...)
* Finds items that are present in all of the input arrays or multisets. NULL and MISSING items are ignored. String items are case-sensitive.
* Arguments:

  * `list1`, `list2` …​: Arrays or multisets, or expressions that evaluate to arrays or multisets.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL, or is not an array or multiset.
  * Returns an error if the input arguments are not all the same type — they must be all multisets or all arrays.
  * Returns an error if any item in an input array or multiset is itself an array, multiset, or object.
* Example:  
array_intersect([null, 2, missing], [3, missing, 2, null]);
* The expected result is:  
[  
  2  
]

### [](#array%5Flength)array\_length

* Syntax:  
array_length(list)
* Returns the number of items in the given array or multiset.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
* Return Value:

  * Returns an integer representing the number of items in the given array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL.
  * Returns an error if `list` is not an array or multiset.
* Example:  
array_length([1, 2, 3, 4]);
* The expected result is:  
4

### [](#array%5Fposition)array\_position

* Syntax:  
array_position(list, val)
* If `list` is an array, this function returns the position of `val` in the array, where the first position is 0\. If `list` is a multiset, the returned value is undefined. A string value argument is case-sensitive.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
  * `val`: A value, or an expression that evaluates to a value.
* Return Value:

  * Returns an integer giving the position of `val` in `list`, or -1 if `val` is not found.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL.
  * Returns an error if `val` is an array, multiset, or object.
  * Returns NULL if `list` is not an array or multiset.
* Example:  
array_position([1, 2, 3, 4], 1);
* The expected result is:  
0

### [](#array%5Fprepend)array\_prepend

* Syntax:  
array_prepend(val1, val2, ..., list)
* Prepends the supplied values to the input array or multiset. Values can be NULL, meaning NULL values are prepended in the output.
* Arguments:

  * `val1`, `val2` …​: Values, or expressions that evaluate to values.
  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if `list` is NULL, or is not an array or multiset.
* Example:  
array_prepend("a", "z", [1, 2, 3]);
* The expected result is:  
[  
  "a",  
  "z",  
  1,  
  2,  
  3  
]

### [](#array%5Fput)array\_put

* Syntax:  
array_put(list, val1, val2, ...)
* Appends each supplied value to the input array or multiset, as long as the input array or multiset does not already contain an item with that value. Values cannot be NULL, meaning you cannot append NULLs.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
  * `val1`, `val2` …​: Values, or expressions that evaluate to values.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL.
  * Returns an error if any value argument is an array, multiset, or object.
* Example:  
array_put([2, 3], 2, 2, 9, 9);
* The expected result is:  
[  
  2,  
  3,  
  9,  
  9  
]

### [](#array%5Frange)array\_range

* Syntax:  
array_range(start_num, end_num [, step_num])
* Returns an array of numbers, starting at `start_num` and ending immediately before `end_num`. If specified, `step_num` determines the step between each number in the array; otherwise, the default step is 1\. The function returns an empty array if it cannot determine a proper sequence with the arguments given.
* Arguments:

  * `start_num`: A number, or an expression that evaluates to a number.
  * `end_num`: A number, or an expression that evaluates to a number.
  * `step_num`: A number, or an expression that evaluates to a number.
* Return Value:

  * Returns a new array.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL.
  * Returns NULL if any argument is not numeric, or if it is NaN, or ±INF.
* Example:  
{"v1": array_range(1, 5),  
 "v2": array_range(5, 1, -1),  
 "v3": array_range(2, 20, -2),  
 "v4": array_range(10, 3, 4),  
 "v5": array_range(1, 6, 0)};
* The expected result is:  
{  
  "v1": [  
    1,  
    2,  
    3,  
    4  
  ],  
  "v2": [  
    5,  
    4,  
    3,  
    2  
  ],  
  "v3": [],  
  "v4": [],  
  "v5": []  
}

### [](#array%5Fremove)array\_remove

* Syntax:  
array_remove(list, val1, val2, ...)
* Removes all the supplied values from the input array or multiset. Values cannot be NULL, meaning you cannot remove NULLs. String value arguments are case-sensitive.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
  * `val1`, `val2` …​: Values, or expressions that evaluate to values.
* Return Value:

  * Returns a new array if `list` is an array; returns a new multiset if `list` is a multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL.
  * Returns an error if any value argument is an array, multiset, or object.
* Example:  
array_remove([1, 2, 2, 3, 4], 2, 4);
* The expected result is:  
[  
  1,  
  3  
]

### [](#array%5Frepeat)array\_repeat

* Syntax:  
array_repeat(val, num_times)
* Returns an array containing the input value the specified number of times.
* Arguments:

  * `val`: A value, or an expression that evaluates to a value.
  * `num_times`: A number, or an expression that evaluates to a number.
* Return Value:

  * Returns an array.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL.
  * Returns NULL if `num_times` is not numeric, or if it is negative, NaN or ±INF, or if it is not an integer value. (For example, 1.2 will produce NULL; 1.0 is OK.)
* Example:  
array_repeat("abc", 3);
* The expected result is:  
[  
  "abc",  
  "abc",  
  "abc"  
]

### [](#array%5Freplace)array\_replace

* Syntax:  
array_replace(list, val1, val2 [, max_num_times])
* Replaces each occurrence of `val1` in the original array or multiset with `val2`. If you supply the optional `max_num_times` argument, the function replaces `val1` the specified number of times. If `max_num_times` is negative, the function replaces all occurrences. The `val2` argument can be NULL, meaning you can replace existing items with NULLs.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
  * `val1`: A value, or an expression that evaluates to a value.
  * `val2`: A value, or an expression that evaluates to a value.
  * `max_num_times`: A number, or an expression that evaluates to a number.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL, except for `val2`.
  * Returns NULL if `list` is not an array or multiset.
  * Returns NULL if `num_times` is not numeric, or if it is not an integer value. (For example, 1.2 will produce NULL; 1.0 is OK.)
  * Returns an error if `val1` is an array, multiset, or object.
* Example:  
array_replace([2,3,3,3,1], 3, 8, 2);
* The expected result is:  
[  
  2,  
  8,  
  8,  
  3,  
  1  
]

### [](#array%5Freverse)array\_reverse

* Syntax:  
array_reverse(list)
* If `list` is an array, this function returns an array with the order of items reversed. If `list` is a multiset, the function returns the same multiset unchanged. The `list` can contain NULL and MISSING items, and both are preserved.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if `list` is MISSING.
  * Returns NULL if `list` is NULL, or is not an array or multiset.
* Example:  
array_reverse([1, 2, 3, 4]);
* The expected result is:  
[  
  4,  
  3,  
  2,  
  1  
]

### [](#array%5Fsort)array\_sort

* Syntax:  
array_sort(list)
* If `list` is an array, this function returns an array with items sorted in ascending order. If `list` is a multiset, the function returns the same multiset unchanged. The `list` can contain NULL and MISSING items, and both are preserved. String items are case-sensitive.
* Arguments:

  * `list`: An array or multiset, or an expression that evaluates to an array or multiset.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if `list` is MISSING.
  * Returns NULL if `list` is NULL, or is not an array or multiset.
  * Returns an error if any item in `list` is itself an array, multiset, or object.
* Example:  
array_sort([1, "Z", "a", "A", "z", 0, null]);
* The expected result is:  
[  
  null,  
  0,  
  1,  
  "A",  
  "Z",  
  "a",  
  "z"  
]

### [](#array%5Fstar)array\_star

* Syntax:  
array_star(ordered_list)
* Takes an array of objects, such as `[{"id":1, "dept":"CS"}, {"id":2, "dept":"FIN"}, {"id":3, "dept":"CS"}]`, and returns a new object summarizing the name-value pairs in the input array. In the returned object, the name of each item is taken from a name-value pair found in the input array, and the value of each item is an array of all the values associated with that name, taken from all objects in the input array.
* Arguments:

  * `ordered_list`: An array, or an expression that evaluates to an array.
* Return Value:

  * Returns a new object.
  * Returns MISSING if `ordered_list` is MISSING.
  * Returns NULL if `ordered_list` is NULL, or is not an array.
  * Returns MISSING if `ordered_list` has no concept of fields — for example, if the input array contains no object items, such as a list of integers.
* Example:  
{"v1": array_star([{"a":1, "b":2}, {"a":9, "b":4}]),  
 "v2": array_star([{"a":1}, {"a":9, "b":4}]),  
 "v3": array_star([{"a":1, "c":5}, {"a":9, "b":4}]),  
 "v4": array_star([{"c":5, "a":1}, "non_object"]),  
 "v5": array_star(["non_object1", "non_object2"])};
* The expected result is:  
{  
  "v1": {  
    "a": [  
      1,  
      9  
    ],  
    "b": [  
      2,  
      4  
    ]  
  },  
  "v2": {  
    "a": [  
      1,  
      9  
    ],  
    "b": [  
      null,  
      4  
    ]  
  },  
  "v3": {  
    "a": [  
      1,  
      9  
    ],  
    "b": [  
      null,  
      4  
    ],  
    "c": [  
      5,  
      null  
    ]  
  },  
  "v4": {  
    "a": [  
      1,  
      null  
    ],  
    "c": [  
      5,  
      null  
    ]  
  }  
}  
where `"v5"` is MISSING.

> [!NOTE]
> In the output object, name-value pairs are ordered by their names, regardless of their original order within the object items in the input array. So in example 4, in the output object, the pair named `"a"` comes before the pair named `"c"`. However, in the output object, the items within each array are not ordered: they appear in the sequence in which they are found in the input array. So in example 1, the pair named `"a"` has the value `[1, 9]`; the first item in the output array (which is `1`) is taken from the first object in the input array, and so on.

### [](#array%5Fsymdiff)array\_symdiff

* Syntax:  
array_symdiff(list1, list2, ...)
* Returns the set symmetric difference, or disjunctive union, of the input arrays or multisets. The output contains only those items that appear in exactly one of the input arrays or multisets.
* Arguments:

  * `list1`, `list2` …​: Arrays or multisets, or expressions that evaluate to arrays or multisets.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL, or is not an array or multiset.
  * Returns an error if the input arguments are not all the same type — they must be all multisets or all arrays.
  * Returns an error if any item in an input array or multiset is itself an array, multiset, or object.
* Example:  
array_symdiff([1, 2], [1, 2, 4], [1, 3]);
* The expected result is:  
[  
  4,  
  3  
]

### [](#array%5Fsymdiffn)array\_symdiffn

* Syntax:  
array_symdiffn(list1, list2, ...)
* Returns a new array or multiset based on the set symmetric difference, or disjunctive union, of the input arrays. The new array or multiset contains only those items that appear in an odd number of input arrays.
* Arguments:

  * `list1`, `list2` …​: Arrays or multisets, or expressions that evaluate to arrays or multisets.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL, or is not an array or multiset.
  * Returns an error if the input arguments are not all the same type — they must be all multisets or all arrays.
  * Returns an error if any item in an input array or multiset is itself an array, multiset, or object.
* Example:  
array_symdiffn([1, 2], [1, 2, 4], [1, 3]);
* The expected result is:  
[  
  1,  
  4,  
  3  
]

> [!NOTE]
> Refer to the following article for more information on the difference between a normal and n-ary symdiff: <https://en.wikipedia.org/wiki/Symmetric%5Fdifference>.

### [](#array%5Funion)array\_union

* Syntax:  
array_union(list1, list2, ...)
* Returns the set union of the input arrays (no duplicates).
* Arguments:

  * `list1`, `list2` …​: Arrays or multisets, or expressions that evaluate to arrays or multisets.
* Return Value:

  * Returns a new array or multiset.
  * Returns MISSING if any argument is MISSING.
  * Returns NULL if any argument is NULL, or is not an array or multiset.
  * Returns an error if the input arguments are not all the same type — they must be all multisets or all arrays.
  * Returns an error if any item in an input array or multiset is itself an array, multiset, or object.
* Example:  
array_union([1, 2], [1, 2, 4], [1, 3]);
* The expected result is:  
[  
  1,  
  2,  
  4,  
  3  
]

## [](#ComparisonFunctions)Comparison Functions

### [](#greatest)greatest

* Syntax:  
greatest(numeric_value1, numeric_value2, ...)
* Computes the greatest value among arguments.
* Arguments:

  * `numeric_value1`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * `numeric_value2`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * …​.
* Return Value:

  * the greatest values among arguments. The returning type is decided by the item type with the highest order in the numeric type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among items.
  * `null` if any argument is a `missing` value or `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": greatest(1, 2, 3), "v2": greatest(float("0.5"), double("-0.5"), 5000) };
* The expected result is:  
{ "v1": 3, "v2": 5000.0 }

### [](#least)least

* Syntax:  
least(numeric_value1, numeric_value2, ...)
* Computes the least value among arguments.
* Arguments:

  * `numeric_value1`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * `numeric_value2`: a `tinyint`/`smallint`/`integer`/`bigint`/`float`/`double` value,
  * …​.
* Return Value:

  * the least values among arguments. The returning type is decided by the item type with the highest order in the numeric type promotion order (`tinyint`\-> `smallint`\->`integer`\->`bigint`\->`float`\->`double`) among items.
  * `null` if any argument is a `missing` value or `null` value,
  * any other non-numeric input value will cause a type error.
* Example:  
{ "v1": least(1, 2, 3), "v2": least(float("0.5"), double("-0.5"), 5000) };
* The expected result is:  
{ "v1": 1, "v2": -0.5 }

## [](#TypeFunctions)Type Functions

### [](#is%5Farray)is\_array

* Syntax:  
is_array(expr)
* Checks whether the given expression is evaluated to be an `array` value.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the argument is an `array` value or not,
  * a `missing` if the argument is a `missing` value,
  * a `null` if the argument is a `null` value.
* Example:  
{  
  "a": is_array(true),  
  "b": is_array(false),  
  "c": isarray(null),  
  "d": isarray(missing),  
  "e": isarray("d"),  
  "f": isarray(4.0),  
  "g": isarray(5),  
  "h": isarray(["1", 2]),  
  "i": isarray({"a":1})  
};
* The expected result is:  
{ "a": false, "b": false, "c": null, "e": false, "f": false, "g": false, "h": true, "i": false }

The function has an alias `isarray`.

### [](#is%5Fmultiset)is\_multiset

* Syntax:  
is_multiset(expr)
* Checks whether the given expression is evaluated to be an `multiset` value.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the argument is an `multiset` value or not,
  * a `missing` if the argument is a `missing` value,
  * a `null` if the argument is a `null` value.
* Example:  
{  
  "a": is_multiset(true),  
  "b": is_multiset(false),  
  "c": is_multiset(null),  
  "d": is_multiset(missing),  
  "e": is_multiset("d"),  
  "f": ismultiset(4.0),  
  "g": ismultiset(["1", 2]),  
  "h": ismultiset({"a":1}),  
  "i": ismultiset({{"hello", 9328, "world", [1, 2, null]}})  
};
* The expected result is:  
{ "a": false, "b": false, "c": null, "e": false, "f": false, "g": false, "h": false, "i": true }

The function has an alias `ismultiset`.

### [](#is%5Fatomic-is%5Fatom)is\_atomic (is\_atom)

* Syntax:  
is_atomic(expr)
* Checks whether the given expression is evaluated to be a value of a [primitive](10%5Fdata%5Ftype.html#PrimitiveTypes) type.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the argument is a primitive type or not,
  * a `missing` if the argument is a `missing` value,
  * a `null` if the argument is a `null` value.
* Example:  
{  
  "a": is_atomic(true),  
  "b": is_atomic(false),  
  "c": isatomic(null),  
  "d": isatomic(missing),  
  "e": isatomic("d"),  
  "f": isatom(4.0),  
  "g": isatom(5),  
  "h": isatom(["1", 2]),  
  "i": isatom({"a":1})  
};
* The expected result is:  
{ "a": true, "b": true, "c": null, "e": true, "f": true, "g": true, "h": false, "i": false }

The function has three aliases: `isatomic`, `is_atom`, and `isatom`.

### [](#is%5Fboolean-is%5Fbool)is\_boolean (is\_bool)

* Syntax:  
is_boolean(expr)
* Checks whether the given expression is evaluated to be a `boolean` value.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the argument is a `boolean` value or not,
  * a `missing` if the argument is a `missing` value,
  * a `null` if the argument is a `null` value.
* Example:  
{  
  "a": isboolean(true),  
  "b": isboolean(false),  
  "c": is_boolean(null),  
  "d": is_boolean(missing),  
  "e": isbool("d"),  
  "f": isbool(4.0),  
  "g": isbool(5),  
  "h": isbool(["1", 2]),  
  "i": isbool({"a":1})  
};
* The expected result is:  
{ "a": true, "b": true, "c": null, "e": false, "f": false, "g": false, "h": false, "i": false }

The function has three aliases: `isboolean`, `is_bool`, and `isbool`.

### [](#is%5Fnumber-is%5Fnum)is\_number (is\_num)

* Syntax:  
is_number(expr)
* Checks whether the given expression is evaluated to be a numeric value.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the argument is a `smallint`/`tinyint`/`integer`/`bigint`/`float`/`double`value or not,
  * a `missing` if the argument is a `missing` value,
  * a `null` if the argument is a `null` value.
* Example:  
{  
  "a": is_number(true),  
  "b": is_number(false),  
  "c": isnumber(null),  
  "d": isnumber(missing),  
  "e": isnumber("d"),  
  "f": isnum(4.0),  
  "g": isnum(5),  
  "h": isnum(["1", 2]),  
  "i": isnum({"a":1})  
};
* The expected result is:  
{ "a": false, "b": false, "c": null, "e": false, "f": true, "g": true, "h": false, "i": false }

The function has three aliases: `isnumber`, `is_num`, and `isnum`.

### [](#is%5Fobject-is%5Fobj)is\_object (is\_obj)

* Syntax:  
is_object(expr)
* Checks whether the given expression is evaluated to be a `object` value.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the argument is a `object` value or not,
  * a `missing` if the argument is a `missing` value,
  * a `null` if the argument is a `null` value.
* Example:  
{  
  "a": is_object(true),  
  "b": is_object(false),  
  "c": isobject(null),  
  "d": isobject(missing),  
  "e": isobj("d"),  
  "f": isobj(4.0),  
  "g": isobj(5),  
  "h": isobj(["1", 2]),  
  "i": isobj({"a":1})  
};
* The expected result is:  
{ "a": false, "b": false, "c": null, "e": false, "f": false, "g": false, "h": false, "i": true }

The function has three aliases: `isobject`, `is_obj`, and `isobj`.

### [](#is%5Fstring-is%5Fstr)is\_string (is\_str)

* Syntax:  
is_string(expr)
* Checks whether the given expression is evaluated to be a `string` value.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the argument is a `string` value or not,
  * a `missing` if the argument is a `missing` value,
  * a `null` if the argument is a `null` value.
* Example:  
{  
  "a": is_string(true),  
  "b": isstring(false),  
  "c": isstring(null),  
  "d": isstr(missing),  
  "e": isstr("d"),  
  "f": isstr(4.0),  
  "g": isstr(5),  
  "h": isstr(["1", 2]),  
  "i": isstr({"a":1})  
};
* The expected result is:  
{ "a": false, "b": false, "c": null, "e": true, "f": false, "g": false, "h": false, "i": false }

The function has three aliases: `isstring`, `is_str`, and `isstr`.

### [](#is%5Fnull)is\_null

* Syntax:  
is_null(expr)
* Checks whether the given expression is evaluated to be a `null` value.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the variable is a `null` or not,
  * a `missing` if the input is `missing`.
* Example:  
{ "v1": is_null(null), "v2": is_null(1), "v3": is_null(missing) };
* The expected result is:  
{ "v1": true, "v2": false }

The function has an alias `isnull`.

### [](#is%5Fmissing)is\_missing

* Syntax:  
is_missing(expr)
* Checks whether the given expression is evaluated to be a `missing` value.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the variable is a `missing` or not.
* Example:  
{ "v1": is_missing(null), "v2": is_missing(1), "v3": is_missing(missing) };
* The expected result is:  
{ "v1": false, "v2": false, "v3": true }

The function has an alias `ismissing`.

### [](#is%5Funknown)is\_unknown

* Syntax:  
is_unknown(expr)
* Checks whether the given variable is a `null` value or a `missing` value.
* Arguments:

  * `expr` : an expression (any type is allowed).
* Return Value:

  * a `boolean` on whether the variable is a `null`/`missing` value (`true`) or not (`` `false ``).
* Example:  
{ "v1": is_unknown(null), "v2": is_unknown(1), "v3": is_unknown(missing) };
* The expected result is:  
{ "v1": true, "v2": false, "v3": true }

The function has an alias `isunknown`.

### [](#to%5Farray)to\_array

* Syntax:  
to_array(expr)
* Converts input value to an `array` value
* Arguments:

  * `expr` : an expression
* Return Value:

  * if the argument is `missing` then `missing` is returned
  * if the argument is `null` then `null` is returned
  * if the argument is of `array` type then it is returned as is
  * if the argument is of `multiset` type then it is returned as an `array` with elements in an undefined order
  * otherwise an `array` containing the input expression as its single item is returned
* Example:  
{  
  "v1": to_array("asterix"),  
  "v2": to_array(["asterix"]),  
};
* The expected result is:  
{ "v1": ["asterix"], "v2": ["asterix"] }

The function has an alias `toarray`.

### [](#to%5Fatomic-to%5Fatom)to\_atomic (to\_atom)

* Syntax:  
to_atomic(expr)
* Converts input value to a [primitive](10%5Fdata%5Ftype.html#PrimitiveTypes) value
* Arguments:

  * `expr` : an expression
* Return Value:

  * if the argument is `missing` then `missing` is returned
  * if the argument is `null` then `null` is returned
  * if the argument is of primitive type then it is returned as is
  * if the argument is of `array` or `multiset` type and has only one element then the result of invoking to\_atomic() on that element is returned
  * if the argument is of `object` type and has only one field then the result of invoking to\_atomic() on the value of that field is returned
  * otherwise `null` is returned
* Example:  
{  
  "v1": to_atomic("asterix"),  
  "v2": to_atomic(["asterix"]),  
  "v3": to_atomic([0, 1]),  
  "v4": to_atomic({"value": "asterix"}),  
  "v5": to_number({"x": 1, "y": 2})  
};
* The expected result is:  
{ "v1": "asterix", "v2": "asterix", "v3": null, "v4": "asterix", "v5": null }

The function has three aliases: `toatomic`, `to_atom`, and `toatom`.

### [](#to%5Fboolean-to%5Fbool)to\_boolean (to\_bool)

* Syntax:  
to_boolean(expr)
* Converts input value to a `boolean` value
* Arguments:

  * `expr` : an expression
* Return Value:

  * if the argument is `missing` then `missing` is returned
  * if the argument is `null` then `null` is returned
  * if the argument is of `boolean` type then it is returned as is
  * if the argument is of numeric type then `false` is returned if it is `0` or `NaN`, otherwise `true`
  * if the argument is of `string` type then `false` is returned if it’s empty, otherwise `true`
  * if the argument is of `array` or `multiset` type then `false` is returned if it’s size is `0`, otherwise `true`
  * if the argument is of `object` type then `false` is returned if it has no fields, otherwise `true`
  * type error is raised for all other input types
* Example:  
{  
  "v1": to_boolean(0),  
  "v2": to_boolean(1),  
  "v3": to_boolean(""),  
  "v4": to_boolean("asterix")  
};
* The expected result is:  
{ "v1": false, "v2": true, "v3": false, "v4": true }

The function has three aliases: `toboolean`, `to_bool`, and `tobool`.

### [](#to%5Fbigint)to\_bigint

* Syntax:  
to_bigint(expr)
* Converts input value to an integer value
* Arguments:

  * `expr` : an expression
* Return Value:

  * if the argument is `missing` then `missing` is returned
  * if the argument is `null` then `null` is returned
  * if the argument is of `boolean` type then `1` is returned if it is `true`, `0` if it is `false`
  * if the argument is of numeric integer type then it is returned as the same value of `bigint` type
  * if the argument is of numeric `float`/`double` type then it is converted to `bigint` type
  * if the argument is of `string` type and can be parsed as integer then that integer value is returned, otherwise `null` is returned
  * if the argument is of `array`/`multiset`/`object` type then `null` is returned
  * type error is raised for all other input types
* Example:  
{  
  "v1": to_bigint(false),  
  "v2": to_bigint(true),  
  "v3": to_bigint(10),  
  "v4": to_bigint(float("1e100")),  
  "v5": to_bigint(double("1e1000")),  
  "v6": to_bigint("20")  
};
* The expected result is:  
{ "v1": 0, "v2": 1, "v3": 10, "v4": 9223372036854775807, "v5": 9223372036854775807, "v6": 20 }

The function has an alias `tobigint`.

### [](#to%5Fdouble)to\_double

* Syntax:  
to_double(expr)
* Converts input value to a `double` value
* Arguments:

  * `expr` : an expression
* Return Value:

  * if the argument is `missing` then `missing` is returned
  * if the argument is `null` then `null` is returned
  * if the argument is of `boolean` type then `1.0` is returned if it is `true`, `0.0` if it is `false`
  * if the argument is of numeric type then it is returned as the value of `double` type
  * if the argument is of `string` type and can be parsed as `double` then that `double` value is returned, otherwise `null` is returned
  * if the argument is of `array`/`multiset`/`object` type then `null` is returned
  * type error is raised for all other input types
* Example:  
{  
  "v1": to_double(false),  
  "v2": to_double(true),  
  "v3": to_double(10),  
  "v4": to_double(11.5),  
  "v5": to_double("12.5")  
};
* The expected result is:  
{ "v1": 0.0, "v2": 1.0, "v3": 10.0, "v4": 11.5, "v5": 12.5 }

The function has an alias `todouble`.

### [](#to%5Fnumber-to%5Fnum)to\_number (to\_num)

* Syntax:  
to_number(expr)
* Converts input value to a numeric value
* Arguments:

  * `expr` : an expression
* Return Value:

  * if the argument is `missing` then `missing` is returned
  * if the argument is `null` then `null` is returned
  * if the argument is of numeric type then it is returned as is
  * if the argument is of `boolean` type then `1` is returned if it is `true`, `0` if it is `false`
  * if the argument is of `string` type and can be parsed as `bigint` then that `bigint` value is returned, otherwise if it can be parsed as `double` then that `double` value is returned, otherwise `null` is returned
  * if the argument is of `array`/`multiset`/`object` type then `null` is returned
  * type error is raised for all other input types
* Example:  
{  
  "v1": to_number(false),  
  "v2": to_number(true),  
  "v3": to_number(10),  
  "v4": to_number(11.5),  
  "v5": to_number("12.5")  
};
* The expected result is:  
{ "v1": 0, "v2": 1, "v3": 10, "v4": 11.5, "v5": 12.5 }

The function has three aliases: `tonumber`, `to_num`, and `tonum`.

### [](#to%5Fobject-to%5Fobj)to\_object (to\_obj)

* Syntax:  
to_object(expr)
* Converts input value to an `object` value
* Arguments:

  * `expr` : an expression
* Return Value:

  * if the argument is `missing` then `missing` is returned
  * if the argument is `null` then `null` is returned
  * if the argument is of `object` type then it is returned as is
  * otherwise an empty `object` is returned
* Example:  
{  
  "v1": to_object({"value": "asterix"}),  
  "v2": to_object("asterix")  
};
* The expected result is:  
{ "v1": {"value": "asterix"}, "v2": {} }

The function has three aliases: `toobject`, `to_obj`, and `toobj`.

### [](#to%5Fstring-to%5Fstr)to\_string (to\_str)

* Syntax:  
to_string(expr)
* Converts input value to a string value
* Arguments:

  * `expr` : an expression
* Return Value:

  * if the argument is `missing` then `missing` is returned
  * if the argument is `null` then `null` is returned
  * if the argument is of `boolean` type then `"true"` is returned if it is `true`, `"false"` if it is `false`
  * if the argument is of numeric type then its string representation is returned
  * if the argument is of `string` type then it is returned as is
  * if the argument is of `array`/`multiset`/`object` type then `null` is returned
  * type error is raised for all other input types
* Example:  
{  
  "v1": to_string(false),  
  "v2": to_string(true),  
  "v3": to_string(10),  
  "v4": to_string(11.5),  
  "v5": to_string("asterix")  
};
* The expected result is:  
{ "v1": "false", "v2": "true", "v3": "10", "v4": "11.5", "v5": "asterix" }

The function has three aliases: `tostring`, `to_str`, and `tostr`.

### [](#typename)typename

* Syntax:  
typename(expr)
* Returns the type of an expression.
* Arguments:

  * `expr`: an expression.
* Return Value:

  * Returns a string, depending on the type of `expr`: number, string, array, object, or boolean.
  * Returns NULL if `expr` is NULL.
* Example:  
{"v1": typename(123),  
 "v2": typename("abc"),  
 "v3": typename([1, 2, 3]),  
 "v4": typename({"abc": 123}),  
 "v5": typename(true)};
* The expected result is:  
{  
  "v1": "number",  
  "v2": "string",  
  "v3": "array",  
  "v4": "object",  
  "v5": "boolean"  
}

### [](#array%5Finfer%5Fschema)array\_infer\_schema

* Syntax:  
array_infer_schema(collection[, parameters])
* Infers the schema of an array or multiset, for example the structure of the elements, data types of various attributes, sample values, and so on. Since an array or multiset can contain items with varying structures, the result of this function is statistical in nature rather than deterministic.  
This function is the equivalent to the SQL++ for Query [INFER statement](../n1ql/n1ql-language-reference/infer.md).  
> [!NOTE]  
> You can infer the schema of a collection by applying this function to a subquery which returns the documents in that collection, or a representative sample of them. The subquery must use the `SELECT VALUE` clause to avoid an additional layer of nesting in the result of the subquery.
* Arguments:

  * `collection`: An array or multiset, or an expression that evaluates to an array or multiset.
  * `parameters`: (Optional) An object, which may contain one or more of the following fields to guide the function.

    * `similarity_metric`: (Optional) A number, or an expression that evaluates to a number, between 0 and 1\. This indicates the percentage match of attributes required for two schemas to have the same flavor. If omitted, it defaults to 0.6.
    * `num_sample_values`: (Optional) An integer, or an expression that evaluates to an integer. This indicates the maximum number of sample values to be returned for each attribute, providing examples of the data format. If omitted, it defaults to 5.
* Return Value:

  * An array of one or more objects, each of which contains an inferred schema in [JSON Schema](http://json-schema.org/documentation.html)format. For details of the schema, refer to the SQL++ for Query [INFER statement](../n1ql/n1ql-language-reference/infer.md).
  * Returns an empty array if `collection` is MISSING or NULL.
  * Returns an error if `collection` is not an array or multiset.
  * Returns an error if `parameters` is not an object.
  * Returns a warning if `similarity_metric` is not a number.
  * Returns a warning if `num_sample_values` is not a number.
  * Returns a warning if the argument name provided is not recognized by array\_infer\_schema
* Example 1:  
Infer schemas from an array or multiset.  
array_infer_schema([{"a": 1},{"a":"aval"},{"a":[1,2]}], {"similarity_metric": 0.6});
* The expected result is:  
[  
  {  
    "#docs": 1,  
    "%docs": 33.33333333333333,  
    "type": "object",  
    "Flavor": "",  
    "properties": {  
      "a": {  
        "#docs": 1,  
        "%docs": 100,  
        "type": "array",  
        "samples": [  
          [  
            1,  
            2  
          ]  
        ],  
        "maxItems": 2,  
        "minItems": 2,  
        "items": "number"  
      }  
    }  
  },  
  {  
    "#docs": 1,  
    "%docs": 33.33333333333333,  
    "type": "object",  
    "Flavor": "'a' = \"aval\"",  
    "properties": {  
      "a": {  
        "#docs": 1,  
        "%docs": 100,  
        "type": "string",  
        "samples": [  
          "aval"  
        ]  
      }  
    }  
  },  
  {  
    "#docs": 1,  
    "%docs": 33.33333333333333,  
    "type": "object",  
    "Flavor": "'a' = 1",  
    "properties": {  
      "a": {  
        "#docs": 1,  
        "%docs": 100,  
        "type": "number",  
        "samples": [  
          1  
        ]  
      }  
    }  
  }  
]  
The function detects that the input data has three flavors of document: one where `a` is 1, one where `a` is `"aval"`, and one where `a` is an array. All documents are objects, and each document only has the `a` property.
* Example 2:  
Infer the schema of the `customers` collection using a subquery.  
array_infer_schema((SELECT VALUE c FROM customers as c), {"num_sample_values": 3});
* The expected result is:  
[  
  {  
    "#docs": 7,  
    "%docs": 100,  
    "type": "object",  
    "Flavor": "",  
    "properties": {  
      "address": {  
        "#docs": 7,  
        "%docs": 100,  
        "type": "object",  
        "samples": [  
          {  
            "street": "690 River St.",  
            "city": "Hanover, MA",  
            "zipcode": "02340"  
          },  
          {  
            "street": "201 Main St.",  
            "city": "St. Louis, MO",  
            "zipcode": "63101"  
          },  
          {  
            "street": "120 Harbor Blvd.",  
            "city": "Boston, MA",  
            "zipcode": "02115"  
          }  
        ],  
        "properties": {  
          "city": {  
            "#docs": 7,  
            "%docs": 100,  
            "type": "string",  
            "samples": [  
              "Boston, MA",  
              "Hanover, MA",  
              "St. Louis, MO"  
            ]  
          },  
          "street": {  
            "#docs": 7,  
            "%docs": 100,  
            "type": "string",  
            "samples": [  
              "201 Main St.",  
              "690 River St.",  
              "120 Harbor Blvd."  
            ]  
          },  
          "zipcode": {  
            "#docs": 6,  
            "%docs": 85.71428571428571,  
            "type": "string",  
            "samples": [  
              "02115",  
              "02340",  
              "63101"  
            ]  
          }  
        }  
      },  
      "custid": {  
        "#docs": 7,  
        "%docs": 100,  
        "type": "string",  
        "samples": [  
          "C13",  
          "C25",  
          "C37"  
        ]  
      },  
      "name": {  
        "#docs": 7,  
        "%docs": 100,  
        "type": "string",  
        "samples": [  
          "T. Cody",  
          "T. Henry",  
          "M. Sinclair"  
        ]  
      },  
      "rating": {  
        "#docs": 6,  
        "%docs": 85.71428571428571,  
        "type": "number",  
        "samples": [  
          640,  
          690,  
          750  
        ]  
      }  
    }  
  }  
]  
The function detects that this collection has only one flavor of document. All documents are objects, and each document has the following properties: `custid` (string), `name` (string), `rating` (number), and `address` (object), which in turn contains the properties `city` (string), `street` (string), and `zipcode` (string).

## [](#ConditionalFunctions)Conditional Functions

### [](#if%5Fnull-ifnull)if\_null (ifnull)

* Syntax:  
if_null(expression1, expression2, ... expressionN)
* Finds first argument which value is not `null` and returns that value
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * a `null` if all arguments evaluate to `null` or no arguments specified
  * a value of the first non-`null` argument otherwise
* Example:  
{  
    "a": if_null(),  
    "b": if_null(null),  
    "c": if_null(null, "analytics"),  
    "d": is_missing(if_null(missing))  
};
* The expected result is:  
{ "a": null, "b": null, "c": "analytics", "d": true }

The function has an alias `ifnull`.

### [](#if%5Fmissing-ifmissing)if\_missing (ifmissing)

* Syntax:  
if_missing(expression1, expression2, ... expressionN)
* Finds first argument which value is not `missing` and returns that value
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * a `null` if all arguments evaluate to `missing` or no arguments specified
  * a value of the first non-`missing` argument otherwise
* Example:  
{  
    "a": if_missing(),  
    "b": if_missing(missing),  
    "c": if_missing(missing, "analytics"),  
    "d": if_missing(null, "analytics")  
};
* The expected result is:  
{ "a": null, "b": null, "c": "analytics", "d": null }

The function has an alias `ifmissing`.

### [](#if%5Fmissing%5For%5Fnull-ifmissingornull-coalesce)if\_missing\_or\_null (ifmissingornull, coalesce)

* Syntax:  
if_missing_or_null(expression1, expression2, ... expressionN)
* Finds first argument which value is not `null` or `missing` and returns that value
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * a `null` if all arguments evaluate to either `null` or `missing`, or no arguments specified
  * a value of the first non-`null`, non-`missing` argument otherwise
* Example:  
{  
    "a": if_missing_or_null(),  
    "b": if_missing_or_null(null, missing),  
    "c": if_missing_or_null(null, missing, "analytics")  
};
* The expected result is:  
{ "a": null, "b": null, "c": "analytics" }

The function has two aliases: `ifmissingornull` and `coalesce`.

### [](#if%5Finf-ifinf)if\_inf (ifinf)

* Syntax:  
if_inf(expression1, expression2, ... expressionN)
* Finds first argument which is a non-infinite (`INF` or`-INF`) number
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * a `missing` if `missing` argument was encountered before the first non-infinite number argument
  * a `null` if `null` argument or any other non-number argument was encountered before the first non-infinite number argument
  * the first non-infinite number argument otherwise
* Example:  
{  
    "a": is_null(if_inf(null)),  
    "b": is_missing(if_inf(missing)),  
    "c": is_null(if_inf(double("INF"))),  
    "d": if_inf(1, null, missing) ],  
    "e": is_null(if_inf(null, missing, 1)) ],  
    "f": is_missing(if_inf(missing, null, 1)) ],  
    "g": if_inf(float("INF"), 1) ],  
    "h": to_string(if_inf(float("INF"), double("NaN"), 1)) ]  
};
* The expected result is:  
{ "a": true, "b": true, "c": true, "d": 1, "e": true, "f": true, "g": 1, "h": "NaN" }

The function has an alias `ifinf`.

### [](#if%5Fnan-ifnan)if\_nan (ifnan)

* Syntax:  
if_nan(expression1, expression2, ... expressionN)
* Finds first argument which is a non-`NaN` number
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * a `missing` if `missing` argument was encountered before the first non-`NaN` number argument
  * a `null` if `null` argument or any other non-number argument was encountered before the first non-`NaN` number argument
  * the first non-`NaN` number argument otherwise
* Example:  
{  
    "a": is_null(if_nan(null)),  
    "b": is_missing(if_nan(missing)),  
    "c": is_null(if_nan(double("NaN"))),  
    "d": if_nan(1, null, missing) ],  
    "e": is_null(if_nan(null, missing, 1)) ],  
    "f": is_missing(if_nan(missing, null, 1)) ],  
    "g": if_nan(float("NaN"), 1) ],  
    "h": to_string(if_nan(float("NaN"), double("INF"), 1)) ]  
};
* The expected result is:  
{ "a": true, "b": true, "c": true, "d": 1, "e": true, "f": true, "g": 1, "h": "INF" }

The function has an alias `ifnan`.

### [](#if%5Fnan%5For%5Finf-ifnanorinf)if\_nan\_or\_inf (ifnanorinf)

* Syntax:  
if_nan_or_inf(expression1, expression2, ... expressionN)
* Finds first argument which is a non-infinite (`INF` or`-INF`) and non-`NaN` number
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * a `missing` if `missing` argument was encountered before the first non-infinite and non-`NaN` number argument
  * a `null` if `null` argument or any other non-number argument was encountered before the first non-infinite and non-`NaN` number argument
  * the first non-infinite and non-`NaN` number argument otherwise
* Example:  
{  
    "a": is_null(if_nan_or_inf(null)),  
    "b": is_missing(if_nan_or_inf(missing)),  
    "c": is_null(if_nan_or_inf(double("NaN"), double("INF"))),  
    "d": if_nan_or_inf(1, null, missing) ],  
    "e": is_null(if_nan_or_inf(null, missing, 1)) ],  
    "f": is_missing(if_nan_or_inf(missing, null, 1)) ],  
    "g": if_nan_or_inf(float("NaN"), float("INF"), 1) ],  
};
* The expected result is:  
{ "a": true, "b": true, "c": true, "d": 1, "e": true, "f": true, "g": 1 }

The function has an alias `ifnanorinf`.

### [](#null%5Fif-nullif)null\_if (nullif)

* Syntax:  
null_if(expression1, expression2)
* Compares two arguments and returns `null` if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * `missing` if any argument is a `missing` value,
  * `null` if

    * any argument is a `null` value but no argument is a `missing` value, or
    * `argument1` \= `argument2`
  * a value of the first argument otherwise
* Example:  
{  
    "a": null_if("analytics", "analytics"),  
    "b": null_if(1, 2)  
};
* The expected result is:  
{ "a": null, "b": 1 }

The function has an alias `nullif`.

### [](#missing%5Fif-missingif)missing\_if (missingif)

* Syntax:  
missing_if(expression1, expression2)
* Compares two arguments and returns `missing` if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * `missing` if

    * any argument is a `missing` value, or
    * no argument is a `null` value and `argument1` \= `argument2`
  * `null` if any argument is a `null` value but no argument is a `missing` value
  * a value of the first argument otherwise
* Example:  
{  
    "a": missing_if("analytics", "analytics")  
    "b": missing_if(1, 2),  
};
* The expected result is:  
{ "b": 1 }

The function has an alias `missingif`.

### [](#nan%5Fif-nanif)nan\_if (nanif)

* Syntax:  
nan_if(expression1, expression2)
* Compares two arguments and returns `NaN` value if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value
  * `NaN` value of type `double` if `argument1` \= `argument2`
  * a value of the first argument otherwise
* Example:  
{  
    "a": to_string(nan_if("analytics", "analytics")),  
    "b": nan_if(1, 2)  
};
* The expected result is:  
{ "a": "NaN", "b": 1 }

The function has an alias `nanif`.

### [](#posinf%5Fif-posinfif)posinf\_if (posinfif)

* Syntax:  
posinf_if(expression1, expression2)
* Compares two arguments and returns `+INF` value if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value
  * `+INF` value of type `double` if `argument1` \= `argument2`
  * a value of the first argument otherwise
* Example:  
{  
    "a": to_string(posinf_if("analytics", "analytics")),  
    "b": posinf_if(1, 2)  
};
* The expected result is:  
{ "a": "+INF", "b": 1 }

The function has an alias `posinfif`.

### [](#neginf%5Fif-neginfif)neginf\_if (neginfif)

* Syntax:  
neginf_if(expression1, expression2)
* Compares two arguments and returns `-INF` value if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression (any type is allowed).
* Return Value:

  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value
  * `-INF` value of type `double` if `argument1` \= `argument2`
  * a value of the first argument otherwise
* Example:  
{  
    "a": to_string(neginf_if("analytics", "analytics")),  
    "b": neginf_if(1, 2)  
};
* The expected result is:  
{ "a": "-INF", "b": 1 }

The function has an alias `neginfif`.

## [](#EnvFunctions)Environment and Identifier Functions

### [](#meta)meta

* Syntax:  
meta(expr)  
meta()
* Return a metadata object for a stored document.
* Arguments:

  * `expr` : an expression returning a stored document
  * none, if the stored document can be determined from the context
* Return Value:

  * a metadata object containing fields `id`, `vbid`, `seq`, `cas`, and `flags`.

### [](#uuid)uuid

* Syntax:  
uuid()
* Generates a `uuid`.
* Arguments:

  * none
* Return Value:

  * a generated, random `uuid`.

## [](#JSONFunctions)JSON Functions

### [](#decode%5Fjson)decode\_json

* Syntax:  
decode_json(expr)
* Unmarshals the JSON-encoded string into a SQL++ value.
* Arguments:

  * `expr`: a JSON-encoded string.
* Return Value:

  * A SQL++ value.
  * If `expr` is NULL or an empty string then NULL is returned.
  * If `expr` is MISSING then MISSING is returned.
* Example:  
decode_json("{\"abc\":1,\"def\":2}");
* The expected result is:  
{  
  "abc": 1,  
  "def": 2  
}

### [](#encode%5Fjson)encode\_json

* Syntax:  
encode_json(expr)
* Marshals the SQL++ value into a JSON-encoded string.
* Arguments:

  * `expr`: a SQL++ value.
* Return Value:

  * A JSON-encoded string.
  * If `expr` is NULL then NULL is returned.
  * If `expr` is MISSING then MISSING is returned.
* Example:  
encode_json({"abc":1,"def":2});
* The expected result is:  
"{ \"abc\": 1, \"def\": 2 }"

### [](#encoded%5Fsize)encoded\_size

* Syntax:  
encoded_size(expr)
* Returns the number of bytes in an uncompressed JSON encoding of the value. The exact size is implementation-dependent.
* Arguments:

  * `expr`: a SQL++ value.
* Return Value:

  * An integer. Never MISSING or NULL. Returns 0 for MISSING.
* Example:  
encoded_size({"abc":1,"def":2});
* The expected result is:  
22

## [](#BitwiseFunctions)Bitwise Functions

All Bit/Binary functions can only operate on 64-bit signed integers.

> [!NOTE]
> All non-integer numbers and other data types result in null.

> [!NOTE]
> The query language uses two’s complement representation.

When looking at the value in binary form, bit 1 is the Least Significant Bit (LSB) and bit 32 is the Most Significant Bit (MSB).

(MSB) Bit 32 → `0000 0000 0000 0000 0000 0000 0000 0000` ← Bit 1 (LSB)

### [](#bitand)bitand

* Syntax:  
BITAND(int_value1, int_value2, ... , int_valueN)
* Returns the result of a bitwise AND operation performed on all input integer values.  
The bitwise AND operation compares each bit of `int_value1` to the corresponding bit of every other `int_value`. If all bits are 1, then the corresponding result bit is set to 1; otherwise it is set to 0 (zero).
* Arguments:

  * `int_valueI`: Integers, or any valid expressions which evaluate to integers, that are used to compare.
* Return Value:

  * An integer, representing the bitwise AND between all of the input integers.
* Limitations:

  * Input values must be integers (such as 1 or 1.0) and cannot contain decimals (such as 1.2).
* Example 1:  
Compare 3 (0011 in binary) and 6 (0110 in binary).  
{ "BitAND": BITAND(3,6) };
* The expected result is:  
{ "BitAND": 2 }  
This results in 2 (0010 in binary) because only bit 2 is set in both 3 (00**1**1) and 6 (01**1**0).
* Example 2:  
Compare 4.5 and 3 (0011 in binary).  
{ "BitAND": BITAND(4.5,3) };
* The expected result is:  
{ "BitAND": null }  
The result is null because 4.5 is not an integer.
* Example 3:  
Compare 4.0 (0100 in binary) and 3 (0011 in binary).  
{ "BitAND": BITAND(4.0,3) };
* The expected result is:  
{ "BitAND": 0 }  
This results in 0 (zero) because 4.0 (0100) and 3 (0011) do not share any bits that are both 1.
* Example 4:  
Compare 3 (0011 in binary) and 6 (0110 in binary) and 15 (1111 in binary).  
{ "BitAND": BITAND(3,6,15) };
* The expected result is:  
{ "BitAND": 2 }  
This results in 2 (0010 in binary) because only the 2nd bit from the right is 1 in all three numbers.

### [](#bitclear)bitclear

* Syntax:  
BITCLEAR(int_value, positions)
* Returns the result after clearing the specified bit, or array of bits in `int_value` using the given `positions`.  
> [!NOTE]  
> Specifying a negative or zero bit position makes the function return a null.
* Arguments:

  * `int_value`: An integer, or any valid expression which evaluates to an integer, that contains the target bit or bits to clear.
  * `positions`: An integer or an array of integers specifying the position or positions to be cleared.
* Return Value:

  * An integer, representing the result after clearing the bit or bits specified.
* Limitations:

  * Input values must be integers (such as 1 or 1.0) and cannot contain decimals (such as 1.2).
* Example 1:  
Clear bit 1 from 6 (0110 in binary).  
{ "BitCLEAR": BITCLEAR(6,1) };
* The expected result is:  
{ "BitCLEAR": 6 }  
This results in 6 (011**0** in binary) because bit 1 was already zero.
* Example 2:  
Clear bits 1 and 2 from 6 (01**10** in binary).  
{ "BitCLEAR": BITCLEAR(6,[1,2]) };
* The expected result is:  
{ "BitCLEAR": 4 }  
This results in 4 (01**0**0 in binary) because bit 2 changed to zero.
* Example 3:  
Clear bits 1, 2, 4, and 5 from 31 (0**11**1**11** in binary).  
{ "BitCLEAR": BITCLEAR(31,[1,2,4,5]) };
* The expected result is:  
{ "BitCLEAR": 4 }  
This results in 4 (0**00**1**00**) because bits 1, 2, 4, and 5 changed to zero.

### [](#bitnot)bitnot

* Syntax:  
BITNOT(int_value)
* Returns the results of a bitwise logical NOT operation performed on an integer value.  
The bitwise logical NOT operation reverses the bits in the value. For each value bit that is 1, the corresponding result bit will be set to 0 (zero); and for each value bit that is 0 (zero), the corresponding result bit will be set to 1.  
> [!NOTE]  
> All bits of the integer will be altered by this operation.
* Arguments:

  * `int_value`: An integer, or any valid expression which evaluates to an integer, that contains the target bits to reverse.
* Return Value:

  * An integer, representing the result after performing the logical NOT operation.
* Limitations:

  * Input values must be integers (such as 1 or 1.0) and cannot contain decimals (such as 1.2).
* Example 1:  
Perform the NOT operation on 3 (0000 0000 0000 0000 0000 0000 0000 0011 in binary).  
{ "BitNOT": BITNOT(3) };
* The expected result is:  
{ "BitNOT": -4 }  
This results in -4 (**1111 1111 1111 1111 1111 1111 1111 1100** in binary) because all bits changed.

### [](#bitor)bitor

* Syntax:  
BITOR(int_value1, int_value2, ... , int_valueN)
* Returns the result of a bitwise inclusive OR operation performed on all input integer values.  
The bitwise inclusive OR operation compares each bit of `int_value1` to the corresponding bit of every other `int_value`. If any bit is 1, the corresponding result bit is set to 1; otherwise, it is set to 0 (zero).
* Arguments:

  * `int_valueI`: Integers, or any valid expressions which evaluate to integers, that are used to compare.
* Return Value:

  * An integer, representing the bitwise OR between all of the input integers.
* Limitations:

  * Input values must be integers (such as 1 or 1.0) and cannot contain decimals (such as 1.2).
* Example 1:  
Perform OR on 3 (0011 in binary) and 6 (0110 in binary).  
{ "BitOR": BITOR(3,6) };
* The expected result is:  
{ "BitOR": 7 }  
This results in 7 (0**111** in binary) because at least 1 bit of each (00**11** and 0**11**0) is 1 in bits 1, 2, and 3.
* Example 2:  
Perform OR on 3 (0011 in binary) and -4 (1000 0000 0000 …​ 0000 1100 in binary).  
{ "BitOR": BITOR(3,-4) };
* The expected result is:  
{ "BitOR": -1 }  
This results in -1 (**1111 1111 1111 …​ 1111 1111** in binary) because the two 1 bits in 3 fill in the two 0 bits in -4 to turn on all the bits.
* Example 3:  
Perform OR on 3 (0011 in binary) and 6 (0110 in binary) and 15 (1111 in binary).  
{ "BitOR": BITOR(3,6,15) };
* The expected result is:  
{ "BitOR": 15 }  
This results in 15 (1111 in binary) because there is at least one 1 in each of the four rightmost bits.

### [](#bitset)bitset

* Syntax:  
BITSET(int_value, positions)
* Returns the result after setting the specified bit `position`, or array of bit positions, to 1 in the given `int_value`.  
> [!NOTE]  
> Specifying a negative or zero position makes the function return a null.
* Arguments:

  * `int_value`: An integer, or any valid expression which evaluates to an integer, that contains the target bit or bits to set.
  * `positions`: An integer or an array of integers specifying the position or positions to be set.
* Return Value:

  * An integer, representing the result after setting the bit or bits specified. If the bit is already set, then it stays set.
* Limitations:

  * Input values must be integers (such as 1 or 1.0) and cannot contain decimals (such as 1.2).
* Example 1:  
Set bit 1 in the value 6 (011**0** in binary).  
{ "BitSET": BITSET(6,1) };
* The expected result is:  
{ "BitSET": 7 }  
This results in 7 (011**1** in binary) because bit 1 changed to 1.
* Example 2:  
Set bits 1 and 2 in the value 6 (01**10** in binary).  
{ "BitSET": BITSET(6,[1,2]) };
* The expected result is:  
{ "BitSET": 7 }  
This also results in 7 (01**11** in binary) because bit 1 changed while bit 2 remained the same.
* Example 3:  
Set bits 1 and 4 in the value 6 (**0**11**0** in binary).  
{ "BitSET": BITSET(6,[1,4]) };
* The expected result is:  
{ "BitSET": 15 }  
This results in 15 (**1**11**1** in binary) because bit 1 and 4 changed to ones.

### [](#bitshift)bitshift

* Syntax:  
BITSHIFT(int_value, shift_amount[, rotate])
* Returns the result of a bit shift operation performed on the integer value `int_value`. The `shift_amount` supports left and right shifts. These are logical shifts. The third parameter `rotate` supports circular shift. This is similar to the BitROTATE function in Oracle.
* Arguments:

  * `int_value`: An integer, or any valid expression which evaluates to an integer, that contains the target bit or bits to shift.
  * `shift_amount`: An integer, or any valid expression which evaluates to an integer, that contains the number of bits to shift.

    * A positive (+) number means this is a LEFT shift.
    * A negative (-) number means this is a RIGHT shift.
  * `rotate`: (Optional) A boolean, or any valid expression which evaluates to a boolean, where:

    * FALSE means this is a LOGICAL shift, where bits shifted off the end of a value are considered lost.
    * TRUE means this is a CIRCULAR shift (shift-and-rotate operation), where bits shifted off the end of a value are rotated back onto the value at the _other_ end. In other words, the bits rotate in what might be thought of as a circular pattern; therefore, these bits are not lost.  
  If omitted, the default is FALSE.  
For comparison, see the below table.

+

| Input             | Shift | Result of Logical Shift (Rotate FALSE) | Result of Circular Shift (Rotate TRUE)         |
| ----------------- | ----- | -------------------------------------- | ---------------------------------------------- |
| 6 (0000 0110)     | 4     | 96 (0110 0000)                         | 96 (0110 0000)                                 |
| 6 (0000 0110)     | 3     | 48 (0011 0000)                         | 48 (0011 0000)                                 |
| 6 (0000 0110)     | 2     | 24 (0001 1000)                         | 24 (0001 1000)                                 |
| 6 (0000 0110)     | 1     | 12 (0000 1100)                         | 12 (0000 1100)                                 |
| **6 (0000 0110)** | **0** | **6 (0000 0110)**                      | **6 (0000 0110)**                              |
| 6 (0000 0110)     | \-1   | 3 (0000 0011)                          | 3 (0000 0011)                                  |
| 6 (0000 0110)     | \-2   | 1 (0000 0001)                          | \-9223372036854775807 (1000 0000 …​ 0000 0001) |
| 6 (0000 0110)     | \-3   | 0 (0000 0000)                          | \-4611686018427387904 (1100 0000 …​ 0000 0000) |
| 6 (0000 0110)     | \-4   | 0 (0000 0000)                          | 6917529027641081856 (0110 0000 …​ 0000 0000)   |
* Return Value:

  * An integer, representing the result of either a logical or circular shift of the given integer.
* Limitations:

  * Input values must be integers (such as 1 or 1.0) and cannot contain decimals (such as 1.2).
* Example 1:  
Logical left shift of the number 6 (0110 in binary) by one bit.  
{ "BitSHIFT": BITSHIFT(6,1,FALSE) };
* The expected result is:  
{ "BitSHIFT": 12 }  
This results in 12 (1100 in binary) because the 1-bits moved from positions 2 and 3 to positions 3 and 4.
* Example 2:  
Logical right shift of the number 6 (0110 in binary) by two bits.  
{ "BitSHIFT": BITSHIFT(6,-2) };
* The expected result is:  
{ "BitSHIFT": 1 }  
This results in 1 (0001 in binary) because the 1-bit in position 3 moved to position 1 and the 1-bit in position 2 was dropped.
* Example 2b:  
Circular right shift of the number 6 (0110 in binary) by two bits.  
{ "BitSHIFT": BITSHIFT(6,-2,TRUE) };
* The expected result is:  
{ "BitSHIFT": -9223372036854775807 }  
This results in -9223372036854775807 (1100 0000 0000 0000 0000 0000 0000 0000 in binary) because the two 1-bits wrapped right, around to the Most Significant Digit position and changed the integer’s sign to negative.
* Example 3:  
Circular left shift of the number 524288 (1000 0000 0000 0000 0000 in binary) by 45 bits.  
{ "BitSHIFT": BITSHIFT(524288,45,TRUE) };
* The expected result is:  
{ "BitSHIFT": 1 }  
This results in 1 because the 1-bit wrapped left, around to the Least Significant Digit position.

### [](#bittest)bittest

* Syntax:  
BITTEST(int_value, positions [, all_set])
* Returns TRUE if the specified bit, or bits, is a 1; otherwise, returns FALSE if the specified bit, or bits, is a 0 (zero).  
> [!NOTE]  
> Specifying a negative or zero bit position will result in null being returned.
* Arguments:

  * `int_value`: An integer, or any valid expression which evaluates to an integer, that contains the target bit or bits to test.
  * `positions`: An integer or an array of integers specifying the position or positions to be tested.
  * `all_set`: (Optional) A boolean, or any valid expression which evaluates to a boolean.

    * When `all_set` is FALSE, then it returns TRUE even if one bit in one of the positions is set.
    * When `all_set` is TRUE, then it returns TRUE only if all input positions are set.  
If omitted, the default is FALSE.
* Return Value:

  * A boolean, that follows the below table:

| int\_value                     | all\_set | Return Value |
| ------------------------------ | -------- | ------------ |
| _all_ specified bits are TRUE  | FALSE    | TRUE         |
| _all_ specified bits are TRUE  | TRUE     | TRUE         |
| _some_ specified bits are TRUE | FALSE    | TRUE         |
| _some_ specified bits are TRUE | TRUE     | FALSE        |
* Limitations:

  * Input values must be integers (such as 1 or 1.0) and cannot contain decimals (such as 1.2).
* Example 1:  
In the number 6 (0110 in binary), is bit 1 set?  
{ "IsBitSET": ISBITSET(6,1) };
* The expected result is:  
{ "IsBitSET": false }  
This returns FALSE because bit 1 of 6 (011**0** in binary) is not set to 1.
* Example 2:  
In the number 1, is either bit 1 or bit 2 set?  
{ "BitTEST": BITTEST(1,[1,2],FALSE) };
* The expected result is:  
{ "BitTEST": true }  
This returns TRUE because bit 1 of the number 1 (000**1** in binary) is set to 1.
* Example 3:  
In the number 6 (0110 in binary), are both bits 2 and 3 set?  
{ "IsBitSET": ISBITSET(6,[2,3],TRUE) };
* The expected result is:  
{ "IsBitSET": true }  
This returns TRUE because both bits 2 and 3 in the number 6 (0**11**0 in binary) are set to 1.
* Example 4:  
In the number 6 (0110 in binary), are all the bits in positions 1 through 3 set?  
{ "BitTEST": BITTEST(6,[1,3],TRUE) };
* The expected result is:  
{ "BitTEST": false }  
This returns FALSE because bit 1 in the number 6 (011**0** in binary) is set to 0 (zero).

The function has an alias `isbitset`.

### [](#bitxor)bitxor

* Syntax:  
BITXOR(int_value1, int_value2, ... , int_valueN)
* Returns the result of a bitwise Exclusive OR operation performed on two or more integer values.  
The bitwise Exclusive OR operation compares each bit of `int_value1` to the corresponding bit of `int_value2`.  
If there are more than two input values, the first two are compared; then their result is compared to the next input value; and so on.  
When the compared bits do not match, the result bit is 1; otherwise, the compared bits do match, and the result bit is 0 (zero), as summarized:

| Bit 1 | Bit 2 | XOR Result Bit |
| ----- | ----- | -------------- |
| 0     | 0     | 0              |
| 0     | 1     | 1              |
| 1     | 0     | 1              |
| 1     | 1     | 0              |
* Arguments:

  * `int_valueI`: Integers, or any valid expressions which evaluate to integers, that are used to compare.
* Return Value:

  * An integer, representing the bitwise XOR between the input integers.
* Limitations:

  * Input values must be integers (such as 1 or 1.0) and cannot contain decimals (such as 1.2).
* Example 1:  
Perform the XOR operation on 3 (0011 in binary) and 6 (0110 in binary).  
{ "BitXOR": BITXOR(3,6) };
* The expected result is:  
{ "BitXOR": 5 }  
This returns 5 (0101 in binary) because the 1st bit pair and 3rd bit pair are different (resulting in 1) while the 2nd bit pair and 4th bit pair are the same (resulting in 0):  
0011 (3)  
0110 (6)  
====  
0101 (5)
* Example 2:  
Perform the XOR operation on 3 (0011 in binary) and 6 (0110 in binary) and 15 (1111 in binary).  
{ "BitXOR": BITXOR(3,6,15) };
* The expected result is:  
{ "BitXOR": 10 }  
This returns 10 (1010 in binary) because 3 XOR 6 equals 5 (0101 in binary), and then 5 XOR 15 equals 10 (1010 in binary).

## [](#WindowFunctions)Window Functions

Window functions are used to compute an aggregate or cumulative value, based on a portion of the tuples selected by a query. For each input tuple, a movable window of tuples is defined. The window determines the tuples to be used by the window function.

The tuples are not grouped into a single output tuple — each tuple remains separate in the query output.

All window functions must be used with an OVER clause. Refer to [Window Queries](3%5Fquery.html#Over%5Fclauses) for details.

Window functions cannot appear in the FROM clause clause or LIMIT clause.

### [](#cume%5Fdist)cume\_dist

* Syntax:  
CUME_DIST() OVER ([window-partition-clause] [window-order-clause])
* Returns the percentile rank of the current tuple as part of the cumulative distribution — that is, the number of tuples ranked lower than or equal to the current tuple, including the current tuple, divided by the total number of tuples in the window partition.  
The window order clause determines the sort order of the tuples. If the window order clause is omitted, the function returns the same result (1.0) for each tuple.
* Arguments:

  * None.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
* Return Value:

  * A number greater than 0 and less than or equal to 1\. The higher the value, the higher the ranking.
* Example:  
For each customer, find the cumulative distribution of all orders by order number.  
FROM orders AS o  
SELECT o.custid, o.orderno, CUME_DIST() OVER (  
  PARTITION BY o.custid  
  ORDER BY o.orderno  
) AS `rank`  
ORDER BY o.custid, o.orderno;
* The expected result is:  
[  
  {  
    "rank": 0.25,  
    "custid": "C13",  
    "orderno": 1002  
  },  
  {  
    "rank": 0.5,  
    "custid": "C13",  
    "orderno": 1007  
  },  
  {  
    "rank": 0.75,  
    "custid": "C13",  
    "orderno": 1008  
  },  
  {  
    "rank": 1,  
    "custid": "C13",  
    "orderno": 1009  
  },  
  {  
    "rank": 1,  
    "custid": "C31",  
    "orderno": 1003  
  },  
  {  
    "rank": 1,  
    "custid": "C35",  
    "orderno": 1004  
  },  
  {  
    "rank": 1,  
    "custid": "C37",  
    "orderno": 1005  
  },  
  {  
    "rank": 0.5,  
    "custid": "C41",  
    "orderno": 1001  
  },  
  {  
    "rank": 1,  
    "custid": "C41",  
    "orderno": 1006  
  }  
]

### [](#dense%5Frank)dense\_rank

* Syntax:  
DENSE_RANK() OVER ([window-partition-clause] [window-order-clause])
* Returns the dense rank of the current tuple — that is, the number of distinct tuples preceding this tuple in the current window partition, plus one.  
The tuples are ordered by the window order clause. If any tuples are tied, they will have the same rank. If the window order clause is omitted, the function returns the same result (1) for each tuple.  
For this function, when any tuples have the same rank, the rank of the next tuple will be consecutive, so there will not be a gap in the sequence of returned values. For example, if there are five tuples ranked 3, the next dense rank is 4.
* Arguments:

  * None.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
* Return Value:

  * An integer, greater than or equal to 1.
* Example:  
Find the dense rank of all orders by number of items.  
FROM orders AS o  
SELECT o.orderno, LEN(o.items) AS items,  
DENSE_RANK() OVER (  
  ORDER BY LEN(o.items)  
) AS `rank`  
ORDER BY `rank`, o.orderno;
* The expected result is:  
[  
  {  
    "items": 0,  
    "rank": 1,  
    "orderno": 1009  
  },  
  {  
    "items": 1,  
    "rank": 2,  
    "orderno": 1008  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1001  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1002  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1003  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1004  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1007  
  },  
  {  
    "items": 3,  
    "rank": 4,  
    "orderno": 1006  
  },  
  {  
    "items": 4,  
    "rank": 5,  
    "orderno": 1005  
  }  
]

### [](#first%5Fvalue)first\_value

* Syntax:  
FIRST_VALUE(expr) [nulls-modifier] OVER (window-definition)
* Returns the requested value from the first tuple in the current window frame, where the window frame is specified by the window definition.
* Arguments:

  * `expr`: The value that you want to return from the first tuple in the window frame. \[[1](#fn%5F1)\]
* Modifiers:

  * [NULLS Modifier](3%5Fquery.html#Window%5Ffunction%5Foptions): (Optional) Determines how NULL or MISSING values are treated when finding the first value in the window frame.

    * `IGNORE NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are ignored when finding the first tuple. In this case, the function returns the first non-NULL, non-MISSING value.
    * `RESPECT NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are included when finding the first tuple.  
If this modifier is omitted, the default is `RESPECT NULLS`.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
  * (Optional) [Window Frame Clause](3%5Fquery.html#Window%5Fframe%5Fclause).
* Return Value:

  * The specified value from the first tuple. The order of the tuples is determined by the window order clause.
  * NULL, if the frame was empty or if all values were NULL or MISSING and the `IGNORE NULLS` modifier was specified.
  * In the following cases, this function may return unpredictable results.

    * If the window order clause is omitted.
    * If the window frame is defined by `ROWS`, and there are tied tuples in the window frame.
  * To make the function return deterministic results, add a window order clause, or add further ordering terms to the window order clause so that no tuples are tied.
  * If the window frame is defined by `RANGE` or `GROUPS`, and there are tied tuples in the window frame, the function returns the first value of the input expression.
* Example:  
For each order, show the customer and the value, including the value of the smallest order from that customer.  
FROM orders AS o  
LET revenue = ROUND((  
  FROM o.items  
  SELECT VALUE SUM(qty * price)  
)[0], 2)  
SELECT o.custid, o.orderno, revenue,  
FIRST_VALUE(revenue) OVER (  
  PARTITION BY o.custid  
  ORDER BY revenue  
) AS smallest_order;
* The expected result is:  
[  
  {  
    "custid": "C13",  
    "orderno": 1009,  
    "revenue": null,  
    "smallest_order": null  
  },  
  {  
    "custid": "C13",  
    "orderno": 1007,  
    "revenue": 130.45,  
    "smallest_order": null  
  },  
  {  
    "custid": "C13",  
    "orderno": 1008,  
    "revenue": 1999.8,  
    "smallest_order": null  
  },  
  {  
    "custid": "C13",  
    "orderno": 1002,  
    "revenue": 10906.55,  
    "smallest_order": null  
  },  
  {  
    "custid": "C31",  
    "orderno": 1003,  
    "revenue": 477.95,  
    "smallest_order": 477.95  
  },  
  {  
    "custid": "C35",  
    "orderno": 1004,  
    "revenue": 199.94,  
    "smallest_order": 199.94  
  },  
  {  
    "custid": "C37",  
    "orderno": 1005,  
    "revenue": 4639.92,  
    "smallest_order": 4639.92  
  },  
  {  
    "custid": "C41",  
    "orderno": 1001,  
    "revenue": 157.73,  
    "smallest_order": 157.73  
  },  
  {  
    "custid": "C41",  
    "orderno": 1006,  
    "revenue": 18847.58,  
    "smallest_order": 157.73  
  }  
]

### [](#lag)lag

* Syntax:  
LAG(expr[, offset[, default]]) [nulls-modifier] OVER ([window-partition-clause] [window-order-clause])
* Returns the value from a tuple at a given offset prior to the current tuple position.  
The window order clause determines the sort order of the tuples. If the window order clause is omitted, the return values may be unpredictable.
* Arguments:

  * `expr`: The value that you want to return from the offset tuple. \[[1](#fn%5F1)\]
  * `offset`: (Optional) A positive integer. If omitted, the default is 1.
  * `default`: (Optional) The value to return when the offset goes out of partition scope. If omitted, the default is NULL.
* Modifiers:

  * [NULLS Modifier](3%5Fquery.html#Window%5Ffunction%5Foptions): (Optional) Determines how NULL or MISSING values are treated when finding the offset tuple in the window partition.

    * `IGNORE NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are ignored when finding the offset tuple.
    * `RESPECT NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are included when finding the offset tuple.  
If this modifier is omitted, the default is `RESPECT NULLS`.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
* Return Value:

  * The specified value from the offset tuple.
  * If the offset tuple is out of partition scope, it returns the default value, or NULL if no default is specified.
* Example:  
For each order, show the customer and the value, including the value of the next-smallest order from that customer.  
FROM orders AS o  
LET revenue = ROUND((  
  FROM o.items  
  SELECT VALUE SUM(qty * price)  
)[0], 2)  
SELECT o.custid, o.orderno, revenue,  
LAG(revenue, 1, "No smaller order") OVER (  
  PARTITION BY o.custid  
  ORDER BY revenue  
) AS next_smallest_order;
* The expected result is:  
[  
  {  
    "custid": "C13",  
    "orderno": 1009,  
    "revenue": null,  
    "next_smallest_order": "No smaller order"  
  },  
  {  
    "custid": "C13",  
    "orderno": 1007,  
    "revenue": 130.45,  
    "next_smallest_order": null  
  },  
  {  
    "custid": "C13",  
    "orderno": 1008,  
    "revenue": 1999.8,  
    "next_smallest_order": 130.45  
  },  
  {  
    "custid": "C13",  
    "orderno": 1002,  
    "revenue": 10906.55,  
    "next_smallest_order": 1999.8  
  },  
  {  
    "custid": "C31",  
    "orderno": 1003,  
    "revenue": 477.95,  
    "next_smallest_order": "No smaller order"  
  },  
  {  
    "custid": "C35",  
    "orderno": 1004,  
    "revenue": 199.94,  
    "next_smallest_order": "No smaller order"  
  },  
  {  
    "custid": "C37",  
    "orderno": 1005,  
    "revenue": 4639.92,  
    "next_smallest_order": "No smaller order"  
  },  
  {  
    "custid": "C41",  
    "orderno": 1001,  
    "revenue": 157.73,  
    "next_smallest_order": "No smaller order"  
  },  
  {  
    "custid": "C41",  
    "orderno": 1006,  
    "revenue": 18847.58,  
    "next_smallest_order": 157.73  
  }  
]

### [](#last%5Fvalue)last\_value

* Syntax:  
LAST_VALUE(expr) [nulls-modifier] OVER (window-definition)
* Returns the requested value from the last tuple in the current window frame, where the window frame is specified by the window definition.
* Arguments:

  * `expr`: The value that you want to return from the last tuple in the window frame. \[[1](#fn%5F1)\]
* Modifiers:

  * [NULLS Modifier](3%5Fquery.html#Window%5Ffunction%5Foptions): (Optional) Determines how NULL or MISSING values are treated when finding the last tuple in the window frame.

    * `IGNORE NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are ignored when finding the last tuple. In this case, the function returns the last non-NULL, non-MISSING value.
    * `RESPECT NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are included when finding the last tuple.  
If this modifier is omitted, the default is `RESPECT NULLS`.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
  * (Optional) [Window Frame Clause](3%5Fquery.html#Window%5Fframe%5Fclause).
* Return Value:

  * The specified value from the last tuple. The order of the tuples is determined by the window order clause.
  * NULL, if the frame was empty or if all values were NULL or MISSING and the `IGNORE NULLS` modifier was specified.
  * In the following cases, this function may return unpredictable results.

    * If the window order clause is omitted.
    * If the window frame clause is omitted.
    * If the window frame is defined by `ROWS`, and there are tied tuples in the window frame.
  * To make the function return deterministic results, add a window order clause, or add further ordering terms to the window order clause so that no tuples are tied.
  * If the window frame is defined by `RANGE` or `GROUPS`, and there are tied tuples in the window frame, the function returns the last value of the input expression.
* Example:  
For each order, show the customer and the value, including the value of the largest order from that customer.  
FROM orders AS o  
LET revenue = ROUND((  
  FROM o.items  
  SELECT VALUE SUM(qty * price)  
)[0], 2)  
SELECT o.custid, o.orderno, revenue,  
LAST_VALUE(revenue) OVER (  
  PARTITION BY o.custid  
  ORDER BY revenue  
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING -- ➊  
) AS largest_order;
* The expected result is:  
[  
  {  
    "custid": "C13",  
    "orderno": 1009,  
    "revenue": null,  
    "largest_order": 10906.55  
  },  
  {  
    "custid": "C13",  
    "orderno": 1007,  
    "revenue": 130.45,  
    "largest_order": 10906.55  
  },  
  {  
    "custid": "C13",  
    "orderno": 1008,  
    "revenue": 1999.8,  
    "largest_order": 10906.55  
  },  
  {  
    "custid": "C13",  
    "orderno": 1002,  
    "revenue": 10906.55,  
    "largest_order": 10906.55  
  },  
  {  
    "custid": "C31",  
    "orderno": 1003,  
    "revenue": 477.95,  
    "largest_order": 477.95  
  },  
  {  
    "custid": "C35",  
    "orderno": 1004,  
    "revenue": 199.94,  
    "largest_order": 199.94  
  },  
  {  
    "custid": "C37",  
    "orderno": 1005,  
    "revenue": 4639.92,  
    "largest_order": 4639.92  
  },  
  {  
    "custid": "C41",  
    "orderno": 1001,  
    "revenue": 157.73,  
    "largest_order": 18847.58  
  },  
  {  
    "custid": "C41",  
    "orderno": 1006,  
    "revenue": 18847.58,  
    "largest_order": 18847.58  
  }  
]  
➀ This clause specifies that the window frame should extend to the end of the window partition. Without this clause, the end point of the window frame would always be the current tuple. This would mean that the largest order would always be the same as the current order.

### [](#lead)lead

* Syntax:  
LEAD(expr[, offset[, default]]) [nulls-modifier] OVER ([window-partition-clause] [window-order-clause])
* Returns the value from a tuple at a given offset ahead of the current tuple position.  
The window order clause determines the sort order of the tuples. If the window order clause is omitted, the return values may be unpredictable.
* Arguments:

  * `expr`: The value that you want to return from the offset tuple. \[[1](#fn%5F1)\]
  * `offset`: (Optional) A positive integer. If omitted, the default is 1.
  * `default`: (Optional) The value to return when the offset goes out of window partition scope. If omitted, the default is NULL.
* Modifiers:

  * [NULLS Modifier](3%5Fquery.html#Window%5Ffunction%5Foptions): (Optional) Determines how NULL or MISSING values are treated when finding the offset tuple in the window partition.

    * `IGNORE NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are ignored when finding the offset tuple.
    * `RESPECT NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are included when finding the offset tuple.  
If this modifier is omitted, the default is `RESPECT NULLS`.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
* Return Value:

  * The specified value from the offset tuple.
  * If the offset tuple is out of partition scope, it returns the default value, or NULL if no default is specified.
* Example:  
For each order, show the customer and the value, including the value of the next-largest order from that customer.  
FROM orders AS o  
LET revenue = ROUND((  
  FROM o.items  
  SELECT VALUE SUM(qty * price)  
)[0], 2)  
SELECT o.custid, o.orderno, revenue,  
LEAD(revenue, 1, "No larger order") OVER (  
  PARTITION BY o.custid  
  ORDER BY revenue  
) AS next_largest_order;
* The expected result is:  
[  
  {  
    "custid": "C13",  
    "orderno": 1009,  
    "revenue": null,  
    "next_largest_order": 130.45  
  },  
  {  
    "custid": "C13",  
    "orderno": 1007,  
    "revenue": 130.45,  
    "next_largest_order": 1999.8  
  },  
  {  
    "custid": "C13",  
    "orderno": 1008,  
    "revenue": 1999.8,  
    "next_largest_order": 10906.55  
  },  
  {  
    "custid": "C13",  
    "orderno": 1002,  
    "revenue": 10906.55,  
    "next_largest_order": "No larger order"  
  },  
  {  
    "custid": "C31",  
    "orderno": 1003,  
    "revenue": 477.95,  
    "next_largest_order": "No larger order"  
  },  
  {  
    "custid": "C35",  
    "orderno": 1004,  
    "revenue": 199.94,  
    "next_largest_order": "No larger order"  
  },  
  {  
    "custid": "C37",  
    "orderno": 1005,  
    "revenue": 4639.92,  
    "next_largest_order": "No larger order"  
  },  
  {  
    "custid": "C41",  
    "orderno": 1001,  
    "revenue": 157.73,  
    "next_largest_order": 18847.58  
  },  
  {  
    "custid": "C41",  
    "orderno": 1006,  
    "revenue": 18847.58,  
    "next_largest_order": "No larger order"  
  }  
]

### [](#nth%5Fvalue)nth\_value

* Syntax:  
NTH_VALUE(expr, offset) [from-modifier] [nulls-modifier] OVER (window-definition)
* Returns the requested value from a tuple in the current window frame, where the window frame is specified by the window definition.
* Arguments:

  * `expr`: The value that you want to return from the offset tuple in the window frame. \[[1](#fn%5F1)\]
  * `offset`: The number of the offset tuple within the window frame, counting from 1.
* Modifiers:

  * [FROM Modifier](3%5Fquery.html#Window%5Ffunction%5Foptions): (Optional) Determines where the function starts counting the offset.

    * `FROM FIRST`: Counting starts at the first tuple in the window frame. In this case, an offset of 1 is the first tuple in the window frame, 2 is the second tuple, and so on.
    * `FROM LAST`: Counting starts at the last tuple in the window frame. In this case, an offset of 1 is the last tuple in the window frame, 2 is the second-to-last tuple, and so on.  
  The order of the tuples is determined by the window order clause. If this modifier is omitted, the default is `FROM FIRST`.
  * [NULLS Modifier](3%5Fquery.html#Window%5Ffunction%5Foptions): (Optional) Determines how NULL or MISSING values are treated when finding the offset tuple in the window frame.

    * `IGNORE NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are ignored when finding the offset tuple.
    * `RESPECT NULLS`: If the values for any tuples evaluate to NULL or MISSING, those tuples are included when finding the offset tuple.  
If this modifier is omitted, the default is `RESPECT NULLS`.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
  * (Optional) [Window Frame Clause](3%5Fquery.html#Window%5Fframe%5Fclause).
* Return Value:

  * The specified value from the offset tuple.
  * In the following cases, this function may return unpredictable results.

    * If the window order clause is omitted.
    * If the window frame is defined by `ROWS`, and there are tied tuples in the window frame.
  * To make the function return deterministic results, add a window order clause, or add further ordering terms to the window order clause so that no tuples are tied.
  * If the window frame is defined by `RANGE` or `GROUPS`, and there are tied tuples in the window frame, the function returns the first value of the input expression when counting `FROM FIRST`, or the last value of the input expression when counting `FROM LAST`.
* Example 1:  
For each order, show the customer and the value, including the value of the second smallest order from that customer.  
FROM orders AS o  
LET revenue = ROUND((  
  FROM o.items  
  SELECT VALUE SUM(qty * price)  
)[0], 2)  
SELECT o.custid, o.orderno, revenue,  
NTH_VALUE(revenue, 2) FROM FIRST OVER (  
  PARTITION BY o.custid  
  ORDER BY revenue  
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING -- ➊  
) AS smallest_order_but_1;
* The expected result is:  
[  
  {  
    "custid": "C13",  
    "orderno": 1009,  
    "revenue": null,  
    "smallest_order_but_1": 130.45  
  },  
  {  
    "custid": "C13",  
    "orderno": 1007,  
    "revenue": 130.45, // ➋  
    "smallest_order_but_1": 130.45  
  },  
  {  
    "custid": "C13",  
    "orderno": 1008,  
    "revenue": 1999.8,  
    "smallest_order_but_1": 130.45  
  },  
  {  
    "custid": "C13",  
    "orderno": 1002,  
    "revenue": 10906.55,  
    "smallest_order_but_1": 130.45  
  },  
  {  
    "custid": "C31",  
    "orderno": 1003,  
    "revenue": 477.95,  
    "smallest_order_but_1": null  
  },  
  {  
    "custid": "C35",  
    "orderno": 1004,  
    "revenue": 199.94,  
    "smallest_order_but_1": null  
  },  
  {  
    "custid": "C37",  
    "orderno": 1005,  
    "revenue": 4639.92,  
    "smallest_order_but_1": null  
  },  
  {  
    "custid": "C41",  
    "orderno": 1001,  
    "revenue": 157.73,  
    "smallest_order_but_1": 18847.58  
  },  
  {  
    "custid": "C41",  
    "orderno": 1006,  
    "revenue": 18847.58, // ➋  
    "smallest_order_but_1": 18847.58  
  }  
]  
➀ This clause specifies that the window frame should extend to the end of the window partition. Without this clause, the end point of the window frame would always be the current tuple. This would mean that for the smallest order, the function would be unable to find the route with the second smallest order.  
➁ The second smallest order from this customer.
* Example 2:  
For each order, show the customer and the value, including the value of the second largest order from that customer.  
FROM orders AS o  
LET revenue = ROUND((  
  FROM o.items  
  SELECT VALUE SUM(qty * price)  
)[0], 2)  
SELECT o.custid, o.orderno, revenue,  
NTH_VALUE(revenue, 2) FROM LAST OVER (  
  PARTITION BY o.custid  
  ORDER BY revenue  
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING -- ➊  
) AS largest_order_but_1;
* The expected result is:  
[  
  {  
    "custid": "C13",  
    "orderno": 1002,  
    "revenue": 10906.55,  
    "largest_order_but_1": 1999.8  
  },  
  {  
    "custid": "C13",  
    "orderno": 1008,  
    "revenue": 1999.8, // ➋  
    "largest_order_but_1": 1999.8  
  },  
  {  
    "custid": "C13",  
    "orderno": 1007,  
    "revenue": 130.45,  
    "largest_order_but_1": 1999.8  
  },  
  {  
    "custid": "C13",  
    "orderno": 1009,  
    "revenue": null,  
    "largest_order_but_1": 1999.8  
  },  
  {  
    "custid": "C31",  
    "orderno": 1003,  
    "revenue": 477.95,  
    "largest_order_but_1": null  
  },  
  {  
    "custid": "C35",  
    "orderno": 1004,  
    "revenue": 199.94,  
    "largest_order_but_1": null  
  },  
  {  
    "custid": "C37",  
    "orderno": 1005,  
    "revenue": 4639.92,  
    "largest_order_but_1": null  
  },  
  {  
    "custid": "C41",  
    "orderno": 1006,  
    "revenue": 18847.58,  
    "largest_order_but_1": 157.73  
  },  
  {  
    "custid": "C41",  
    "orderno": 1001,  
    "revenue": 157.73, // ➋  
    "largest_order_but_1": 157.73  
  }  
]  
➀ This clause specifies that the window frame should extend to the end of the window partition. Without this clause, the end point of the window frame would always be the current tuple. This would mean the function would be unable to find the second largest order for smaller orders.  
➁ The second largest order from this customer.

### [](#ntile)ntile

* Syntax:  
NTILE(num_tiles) OVER ([window-partition-clause] [window-order-clause])
* Divides the window partition into the specified number of tiles, and allocates each tuple in the window partition to a tile, so that as far as possible each tile has an equal number of tuples. When the set of tuples is not equally divisible by the number of tiles, the function puts more tuples into the lower-numbered tiles. For each tuple, the function returns the number of the tile into which that tuple was placed.  
The window order clause determines the sort order of the tuples. If the window order clause is omitted then the tuples are processed in an undefined order.
* Arguments:

  * `num_tiles`: The number of tiles into which you want to divide the window partition. This argument can be an expression and must evaluate to a number. If the number is not an integer, it will be truncated.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
* Return Value:

  * An value greater than or equal to 1 and less than or equal to the number of tiles.
* Example:  
Allocate each order to one of three tiles by value.  
FROM orders AS o  
LET revenue = ROUND((  
  FROM o.items  
  SELECT VALUE SUM(qty * price)  
)[0], 2)  
SELECT o.orderno, revenue,  
NTILE(3) OVER (  
  ORDER BY revenue  
) AS `ntile`;
* The expected result is:  
[  
  {  
    "ntile": 1,  
    "orderno": 1009,  
    "revenue": null  
  },  
  {  
    "ntile": 1,  
    "orderno": 1007,  
    "revenue": 130.45  
  },  
  {  
    "ntile": 1,  
    "orderno": 1001,  
    "revenue": 157.73  
  },  
  {  
    "ntile": 2,  
    "orderno": 1004,  
    "revenue": 199.94  
  },  
  {  
    "ntile": 2,  
    "orderno": 1003,  
    "revenue": 477.95  
  },  
  {  
    "ntile": 2,  
    "orderno": 1008,  
    "revenue": 1999.8  
  },  
  {  
    "ntile": 3,  
    "orderno": 1005,  
    "revenue": 4639.92  
  },  
  {  
    "ntile": 3,  
    "orderno": 1002,  
    "revenue": 10906.55  
  },  
  {  
    "ntile": 3,  
    "orderno": 1006,  
    "revenue": 18847.58  
  }  
]

### [](#percent%5Frank)percent\_rank

* Syntax:  
PERCENT_RANK() OVER ([window-partition-clause] [window-order-clause])
* Returns the percentile rank of the current tuple — that is, the rank of the tuples minus one, divided by the total number of tuples in the window partition minus one.  
The window order clause determines the sort order of the tuples. If the window order clause is omitted, the function returns the same result (0) for each tuple.
* Arguments:

  * None.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
* Return Value:

  * A number between 0 and 1\. The higher the value, the higher the ranking.
* Example:  
For each customer, find the percentile rank of all orders by order number.  
FROM orders AS o  
SELECT o.custid, o.orderno, PERCENT_RANK() OVER (  
  PARTITION BY o.custid  
  ORDER BY o.orderno  
) AS `rank`;
* The expected result is:  
[  
  {  
    "rank": 0,  
    "custid": "C13",  
    "orderno": 1002  
  },  
  {  
    "rank": 0.3333333333333333,  
    "custid": "C13",  
    "orderno": 1007  
  },  
  {  
    "rank": 0.6666666666666666,  
    "custid": "C13",  
    "orderno": 1008  
  },  
  {  
    "rank": 1,  
    "custid": "C13",  
    "orderno": 1009  
  },  
  {  
    "rank": 0,  
    "custid": "C31",  
    "orderno": 1003  
  },  
  {  
    "rank": 0,  
    "custid": "C35",  
    "orderno": 1004  
  },  
  {  
    "rank": 0,  
    "custid": "C37",  
    "orderno": 1005  
  },  
  {  
    "rank": 0,  
    "custid": "C41",  
    "orderno": 1001  
  },  
  {  
    "rank": 1,  
    "custid": "C41",  
    "orderno": 1006  
  }  
]

### [](#rank)rank

* Syntax:  
RANK() OVER ([window-partition-clause] [window-order-clause])
* Returns the rank of the current tuple — that is, the number of distinct tuples preceding this tuple in the current window partition, plus one.  
The tuples are ordered by the window order clause. If any tuples are tied, they will have the same rank. If the window order clause is omitted, the function returns the same result (1) for each tuple.  
When any tuples have the same rank, the rank of the next tuple will include all preceding tuples, so there may be a gap in the sequence of returned values. For example, if there are five tuples ranked 3, the next rank is 8.  
To avoid gaps in the returned values, use the DENSE\_RANK() function instead.
* Arguments:

  * None.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
* Return Value:

  * An integer, greater than or equal to 1.
* Example:  
Find the rank of all orders by number of items.  
FROM orders AS o  
SELECT o.orderno, LEN(o.items) AS items,  
RANK() OVER (  
  ORDER BY LEN(o.items)  
) AS `rank`;
* The expected result is:  
[  
  {  
    "items": 0,  
    "rank": 1,  
    "orderno": 1009  
  },  
  {  
    "items": 1,  
    "rank": 2,  
    "orderno": 1008  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1004  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1007  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1002  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1001  
  },  
  {  
    "items": 2,  
    "rank": 3,  
    "orderno": 1003  
  },  
  {  
    "items": 3,  
    "rank": 8,  
    "orderno": 1006  
  },  
  {  
    "items": 4,  
    "rank": 9,  
    "orderno": 1005  
  }  
]

### [](#ratio%5Fto%5Freport)ratio\_to\_report

* Syntax:  
RATIO_TO_REPORT(expr) OVER (window-definition)
* Returns the fractional ratio of the specified value for each tuple to the sum of values for all tuples in the window frame.
* Arguments:

  * `expr`: The value for which you want to calculate the fractional ratio. \[[1](#fn%5F1)\]
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
  * (Optional) [Window Frame Clause](3%5Fquery.html#Window%5Fframe%5Fclause).
* Return Value:

  * A number between 0 and 1, representing the fractional ratio of the value for the current tuple to the sum of values for all tuples in the current window frame. The sum of returned values for all tuples in the current window frame is 1.
  * If the input expression does not evaluate to a number, or the sum of values for all tuples is zero, it returns NULL.
* Example:  
For each customer, calculate the value of each order as a fraction of the total value of all orders.  
FROM orders AS o  
LET revenue = ROUND((  
  FROM o.items  
  SELECT VALUE SUM(qty * price)  
)[0], 2)  
SELECT o.custid, o.orderno,  
RATIO_TO_REPORT(revenue) OVER (  
  PARTITION BY o.custid  
) AS fractional_ratio;
* The expected result is:  
[  
  {  
    "custid": "C13",  
    "orderno": 1007,  
    "fractional_ratio": 0.010006289887088855  
  },  
  {  
    "custid": "C13",  
    "orderno": 1002,  
    "fractional_ratio": 0.8365971710849288  
  },  
  {  
    "custid": "C13",  
    "orderno": 1009,  
    "fractional_ratio": null  
  },  
  {  
    "custid": "C13",  
    "orderno": 1008,  
    "fractional_ratio": 0.15339653902798234  
  },  
  {  
    "custid": "C31",  
    "orderno": 1003,  
    "fractional_ratio": 1  
  },  
  {  
    "custid": "C35",  
    "orderno": 1004,  
    "fractional_ratio": 1  
  },  
  {  
    "custid": "C37",  
    "orderno": 1005,  
    "fractional_ratio": 1  
  },  
  {  
    "custid": "C41",  
    "orderno": 1006,  
    "fractional_ratio": 0.9917007404772666  
  },  
  {  
    "custid": "C41",  
    "orderno": 1001,  
    "fractional_ratio": 0.008299259522733382  
  }  
]

### [](#row%5Fnumber)row\_number

* Syntax:  
ROW_NUMBER() OVER ([window-partition-clause] [window-order-clause])
* Returns a unique row number for every tuple in every window partition. In each window partition, the row numbering starts at 1.  
The window order clause determines the sort order of the tuples. If the window order clause is omitted, the return values may be unpredictable.
* Arguments:

  * None.
* Clauses:

  * (Optional) [Window Partition Clause](3%5Fquery.html#Window%5Fpartition%5Fclause).
  * (Optional) [Window Order Clause](3%5Fquery.html#Window%5Forder%5Fclause).
* Return Value:

  * An integer, greater than or equal to 1.
* Example:  
For each customer, number all orders by value.  
FROM orders AS o  
LET revenue = ROUND((  
  FROM o.items  
  SELECT VALUE SUM(qty * price)  
)[0], 2)  
SELECT o.custid, o.orderno,  
ROW_NUMBER() OVER (  
  PARTITION BY o.custid  
  ORDER BY revenue  
) AS `row`;
* The expected result is:  
[  
  {  
    "row": 1,  
    "custid": "C13",  
    "orderno": 1009  
  },  
  {  
    "row": 2,  
    "custid": "C13",  
    "orderno": 1007  
  },  
  {  
    "row": 3,  
    "custid": "C13",  
    "orderno": 1008  
  },  
  {  
    "row": 4,  
    "custid": "C13",  
    "orderno": 1002  
  },  
  {  
    "row": 1,  
    "custid": "C31",  
    "orderno": 1003  
  },  
  {  
    "row": 1,  
    "custid": "C35",  
    "orderno": 1004  
  },  
  {  
    "row": 1,  
    "custid": "C37",  
    "orderno": 1005  
  },  
  {  
    "row": 1,  
    "custid": "C41",  
    "orderno": 1001  
  },  
  {  
    "row": 2,  
    "custid": "C41",  
    "orderno": 1006  
  }  
]

---

1. If the query contains the GROUP BY clause or any [aggregate functions](#AggregateFunctions), this expression must only depend on GROUP BY expressions or aggregate functions.