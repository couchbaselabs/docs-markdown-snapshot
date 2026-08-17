---
title: Plan Your Agentic App
description: Before you start building, you should plan the tools, framework,
  and structure of your agent application.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/agent-tutorial/pages/plan-agentic-app.adoc
  xref: xref:ai:agent-tutorial:plan-agentic-app.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/agent-tutorial/plan-agentic-app.html)

# Plan Your Agentic App

> Before you start building, you should plan the tools, framework, and structure of your agent application. 

An AI agent could be a simple application like a chatbot, or a more specialized application designed to solve a specific problem, like a smart web crawler. For more information about agentic apps, see [About Agentic Apps](about-agentic-app.md).

> [!TIP]
> The Couchbase AI Data Plane also offers notebooks and sample code hosted on Google Colab and GitHub to get you started with a prebuilt agentic app in your choice of agent framework:
> 
> * Colab: [LangGraph](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)
> * GitHub: [LangGraph](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)

To effectively plan a new agentic app, you need to consider:

* The Large Language Model (LLM) you want to use to power your application.  
For more information about how to set up an embedding model or LLM on the AI Data Plane, see [Deploy an Embedding Model](../build/model-service/deploy-embed-model.md) or [Deploy a Large Language Model (LLM)](../build/model-service/deploy-llm-model.md). For more information about how to choose an LLM, see [Large Language Model (LLM)](#llm).
* The agent development framework you want to use to write and develop your agent code.  
For more information about how to choose an agent development framework and an overview of different available frameworks, see [Agent Development Framework](#agent-framework).
* The underlying storage you want to use for memory and agent data.  
For more information about using a Capella operational cluster for vector and data storage, see [Process Your Data For the Couchbase AI Data Plane](../build/vectorization-service/data-processing.md).
* The tools your agent needs to use to solve user problems.  
For more information about how the AI Data Plane can help manage your agent's tools, see [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md).
* The interface you want to use for user interactions with your application, such as a web application, command-line tool, or API.
* The way you want to test and evaluate the performance of your agentic app.  
For more information about using the AI Data Plane for evaluating your agent, see [Monitor and Observe with Agent Tracer](../build/agent-tracer/agent-tracer.md).

## [](#llm)Large Language Model (LLM)

Choosing the LLM for your agentic app depends on the specific use case for your agent.

If you choose to develop a multi-agent application to split agent tasks, you can use a different LLM for each agent, specialized to that specific task. You can also choose to call other LLM's when calling tools from an agent.

You should consider the following factors when choosing an LLM for your agentic app:

* [Context Size](#context-size)
* [Latency and Accuracy](#latency-and-accuracy)
* [Cost](#cost)
* [Tooling Support and Developer Ecosystem](#tooling-support)
* [Model Location](#model-location)
* [Reasoning Framework](#reasoning-framework)

### [](#context-size)Context Size

An LLM's context size, also known as context window or context length, determines how much information your agent can use for its tasks at once. It's comparable to a human's working memory. LLM context is made of tokens, or the smallest unit of language that an LLM can process. If a prompt, user conversation, or other information given to an LLM is larger than the model's context size, the LLM can lose information or need a summary to continue processing. Larger context size can increase accuracy, decrease hallucinations, and improve responses, but can increase costs.

Some agent tasks require models with larger context sizes. Agents that function as a customer support agent, contract analysis helper, or developer assistant all need larger context from the base LLM to support the functions of those use cases.

For example, if your agent needs to do any of the following, you'll need an LLM that supports a larger context size:

* Reference user conversations over time.
* Reference long documents.
* Use long-term memory for consistency across agent steps.
* Handle complex workflows or cooperate with multiple agents.

### [](#latency-and-accuracy)Latency and Accuracy

A key factor in an LLM's latency is the rate at which the LLM can process tokens, or its TPM/TPS (Tokens Per Minute or Tokens Per Second). A larger model takes longer to process tokens than a smaller model, which can make your agent feel slower to respond to an end user.

Both generating and processing tokens can increase latency on your model. Agents that need to be highly responsive and interactive for an end user might not benefit from a high-end model, because of the required latency.

When choosing your LLM, you need to decide if the quality and accuracy of your agent's responses matters more than the response speed.

If you need an agent that feels engaging and responsive, you might want a smaller, faster LLM. With correct tuning in your agent, such as long, detailed prompts and few-shot examples, you can still maintain quality outputs with speed and lower costs.

### [](#cost)Cost

If you need to keep a lot of context for your agent and chain a lot of calls to your LLM, the cost of that LLM increases. Tool and function calling requires processing tokens, and increases LLM costs.

Keeping context available for your agent, either through longer-term storage between sessions, or during a user interaction, can also increase your costs.

To reduce costs, you can try processing your agent interactions in batches. Batch processing reduces LLM costs but can reduce interactivity and increase the latency of your agent's responses.

You can also try to use a different LLM for different tasks. Use larger, more advanced models for complex reasoning, and smaller models for less complex tasks to keep your costs manageable. [Caching frequently used results from an LLM call](../build/model-service/configure-value-adds.md#caching) can also help.

### [](#tooling-support)Tooling Support and Developer Ecosystem

Different LLMs have different tooling support and tooling ecosystems. Not all LLMs support the same external tools or APIs. Similarly, not all LLMs have SDKs or easy integrations with development frameworks, like [LangGraph](https://langchain-ai.github.io/langgraph/) or [LlamaIndex](https://docs.llamaindex.ai/en/stable/).

When evaluating an LLM for tooling support, make sure to consider:

* Availability of official SDKs and libraries for your preferred programming language for your agent.
* Community support, documentation quality, and frequency of updates.
* Compatibility with your preferred orchestration frameworks, agent libraries, and workflow tools.
* Built-in support for features like function calling, retrieval-augmented generation (RAG), or custom tool integration.

If your agent needs to use APIs or integrate with other tools and systems, make sure that your LLM can support those integrations.

### [](#model-location)Model Location

Where you host your LLM can change your costs, model performance, data control, and model options.

Externally hosted models offer good performance, but you'll have less control over your data and do not have the same options to fine-tune model responses and behavior. Your usage costs might also be higher.

An open source, self-hosted model can reduce costs for higher volumes of usage, and keep sensitive data safe.

The Couchbase AI Data Plane offers a range of models that can be hosted inside your own VPC, giving full control over your data, model versioning, and more. For more information about hosting models on the AI Data Plane, see [Deploy Models with the AI Data Plane Model Service](../build/model-service/model-service.md).

### [](#reasoning-framework)Reasoning Framework

Related to your LLM, you need to choose how your agentic app should reason about or attempt to solve a user problem.

The reasoning framework for an agentic app is different from a model that has reasoning capabilities. A reasoning framework is an underlying structural decision for your application.

Your specific reasoning framework can also influence what [LLM](#llm) you use in your application.

Generally, agentic apps can use the following reasoning frameworks:

* [ReAct (Reasoning and Acting) Framework](#react)
* [ReWOO (Reasoning Without Observation) Framework](#rewoo)

#### [](#react)ReAct (Reasoning and Acting) Framework

In the ReAct framework, agents work through problems in a defined chain of thought-action-observation, to eventually arrive at a final answer.

Using prompts, the agent starts by using reasoning steps, or thoughts, to break down a task into smaller steps. The agent uses actions, such as calling tools, to gather more information. Then, the agent evaluates the information it's gathered, using its observations to return the final answer - or start another thought.

You'll also need to think about how many times you want to allow your agent to repeat the thought-action-observation loop, and write prompts that support and encourage ReAct in your model.

Use ReAct for your agent when you need to solve complex, multi-step problems with iterative reasoning and tool usage. ReAct works well when you need transparency in reasoning and an adaptable agent that can handle ambiguous or changing user requests.

When designing a ReAct agent, you need to choose an LLM that supports ReAct agent requirements, or talking through complex tasks and thought processes in a verbal way. Models that take direction and instruction well and support advanced reasoning work best with ReAct agents.

#### [](#rewoo)ReWOO (Reasoning Without Observation) Framework

In the ReWOO framework, agents solve tasks by turning problems into specific tasks. A ReWOO agent reasons about each task independently, instead of using the thought-action-observation loop like in the [ReAct framework](#react).

ReWOO agents start by generating a plan of actions, to help define a structure for the reasoning process. They then execute those actions, such as calling external tools, and use the LLM to format the information required for each action. An agent finishes by combining the results into a single, final answer.

ReWOO can simplify agent workflows and reduce latency, as the agent does not stop to observe or adjust its reasoning after each step. Use a ReWoo model when:

* Your agent and LLM can divide a problem into independent steps.
* Iterative feedback and reasoning checks are less important.
* You need predictable, fast execution in your agent.

If you want to use ReWOO in your agent, choose an LLM that can follow structured plans and handle multi-step instructions efficiently.

## [](#agent-framework)Agent Development Framework

When planning your agentic app, your specific agent development framework influences your programming language, the structure of your agent interactions, and data flow. It can limit or expand the growth of your application and determine how easily you can develop a production-ready solution.

Your agent development framework might also change which [LLM](#llm) you can use. Some frameworks offer more model flexibility than others.

Choose an agent development framework that supports your current and projected future needs for your application.

For the examples in this documentation, Couchbase has used [LangGraph and LangChain](#langgraph-langchain). Some of the top agent development frameworks include:

* [LangGraph and LangChain](#langgraph-langchain)
* [LlamaIndex](#llamaindex)
* [CrewAI](#crewai)
* [AutoGen](#autogen)

### [](#langgraph-langchain)LangGraph and LangChain

[LangGraph](https://www.langchain.com/langgraph) is a stateful, multi-agent framework built with [LangChain](https://www.langchain.com/). LangGraph uses graphs and state machines to define agents and can be used for multi-agent workflows. Specifically, LangGraph is great for complex workflows, including tool routing and complex tool usage.

LangGraph can support single, multi-agent, or hierarchical agent architectures, with flexibility around how much control and autonomy you want to give to your agent. You can also choose to stream messages from agents or workflows to keep users informed at each step of your application's flow.

LangGraph and LangChain are built on Python and require a Python installation to run.

LangGraph works best for an agent application that needs:

* Memory.
* The ability to try tool or prompt calls.
* To chain tool calls together.
* A reproducible control flow.

### [](#llamaindex)LlamaIndex

[LlamaIndex](https://www.llamaindex.ai/) is a framework that supports single or multi-agent applications. The framework emphasizes their support for Retrieval Augmented Generation (RAG) pipelines, and an extended developer ecosystem with third-party connectors and integrations. It can also work with LangChain agents to support external data and querying, or work as a standalone framework.

LlamaIndex is built on Python or JavaScript/TypeScript.

To get started with limited code, you can use [the create-llama command-line tool](https://www.npmjs.com/package/create-llama) to automatically generate a working application in Next.js or Python.

LlamaIndex works best for an agent application that needs:

* To integrate with multiple external data sources.
* To support RAG.
* Complex task routing and agent architecture.

### [](#crewai)CrewAI

[CrewAI](https://www.crewai.com/) is a multi-agent platform, designed to organize multiple agents into teams, called crews. Agents in a crew all have a specific role, goal, and tools, and can communicate with other agents.

CrewAI emphasizes options for no-code and automatic UI generation and deployment. The platform is based on building multi-agent applications, designed to accomplish specific tasks in defined processes of collaboration across agents. The framework is built on Python.

CrewAI works best for an agent application that needs:

* Cooperation across multiple agents to complete user tasks.
* Support for parallel processing on tasks.
* Rapid prototyping support or no-code contribution options.
* Integrated insights and metrics on a single platform.

### [](#autogen)AutoGen

[AutoGen](https://www.microsoft.com/en-us/research/project/autogen/) is an event-driven programming framework for building multi-agent AI systems and agentic apps. AutoGen uses a chat-based system that lets agents solve problems collaboratively.

AutoGen also supports a low to no-code option, called [AutoGen Studio](https://microsoft.github.io/autogen/stable//user-guide/autogenstudio-user-guide/index.html), which provides a graphical interface for creating agentic apps. You can use AutoGen to create single agents or multi-agent architectures.

AutoGen is based on Python and requires a Python installation to run.

AutoGen works best for an agent application that needs:

* External tooling and code execution support.
* A collaborative agent approach to negotiate the best solution, such as deliberative tasks or coding.
* Less long-running memory or retries.

## [](#see-also)See Also

* [About Agentic Apps](about-agentic-app.md)
* [About RAG Blueprints](rag-patterns.md)
* [Couchbase AI Data Plane](../get-started/intro.md)
* [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md)