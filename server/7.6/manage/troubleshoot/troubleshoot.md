---
title: Troubleshoot
description: Common errors, general tips, and an account of how to handle core files.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/troubleshoot/troubleshoot.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.6@server:manage:troubleshoot/troubleshoot.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/manage/troubleshoot/troubleshoot.html)

# Troubleshoot

> Common errors, general tips, and an account of how to handle core files. 

## [](#about-this-section)About This Section

This section describes the most commonly encountered errors when using Couchbase Server and what you should do when you encounter them. You will also learn some general tips to keep in mind when troubleshooting your cluster, the various log files you might want to look into when troubleshooting an issue, and how you can report an issue to the Couchbase support.

## [](#using-log-files)Using Log Files

Couchbase _log files_ should be used when determining key events that have occurred on Couchbase Server. A complete explanation is provided in [Manage Logging](../manage-logging/manage-logging.md).

## [](#general-tips)General Tips

The following are some general tips that may be useful before performing any more detailed investigations:

* Try pinging the node.
* Try connecting to Couchbase Server Web Console on the node.
* Try to use `telnet` to connect to the various ports that Couchbase Server uses.
* Try reloading the web page.
* Check firewall settings (if any) on the node. Make sure there isn't a firewall between you and the node. On a Windows system, for example, the Windows firewall might be blocking the ports (**Control Panel** **Windows Firewall**.
* Make sure that the documented ports are open between nodes and make sure the data operation ports are available to clients.
* Check your browser's security settings.
* Check any other security software installed on your system, such as antivirus programs.
* Generate a Diagnostic Report for use by Couchbase Technical Support to help determine what the problem is. There are two ways of collecting this information:

  * Click the **Collect info** tab on the **Log** page and select the nodes to obtain a snapshot of your system's configuration and log information for deeper analysis. Send the collected log files to the Couchbase support.
  * Run `cbcollect_info` on each node within your cluster. This command requires the name of the zip file, and it must be run individually on each node within the cluster.  
  To run, you must specify the name of the file to be generated:  
  > cbcollect_info nodename.zip