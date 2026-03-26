---
title: Component Structure and Configuration
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/component-configuration.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:home:contribute:component-configuration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/component-configuration.html)

# Component Structure and Configuration

> [!NOTE]
> This documentation is out of date

## [](#terminology-and-structure)Terminology and Structure

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

## [](#config)Configuring a Component

Usually, you only edit the component descriptor file, _antora.yml_, when cutting a release branch and registering or deregistering a navigation file. The component descriptor assigns metadata to each component-version and used to build its page IDs, navigation menus, and URL segments. The following example shows the configuration for Couchbase Server 5.5 that's specified in its _antora.yml_ file.

antora.yml for Couchbase Server 5.5

```yaml
name: server
title: Couchbase Server
version: '5.5'
start_page: introduction:intro.adoc
nav:
- modules/ROOT/nav.adoc
```

`name`

The component coordinate used when creating an [xref from a page in one component to a page in another component](cross-references.md#component-coordinate).

`title`

The component name displayed in the [component and component version selector menus](nav-menus-and-files.md).

`version`

The version coordinate used when locking an xref destination target to a specific version of a page. Writers rarely use this coordinate because in-component xrefs target pages in the same component-version by default, and xrefs that link to pages in other components automatically jump to the latest version of the other component.

The UI uses `version` to sort component-versions in the [component version selector menu](nav-menus-and-files.md).

`version_title`

The version name displayed in the [component version selector menu](nav-menus-and-files.md). If this key isn't set, the value of `version` is used instead.

`start_page`

By default, Antora looks in ROOT for the file _index.adoc_ and uses it as the start page for a component. If ROOT doesn't contain _index.adoc_ (or you don't want to use that file as the component's start page), you must explicitly set a start page using its page ID.

`nav`

The nav key accepts a list of [navigation file](nav-menus-and-files.md#nav-file) paths. The order of the values dictates the order the contents of the navigation files are assembled in the published [component menu](nav-menus-and-files.md#component-menu).

## [](#supplemental-component-descriptor-files)Supplemental Component Descriptor Files

The Server component is aggregated from the _docs-server_, _couchbase-cli_, _backup_, and _asterix-opt_ repositories. When parts of a component are stored in multiple repositories, one _antora.yml_ file acts as the primary component descriptor. The primary file contains the `name`, `title`, `version`, and `nav` configuration. The component descriptor files in the other repositories are supplemental. They only contain `name` and `version`, so Antora can classify the content files' component-versions.

The following _antora.yml_ file supplements the [primary component descriptor file](#primary) shown in the previous section.

Supplemental _antora.yml_ in couchbase-cli repository

```yaml
name: server
version: '5.5'
```

Before releasing a new version of the Couchbase Server component to the production site, all of the repositories that contribute documentation to Server must have a branch containing a matching component-version. Otherwise, the new version will be missing pages and contain broken links.

## [](#learn-more)Learn More

* [Reference (xref) a page in another component](cross-references.md#component-coordinate).
* [Update a navigation file](update-nav.md).