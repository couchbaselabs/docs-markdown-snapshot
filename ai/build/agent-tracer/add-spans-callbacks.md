---
title: Add Spans and Callbacks to Your Agent
description: Add spans and callbacks to your agentic app code to generate logs
  through the Agent Catalog.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/agent-tracer/add-spans-callbacks.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ai/build/agent-tracer/add-spans-callbacks.html)

# Add Spans and Callbacks to Your Agent

> Add spans and callbacks to your agentic app code to generate logs through the Agent Catalog. 

You can then examine these logs through the Agent Tracer or query them with the [Query Service](../../../cloud/n1ql/query.md) or [Capella Analytics](../../../analytics/intro/intro.md).

## [](#prerequisites)Prerequisites

* You have built an agentic app, integrated with the Agent Catalog.  
To use the Agent Tracer, you must have at least completed the [Prerequisites](../integrate-agent-with-catalog.md#prerequisites) and [Installed and Set Up Environment Variables](../integrate-agent-with-catalog.md#install).  
You must configure environment variables for a Capella operational cluster to use Agent Tracer and [View Traces in Agent Tracer](view-traces.md).

## [](#procedure)Procedure

To start logging agent activity with the Agent Catalog:

1. If you have not already, initialize the Agent Catalog package in your project by running the following command inside your project’s root directory:  
```console  
agentc init  
```
2. [Add a Root Span to Your Agentic App](#root-span)
3. [Define the Span for Chat Callbacks on Your Chat Model](#callbacks)
4. (Optional) [Add a Child Span For Each Agent or Task](#child-span)
5. (Optional) [Log The Results of Tool Calls](#tool-results)
6. (Optional) [Customize Log Messages with Span.log()](#span-log)
7. (Optional) [Add Tags to Spans or Logs](#add-tags)

### [](#root-span)Add a Root Span to Your Agentic App

To add a root span for your agentic app:

1. In your agent code, make sure you have imported the `agentc` package:  
```python  
import agentc  
```
2. Add the following code, replacing the `name="root"` attribute with the name you want to appear in Agent Tracer for your app:  
```python  
catalog = agentc.Catalog()  
root_span = catalog.Span(name="root_span")  
```

### [](#callbacks)Define the Span for Chat Callbacks on Your Chat Model

Defining a span for chat callbacks on your LLM varies depending on your chosen agent framework.

* LangChain/LangGraph
* LlamaIndex

Create a span and chat model, then attach the span to the chat model’s callback to log all LLM calls, using the given span as the root.

The callback logs `ChatCompletionContent` and `ToolCallContent`.

```python
import langchain_openai
import langchain_core.tools
import langgraph.prebuilt
import agentc_langchain.chat
import agentc_langgraph
import agentc

# Create a span to bind to the chat model messages.
catalog = agentc.Catalog()
root_span = catalog.Span(name="root_span")

# Create a chat model.
chat_model = langchain_openai.chat_models.ChatOpenAI(model="gpt-4o", callbacks=[])

# Create a callback with the appropriate span, and attach it to the chat model.
my_agent_span = root_span.new(name="My Agent")
callback = agentc_langchain.chat.Callback(span=my_agent_span)
chat_model.callbacks.append(callback)
```

You can also define the chat model callback to record the exact tools and output used by your chat model:

```python
# Grab the correct tools and output from the catalog.
my_agent_prompt = catalog.find("prompt", name="my_agent")
my_agent_tools = [
    langchain_core.tools.StructuredTool.from_function(tool.func) for tool in my_agent_prompt.tools
]
my_agent_output = my_agent_prompt.output

# Create a callback with the appropriate span, tools, and output, and attach it to the chat model.
my_agent_span = root_span.new(name="My Agent")
callback = agentc_langchain.chat.Callback(
    span=my_agent_span,
    tools=my_agent_tools,
    output=my_agent_output
)
chat_model.callbacks.append(callback)
```

Create a span and chat model, then attach the span to the chat model’s callback to log events from LlamaIndex, using the given span as the root.

The callback logs `ChatCompletionContent` and `ToolCallContent`.

```python
import agentc
import llama_index.core.llms
import llama_index.llms.openai

# Create a root span to bind to the messages.
catalog = agentc.Catalog()
root_span = catalog.Span(name="root_span")

# Define the chat model.
chat_model = llama_index.llms.openai.OpenAI(model="gpt-4o")

# In this example, we also get a prompt from the catalog
my_prompt = catalog.find("prompt", name="talk_like_a_pirate")

# Create the callback and attach it to the chat model
my_agent_span = root_span.new(name="My Agent")
chat_model.callback_manager.add_handler(Callback(span=my_agent_span))
result = chat_model.chat(
    [
        llama_index.core.llms.ChatMessage(role="system", content=my_prompt.content),
        llama_index.core.llms.ChatMessage(role="user", content="What is your name?"),
    ]
)
```

You can also choose event starts and ends to ignore:

```python

chat_model.callback_manager.add_handler(Callback(
  span=my_agent_span, 
  event_starts_to_ignore=["tree"],
  event_ends_to_ignore=None
))
```

For more information about the available LlamaIndex event types, see [the LlamaIndex documentation](https://developers.llamaindex.ai/python/framework-api-reference/callbacks/#llama%5Findex.core.callbacks.schema.CBEventType).

### [](#child-span)Add a Child Span For Each Agent or Task

To add additional spans to your agentic app:

1. Add a `.new` method call off the span where you want to define a new child span.  
For example, if you wanted to define an application for planning flights, with different spans for each agent in LangGraph, starting with a `root_span` called `flight_planner`:  
```python  
import agentc  
import langgraph.graph  
catalog = agentc.Catalog()  
root_span = catalog.Span(name="flight_planner")  
def front_desk_agent(...):  
    with root_span.new(name="front_desk_agent") as front_desk_span:  
        ...  
def route_finding_agent(...):  
    with root_span.new(name="route_finding_agent") as route_finding_span:  
        ...  
workflow = langgraph.graph.StateGraph()  
workflow.add_node("front_desk_agent", front_desk_agent)  
workflow.add_node("route_finding_agent", route_finding_agent)  
workflow.set_entry_point("front_desk_agent")  
workflow.add_edge("front_desk_agent", "route_finding_agent")  
...  
```

### [](#tool-results)Log The Results of Tool Calls

With just [chat callbacks on your chat model](#callbacks), Agent Catalog cannot log the results of tool calls in your application.

To log the results of tool calls in your agent app, do 1 of the following:

1. Add a configured `ToolNode` class for the tools in your agent to log tool call results:  
```python  
import langchain_openai  
import langchain_core.tools  
import langgraph.prebuilt  
import agentc_langchain.chat  
import agentc_langgraph  
import agentc  
# Create a span to bind to the chat model messages.  
catalog = agentc.Catalog()  
root_span = catalog.Span(name="root_span")  
# Create a chat model.  
chat_model = langchain_openai.chat_models.ChatOpenAI(model="gpt-4o", callbacks=[])  
# Create a callback with the appropriate span, and attach it to the chat model.  
my_agent_span = root_span.new(name="my_agent")  
callback = agentc_langchain.chat.Callback(span=my_agent_span)  
chat_model.callbacks.append(callback)  
# Grab the correct tools and output from the catalog.  
my_agent_prompt = catalog.find("prompt", name="my_agent")  
my_agent_tools = agentc_langgraph.tool.ToolNode(  
    span=my_agent_span,  
    tools=[  
        langchain_core.tools.tool(  
            tool.func,  
            args_schema=tool.input,  
        ) for tool in my_agent_prompt.tools  
    ]  
)  
my_agent_output = my_agent_prompt.output  
# Finally, build your agent.  
my_agent = langgraph.prebuilt.create_react_agent(  
    model=chat_model,  
    tools=my_agent_tools,  
    prompt=my_agent_prompt,  
    response_format=my_agent_output  
)  
```  
The `ToolNode` class assigns a span to the tool call results. The Agent Catalog generates `ToolResultContent` logs under the assigned span.  
For more information about the other parameters for a `ToolNode` class, see the [LangChain documentation](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool%5Fnode.ToolNode).
2. Define a custom log message to log tool results. See [Customize Log Messages with Span.log()](#span-log).

### [](#span-log)Customize Log Messages with Span.log()

You can choose to customize logging output from different areas of your agent app by calling the `.log()` method on a span.

For example, to log your own custom [key-value content](#key-value) pairs to your logs from a span:

```python
import my_agent_app
import my_output_evaluator
import agentc

# Create the catalog instance and the root span, evaluation_suite
catalog = agentc.Catalog()
evaluation_span = catalog.Span(name="evaluation_suite")

with open("my-evaluation-suite.json") as fp:
    for i, line in enumerate(fp):
        with evaluation_span.new(name=f"evaluation{i}") as span:
            output = my_agent_app(span)
            span["positive_sentiment"] = my_output_evaluator.positive(output)
            # Create a custom KeyValueContent log for negative sentiment received from the result of my_output_evaluator
            span.log(
                content={
                    "kind": "key-value",
                    "key": "negative_sentiment",
                    "value": my_output_evaluator.negative(output)
                    },
                # Add a custom annotation to the second log entry. These show up as Tags in Agent Tracer.
                alpha="SDGD"
            )
```

The `content` parameter on the `.log()` method can be 1 of the following:

| Content Value         | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SystemContent         | Logs messages generated by the system or application. System messages are commonly used to record the contents used to generate chat completion messages or tool calls. For more information, see [SystemContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.SystemContent).                                                                                      |
| ToolCallContent       | Logs messages, typically generated by the LLM, for calling a tool. Tool call messages typically contain the tool name and the arguments passed to the tool, as tool\_args. For more information, see [ToolCallContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.ToolCallContent).                                                                               |
| ToolResultContent     | Logs messages that contain the results of calling a tool. If you choose to add a tool\_call\_id to your ToolCallContent logs and ToolResultContent to link logs together on your tools. For more information, see [ToolResultContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.ToolResultContent).                                                              |
| ChatCompletionContent | Logs messages generated from the LLM in your agent app. These messages are separate from tool calls, and contain the output text from the LLM. For more information, see [ChatCompletionContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.ChatCompletionContent).                                                                                               |
| RequestHeaderContent  | Logs messages that contain information about chat completion or tool call events. These messages are typically tool names, descriptions, function schemas, and output types. For more information, see [RequestHeaderContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.RequestHeaderContent).                                                                   |
| UserContent           | Logs messages sent directly by the user to the agent application. These messages do not include messages generated by a prior LLM call. For more information, see [UserContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.UserContent).                                                                                                                          |
| AssistantContent      | Logs messages sent directly back to the user. These messages might not be strictly ChatCompletionContent messages, especially if your app uses multiple LLM calls before sending a message back to the user. For more information, see [AssistantContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.AssistantContent).                                           |
| BeginContent          | Logs messages that are used as markers and indicate the start of a span in your agent app. BeginContent messages can also record an entrance state for your app. For more information, see [BeginContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.BeginContent).                                                                                               |
| EndContent            | Logs messages that are used as markers and indicate the end of a span in your agent app. EndContent messages can also record the exit state for your app. For more information, see [EndContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.EndContent).                                                                                                          |
| EdgeContent           | Logs messages that involve the handoff of some state to another span in your app. If you have created a multi-agent app, EdgeContent messages can capture how an agent calls another. EdgeContent messages use a source and dest span to capture these messages. For more information, see [EdgeContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.EdgeContent). |
| KeyValueContent       | Logs any data you want to include for a specific span. These messages are different from tags, which you would attach to a log that already has content. You can specify a key to record a name for your entry and its value. For more information, see [KeyValueContent](https://couchbaselabs.github.io/agent-catalog/log.html#agentc%5Fcore.activity.models.content.KeyValueContent).                            |

### [](#add-tags)Add Tags to Spans or Logs

You can add custom tags on any span or message, to make filtering easier when you [View Traces in Agent Tracer](view-traces.md).

To add custom tags to your agent app, do 1 of the following:

1. [Add a Tag to a Span](#tag-span).
2. [Add a Tag to a Message](#tag-message).

#### [](#tag-span)Add a Tag to a Span

If you add a tag to a span, all messages within that span will be logged with that tag. Add the tag as an additional argument to the `span.new()` method.

For example, this adds a new `alpha` tag with a value of `SDGD` to logs in the `new_span`:

```python
my_root_span.new(name="new_span", alpha="SDGD")
```

#### [](#tag-message)Add a Tag to a Message

If you add the tag to a `.log()` method, only that message will be logged with that tag. Add the tag as an additional argument to the `.log()` method.

For example:

```python
span.log(
                content={
                    "kind": "key-value",
                    "key": "negative_sentiment",
                    "value": my_output_evaluator.negative(output)
                    },
                # Add a custom annotation to the second log entry. These show up as Tags in Agent Tracer.
                alpha="SDGD"
            )
```

## [](#next-steps)Next Steps

After you have configured your agent app to generate logs, you can [View Traces in Agent Tracer](view-traces.md) or [Query Agent Catalog Traces with SQL++](query-traces.md).