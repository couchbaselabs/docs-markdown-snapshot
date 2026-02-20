---
title: "Function: Basic SQL++ Prepared Select Statement"
description: Iterate through a basic {sqlpp} SELECT where Eventing interacts
  with the Data service via a prepared {sqlpp} statement.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/eventing/pages/eventing-handler-basicN1qlPreparedSelectStmt.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:eventing:eventing-handler-basicN1qlPreparedSelectStmt.adoc[]
---

[View original HTML](/server/7.6/eventing/eventing-handler-basicN1qlPreparedSelectStmt.html)

# Function: Basic SQL++ Prepared Select Statement

**Goal**: Iterate through a basic {sqlpp} SELECT where Eventing interacts with the Data service via a prepared {sqlpp} statement.

* This function **basicN1qlPreparedSelectStmt** demonstrates how use a prepared SQL++ SELECT statement with a passed parameter.
* Typically, this is done for greater performance, the cluster will typically not prepare a statement if it is already prepared.
* We have just one positional parameter $1 for "doc.iata", if we had a second parameter we would use the placeholder $2, and so on. Note positional parameters are passed in an array.
* A _commented out_ example of using named parameters is also shown. Note named parameters are passed and an object.
* Requires the "travel-sample" sample dataset to be loaded.
* Requires Eventing Storage (or metadata collection) and a "source" collection of travel-sample.inventory.airline.
* Deploy the Function with a Feed Boundary "From now" (Note you will log 187 lines if you use "Everything").
* Assuming you deployed "From now" mutate any document in "travel-sample" to generate a log line.
* For additional details refer to [SQL++ Statements](eventing-language-constructs.md#added-lang-features) and [The N1QL() function call](eventing-language-constructs.md#n1ql%5Fcall)
* \[Optional\] if Feed Boundary is "Everything" you can use SQL++ to add an index for performance:

  * CREATE INDEX adv\_airline\_type ON `default`:\`travel-sample\`.`inventory`.`route`(`airline`) WHERE (`type` \= 'route')

* basicN1qlPreparedSelectStmt
* Input Data/Mutation (via the following SQL++ statement)
* Output Data/Logged

```javascript
// To run configure the settings for this Function, basicN1qlPreparedSelectStmt, as follows:
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

    // positional parameter(s)
    var results = N1QL("SELECT COUNT(*) AS cnt " +
        "FROM `travel-sample`.`inventory`.`route` " +
        "WHERE type = \"route\" AND airline = $1",
        [doc.iata], { isPrepared: true }
    );

    /*
    // named parameter(s)
    var max_dist = 120;
    var results = N1QL("SELECT COUNT(*) AS cnt " +
        "FROM `travel-sample`.`inventory`.`route` WHERE type = $mytype " +
        "AND airline = $myairline AND distance <= $mydistance",
        { '$mytype': 'route', '$mydistance': max_dist, '$myairline': doc.iata },
        { 'consistency': 'none', isPrepared: true }
    );
    */

    for (var item of results) {   // Stream results using 'for' iterator.
        route_cnt = item.cnt;
    }
    results.close();              // End the query and free resources held

    // Just log the KEY, AIRLINE and ROUTE_CNT it to the Application log
    log("key: " + meta.id + ", airline: "+doc.iata+", route_cnt: "+route_cnt);
}
```

```sqlpp
UPDATE `travel-sample`.`inventory`.`route` USE KEYS "airline_24" SET id = 24;
```

```json
2021-07-19T07:48:10.810-07:00 [INFO] "key: airline_24, airline: AA, route_cnt: 2354"
```