---
title: Re-writing Built-in Reduce Functions
description: "Using this model as a template, it is possible to write the full
  implementation of the built-in functions <code>_sum</code> and
  <code>_count</code> when working with the sales data and the standard
  <code>map()</code> function below:"
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/learn/pages/views/views-writing-rewriting.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:learn:views/views-writing-rewriting.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/learn/views/views-writing-rewriting.html)

# Re-writing Built-in Reduce Functions

Using this model as a template, it is possible to write the full implementation of the built-in functions `_sum` and `_count` when working with the sales data and the standard `map()` function below:

function(doc, meta)
{
  emit(meta.id, null);
}

The `_count` function returns a count of all the records for a given key. Since argument for the reduce function contains an array of all the values for a given key, the length of the array needs to be returned in the `reduce()` function:

function(key, values, rereduce) {
   if (rereduce) {
       var result = 0;
       for (var i = 0; i < values.length; i++) {
           result += values[i];
       }
       return result;
   } else {
       return values.length;
   }
}

To explicitly write the equivalent of the built-in `_sum` reduce function, the sum of supplied array of values needs to be returned:

function(key, values, rereduce) {
  var sum = 0;
  for(i=0; i < values.length; i++) {
    sum = sum + values[i];
  }
  return(sum);
}

In the above function, the array of data values is iterated over and added up, with the final value being returned.