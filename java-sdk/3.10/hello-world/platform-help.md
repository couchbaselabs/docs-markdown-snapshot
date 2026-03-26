---
title: Platform Introduction
description: A simple Java orientation intro for <em>non-Java</em> folk who are
  evaluating the Couchbase Scala SDK.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.10/modules/hello-world/pages/platform-help.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.10@java-sdk:hello-world:platform-help.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.10/hello-world/platform-help.html)

# Platform Introduction

> A simple Java orientation intro for _non-Java_ folk who are evaluating the Couchbase Scala SDK. 

> [!IMPORTANT]
> Is This Page for You?
> 
> This page is to help evaluate the Couchbase Java SDK, if Java is not where you spend the majority of your working day. It is aimed at Software Architects, QE folk, managers, and anyone else who needs to run through using the Java SDK without necessarily being comfortable with the Java environment. If this is not you, head back to the [rest of the Couchbase Java SDK documentation](overview.md).

## [](#jvm-installation)JVM Installation

Java is a JVM language - like Scala, Kotlin, and Clojure, it runs on a Java Virtual Machine. Running JVM programs necessitates a Java Runtime Environment (JRE), but to develop a Scala (say) or Java app you need a Java Development Kit (JDK). The Couchbase Java SDK can run on any LTS (long-term support) JDK — see the [compatibility page](../project-docs/compatibility.md) for full information.

To install the JDK we are going to use a JVM-management tool called `sdkman`.

### [](#sdkman)SDKMAN!

SDKMAN! — the Software Development Kit Manager — enables multiple Java versions and runtimes to be installed and managed, without intefering with your system's default JVM.

This third party tool is unnecessary in most production environments, but ideal for development machines. Installation instructions can be found on the [SDKMAN! website](https://sdkman.io/install).

Once SDKMAN! is installed, use it to install the latest version of Java:

```console
$ sdk install java 23.0.2-oracle
```

You may be prompted to set that version as a default — say yes (by pressing **<Enter>**). More details of SDKMAN! use can be found on the [SDKMAN! website](https://sdkman.io/install).