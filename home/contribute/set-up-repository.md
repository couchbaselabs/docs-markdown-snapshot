---
title: Set Up Documentation Repositories
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/set-up-repository.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:home:contribute:set-up-repository.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/set-up-repository.html)

# Set Up Documentation Repositories

To contribute to the Couchbase Documentation, you need to get the repository that contains the documentation files onto your computer. For a quick overview on some terminology and concepts related to GitHub repositories, see [About repositories in the GitHub Documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories).

You only need to do these steps the first time you contribute to a repository.

## [](#find-the-correct-repository)Find the Correct Repository

To start, you need to know which Couchbase Documentation repository contains the files you need to edit.

> [!TIP]
> You can quickly find the correct repository for a page by using the ![edit](_images/edit.svg) **Edit on GitHub** button at the top of a page on the Couchbase Docs site.

Couchbase Documentation repositories are usually prefixed with `docs-`.

## [](#clone)Clone the Repository

> [!NOTE]
> Contributors from outside Couchbase need to [fork documentation repositories](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) to contribute changes. If you're a Couchbase employee, DO NOT fork repositories to contribute to Couchbase Documentation.

After you have found the repository that you want to work in, you need to clone it onto your computer:

1. On the GitHub page for the repository, click **Code**.
2. In the **Local** tab, do one of the following:

  1. To copy a command to use in your terminal, click **HTTPS** and then the **Copy** icon. Continue to [Clone with the Command Line](#clone-with-the-command-line)
  2. To clone the repository using [GitHub Desktop](install-git-and-editor.md#install-github-desktop), click **Open with GitHub Desktop**. Continue to [Clone with GitHub Desktop](#clone-with-github-desktop).
  3. To clone the repository using VS Code, see [Clone with VS Code](#clone-with-vs-code).

### [](#clone-with-the-command-line)Clone with the Command Line

To continue cloning the repository with the command line:

1. Do one of the following:

  1. Create a new folder on your computer where you want to store the files for the new repository. Consider giving the folder the same name as the repository.
  2. Select an existing folder where you want to store the files for the new repository.
2. Open a new terminal window.
3. In your terminal, enter the following command, replacing `<path/to/folder>` with the path to your folder from Step 1, and press Enter:  
$ cd <path/to/folder>
4. Type `git clone`, paste the URL you copied from GitHub, and press Enter. The command should look similar to the following:  
git clone https://github.com/couchbaselabs/docs-devex.git

Wait for the clone process to finish downloading the main branch of the repository onto your computer.

### [](#clone-with-github-desktop)Clone with GitHub Desktop

To continue cloning the repository with GitHub Desktop, follow the instructions in the [GitHub Desktop documentation](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop).

Wait for the clone process to finish downloading the main branch of the repository onto your computer.

### [](#clone-with-vs-code)Clone with VS Code

To clone a repository using VS Code, follow the instructions in the [VS Code documentation](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#%5Fopen-a-git-repository).

## [](#next-steps)Next Steps

1. [Get an overview of the entire contributing workflow](workflow-overview.md).
2. [Choose a base branch](create-branches.md#base-branch).
3. [Create a working branch in VS Code](create-branches.md#work-branch-vs-code) or [from the command line](create-branches.md#work-branch-cli).