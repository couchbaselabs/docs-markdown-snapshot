---
title: About Couchbase Documentation Repositories
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/repositories.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:home:contribute:repositories.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/repositories.html)

# About Couchbase Documentation Repositories

The Couchbase Documentation site is built using multiple GitHub repositories. Each product tends to have its own GitHub repository or repositories. Some repositories contain common files for multiple products.

For a quick overview on some terminology and concepts related to GitHub repositories in general, see [About repositories in the GitHub Documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories).

Each repository follows the standard structure for an Antora component and its modules. For more information about our specific Antora repository file structure, see [Directory Structure and Key Files](#dir-structure).

## [](#repo-urls)Documentation Repository Roster

The Couchbase documentation is stored several organizations and multiple repositories on GitHub. The following repositories accept contributions via the regular workflow and use a standard branch pattern.

* [Couchbase Server](https://github.com/couchbase/docs-server)
* [Developer Docs](https://github.com/couchbaselabs/docs-devex)
* [REST APIs](https://github.com/couchbaselabs/cb-swagger)
* [Couchbase Lite](https://github.com/couchbaselabs/docs-couchbase-lite)
* [Sync Gateway](https://github.com/couchbaselabs/docs-sync-gateway)
* [C SDK](https://github.com/couchbase/docs-sdk-c)
* [.NET SDK](https://github.com/couchbase/docs-sdk-dotnet)
* [Go SDK](https://github.com/couchbase/docs-sdk-go)
* [Java SDK](https://github.com/couchbase/docs-sdk-java)
* [Kotlin SDK](https://github.com/couchbase/docs-sdk-kotlin)
* [Node.js SDK](https://github.com/couchbase/docs-sdk-nodejs)
* [PHP SDK](https://github.com/couchbase/docs-sdk-php)
* [Python SDK](https://github.com/couchbase/docs-sdk-python)
* [Ruby SDK](https://github.com/couchbase/docs-sdk-ruby)
* [Scala SDK](https://github.com/couchbase/docs-sdk-scala)
* [SDK Common](https://github.com/couchbase/docs-sdk-common)
* [Home and Contribute](https://github.com/couchbase/docs-site)

For a complete list, see the Documentation Repos Master List on the internal Couchbase Confluence.

### [](#repo-special)Repositories that Require Special Handling

Some Couchbase repositories only accept contributions via Gerrit, use custom branch patterns, and have additional content and AsciiDoc requirements. Review the project's README for the latest contributing requirements, or ask another Couchbase Documentation team member.

#### [](#cli)CLI

The CLI repository uses the Gerrit workflow and custom branch patterns. Additionally, the AsciiDoc files in this repository are used to create two sets of documentation:

1. The CLI pages incorporated in the Couchbase Server component.
2. Standalone man pages that are bundled with the Server software.

When editing these files, use the man page section structure and formatting.

* [CLI](https://github.com/couchbase/couchbase-cli)

#### [](#connectors)Connectors

The connector repositories use the Gerrit workflow.

* [Elasticsearch Connector](https://github.com/couchbaselabs/couchbase-elasticsearch-connector)
* [Kafka Connector](https://github.com/couchbase/kafka-connect-couchbase)
* [Spark Connector](https://github.com/couchbase/couchbase-spark-connector)

### [](#repo-private)Private Repositories

Some Couchbase repositories are private. Only Couchbase employees can contribute to the documentation in these components.

#### [](#backup)Backup

The Backup repository uses the Gerrit workflow and custom branch patterns. Like the CLI repository, this repository is used to create the Backup pages in the Couchbase documentation, and standalone man pages.

#### [](#autonomous-operator)Autonomous Operator

The Autonomous Operator repository uses the Gerrit workflow and custom branch patterns.

#### [](#analytics)Analytics

The Analytics service documentation uses the Gerrit workflow. It is maintained in collaboration with the [AsterixDB](https://github.com/couchbase/asterixdb) project.

## [](#dir-structure)Directory Structure and Key Files

All Couchbase Documentation repositories use a standard directory structure and some common files and features. This ensures that Antora can locate the documentation components, collect the content files, and then build docs.couchbase.com.

Here are some key terms for Couchbase Documentation repositories and files:

Component

A component contains:

* AsiiDoc content files
* Assets, like images
* Examples, like code samples
* Navigation files
* A component descriptor file (`antora.yml`).  
All of the files in a component are versioned together, based on the `antora.yml`.  
Components can sometimes be distributed across several GitHub repositories. For example, the component for the Server documentation is built from `docs-server`, `couchbase-cli`, `backup`, and `asterix-opt`.

All components are identified by `antora.yml` \- not a repository or directory.

Component Descriptor

A component must contain a component descriptor file named _antora.yml_. When Antora finds _antora.yml_ in a repository, it knows it has located a component (or part of component). The component descriptor tags the files under its hierarchy with the specified component name and version.

Component-Version

A component version is a specific version of the documentation stored in a component. Component names and component versions do not always map to a GitHub repository and branch. They can be set and modified independently from the GitHub repository and branch structure.

Module

Modules organize content files, including text, images, and code samples, inside a component. Modules are stored under the `modules` folder in a component. Components can contain multiple modules.

ROOT Module

The `ROOT` module contains necessary top-level content associated with a component. For example, the `ROOT` module contains the navigation files for a component. When pages in the `ROOT` module are published, these pages are promoted a level above any other modules' pages in that component's URL.

Navigation Files

The `ROOT` module usually contains a navigation file called `nav.adoc`. It contains an unordered list of [cross references](cross-references.md) to documentation pages in specific modules inside the component. Antora uses navigation files to build [navigation menus](nav-menus-and-files.md) for a component. For more information about working with navigation files, see [Update a Navigation File](update-nav.md).

Pages

A `pages` directory exists under a specific module in the `modules` directory. The `pages` directory specifically contains any AsciiDoc text files for whole pages in the Couchbase Documentation. For more information about structuring files in the `pages` directory, see [Standard Document Structure](pages.md).

Partials

A `partials` directory exists under a specific module in the `modules` directory. The `partials` directory contains AsciiDoc files that can be inserted inside files in the `pages` directory. This is helpful for content reuse and single-sourcing information across multiple pages. For more information about partials, see [Include Examples and Partials](includes.md).

Assets

An `assets` directory exists under a specific module in the `modules` directory. The `assets` directory can contain sub-directories, like `images`, that organize images and other multimedia files for the documentation. You can insert files in these directories into files in the `pages` directory. For more information about how to insert images into documentation, see [basics.adoc#images](basics.md#images).

Examples

An `examples` directory exists under a specific module in the `modules` directory. The `examples` directory contains non-AsiiDoc or image files, usually source code, for inserting as examples into the documentation. For more information about how to work with code examples, see [Code Blocks for Example Code](code-blocks.md).

## [](#next-steps)Next Steps

1. [Choose a base branch](create-branches.md#base-branch).
2. [Create a working branch for your changes](create-branches.md).