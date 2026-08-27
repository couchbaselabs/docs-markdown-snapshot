---
title: Date/Time Parser Layout Styles
description: When you create a custom date/time parser with the Couchbase Server
  Web Console, you must choose a specific layout style for your date/time
  layouts.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/date-time-parser-layout-styles.adoc
  xref: xref:server:search:date-time-parser-layout-styles.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/search/date-time-parser-layout-styles.html)

# Date/Time Parser Layout Styles

> When you create a custom date/time parser with the Couchbase Server Web Console, you must choose a specific layout style for your date/time layouts. 

You can choose from the following layout styles for a date/time parser.

> [!TIP]
> Date/time layouts should always be surrounded by quotes.

| Layout Style     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         | Example Layouts                                                                                                                  |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **flexiblego**   | Date/time layouts must be provided with golang specific constants. A **flexiblego** date/time layout is not validated automatically by the Server Web Console. For more information about **flexiblego** time layout syntax, see [Go Date/Time Layout Style Syntax](#go).                                                                                                                                                                           | "01/02 03:04:05PM '25 -0700" "Mon Jan \_2 15:04:05 MST 2025" "Monday January 02 15:04:05 -0700 2025" "2025-01-02T15:04:05Z07:00" |
| **isostyle**     | Date/time layouts must be provided as ISO date format strings, commonly used in programming languages like Java and Swift. Letters in the range A-Z and a-z are reserved for layout patterns. Any other characters are considered as a literal part of a date string. The count of pattern letters determines the specific format. For more information about **isostyle** time layout syntax, see [ISO Style Date/Time Layout Style Syntax](#iso). | "yyyy/MM/dd h:mma" "dd/MM/yyyy HH:mm:ss" "yyyy-MM-dd'T'HH:mm:ssXX" "dd MMMM yy ha z" "yyyy; MMM dd (EEE) hh:mm:ss.SSSSSaa xx"    |
| **percentstyle** | Date/time layouts are provided using format specifiers surrounded by % characters, commonly used in programming languages like C and Python. Any other characters in a layout string are considered literal characters. For more information about **percentstyle** time layout syntax, see [Percent Style Date/Time Layout Style Syntax](#percent).                                                                                                | "%Y/%m/%d %l:%M%p" "%d/%m/%Y %H:%M:%S" "%Y-%m-%dT%H:%M:%S%z" "%d %B %y %l%p %Z" "%Y; %b %d (%a) %I:%M:%S.%N%P %z"                |

## [](#go)Go Date/Time Layout Style Syntax

**flexiblego** and **sanitizedgo** date/time layouts use the following syntax:

| Date Time Component                                                                | Syntax                                                                              |                                      |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------ |
| Year                                                                               | 4 digit year                                                                        | 2025                                 |
| 2 digit year                                                                       | 25                                                                                  |                                      |
| Month                                                                              | Unpadded month                                                                      | 1                                    |
| Zero-padded month                                                                  | 01                                                                                  |                                      |
| Full English month                                                                 | January                                                                             |                                      |
| Abbreviated English month                                                          | Jan                                                                                 |                                      |
| Unpadded day of the month                                                          | 2                                                                                   |                                      |
| Space-padded day of the month                                                      | \_2                                                                                 |                                      |
| Zero-padded day of the month                                                       | 02                                                                                  |                                      |
| Day                                                                                | Full English day                                                                    | Monday                               |
| Abbreviated English day                                                            | Mon                                                                                 |                                      |
| Space-padded 3 digit day of the year                                               | \_\_2 \_52                                                                          |                                      |
| Zero-padded 3 digit day of the year                                                | 002                                                                                 |                                      |
| Hour                                                                               | Unpadded hour (1-12)                                                                | 3                                    |
| Zero-padded 2 digit hour                                                           | 03 15                                                                               |                                      |
| AM or PM                                                                           | AM / PM am / pm                                                                     |                                      |
| Minute                                                                             | Unpadded minute                                                                     | 4                                    |
| Zero-padded minute                                                                 | 04                                                                                  |                                      |
| Second                                                                             | Unpadded second                                                                     | 5                                    |
| Zero-padded second                                                                 | 05                                                                                  |                                      |
| Fraction of a Second                                                               | Fraction of a second to a given number of decimal places, including trailing zeroes | ,000                                 |
| Fraction of a second to a given number of decimal places, removing trailing zeroes | ,999                                                                                |                                      |
| Time Zone                                                                          | Time zone as UTC offset                                                             | \-07 \-0700 \-07:00 Z07 Z0700 Z07:00 |

## [](#percent)Percent Style Date/Time Layout Style Syntax

**percentstyle** date/time layouts use the following syntax:

| Date Time Component                             | Example                   | Syntax                        |     |
| ----------------------------------------------- | ------------------------- | ----------------------------- | --- |
| Year                                            | 4 digit year              | 2025                          | %Y  |
| 2 digit year                                    | 25                        | %y                            |     |
| Month                                           | Unpadded month            | 1                             | %o  |
| Zero-padded month                               | 01                        | %m                            |     |
| Full English month                              | January                   | %B                            |     |
| Abbreviated English month                       | Jan                       | %b                            |     |
| Day                                             | Unpadded day of the month | 2                             | %e  |
| Zero-padded day of the month                    | 02                        | %d                            |     |
| Full English day                                | Monday                    | %A                            |     |
| Abbreviated English day                         | Mon                       | %a                            |     |
| Hour                                            | Unpadded hour (1-12)      | 3                             | %1  |
| Zero-padded 2 digit hour                        | 03 15                     | %I                            |     |
| AM or PM                                        | AM / PM am / pm           | %p (uppercase) %P (lowercase) |     |
| Minute                                          | Unpadded minute           | 4                             | %i  |
| Zero-padded minute                              | 04                        | %M                            |     |
| Second                                          | Unpadded second           | 5                             | %s  |
| Zero-padded second                              | 05                        | %S                            |     |
| Microseconds and Nanoseconds                    | Microseconds              | 15:03:02.000000               | .%f |
| Nanoseconds                                     | 15:03:02.000000000000     | .%N                           |     |
| Time Zone                                       | Time zone name            | UTC JST GMT                   | %Z  |
| Time zone as UTC offset, formatted as +hhmm     | +0500 \-0600              | %z                            |     |
| Time zone as UTC offset, formatted as +hh:mm    | +05:00 \-06:00            | %z:M                          |     |
| Time zone as UTC offset, formatted as +hh:mm:ss | +05:00:00 +06:00:00       | %z:S                          |     |
| Time zone as UTC offset, formatted as +hh       | +05 \-06                  | %zH                           |     |
| Time zone as UTC offset, formatted as +hhmmss   | +050000 \-060000          | %zS                           |     |

## [](#iso)ISO Style Date/Time Layout Style Syntax

**isostyle** date/time layouts use the following syntax:

| Date Time Component                             | Example                   | Syntax                                                                                                              |                                              |
| ----------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Year                                            | 4 digit year              | 2025                                                                                                                | YYYY / yyyy / uuuu YYY / yyy / uuu Y / y / u |
| 2 digit year                                    | 25                        | YY / yy / uu                                                                                                        |                                              |
| Zero padded year                                | 02025                     | YYYYY / yyyyy / uuuuu The number of Y/y/u characters determines the number of zeroes added before the 4 digit year. |                                              |
| Month                                           | Unpadded month            | 1                                                                                                                   | M                                            |
| Zero-padded month                               | 01                        | MM                                                                                                                  |                                              |
| Full English month                              | January                   | MMMM                                                                                                                |                                              |
| Abbreviated English month                       | Jan                       | MMM                                                                                                                 |                                              |
| Day                                             | Unpadded day of the month | 2                                                                                                                   | d                                            |
| Zero-padded day of the month                    | 02                        | dd                                                                                                                  |                                              |
| Full English day                                | Monday                    | EEEE                                                                                                                |                                              |
| Abbreviated English day                         | Mon                       | E / EE / EEE                                                                                                        |                                              |
| Hour                                            | Unpadded hour (1-12)      | 3                                                                                                                   | h / K                                        |
| Zero-padded 2 digit hour                        | 03 15                     | hh / KK                                                                                                             |                                              |
| AM or PM                                        | AM / PM am / pm           | a (uppercase) aa (lowercase)                                                                                        |                                              |
| Minute                                          | Unpadded minute           | 4                                                                                                                   | m                                            |
| Zero-padded minute                              | 04                        | mm                                                                                                                  |                                              |
| Second                                          | Unpadded second           | 5                                                                                                                   | s                                            |
| Zero-padded second                              | 05                        | ss                                                                                                                  |                                              |
| Fractions of a second                           | 15:03:02.000000           | .S \- the number of S's determines the number of decimal places                                                     |                                              |
| Time Zone                                       | Time zone name            | UTC JST GMT                                                                                                         | z / zz / zzz / zzzz                          |
| Time zone as UTC offset, formatted as +hhmm     | +0500 \-0600              | XX / xx                                                                                                             |                                              |
| Time zone as UTC offset, formatted as +hh:mm    | +05:00 \-06:00            | XXX / xxx                                                                                                           |                                              |
| Time zone as UTC offset, formatted as +hh:mm:ss | +05:00:00 +06:00:00       | XXXXX / xxxxx                                                                                                       |                                              |
| Time zone as UTC offset, formatted as +hh       | +05 \-06                  | X / x                                                                                                               |                                              |
| Time zone as UTC offset, formatted as +hhmmss   | +050000 \-060000          | XXXX / xxxx                                                                                                         |                                              |

## [](#see-also)See Also

* [Default Date/Time Parsers](default-date-time-parsers-reference.md)
* [Create a Custom Date/Time Parser](create-custom-date-time-parser.md)
* [Customize a Search Index with the Web Console](customize-index.md)