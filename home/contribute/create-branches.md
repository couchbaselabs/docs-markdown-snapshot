---
title: Create a New Working Branch
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/create-branches.adoc
  xref: xref:home:contribute:create-branches.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/create-branches.html)

# Create a New Working Branch

Before you start making any changes to the files in a [Couchbase Documentation repository](repositories.md), you must create a new branch for your work.

For a quick overview on some terminology and concepts related to GitHub repositories, see [About repositories in the GitHub Documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories).

You can create branches from:

* The command line
* [VS Code](install-git-and-editor.md#install-vs-code)
* [GitHub Desktop](install-git-and-editor.md#install-github-desktop)

First, make sure you choose the right base branch for your work.

## [](#base-branch)Choose the Right Base Branch

The branch you choose as your base branch sets the source of truth for your new documentation.

Every Couchbase Documentation repository has 1 or more configured base branches that we use to build the documentation. Usually, you should choose one of these configured base branches as your base branch for your working branch.

For example, the Couchbase Capella documentation has a single base branch, `main`. Some other documentation repositories still use `master` as their base branch. Couchbase Server, Couchbase Mobile, and the Couchbase SDKs use `release/x.x` branches to organize the documentation according to the product version it describes.

The single base branch or `release/x.x` branches for the latest few releases of a product are the only branches that get built into the main Couchbase Documentation site.

We use working branches to keep changes separate and easier to reconcile, especially with multiple people working on the same files. Working branches should try to aim to solve a single issue at a time.

Typically, you should:

* Choose the `main`, `master`, or appropriate `release/x.x` branch for your changes.  
For example, if an issue or a fix only relates to the 7.0 version of a product, then you should base your working branch on `release/7.0`.
* Name your working branch based on the ticket number for the issue.
* Create a pull request (PR) for your working branch that targets your original base branch.

If you're ever unsure about the correct branch to use for an issue:

* Look for the **Affects versions** field on your assigned ticket
* Ask another member of the Documentation team
* Check that the repository [does not require special handling](repositories.md#repo-special)

## [](#work-branch-vs-code)Create a Working Branch in VS Code

Before you can create a new working branch in VS Code, make sure you have:

* [Created a GitHub account](install-git-and-editor.md#gh-account)
* [Installed Git](install-git-and-editor.md#install-git)
* [Installed VS Code](install-git-and-editor.md#install-vs-code)
* [Set up the correct Documentation repository](set-up-repository.md)

To create a new working branch in VS Code:

1. Start VS Code.
2. On the **Welcome** tab, click **Open Folder**.
3. Select the folder on your computer where you [cloned the Documentation repository](set-up-repository.md).
4. Click **Select Folder**.
5. Click ![The Source Control icon from the VS Code editor. It shows a forked line.](_images/source-control.png) **Source Control**.  
VS Code might prompt you that the repository has been marked as unsafe:  
![The Source Control panel, which displays a warning that the detected Git repository is unsafe.](_images/unsafe-repo-1.png)
6. Click **Manage Unsafe Repositories** and select the repository to continue:  
![The Command Palette in VS code, which lets the user select the repository they want to mark as safe.](_images/unsafe-repo-2.png)
7. Point to the **Source Control** label and click **…​** (**More Actions…​**):  
![The Source Control panel in VS Code. The user has pointed to the top of the panel and brought up the additional context menu, and the More Actions button is highlighted.](_images/more-actions.png)
8. Click **Checkout to…​**.
9. [Choose the correct base branch for your new working branch](#base-branch).  
You can select it from the list of branches or type to search for the correct branch. If this is the first time you're choosing your base branch, the branch name must be prefixed with `origin/`.
10. To get the latest copy of any changes on your base branch, click **Sync Changes**.
11. Point to the **Source Control** label again and click **…​** (**More Actions…​**).
12. Go to **Branch** **Create Branch…​**.
13. Enter a name for your new working branch.  
Start with the name of your ticket, if you have one. Provide a few words, separated by dashes (`-`) to describe the changes on the branch. Try to stick to 3-5 words.
14. Press Enter.
15. Click **Publish Branch**.

Now you can [add or edit new pages in your new branch](#next-steps).

## [](#work-branch-cli)Create a Working Branch from the Command Line

Before you can create a new working branch using the command line, make sure you have:

* [Created a GitHub account](install-git-and-editor.md#gh-account)
* [Installed Git](install-git-and-editor.md#install-git)
* [Set up the correct Documentation repository](set-up-repository.md)

To create a new working branch from the command line:

1. Open your terminal.
2. Navigate into the directory on your computer that contains the Documentation repository you want to work with:  
```console  
$ cd <path/to/repository>  
```
3. [Choose the correct base branch for your new working branch](#base-branch). After you know the correct branch name, enter the following command to check out the branch:  
```console  
$ git checkout <name-of-base-branch>  
```
4. Run a pull to make sure you have downloaded the latest changes from the branch:  
```console  
$ git pull upstream <name-of-base-branch>  
```
5. Use the same checkout command with the `-b` flag to create a new branch from the base branch and check it out:  
```console  
$ git checkout -b <name-of-new-working-branch>  
```  
Start your branch name with the name of your ticket, if you have one. Provide a few words, separated by dashes (`-`) to describe the changes on the branch. Try to stick to 3-5 words.

Now you can [add or edit new pages in your new branch](#next-steps).

## [](#next-steps)Next Steps

* [Edit existing documentation using VS Code](edit-pages.md).
* [Add new documentation pages](add-pages.md).