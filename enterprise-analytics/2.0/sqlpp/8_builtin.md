[View original HTML](/enterprise-analytics/2.0/sqlpp/8_builtin.html)

> This section introduces the builtin SQL++ for Enterprise Analytics functions. 

For reference, a categorized list of all of the builtin functions follows. Use the category linked at the end of each list for descriptions and examples of those functions.

Some of the examples in this section assume that you’re using a database called `sampleAnalytics` and a scope called `Commerce`. See [intro:connecting-to-data-sources.adoc#install-the-commerce-dataset-in-standalone-collections](../intro/connecting-to-data-sources.md#install-the-commerce-dataset-in-standalone-collections) to install the Commerce dataset.

## [](#numeric-functions)Numeric Functions

|       |         |       |         |       |
| ----- | ------- | ----- | ------- | ----- |
| abs   | acos    | asin  | atan    | atan2 |
| ceil  | cos     | cosh  | degrees | e     |
| exp   | floor   | ln    | log     | pi    |
| power | radians | round | sign    | sin   |
| sinh  | sqrt    | tan   | tanh    | trunc |

See [Numeric Functions](8%5Fbuiltin%5Fnum.md).

## [](#string-functions)String Functions

|                  |                 |              |                    |              |
| ---------------- | --------------- | ------------ | ------------------ | ------------ |
| concat           | contains        | ends\_with   | initcap (or title) | length       |
| lower            | ltrim           | position     | regexp\_contains   | regexp\_like |
| regexp\_position | regexp\_replace | repeat       | replace            | reverse      |
| rtrim            | split           | starts\_with | substr             | trim         |

See [String Functions](8%5Fbuiltin%5Fstr.md).

## [](#temporal-functions)Temporal Functions

|                           |                             |                       |                                     |                                         |
| ------------------------- | --------------------------- | --------------------- | ----------------------------------- | --------------------------------------- |
| now\_local (clock\_local) | now\_millis (clock\_millis) | now\_str (clock\_str) | now\_tz (clock\_tz)                 | now\_utc (clock\_utc)                   |
| date\_add\_millis         | date\_add\_str              | date\_diff\_millis    | date\_diff\_str                     | date\_format\_str                       |
| date\_part\_millis        | date\_part\_str             | date\_range\_millis   | date\_range\_str                    | date\_trunc\_millis                     |
| date\_trunc\_str          | duration\_to\_str           | millis                | millis\_to\_str (millis\_to\_local) | millis\_to\_tz (millis\_to\_zone\_name) |
| millis\_to\_utc           | str\_to\_duration           | str\_to\_millis       | str\_to\_utc                        | str\_to\_tz (str\_to\_zone\_name)       |

See [Temporal Functions](8%5Fbuiltin%5Ftemp.md).

## [](#object-functions)Object Functions

|             |                |                |                 |                |
| ----------- | -------------- | -------------- | --------------- | -------------- |
| object\_add | object\_concat | object\_length | object\_names   | object\_pairs  |
| object\_put | object\_rename | object\_remove | object\_replace | object\_unwrap |

See [Object Functions](8%5Fbuiltin%5Fobj.md).

## [](#aggregate-functions)Aggregate Functions

|                     |                      |                     |                   |                  |
| ------------------- | -------------------- | ------------------- | ----------------- | ---------------- |
| array\_count        | array\_avg           | array\_sum          | array\_min        | array\_max       |
| array\_stddev\_samp | array\_stddev\_pop   | array\_var\_samp    | array\_var\_pop   | array\_skewness  |
| array\_kurtosis     | strict\_count        | strict\_avg         | strict\_sum       | strict\_min      |
| strict\_max         | strict\_stddev\_samp | strict\_stddev\_pop | strict\_var\_samp | strict\_var\_pop |

See [Aggregate Functions](8%5Fbuiltin%5Fagg.md).

## [](#array-functions)Array Functions

|                |                |                  |                 |                 |
| -------------- | -------------- | ---------------- | --------------- | --------------- |
| array\_append  | array\_concat  | array\_contains  | array\_distinct | array\_flatten  |
| array\_ifnull  | array\_insert  | array\_intersect | array\_length   | array\_position |
| array\_prepend | array\_put     | array\_range     | array\_remove   | array\_repeat   |
| array\_replace | array\_reverse | array\_sort      | array\_star     | array\_symdiff  |

See [Array Functions](8%5Fbuiltin%5Farr.md).

## [](#comparison-functions)Comparison Functions

greatest

least

See [Comparison Functions](8%5Fbuiltin%5Fcomp.md).

## [](#type-functions)Type Functions

|                      |                       |                        |                        |                      |
| -------------------- | --------------------- | ---------------------- | ---------------------- | -------------------- |
| is\_array            | is\_multiset          | is\_atomic (is\_atom)  | is\_Boolean (is\_bool) | is\_number (is\_num) |
| is\_object (is\_obj) | is\_string (is\_str)  | is\_null               | is\_missing            | is\_unknown          |
| to\_array            | to\_atomic (to\_atom) | to\_boolean (to\_bool) | to\_bigint             | to\_double           |
| to\_number (to\_num) | to\_object (to\_obj)  | to\_string (to\_str)   | typename               | array\_infer\_schema |

See [Type Functions](8%5Fbuiltin%5Ftype.md).

## [](#conditional-functions)Conditional Functions

|                               |                         |                                                   |                 |                       |
| ----------------------------- | ----------------------- | ------------------------------------------------- | --------------- | --------------------- |
| if\_null (ifnull)             | if\_missing (ifmissing) | if\_missing\_or\_null (ifmissingornull, coalesce) | if\_inf (ifinf) | if\_nan (ifnan)       |
| if\_nan\_or\_inf (ifnanorinf) | null\_if (nullif)       | missing\_if (missingif)                           | nan\_if (nanif) | posinf\_if (posinfif) |

See [Conditional Functions](8%5Fbuiltin%5Fcond.md).

## [](#environment-and-identifier-functions)Environment and Identifier Functions

meta

uuid

See [Environment and Identifier Functions](8%5Fbuiltin%5Fenv.md).

## [](#json-functions)JSON Functions

decode\_json

encode\_json

encoded\_size

See [JSON Functions](8%5Fbuiltin%5Fjson.md).

## [](#bitwise-functions)Bitwise Functions

|        |          |        |       |        |
| ------ | -------- | ------ | ----- | ------ |
| bitand | bitclear | bitnot | bitor | bitset |

See [Bitwise Functions](8%5Fbuiltin%5Fbit.md).

## [](#window-functions)Window Functions

|            |             |              |               |             |
| ---------- | ----------- | ------------ | ------------- | ----------- |
| cume\_dist | dense\_rank | first\_value | lag           | last\_value |
| lead       | nth\_value  | ntile        | percent\_rank | rank        |

See [Window Functions](8%5Fbuiltin%5Fwin.md).