---
title: Query Agent Catalog Traces with SQL++
description: You can also use SQL++ through the Query Service or Capella
  Analytics to query your Agent Catalog activity logs.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/agent-tracer/query-traces.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:ai:build:agent-tracer/query-traces.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/agent-tracer/query-traces.html)

# Query Agent Catalog Traces with SQL++

> You can also use SQL++ through the Query Service or Capella Analytics to query your Agent Catalog activity logs. 

Using queries might return more details on traces that you cannot see through the [Agent Tracer UI](view-traces.md).

## [](#prerequisites)Prerequisites

* You have completed the [Prerequisites](../integrate-agent-with-catalog.md#prerequisites) and [Installed and Set Up Environment Variables](../integrate-agent-with-catalog.md#install) for the Agent Catalog.
* You have deployed a single node or multi-node Capella operational cluster running Couchbase Server version 8.0 or later with the Search Service enabled.  
This should be the same cluster you add to your environment variables for the Agent Catalog.  
For more information about how to add Services to a cluster, see [Modify the Cluster Configuration](../../../cloud/clusters/modify-database.md#modify-existing-service).
* You have [indexed and published tools and prompts to the Agent Catalog](../integrate-agent-with-catalog.md#index-publish).
* You have [Add Spans and Callbacks to Your Agent](add-spans-callbacks.md).
* If you want to use Capella Analytics to query traces, you must [create a Capella Analytics cluster](../../../analytics/admin/prepare-project.md) and [configure your Agent Catalog cluster as a remote data source](../../../analytics/sources/remote-cb-capella.md).
* Your user account has the [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Creator](../../../cloud/organizations/organization-user-roles.md#organization-role-project-creator) organization role, or 1 of the following project roles:

  * [Project Owner](../../../cloud/projects/project-roles.md#project-owner-role)
  * [Data Reader](../../../cloud/projects/project-roles.md#project-cluster-data-reader)
  * [Data Writer](../../../cloud/projects/project-roles.md#project-cluster-data-reader-writer)
* You have logged into the Capella UI.

## [](#procedure)Procedure

To query traces from the Agent Catalog:

* Query Service
* Capella Analytics

1. In the Capella UI, on the **Operational** page, click the name of the cluster where you uploaded your Agent Catalog activity.
2. Go to **Data Tools** **Query**.
3. Do 1 of the following, or write your own query for your log data:

  1. [Query the Sessions View](#sessions-view)
  2. [Query the Exchanges View](#exchanges-view)
  3. [Query the ToolInvocations View](#tools-view)

1. In the Capella UI, on the **Analytics** page, click the name of the cluster where you created the link to your Agent Catalog operational cluster.
2. Do 1 of the following, or write your own query for your log data:

  1. [Query the Sessions View](#sessions-view)
  2. [Query the Exchanges View](#exchanges-view)
  3. [Query the ToolInvocations View](#tools-view)

### [](#sessions-view)Query the Sessions View

The following example queries use a generated data view called `Sessions` to return data on specific sessions in your agent activity. This can include agent handoff information, for help with debugging multi-agent systems.

* Query Service
* Capella Analytics

Copy and paste the following query into the Query Service's Query Workbench, replacing the placeholders with the bucket and scope for your Agent Catalog activity logs:

```sqlpp
FROM
        `[BUCKET_NAME]`.`[SCOPE_NAME]`.Sessions() s
    SELECT
        s.sid,
        s.cid,
        s.root,
        s.start_t,
        s.content,
        s.ann
    LIMIT 10;
```

If you want to specifically filter for agent handoff messages in the `Sessions` view, add a [WHERE clause](../../../cloud/n1ql/n1ql-language-reference/where.md) to your query for `kind = "edge"`:

FROM
        `[BUCKET_NAME]`.`[SCOPE_NAME]`.Sessions() s
    SELECT
        s.sid,
        s.cid,
        s.root,
        s.start_t,
        s.content,
        s.ann
    WHERE kind = "edge"
    LIMIT 10;

Copy and paste the following query into the Capella Analytics workbench. Replace the placeholders with the database, scope, and collection link name from your Analytics cluster remote link to your Agent Catalog activity logs. This query creates the `Sessions` data view:

```sqlpp
CREATE OR REPLACE ANALYTICS VIEW `[DATABASE_NAME]`.`[SCOPE_NAME]`.Sessions AS
    FROM
        `[DATABASE_NAME]`.`[SCOPE_NAME]`.`[COLLECTION_NAME]` AS l
    LETTING
        sid = l.span.session,
        cid = {
            "identifier": l.catalog_version.identifier,
            "timestamp": l.catalog_version.timestamp
        },
        root = l.span.name[0]
    GROUP BY
        sid,
        cid,
        root
        GROUP AS g
    LETTING
        content = (
            FROM
                g AS gi
            SELECT
                gi.l.content     AS event,
                gi.l.timestamp   AS timestamp,
                gi.l.span.name   AS name,
                gi.l.annotations AS annotations,
                ROW_NUMBER()
                    OVER (
                        ORDER BY
                            STR_TO_MILLIS(gi.l.timestamp) ASC
                    ) AS seq_num
            ORDER BY
                seq_num
        ),
        annotations = (
            FROM
                g AS gi
            WHERE
                gi.l.annotations IS NOT UNKNOWN
            SELECT DISTINCT
                gi.l.span.name,
                gi.l.annotations
        )
    SELECT
        sid                  AS sid,
        cid                  AS cid,
        root                 AS root,
        content              AS content,
        content[0].timestamp AS start_t,
        annotations          AS ann
    ORDER BY
        STR_TO_MILLIS(start_t) ASC;
```

Then, run the following query to return 10 `Sessions` records:

```sqlpp
FROM
      `[DATABASE_NAME]`.`[SCOPE_NAME]`.Sessions s
    SELECT
        s.sid,
        s.cid,
        s.root,
        s.start_t,
        s.content,
        s.ann
    LIMIT 10;
```

If you want to specifically filter for agent handoff messages in the `Sessions` view, add a [WHERE clause](../../../analytics/sqlpp/3%5Fquery.md#Where%5Fhaving%5Fclauses) to your query for `kind = "edge"`:

FROM
      `[DATABASE_NAME]`.`[SCOPE_NAME]`.Sessions s
    SELECT
        s.sid,
        s.cid,
        s.root,
        s.start_t,
        s.content,
        s.ann
    WHERE kind = "edge"
    LIMIT 10;

The records in the `Sessions` view contain the following information:

| Key      | Description                                                                                                                                                                                                                                                                                      |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| sid      | The session ID value. Set a session string on a span to customize this value, or accept the default generated UUIDs. For more information, see the [Agent Catalog documentation on Log.Span](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.log.Log.Span). |
| cid      | The specific catalog version.                                                                                                                                                                                                                                                                    |
| root     | The name of the root span, as configured in [Add a Root Span to Your Agentic App](add-spans-callbacks.md#root-span).                                                                                                                                                                             |
| start\_t | The start time of the session.                                                                                                                                                                                                                                                                   |
| content  | The events that occurred during the session, such as user messages, LLM responses, or internal agent thinking.                                                                                                                                                                                   |
| ann      | Any [custom tags](add-spans-callbacks.md#add-tags) added to the messages or the span.                                                                                                                                                                                                            |

### [](#exchanges-view)Query the Exchanges View

The following example queries use a generated data view called `Exchanges` to return data on specific exchanges, or the events between a user's input and the agent's response.

* Query Service
* Capella Analytics

Copy and paste the following query into the Query Service's Query Workbench, replacing `agent-catalog` and `agent-activity` with the bucket and scope for your Agent Catalog activity logs:

```sqlpp
FROM
        `[BUCKET_NAME]`.`[SCOPE_NAME]`.Exchanges() e
    SELECT
        e.sid,
        e.root,
        e.input,
        e.output,
        e.content
    ORDER BY
        e.output.timestamp DESC
    LIMIT 1;
```

Copy and paste the following query into the Capella Analytics workbench. Replace the placeholders with the database, scope, and collection link name from your Analytics cluster remote link to your Agent Catalog activity logs. This query creates the `Exchanges` data view:

```sqlpp
CREATE OR REPLACE ANALYTICS VIEW `[BUCKET_NAME]`.`[SCOPE_NAME]`.Exchanges AS
    WITH
        RowOrderedLogs AS (
            FROM
                `[BUCKET_NAME]`.`[SCOPE_NAME]`.`[LOG_COLLECTION_NAME]` AS l
            SELECT
                l.content.kind AS kind,
                l.span.session AS sid,
                l.*,
                ROW_NUMBER()
                    OVER (
                        PARTITION BY
                            sid
                        ORDER BY
                            STR_TO_MILLIS(l.timestamp) ASC
                    ) AS rn
        ),
        UserToAssistantRows AS (
            FROM
                RowOrderedLogs rol
            GROUP BY
                rol.sid
                GROUP AS g
            LETTING
                input_rows = (
                    FROM
                        g AS gi
                    WHERE
                        gi.rol.kind = "user"
                    SELECT VALUE
                        gi.rol.rn
                    ORDER BY
                        gi.rol.rn ASC
                ),
                output_rows = (
                    FROM
                        g AS gi
                    WHERE
                        gi.rol.kind = "assistant"
                    SELECT VALUE
                        gi.rol.rn
                    ORDER BY
                        gi.rol.rn ASC
                ),
                -- We are looking for the row numbers corresponding to user -- assistant pairs here.
                input_output_pairs = (
                    FROM
                       input_rows AS iro,
                       output_rows AS oro
                    WHERE
                        iro < oro
                    GROUP BY
                        iro
                        GROUP AS gi
                    -- We are interested in the closest assistant message to the user message.
                    LETTING
                        ordered_output = (
                            FROM
                                gi AS gii
                            SELECT VALUE
                                gii.oro
                            ORDER BY
                                gii.oro ASC
                        )
                    SELECT
                        iro               AS input_row,
                        ordered_output[0] AS output_row
                )
            SELECT
                rol.sid            AS sid,
                input_output_pairs AS pairs
        ),
        UserToAssistantUnnested AS (
            FROM
                UserToAssistantRows AS u2a,
                u2a.pairs AS p
            SELECT
                u2a.sid      AS sid,
                p.input_row  AS inp_rn,
                p.output_row AS out_rn
        )
    FROM
        UserToAssistantUnnested AS u2au,
        RowOrderedLogs AS rol
    WHERE
        rol.sid = u2au.sid AND
        rol.rn >= u2au.inp_rn AND
        rol.rn <= u2au.out_rn
    GROUP BY
        rol.sid          AS sid,
        rol.span.name[0] AS root,
        u2au.inp_rn      AS inp_rn,
        u2au.out_rn      AS out_rn
        GROUP AS g
    LETTING
        content = (
            FROM
                g AS gi
            SELECT VALUE
                OBJECT_REMOVE(gi.rol, "rn")
            ORDER BY
                gi.rol.timestamp ASC
        ),
        input_content = (
            FROM
                g AS gi
            WHERE
                gi.rol.rn = inp_rn
            SELECT VALUE
                OBJECT_REMOVE(gi.rol, "rn")
            LIMIT 1
        )[0],
        output_content = (
            FROM
                g AS gi
            WHERE
                gi.rol.rn = out_rn
            SELECT VALUE
                OBJECT_REMOVE(gi.rol, "rn")
            LIMIT 1
        )[0]
    SELECT
        sid            AS sid,
        root           AS root,
        input_content  AS `input`,
        output_content AS `out`,
        content        AS content;
```

Then, run the following query to return the most recent exchange record:

```sqlpp
FROM 
      `[DATABASE_NAME]`.`[SCOPE_NAME]`.Exchanges e
    SELECT 
        e.sid,
        e.root,
        e.input,
        e.out,
        e.content
    ORDER BY e.out.timestamp DESC
    LIMIT 1;
```

The records in the `Exchanges` view contain the following information:

| Key                                        | Description                                                                                                                                                                                                                                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| sid                                        | The session ID value. Set a session string on a span to customize this value, or accept the default generated UUIDs. For more information, see the [Agent Catalog documentation on Log.Span](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.log.Log.Span). |
| root                                       | The name of the root span, as configured in [Add a Root Span to Your Agentic App](add-spans-callbacks.md#root-span).                                                                                                                                                                             |
| input                                      | The user's input to the agent app.                                                                                                                                                                                                                                                               |
| output (out in the Capella Analytics view) | The assistant's response to the user's input.                                                                                                                                                                                                                                                    |
| content                                    | All intermediate content logs between the input and output events, including messages sent to the LLM, tools executed, and so on.                                                                                                                                                                |

### [](#tools-view)Query the ToolInvocations View

The following example queries use a generated data view called `ToolInvocations` to return data on tool calls and tool results.

You must have [configured your logs to record and associate tool calls with tool results](add-spans-callbacks.md#tool-results).

* Query Service
* Capella Analytics

Copy and paste the following query into the Query Service's Query Workbench, replacing `agent-catalog` and `agent-activity` with the bucket and scope for your Agent Catalog activity logs:

```sqlpp
FROM
        `[BUCKET_NAME]`.`[SCOPE_NAME]`.ToolInvocations() ti
    SELECT
        ti.sid,
        ti.root,
        ti.tool_call,
        ti.tool_result
    ORDER BY
        ti.tool_result.timestamp DESC
    LIMIT 1;
```

Copy and paste the following query into the Capella Analytics workbench. Replace the placeholders with the database, scope, and collection link name from your Analytics cluster remote link to your Agent Catalog activity logs. This query creates the `ToolInvocations` data view:

```sqlpp
CREATE OR REPLACE ANALYTICS VIEW `[BUCKET_NAME]`.`[SCOPE_NAME]`.ToolInvocations AS
    FROM
        (
            WITH
                RowOrderedToolLogs AS (
                    FROM
                        `[BUCKET_NAME]`.`[SCOPE_NAME]`.`[LOG_COLLECTION_NAME]` AS l
                    WHERE
                        l.content.kind = "tool-call" OR
                        l.content.kind = "tool-result"
                    SELECT
                        l.content.kind AS kind,
                        l.span.session AS sid,
                        l.*,
                        ROW_NUMBER()
                            OVER (
                                PARTITION BY
                                    sid
                                ORDER BY
                                    STR_TO_MILLIS(l.timestamp) ASC
                            ) AS rn
                ),
                CallToResultRows AS (
                    FROM
                        RowOrderedToolLogs rol
                    GROUP BY
                        rol.sid
                        GROUP AS g
                    LETTING
                        input_rows = (
                            FROM
                                g AS gi
                            WHERE
                                gi.rol.kind = "tool-call"
                            SELECT VALUE
                                gi.rol.rn
                            ORDER BY
                                gi.rol.rn ASC
                        ),
                        output_rows = (
                            FROM
                                g AS gi
                            WHERE
                                gi.rol.kind = "tool-result"
                            SELECT VALUE
                                gi.rol.rn
                            ORDER BY
                                gi.rol.rn ASC
                        ),
                        input_output_pairs = (
                            FROM
                               input_rows AS iro,
                               output_rows AS oro
                            WHERE
                                iro < oro
                            GROUP BY
                                iro
                                GROUP AS gi
                            LETTING
                                ordered_output = (
                                    FROM
                                        gi AS gii
                                    SELECT VALUE
                                        gii.oro
                                    ORDER BY
                                        gii.oro ASC
                                )
                            SELECT
                                iro               AS input_row,
                                ordered_output[0] AS output_row
                        )
                    SELECT
                        rol.sid            AS sid,
                        input_output_pairs AS pairs
                ),
                CallToResultRowsUnnested AS (
                    FROM
                        CallToResultRows AS c2r,
                        c2r.pairs AS p
                    SELECT
                        c2r.sid      AS sid,
                        p.input_row  AS inp_rn,
                        p.output_row AS out_rn
                ),
                ToolCalls AS (
                    FROM
                        `[BUCKET_NAME]`.`[SCOPE_NAME]`.`[LOG_COLLECTION_NAME]` AS l
                    WHERE
                        l.content.kind = "tool-call"
                    SELECT VALUE
                        l
                ),
                ToolResults AS (
                    FROM
                        `[BUCKET_NAME]`.`[SCOPE_NAME]`.`[LOG_COLLECTION_NAME]` AS l
                    WHERE
                        l.content.kind = "tool-result"
                    SELECT VALUE
                        l
                )
            FROM
                CallToResultRowsUnnested AS c2ru,
                RowOrderedToolLogs AS rol1,
                RowOrderedToolLogs AS rol2
            LETTING
                tool_call = OBJECT_REMOVE(rol1, "rn"),
                tool_result = OBJECT_REMOVE(rol2, "rn")
            WHERE
                rol1.rn = c2ru.inp_rn AND
                rol2.rn = c2ru.out_rn
            SELECT
                c2ru.sid       AS sid,
                c2ru.span.name AS root,
                tool_call      AS tool_call,
                tool_result    AS tool_result
            UNION ALL
            FROM
                ToolCalls AS tc,
                ToolResults AS tr
            WHERE
                tc.content.tool_call_id = tr.content.tool_call_id
            SELECT
                tc.span.session AS sid,
                tc.span.name    AS root,
                tc              AS tool_call,
                tr              AS tool_result
        ) AS ti
    GROUP BY
        tc.identifier
        GROUP AS g
    SELECT VALUE
        g[0].ti;
```

Then, run the following query to return the most recent tool invocation record:

```sqlpp
FROM
        `[BUCKET_NAME]`.`[SCOPE_NAME]`.ToolInvocations ti
    SELECT
        ti.sid,
        ti.root,
        ti.tool_call,
        ti.tool_result
    ORDER BY
        ti.tool_result.timestamp DESC
    LIMIT 1;
```

The records in the `ToolInvocations` view contain the following information:

| Key          | Description                                                                                                                                                                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| sid          | The session ID value. Set a session string on a span to customize this value, or accept the default generated UUIDs. For more information, see the [Agent Catalog documentation on Log.Span](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.log.Log.Span). |
| root         | The name of the root span, as configured in [Add a Root Span to Your Agentic App](add-spans-callbacks.md#root-span).                                                                                                                                                                             |
| tool\_call   | The tool call from your agent application.                                                                                                                                                                                                                                                       |
| tool\_result | The results returned by the tool call.                                                                                                                                                                                                                                                           |

## [](#next-steps)Next Steps

To view traces in the Agent Tracer UI, see [View Traces in Agent Tracer](view-traces.md).

To view details about specific tools and prompts published to Agent Catalog from your project, see [Use the Agent Catalog Tools and Prompts Hub](../tools-prompts-hub.md).