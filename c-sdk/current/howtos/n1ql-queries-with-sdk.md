[View original HTML](/c-sdk/current/howtos/n1ql-queries-with-sdk.html)

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. Querying can solve typical programming tasks such as finding a user profile by email address, facebook login, or user ID. 

Our query service uses SQL++ (formerly N1QL), which will be fairly familiar to anyone who’s used any dialect of SQL. [Further resources](#<em>additional%5Fresources) for learning about SQL++ are listed at the bottom of the page. Before you get started you may wish to checkout the [SQL++ intro page](../../../server/current/n1ql/n1ql-language-reference/index.md), or just dive in with a query against our travel sample data set. In this case, the one thing that you need to know is that in order to make a Bucket queryable, it must have at least one index defined. You can define a \_primary index on a bucket. When a primary index is defined you can issue non-covered queries on the bucket as well.

```c
    std::string statement =
            "SELECT airportname, city, country FROM `" + bucket_name
                    + R"(` WHERE type="airport" AND city="New York")";

    lcb_CMDQUERY *cmd = nullptr;
    check(lcb_cmdquery_create(&cmd), "create QUERY command");
    check(lcb_cmdquery_statement(cmd, statement.c_str(), statement.size()),
            "assign statement for QUERY command");
    check(lcb_cmdquery_callback(cmd, query_callback), "assign callback for QUERY command");
    check(lcb_query(instance, &result, cmd), "schedule QUERY command");
    check(lcb_cmdquery_destroy(cmd), "destroy QUERY command");
    lcb_wait(instance, LCB_WAIT_DEFAULT);
```

## [](#queries-placeholders)Queries & Placeholders

Placeholders allow you to specify variable constraints for an otherwise constant query. There are two variants of placeholders: postional and named parameters. Positional parameters use an ordinal placeholder for substitution and named parameters use variables. Note that both parameters and options are optional.

```c
    std::string statement =
            "SELECT airportname, city, country FROM `" + bucket_name
                    + R"(` WHERE type="airport" AND city=$1)";

    lcb_CMDQUERY *cmd = nullptr;
    check(lcb_cmdquery_create(&cmd), "create QUERY command");
    check(lcb_cmdquery_statement(cmd, statement.c_str(), statement.size()),
            "assign statement for QUERY command");
    std::string city_json = "\"" + city + "\""; // production code should use JSON encoding library
    check(lcb_cmdquery_positional_param(cmd, city_json.c_str(), city_json.size()),
            "add positional parameter for QUERY comand");
    // Enable using prepared (optimized) statements
    check(lcb_cmdquery_adhoc(cmd, false), "enable prepared statements for QUERY command");
    check(lcb_cmdquery_callback(cmd, query_callback), "assign callback for QUERY command");
    check(lcb_query(instance, &result, cmd), "schedule QUERY command");
    check(lcb_cmdquery_destroy(cmd), "destroy QUERY command");
    lcb_wait(instance, LCB_WAIT_DEFAULT);
```

## [](#the-query-result)The Query Result

The result for each query is JSON and as a result queries will function the same regardless whether they are executed using the _cbq_ shell, an SDK, or using the REST API directly. Nevertheless, the result format recieved using an SDK may be different than that received using the `cbq` or the REST API.

## [](#query-options)Query Options

__Table 1\. Available Query options__
| Name                                                                                           | Description                                                                                                                    |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| lcb\_cmdquery\_reset(command)                                                                  | Reset the structure so that it may be reused for a subsequent query.                                                           |
| lcb\_cmdquery\_encoded\_payload(command,payload,payload length)                                | Get the JSON-encoded query payload.                                                                                            |
| lcb\_cmdquery\_payload(command, query, query length)                                           | Sets the JSON-encodes query payload to be executed.                                                                            |
| lcb\_cmdquery\_statement(command, statement, statement length )                                | Sets the actual statement to be executed.                                                                                      |
| lcb\_cmdquery\_scope\_name(command, scope name, scope length)                                  | Associate scope name with the query.                                                                                           |
| lcb\_cmdquery\_named\_param(command, argument name, name length, argument value, value length) | Sets a named argument for the query.                                                                                           |
| lcb\_cmdquery\_positional\_param(command, argument value, argument length)                     | Adds a positional argument for the query.                                                                                      |
| lcb\_cmdquery\_readonly(command, readonly)                                                     | Marks query as read-only ( set readonly value to non zero ).                                                                   |
| lcb\_cmdquery\_scan\_cap(command, value)                                                       | Sets maximum buffered channel size between the indexer client and the query service for index scans.                           |
| lcb\_cmdquery\_flex\_index(command, value)                                                     | Tells the query engine to use a flex index (utilizing the search service).                                                     |
| lcb\_cmdquery\_pipeline\_cap(command, item number)                                             | Sets maximum number of items each execution operator can buffer between various operators.                                     |
| lcb\_cmdquery\_pipeline\_batch(command, item number)                                           | Sets the number of items execution operators can batch for fetch from the KV.                                                  |
| lcb\_cmdquery\_consistency(command, mode)                                                      | Sets the consistency mode for the request.                                                                                     |
| lcb\_cmdquery\_consistency\_token\_for\_keyspace(command, keyspace, keyspace length, token)    | Indicate that the query should synchronize its internal snapshot to reflect the changes indicated by the given mutation token. |
| lcb\_cmdquery\_option(command, option name, name length, option value, value length)           | Set a query option.                                                                                                            |

## [](#examples)Examples

As well as the [API docs](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/group%5F%5Flcb-n1ql-api.html), there are examples in the GitHub repo for:

* [Query Example](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/query-criteria.cc)
* [Querying with Placeholders](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/query-placeholders.cc)
* [Scan Consistency](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/query-consistency.cc)
* [AtPlus (Read Your Own Writes)](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/query-atplus.cc)

## [](#querying-at-scope-level)Querying at Scope Level

It is possible to query off the [Scope level](../../../server/current/learn/data/scopes-and-collections.md) _with Couchbase Server 7.0_, using the `lcb_cmdquery_scope_name()` method. It takes the statement as a required argument, and then allows additional options if needed.

Usage details for this and `lcb_cmdquery_scope_qualifier()` can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/group%5F%5Flcb-n1ql-api.html#gadcd89153027afd789e2d31e250424c48).

## [](#additional-resources)Additional Resources

|  | The Query Service is not the only query option in Couchbase. Be sure to check that your use case fits your selection of query service. |
|  | -------------------------------------------------------------------------------------------------------------------------------------- |

The [Server doc SQL++ intro](../../../server/current/n1ql/n1ql-language-reference/index.md) introduces up a complete guide to the SQL++ language, including all of the latest additions.

The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.