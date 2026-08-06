---
title: Setting Up Couchbase Python SDK with pyenv
description: Discover how to get up and running developing applications with the
  Couchbase Python SDK 4.0+ using a virtual python installation
editUrl: https://github.com/couchbase/docs-sdk-python/edit/release/4.6/modules/hello-world/pages/platform-help.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:python-sdk:hello-world:platform-help.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/hello-world/platform-help.html)

# Setting Up Couchbase Python SDK with pyenv

> Discover how to get up and running developing applications with the Couchbase Python SDK 4.0+ using a virtual python installation 

A simple Python orientation intro for \_non-\_Python folk who are evaluating the Couchbase Python SDK.

> [!IMPORTANT]
> Is This Page for You?
> 
> This page is to help evaluate the Couchbase Python SDK, if Python is not where you spend the majority of your working day. It is aimed at Software Architects, QE folk, managers, and anyone else who needs to run through using the Python SDK without necessarily being comfortable with installing and developing with Python. If this is not you, head back to the [rest of the Couchbase Python SDK documentation](overview.md).

## [](#installing)Installing

First thing is to get up and running with a virtual Python environment, to avoid any problems with needing to run programs on a different version of Python from the one your systems utilities depend upon. If you have a relatively recent version of GNU/Linux or macOS, then you can skip this step and just work with your operating system's Python 3 environment. If you are running Windows, skip to the Windows section. But if you are developing for an older platform — such as an old Red Hat installation — then read on.

You most likely already have python installed on your development machine. You can verify this with:

```console
$ python3 --version
```

Note that with some operating systems the `3` will not be necessary, but `python3` will work on all systems where it is installed.

You should see output like this:

```console
Python 3.12.3
```

### [](#installing-on-gnulinux)Installing on GNU/Linux

Now follow along the steps on the [installation page](../project-docs/sdk-full-installation.md#installation).