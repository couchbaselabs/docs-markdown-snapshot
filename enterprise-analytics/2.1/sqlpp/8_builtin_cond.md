---
title: Conditional Functions
description: This topic describes the builtin SQL++ conditional functions for
  Enterprise Analytics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/8_builtin_cond.adoc
  xref: xref:2.1@enterprise-analytics:sqlpp:8_builtin_cond.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sqlpp/8_builtin_cond.html)

# Conditional Functions

> This topic describes the builtin SQL++ conditional functions for Enterprise Analytics. 

## [](#if%5Fnull-ifnull)if\_null (ifnull)

* Syntax:  
if_null(expression1, expression2, ... expressionN)
* Finds first argument whose value is not `null` and returns that value
* Arguments:

  * `expressionI` : an expression of any type.
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

## [](#if%5Fmissing-ifmissing)if\_missing (ifmissing)

* Syntax:  
if_missing(expression1, expression2, ... expressionN)
* Finds first argument whose value is not `missing` and returns that value
* Arguments:

  * `expressionI` : an expression of any type.
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

## [](#if%5Fmissing%5For%5Fnull-ifmissingornull-coalesce)if\_missing\_or\_null (ifmissingornull, coalesce)

* Syntax:  
if_missing_or_null(expression1, expression2, ... expressionN)
* Finds first argument whose value is not `null` or `missing` and returns that value.
* Arguments:

  * `expressionI` : an expression of any type.
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

## [](#if%5Finf-ifinf)if\_inf (ifinf)

* Syntax:  
if_inf(expression1, expression2, ... expressionN)
* Finds first argument which is a non-infinite number (`INF` or `-INF`), while skipping `missing`.
* Arguments:

  * `expressionI` : an expression of any type.
* Return Value:

  * a `null` if `null` argument or any other non-number argument was encountered before the first non-infinite number argument
  * the first non-infinite number argument encountered. Otherwise, `null` is returned
* Example:  
{  
    "a": is_null(if_inf(null, null)),  
    "b": is_null(if_inf(missing, missing)),  
    "c": is_null(if_inf(double("INF"), double("INF"))),  
    "d": if_inf(1, null, missing),  
    "e": is_null(if_inf(null, missing, 1)),  
    "f": is_null(if_inf(missing, null, 1)),  
    "g": if_inf(float("INF"), 1),  
    "h": to_string(if_inf(float("INF"), double("NaN"), 1))  
};
* The expected result is:  
{ "a": true, "b": true, "c": true, "d": 1, "e": true, "f": true, "g": 1, "h": "NaN" }

The function has an alias `ifinf`.

## [](#if%5Fnan-ifnan)if\_nan (ifnan)

* Syntax:  
if_nan(expression1, expression2, ... expressionN)
* Finds first argument which is a non-`NaN` number, while skipping `missing`
* Arguments:

  * `expressionI` : an expression of any type.
* Return Value:

  * a `null` if `null` argument or any other non-number argument was encountered before the first non-`NaN` number argument
  * the first non-`NaN` number argument encountered. Otherwise, `null` is returned
* Example:  
{  
    "a": is_null(if_nan(null, null)),  
    "b": is_null(if_nan(missing, missing)),  
    "c": is_null(if_nan(double("NaN"), double("NaN"))),  
    "d": if_nan(1, null, missing),  
    "e": is_null(if_nan(null, missing, 1)),  
    "f": is_null(if_nan(missing, null, 1)),  
    "g": if_nan(float("NaN"), 1),  
    "h": to_string(if_nan(float("NaN"), double("INF"), 1))  
};
* The expected result is:  
{ "a": true, "b": true, "c": true, "d": 1, "e": true, "f": true, "g": 1, "h": "INF" }

The function has an alias `ifnan`.

## [](#if%5Fnan%5For%5Finf-ifnanorinf)if\_nan\_or\_inf (ifnanorinf)

* Syntax:  
if_nan_or_inf(expression1, expression2, ... expressionN)
* Finds first argument which is a non-infinite (`INF` or `-INF`) and non-`NaN` number, while skipping `missing`
* Arguments:

  * `expressionI` : an expression of any type.
* Return Value:

  * a `null` if `null` argument or any other non-number argument was encountered before the first non-infinite and non-`NaN` number argument
  * the first non-infinite and non-`NaN` number argument encountered. Otherwise `null` is returned
* Example:  
{  
    "a": is_null(if_nan_or_inf(null, null)),  
    "b": is_null(if_nan_or_inf(missing, missing)),  
    "c": is_null(if_nan_or_inf(double("NaN"), double("INF"))),  
    "d": if_nan_or_inf(1, null, missing),  
    "e": is_null(if_nan_or_inf(null, missing, 1)),  
    "f": is_null(if_nan_or_inf(missing, null, 1)),  
    "g": if_nan_or_inf(float("NaN"), float("INF"), 1)  
};
* The expected result is:  
{ "a": true, "b": true, "c": true, "d": 1, "e": true, "f": true, "g": 1 }

The function has an alias `ifnanorinf`.

## [](#null%5Fif-nullif)null\_if (nullif)

* Syntax:  
null_if(expression1, expression2)
* Compares two arguments and returns `null` if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression of any type.
* Return Value:

  * `null` if `argument1` \= `argument2` evaluates to `true`
  * the first argument if `argument1` \= `argument2` evaluates to `false`, `null`, or `missing`
* Example:  
{  
    "a": null_if("analytics", "analytics"),  
    "b": null_if(1, 2),  
    "c": null_if(1, "analytics"),  
    "d": null_if("analytics", 1),  
    "e": null_if(1, null),  
    "f": null_if(1, missing),  
    "g": null_if(null, 1),  
    "h": is_missing(null_if(missing, 1))  
};
* The expected result is:  
{ "a": null, "b": 1, "c": 1, "d": "analytics", "e": 1, "f": 1, "g": null, "h": true }

The function has an alias `nullif`.

## [](#missing%5Fif-missingif)missing\_if (missingif)

* Syntax:  
missing_if(expression1, expression2)
* Compares two arguments and returns `missing` if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression of any type.
* Return Value:

  * `missing` if `argument1` \= `argument2` evaluates to `true`
  * the first argument if `argument1` \= `argument2` evaluates to `false`, `null`, or `missing`
* Example:  
{  
    "a": is_missing(missing_if("analytics", "analytics")),  
    "b": missing_if(1, 2),  
    "c": missing_if(1, "analytics"),  
    "d": missing_if("analytics", 1),  
    "e": missing_if(1, null),  
    "f": missing_if(1, missing),  
    "g": missing_if(null, 1),  
    "h": is_missing(missing_if(missing, 1))  
};
* The expected result is:  
{ "a": true, "b": 1, "c": 1, "d": "analytics", "e": 1, "f": 1, "g": null, "h": true }

The function has an alias `missingif`.

## [](#nan%5Fif-nanif)nan\_if (nanif)

* Syntax:  
nan_if(expression1, expression2)
* Compares two arguments and returns `NaN` value if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression of any type.
* Return Value:

  * `NaN` if `argument1` \= `argument2` evaluates to `true`
  * the first argument if `argument1` \= `argument2` evaluates to `false`, `null`, or `missing`
* Example:  
{  
    "a": to_string(nan_if("analytics", "analytics")),  
    "b": nan_if(1, 2),  
    "c": nan_if(1, "analytics"),  
    "d": nan_if("analytics", 1),  
    "e": nan_if(1, null),  
    "f": nan_if(1, missing),  
    "g": nan_if(null, 1),  
    "h": is_missing(nan_if(missing, 1))  
};
* The expected result is:  
{ "a": "NaN", "b": 1, "c": 1, "d": "analytics", "e": 1, "f": 1, "g": null, "h": true }

The function has an alias `nanif`.

## [](#posinf%5Fif-posinfif)posinf\_if (posinfif)

* Syntax:  
posinf_if(expression1, expression2)
* Compares two arguments and returns `+INF` value if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression of any type.
* Return Value:

  * `+INF` value of type double if `argument1` \= `argument2` evaluates to `true`
  * a value of the first argument otherwise (if `argument1` \= `argument2` evaluates to `false`, `null`, or `missing`)
* Example:  
{  
    "a": to_string(posinf_if("analytics", "analytics")),  
    "b": posinf_if(1, 2),  
    "c": posinf_if(1, "analytics"),  
    "d": posinf_if("analytics", 1),  
    "e": posinf_if(1, null),  
    "f": posinf_if(1, missing),  
    "g": posinf_if(null, 1),  
    "h": is_missing(posinf_if(missing, 1))  
};
* The expected result is:  
{ "a": "+INF", "b": 1, "c": 1, "d": "analytics", "e": 1, "f": 1, "g": null, "h": true }

The function has an alias `posinfif`.

## [](#neginf%5Fif-neginfif)neginf\_if (neginfif)

* Syntax:  
neginf_if(expression1, expression2)
* Compares two arguments and returns `-INF` value if they are equal, otherwise returns the first argument.
* Arguments:

  * `expressionI` : an expression of any type.
* Return Value:

  * `-INF` value of type `double` if `argument1` \= `argument2` evaluates to `true`
  * a value of the first argument if `argument1` \= `argument2` evaluates to `false`, `null`, or `missing`
* Example:  
{  
    "a": to_string(neginf_if("analytics", "analytics")),  
    "b": neginf_if(1, 2),  
    "c": neginf_if(1, "analytics"),  
    "d": neginf_if("analytics", 1),  
    "e": neginf_if(1, null),  
    "f": neginf_if(1, missing),  
    "g": neginf_if(null, 1),  
    "h": is_missing(neginf_if(missing, 1))  
};
* The expected result is:  
{ "a": "-INF", "b": 1, "c": 1, "d": "analytics", "e": 1, "f": 1, "g": null, "h": true }

The function has an alias `neginfif`.