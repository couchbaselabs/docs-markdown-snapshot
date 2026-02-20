---
title: About Agentic Apps
description: An overview of the key concepts involved in agentic apps.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/agent-tutorial/pages/about-agentic-app.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:agent-tutorial:about-agentic-app.adoc[]
---

[View original HTML](/ai/agent-tutorial/about-agentic-app.html)

# About Agentic Apps

> An overview of the key concepts involved in agentic apps. 

## [](#whats-an-agentic-app)What’s an Agentic App?

An agentic app uses a Large Language Model (LLM) to simulate reasoning, planning, and decision-making. This enables agentic apps to handle tasks with less explicit step-by-step programming.

Agentic apps tend to have these properties:

* **Being Goal-Oriented:** Tell your agent your specific goal, and it figures out how to meet that goal.
* **Autonomous Execution:** An agent can take actions without step-by-step instructions.
* **Multi-Step Reasoning:** An agent can break down complex tasks into smaller steps.
* **Tool and API Usage:** An agent can interact with external services, databases, or devices.

The defining feature of agentic apps is that they use an LLM to make decisions and execute steps towards a goal. The LLM is the brain of the app. It has agency to make decisions and use the tools it has available.

There’s no universally agreed definition for an agentic app. Apps can range from straight-forward assistants to fully autonomous agents.

Couchbase offers AI services that can support your agentic apps, making them easier to build, faster to run and cheaper to support. For more information about AI Services, see [Capella AI Services](../get-started/intro.md).

> [!TIP]
> Couchbase AI Services also offers notebooks and sample code hosted on Google Colab and GitHub to get you started with a prebuilt agentic app in your choice of agent framework:
> 
> * Colab: [LangGraph](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)
> * GitHub: [LangGraph](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)

## [](#why-create-agentic-apps)Why Create Agentic Apps?

Agentic apps can have benefits over using a traditionally programmed app:

| Benefit                                                                                                                   | Agentic App                                                                      | Traditional App                                                              |
| ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| High level of automation saves time, reduces repetitive work, and minimizes user effort.                                  | Users state their goal, and the app handles the entire process.                  | Users must manually perform each step or input fields and configure options. |
| More natural, human-like interaction. Closer to delegating tasks to a personal assistant.                                 | Focuses on what the user wants, figuring out the how automatically.              | Focuses on how to do something and uses step-by-step navigation.             |
| Multi-step reasoning and decision-making handles complex, changing scenarios without requiring constant user input.       | Can plan, adapt, and make decisions dynamically based on context and data.       | Executes predefined workflows with limited flexibility.                      |
| Proactive assistance improves convenience and reduces stress for the user.                                                | Can anticipate needs and act, such as rebooking a flight when detecting a delay. | Reacts only when the user initiates an action.                               |
| Integration with multiple tools and APIs expands capabilities without requiring the user to switch between multiple apps. | Can connect to external services, databases, and devices to complete tasks.      | Often limited to its own built-in features.                                  |
| Personalization and adaptation delivers increasingly relevant and efficient results.                                      | Learns from user behavior and preferences to improve over time.                  | Offers static features and settings.                                         |
| Frees mental bandwidth for more important decisions.                                                                      | Handles the complexity in the background.                                        | Users must remember steps, options, and settings.                            |

## [](#example-personal-finance-assistant-app)Example: Personal Finance Assistant App

Consider a personal finance assistant app. A traditional budgeting app might let you track spending, set goals, and receive alerts. When something unusual happens — like a duplicate charge or overspending in 1 category — you would still need to investigate and take action yourself.

An agentic app can go further:

* Monitor your transactions in real time.
* Detect unusual activity or overspending.
* Retrieve your budget and compare against goals.
* Suggest adjustments, such as moving money between accounts.
* Take action automatically if given prior permission, such as paying a bill or flagging a charge.

The app has less reliance on waiting for a user to interact with it to further the goal. The app can plan, adapt, and act on the user’s behalf.

To make this work, the app needs to interpret events, such as user goals, and decide on next steps. It needs some way to store preferences and past actions. It also requires access to banking APIs, budgeting systems, and notification services.

You can mix and match these components to build your app. Similarly, you can chain multiple LLMs to specialize in different tasks or add new tools as the app grows in capability.

![Diagram](_images/diag-9ec73d6ae330f7a21ccab1cab7397343b7059d5e.svg) 

The agent has access to tools and instructions, then tries to accomplish the goals. It’s possible to add modularly to this structure, introducing additional tools, memory sources and even LLMs specialized for different tasks.

## [](#key-concepts-of-agentic-apps)Key Concepts of Agentic Apps

Every agentic app is a combination of key concepts. It’s up to you how to combine these building blocks.

### [](#the-llm)The LLM

Rather than a complex decision tree, agentic apps use a Large Language Model (LLM) as a reasoning engine. The LLM can take instructions and make decisions on how to proceed.

It’s responsible for:

* Understanding the user’s request.
* Breaking it into smaller tasks.
* Deciding which tools to use and in what order.
* Integrating results into a coherent response.

For more information about how to deploy an LLM on Capella AI Services, see [Deploy a Large Language Model (LLM)](../build/model-service/deploy-llm-model.md).

### [](#the-orchestration-layer)The Orchestration Layer

The orchestration layer is the glue between the LLM and the rest of the app.

* Manages the prompt, updating it with context such as the conversation history.
* Decides when to call external tools or APIs.
* Injects retrieved knowledge into the prompt.
* Applies guardrails and safety checks.
* Handles retries, error recovery, and monitoring.

Keep in mind that the LLM can do some of this by itself. Some apps are more agentic than others. When you [plan your agentic app](plan-agentic-app.md), you need to decide the right balance between using your LLM and using the more traditionally programmed orchestration layer.

### [](#the-prompts)The Prompts

Prompts are how you tell the LLM what role it’s playing, how it should behave and what information it has available. In all but the most basic apps, a prompt is not just an initial instruction or user input. A prompt is a constructed input assembled by the orchestration layer. The prompt grows and changes as the app progresses through its workflow and more information becomes available. This is how the LLM stays informed of the app’s current state.

Prompts can include:

* The agent’s persona or style.
* Rules for interacting with the user.
* Step-by-step instructions for solving a problem.
* Information retrieved through RAG.
* Guardrails to prevent the app acting inappropriately.

A well-crafted prompt is like a good brief to a human assistant. It sets expectations and boundaries while providing all the information required to complete the task.

### [](#the-memory)The Memory

Most apps rely on some kind of memory to function. The LLM must take all information required to make decisions as part of the prompt.

Memory comes in 2 main forms:

1. **Short-term memory**: Keeps track of the current conversation or task state.
2. **Long-term memory**: Stores knowledge, past results, and important context for future use.

In both cases, the prompt incorporates memory, which the prompt then passes to the LLM. For short term memory, this can mean adding the conversation history into the prompt. The prompt contains context, which is all of the information the model has available to generate its output.

The model does not know everything and specific tasks require specialist context such as domain knowledge or sensitive user information. Agentic apps can retrieve context from an external source, such as fetching documents from a vector database. This is known as Retrieval Augmented Generation (RAG). Other types of RAG can retrieve information from tools such as a web search, often termed Tool Augmented Generation.

For more information about RAG, see [About RAG Blueprints](rag-patterns.md).

For more information about using a Capella operational cluster as a vector store, see [Process Your Data For Capella AI Services](../build/vectorization-service/data-processing.md).

### [](#the-tools)The Tools

Tools are the ways the agent interacts with the other systems either within the app or the outside world.

Tools might be:

* APIs
* Databases or document stores
* Web searches
* Pre-written code functions
* Other agents

Depending on the framework, the LLM may suggest tool usage, or the orchestration layer may decide when to invoke tools. Capella AI Services can also help you manage tool calling and tool versioning in your agentic apps. For more information, see [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md).

### [](#the-frameworks)The Frameworks

While you can build an agentic app entirely yourself, they can become complex as the app grows. Frameworks provide reusable building blocks and patterns that make this easier, such as:

* **Prompt management:** Ways to structure, template, and evolve prompts as the app runs. For help with prompt management, you can also use the [Agent Catalog](../build/integrate-agent-with-catalog.md).
* **Memory handling:** Utilities for storing and retrieving both short-term and long-term memory and context.
* **Tool integration:** Standard ways to connect APIs, databases, or functions so the LLM can use them.
* **Orchestration:** Mechanisms for coordinating multiple steps, handling branching workflows, retries, and error recovery.
* **Guardrails:** Ways to enforce rules, validate tool calls, and keep the agent within safe boundaries.

You do not need a framework to build an agentic app but they can:

* Save time by handling common patterns.
* Provide structure as your app grows more complex.
* Make it easier to swap out components such as different LLMs or memory stores.

For more information about agent frameworks, see [Agent Development Framework](plan-agentic-app.md#agent-framework).

## [](#putting-it-all-together)Putting It All Together

The above concepts combine to make an agentic app. Agentic apps tend to be quite modular as the LLM makes it easy to add or swap parts out.

![Diagram](_images/diag-ea9bd35224ee9822cfa557b679956f15fc7b8c8b.svg) 

This cycle can repeat, allowing the user to respond in natural language and allowing the LLM to guide the app accordingly.

## [](#see-also)See Also

* [Plan Your Agentic App](plan-agentic-app.md)
* [About RAG Blueprints](rag-patterns.md)
* [Capella AI Services](../get-started/intro.md)
* [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md)