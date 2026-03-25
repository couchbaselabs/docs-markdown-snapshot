---
title: Install Antora
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/install-antora.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:home:contribute:install-antora.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/install-antora.html)

# Install Antora

## [](#install-system-prerequisites)Install System Prerequisites

Antora runs on all Linux distributions, macOS, and Windows. If you have never used Antora, you may first need to install Node using nvm. Follow the installation instructions for all Antora prerequisites for your operating system:

* [Linux: Install Node](https://docs.antora.org/antora/latest/install/linux-requirements/)
* [macOS: Install Node](https://docs.antora.org/antora/latest/install/macos-requirements/)
* [Windows: Install Node](https://docs.antora.org/antora/latest/install/windows-requirements/)

## [](#install-the-antora-cli-and-site-generator)Install the Antora CLI and Site Generator

To generate the Couchbase documentation, you need the Antora command line interface (CLI) and the Antora site generator.

To install the CLI and the site generator:

1. Open a terminal window.
2. Copy and paste the following command and press Enter:  
```console  
npm i -g @antora/cli@3.1 @antora/site-generator@3.1  
```  
This installs the Antora CLI and site generator globally on your computer.
3. Copy and paste the following command and press Enter:  
```console  
 $ antora -v  
```  
This checks that Antora is available on your PATH. If installation was successful, you should see the Antora version number displayed in your terminal window.

## [](#next-step)Next Step

[Get the Couchbase documentation site playbook](playbook.md).