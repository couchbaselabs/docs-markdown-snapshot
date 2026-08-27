---
title: finderr
description: The <code class="cmd">finderr</code> tool returns the full details
  of any Query service or cbq shell error.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/cli/pages/finderr.adoc
  xref: xref:server:cli:finderr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/cli/finderr.html)

# finderr

> The `finderr` tool returns the full details of any Query service or cbq shell error. 

## [](#syntax)Syntax

The basic syntax is:

finderr <number|string|regex>

## [](#description)Description

Depending upon your platform, this tool is at the following locations:

| Operating system | Location                                                                 |
| ---------------- | ------------------------------------------------------------------------ |
| Linux            | /opt/couchbase/bin/                                                      |
| Windows          | C:\\Program Files\\Couchbase\\Server\\bin\\                              |
| Mac OS X         | /Applications/CouchbaseServer.app/Contents/Resources/couchbase-core/bin/ |

## [](#options)Options

The tool takes a single argument, which must be one of the following:

number

A number representing an error code. In this case, the tool returns the full details of the error matching the error code.

string

A string. In this case, the tool searches for the target string in all of the error message fields except for `USER ERROR`, and returns the full details of any errors that match the string.

regex

A regular expression. In this case, the tool searches for the regular expression in all of the error message fields except for `USER ERROR`, and returns the full details of any errors that match the pattern.

## [](#output)Output

If the tool finds a single error that matches the find argument, it outputs the full details of the error.

If the tool finds multiple errors that match the find argument, it outputs a list showing the code and description of each matching error. You can use the tool again, passing the code or description as an argument, to get the full details of any of these errors.

Full error details include some or all of the following fields.

| Name            | Description                                                                                                                                                           |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **APPLIES TO**  | One of the following: cbq-shell: The error applies to the cbq shell. Server: The error applies to the server.                                                         |
| **CODE**        | A number representing the error.                                                                                                                                      |
| **DESCRIPTION** | Message describing why the error occurred.                                                                                                                            |
| **REASON**      | List of possible causes of the error.                                                                                                                                 |
| **USER ACTION** | List of possible steps a user can take to mitigate the error.                                                                                                         |
| **USER ERROR**  | One of the following: Yes: The error was caused by the user. No: The error was caused by other services, or was internal to the server. Maybe: A combination of both. |

> [!NOTE]
> The error details also include a `SYMBOL` field, which contains a representation string for the error. This field is for internal use only, and is not shown in the output. However, the tool does search this field when the find argument is a string or a regular expression.

## [](#examples)Examples

Example 1\. Find error details by code number

Command

```sh
./finderr 5011
```

Output

CODE
  5011 (error)


DESCRIPTION
  Abort: «reason»


REASON
  The SQL++ abort() function was called in the statement.
  e.g. SELECT abort('An example cause')


USER ERROR
  Yes


APPLIES TO
  Server

Example 2\. Find error details by matching a string

Command

```sh
./finderr "A semantic error is present in the statement."
```

Output

CODE
  3100 (error)


DESCRIPTION
  A semantic error is present in the statement.


REASON
  The statement includes portions that violate semantic constraints.


USER ACTION
  The cause will contain more detail on the violation; revise the statement and re-submit.


USER ERROR
  Yes


APPLIES TO
  Server

Example 3\. Find multiple errors by matching a string

Command

```sh
./finderr "semantic"
```

Output

Matching errors
  3100 A semantic error is present in the statement.
  3220 «name» window function «clause» «reason»
  3300 recursive_with semantics: «cause»

Example 4\. Find multiple errors by matching a regular expression

Command

```sh
./finderr "[UI][NP]SERT"
```

Output

Matching errors
  3150 MERGE with ON KEY clause cannot have document key specification in INSERT action.
  3160 MERGE with ON clause must have document key specification in INSERT action
  3180 MERGE with ON KEY clause cannot have USE INDEX hint specified on target.
  5006 Out of key validation space.
  5050 No INSERT key for «document»
  5060 No INSERT value for «document»
  5070 Cannot INSERT non-string key «key» of type «type»
  5071 Cannot INSERT non-OBJECT options «options» of type «type»
  5072 No UPSERT key for «value»
  5073 Cannot act on the same key multiple times in an UPSERT statement
  5075 No UPSERT value for «value»
  5078 Cannot UPSERT non-string key «key» of type «type».
  5079 Cannot UPSERT non-OBJECT options «value» of type «type».
  5330 Multiple INSERT of the same document (document key «key») in a MERGE statement
 12036 Error in INSERT of key: «key»
 15005 No keys to insert «details»

## [](#see-also)See Also

* The SQL++ [FINDERR()](../n1ql/n1ql-language-reference/metafun.md#finderr) function
* [SQL++ Error Codes](../n1ql/n1ql-language-reference/n1ql-error-codes.md)