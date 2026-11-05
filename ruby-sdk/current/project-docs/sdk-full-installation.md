---
title: Full Installation
description: Installation instructions for the Couchbase Ruby Client.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Ruby SDK
    version: "3.9"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/release/3.9/modules/project-docs/pages/sdk-full-installation.adoc
  xref: xref:ruby-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Couchbase Ruby Client. 

## [](#prerequisites)Prerequisites

Ruby SDK supports MRI Ruby versions 4.0, 3.4, and 3.3.

## [](#installing-the-sdk)Installing the SDK

The source package is available through <https://rubygems.org/gems/couchbase> and can be installed with:

```console
gem install couchbase
```

Note that `--pre` is necessary when the SDK in Beta/Preview phase — `gem install --pre couchbase` — otherwise the latest stable release will be installed.

In addition to rubygems.org, we also maintain official gem repositories, where we publish not only source version of the package, but also precompiled binaries for Linux and MacOS.

To use official repository, it have to be registered in the `.gemrc` file:

```bash
gem sources --add https://packages.couchbase.com/clients/ruby/
```

The repository could be also specified in `Gemfile` for bundler. And in this case the source would be applied only for Couchbase SDK library:

```ruby
gem "couchbase", "3.9.1", :source => "https://packages.couchbase.com/clients/ruby/"
```

Or run in terminal:

```bash
gem install couchbase --clear-sources --source https://packages.couchbase.com/clients/ruby/
```

And finally, it is possible to download the package and install from the file. In the notes below, we specify tables with links to every release package along with precompiled binaries.

```bash
wget https://packages.couchbase.com/clients/ruby/sdk-3.9.1/couchbase-3.9.1-x86_64-linux.gem
gem install couchbase-3.9.1-x86_64-linux.gem
```

The URL structure is:

```shell
https://packages.couchbase.com/clients/ruby/sdk-3.9.1/couchbase-3.9.1-%{platform}.gem
```

where "platform" placeholder can take values: `arm64-darwin`, `x86_64-darwin`, `x86_64-linux`, `x86_64-linux-musl`. To see platform string the following command:

```bash
ruby -rrbconfig -e 'puts RbConfig::CONFIG["platform"]'
```