---
title: set checkpoint_param
description: The command <code class="cmd">set checkpoint_param</code> sets the checkpoint.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbepctl/set-checkpoint_param.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/cli/cbepctl/set-checkpoint_param.html)

# set checkpoint_param

> The command `set checkpoint_param` sets the checkpoint. 

## [](#syntax)Syntax

The basic syntax is:

cbepctl [host]:11210 -b [bucket-name] set checkpoint_param [parameter] [value]

## [](#description)Description

This command configures a checkpoint.

## [](#options)Options

The following are the command options:

__Table 1\. set checkpoint\_param options__
| Options                    | Description                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| chk\_max\_items            | Max number of items allowed in a checkpoint.                                                                        |
| chk\_period                | Time bound (in sec.) on a checkpoint.                                                                               |
| item\_num\_based\_new\_chk | True if a new checkpoint can be created based on. The number of items in the open checkpoint.                       |
| keep\_closed\_chks         | True if we want to keep closed checkpoints in memory, as long as the current memory usage is below high water mark. |
| max\_checkpoints           | Max number of checkpoints allowed per vBucket.                                                                      |
| enable\_chk\_merge         | True, if merging closed checkpoints is enabled.                                                                     |