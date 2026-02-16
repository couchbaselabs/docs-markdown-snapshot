[View original HTML](/analytics/sqlpp/8_builtin_temp.html)

|  | In SQL++ for Capella Analytics, temporal functions only support ISO-8601 example date formats. They do not support date string codes, Go reference dates, or percent-style dates, which are supported by SQL++ for Query. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

> This topic describes the builtin SQL++ for Capella Analytics temporal functions. 

## [](#datefun%5F%5Ffn-date-now-local)now\_local (clock\_local)

* Syntax:  
now_local([fmt])
* The current time (at query compilation time) on the node that compiled the query, in the specified string format.
* Arguments:

  * `fmt`: A string, or an expression that evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string) to use for the result.  
  This argument is optional. If you do not specify the format, or you specify an incorrect format, it defaults to the combined full date and time.
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

## [](#datefun%5F%5Ffn-date-now-millis)now\_millis (clock\_millis)

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

## [](#datefun%5F%5Ffn-date-now-str)now\_str (clock\_str)

* Syntax:  
now_str([fmt])
* The current time (at query compilation time) on the node that compiled the query, in the specified string format.
* Arguments:

  * `fmt`: A string, or an expression that evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string) to use for the result.  
  This argument is optional. If you do not specify the format, or you specify an incorrect format, it defaults to the combined full date and time.
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

## [](#datefun%5F%5Ffn-date-now-tz)now\_tz (clock\_tz)

* Syntax:  
now_tz(tz [, fmt])
* The current time (at query compilation time) in the timezone given by the timezone argument passed to the function. This time is the local system time converted to the specified timezone.  
As this function converts the local time, it may not accurately represent the true time in that timezone.
* Arguments:

  * `tz`: A string, or an expression that evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.html#date-timezone) to convert the local time to.  
  If this argument is not a valid timezone then `null` is returned as the result.
  * `fmt`: A string, or an expression that evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string) to use for the result.  
  This argument is optional. If you do not specify the format, or you specify an incorrect format, it defaults to the combined full date and time.
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

## [](#datefun%5F%5Ffn-date-now-utc)now\_utc (clock\_utc)

* Syntax:  
now_utc([fmt])
* The current time in UTC. This time is the local system time converted to UTC. This function is provided for convenience and is the same as `now_tz('UTC')`.
* Arguments:

  * `fmt`: A string, or an expression that evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string) to use for the result.  
  This argument is optional. If you do not specify the format, or you specify an incorrect format, it defaults to the combined full date and time.
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

## [](#datefun%5F%5Ffn-date-add-millis)date\_add\_millis

* Syntax:  
date_add_millis(date1, n, part)
* Performs date arithmetic on a particular component of an Epoch/UNIX timestamp value. This calculation is specified by the arguments `n` and `part`. For example, a value of 3 for `n` and a value of `day` for `part` would add 3 days to the date specified by `date1`.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds.  
  If this argument is not an integer then `null` is returned.
  * `n`: The value to increment the date component by. This value must be an integer, or an expression which evaluates to an integer, and may be negative to perform date subtraction.  
  If a non-integer is passed to the function then `null` is returned.
  * `part`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) of the date to increment.  
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

## [](#datefun%5F%5Ffn-date-add-str)date\_add\_str

* Syntax:  
date_add_str(date1, n, part)
* Performs date arithmetic on a date string. This calculation is specified by the arguments `n` and `part`. For example a value of 3 for `n` and a value of `day` for `part` would add 3 days to the date specified by `date1`.
* Arguments:

  * `date1`: A string, or an expression that evaluates to a string, representing the date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string).
  * `n`: The value to increment the date component by. This value must be an integer, or an expression which evaluates to an integer, and may be negative to perform date subtraction.  
  If a non-integer is passed to the function then `null` is returned.
  * `part`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) of the date to increment.  
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

## [](#datefun%5F%5Ffn-date-diff-millis)date\_diff\_millis

* Syntax:  
date_diff_millis(date1, date2, part)
* Finds the elapsed time between two Epoch/UNIX timestamps. This elapsed time is measured from the date specified by `date2` to the date specified by `date1`. If `date1` is greater than `date2`, then the value returned is positive, otherwise the value returned is negative.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds.  
  If this argument is not an integer, then `null` is returned.
  * `date2`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value to subtract from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) of the date to increment.  
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

## [](#datefun%5F%5Ffn-date-diff-str)date\_diff\_str

* Syntax:  
date_diff_str(date1, date2, part)
* Finds the elapsed time between two dates specified as formatted strings. This elapsed time is measured from the date specified by `date2` to the date specified by `date1`. If `date1` is greater than `date2` then the value returned is positive, otherwise the value returned is negative.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value to subtract from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `date2`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value to subtract from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) of the date to increment.  
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

## [](#datefun%5F%5Ffn-date-format-str)date\_format\_str

* Syntax:  
date_format_str(date1, fmt)
* Converts datetime strings from one supported date string format to a different supported date string format.
* Arguments:

  * `date1`: A string, or an expression that evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string).  
  If this argument is not a valid date string then `null` is returned.
  * `fmt`: A string, or an expression that evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string) to use for the result.  
  If you specify an incorrect format, it defaults to the combined full date and time.
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

## [](#datefun%5F%5Ffn-date-part-millis)date\_part\_millis

* Syntax:  
date_part_millis(date1, part [, tz])
* Extracts the value of a given date component from an Epoch/UNIX timestamp value.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value to subtract from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function, then `null` is returned.
  * `tz`: A string, or an expression that evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.html#date-timezone) to convert the local time to.  
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

## [](#datefun%5F%5Ffn-date-part-str)date\_part\_str

* Syntax:  
date_part_str(date1, part)
* Extracts the value of a given date component from a date string.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value to subtract from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) of the date to increment.  
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

## [](#datefun%5F%5Ffn-date-range-millis)date\_range\_millis

* Syntax:  
date_range_millis(date1, date2, part [,n])
* Generates an array of dates from the start date specified by `date1` and the end date specified by `date2`, as Epoch/UNIX timestamps. The difference between each subsequent generated date can be adjusted.  
It’s possible to generate very large arrays using this function. In some cases the query engine may be unable to process all of these and cause excessive resource consumption. It’s therefore recommended that you first validate the inputs to this function to make sure that the generated result is a reasonable size.  
If the start date is greater than the end date passed to the function then an error is not thrown, but the result array is empty. You can generate an array of descending dates by setting the start date greater than the end date and specifying a negative value for `n`.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value to subtract from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `date2`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the value to subtract from `date1`.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) of the date to increment.  
  If an invalid part is passed to the function, then `null` is returned.
  * `n`: An integer, or an expression which evaluates to an integer, representing the value by which to increment the part component for each generated date.  
  This argument is optional. If not specified, it defaults to 1\. If you specify a value that is not an integer, then `null` is returned.
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

## [](#datefun%5F%5Ffn-date-range-str)date\_range\_str

* Syntax:  
date_range_str(start_date, end_date, date_interval [, quantity_int ])
* Generates an array of date strings between the start date and end date, calculated by the interval and quantity values. The input dates can be in any of the [supported date formats](../n1ql/n1ql-language-reference/datefun.html#date-formats).  
It’s possible to generate very large arrays using this function. In some cases the query engine may be unable to process all of these and cause excessive resource consumption. It’s therefore recommended that you first validate the inputs of this function to make sure that the generated result is a reasonable size.  
If the `start_date` is greater than the `end_date`, an error is not thrown, but the result array is empty. You can generate an array of descending dates by setting the `start_date` greater than the `end_date` and specifying a negative value for `quantity_number`.  
Both specified dates must have the same string format, otherwise `null` is returned. To make sure that both dates have the same format, you should use [date\_format\_str()](#datefun%5F%5Ffn-date-format-str).
* Arguments:

  * `start_date`: A string, or an expression that evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string). This is the date used as the start date of the array generation.  
  If this argument is not an integer, then `null` is returned.
  * `end_date`: A string, or an expression that evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string). This is the date used as the end date of the array generation. This value is exclusive, that is, the end date is not included in the result.  
  If this argument is not an integer, then `null` is returned.
  * `date_interval`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) of the date to increment.  
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

## [](#datefun%5F%5Ffn-date-trunc-millis)date\_trunc\_millis

* Syntax:  
date_trunc_millis(date1, part)
* Truncates an Epoch/UNIX timestamp up to the specified date component.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the date used as the date to truncate.  
  If this argument is not an integer, then `null` is returned.
  * `part`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) to truncate to.  
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

## [](#datefun%5F%5Ffn-date-trunc-str)date\_trunc\_str

* Syntax:  
date_trunc_str(date1, part)
* Truncates a date string up to the specified date component.
* Arguments:

  * `date1`: A string, or an expression that evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string). This is the date that is truncated.  
  If this argument is not a valid date format, then `null` is returned.
  * `part`: A string, or an expression that evaluates to a string, representing the [component](../n1ql/n1ql-language-reference/datefun.html#manipulating-components) to truncate to.  
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

## [](#datefun%5F%5Ffn-date-duration-to-str)duration\_to\_str

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

## [](#datefun%5F%5Ffn-date-millis)millis

* Syntax:  
millis(date1)
* Converts a date string to Epoch/UNIX milliseconds.
* Arguments:

  * `date1`: A string, or an expression that evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string). This is the date to convert to Epoch/UNIX milliseconds.  
  If this argument is not a valid date format. then `null` is returned.
* Return Value:

  * An integer representing the date string converted to Epoch/UNIX milliseconds.
* Example:  
{"DateStringInMilliseconds": millis("2016-05-15T03:59:00Z")};
* The expected result is:  
{  
  "DateStringInMilliseconds": 1463284740000  
}

## [](#datefun%5F%5Ffn-date-millis-to-str)millis\_to\_str (millis\_to\_local)

* Syntax:  
millis_to_str(date1 [, fmt ])
* Converts an Epoch/UNIX timestamp into the specified date string format.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the date to convert.  
  If this argument is not an integer, then `null` is returned.
  * `fmt`: A string, or an expression that evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string) to use for the result.  
  This argument is optional. If you do not specify the format, or you specify an incorrect format, it defaults to the combined full date and time.
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

## [](#datefun%5F%5Ffn-date-millis-to-tz)millis\_to\_tz (millis\_to\_zone\_name)

* Syntax:  
millis_to_tz(date1, tz [, fmt])
* Converts an Epoch/UNIX timestamp into the specified time zone in the specified date string format.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the date to convert.  
  If this argument is not an integer, then `null` is returned.
  * `tz`: A string, or an expression that evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.html#date-timezone) to convert the local time to.  
  This argument is optional. If not specified, it defaults to the system timezone.  
  If an incorrect time zone is provided, then `null` is returned.
  * `fmt`: A string, or an expression that evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string) to use for the result.  
  This argument is optional. If you do not specify the format, or you specify an incorrect format, it defaults to the combined full date and time.
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

## [](#datefun%5F%5Ffn-date-millis-to-utc)millis\_to\_utc

* Syntax:  
millis_to_utc(date1 [, fmt])
* Converts an Epoch/UNIX timestamp into local time in the specified date string format.
* Arguments:

  * `date1`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds. This is the date to convert to UTC.  
  If this argument is not an integer, then `null` is returned.
  * `fmt`: A string, or an expression that evaluates to a string, representing an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string) to use for the result.  
  This argument is optional. If you do not specify the format, or you specify an incorrect format, it defaults to the combined full date and time.
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

## [](#datefun%5F%5Ffn-date-str-to-duration)str\_to\_duration

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

  * `duration`: A string, or an expression that evaluates to a string, representing the duration to convert.  
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

## [](#datefun%5F%5Ffn-date-str-to-millis)str\_to\_millis

* Syntax:  
str_to_millis(date1)
* Converts a date string to Epoch/UNIX milliseconds.
* Arguments:

  * `date1`: A string, or an expression that evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string). This is the date to convert to Epoch/UNIX milliseconds.  
  If this argument is not a valid date format, then `null` is returned.
* Return Value:

  * An integer representing the date string converted to Epoch/UNIX milliseconds.
* Example:  
{"Milliseconds": str_to_millis("2016-05-15T03:59:00Z")};
* The expected result is:  
{  
  "Milliseconds": 1463284740000  
}

## [](#datefun%5F%5Ffn-date-str-to-utc)str\_to\_utc

* Syntax:  
str_to_utc(date1)
* Converts a date string into the equivalent date in UTC. The output date format follows the date format of the date passed as input.
* Arguments:

  * `date1`: A string, or an expression that evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string). This is the date to convert to UTC.  
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

## [](#datefun%5F%5Ffn-date-str-to-tz)str\_to\_tz (str\_to\_zone\_name)

* Syntax:  
str_to_tz(date1, tz)
* Converts a date string to its equivalent in the specified timezone. The output date format follows the date format of the date passed as input.
* Arguments:

  * `date1`: A string, or an expression that evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string). This is the date to convert to UTC.  
  If this argument is not a valid date format then `null` is returned.
  * `tz`: A string, or an expression that evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.html#date-timezone) to convert the local time to.  
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

## [](#datefun%5F%5Ffn-date-weekday-millis)weekday\_millis

* Syntax:  
weekday_millis(expr [, tz ])
* Converts a date string to its equivalent in the specified timezone. The output date format follows the date format of the date passed as input.
* Arguments:

  * `expr`: An integer, or an expression which evaluates to an integer, representing an Epoch/UNIX timestamp in milliseconds.
  * `tz`: A string, or an expression that evaluates to a string, representing the [timezone](../n1ql/n1ql-language-reference/datefun.html#date-timezone) for the `expr` argument.  
  This argument is optional. If not specified, it defaults to the system timezone. If an incorrect time zone is provided then `null` is returned.
* Return Value:

  * A single date string representing the date string converted to the specified timezone.
* Example:  
{"Day": weekday_millis(1486237655742, 'America/Tijuana')};
* The expected result is:  
{  
  "Day": "Saturday"  
}

## [](#datefun%5F%5Ffn-date-weekday-str)weekday\_str

* Syntax:  
weekday_str(date)
* Returns the day of the week string value from the input date string. Returns the weekday name from the input date in Unix timestamp. Note that this function returns the string value of the day of the week, whereas [date\_part\_str()](#datefun%5F%5Ffn-date-part-str) with `part` \= "dow" returns an integer value of the weekday (0-6).
* Arguments:

  * `date`: A string, or an expression that evaluates to a string, representing a date in an [ISO-8601 example date format](../n1ql/n1ql-language-reference/datefun.html#date-string). This is the date to convert to UTC.  
  If this argument is not a valid date format then `null` is returned.
* Return Value:

  * The text string name of the day of the week, such as "Monday" or "Friday".
* Example:  
{"Day": weekday_str('2017-02-05')};
* The expected result is:  
{  
  "Day": "Sunday"  
}