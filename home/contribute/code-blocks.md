---
title: Code Blocks for Example Code
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/code-blocks.adoc
  xref: xref:home:contribute:code-blocks.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/code-blocks.html)

# Code Blocks for Example Code

Use code blocks inside a documentation page to add example code.

Code samples should be stored in the `examples` directory for a module and added to documentation pages with the [include:: directive](#include-code). Some SDK examples have been added to the special `devguide` module inside each SDK docs repository. Using the `examples` directory and keeping code separate from AsciiDoc pages helps with our goal of automated code sample testing and maintenance.

Do not insert example code without testing that your code works.

## [](#code-example-formatting)Code Example Formatting

Add a source code example by adding a source block to an AsciiDoc page.

Source blocks display content exactly as entered, preserving indents and line breaks.

Add the attribute `[source,<language>]` to a source block to add code syntax highlighting in the published documentation.

For example, the following AsciiDoc:

.Optional title
[source,java]
----
KStreamBuilder builder = new KStreamBuilder();

KStream<String, GenericRecord> source = builder
        .stream("streaming-topic-beer-sample");
----

Renders as:

Optional title

```java
KStreamBuilder builder = new KStreamBuilder();

KStream<String, GenericRecord> source = builder
        .stream("streaming-topic-beer-sample");
```

If you need to add any commands to documentation that are run in the command line, use `[source,console]` and add a `$` to the start of each command.

For example, the following AsciiDoc:

[source,console]
----
$ curl GET -u admin:password http://ip.for.destination.cluster:8091/pools/default/buckets
----

Renders as:

```console
$ curl GET -u admin:password http://ip.for.destination.cluster:8091/pools/default/buckets
```

> [!TIP]
> Make sure to use `[source,console]` together with the `$` before each command. `[source,console]` makes sure that the user does not copy the `$` character when they copy from a code block.

## [](#callouts)Callout Numbers

> [!WARNING]
> Do not use the built-in callout numbers to add annotations and explanations to your example code. For more information about alternatives, see [Explaining Code Examples](#styleguide:examples.adoc#explaining-code-examples) in the style guide. The following section has been left for reference on the mechanics of code callouts, for when you encounter them in documentation.

Callouts add annotations to lines in code blocks. The first callout number must be placed after the final character on a code line. The responding callout is listed below the block and followed by the annotation text. Multiple callout numbers can be used on a single line.

[source,javascript]
----
function OnUpdate(doc, meta) {
  var strong = 70;
  var stmt =
    SELECT *                  // <1>
    FROM `beer-samples`       // <2>
    WHERE abv > $strong;
  for (var beer of stmt) {    // <3>
    break;                    // <4>
  }
}
----
<1> N1QL queries are embedded directly.
<2> Token escaping is standard N1QL style.
<3> Stream results using 'for' iterator.
<4> Cancel streaming query by breaking out.

Will render as:

```javascript
function OnUpdate(doc, meta) {
  var strong = 70;
  var stmt =
    SELECT *                  (1)
    FROM `beer-samples`       (2)
    WHERE abv > $strong;
  for (var beer of stmt) {    (3)
    break;                    (4)
  }
}
```

| **1** | N1QL queries are embedded directly.     |
| ----- | --------------------------------------- |
| **2** | Token escaping is standard N1QL style.  |
| **3** | Stream results using 'for' iterator.    |
| **4** | Cancel streaming query by breaking out. |

> [!TIP]
> To make callouts copy-and-paste friendly, put them behind the line comment syntax of the code snippet's language. For example, callouts in a YAML example are placed behind the hash symbol (`#`).

The callout list does not have to follow immediately after the code block containing the callouts. For example, you can include an introductory sentence or paragraph between the code block and the callout list.

Instead of marking up each callout with its own number, such as `<1>`, `<2>`, `<3>`, you can use `<.>` for each callout. When you use this method, the callouts are numbered automatically.

## [](#include-code)Inserting Examples with the Include Directive

Use the `include::` directive to insert a sample code file or tagged region from the `examples` directory into a file in the `pages` directory of a module. Using the `include::` directive also adds the **View on GitHub** button to the code sample, so readers can view the source file directly.

You need to know the resource ID of the example file to include it inside a page.

For example, the following inserts the `contact.json` file into a file in the `pages` directory from the `examples` directory in the same module:

.Query result
[source,json]
----
include::example$contact.json[]
----

### [](#insert-part-of-an-example)Insert Part of an Example

If you only want to insert part of an example code file, add tags around the part of the sample you want to include, using the comment character from your source language - such as `//` or `#`.

Start a tagged region with `tag::<tag-name>`. End a tagged region with `end::<tag-name>`.

For example, the following Ruby code adds a `read-only` tag:

# tag::read-only[]
options = Cluster::QueryOptions.new
options.readonly = true
cluster.query(
    'SELECT COUNT(*) AS airport_count FROM `travel-sample` WHERE type = "airport"',
    options)
# end::read-only[]

Then, in the square brackets (`[]`) at the end of the `include::` directive, add the tag name:

.Read-only Query
[source,json]
----
include::example$query.rb[tag=read-only]
----

## [](#learn-more)Learn More

* [Assign an ID to a code block](ids.md#code-block-id).
* [Create a tabs set](tabs.md).
* [Include examples](includes.md).
* [Tag regions of an example file](includes.md#tag-region).

## [](#additional-resources)Additional Resources

The Antora and Asciidoctor documentation provide more information about including code examples.

* [Antora resource ID structure](https://docs.antora.org/antora/latest//page/resource-id/)
* [Insert code snippets and files with the include directive](https://docs.antora.org/antora/latest//asciidoc/include-example/)
* [Select code regions with the tag macro](https://asciidoctor.org/docs/user-manual/#by-tagged-regions)
* [Normalize block indentation with the indent attribute](https://asciidoctor.org/docs/user-manual/#normalize-block-indentation)