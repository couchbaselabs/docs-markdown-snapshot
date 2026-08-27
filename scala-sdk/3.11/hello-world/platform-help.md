---
title: Platform Introduction
description: A simple Scala orientation intro for <em>non-Scala</em> folk who
  are evaluating the Couchbase Scala SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.11/modules/hello-world/pages/platform-help.adoc
  xref: xref:3.11@scala-sdk:hello-world:platform-help.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.11/hello-world/platform-help.html)

# Platform Introduction

> A simple Scala orientation intro for _non-Scala_ folk who are evaluating the Couchbase Scala SDK. 

> [!IMPORTANT]
> Is This Page for You?
> 
> This page is to help evaluate the Couchbase Scala SDK, if Scala is not where you spend the majority of your working day. It is aimed at Software Architects, QE folk, managers, and anyone else who needs to run through using the Scala SDK without necessarily being comfortable with the Scala environment. If this is not you, head back to the [rest of the Couchbase Scala SDK documentation](overview.md).

It may be that you are a Java developer trying out our Scala SDK, or someone else who has a JDK installed, in which case feel free to skip ahead a section, but note that we will be installing `sdkman` in the next section, and using that to manage Scala installation.

## [](#jvm-installation)JVM Installation

Scala is a JVM language - like Java, Kotlin, and Clojure, it runs on a Java Virtual Machine. Running JVM programs necessitates a Java Runtime Environment (JRE), but to develop a Scala or Java app you need a Java Development Kit (JDK). The Scala SDK can run on any LTS (long-term support) JDK — see the [compatibility page](../project-docs/compatibility.md) for full information.

To install the JDK we are going to use a JVM-management tool called `sdkman`.

### [](#sdkman)SDKMAN!

SDKMAN! — the Software Development Kit Manager — enables multiple Java versions and runtimes to be installed and managed, without intefering with your system's default JVM.

This third party tool is unnecessary in most production environments, but ideal for development machines. Installation instructions can be found on the [SDKMAN! website](https://sdkman.io/install).

Once SDKMAN! is installed, use it to install the latest version of Scala 2.13:

```console
$ sdk install scala 2.13.15
```

You may be prompted to set that version as a default — say yes (by pressing **<Enter>**). More details of SDKMAN! use can be found on the [SDKMAN! website](https://sdkman.io/install).

## [](#repl)REPL

Like many modern languages, Scala ships with a REPL (which stands for \*R\*ead \*E\*valuate \*P\*rint \*L\*oop), an interactive terminal in which you can try out code snippets, and build programs iteratively. It's a great way to work through a _Hello World_ program. To give it a go, simply type `scala` into your terminal (we'll assume that you know to press `<Enter>` after commands).

```console
$ scala
```

```scala
Welcome to Scala 2.13.15 (OpenJDK 64-Bit Server VM, Java 11.0.11).
Type in expressions for evaluation. Or try :help.

scala>
```

You can see the commands available with `:help`, and leave the REPL any time with `:q`.

### [](#quick-intro-to-scala)Quick Intro to Scala

Just enter `6 * 7` to see that everything is working fine. You should see the result returned:

```scala
val res0: Int = 42
```

Which tells you that the answer is an `Int`, or integer object. The interpreter has assigned that result to a variable, `res0` (you may see something different, depending upon what you have already entered into the REPL), and you can even work with that label — enter `res0` into the REPL:

```scala
scala> res0
val res1: Int = 42
```

#### [](#static-typing)Static Typing

Scala is a statically typed language — like in Java, values _and_ variables have types — but unlike Java, Scala uses _type inference_ to determine type, cutting down on repetitive boilerplate.

```scala
scala> :type "hello"
String
```

We know "hello" is a string, as it's enclosed in double quote marks — and the compiler knows that too.

Let's try a different data structure. Put the following into the REPL:

```scala
val customers - Array(
                   Map(),
                   Map()
               )
```

## [](#installing-the-scala-sdk)Installing the Scala SDK

Maven, Gradle, or the Scala Build Tool (SBT) may all be used to manage dependencies, building, and deployment. Here we will use SBT:

```console
$ sdk install sbt
```

You can start SBT and run an interactive session. First change dirctory to an empty folder, then run:

```console
$ sbt
```

SBT will take a while to start up as it upgrades various things for you and builds a new project.

## [](#running-your-project)Running Your Project

```sbt
libraryDependencies += "com.couchbase.client" %% "scala-client" % "3.11.3"
```

**TODO**some intermediate steps…​.

```console
$ sbt run
```

## [](#further-reading)Further Reading

* The [Scala SBT site](https://scala-sbt.org/).