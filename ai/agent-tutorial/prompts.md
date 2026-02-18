---
title: About Prompts and Prompt Engineering
description: Learn how prompts, context, and orchestration work together in agentic apps.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/agent-tutorial/pages/prompts.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ai/agent-tutorial/prompts.html)

# About Prompts and Prompt Engineering

> Learn how prompts, context, and orchestration work together in agentic apps. 

## [](#why-prompts)Why Prompts?

In an agentic app, the Large Language Model (LLM) is the reasoning engine. The LLM does not automatically know what to do but instead relies on the prompt it receives. The prompt is the input that tells the LLM:

* What role it’s playing.
* What tools it can use.
* What the user wants.
* What context is relevant right now.
* What rules or guardrails it must follow.

Understanding prompts and how they evolve during a workflow helps take away some of the mystery of agentic apps.

## [](#what-goes-into-a-prompt)What Goes Into a Prompt?

A prompt is more than just the user’s request. It’s a structured input assembled by the orchestration layer and contains multiple things.

| Component             | Description                                     | Example                                                   |
| --------------------- | ----------------------------------------------- | --------------------------------------------------------- |
| User input            | The goal or request from the user.              | Plan me a trip to Rome.                                   |
| System role / persona | Instructions about how the LLM should behave.   | You’re a helpful travel assistant.                        |
| Context               | Memory, retrieved knowledge, or current state.  | User prefers budget airlines, vegetarian meals.           |
| Tools                 | What the LLM can call or interact with.         | You can use the Flights API and Hotels API.               |
| Guardrails            | Rules and constraints that the LLM must follow. | Never book without confirmation. Stay under $1500 budget. |
| Intermediate results  | Outputs from previous steps in the workflow.    | Here are the available flights.                           |

This combination is what allows the LLM to reason, plan, and act.

## [](#context-and-context-engineering)Context and Context Engineering

Context is everything the LLM needs to make a good decision. It comes in 2 main forms:

* **Short-term context**: The current conversation or workflow state.
* **Long-term context**: The stored preferences, history, or knowledge retrieved from a database.

Context engineering is the practice of deciding what to include in the prompt and how to structure it. Too little context, and the LLM makes poor decisions. With too much context, the prompt becomes slow or confusing. The size of the prompt is also limited by the context size of the LLM.

Capella AI Services can help you manage your prompts using the [Agent Catalog](../build/integrate-agent-with-catalog.md) and the [Prompts Hub](../build/tools-prompts-hub.md#prompts-hub).

## [](#guardrails)Guardrails

Guardrails are rules that keep the agent safe, reliable, and aligned with user expectations. They’re included in the prompt itself, enforced programmatically by the orchestration layer, or both.

Guardrails protect against:

* Malicious or unsafe outputs, to prevent harmful, biased, or toxic content generation.
* Data leakage, to stop accidental exposure of sensitive or private information.
* Over-permissioning or unsafe actions, to avoid the AI taking risky steps such as deleting files.
* Prompt injections or jailbreaks, to protect against adversarial input designed to bypass safety rules.
* Hallucinations and misinformation, to reduce the risk of the model fabricating false or misleading outputs.
* Regulatory and compliance risks, to make sure outputs stay within legal and ethical boundaries.

For example, a prompt could include the following to add guardrails:

* `Do not share personal data`
* `Never execute a payment without explicit confirmation`
* `If uncertain, ask the user before proceeding`

Guardrails help make sure the LLM does not go off track whether by accident or through a malicious user.

For more information about guardrails on the Capella Model Service, see [Configure Guardrails and Security](../build/model-service/configure-guardrails-security.md).

## [](#the-orchestration-layers-role)The Orchestration Layer’s Role

The orchestration layer is responsible for building and updating the prompt as the workflow progresses. It decides:

* What context to fetch and include.
* When to call external tools or APIs.
* How to inject results back into the prompt.
* When to apply guardrails or safety checks.

## [](#how-agentic-apps-differ-from-traditional-apps)How Agentic Apps Differ from Traditional Apps

For experienced developers, you can think of the prompt as an evolution of a state object in a traditional app. Instead of storing values in variables to decribe the app’s state, an evolving prompt tells the LLM what state the app is in.

* In a traditional app, the structure of the state (variables, objects) and the logic is explicit.
* In an agentic app, the state is flattened into natural language (the prompt), and the LLM applies reasoning to decide what to do.

For example, if you were designing a travel app, the difference in state management between a traditional and agentic app could look like the following:

Traditional equivalent

```js
state = {
  destination: "Rome",
  budget: 1500,
  flights: [ ... ],
  hotels: [ ... ],
  preferences: { airline: "budget", meals: "vegetarian" }
}

// app logic:
if (state.budget > cheapestFlight + cheapestHotel) {
  suggestItinerary()
}
```

Agentic equivalent

```text
System: You are a helpful travel assistant.
User request: Plan me a 5-day trip to Rome in October, under $1500.
Context: User prefers budget airlines, vegetarian meals.
Flights API results: Airline A $400, Airline B $550.
Hotels API results: Hotel X $100/night, Hotel Y $150/night.
```

> [!TIP]
> Couchbase AI Services also offers notebooks and sample code hosted on Google Colab and GitHub to get you started with a prebuilt agentic app in your choice of agent framework:
> 
> * Colab: [LangGraph](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)
> * GitHub: [LangGraph](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)

## [](#example-travel-planner-app)Example: Travel Planner App

The following is an example of a travel planner app, with a prompt that evolves as it progresses through the app workflow. The example app can take a request from the user, find flights, find hotels, and suggest an itinerary.

![Diagram](_images/diag-cd74872f08b3d56b3e94955bbb777d5f68014ad2.svg) 

### [](#step-1-user-request)Step 1: User Request

User: `Plan me a 5-day trip to Rome in October, under $1500.`

Prompt at this stage

```text
System: You are a helpful travel assistant.

You can use the Flights API and Hotels API.

Always respect the user's budget and preferences.

Never book without confirmation.

User request: Plan me a 5-day trip to Rome in October, under $1500.
```

### [](#step-2-fetch-flights)Step 2: Fetch Flights

The LLM suggests checking flights. The orchestrator calls the Flights API and gets results.

Prompt at this stage

```text
System: You are a helpful travel assistant.

You can use the Flights API and Hotels API.

Always respect the user's budget and preferences.

Never book without confirmation.

User request: Plan me a 5-day trip to Rome in October, under $1500.

Context: User prefers budget airlines. Vegetarian meals when available.

Flights API results:


- Airline A: $400 round trip

- Airline B: $550 round trip
```

### [](#step-3-fetch-hotels)Step 3: Fetch Hotels

The LLM suggests checking hotels. The orchestrator calls the Hotels API and gets results.

Prompt at this stage

```text
System: You are a helpful travel assistant.

You can use the Flights API and Hotels API.

Always respect the user's budget and preferences.

Never book without confirmation.

User request: Plan me a 5-day trip to Rome in October, under $1500.

Context: User prefers budget airlines. Vegetarian meals when available.

Flights API results:


- Airline A: $400 round trip

- Airline B: $550 round trip

Hotels API results:


- Hotel X: $100/night

- Hotel Y: $150/night
```

### [](#step-4-suggest-itinerary)Step 4: Suggest Itinerary

Now the LLM can reason:

`Flight A ($400) + Hotel X ($500) = $900 total, within budget.`

It proposes an itinerary.

Prompt at this stage

```text
System: You are a helpful travel assistant.

You can use the Flights API and Hotels API.

Always respect the user's budget and preferences.

Never book without confirmation.

User request: Plan me a 5-day trip to Rome in October, under $1500.

Context: User prefers budget airlines. Vegetarian meals when available.

Flights API results:


- Airline A: $400 round trip

- Airline B: $550 round trip

Hotels API results:


- Hotel X: $100/night

- Hotel Y: $150/night

Proposed plan:


- Flight A ($400)

- Hotel X ($500 for 5 nights)

- Total: $900
```

## [](#key-takeaways)Key Takeaways

* Prompts in an agentic app are not static.
* Prompts evolve as the workflow progresses, with the orchestration layer adding context, results, and rules.
* Structured inputs guide agentic apps, not hidden intelligence.

## [](#see-also)See Also

* [About Agentic Apps](about-agentic-app.md)
* [Plan Your Agentic App](plan-agentic-app.md)
* [About RAG Blueprints](rag-patterns.md)
* [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md)