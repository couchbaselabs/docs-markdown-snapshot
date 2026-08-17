---
title: "Function: Basic SQL++ SELECT Statement"
description: Iterate through a basic N1QL SELECT where Eventing interacts with
  the Data service via an inline {sqlpp} statement.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/eventing/pages/eventing-handler-basicN1qlSelectStmt.adoc
  xref: xref:7.6@server:eventing:eventing-handler-basicN1qlSelectStmt.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/eventing/eventing-handler-basicN1qlSelectStmt.html)

# Function: Basic SQL++ SELECT Statement

**Goal**: Iterate through a basic N1QL SELECT where Eventing interacts with the Data service via an inline {sqlpp} statement.

* This function **basicN1qlSelectStmt** demonstrates how to use an inline N1QL SELECT statement with a passed parameter.
* Requires the "travel-sample" sample dataset to be loaded.
* Requires Eventing Storage (or metadata collection) and a "source" collection of travel-sample.inventory.airline.
* Assuming you deployed "From now" mutate any document in "travel-sample" to generate a log line.
* For more detail refer to [SQL++ Statements](eventing-language-constructs.md#added-lang-features).
* Configure the Function with a Feed Boundary "From now" (Note you will log 187 lines if you use "Everything").
* \[Optional\] if Feed Boundary is "Everything" you can use SQL++ to add an index for performance:

  * CREATE INDEX adv\_airline\_type ON `default`:\`travel-sample\`.`inventory`.`route`(`airline`) WHERE (`type` \= 'route')

* basicN1qlSelectStmt
* Input Data/Mutation (via the following SQL++ statement)
* Output Data/Logged

```javascript
// To run configure the settings for this Function, basicN1qlSelectStmt, as follows:
//
// Version 7.1+
//   "Function Scope"
//     *.* (or try travel-sample.inventory if non-privileged)
// Version 7.0+
//   "Listen to Location"
//     travel-sample.inventory.airline
//   "Eventing Storage"
//     rr100.eventing.metadata
//   Binding(s) - none
//
// Version 6.X
//   "Source Bucket"
//     travel-sample
//   "MetaData Bucket"
//     metadata
//   Binding(s) - none

function OnUpdate(doc, meta) {
    // ignore information we don't care about
    if (doc.type !== 'airline') return;

    var route_cnt = 0;       // we want to get the total routes per iata
    var airline = doc.iata;  // need a true variable as a SQL++ parameter

    var results =
        SELECT COUNT(*) AS cnt
        FROM `travel-sample`.`inventory`.`route`
        WHERE type = "route" AND airline = $airline;

    for (var item of results) {   // Stream results using 'for' iterator.
        route_cnt = item.cnt;
    }
    results.close();              // End the query and free resources held

    // Just log the KEY, AIRLINE and ROUTE_CNT it to the Application log
    log("key: " + meta.id + ", airline: "+doc.iata+", route_cnt: "+route_cnt);
}
```

```sqlpp
UPDATE `travel-sample`.`inventory`.`airline` USE KEYS "airline_24" SET id = 24
```

```json
2021-07-19T07:37:39.237-07:00 [INFO] "key: airline_24, airline: AA, route_cnt: 2354"
```