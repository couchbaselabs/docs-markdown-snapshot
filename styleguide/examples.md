---
title: Code Examples
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/styleguide/modules/ROOT/pages/examples.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/styleguide/examples.html)

# Code Examples

Add code examples where possible to show users how to work with Couchbase products.

When adding a code example:

Do

* Make it relevant and applicable to your explanation.
* Make sure it’s a working code sample that the user could use in their own projects.
* Put the code example in its own separate file.
* Use the correct format for [Code Placeholders](placeholders.md).

Do Not

* Include cultural references.
* Write the code sample directly inside the .adoc file.

## [](#introducing-examples)Introducing Examples

Use the following guidelines for adding an example into your documentation:

* Do not use directional language to describe where in the text your example is, like `above` or `below`. Use `preceding,` `previous,` or `following.`
* Similar to [links](links.md), use `see.`
* Use a colon at the end of the phrase you use to introduce your example.

| Acceptable                                                                                                             | Not Acceptable                                     |
| ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| See the following example:                                                                                             | See the example below.                             |
| For an example of how to use a SELECT query, see the following: The following example shows how to use a SELECT query: | The example below shows how to use a SELECT query. |

## [](#adding-a-code-example)Adding a Code Example

Antora supports two different methods of inserting smaller blocks of code into a page:

* Add tags inside code comments to mark the code to include.
* Choose specific line numbers to include.

### [](#tags)Tags

To start a code sample, in the source code file, add `tag::<TAG_NAME>[]` in a code comment before the lines of code you want to include.

To end a code sample, in the source code file, add `end::<TAG_NAME>[]` in a code comment following the lines of code you want to include.

For example, the following code has two tags, `using` and `connect`:

```c#
using System;
// #tag::using[]
using System.Threading.Tasks;
using Couchbase;
// #end::using[]

namespace examples
{
    class StartUsing
    {
        static async Task Main(string[] args)
        {

            // #tag::connect[]
             var cluster = await Cluster.ConnectAsync("couchbase://localhost", "username", "password");
            // #end::connect[]

        ...
        }
    }
}
```

### [](#line-numbers)Line Numbers

To include a specific set of lines of code in your code, use the `lines` attribute inside your include directive.

For example, the following code would include lines 1-3 of the code file `select-true-alias-get-business-days.n1ql`:

include::example$javascript-udfs/select-true-alias-get-business-days.n1ql[lines=1..3]

For more information about how to include specific lines of content, see [Include Content by Line Ranges](https://docs.asciidoctor.org/asciidoc/latest/directives/include-lines/) in the Asciidoctor Documentation.

## [](#explaining-code-examples)Explaining Code Examples

Avoid the [built-in code callouts](#home:contribute:code-blocks.adoc#callouts) in Antora, where possible.

Use small code examples with the explanation in regular text around the example. Add one-line code comments directly to the code where appropriate to explain the assumptions made in a code example.

Let the user know they should remove the comments to use the code in a production environment.

When you need to explain a larger code example:

1. Show the full example and provide a brief explanation.
2. Create a smaller code example out of the larger block of code.
3. Provide a more detailed explanation for the smaller code example.
4. Repeat Steps 2 and 3 until you’ve explained the code.