---
title: Built-in Utility Functions
description: Utility functions are available that can be used within
  <code>map()</code> and <code>reduce()</code> functions.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/views/views-writing-utility.adoc
  xref: xref:server:learn:views/views-writing-utility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/learn/views/views-writing-utility.html)

# Built-in Utility Functions

> Utility functions are available that can be used within `map()` and `reduce()` functions. 

Couchbase Server incorporates different utility functions beyond the core JavaScript functionality that can be used within `map()` and `reduce()` functions where relevant.

* `dateToArray(date)`

Converts a JavaScript Date object or a valid date string such as "2012-07-30T23:58:22.193Z" into an array of individual date components. For example, the previous string would be converted into a JavaScript array:

[2012, 7, 30, 23, 58, 22]

The function can be particularly useful when building views using dates as the key where the use of a reduce function is being used for counting or rollup.

Currently, the function works only on UTC values. Timezones are not supported.

* `decodeBase64(doc)`

Converts a binary (base64) encoded value stored in the database into a string. This can be useful if you want to output or parse the contents of a document that has not been identified as a valid JSON value.

* `sum(array)`

When supplied with an array containing numerical values, each value is summed and the resulting total is returned.

For example:

sum([12,34,56,78])