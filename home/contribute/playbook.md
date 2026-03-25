---
title: Configure Your Antora Playbook
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/playbook.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:home:contribute:playbook.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/playbook.html)

# Configure Your Antora Playbook

The `docs-site` repository contains necessary files for building and publishing the Couchbase Documentation site.

For example, it contains the:

* staging playbook
* production playbook
* site extensions
* `home` docs component

To generate a local copy of the documentation site on your computer, you need the `antora-playbook.yml` file. This YAML file provides key site configuration information to Antora.

To generate the documentation site on your device, you need its playbook. The playbook provides the site configuration to Antora.

## [](#clone-the-playbook-project)Clone the Playbook Project

Just like any other documentation repository, you need to get the `docs-site` repository onto your computer:

1. Go to the [docs-site repository](https://github.com/couchbase/docs-site).
2. Follow the instructions in [Clone the Repository](set-up-repository.md#clone).

> [!NOTE]
> Contributors from outside Couchbase need to [fork documentation repositories](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) to contribute changes. If you’re a Couchbase employee, DO NOT fork repositories to contribute to Couchbase Documentation.

## [](#configure-a-local-antora-playbook)Configure a Local Antora Playbook

To generate a local copy of the documentation site and preview your changes, you need to configure a playbook file to use your local repositories.

To configure a local playbook file:

1. Create a copy of the `antora-playbook.yml` file inside the top-level folder of the `docs-site` repository on your computer.
2. Rename the copy to `local-antora-playbook.yml`.  
This stops your local playbook from being detected by Git. You can safely make changes to the file without worrying about committing those changes to the `docs-site` repository.
3. Open your new `local-antora-playbook.yml` in VS Code or your preferred editor.
4. Inside the `local-antora-playbook.yml`, under `antora > extensions`, delete the entry for the `"@antora/collector-extension"`.
5. [Choose whether to remove any repositories from your local build](#remove).
6. [Set the playbook to use the local version of the repository where you made your changes](#local-repo).
7. (Optional) [Set up Kroki to build diagrams](#setup-kroki-server).
8. Save the playbook file.

### [](#remove)Remove a Repository’s Files from Your Local Build

To remove the files from a repository from your local build and speed up the build process:

1. Under `sources`, locate the `url` key entry for the repository you want to remove.
2. Add a hash (`#`) to the start of the line with the `-url` key.
3. If the `-url` key is followed by a `branches` or `start_path` key, add a hash (`#`) to the start of those lines, too.  
For example, to remove the `couchbaselabs/docs-style-guide` files from a local build:  
```yaml
---  
sources:
  - url: .  
    branches: HEAD  
    start_path: home  
  #- url: https://github.com/couchbaselabs/docs-style-guide  
    #branches: main  
    #start_paths: [styleguide, ui-ux, pendo]
---  
```

> [!TIP]
> You can also delete the entire `-url` key entry for a repository to remove it from your build - but keep in mind that you might need to add it back in later for other documentation work.

### [](#local-repo)Use Your Local Repository in a Build

To use the files from your local repository in a build and preview your changes:

1. Under `sources`, locate the `url` key entry for the repository you modified and want to preview.
2. Change the `-url` key to either:

  1. The relative system path from your `docs-site` repository to the local repository.
  2. The absolute system path to the local repository.  
  For example, if you store all of your Documentation repositories in the same parent folder on your computer, and you modified files in the `docs-server` repository:  
  ```yaml
- url: ../docs-server  
      branches: [release/7.6, release/7.2, release/7.1, release/7.0]
- url: https://github.com/couchbase/docs-sdk-common  
      branches: [temp/7.5, release/7.2, release/7.1.2, release/7.1, release/7.0, release/6.6, release/6.5]  
  ```
3. On the line following the `-url` key, add a `branches` key, if there is not one already.
4. In the `branches` key, set the value to `HEAD`.  
You can keep additional version branches or set your local repository to the only branch to build. If you do keep multiple branches, do not keep the branch that you used as a base for your local changes.  
For example, if your working branch was based off of `docs-server release/7.6` and you wanted to keep the other release branches in your build:  
```yaml
- url: ../docs-server  
    branches: [HEAD, release/7.2, release/7.1, release/7.0]
- url: https://github.com/couchbase/docs-sdk-common  
    branches: [temp/7.5, release/7.2, release/7.1.2, release/7.1, release/7.0, release/6.6, release/6.5]  
```  
To use only your working branch, your YAML should look like the following:

- url: ../docs-server
    branches: HEAD
- url: https://github.com/couchbase/docs-sdk-common
    branches: [temp/7.5, release/7.2, release/7.1.2, release/7.1, release/7.0, release/6.6, release/6.5]

### [](#setup-kroki-server)Set Up The Kroki Server to Add Diagrams to Your Local Build

The Couchbase Documentation uses [Kroki](https://kroki.io) to generate diagrams from structured textual descriptions for easier maintenance.

The `antora-playbook.yml` uses the production Kroki server set up by Couchbase, but using this server will cause failures in your build and greatly extend the build time.

You can choose to use the public Kroki server, or comment out the Kroki configuration with hashes (`#`) to remove Kroki diagrams from your build.

To use the public Kroki server:

1. Under `asciidoc > attributes`, find the `kroki-server-url` key.
2. Set the `kroki-server-url` key to `<https://kroki.io>`:  
```yaml  
kroki-server-url: https://kroki.io  
```

If the public Kroki server is down or you just do not want diagrams in your build, add a hash before the following key entries in the playbook:

* `kroki-server-url` (under `asciidoc > attributes`)
* `kroki-fetch-diagram` (under `asciidoc > attributes`)
* `asciidoctor-kroki` (under `asciidoc > extensions`)

## [](#lightweight-local-playbook)Lightweight Local Playbook Example

You might have to comment out a number of repositories from the base Antora playbook file before you can successfully run a local build.

You can choose to start with a much more minimalist playbook to make things easier, and only add the repositories that you’re planning to work on.

For an example lightweight local playbook, see the [example local-staging-antora-playbook.yml file](https://github.com/couchbase/docs-site/blob/master/home/modules/contribute/examples/local-staging-antora-playbook.yml).

## [](#next-steps)Next Steps

[Set Up Documentation Repositories](set-up-repository.md)