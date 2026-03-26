---
title: String Functions
description: This topic describes the builtin SQL++ for Enterprise Analytics
  string functions.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/8_builtin_str.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:sqlpp:8_builtin_str.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sqlpp/8_builtin_str.html)

# String Functions

> This topic describes the builtin SQL++ for Enterprise Analytics string functions. 

## [](#concat)concat

* Syntax:  
concat(string1, string2, ...)
* Returns a concatenated string from arguments.
* Arguments:

  * `string1`: a string value,
  * `string2`: a string value,
  * …​.
* Return Value:

  * a concatenated string from arguments,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value causes a type error.
* Example:  
concat("test ", "driven ", "development");
* The expected result is:  
"test driven development"

## [](#contains)contains

* Syntax:  
contains(string, substring_to_contain)
* Checks whether the string `string` contains the string `substring_to_contain`
* Arguments:

  * `string` : a `string` that might contain the given substring,
  * `substring_to_contain` : a target `string` that might be present in the `string`.
* Return Value:

  * a `Boolean` value, `true` if `string` contains `substring_to_contain`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value causes a type error,
  * `false` otherwise.
* Example:  
{ "v1": contains("I like x-phone", "phone"), "v2": contains("one", "phone") };
* The expected result is:  
{ "v1": true, "v2": false }

## [](#ends%5Fwith)ends\_with

* Syntax:  
ends_with(string, substring_to_end_with)
* Checks whether the string `string` ends with the string `substring_to_end_with`.
* Arguments:

  * `string` : a `string` that might end with the given string,
  * `substring_to_end_with` : a `string` that might be the ending substring.
* Return Value:

  * a `Boolean` value, `true` if `string` contains `substring_to_contain`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value causes a type error,
  * `false` otherwise.
* Example:  
{  
  "v1": ends_with(" love product-b its shortcut_menu is awesome:)", ":)"),  
  "v2": ends_with(" awsome:)", ":-)")  
};
* The expected result is:  
{ "v1": true, "v2": false }

## [](#initcap-or-title)initcap (or title)

* Syntax:  
initcap(string)
* Converts a given string `string` so that the first letter of each word is uppercase and every other letter is lowercase. The function has an alias called "title".
* Arguments:

  * `string` : a `string` to convert.
* Return Value:

  * a `string` as the title form of the given `string`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value causes a type error.
* Example:  
{ "v1": initcap("ANALYTICS is here!"), "v2": title("ANALYTICS is here!") };
* The expected result is:  
{ "v1": "Analytics Is Here!", "v2": "Analytics Is Here!" }

## [](#length)length

* Syntax:  
length(string)
* Returns the length of the string `string` in code point units. See the following examples for more details.
* Arguments:

  * `string` : a `string` or `null` that represents the string to check.
* Return Value:

  * an `bigint` that represents the length of `string`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value causes a type error.
* Example:  
length("test string");
* The expected result is:  
11
* Example:  
length("👩‍👩‍👧‍👦");
* The expected result for this emoji character 👩‍👩‍👧‍👦 with 7 code points:  
7

## [](#lower)lower

* Syntax:  
lower(string)
* Converts a given string `string` to its lowercase form.
* Arguments:

  * `string` : a `string` to convert.
* Return Value:

  * a `string` as the lowercase form of the given `string`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value causes a type error.
* Example:  
lower("ANALYTICS");
* The expected result is:  
"analytics"

## [](#ltrim)ltrim

* Syntax:  
ltrim(string[, chars]);
* Returns a new string with all leading characters that appear in `chars` removed. By default, white space is the character to trim. Here, one character means one code point. For example, the emoji 4-people-family notation 👩‍👩‍👧‍👦 contains 7 code points, and it's possible to trim a few code points (such as a 2-people-family 👨‍👦) from it. See the following example for more details.
* Arguments:

  * `string` : a `string` to trim,
  * `chars` : a `string` that contains characters that are used to trim.
* Return Value:

  * a trimmed, new `string`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value causes a type error.
* Related functions: see `trim()`, `rtrim()`
* Example:  
ltrim("me like x-phone", "eml");
* The expected result is:  
" like x-phone"
* Example with multi-codepoint notation (trim the man and boy from the family of man, woman, girl and boy):  
ltrim("👨‍👩‍👧‍👦", "👨‍👦")
* The expected result is (only woman, girl and boy are left in the family):  
"👩‍👧‍👦"

## [](#position)position

* Syntax:  
position(string, string_pattern)
* Returns the first position of `string_pattern` within `string`. The result is counted in the unit of code points. See the following example for more details.
* The function returns the 0-based position. Another version of the function returns the 1-based position. Below are the aliases for each version:

  * 0-based: `position`, `pos`, `position0`, `pos0`.
  * 1-based: `position1`, `pos1`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` to match.
* Return Value:

  * the first position that `string_pattern` appears within `string`, starting at 0, or -1 if it does not appear,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value returns a `null`.
* Example:  
{  
  "v1": position("ppphonepp", "phone"),  
  "v2": position("hone", "phone"),  
  "v3": position1("ppphonepp", "phone"),  
  "v4": position1("hone", "phone")  
};
* The expected result is:  
{ "v1": 2, "v2": -1, v3": 3, "v4": -1 }
* Example of multi-code-point character:  
position("👩‍👩‍👧‍👦🏀", "🏀");
* The expected result is (the emoji family character has 7 code points):  
7

## [](#regexp%5Fcontains)regexp\_contains

* Syntax:  
regexp_contains(string, string_pattern[, string_flags])
* Checks whether the strings `string` contains the regular expression pattern `string_pattern` (a Java regular expression pattern).
* Aliases:

  * `regexp_contains`, `regex_contains`, `contains_regexp`, `contains_regex`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` to match.
  * `string_flag` : Optional. A `string` with flags to use during regular expression matching.

    * The following modes are enabled with these flags: dotall (s), multiline (m), case\_insensitive (i), and comments and whitespace (x).
* Return Value:

  * a `Boolean`, returns `true` if `string` contains the pattern `string_pattern`, `false` otherwise.
  * `missing` if any argument is a `missing` value.
  * `null` if any argument is a `null` value but no argument is a `missing` value.
  * any other non-string input value returns a `null`.
* Example:  
{  
  "v1": regexp_contains("pphonepp", "p*hone"),  
  "v2": regexp_contains("hone", "p+hone")  
};
* The expected result is:  
{ "v1": true, "v2": false }

## [](#regexp%5Flike)regexp\_like

* Syntax:  
regexp_like(string, string_pattern[, string_flags])
* Checks whether the string `string` exactly matches the regular expression pattern `string_pattern`(a Java regular expression pattern).
* Aliases:

  * `regexp_like`, `regex_like`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` that might be contained.
  * `string_flag` : Optional. A `string` with flags to use during regular expression matching.

    * The following modes are enabled with these flags: dotall (s), multiline (m), case\_insensitive (i), and comments and whitespace (x).
* Return Value:

  * a `Boolean` value, `true` if `string` contains the pattern `string_pattern`, `false` otherwise.
  * `missing` if any argument is a `missing` value.
  * `null` if any argument is a `null` value but no argument is a `missing` value.
  * any other non-string input value returns a `null`.
* Example:  
{  
  "v1": regexp_like(" can't stand acast the network is horrible:(", ".*acast.*"),  
  "v2": regexp_like("acast", ".*acst.*")  
};
* The expected result is:  
{ "v1": true, "v2": false }

## [](#regexp%5Fposition)regexp\_position

* Syntax:  
regexp_position(string, string_pattern[, string_flags])
* Returns first position of the regular expression `string_pattern` (a Java regular expression pattern) within `string`. The function returns the 0-based position. Another version of the function returns the 1-based position. Below are the aliases for each version:
* Aliases:

  * 0-Based: `regexp_position`, `regexp_pos`, `regexp_position0`, `regexp_pos0`, `regex_position`, `regex_pos`, `regex_position0`, `regex_pos0`.
  * 1-Based: `regexp_position1`, `regexp_pos1`, `regex_position1` `regex_pos1`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` to be matched.
  * `string_flag` : Optional. A `string` with flags to use during regular expression matching.

    * The following modes are enabled with these flags: dotall (s), multiline (m), case\_insensitive (i), and comments and whitespace (x).
* Return Value:

  * the first position that the regular expression `string_pattern` appears in `string`(starting at 0), or -1 if it does not appear.
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value returns a `null`.
* Example:  
{  
  "v1": regexp_position("pphonepp", "p*hone"),  
  "v2": regexp_position("hone", "p+hone"),  
  "v3": regexp_position1("pphonepp", "p*hone"),  
  "v4": regexp_position1("hone", "p+hone")  
};
* The expected result is:  
{ "v1": 0, "v2": -1, "v3": 1, "v4": -1 }

## [](#regexp%5Freplace)regexp\_replace

* Syntax:  
regexp_replace(string, string_pattern, string_replacement[, string_flags])  
regexp_replace(string, string_pattern, string_replacement[, replacement_limit])
* Checks whether the string `string` matches the given regular expression pattern `string_pattern` (a Java regular expression pattern), and replaces the matched pattern `string_pattern` with the new pattern `string_replacement`.
* Aliases:

  * `regexp_replace`, `regex_replace`.
* Arguments:

  * `string` : a `string` that might contain the pattern.
  * `string_pattern` : a pattern `string` to be matched.
  * `string_replacement` : a pattern `string` to use as the replacement.
  * `string_flag` : Optional. A `string` with flags to use during replace.

    * The following modes are enabled with these flags: dotall (s), multiline (m), case\_insensitive (i), and comments and whitespace (x).
  * `replacement_limit`: Optional. An `integer` specifying the maximum number of replacements to make (if negative then all occurrences will be replaced)
* Return Value:

  * Returns a `string` that is obtained after the replacements.
  * `missing` if any argument is a `missing` value.
  * `null` if any argument is a `null` value but no argument is a `missing` value.
  * any other non-string input value returns a `null`.
* Example:  
regexp_replace(" like x-phone the voicemail_service is awesome", " like x-phone", "like product-a");
* The expected result is:  
"like product-a the voicemail_service is awesome"

## [](#repeat)repeat

* Syntax:  
repeat(string, n)
* Returns a string formed by repeating the input `string` `n` times.
* Arguments:

  * `string` : a `string` to be repeated,
  * `n` : an `tinyint`/`smallint`/`integer`/`bigint` value - how many times the string should be repeated.
* Return Value:

  * a string that repeats the input `string` `n` times,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * a type error will be raised if:

    * the first argument is any other non-string value,
    * or, the second argument is not a `tinyint`, `smallint`, `integer`, or `bigint`.
* Example:  
repeat("test", 3);
* The expected result is:  
"testtesttest"

## [](#replace)replace

* Syntax:  
replace(string, search_string, replacement_string[, limit])
* Finds occurrences of the given substring `search_string` in the input string `string`and replaces them with the new substring `replacement_string`.
* Arguments:

  * `string` : an input `string`,
  * `search_string` : a `string` substring to be searched for,
  * `replacement_string` : a `string` to use as the replacement,
  * `limit` : Optional. An `integer` \- maximum number of occurrences to be replaced. If not specified or negative then all occurrences will be replaced
* Return Value:

  * Returns a `string` that is obtained after the replacements,
  * `missing` if any argument is a `missing` value,
  * any other non-string input value or non-integer `limit` causes a type error,
  * `null` if any argument is a `null` value but no argument is a `missing` value.
* Example:  
{  
  "v1": replace(" like x-phone the voicemail_service is awesome", " like x-phone", "like product-a"),  
  "v2": replace("x-phone and x-phone", "x-phone", "product-a", 1)  
};
* The expected result is:  
{  
  "v1": "like product-a the voicemail_service is awesome",  
  "v2": "product-a and x-phone"  
}

## [](#reverse)reverse

* Syntax:  
reverse(string)
* Returns a string formed by reversing characters in the input `string`. For characters of multiple code points, code point is the minimal unit to reverse. See the following examples for more details.
* Arguments:

  * `string` : a `string` to be reversed
* Return Value:

  * a string containing characters from the the input `string` in the reverse order,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * a type error will be raised if:

    * the first argument is any other non-string value
* Example:  
reverse("hello");
* The expected result is:  
"olleh"
* Example of multi-code-point character (Korean):  
reverse("한글");
* The expected result, in which the Korean characters are split into code points and then the code points are reversed:  
"ᆯᅳᄀᆫᅡᄒ"

## [](#rtrim)rtrim

* Syntax:  
rtrim(string[, chars]);
* Returns a new string with all trailing characters that appear in `chars` removed. By default, white space is the character to trim. Note that here one character means one code point. For example, the emoji 4-people-family notation "👩‍👩‍👧‍👦" contains 7 code points, and it is possible to trim a few code points (such as a 2-people-family "👨‍👦") from it. See the following example for more details.
* Arguments:

  * `string` : a `string` to be trimmed,
  * `chars` : a `string` that contains characters that are used to trim.
* Return Value:

  * a trimmed, new `string`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value causes a type error.
* Related functions: see `trim()`, `ltrim()`
* Example:  
{  
  "v1": rtrim("i like x-phone", "x-phone"),  
  "v2": rtrim("i like x-phone", "onexph")  
};
* The expected result is:  
{ "v1": "i like ", "v2": "i like x-" }
* Example with multi-codepoint notation (trim the man and boy from the family of man, woman, girl and boy):  
rtrim("👨‍👩‍👧‍👦", "👨‍👦")
* The expected result is (only man, woman and girl are left in the family):  
"👨‍👩‍👧"

## [](#split)split

* Syntax:  
split(string, sep)
* Splits the input `string` into an array of substrings separated by the string `sep`.
* Arguments:

  * `string` : a `string` to be split.
* Return Value:

  * an array of substrings by splitting the input `string` by `sep`,
  * in case of two consecutive `sep`s in the `string`, the result of splitting the two consecutive `sep`s will be the empty string `""`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value causes a type error.
* Example:  
split("test driven development", " ");
* The expected result is:  
[ "test", "driven", "development" ]
* Example with two consecutive `sep`s in the `string`:  
split("123//456", "/");
* The expected result is:  
[ "123", "", "456" ]

## [](#starts%5Fwith)starts\_with

* Syntax:  
starts_with(string, substring_to_start_with)
* Checks whether the string `string` starts with the string `substring_to_start_with`.
* Arguments:

  * `string` : a `string` that might start with the given string.
  * `substring_to_start_with` : a `string` that might be contained as the starting substring.
* Return Value:

  * a `Boolean`, returns `true` if `string` starts with the string `substring_to_start_with`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value causes a type error,
  * `false` otherwise.
* Example:  
{  
  "v1" : starts_with(" like the plan, amazing", " like"),  
  "v2" : starts_with("I like the plan, amazing", " like")  
};
* The expected result is:  
{ "v1": true, "v2": false }

## [](#substr)substr

* Syntax:  
substr(string, offset[, length])
* Returns the substring from the given string `string` based on the given start offset `offset` with the optional `length`. Note that both of the `offset` and `length` are in the unit of code point (e.g. the emoji family 👨‍👩‍👧‍👦 has 7 code points). The function uses the 0-based position. Another version of the function uses the 1-based position. Below are the aliases for each version:
* Aliases:

  * 0-Based: `substring`, `substr`, `substring0`, `substr0`.
  * 1-Based: `substring1`, `substr1`.
* Arguments:

  * `string` : a `string` to extract.
  * `offset` : an `tinyint`/\`sm, starting at 0\. If negative then counted from the end of the string.
  * `length` : Optional. A `tinyint`/`smallint`/`integer`/`bigint` value as the length of the substring.
* Return Value:

  * a `string` that represents the substring,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value, or if the substring could not be obtained because the starting offset is not within string bounds or `length` is negative.
  * a `null` will be returned if:

    * the first argument is any other non-string value.
    * the second argument is not a `tinyint`, `smallint`, `integer`, or `bigint`.
    * the third argument is not a `tinyint`, `smallint`, `integer`, or `bigint` if the argument is present.
* Example:  
{ "v1": substr("test string", 6, 3), "v2": substr1("test string", 6, 3) };
* The expected result is:  
{ "v1": "tri", "v2": "str" }

The function has an alias `substring`.

## [](#trim)trim

* Syntax:  
trim(string[, chars]);
* Returns a new string with all leading and trailing characters that appear in `chars` removed. By default, white space is the character to trim. Note that here one character means one code point. For example, the emoji 4-people-family notation "👩‍👩‍👧‍👦" contains 7 code points, and it is possible to trim a few code points (such as a 2-people-family "👨‍👦") from it. See the following example for more details.
* Arguments:

  * `string` : a `string` to be trimmed,
  * `chars` : a `string` that contains characters that are used to trim.
* Return Value:

  * a trimmed, new `string`,
  * `missing` if any argument is a `missing` value,
  * `null` if any argument is a `null` value but no argument is a `missing` value,
  * any other non-string input value causes a type error.
* Related functions: see `ltrim()`, `rtrim()`
* Example:  
trim("i like x-phone", "xphoen");
* The expected result is:  
" like "
* Example with multi-codepoint notation (trim the man and boy from the family of man, woman, girl and boy):  
trim("👨‍👩‍👧‍👦", "👨‍👦")
* The expected result is (only woman and girl are left in the family):  
"👩‍👧"

## [](#upper)upper

* Syntax:  
upper(string)
* Converts a given string `string` to its uppercase form.
* Arguments:

  * `string` : a `string` to be converted.
* Return Value:

  * a `string` as the uppercase form of the given `string`,
  * `missing` if the argument is a `missing` value,
  * `null` if the argument is a `null` value,
  * any other non-string input value causes a type error.
* Example:  
upper("hello")
* The expected result is:  
"HELLO"

## [](#concat2)concat2

* Syntax:  
concat2(string_separator, string_or_array_of_strings1, string_or_array_of_strings2, ...)
* This function takes the input strings, or arrays of strings, and concatenates them with the specified separator between each input string. Arrays of strings are flattened and concatenated in the same order. If there is only a single string argument, the separator is not used.
* Arguments:

  * `string_separator`: a string value representing the separator to use between the concatenated strings.
  * `string_or_array_of_strings1`: a string or an array of strings to be concatenated.
  * …​.
* Return Value:

  * a concatenated string from arguments with separator between each argument.
  * `missing` if any argument is a `missing` value.
  * `missing` if an array is provided, and any element in the array is `missing`.
  * `null` if any argument (or any array element) is a `null` but no argument (or any array element) is a `missing`value.
  * any other non-string input value returns a `null`.
* Example:  
concat2("-", "ab", "cd", ["e", "f", "g"]);
* The expected result is:  
"ab-cd-e-f-g"