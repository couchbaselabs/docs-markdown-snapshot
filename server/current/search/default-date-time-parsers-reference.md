[View original HTML](/server/current/search/default-date-time-parsers-reference.html)

> Use a date/time parser to tell the Search Service how to interpret date and time data in your documents. 

You can use one of the default date/time parsers, or [create your own](create-custom-date-time-parser.md).

Set the default date/time parser for your Search index from the Server Web Console’s' [Advanced Settings](set-advanced-settings.md) or your [JSON Search index definition](search-index-params.md#default-date-time-parser).

You can also set a date/time parser when using [Date Range facets](search-request-params.md#date) or a [date range query](search-request-params.md#date-range-queries).

The following default date/time parsers are available:

| Date/Time Parser | Description                                                                                                                                                                                                           |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dateTimeOptional | The dateTimeOptional date/time parser uses 6 layouts, in [percentStyle](date-time-parser-layout-styles.md#percent) format, to parse date and time strings. See [dateTimeOptional Layouts](#datetimeoptional-layouts). |
| unix\_micro      | The unix\_micro date/time parser expects a date and time string represented as the number of microseconds since the Unix epoch (1970-01-01T00:00:00Z).                                                                |
| unix\_milli      | The unix\_milli date/time parser expects a date and time string represented as the number of milliseconds since the Unix epoch (1970-01-01T00:00:00Z).                                                                |
| unix\_nano       | The unix\_nano date/time parser expects a date and time string represented as the number of nanoseconds since the Unix epoch (1970-01-01T00:00:00Z).                                                                  |
| unix\_sec        | The unix\_sec date/time parser expects a date and time string represented as the number of seconds since the Unix epoch (1970-01-01T00:00:00Z).                                                                       |

## [](#datetimeoptional-layouts)dateTimeOptional Layouts

The following layouts are included in the `dateTimeOptional` date/time parser:

| Layout                   | Example Date/Time String       |
| ------------------------ | ------------------------------ |
| %Y-%m-%dT%H:%M:%S.%N%z:M | 2023-09-15T14:24:50.1567+05:30 |
| %Y-%m-%dT%H:%M:%S%z:M    | 2023-09-15T14:24:50+05:30      |
| %Y-%m-%dT%H:%M:%S        | 2023-09-15T14:24:50            |
| %Y-%m-%d %H:%M:%S        | 2023-09-15 14:24:50            |
| %Y-%m-%d %H:%M:%S %z     | 2023-09-15 14:24:50 +0530      |
| %Y-%m-%d                 | 2023-09-15                     |

## [](#missing-values)Defaults for Missing Date/Time Values

If a date/time string is missing a value, the Search Service uses the following default values to make a complete date/time string:

| Value                    | Default    |
| ------------------------ | ---------- |
| Month                    | 01/January |
| Day                      | 01         |
| Hour                     | 00         |
| Minute                   | 00         |
| Second                   | 00         |
| Timezone                 | UTC        |
| Timezone Offset from UTC | +00:00     |
| Fraction of a second     | nil        |

## [](#see-also)See Also

* [Date/Time Parser Layout Styles](date-time-parser-layout-styles.md)
* [Create a Custom Date/Time Parser](create-custom-date-time-parser.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)