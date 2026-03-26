---
title: AsciiDoc Basics
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/basics.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:home:contribute:basics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/basics.html)

# AsciiDoc Basics

Use the following as a reference for some of the common AsciiDoc markup used to write Couchbase Documentation.

## [](#inline-styles)Inline Styles

Use inline styles to add special markup to characters, words, or whole sentences inside your documentation.

### [](#bold-and-code-styles)Bold and Code Styles

Use the **bold** and `code` (highlighted monospace font) styles to mark up UI elements and user input in the documentation.

For example:

```asciidoc
A bold *word*, a *bold phrase*, and bold c**hara**cter**s**.

A monospace `word`, a `monospace phrase`, and monospace c``hara``cter``s``.

`*monospace bold phrase*` and ``**char**``acter``**s**``
```

Renders as:

A bold **word**, a **bold phrase**, and bold c**hara**cter**s**.

A monospace `word`, a `monospace phrase`, and monospace c`hara`cter`s`.

`**monospace bold phrase**` and `**char**`acter`**s**`

You can add multiple inline styles to text as long as the syntax is placed in the correct order. Monospace syntax (`` ` ``) is always the outermost formatting set.

For more information about when to use monospace and bold font, see [Monospace Font (Highlighted)](../../styleguide/monospace-highlight.md) or [Bold](../../styleguide/bold.md).

Do not use the `code` style to mark up extended code samples or examples in the documentation. To mark up code blocks and include example files, see [Code Blocks and Callouts](code-blocks.md).

> [!NOTE]
> Couchbase style does not allow the use of italic markup for text. For more information, see [Italics](../../styleguide/italic.md).

### [](#ui-macros)Button, Keyboard, and Menu UI Macros

Couchbase style uses 3 different markup styles for different user interactions with the UI:

* Use the **button macro** to mark up specific button interactions in a UI procedure.
* Use the **keyboard macro** to mark up keyboard input.
* Use the **menu UI macro** to mark up menu navigation in a UI procedure.

For example:

```asciidoc
Click the btn:[Submit] button.

Press kbd:[esc] to exit insert mode.

You can cancel a running query by using the kbd:[Ctrl+C] keys.

In the tool bar, select menu:File[Save].

Select menu:View[Zoom > Reset] to reset the zoom level.
```

Renders as:

Click the **Submit** button.

Press esc to exit insert mode.

You can cancel a running query by using the Ctrl+C keys.

In the tool bar, select **File** **Save**.

Select **View** **Zoom** **Reset** to reset the zoom level.

For more information about when to use each type of markup, see:

* [Button Macro](../../styleguide/button-macro.md)
* [Keyboard Macro](../../styleguide/keyboard-macro.md)
* [Menu UI Macro](../../styleguide/menu-ui-macro.md)

### [](#links-and-urls)Links and URLs

Antora and AsciiDoc turn any URLs that begin with one of the common schemes (`http`, `https`, `ftp`, `irc`, `mailto`, or any email address) into links automatically.

Add the exact text of the link into your AsciiDoc file, ending with a set of square brackets (`[]`).

Enter the text you want to display as the link text inside the square brackets, or leave them empty to display the link as-is. Add a caret to the end of your link text `^` for any links that go to external websites.

This will open the page in a new tab, so readers do not actually leave the Couchbase Documentation.

For example:

https://www.couchbase.com/[The Couchbase Website^]

https://github.com/[]

mailto:someone@something.com[]

Renders as:

[The Couchbase Website](https://www.couchbase.com/)

<https://github.com/>

[someone@something.com](mailto:someone@something.com)

Avoid using the `` macro — you'll only need it in rare circumstances, such as for links with unusual schemes.

> [!WARNING]
> Do NOT use URLs or system paths to link between pages in the Couchbase Documentation. If the page is inside a Couchbase Docs repository on GitHub, you must use a [cross reference](cross-references.md) to link to it. Xrefs ensure domain, component, and version portability.

#### [](#url-best-practices)URL Best Practices

* Always use the secure `https://` scheme for external webpage links.
* [Escape](#escaping) `http://localhost` URLs in regular text so they do not become links.
* Create [attributes](attributes-and-roles.md) for long URLs to improve the source readability for other contributors.
* Create [attributes](attributes-and-roles.md) for URLs that contain sets of symbols, such as multiple underscores (`_`) and backticks (`` ` ``), that could be misinterpreted as inline markup.
* Create attributes for URLs used several times on the same page.
* Do not use URLs for linking between documentation pages or to in-page anchors. Use [cross references](cross-references.md), instead.

### [](#escaping)How To Escape Any Inline AsciiDoc Markup

When you need to display any kind of AsciiDoc markup as-is in your published page, such as a link that should be inactive, you can escape the markup by adding a single backslash (`\`) to the start of the markup.

For URLs, if you also need to add markup while marking the link inactive, use a plus sign (`+`) inside any inline style markup.

For example:

```asciidoc
If it is not specified, the default URL \http://localhost:8091 is used.

If it is not specified, the default URL `+http://localhost:8091+` is used.
```

Renders as:

If you do not specify a URL, the default URL http://localhost:8091 is used.

If you do not specify a URL, the default URL `http://localhost:8091` is used.

## [](#description-lists)Description Lists

Use description lists for writing out terms and definitions in your documentation, such as in a glossary.

Mark the term you want to highlight with a set of double colons (`::`) before writing the definition on the same line. If you need to add a second line of text on a new line in your definition, add a plus sign (`+`) to the empty line between the start of the term and definition, and the second line of content.

Block content like lists can be entered on a new line below the term and its double colons.

For example:

```asciidoc
Bucket:: The top-level data storage container for data in a Capella database.
A database can have multiple buckets, but must contain at least 1 bucket before it can store any data.
+
For more information about buckets, see Buckets, Scopes, and Collections.
These sentences appear as a new line for the definition of *Bucket*.

Scope:: A data storage container inside a Capella database.
Add scopes to a bucket to organize and group related collections in a Capella database.
+
NOTE: A bucket can only contain a maximum of 1000 scopes.
This admonition is part of the definition for *Scope*.

Collection::
* Collections exist inside scopes.
.. Create a new collection to store your documents.
.. This is the final list item.
```

Renders as:

Bucket

The top-level data storage container for data in a Capella database. A database can have multiple buckets, but must contain at least 1 bucket before it can store any data.

For more information about buckets, see Buckets, Scopes, and Collections. These sentences appear as a new line for the definition of **Bucket**.

Scope

A data storage container inside a Capella database. Add scopes to a bucket to organize and group related collections in a Capella database.

> [!NOTE]
> A bucket can only contain a maximum of 1000 scopes. This admonition is part of the definition for **Scope**.

Collection

* Collections exist inside scopes.

  1. Create a new collection to store your documents.
  2. This is the final list item.

For more information about description lists in AsciiDoc, see [Description Lists](https://docs.asciidoctor.org/asciidoc/latest/lists/description/) in the AsciiDoctor Docs.

## [](#ordered-lists)Ordered Lists

Use an ordered list when you have a procedure, task, or collection of items where the order matters.

Use a period (.) to render an item as an ordered list item. The number of periods sets the depth of the list item.

For more information about when to use ordered lists, see [Ordered Lists](../../styleguide/ordered-list.md).

For example:

```asciidoc
. Step 1, Level 1
.. Step 1, Level 2
... Step 1, Level 3
.... Step 1, Level 4
..... Step 1, Level 5
. Step 2
```

Renders as:

1. Step 1, Level 1

  1. Step 1, Level 2

    1. Step 1, Level 3

      1. Step 1, Level 4

        1. Step 1, Level 5
2. Step 2

## [](#unordered-lists)Unordered Lists

Use an unordered or bulleted list when you have a collection of three or more things and the order of the items does not matter. These items could be nouns, phrases, or topics.

Use an asterix (\*) to render an item as an unordered list item. The number of asterixes sets the depth of the list item.

For more information about when to use unordered lists, see [Unordered Lists](../../styleguide/unordered-list.md).

For example:

```asciidoc
* Level 1
** Level 2
*** Level 3
**** Level 4
***** Level 5
* Level 1
```

Renders as:

* Level 1

  * Level 2

    * Level 3

      * Level 4

        * Level 5
* Level 1

[Navigation files](update-nav.md) also use the unordered list syntax.

## [](#images)Images

The block image macro (`image::[]`) and the inline image macro (`image:[]`) accept SVG, PNG, JPG/JPEG, and GIF file formats.

Block images, indicated by two colons (`::`), are entered on their own line and displayed on their own line. Optional attributes and values are entered inside the macro's attribute list (`[]`). In the [block image example](#block), the first positional value is empty, so the opening square bracket (`[`) is directly followed by a comma (`,`). The second positional value, `280`, indicates the maximum width of the image. The next attribute, `align`, and its assigned value `left`, places the image against the left page margin.

If the macro's attribute list is empty (e.g., `image::filename.jpg[]`), the image is displayed at its original size and centered on the page.

Block image

```asciidoc
image::console-login.png[,280,align=left]
```

Renders as:

![console login](_images/console-login.png) 

The inline image macro, indicated by a single colon (`:`), is used for displaying small images and icons directly in the flow of a sentence.

For example:

```asciidoc
Click the image:edit.svg[,16] icon.
```

Renders as:

Click the ![edit](_images/edit.svg) icon.

## [](#admonitions)Admonitions

Couchbase Documentation uses 5 different admonition types:

* NOTE
* TIP
* IMPORTANT
* CAUTION
* WARNING

A basic admonition contains only a few lines of text.

For example:

```asciidoc
TIP: Positional parameters are set using the `-args` query parameter.

NOTE: Once a node has been successfully added, the Couchbase Server cluster indicates that a rebalance is required to complete the operation.

IMPORTANT: The node names passed to the `nodes` parameter must include the cluster administration port (by default 8091).
For example `WITH {"nodes": ["192.0.2.0:8091"]}` instead of `WITH {"nodes": ["192.0.2.0"]}`.

WARNING: Never stop or restart Couchbase Server before you first remove that node from a cluster.

CAUTION: Don't stick forks in power sockets.
```

Renders as:

> [!TIP]
> Positional parameters are set using the `-args` query parameter.

> [!NOTE]
> Once a node has been successfully added, the Couchbase Server cluster indicates that a rebalance is required to complete the operation.

> [!IMPORTANT]
> The node names passed to the `nodes` parameter must include the cluster administration port (by default 8091). For example `WITH {"nodes": ["192.0.2.0:8091"]}` instead of `WITH {"nodes": ["192.0.2.0"]}`.

> [!WARNING]
> Never stop or restart Couchbase Server before you first remove that node from a cluster.

> [!CAUTION]
> Don't stick forks in power sockets.

If you need to include compound or block content inside your admonition, use a compound admonition.

A compound admonition is any admonition block that contains more than one paragraph or contains a block other than a paragraph - such as a list or other block element. The contents of the compound admonition must be wrapped in the example block delimiter, which is 4 equals signs (`====`).

The admonition type must be assigned as the block style, using square brackets above the first set of delimiters (`[IMPORTANT]`).

For example:

```asciidoc
[IMPORTANT]
.Optional Title
====
Use an example block to create an admonition that contains compound content, such as:

* Lists
* Multiple paragraphs
* Source code
====
```

Renders as:

> [!IMPORTANT]
> Optional Title
> 
> Use an example block to create an admonition that contains compound content, such as:
> 
> * Lists
> * Multiple paragraphs
> * Source code

## [](#tables)Tables

Display content in a table to show the relationship between different pieces of information.

Start a table in your documentation with the delimiter `|====` (a vertical bar followed by 4 equals signs).

Set the number of columns in your table using vertical bars (`|`) or by adding a `cols` attribute in square brackets (`[]`) before the table delimiter.

Enter the name of each column after each vertical bar.

Start a new cell by adding additional vertical bars.

To make your documentation easier for maintainers to understand, try to enter each cell on a new line.

Cells are grouped into rows. Each row must share the same number of cells, taking into account any column or row spans.

For example, the following table has 2 columns with 2 rows:

Table with implicit column value and header row

```asciidoc
|====
|Name of Column 1 |Name of Column 2

|Cell in column 1, row 1
|Cell in column 2, row 1

|Cell in column 1, row 2
|Cell in column 2, row 2
|====
```

It renders as:

| Name of Column 1        | Name of Column 2        |
| ----------------------- | ----------------------- |
| Cell in column 1, row 1 | Cell in column 2, row 1 |
| Cell in column 1, row 2 | Cell in column 2, row 2 |

Since tables are AsciiDoc block elements, they can have titles, roles, [IDs](ids.md), and table-specific [attributes](attributes-and-roles.md).

For example, the following table:

* Sets an optional table title.
* Sets an optional ID value, for linking directly to this table from a [cross reference](cross-references.md).
* Sets the width of the third column to be twice the width of the first 2 columns by setting `cols="1,1,2"`.
* Sets the first row as the header row explicitly by setting `options="header"`.

Table with title, ID, `cols`, and `options="header"`

```asciidoc
.Optional title
[#optional-id,cols="1,1,2",options="header"]
|===

|Name of Column 1
|Name of Column 2
|Name of Column 3

|Cell in column 1, row 1
|Cell in column 2, row 1
|Cell in column 3, row 1

|Cell in column 1, row 2
|Cell in column 2, row 2
|Cell in column 3, row 2
|===
```

It renders as:

__Table 1\. Optional title__
| Name of Column 1        | Name of Column 2        | Name of Column 3        |
| ----------------------- | ----------------------- | ----------------------- |
| Cell in column 1, row 1 | Cell in column 2, row 1 | Cell in column 3, row 1 |
| Cell in column 1, row 2 | Cell in column 2, row 2 | Cell in column 3, row 2 |

Here's an example of a table with a title, implicit header row, and the proportional width of the two columns set.

```asciidoc
.CLI parameters for adding a node
[cols="1,2"]
|===
|Parameter |Description

|`--cluster`
|The IP address of a node in the existing cluster.

|`--user`
|The username for the existing cluster.

|`--password`
|The password for the existing cluster.
|===
```

Renders as:

__Table 2\. CLI parameters for adding a node__
| Parameter   | Description                                       |
| ----------- | ------------------------------------------------- |
| \--cluster  | The IP address of a node in the existing cluster. |
| \--user     | The username for the existing cluster.            |
| \--password | The password for the existing cluster.            |

### [](#block-elements-in-tables)Block Elements in Tables

You can add block-level elements, such as code blocks, lists, multiple paragraphs, and admonitions, to a table cell.

To add any block-level elements to a table cell, you must add an `a` before the vertical bar for that cell.

For example:

```asciidoc
.cbq Shell Commands
[#table-cbq-shell-commands,cols="1,2,4"]
|===
|Shell Command |Arguments |Description and Examples

|`\SET`
|`parameter=prefix:variable name`
a|
Sets the top most value of the stack for the given variable with the specified value.

Variables can be of the following types:

[#set-var-types]
* Query parameters
* Session variables
* User-defined
* Pre-defined and named parameters.

|`\PUSH`
|`parameter value`
a|
Pushes the specified value on to the given parameter stack.

----
cbq> \PUSH -args  [8];
----

.Resulting variable stack
----
cbq> \SET;
 Query Parameters :
 Parameter name : args
 Value : [[6,7] [8] [8]]
...
cbq>
----
|===
```

Renders as:

__Table 3\. cbq Shell Commands__
| Shell Command | Arguments                      | Description and Examples                                                                                                                                                                                         |
| ------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \\SET         | parameter=prefix:variable name | Sets the top most value of the stack for the given variable with the specified value. Variables can be of the following types: Query parameters Session variables User-defined Pre-defined and named parameters. |
| \\PUSH        | parameter value                | Pushes the specified value on to the given parameter stack. cbq> \\PUSH -args  \[8\]; Resulting variable stack cbq> \\SET;  Query Parameters :  Parameter name : args  Value : \[\[6,7\] \[8\] \[8\]\] ... cbq>  |

### [](#column-and-row-spans)Column and Row Spans

You can extend cells to span multiple rows or columns:

* To have a cell span multiple columns, before the vertical bar (`|`) for the cell:

  1. Add the number of columns the cell should span.
  2. Add a plus sign (`+`) operator after the number. For example, `2+|` would span 2 columns.
* To have a cell span multiple rows, before the vertical bar (`|`) for the cell:

  1. Add a period (`.`).
  2. Add the number of rows the cell should span.
  3. Add a plus sign (`+`) operator after the number. For example, `.3+|` would span 3 rows.

For example, the following table uses row and column spans:

```asciidoc
|===

|Cell in column 1, row 1 |Cell in column 2, row 1 |Cell in column 3, row 1

3+|Content in a single cell that spans columns 1, 2, and 3

|Cell in column 1, row 3
|Cell in column 2, row 3
|Cell in column 3, row 3

.2+|Content in a single cell that spans rows 4 and 5
|Cell in column 2, row 4
|Cell in column 3, row 4

|Cell in column 2, row 5
|Cell in column 3, row 5
|===
```

It renders as:

| Cell in column 1, row 1                                 | Cell in column 2, row 1 | Cell in column 3, row 1 |
| ------------------------------------------------------- | ----------------------- | ----------------------- |
| Content in a single cell that spans columns 1, 2, and 3 |                         |                         |
| Cell in column 1, row 3                                 | Cell in column 2, row 3 | Cell in column 3, row 3 |
| Content in a single cell that spans rows 4 and 5        | Cell in column 2, row 4 | Cell in column 3, row 4 |
| Cell in column 2, row 5                                 | Cell in column 3, row 5 |                         |

### [](#table-widths)Table Widths

By default, table width is set to 100%.

You can override the table width default by:

* Setting the width explicitly with a percentage value (`%`) and the width attribute.  
For example, `[width=50%]`.
* Setting the `autowidth` option, so that table only expands to accommodate the contents  
For example, `[%autowidth]`.
* Assigning a [role](attributes-and-roles.md) to the table to control the width with CSS.  
For example, `[.narrow]`.

For more information, see the [Asciidoctor table width documentation](https://asciidoctor.org/docs/user-manual/#table-width).

### [](#table-attributes-and-options)Table Attributes and Options

AsciiDoc has a lot of table attributes, options, and specifiers. For more examples and information, see the [Asciidoctor table documentation](https://asciidoctor.org/docs/user-manual/#tables).

## [](#learn-more)Learn More

* [Document-to-document cross references](cross-references.md)
* [Element IDs](ids.md)
* [Code blocks](code-blocks.md)
* [Tabs sets](tabs.md)
* [Example and partial file includes](includes.md)
* [Page roles](attributes-and-roles.md#page-roles)
* [Attributes](attributes-and-roles.md)

## [](#additional-resources)Additional Resources

You can find more AsciiDoc examples in the [Pages category of the Antora documentation](https://docs.antora.org/antora/2.0/page/).