---
title: Tabbed Content
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/tabs.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:home:contribute:tabs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/tabs.html)

# Tabbed Content

> [!TIP]
> For guidance around when to use tabbed content in your docs, see [styleguide:ROOT:tabs-set.adoc](#styleguide:ROOT:tabs-set.adoc).

To add tabbed content to your docs page:

1. Add the `:tabs:` attribute to the front matter of your `.adoc` file:  
```asciidoc  
= Document Title  
:page-topic-type: guide  
:description: This is a description of the document.  
:page-toclevels: 3  
:tabs:  
:keywords: cmek, encryption, security, backups  
```
2. If you’re going to add multiple tabs with the same options on your page, make sure to also add `:tabs-sync-option:`:  
```asciidoc  
= Document Title  
:page-topic-type: guide  
:description: This is a description of the document.  
:page-toclevels: 3  
:tabs:  
:tabs-sync-option:  
:keywords: cmek, encryption, security, backups  
```  
> [!NOTE]  
> Tabs will not sync across your page if tab names are not an exact match. Make sure to use the same name for each tab for `tabs-sync-option` to work as expected and sync a user’s tab selection across the page.
3. In your `.adoc` file, start the tabbed content by adding `[tabs]` to a content block:  
```asciidoc  
[{tabs}]  
====  
====  
```
4. Define the title of your first tab by marking it with 2 colons, inside the `tabs` content block:  
```asciidoc  
[{tabs}]  
====  
My First Tab::  
====  
```
5. Write the content for your first tab. Make sure that any new lines or block content are connected together using a `+` inside your tab:  
```asciidoc  
[{tabs}]  
====  
My First Tab::
+  
This is the content for my first tab.  
I need it to display together.
+  
I want to add a code block:
+  
// In these examples, code blocks are marked with 3 (---) dashes to make them render correctly in the example block.  
// Use 4 (----) dashes in your own code blocks.  
[source,txt]
---  
Yay a code block!
---
+  
[NOTE]
--  
This is a note.  
We need to use a different delimiter.
--  
====  
```  
You can also enclose the entire contents of your tab inside a delimited open block (`--`) to reduce the number of `+` you need to add:  
```asciidoc  
[{tabs}]  
====  
My First Tab::
+
--  
This is the content for my first tab.  
I need it to display together.  
I want to add a code block:  
// In these examples, code blocks are marked with 3 (---) dashes to make them render correctly in the example block.  
// Use 4 (----) dashes in your own code blocks.  
[source,txt]
---  
Yay a code block!
---
+  
[NOTE]
---  
This is a note.  
We need to use a different delimiter.
---
--  
====  
```
6. Repeat for any additional tabs:  
```asciidoc  
[{tabs}]  
====  
My First Tab::
+  
This is the content for my first tab.  
I need it to display together.
+  
I want to add a code block:
+  
// In these examples, code blocks are marked with 3 (---) dashes to make them render correctly in the example block.  
// Use 4 (----) dashes in your own code blocks.  
[source,txt]
---  
Yay a code block!
---
+  
[NOTE]
--  
This is a note.  
We need to use a different delimiter.
--  
// Make sure to leave a blank line between the end of the first tab's content and your next tab title.  
My Second Tab::
+
--  
This is the second tab, even better than the first.  
Woohoo tabs!
--  
====  
```

Your tabs should render like this:

* My First Tab
* My Second Tab

This is the content for my first tab. I need it to display together.

I want to add a code block:

```txt
Yay a code block!
```

> [!NOTE]
> This is a note.
> 
> We need to use a different delimiter.

This is the second tab, even better than the first.

Woohoo tabs!

See a tabs set in action on the [Sync Gateway Getting Started page](../../sync-gateway/current/start-here/get-started-prepare.md#installation).