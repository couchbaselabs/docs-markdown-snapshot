---
title: String Functions
description: String functions perform operations on a string input value and
  returns a string or other value.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/stringfun.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:n1ql:n1ql-language-reference/stringfun.adoc[]
---

[View original HTML](/server/7.2/n1ql/n1ql-language-reference/stringfun.html)

# String Functions

String functions perform operations on a string input value and returns a string or other value.

> [!NOTE]
> If any arguments to any of the following functions are `MISSING` then the result is also `MISSING` (i.e. no result is returned). Similarly, if any of the arguments passed to the functions are `NULL` or are of the wrong type (e.g. an integer instead of a string), then `NULL` is returned as the result.

## [](#fn-str-concat)CONCAT(`string1`, `string2`, …)

### [](#description)Description

This function takes two or more strings and returns a new string after concatenating the input strings. If there are fewer than two arguments, then it returns an error.

### [](#arguments)Arguments

string1, string2, ...

\[At least 2 are required\] The strings, or valid [expressions](index.md) which evaluate to strings, to be concatenated together.

### [](#return-value)Return Value

A new string, concatenated from the input strings.

### [](#examples)Examples

```sqlpp
SELECT CONCAT("abc", "def", "ghi") AS concat;
```

```json
[
  {
    "concat": "abcdefghi"
  }
]
```

## [](#fn-str-concat2)CONCAT2(`separator`, `arg1`, `arg2`, …)

### [](#description-2)Description

This function takes the input strings, or arrays of strings, and concatenates them with the specified separator between each input string. If there are fewer than two arguments, then it returns an error.

### [](#arguments-2)Arguments

separator

\[Required\] The string to separate the input strings. If no separator is required, specify the empty string "".

arg1, arg2, ...

\[At least 1 is required\] The strings, or arrays of strings, to be concatenated together.

### [](#return-value-2)Return Value

A new string, concatenated from the inputs, with the separator between each input. Arrays of strings are flattened and concatenated in the same order. If there is only one string argument, the separator is not used.

If any argument or array element is MISSING, returns MISSING. If any argument or array element is non-string, returns NULL.

### [](#examples-2)Examples

```sqlpp
SELECT CONCAT2('-','a','b',['c','d'],['xyz']) AS c1,
CONCAT2('-','a') AS c2,
CONCAT2('-',['b']) AS c3;
```

```json
[
  {
    "c1": "a-b-c-d-xyz",
    "c2": "a",
    "c3": "b"
  }
]
```

## [](#fn-str-contains)CONTAINS(in\_str, search\_str)

### [](#description-3)Description

Checks whether or not the specified search string is a substring of the input string (i.e. exists within). This returns `true` if the substring exists within the input string, otherwise `false` is returned.

### [](#arguments-3)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to search within.

search\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to search for.

### [](#return-value-3)Return Value

A boolean, representing whether the search string exists within the input string.

### [](#examples-3)Examples

```sqlpp
SELECT CONTAINS("N1QL is awesome", "N1QL") as n1ql,
       CONTAINS("N1QL is awesome", "SQL") as no_sql;
```

```json
{
    "results": [
        {
            "n1ql": true,
            "no_sql": false
        }
    ]
}
```

## [](#fn-str-initcap)INITCAP(in\_str)

### [](#description-4)Description

Converts the string so that the first letter of each word is uppercase and every other letter is lowercase (known as 'Title Case').

### [](#arguments-4)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to convert to title case.

### [](#return-value-4)Return Value

A string, representing the input string converted to title case.

### [](#limitations)Limitations

This function capitalizes the initial letter of every word in the sentence, this means that even short words such as "the" and "or" will be capitalized. This does not strictly follow title case conventions used in the writing domain.

### [](#examples-4)Examples

```sqlpp
SELECT INITCAP("N1QL is awesome") as n1ql;
```

```json
{
    "results": [
        {
            "n1ql": "N1ql Is Awesome"
        }
    ]
}
```

## [](#fn-str-length)LENGTH(in\_str)

_Equivalent_: [LEN()](metafun.md#len)

### [](#description-5)Description

Finds the length of a string, where length is defined as the number of code points within the string.

### [](#arguments-5)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to find the length of.

### [](#return-value-5)Return Value

An integer representing the length of the string.

### [](#examples-5)Examples

```sqlpp
SELECT LENGTH("N1QL is awesome") AS ascii,
       LENGTH("Café") AS diacritic,
       LENGTH("🙂") AS emoji,
       LENGTH("") AS zero;
```

```json
{
    "results": [
        {
            "ascii": 15,
            "diacritic": 5,
            "emoji": 4,
            "zero": 0
        }
    ]
}
```

## [](#fn-str-lower)LOWER(in\_str)

### [](#description-6)Description

Converts all characters in the input string to lower case. This is useful for canonical comparison of string values.

### [](#arguments-6)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to convert to lower case.

### [](#return-value-6)Return Value

A string representing the input string converted to lower case.

### [](#examples-6)Examples

```sqlpp
SELECT LOWER("N1QL is awesome") as n1ql;
```

```json
{
    "results": [
        {
            "n1ql": "n1ql is awesome"
        }
    ]
}
```

## [](#fn-str-lpad)LPAD(in\_str, size \[, char\])

### [](#description-7)Description

Pads a string with leading characters. The function adds characters to the beginning of the string to pad the string to a specified length.

### [](#arguments-7)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to add the leading characters to.

size

An integer, or any valid [expression](index.md) which evaluates to an integer, that specifies the desired length of the result string.

char

\[Optional; default is Unicode U+0020, i.e. space `" "`\]

A string, or any valid [expression](index.md) which evaluates to a string, that represents the characters to add to the input string.

### [](#return-value-7)Return Value

A string representing the input string with leading characters added.

* If the specified size is smaller than the length of the input string, the input string is truncated and no padding is added.
* If the specified size is larger than the length of the input string, but shorter than the length of the input string plus the padding characters, the padding characters are truncated.
* If the specified size is greater than the length of the input string plus the padding characters, the padding characters are repeated in order until the specified size is reached.

### [](#examples-7)Examples

```sqlpp
SELECT LPAD("N1QL is awesome", 20) AS implicit_padding,
       LPAD("N1QL is awesome", 20, "-*") AS repeated_padding,
       LPAD("N1QL is awesome", 20, "987654321") AS truncate_padding,
       LPAD("N1QL is awesome", 4, "987654321") AS truncate_string;
```

```json
{
    "results": [
        {
            "implicit_padding": "     N1QL is awesome",
            "repeated_padding": "-*-*-N1QL is awesome",
            "truncate_padding": "98765N1QL is awesome",
            "truncate_string": "N1QL"
        }
    ]
}
```

## [](#fn-str-ltrim)LTRIM(in\_str \[, char\])

### [](#description-8)Description

Removes all leading characters from a string. The function removes all consecutive characters from the beginning of the string that match the specified characters and stops when it encounters a character that does not match any of the specified characters.

### [](#arguments-8)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to remove the leading characters from.

char

\[Optional; default is whitespace, i.e. space `" "`, tab `"\t"`, newline `"\n"`, formfeed `"\f"`, or carriage return `"\r"`\]

A string, or any valid [expression](index.md) which evaluates to a string, that represents the characters to trim from the input string. Each character in this string will be trimmed from the input string, it is therefore not necessary to delimit the characters to trim. For example, specifying a character value of `"abc"` will trim the characters "a", "b" and "c" from the start of the string.

### [](#return-value-8)Return Value

A string representing the input string with leading characters removed.

### [](#examples-8)Examples

```sqlpp
SELECT LTRIM("...N1QL is awesome", ".") as dots,
       LTRIM("     N1QL is awesome", " ") as explicit_spaces,
       LTRIM("	  N1QL is awesome") as implicit_spaces,
       LTRIM("N1QL is awesome") as no_dots;
```

```json
{
    "results": [
        {
            "dots": "N1QL is awesome",
            "explicit_spaces": "N1QL is awesome",
            "implicit_spaces": "N1QL is awesome",
            "no_dots": "N1QL is awesome"
        }
    ]
}
```

## [](#fn-str-mask)MASK(in\_str \[, options\])

### [](#description-9)Description

Overlays specified characters in the string with masking characters. This may be useful when returning sensitive information, such as credit card numbers or email addresses.

### [](#arguments-9)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that represents the string to mask.

options

An object containing the following possible parameters:

mask

A string containing masking characters that will be used to overlay the input string. May optionally also contain _hole_ characters, representing gaps in the mask; and _inject_ characters, that are inserted into the output. (Default: `********`)

hole

A string containing the character or characters used to indicate holes in the mask string. (Default: space)

inject

A string containing the character or characters in the mask string that are inserted into the output, rather than overlaying the input. (Default: none)

length

Determines the length of the output string. (Default: missing)

* If this property is missing, or set to anything other than `"source"`, the length of the output is dynamic. Any characters in the input up to the anchor point (see below) are included in the output. The mask then starts at the anchor point, and continues for the length of the specified mask string. Any characters in the input beyond the end of the mask are deleted. This method may therefore obscure the number of characters in the input.
* If the value is `"source"`, the length of the output is the same as the length of the input. Any characters in the input up to the anchor point are included in the output. The mask then starts at the anchor point. If the mask is _longer than_ the remaining length of the input, the mask is truncated to fit. If the mask string is _shorter than or the same length as_ the remaining length of the input, the mask continues for the length of the specified mask string. Any characters in the input beyond the end of the mask are included in the output.

anchor

Determines where in the input string the mask should start. Possible values are `"start"`, `"end"`, a regular expression string, a positive integer, or a negative integer. (Default: `"start"`)

* `"start"` — the mask begins at the start of the input and is applied towards the end.
* `"end"` — the mask begins at the end of the input and is applied from the end towards the start.
* Regular expression — the mask begins at the first point in the input which matches the regular expression, and is applied towards the end. If you need to match the strings `"start"` or `"end"`, use patterns such as `"[s]tart"` or `"[e]nd"`.
* Positive integer — the mask begins the specified number of characters after the start of the input, and is applied towards the end.
* Negative integer — the mask begins the specified number of characters before the end of the input, and is applied towards the start.

If an anchor places the mask outside the boundaries of the input string, the input string is returned unchanged.

### [](#return-value-9)Return Value

A string representing the masked input string.

### [](#examples-9)Examples

Default mask, custom mask, custom mask demonstrating holes.

```sqlpp
SELECT MASK('SomeTextToMask') AS mask,
       MASK('SomeTextToMask', {"mask": "++++"}) AS mask_custom,
       MASK('SomeTextToMask', {"mask": "++++    ++++"}) AS mask_hole;
```

```json
{
    "results": [
        {
            "mask": "********",
            "mask_custom": "++++",
            "mask_hole": "++++Text++++"
        }
    ]
}
```

Mask with character injection.

```sqlpp
SELECT MASK('1234abcd5678efgh', {"mask": "****-****-****-####",
                                 "hole": "#",
                                 "inject": "-"}) AS mask_inject;
```

```json
{
    "results": [
        {
            "mask_inject": "****-****-****-efgh"
        }
    ]
}
```

Mask anchored to the end of the source, with the output length determined by the source.

```sqlpp
SELECT MASK('1234abcd5678efgh', {"mask": "****", "anchor": "end", "length": "source"})
AS end_anchor;
```

```json
{
    "results": [
        {
            "end_anchor": "1234abcd5678****"
        }
    ]
}
```

Mask anchored at the pattern `d5`.

```sqlpp
SELECT MASK('1234abcd5678efgh', {"mask": "****", "anchor": "d5"}) AS regex_anchor;
```

```json
{
    "results": [
        {
            "regex_anchor": "1234abc****"
        }
    ]
}
```

Mask anchored 2 characters from the end of the source, with length determined by the input string.

```sqlpp
SELECT MASK('1234abcd5678efgh', {"mask": "****", "anchor": -2, "length": "source"})
AS negative_anchor
```

```json
{
    "results": [
        {
            "negative_anchor": "1234abcd56****gh"
        }
    ]
}
```

Mask anchored at the 14th character, with length determined by the input string.

```sqlpp
SELECT MASK('1234abcd5678efgh', {"mask": "****", "anchor": 14, "length": "source"})
AS positive_anchor;
```

```json
{
    "results": [
        {
            "positive_anchor": "1234abcd5678ef**"
        }
    ]
}
```

## [](#fn-str-position)POSITION(in\_str, search\_str)

### [](#description-10)Description

Finds the first position of the search string within the string, this position is zero-based, i.e., the first position is 0\. If the search string does not exist within the input string then the function returns -1.

### [](#arguments-10)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to search within.

search\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to search for.

### [](#return-value-10)Return Value

An integer representing the first position of the search string.

### [](#examples-10)Examples

```sqlpp
SELECT POSITION("N1QL is awesome", "awesome") as awesome,
       POSITION("N1QL is awesome", "N1QL") as n1ql,
       POSITION("N1QL is awesome", "SQL") as sql
```

```json
{
    "results": [
        {
            "awesome": 8,
            "n1ql": 0,
            "sql": -1
        }
    ]
}
```

## [](#fn-str-repeat)REPEAT(in\_str, n)

### [](#description-11)Description

Creates a new string which is the input string repeated the specified number of times.

### [](#arguments-11)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to repeat.

n

An integer, or any valid [expression](index.md) which evaluates to an integer, that is the number of times to repeat the string.

### [](#return-value-11)Return Value

A string representing the string generated by repeating the input string.

### [](#limitations-2)Limitations

It is possible to generate very large strings using this function. In some cases the query engine may be unable to process all of these and cause excessive resource consumption. It is therefore recommended that you first validate the inputs to this function to ensure that the generated result is a reasonable size.

### [](#examples-11)Examples

```sqlpp
SELECT REPEAT("N1QL", 0) as empty_string,
       REPEAT("N1QL", 3) as n1ql_3;
```

```json
{
    "results": [
        {
            "empty_string": "",
            "n1ql_3": "N1QLN1QLN1QL"
        }
    ]
}
```

## [](#fn-str-replace)REPLACE(in\_str, search\_str, replace \[, n \])

### [](#description-12)Description

Replaces occurrences of a given substring in an input string.

### [](#arguments-12)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to search for replacements in.

search\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to replace.

replace

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to replace the search string with.

n

\[Optional; default is all instances of the search string are replaced\]

An integer, or any valid [expression](index.md) which evaluates to an integer, which represents the number of instances of the search string to replace. If a negative value is specified then all instances of the search string are replaced.

### [](#return-value-12)Return Value

A string representing the input string with the specified substring replaced.

### [](#examples-12)Examples

```sqlpp
SELECT REPLACE("SQL SQL SQL", "S", "N1", -2) as negative_n,
       REPLACE("SQL SQL SQL", "S", "N1", 2) as replace_2,
       REPLACE("SQL SQL SQL", "S", "N1") as replace_all;
```

```json
{
    "results": [
        {
            "negative_n": "N1QL N1QL N1QL",
            "replace_2": "N1QL N1QL SQL",
            "replace_all": "N1QL N1QL N1QL"
        }
    ]
}
```

## [](#fn-str-reverse)REVERSE(in\_str)

### [](#description-13)Description

Reverses the order of the characters in a given string. i.e. The first character becomes the last character and the last character becomes the first character etc. This is useful for testing whether or not a string is a palindrome.

### [](#arguments-13)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to reverse.

### [](#return-value-13)Return Value

A string representing the input string with its characters reversed.

### [](#examples-13)Examples

```sqlpp
SELECT REVERSE("N1QL is awesome") as n1ql,
       REVERSE("racecar") as palindrome;
```

```json
{
    "results": [
        {
            "n1ql": "emosewa si LQ1N",
            "palindrome": "racecar"
        }
    ]
}
```

## [](#fn-str-rpad)RPAD(in\_str, size \[, char\])

### [](#description-14)Description

Pads a string with trailing characters. The function adds characters to the end of the string to pad the string to a specified length.

### [](#arguments-14)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to add the trailing characters to.

size

An integer, or any valid [expression](index.md) which evaluates to an integer, that specifies the desired length of the result string.

char

\[Optional; default is Unicode U+0020, i.e. space `" "`\]

A string, or any valid [expression](index.md) which evaluates to a string, that represents the characters to add to the input string.

### [](#return-value-14)Return Value

A string representing the input string with trailing characters added.

* If the specified size is smaller than the length of the input string, the input string is truncated and no padding is added.
* If the specified size is larger than the length of the input string, but shorter than the length of the input string plus the padding characters, the padding characters are truncated.
* If the specified size is greater than the length of the input string plus the padding characters, the padding characters are repeated in order until the specified size is reached.

### [](#examples-14)Examples

```sqlpp
SELECT RPAD("N1QL is awesome", 20) AS implicit_padding,
       RPAD("N1QL is awesome", 20, "-*") AS repeated_padding,
       RPAD("N1QL is awesome", 20, "123456789") AS truncate_padding,
       RPAD("N1QL is awesome", 4, "123456789") AS truncate_string;
```

```json
{
    "results": [
        {
            "implicit_padding": "N1QL is awesome     ",
            "repeated_padding": "N1QL is awesome-*-*-",
            "truncate_padding": "N1QL is awesome12345",
            "truncate_string": "N1QL"
        }
    ]
}
```

## [](#fn-str-rtrim)RTRIM(in\_str \[, char\])

### [](#description-15)Description

Removes all trailing characters from a string. The function removes all consecutive characters from the end of the string that match the specified characters and stops when it encounters a character that does not match any of the specified characters.

### [](#arguments-15)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to convert to remove trailing characters from.

char

\[Optional; default is whitespace, i.e. space `" "`, tab `"\t"`, newline `"\n"`, formfeed `"\f"`, or carriage return `"\r"`\]

A string, or any valid [expression](index.md) which evaluates to a string, that represents the characters to trim from the input string. Each character in this string will be trimmed from the input string, it is therefore not necessary to delimit the characters to trim. For example specifying a character value of `"abc"` will trim the characters `"a"`, `"b"` and `"c"` from the start of the string.

### [](#return-value-15)Return Value

A string representing the input string with its trailing characters removed.

### [](#examples-15)Examples

```sqlpp
SELECT RTRIM("N1QL is awesome...", ".") as dots,
       RTRIM("N1QL is awesome     ", " ") as explicit_spaces,
       RTRIM("N1QL is awesome     ") as implicit_spaces,
       RTRIM("N1QL is awesome") as no_dots;
```

```json
{
    "results": [
        {
            "dots": "N1QL is awesome",
            "explicit_spaces": "N1QL is awesome",
            "implicit_spaces": "N1QL is awesome",
            "no_dots": "N1QL is awesome"
        }
    ]
}
```

## [](#fn-str-split)SPLIT(in\_str \[, in\_substr\])

### [](#description-16)Description

Splits the string into an array of substrings, based on the specified separator string.

### [](#arguments-16)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to split.

in\_substr

A string, or any valid [expression](index.md) which evaluates to a string, that is the substring to split the input string on.

### [](#return-value-16)Return Value

An array of strings containing the strings created by splitting the input string.

### [](#examples-16)Examples

```sqlpp
SELECT SPLIT("N1QL is awesome", " ") as explicit_spaces,
       SPLIT("N1QL is awesome") as implicit_spaces,
       SPLIT("N1QL is awesome", "is") as split_is
```

```json
{
    "results": [
        {
            "explicit_spaces": [
                "N1QL",
                "is",
                "awesome"
            ],
            "implicit_spaces": [
                "N1QL",
                "is",
                "awesome"
            ],
            "split_is": [
                "N1QL ",
                " awesome"
            ]
        }
    ]
}
```

## [](#fn-str-substr)SUBSTR(in\_str, start\_pos \[, length\])

### [](#description-17)Description

Returns the substring (of given length) starting at the provided position. The position is zero-based, i.e. the first position is 0\. If position is negative, it is counted from the end of the string; -1 is the last position in the string.

### [](#arguments-17)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to convert to extract the substring from.

start\_pos

An integer, or any valid [expression](index.md) which evaluates to an integer, that is the start position of the substring.

length

\[Optional; default is to capture to the end of the string\]

An integer, or any valid [expression](index.md) which evaluates to an integer, that is the length of the substring to extract.

### [](#return-value-17)Return Value

A string representing the substring extracted from the input string.

### [](#examples-17)Examples

```sqlpp
SELECT SUBSTR("N1QL is awesome", 3) as end_of_string,
       SUBSTR("N1QL is awesome", 3, 1) as single_letter,
       SUBSTR("N1QL is awesome", 3, 3) as three_letters
```

```json
{
    "results": [
        {
            "end_of_string": "L is awesome",
            "single_letter": "L",
            "three_letters": "L i"
        }
    ]
}
```

## [](#fn-str-suffixes)SUFFIXES(in\_str)

### [](#description-18)Description

Generates an array of all the suffixes of the input string.

### [](#arguments-18)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to generate the suffixes of.

### [](#return-value-18)Return Value

An array of strings containing all of the suffixes of the input string.

### [](#examples-18)Examples

```sqlpp
SELECT SUFFIXES("N1QL is awesome") as n1ql
```

```json
{
    "results": [
        {
            "n1ql": [
                "N1QL is awesome",
                "1QL is awesome",
                "QL is awesome",
                "L is awesome",
                " is awesome",
                "is awesome",
                "s awesome",
                " awesome",
                "awesome",
                "wesome",
                "esome",
                "some",
                "ome",
                "me",
                "e"
            ]
        }
    ]
}
```

The following example uses the `SUFFIXES()` function to index and query the airport names when a partial airport name is given.

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

```sqlpp
CREATE INDEX autocomplete_airport_name
ON airport ( DISTINCT ARRAY array_element FOR array_element
IN SUFFIXES(LOWER(airportname)) END )
```

```sqlpp
SELECT airportname
FROM airport
WHERE ANY array_element
IN SUFFIXES(LOWER(airportname)) SATISFIES array_element LIKE 'washing%' END
```

```json
{
    "results": [
        {
            "airportname": "Ronald Reagan Washington Natl"
        },
        {
            "airportname": "Washington Dulles Intl"
        },
        {
            "airportname": "Baltimore Washington Intl"
        },
        {
            "airportname": "Washington Union Station"
        }
    ]
}
```

This [blog](https://dzone.com/articles/a-couchbase-index-technique-for-like-predicates-wi) provides more information about this example.

## [](#fn-str-title)TITLE(in\_str)

Alias for [INITCAP()](#fn-str-initcap).

## [](#fn-str-token)TOKENS(in\_str, opt)

### [](#description-19)Description

This function tokenizes (i.e. breaks up into meaningful segments) the given input string based on specified delimiters, and other options. It recursively enumerates all tokens in a JSON value and returns an array of values (JSON atomic values) as the result.

### [](#arguments-19)Arguments

in\_str

A valid JSON object, this can be anything: constant literal, simple JSON value, JSON key name or the whole document itself.

The following table lists the rules for each JSON type:

| JSON Type | Return Value                                                                        |
| --------- | ----------------------------------------------------------------------------------- |
| MISSING   | \[\]                                                                                |
| NULL      | \[NULL\]                                                                            |
| false     | \[false\]                                                                           |
| true      | \[true\]                                                                            |
| number    | \[number\]                                                                          |
| string    | SPLIT(string)                                                                       |
| array     | FLATTEN(TOKENS(element) for each element in array (Concatenation of element tokens) |
| object    | For each name-value pair, name+TOKENS(value)                                        |

opt

A JSON object indicating the options passed to the `TOKENS()` function. Options can take the following options, and each invocation of `TOKENS()` can choose one or more of the options:

{"name": true}

**Optional**. Valid values are `true` or `false`. By default, this is set to true and `TOKENS()` will include field names. You can choose to not include field names by setting this option to `false`.

{"case":"lower"}

**Optional**. Valid values are `lower` or `upper`. Default is neither, as in it returns the case of the original data. Use this option to specify the case sensitivity.

{"specials": true}

**Optional**. Use this option to preserve strings with specials characters, such as email addresses, URLs, and hyphenated phone numbers. The default value is `false`.

> [!NOTE]
> The `specials` options preserves special characters except at the end of a word.

### [](#return-value-19)Return Value

An array of strings containing all of the tokens obtained from the input string.

### [](#examples-19)Examples

> [!NOTE]
> By default, for speed, the results are randomly ordered. To make the difference more clear between the first two example queries, the `ARRAY_SORT()` function is used.

List the tokens of an array where `specials` is FALSE

```sqlpp
SELECT ARRAY_SORT(
  TOKENS( ['jim@example.com, kim@example.com, http://example.com/, 408-555-1212'],
          {'specials': false} ));
```

```json
[
  {
    "$1": [
      "1212",
      "408",
      "555",
      "abc",
      "com",
      "http",
      "jim",
      "kim"
    ]
  }
]
```

List the tokens of an array where `specials` is TRUE

```sqlpp
SELECT ARRAY_SORT(
  TOKENS( ['jim@example.com, kim@example.com, http://example.com/, 408-555-1212'],
          {'specials': true} ));
```

```json
[
  {
    "$1": [
      "1212",
      "408",
      "408-555-1212",
      "555",
      "abc",
      "com",
      "http",
      "http://example.com",
      "jim",
      "jim@example.com",
      "kim",
      "kim@example.com"
    ]
  }
]
```

Convert all of the URL data into UPPER case and adds the full URL to the delimited words

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

```sqlpp
SELECT ARRAY_SORT( TOKENS(url) ) AS defaulttoken,
       ARRAY_SORT( TOKENS(url, {"specials":true, "case":"UPPER"}) ) AS specialtoken
FROM hotel
LIMIT 1;
```

```json
[
  {
    "defaulttoken": [
      "http",
      "org",
      "uk",
      "www",
      "yha"
    ],
    "specialtoken": [
      "HTTP",
      "HTTP://WWW.YHA.ORG.UK",
      "ORG",
      "UK",
      "WWW",
      "YHA"
    ]
  }
]
```

You can also use `{"case":"lower"}` or `{"case":"upper"}` to have case sensitive search. Index creation and querying can use this and other parameters in combination. These parameters should be passed within the query predicates as well. The parameters and values must match exactly for N1QL to pick up and use the index correctly.

Create an index with `case` and use it your application

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

```sqlpp
CREATE INDEX idx_url_upper_special ON hotel(
    DISTINCT ARRAY v FOR v IN
        TOKENS(url, {"specials":true, "case":"UPPER"})
    END );
```

```sqlpp
SELECT name, address, url
FROM hotel
WHERE ANY v IN TOKENS(url, {"specials":true, "case":"UPPER"})
      SATISFIES v = "HTTP://WWW.YHA.ORG.UK"
      END;
```

```json
{
    "results": [
        {
            "address": "Capstone Road, ME7 3JE",
            "name": "Medway Youth Hostel",
            "url": "http://www.yha.org.uk"
        }
    ]
}
```

## [](#fn-str-trim)TRIM(in\_str \[, char\])

### [](#description-20)Description

Removes all leading and trailing characters from a string. The function removes all consecutive characters from the beginning and end of the string that match the specified characters and stops when it encounters a character that does not match any of the specified characters. This function is equivalent to calling `LTRIM()` and `RTRIM()` successively.

### [](#arguments-20)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to convert to remove trailing and leading characters from.

char

\[Optional; default is Unicode U+0020, i.e. `" "`\]

A string, or any valid [expression](index.md) which evaluates to a string, that represents the characters to trim from the input string. Each character in this string will be trimmed from the input string, it is therefore not necessary to delimit the characters to trim. For example specifying a character value of `"abc"` will trim the characters `"a"`, `"b"` and `"c"` from the start of the string.

### [](#return-value-20)Return Value

A string representing the input string with trailing and leading characters removed.

### [](#examples-20)Examples

```sqlpp
SELECT TRIM("...N1QL is awesome...", ".") as dots,
       TRIM("     N1QL is awesome     ", " ") as explicit_spaces,
       TRIM("     N1QL is awesome     ") as implicit_spaces,
       TRIM("N1QL is awesome") as no_dots;
```

```json
{
    "results": [
        {
            "dots": "N1QL is awesome",
            "explicit_spaces": "N1QL is awesome",
            "implicit_spaces": "N1QL is awesome",
            "no_dots": "N1QL is awesome"
        }
    ]
}
```

## [](#fn-str-upper)UPPER(in\_str)

### [](#description-21)Description

Converts all characters in the input string to upper case.

### [](#arguments-21)Arguments

in\_str

A string, or any valid [expression](index.md) which evaluates to a string, that is the string to convert to upper case.

### [](#return-value-21)Return Value

A string representing the input string converted to upper case.

### [](#examples-21)Examples

```sqlpp
SELECT UPPER("N1QL is awesome") as n1ql;
```

```json
{
    "results": [
        {
            "n1ql": "N1QL IS AWESOME"
        }
    ]
}
```