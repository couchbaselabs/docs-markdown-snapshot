---
title: Edit Existing Documentation
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/edit-pages.adoc
  xref: xref:home:contribute:edit-pages.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/edit-pages.html)

# Edit Existing Documentation

Use the following as a reference for how to edit documentation using VS Code. You can choose to write AsciiDoc in a plain text editor, or whichever integrated development environment (IDE) you prefer.

The Documentation team recommends VS Code due to the extensions available, such as Vale, for running automated checks on your documentation.

> [!TIP]
> See the [VS Code documentation](https://code.visualstudio.com/docs/getstarted/userinterface) for an overview of the user interface, and to get more familiar with how to work in VS Code.

## [](#general-editing-steps-using-vs-code)General Editing Steps Using VS Code

In general, to edit an existing page of the documentation in VS Code:

1. Start VS Code.
2. On the **Welcome** tab, click **Open Folder**.
3. Select the folder on your computer where you [cloned the documentation repository](set-up-repository.md).
4. Click **Select Folder**.  
> [!TIP]  
> If you enabled the **Open with Code** context menu action when you installed VS Code, you can quickly open a repository from your file explorer instead of following these steps. Open the folder in the file explorer, and from the top level of the repository's directory, right-click and click **Open with Code**.
5. [Create a new working branch](create-branches.md) for your documentation changes.
6. Click ![The Explorer icon from the VS Code editor. It shows 2 overlapping pieces of paper.](_images/explorer.png) **Explorer**.
7. In the Explorer pane, locate the file for the page, partial, or example you want to edit.
8. Double-click the file to open it in an editor pane.
9. Make edits to the content.  
For AsciiDoc help, see [AsciiDoc Basics](basics.md). For style conventions, see [styleguide:index.adoc](#styleguide:index.adoc).
10. Do one of the following:

  1. Press CTRL+S to save the file.
  2. Go to **File** **Auto Save** to toggle auto-save for your editor.

To check your edits, [configure and build a local test site](test-site.md).

## [](#use-find-and-replace)Use Find and Replace

To speed up making edits to multiple instances of a word, attribute, link, or other text in a file, use VS Code's **Find and Replace** feature.

To use Find and Replace:

1. Click ![The Search icon from the VS Code editor. It shows a magnifying glass.](_images/search.png) **Search**.
2. In the **Search** field, enter the term you want to find and press Enter to search.
3. Click the caret (`>`) next to the text field to show the **Replace** field.
4. Enter the term you want to use to replace your search term.  
> [!TIP]  
> If your search term appears in different casing that you want to preserve through your search results, you can click **AB (Preserve Case)** on the **Replace** field to keep the original casing in your replacement.
5. Do one of the following:

  1. To replace every instance in your search results, next to the **Replace** field, click **Replace All**.
  2. To replace every instance in a specific file in your search results, point to a filename in your results, and next to the file path, click **Replace All** when it appears.
  3. To replace individual instances in your search results, point to a result, and click **Replace** when it appears.

VS Code's Find and Replace supports case and whole word matching, as well as regular expressions.

You can also click **…​ (Toggle Search Details)** to add or remove directories or individual files from your search results.

## [](#next-steps)Next Steps

1. [Create a local playbook and build the site using your changes](test-site.md).
2. [Stage and commit your changes](send-pr.md).