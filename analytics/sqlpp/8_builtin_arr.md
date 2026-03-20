---
title: Array Functions
description: This topic describes the builtin SQL++ for Capella Analytics array functions.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/8_builtin_arr.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:analytics:sqlpp:8_builtin_arr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sqlpp/8_builtin_arr.html)

# Array Functions

> This topic describes the builtin SQL++ for Capella Analytics array functions. Array functions can take multiple arguments—one of which is often an array—and typically produce either another array or a single value. 

## [](#array%5Fappend)array\_append

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

## [](#array%5Fconcat)array\_concat

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

## [](#array%5Fcontains)array\_contains

* Syntax:  
array_contains(list, val)
* Checks whether the input array or multiset contains the value argument. A string value argument is case-sensitive.
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

## [](#array%5Fdistinct)array\_distinct

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

## [](#array%5Fflatten)array\_flatten

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

## [](#array%5Fifnull)array\_ifnull

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

## [](#array%5Finsert)array\_insert

* Syntax:  
array_insert(list, pos, val1, val2, ...)
* Inserts the supplied values into the original array or multiset. Values can be NULL, meaning you can insert NULLs.  
When the input is an array, the supplied values are inserted at the specified position. If the position is positive, the position before the first item is 0, the position before the second item is 1, and so on. If the position is negative, the position before the last item is -1, the position before the second-last item is -2, and so on. For example, in the array \[5,6\], the valid positions are 0, 1, 2, -1, -2\. If the input array or multiset is empty, the only valid position is 0\. If the position is a floating-point number, it’s cast to integer.  
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

## [](#array%5Fintersect)array\_intersect

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

## [](#array%5Flength)array\_length

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

## [](#array%5Fposition)array\_position

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

## [](#array%5Fprepend)array\_prepend

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

## [](#array%5Fput)array\_put

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

## [](#array%5Frange)array\_range

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

## [](#array%5Fremove)array\_remove

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

## [](#array%5Frepeat)array\_repeat

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

## [](#array%5Freplace)array\_replace

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

## [](#array%5Freverse)array\_reverse

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

## [](#array%5Fsort)array\_sort

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

## [](#array%5Fstar)array\_star

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
> In the output object, name-value pairs are ordered by their names, regardless of their original order within the object items in the input array. In example 4, in the output object the pair named `"a"` comes before the pair named `"c"`. However, in the output object, the items within each array are not ordered: they appear in the sequence in which they are found in the input array. So in example 1, the pair named `"a"` has the value `[1, 9]`; the first item in the output array (which is `1`) is taken from the first object in the input array, and so on.

## [](#array%5Fsymdiff)array\_symdiff

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

## [](#array%5Fsymdiffn)array\_symdiffn

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
> Refer to the following article for more information about the difference between a normal and n-ary symdiff: <https://en.wikipedia.org/wiki/Symmetric%5Fdifference>.

## [](#array%5Funion)array\_union

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