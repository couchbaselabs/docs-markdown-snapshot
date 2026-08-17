---
title: Add a New Documentation Page
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/add-pages.adoc
  xref: xref:home:contribute:add-pages.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/add-pages.html)

# Add a New Documentation Page

To add a new page to the Couchbase documentation, you need to create a new AsciiDoc file.

## [](#create-a-new-asciidoc-file)Create a New AsciiDoc File

1. Open the documentation repository that you want to work in with VS Code.  
> [!TIP]  
> If you enabled the **Open with Code** shortcut when you [installed VS Code](#install-git-and-editor), you can right-click inside your file explorer window from a repository to quickly open it in VS Code.
2. In the VS Code **Explorer** panel, navigate to the **pages** folder where you want to add a new page.  
The folder structure for a documentation repository could look like the following:

- <component-name>
    -- modules
        --- <module-name>
            ---- assets
            ---- examples
            ---- pages
            ---- partials  
Specifically, the folder structure for this component, the `home` component of the Couchbase docs, looks like:

- home
    -- modules
        --- contribute
            ---- assets
            ---- examples
            ---- pages
            ---- partials
        --- ROOT
            ---- assets
            ---- pages
            ---- partials
3. Right-click the **pages** folder and click **New File**.
4. Enter a name for your new AsciiDoc file. This filename will appear in the page's URL when it's published to our documentation site.  
Make sure your filename:

  * Uses lowercase letters (a-z).
  * Separates words with hyphens (`-`).
  * Does not use symbols or special characters, such as `!`, `@`, `#`, or others.
5. End the filename with the AsciiDoc file extension, `.adoc`, and press Enter.  
VS Code automatically opens the new file.
6. On the first line of the new file, enter a [document title](pages.md#doc-title), starting with an `=`.
7. Write your documentation using proper AsciiDoc syntax. For more information about AsciiDoc syntax, see [AsciiDoc Basics](basics.md) or [the AsciiDoc Language documentation](https://docs.asciidoctor.org/asciidoc/latest/).
8. Save the file, or take advantage of VS Code's autosave feature (**File** **Auto Save**).

Any AsciiDoc file saved to a **pages** directory in an Antora documentation component is automatically published to the site.

## [](#next-steps)Next Steps

* [Add a page to a component navigation menu](update-nav.md).
* [Build the docs site locally to test and preview your changes](test-site.md).