---
title: Monitor and Observe with Agent Tracer
description: Use the Agent Tracer with the Agent Catalog and your agentic app to
  monitor and observe agent activity.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/agent-tracer/agent-tracer.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:build:agent-tracer/agent-tracer.adoc[]
---

[View original HTML](/ai/build/agent-tracer/agent-tracer.html)

# Monitor and Observe with Agent Tracer

> Use the Agent Tracer with the Agent Catalog and your agentic app to monitor and observe agent activity. 

If your agentic app [is configured to log activity](add-spans-callbacks.md), the Agent Catalog continuously collects log data in the `.agent-activity` folder in your project. If you have configured a Capella operational cluster in your Agent Catalog environment variables, your logs are automatically forwarded and can be viewed in Agent Tracer, or queried with the [Query Service](../../../cloud/n1ql/query.md) or [Capella Analytics](../../../analytics/intro/intro.md).

Agent Tracer can help you troubleshoot when agent behavior goes wrong, such as:

| Scenario                         | How to Use Agent Tracer                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Agent acts unpredictably         | Check the exact prompts sent to your agent and the generated thinking from your LLM during a user session.               |
| Wrong tool called                | Check the tools the agent called and troubleshoot, whether it’s similar names or overlapping and confusing descriptions. |
| Inter-agent coordination failure | Inspect the context handed off between agents - find withheld information or reasoning-action mismatches.                |
| Tool schema mismatch             | Compare the tool inputs provided to your agent’s LLM with your expected schema.                                          |
| Agent stuck in a loop            | Check whether the same tool or a set of tools are called in a loop, and check the agent’s reasoning log.                 |

To capture agent activity, add spans and callbacks to your application.

## [](#agentic-app-spans)Agentic App Spans

A span contains a specific operation or chunk of work within your agentic app, similar to an [Open Telemetry span](https://opentelemetry.io/docs/specs/otel/overview/#spans). A single span could be:

* A tool execution
* A Large Language Model (LLM) call
* A document retrieval

When defining spans in your app, you start with a root span, that contains the entire application. The name of your root span also sets the name of your application in Agent Tracer when you [View Traces in Agent Tracer](view-traces.md).

Define child spans from your root span to change what information gets logged at each step of your app. Customizing spans to a specific operation makes it easier to trace your agent activity in Agent Tracer and your log files.

You can also [add custom tags](add-spans-callbacks.md#add-tags) to specific traces to make them easier to find.

## [](#trace-types)Agent Tracer Trace Types

The following kinds of traces and information are captured and viewable in Agent Tracer:

| Trace Type   | Description                                                                                                                                                |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User         | Messages sent from an end user to your agentic app.                                                                                                        |
| Internal     | Request header messages that provide agents with available tools or other information.                                                                     |
| LLM          | Chat completion messages from the LLM to address the user request.                                                                                         |
| Tool Call    | Messages generated from tool calls, including tool names and arguments.                                                                                    |
| Tool Results | Messages containing tool results. Requires [ToolNode callbacks](add-spans-callbacks.md#tool-results) or [custom logging](add-spans-callbacks.md#span-log). |
| Hand-off     | Messages for transitions between different agents in a multi-agent app.                                                                                    |
| System       | System-generated messages for tracking the internal control flow of an app.                                                                                |
| Assistant    | Final response delivered to the user.                                                                                                                      |

## [](#see-also)See Also

* [Add Spans and Callbacks to Your Agent](add-spans-callbacks.md)
* [View Traces in Agent Tracer](view-traces.md)