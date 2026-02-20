---
title: Object Functions
description: This topic describes the builtin SQL++ for Enterprise Analytics
  object functions.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/8_builtin_obj.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:sqlpp:8_builtin_obj.adoc[]
---

[View original HTML](/enterprise-analytics/current/sqlpp/8_builtin_obj.html)

# Object Functions

> This topic describes the builtin SQL++ for Enterprise Analytics object functions. 

## [](#object%5Fadd)object\_add

* Syntax:  
object_add(object, new_attr_key, new_attr_value)
* Adds a new field—name-value pair—to a given object. This function does not update an existing field in a given object.
* Arguments:

  * `object`: An object, or an expression that evaluates to an object.
  * `new_attr_key`: A string, or an expression which evaluates to a string, representing a field name.
  * `new_attr_value`: A value, or any expression which evaluates to a value.
* Return Value:

  * The original JSON object, also including the added field.
  * If you add a duplicate field—that is, if the name is found—this function returns the object unmodified.
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

## [](#object%5Fconcat)object\_concat

* Syntax:  
object_concat(obj1, obj2 ...)  
object_concat(array)
* Concatenates the input objects. This function has two possible syntaxes. The first requires any number of object arguments. The second requires a single array argument, containing any number of objects.  
You can use the array syntax in situations where you do not know ahead of time how many input objects there are to concatenate; or where you want to concatenate objects which are generated dynamically, for example by a subquery.
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

## [](#object%5Flength)object\_length

* Syntax:  
object_length(object)
* Counts the number of fields—name-value pairs—in an object.
* Arguments:

  * `object`: An object, or an expression that evaluates to an object.
* Return Value:

  * The number of fields in the object.
* Example:  
object_length({"abc":1, "def":2, "ghi":3});
* The expected result is:  
3

## [](#object%5Fnames)object\_names

* Syntax:  
object_names(object)
* Returns the names of all fields—name-value pairs—in an object.
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

## [](#object%5Fpairs)object\_pairs

* Syntax:  
object_pairs(object)
* Returns the names and values of all fields—name-value pairs—in an object.
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

## [](#object%5Fput)object\_put

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
  * If `attr_value` is MISSING, it deletes the corresponding existing field if any, like `object_remove()`.
* Example:  
object_put({"a": 1, "b": 2}, "a", 3);
* The expected result is:  
{  
  "a": 3,  
  "b": 2  
}

## [](#object%5Frename)object\_rename

* Syntax:  
object_rename(object, old_attr_key, new_attr_key)
* Renames a field—name-value pair—in the JSON input object.
* Arguments:

  * `object`: Any JSON object, or SQL++ expression that can evaluate to a JSON object.
  * `old_attr_key`: A string, or an expression which evaluates to a string, representing the old, original field name inside the JSON object.
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

## [](#object%5Fremove)object\_remove

* Syntax:  
object_remove(object, attr_key)
* Removes the specified field—name-value pair—from the given object.
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

## [](#object%5Freplace)object\_replace

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

## [](#object%5Funwrap)object\_unwrap

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

## [](#object%5Fvalues)object\_values

* Syntax:  
object_values(object)
* Returns the values from all the fields—name-value pairs—in the object.
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