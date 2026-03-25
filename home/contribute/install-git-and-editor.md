---
title: Install Git and an AsciiDoc Editor
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/install-git-and-editor.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:home:contribute:install-git-and-editor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/install-git-and-editor.html)

# Install Git and an AsciiDoc Editor

To get started with authoring Couchbase documentation, you need to:

1. [Create a GitHub Account](#gh-account)
2. [Download and Install Git](#install-git)
3. [Install an AsciiDoc Editor](#install-editor)

## [](#gh-account)Create a GitHub Account

The Couchbase documentation is stored on GitHub, so if you do not have a GitHub account, you need to [create one](https://github.com/join).

If you’re an official member of the Documentation team, other team members should help add your GitHub to the correct organizations, groups, and repositories on GitHub. Couchbase does not provide you with a GitHub account.

## [](#install-git)Download and Install Git

To clone and work with Git repositories on your device, or what’s known as local repositories, install Git using your operating system’s package manager. Alternatively, you can download it from the [Git project](https://git-scm.com/downloads).

### [](#install-github-desktop)Install GitHub Desktop

If you’re more comfortable working with a visual interface for interacting with Git, instead of using the command line and a terminal, consider installing [GitHub Desktop](https://desktop.github.com/).

GitHub Desktop makes it easier to interact with Git and provides a fast way to [clone new repositories](set-up-repository.md#clone-the-repository) onto your computer.

You can also just use [VS Code](#install-vs-code) and its integrated interface for Git.

## [](#install-editor)Install an AsciiDoc Editor

> [!NOTE]
> The current recommendation is to install VS Code.

AsciiDoc is the markup language Couchbase uses for writing documentation. You can write an AsciiDoc document using a plain text editor or integrated development environment (IDE). If you do not have a preferred text editor or IDE, install VS Code and the listed AsciiDoc packages for an enhanced experience.

### [](#install-vs-code)Download and Install VS Code

Visual Studio Code is a free, open-source code editor that runs on all platforms.

1. Go to the [VS Code home page](https://code.visualstudio.com/). The VS Code home page should detect your operating system automatically and provide the correct download options.
2. Download and install VS Code. Use the links below for additional installation instructions.

  * [VS Code for Linux](https://code.visualstudio.com/docs/setup/linux)
  * [VS Code for macOS](https://code.visualstudio.com/docs/setup/mac)
  * [VS Code for Windows](https://code.visualstudio.com/docs/setup/windows)

### [](#adoc-packages)Install the AsciiDoc Packages

After you have installed VS Code:

1. Start VS Code and go click **Extensions** beside the file explorer panel, or press Ctrl+Shift+X.
2. In the **Search extensions in Marketplace** field, search for and install the following packages:  
AsciiDoc  
The `AsciiDoc` package by `asciidoctor` provides some nice-to-have features for editing AsciiDoc files in VS Code.  
Vale VSCode  
The `Vale VSCode` package by `Chris Chinchilla` powers in-editor text linting, including a spellchecker, that the Documentation team uses on all documentation files.  
You could also consider installing:  
GitHub Pull Requests  
This official GitHub extension lets you create GitHub pull requests directly inside VS Code. You will need to create pull requests for any changes you want to add to the documentation.

## [](#next-step)Next Step

[Install Antora](install-antora.md).