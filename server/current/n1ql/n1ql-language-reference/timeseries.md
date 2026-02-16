[View original HTML](/server/current/n1ql/n1ql-language-reference/timeseries.html)

The \_TIMESERIES function enables you to query time series data.

The time series data must be stored in Couchbase time series documents. For more information, see [Store and Process Time Series Data](time-series.md).

The function dynamically generates data point objects from the array of time series data in the input document. For a regular time series, the function uses the time series interval to generate a date-time stamp for each time point automatically.

## [](#syntax)Syntax

_TIMESERIES(_document_, _options_)

### [](#arguments)Arguments

document

An expression resolving to a time series document.

options

A JSON object specifying options for the function.

### [](#options)Options

| Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Schema                                              |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **ts\_data** _optional_     | The path to the time series data in the document. If omitted, the function uses the ts\_data field in the document. If the function cannot find the time series data, the document is ignored. **Default:** ts\_data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String                                              |
| **ts\_interval** _optional_ | The path to the time series interval in the document. If omitted, the function uses the ts\_interval field in the document. If the function cannot find the time series interval, the time series is assumed to be irregular. **Default:** ts\_interval                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String                                              |
| **ts\_start** _optional_    | The path to the start date and time for the document. If omitted, the function uses the ts\_start field in the document. If the function cannot find the start date and time, the document is ignored. **Default:** ts\_start                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String                                              |
| **ts\_end** _optional_      | The path to the end date and time for the document. If omitted, the function uses the ts\_end field in the document. If the function cannot find the end date and time, the document is ignored. **Default:** ts\_end                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String                                              |
| **ts\_keep** _optional_     | Whether the timeline should be removed to save memory. If true, the timeline is kept. **Default:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Boolean                                             |
| **ts\_ranges** _optional_   | One or more date-time ranges, which are used to filter the time series data. Time series data outside the specified range or ranges is filtered out. For a single predicate range, this is an expression resolving to an array containing two integers, both representing milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix%5Ftime). The first value is the start of the filtered time series range, and the second is the end of the filtered time series range. Both values are inclusive. If you need the start of the range to be exclusive, increase the start value by one. If you need the end of the range to be exclusive, decrease the end value by one. Both values must be present. If you need the start of the range to be unbounded, use 0. If you need the end of the range to be unbounded, use [MaxInt64](https://docs.gtk.org/glib/const.MAXINT64.html) — that is, (2^63)-1. To filter on multiple predicate ranges, this option can be an array of arrays, in which each nested array contains a pair of millisecond integers as above. If omitted, the time series data is not filtered. | Array of integers, or array of arrays of integers   |
| **ts\_project** _optional_  | An integer, or an array of integers, indicating which values should be returned for each data point. 0 indicates the first value, 1 the second value, and so on. If omitted, all values are returned for every data point.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Numeric expression, or array of numeric expressions |

## [](#return-values)Return Values

The function returns an array of objects, with one object for each data point in the selected range. Each object has the following fields:

\_t

An integer representing the time at that data point, in milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix%5Ftime).

\_v0, \_v1, …​

The value or values at that time point.

## [](#usage)Usage

You can use the \_TIMESERIES function anywhere in a query, but typically you use it as the right-hand side of an [UNNEST](unnest.md) clause.

You cannot use the \_TIMESERIES function in an index definition.

If your query contains predicates on date-time ranges, and you are using an index for your time series documents, you should include the range predicates in the WHERE clause of the query, as well as the `ts_ranges` option of the \_TIMESERIES function. This pushes the range predicates to the index scan.

A query containing date-time range predicates in both the \_TIMESERIES function and the WHERE clause may become repetitive and hard to understand, especially with complex range predicates. To make your queries easier to read, use a query parameter or common table expression to store the date-time range predicates.

## [](#examples)Examples

Example 1\. Query regular time series data

The following query selects time series data for mean temperatures in the specified time range. Each time series document contains a month’s data.

```sqlpp
WITH docs AS (
  [
    {
      "region": "UK",
      "ts_data": [18.5, 18.5, 18.5, 18.5, 20, 20, 20, 20, 20, 20, 20, 20, 20,
                  20, 20, 20, 20, 20, 20, 20, 20, 16.5, 16.5, 16.5, 16.5, 16.5,
                  16.5, 16.5, 16.5, 16.5, 16.5],
      "ts_end": 1375228800000,
      "ts_start": 1372636800000,
      "ts_interval": 86400000
    },
    {
      "region": "UK",
      "ts_data": [19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5,
                  17, 15.5, 15.5, 15.5, 15.5, 15.5, 15.5, 15.5, 15.5, 15.5,
                  15.5, 15.5, 15.5, 15.5, 15.5, 15.5, 15.5, 14, 14, 14, 14],
      "ts_end": 1377907200000,
      "ts_start": 1375315200000,
      "ts_interval": 86400000
    }
  ]
),
range_start AS (1375056000000),
range_end AS (1375574400000)
SELECT t.* FROM docs AS d
UNNEST _timeseries(d, {"ts_ranges": [range_start, range_end]}) AS t
WHERE d.region = 'UK'
  AND (d.ts_start <= range_end AND d.ts_end >= range_start);
```

Note that the specified range predicate cuts across more than one time series document.

For each time point, the \_TIMESERIES function calculates the date-time stamp `_t` and returns a single value `_v0`.

Results

```json
[
  {
    "_t": 1375056000000,
    "_v0": 16.5
  },
  {
    "_t": 1375142400000,
    "_v0": 16.5
  },
  {
    "_t": 1375228800000,
    "_v0": 16.5
  },
  {
    "_t": 1375315200000,
    "_v0": 19.5
  },
  {
    "_t": 1375401600000,
    "_v0": 19.5
  },
  {
    "_t": 1375488000000,
    "_v0": 19.5
  },
  {
    "_t": 1375574400000,
    "_v0": 19.5
  }
]
```

Example 2\. Query regular time series data with multiple data points

The following query selects time series data for daily low and high temperatures in the specified time range. Each time series document contains a month’s data.

```sqlpp
WITH docs AS (
  [
    {
      "region": "UK",
      "ts_data": [
        [10, 27], [10, 27], [10, 27], [10, 27], [10, 30], [10, 30], [10, 30],
        [10, 30], [10, 30], [10, 30], [10, 30], [10, 30], [10, 30], [10, 30],
        [10, 30], [10, 30], [10, 30], [10, 30], [10, 30], [10, 30], [10, 30],
        [10, 23], [10, 23], [10, 23], [10, 23], [10, 23], [10, 23], [10, 23],
        [10, 23], [10, 23], [10, 23]
      ],
      "ts_end": 1375228800000,
      "ts_start": 1372636800000,
      "ts_interval": 86400000
    },
    {
      "region": "UK",
      "ts_data": [
        [12, 27], [12, 27], [12, 27], [12, 27], [12, 27], [12, 27], [12, 27],
        [12, 27], [12, 27], [12, 27], [12, 22], [9, 22], [9, 22], [9, 22],
        [9, 22], [9, 22], [9, 22], [9, 22], [9, 22], [9, 22], [9, 22],
        [9, 22], [9, 22], [9, 22], [9, 22], [9, 22], [9, 22], [9, 19],
        [9, 19], [9, 19], [9, 19]
      ],
      "ts_end": 1377907200000,
      "ts_start": 1375315200000,
      "ts_interval": 86400000
    }
  ]
),
range_start AS (1375056000000),
range_end AS (1375574400000)
SELECT MILLIS_TO_TZ(t._t,"UTC") AS day, t._v0 AS low, t._v1 AS high
FROM docs AS d
UNNEST _timeseries(d, {"ts_ranges": [range_start, range_end]}) AS t
WHERE d.region = 'UK'
  AND (d.ts_start <= range_end AND d.ts_end >= range_start);
```

Note that the specified time range predicate cuts across more than one time series document.

For each time point, the \_TIMESERIES function calculates the date-time stamp `_t` and returns the values `_v0` and `_v1`.

The query adds aliases to the data returned by the \_TIMESERIES function and converts the date-time stamp to a readable date-time string.

Results

```json
[
  {
    "day": "2013-07-29T00:00:00Z",
    "high": 23,
    "low": 10
  },
  {
    "day": "2013-07-30T00:00:00Z",
    "high": 23,
    "low": 10
  },
  {
    "day": "2013-07-31T00:00:00Z",
    "high": 23,
    "low": 10
  },
  {
    "day": "2013-08-01T00:00:00Z",
    "high": 27,
    "low": 12
  },
  {
    "day": "2013-08-02T00:00:00Z",
    "high": 27,
    "low": 12
  },
  {
    "day": "2013-08-03T00:00:00Z",
    "high": 27,
    "low": 12
  },
  {
    "day": "2013-08-04T00:00:00Z",
    "high": 27,
    "low": 12
  }
]
```

To view the results as a chart:

1. Click **Chart**.
2. In **Chart Type**, select `Multi-Connected Points by Column`.
3. In **X-Axis**, select `day`.
4. In **Y-Values**, select both `high` and `low`.

![Line chart showing high and low temperatures over 7 days](../_images/time-series-regular.svg) 

Example 3\. Query irregular time series data

The following query selects time series data for house sales and prices in the specified time range. Each time series document contains a decade’s data. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

```sqlpp
WITH docs AS (
  [
    {
      "district": "South",
      "ts_data": [
        [852595200000, 69950],
        [852854400000, 67000],
        [884044800000, 71500],
        [884131200000, 73000],
        [884217600000, 72000]
      ],
      "ts_end": 884217600000,
      "ts_start": 852595200000
    },
    {
      "district": "South",
      "ts_data": [
        [978912000000,115000],
        [1010534400000,139950],
        [1073347200000,195000],
        [1105056000000,225000],
        [1136678400000,210000]
      ],
      "ts_end": 1136678400000,
      "ts_start": 978912000000
    },
    {
      "district": "South",
      "ts_data": [
        [1294531200000,200000],
        [1326326400000,212000],
        [1357430400000,171000],
        [1420675200000,252500],
        [1452384000000,330000],
        [1483660800000,290000],
        [1514764800000,325000]
      ],
      "ts_end": 1514764800000,
      "ts_start": 1294531200000
    }
  ]
),
range_start AS (1104537600000),
range_end AS (1419984000000)
SELECT MILLIS_TO_TZ(t._t,"UTC") AS date, t._v0 AS price
FROM docs AS d
UNNEST _timeseries(d, {"ts_ranges": [range_start, range_end]}) AS t
WHERE d.district = 'South'
  AND (d.ts_start <= range_end AND d.ts_end >= range_start);
```

Note that the specified time range cuts across more than one time series document.

For each time point, the \_TIMESERIES function returns the date-time stamp `_t` and a single value `_v0`.

The query adds aliases to the data returned by the \_TIMESERIES function and converts the date-time stamp to a readable date-time string.

Results

```json
[
  {
    "date": "2005-01-07T00:00:00Z",
    "price": 225000
  },
  {
    "date": "2006-01-08T00:00:00Z",
    "price": 210000
  },
  {
    "date": "2011-01-09T00:00:00Z",
    "price": 200000
  },
  {
    "date": "2012-01-12T00:00:00Z",
    "price": 212000
  },
  {
    "date": "2013-01-06T00:00:00Z",
    "price": 171000
  }
]
```

To view the results as a chart:

1. Click **Chart**.
2. In **Chart Type**, select `Line`.
3. In **X-Axis**, select `date`.
4. In **Y-Axis**, select `price`.

![Line chart showing house prices over 10 years](../_images/time-series-irregular.svg) 

Example 4\. Use window functions with time series data

Before you try this example, you must follow all the examples in [Store and Process Time Series Data](time-series.md) to import time series data.

For this example, set the query context to the `time` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

The following query returns the weekly average and four-week moving average for temperature over a two-month range.

```sqlpp
WITH range_start AS (STR_TO_MILLIS ("2013-07-01", "YYYY-MM-DD")),
       range_end AS (STR_TO_MILLIS ("2013-08-31", "YYYY-MM-DD"))
SELECT MILLIS_TO_TZ(week*1000*60*60*24*7, "UTC") AS week_of,
       week_avg,
       AVG(week_avg) OVER (ORDER BY week ROWS 4 PRECEDING) AS four_week_mov_avg
FROM weather AS d
UNNEST _timeseries(d, {"ts_ranges": [range_start, range_end]}) AS t
WHERE d.region = 'UK'
  AND (d.ts_start <= range_end AND d.ts_end >= range_start)
GROUP BY IDIV(t._t, 1000*60*60*24*7) AS week
LETTING week_avg = AVG(t._v0);
```

Results

```json
[
  {
    "four_week_mov_avg": 18.5,
    "week_avg": 18.5,
    "week_of": "2013-06-27T00:00:00Z"
  },
  {
    "four_week_mov_avg": 19.142857142857142,
    "week_avg": 19.785714285714285,
    "week_of": "2013-07-04T00:00:00Z"
  },
  {
    "four_week_mov_avg": 19.428571428571427,
    "week_avg": 20,
    "week_of": "2013-07-11T00:00:00Z"
  },
  {
    "four_week_mov_avg": 19.19642857142857,
    "week_avg": 18.5,
    "week_of": "2013-07-18T00:00:00Z"
  },
  {
    "four_week_mov_avg": 18.657142857142855,
    "week_avg": 16.5,
    "week_of": "2013-07-25T00:00:00Z"
  },
  {
    "four_week_mov_avg": 18.857142857142854,
    "week_avg": 19.5,
    "week_of": "2013-08-01T00:00:00Z"
  },
  {
    "four_week_mov_avg": 18.385714285714286,
    "week_avg": 17.428571428571427,
    "week_of": "2013-08-08T00:00:00Z"
  },
  {
    "four_week_mov_avg": 17.485714285714288,
    "week_avg": 15.5,
    "week_of": "2013-08-15T00:00:00Z"
  },
  {
    "four_week_mov_avg": 16.842857142857145,
    "week_avg": 15.285714285714286,
    "week_of": "2013-08-22T00:00:00Z"
  },
  {
    "four_week_mov_avg": 16.342857142857145,
    "week_avg": 14,
    "week_of": "2013-08-29T00:00:00Z"
  }
]
```

To view the results as a chart:

1. Click **Chart**.
2. In **Chart Type**, select `Multi-Connected Points by Column`.
3. In **X-Axis**, select `week_of`.
4. In **Y-Values**, select both `four_week_mov_avg` and `week_avg`.

![Line chart showing weekly average temperature and four-week moving average over 2 months](../_images/time-series-window.svg) 

Example 5\. Query time series data with multiple predicate ranges

Before you try this example, you must follow all the examples in [Store and Process Time Series Data](time-series.md) to import time series data.

For this example, set the query context to the `time` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

The following query returns the weekly average and four-week moving average for temperature over March, April, and May.

```sqlpp
WITH datarange AS (
     [
       [STR_TO_MILLIS("2013-03-01", "YYYY-MM-DD"),
        STR_TO_MILLIS("2013-03-31", "YYYY-MM-DD")],
       [STR_TO_MILLIS("2013-05-01", "YYYY-MM-DD"),
        STR_TO_MILLIS("2013-05-31", "YYYY-MM-DD")],
       [STR_TO_MILLIS("2013-07-01", "YYYY-MM-DD"),
        STR_TO_MILLIS("2013-07-31", "YYYY-MM-DD")]
     ]),
     docs AS (
      SELECT DISTINCT RAW META(d).id
      FROM datarange AS tr
      JOIN weather AS d
      ON d.region = 'UK' AND (d.ts_start <= tr[1] AND d.ts_end>= tr[0]))
SELECT MILLIS_TO_TZ(week*1000*60*60*24*7, "UTC") AS week_of,
       week_avg,
       AVG(week_avg) OVER (ORDER BY week ROWS 4 PRECEDING) AS four_week_mov_avg
FROM weather AS d
USE KEYS docs
UNNEST _timeseries(d, {"ts_ranges": datarange }) AS t
GROUP BY IDIV(t._t, 1000*60*60*24*7) AS week
LETTING week_avg = AVG(t._v0);
```

Results

```json
[
  {
    "four_week_mov_avg": 5.5,
    "week_avg": 5.5,
    "week_of": "2013-02-28T00:00:00Z"
  },
  {
    "four_week_mov_avg": 5.5,
    "week_avg": 5.5,
    "week_of": "2013-03-07T00:00:00Z"
  },
  {
    "four_week_mov_avg": 5.5476190476190474,
    "week_avg": 5.642857142857143,
    "week_of": "2013-03-14T00:00:00Z"
  },
  {
    "four_week_mov_avg": 5.785714285714286,
    "week_avg": 6.5,
    "week_of": "2013-03-21T00:00:00Z"
  },
  {
    "four_week_mov_avg": 5.928571428571429,
    "week_avg": 6.5,
    "week_of": "2013-03-28T00:00:00Z"
  },
  {
    "four_week_mov_avg": 7.028571428571428,
    "week_avg": 11,
    "week_of": "2013-04-25T00:00:00Z"
  },
  {
    "four_week_mov_avg": 8.128571428571428,
    "week_avg": 11,
    "week_of": "2013-05-02T00:00:00Z"
  },
  {
    "four_week_mov_avg": 9.585714285714285,
    "week_avg": 12.928571428571429,
    "week_of": "2013-05-09T00:00:00Z"
  },
  {
    "four_week_mov_avg": 10.985714285714284,
    "week_avg": 13.5,
    "week_of": "2013-05-16T00:00:00Z"
  },
  {
    "four_week_mov_avg": 12.385714285714284,
    "week_avg": 13.5,
    "week_of": "2013-05-23T00:00:00Z"
  },
  {
    "four_week_mov_avg": 12.885714285714283,
    "week_avg": 13.5,
    "week_of": "2013-05-30T00:00:00Z"
  },
  {
    "four_week_mov_avg": 14.385714285714283,
    "week_avg": 18.5,
    "week_of": "2013-06-27T00:00:00Z"
  },
  {
    "four_week_mov_avg": 15.757142857142856,
    "week_avg": 19.785714285714285,
    "week_of": "2013-07-04T00:00:00Z"
  },
  {
    "four_week_mov_avg": 17.057142857142857,
    "week_avg": 20,
    "week_of": "2013-07-11T00:00:00Z"
  },
  {
    "four_week_mov_avg": 18.057142857142857,
    "week_avg": 18.5,
    "week_of": "2013-07-18T00:00:00Z"
  },
  {
    "four_week_mov_avg": 18.657142857142855,
    "week_avg": 16.5,
    "week_of": "2013-07-25T00:00:00Z"
  }
]
```

## [](#related-links)Related Links

* Overview: [Store and Process Time Series Data](time-series.md)

---

[1](#%5Ffootnoteref%5F1). Contains HM Land Registry data © Crown copyright and database right 2021\. This data is licensed under the Open Government Licence v3.0\.