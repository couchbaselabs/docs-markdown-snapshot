---
title: Statistics
description: You can fetch Eventing Statistics for each deployed Function from
  an Eventing node using the Capella UI.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-statistics.adoc
pubDate: 2026-05-08T05:30:25.589Z
link: xref:cloud:eventing:eventing-statistics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-statistics.html)

# Statistics

> You can fetch Eventing Statistics for each deployed Function from an Eventing node using the Capella UI. 

## [](#via-the-capella-ui-eventing-tab)Via the Capella UI Eventing Tab

Eventing Statistics can be displayed in the Eventing tab for each deployed Function by clicking on the Function name to expand the Function controls. The following key metrics or Deployment Statistics are updated every 10 seconds by default and displayed as numeric values:

* **success** \- displays the number of times the function's handler code executed successfully, including mutation and timer callbacks.
* **failure** \- displays the number of times the function encountered an error during execution.
* **timeout** \- displays the number of times the function's execution was aborted because it exceeded the maximum allowed execution time.
* **backlog** \- displays the number of mutations waiting to be processed by the function.

In addition to the numeric statistics, you can also click the Log button () to display the log for any deployed function.