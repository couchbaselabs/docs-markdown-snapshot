---
title: Integrate an Agent with the Agent Catalog
description: Use the Couchbase Agent Catalog to create your own custom AI agents
  with your preferred Large Language Model (LLM) and agent framework.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/integrate-agent-with-catalog.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ai/build/integrate-agent-with-catalog.html)

# Integrate an Agent with the Agent Catalog

> Use the Couchbase Agent Catalog to create your own custom AI agents with your preferred Large Language Model (LLM) and agent framework. 

An AI agent could be a simple application like a chatbot, or a more specialized application designed to solve a specific problem, like a smart web crawler.

Use Capella AI Services together with the Couchbase Agent Catalog to integrate Capella-hosted models into your agent. The Agent Catalog features a command-line tool and a Python SDK to support your development. It works with Capella as a profile store, transactional store, or vector store.

> [!TIP]
> Couchbase AI Services also offers notebooks and sample code hosted on Google Colab and GitHub to get you started with a prebuilt agentic app in your choice of agent framework:
> 
> * Colab: [LangGraph](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)
> * GitHub: [LangGraph](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)

The Agent Catalog also helps you:

* Write tools for using data you have stored in a Capella operational cluster.
* Centralize and reuse your tools across your development teams.
* Examine and monitor agent responses with the [Agent Tracer](agent-tracer/agent-tracer.md).
* Version your user and system prompts and other agent-specific metadata.
* Search for tools based on the question you want to answer, with support for catalogs of hundreds of tools.

The Agent Catalog is not an agent framework, but works with agent frameworks to help you develop and manage your tools and prompts. You can use any Python-based agent framework, such as [LangChain](https://www.langchain.com/) or [ControlFlow](https://controlflow.ai/welcome). Any agent framework that expects lists of Python functions and strings for prompts can use the Agent Catalog.

The Agent Catalog does not execute tools itself - tool execution is managed by your chosen framework. The Agent Catalog lets you manage and audit agent application activity, such as:

* Tool calls
* Tool results
* Agent handoffs
* LLM generations

You can also use it to manage your agent’s tools and prompts, through [Git](https://git-scm.com/) versioning and source control.

You can create new projects with the Agent Catalog, or integrate it into an existing project.

> [!NOTE]
> The Agent Catalog uses the [Python programming language](https://www.python.org/).

## [](#prerequisites)Prerequisites

* You have created an operational cluster in Capella that has the following:

  * Couchbase Server version 8.0 or later.
  * (Optional) To support the full capabilities of the Agent Catalog, including semantic search, make sure the Search Service is running on at least 1 Service Group. For more information, see [Services and Service Groups](../../cloud/clusters/databases.md#couchbase-services).
  * A bucket that can store data from the Agent Catalog.  
  Use any bucket settings you would prefer for your particular use case. For more information, see [Manage Buckets](../../cloud/clusters/data-service/manage-buckets.md).
  * Cluster access credentials that have read and write access to your Agent Catalog bucket. For more information, see [Manage Cluster Access Credentials](../../cloud/clusters/manage-database-users.md).
* You have added the IP address you want to use to connect to your Capella cluster to your list of Allowed IP Addresses. For more information about allowed IP addresses, see [Configure Allowed IP Addresses](../../cloud/clusters/allow-ip-address.md).
* You have the connection string for your Capella cluster.  
From the **Databases** page, go to **Connect** and copy the **Public Connection String** from any of the connection methods.
* You have installed [Python version 3.12 or later](https://www.python.org/downloads/).
* You have installed [Git](https://git-scm.com/) and set up a GitHub repository for your project inside your Python virtual environment. For more information about how to set up a GitHub repository, see the [GitHub Documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories?tool=cli).

## [](#install)Install and Set Up Environment Variables

To get started with the Couchbase Agent Catalog:

1. (Optional) Set up a virtual environment in your project to avoid conflicts with your system install of Python.  
For example, you could install and use [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
2. Install the Agent Catalog package in your project:  
```console  
pip install agentc  
```  
> [!TIP]  
> To install the helper packages for [LangChain](https://www.langchain.com/), [LangGraph](https://www.langchain.com/langgraph), or [LlamaIndex](https://www.llamaindex.ai/), run:  
>  
> ```console  
> pip install agentc[langchain,langgraph,llamaindex]  
> ```  
>  
> These helper packages contain custom helper functions to help automatically integrate Agent Catalog into the existing features in your chosen framework. For example, you could use `agentc_langgraph.agent.agent.ReActAgent.create_react_agent` instead of `langchain.agents.react.agent.create_react_agent` for easier logging.  
>  
> For alternate installation instructions for Agent Catalog, see the [agent-catalog documentation](https://couchbaselabs.github.io/agent-catalog/install.html#installation).
3. Add the required environment variables for the Agent Catalog to an `.env` file at the root of your project:  
```txt  
# Enter the connection string for your Capella cluster.  
AGENT_CATALOG_CONN_STRING=$CONNECTION_STRING  
# Enter the username from the cluster access credentials you created for your Agent Catalog bucket.  
AGENT_CATALOG_USERNAME=$CLUSTER_ACCESS_CREDENTIALS_USERNAME  
# Enter the password from the cluster access credentials you created for your Agent Catalog bucket.  
AGENT_CATALOG_PASSWORD=$CLUSTER_ACCESS_CREDENTIALS_PASSWORD  
# Enter the name of the bucket you created for the Agent Catalog.  
AGENT_CATALOG_BUCKET=$BUCKET_NAME  
# Enter the directory where you want to save your local Agent Catalog. The default is .agent-catalog.  
AGENT_CATALOG_CATALOG=.agent-catalog  
# Enter the directory where you want to save your local agent activity files. The default is .agent-activity.  
AGENT_CATALOG_ACTIVITY=.agent-activity  
```
4. (Optional) If you plan to use an OpenAI model with your agent, you can also add the following to your `.env` file:  
```txt  
OPENAI_API_KEY=$API_KEY  
```  
For more information about how to find your OpenAI API key, see [the OpenAI Help Center](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).  
> [!TIP]  
> You can use any LLM you want with the Agent Catalog and your chosen agent framework. Make sure you add any required API keys to your `.env` file.
5. (Optional) Add additional environment variables for other features of the Agent Catalog:  
```txt  
# If you want to use TLS for secure connections, enter the path to the TLS root certificate for your Couchbase cluster  
AGENT_CATALOG_CONN_ROOT_CERTIFICATE=$PATH_TO_ROOT_CERTIFICATE  
# If you do not want the Agent Catalog CLI to prompt for user input, enter False. The default is True.  
AGENT_CATALOG_INTERACTIVE=True  
# If you want to view debug messages for the Agent Catalog CLI and SDK, enter True.  
AGENT_CATALOG_DEBUG=False  
# Enter the version of your catalog that the Agent Catalog SDK should use to serve tools and prompts. By default, the SDK uses the latest version available in the Git repository for your project.  
AGENT_CATALOG_SNAPSHOT=$CATALOG_VERSION_VALUE  
# If you want your generated tool code from your agentc.Provider instances for prompts and other tools to be written to disk, enter the file location where the Agent Catalog should write the generated code.  
AGENT_CATALOG_PROVIDER_OUTPUT=$PATH_TO_OUTPUT_LOCATION  
# If you want audit logs generated by agentc.Auditor instances to write to a different location, enter the file location where you want to write and rotate logs. The default is ./agent-activity  
AGENT_CATALOG_AUDITOR_OUTPUT=./agent-activity  
# If you want to use a specific embedding model for indexing and querying tools and prompts, enter a valid embedding model supported by the sentence_transformers.SentenceTransformer class. The default is all-MiniLM-L12-v2.  
AGENT_CATALOG_EMBEDDING_MODEL=all-MiniLM-L12-v2  
# Enter a value for the total number of Vector Search index partitions you want to have on the nodes in your Couchbase cluster. Partitions increase performance, but also complexity and resource usage. The default value is 2 * the number of nodes with the Search Service in your cluster.  
AGENT_CATALOG_INDEX_PARTITION=$NUMBER_OF_INDEX_PARTITIONS  
# Enter a value for the maximum number of source partitions allowed for a Vector Search index definition. The default value is 1024.  
AGENT_CATALOG_MAX_SOURCE_PARTITION=1024  
```
6. Initialize the Agent Catalog in your project:  
```console  
agentc init  
```

You can also set options to install Git hooks to automatically index and publish your prompts, or skip local or remote Couchbase cluster initialization. For more information, see the [agent-catalog documentation](https://couchbaselabs.github.io/agent-catalog/cli.html#init-command).

After you install the Agent Catalog package, you should have access to the following in your project:

* `agentc-cli`: The Agent Catalog command-line tool
* `agentc-core`: The Agent Catalog core SDK package

## [](#develop-your-ai-agent)Develop Your AI Agent

To start developing your own AI agent with the Agent Catalog:

1. [Build any tools or prompts you want to use in your AI agent](#build).
2. [Index and publish your tools and prompts to the Agent Catalog and your Couchbase cluster](#index-publish).
3. [Call a tool or prompt from inside your agent code](#call).
4. [Configure and use the Agent Tracer to analyze and monitor your agent’s activity and performance](agent-tracer/agent-tracer.md).

If you want to integrate the Agent Catalog with an existing agent:

1. [Configure your existing tools to be indexed by the Agent Catalog](#add-existing-tool).
2. [Index and publish your tools and prompts to the Agent Catalog and your Couchbase cluster](#index-publish).
3. [Adjust your code to call the tool or prompt from the catalog inside your agent code](#call).
4. [Configure and use the Agent Tracer to analyze and monitor your agent’s activity and performance](agent-tracer/agent-tracer.md).

If you need to, at any time, you can also [Clean or Delete Data From Agent Catalog](#delete).

### [](#build)Build New Tools and Prompts

Choose what type of tool or prompt you want to use in your AI agent and add to the Agent Catalog.

The Agent Catalog converts the SQL++ queries, semantic searches, and HTTP requests you create into Python functions, after you retrieve them from the catalog using `get_item`. You can use these functions during LLM function and tool calls and execute them in your choice of agent framework. Your agent framework uses your prompts to create a final LLM prompt, which guides the LLM to choose the relevant tools for a question.

> [!TIP]
> The [agent-catalog GitHub repository](https://github.com/couchbaselabs/agent-catalog/) has some example code and tools that you can use right away in your agent.
> 
> Find these tools in the [examples](https://github.com/couchbaselabs/agent-catalog/tree/master/examples) folder, under `tools` for your specific framework.

* Python Function
* SQL++ Query
* Semantic Search
* HTTP Request
* Prompt

To add a new Python function as a tool for your agent, you can use the Agent Catalog command-line tool’s `add` command:

```console
agentc add 
Record Kind (python_function, sqlpp_query, semantic_search, http_request, prompt): python_function
Now building a new tool / prompt file. The output will be saved to: $PROJECT_PATH
Type: python_function

# Your function name must be written in snake case. 
Name: my_python_function 

Description: My first Python tool for my AI agent
Python (function) tool written to: $PROJECT_PATH\my_python_function.py
```

The Agent Catalog command-line tool creates a new `.py` file with your chosen tool name inside your project directory. The Python function comes with placeholder code to help get you started:

```python
# The following file has been automatically generated by agentc at 11:05AM on October 31, 2024.

from agentc import tool
from pydantic import BaseModel


# Although Python uses duck-typing, the specification of models greatly improves the response quality of LLMs.
# It is highly recommended that all tools specify the models of their bound functions using Pydantic or dataclasses.
# class SalesModel(BaseModel):
#     input_sources: list[str]
#     sales_formula: str


# Only functions decorated with "tool" will be indexed.
# All other functions / module members will be ignored by the indexer.
tool
def my_python_function(<<< Replace me with your input type! >>>) -> <<< Replace me with your output type! >>>:
    """My first Python tool for my AI agent"""

    <<< Replace me with your Python code! >>>
```

You can also create a new Python function file manually or configure an existing Python function for your catalog. See [Add Existing Tools or Prompts to the Agent Catalog](#add-existing-tool).

You can reference tools that have their Python source code outside your project’s GitHub repository, as long as they can be imported with an `import` statement.

You can add a SQL++ query that you want to use to search for data inside your Couchbase cluster. You can add any existing SQL++ query into a `.sqlpp` file to use with your agent. Use the Agent Catalog’s `add` command to create a new query:

```console
agentc add
Record Kind (python_function, sqlpp_query, semantic_search, http_request, prompt): sqlpp_query
Now building a new tool / prompt file. The output will be saved to: $PROJECT_PATH
Type: sqlpp_query

# Your sqlpp_query name must be written in snake case.
Name: my_sqlpp_query

Description: A query to find a list of direct routes between two airports, using source_airport and destination_airport.
SQL++ query tool written to: $PROJECT_PATH\my_sqlpp_query.sqlpp
```

The Agent Catalog command-line tool creates a new `.sqlpp` file with your chosen query name inside your project directory. The query includes some placeholder code and comments to help get you started:

```sqlpp
--
/*
# The name of the query must be a valid Python identifier - the name cannot include spaces.
name: my_sqlpp_query

# The description will be used in the docstring for this query's generated Python function.
description: >
    A query to find a list of direct routes between two airports, using source_airport and destination_airport.

# The inputs used to resolve the named parameters in the SQL++ query below.
# Inputs are described using a JSON object that follows the JSON schema standard.
# This field is mandatory, and will be used to build a Pydantic model.
# See https://json-schema.org/learn/getting-started-step-by-step for more info.
input: >
   <<< Replace me with your input type! >>>

# The outputs used describe the structure of the SQL++ query result.
# Outputs are described using a JSON object that follows the JSON schema standard.
# This field is mandatory, and will be used to build a Pydantic model.
# We recommend using the 'INFER' command to build a JSON schema from your query results.
# See https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/infer.html.
# In the future, this field will be optional (we will INFER the query automatically for you).
output: >
   <<< Replace me with your output type! >>>

# As a supplement to the tool similarity search, users can optionally specify search annotations.
# The values of these annotations MUST be strings (e.g., not 'true', but '"true"').
# This field is optional, and does not have to be present.
# annotations:
#   gdpr_2016_compliant: "false"
#   ccpa_2019_compliant: "true"

# The "secrets" field defines search keys that will be used to query a "secrets" manager.
# Note that these values are NOT the secrets themselves, rather they are used to lookup secrets.
secrets:

    # All Couchbase tools (e.g., semantic search, SQL++) must specify conn_string, username, and password.
    - couchbase:
        conn_string: CB_CONN_STRING
        username: CB_USERNAME
        password: CB_PASSWORD
*/
<<< Replace me with your SQL++ query! >>>
```

You can also create a new SQL++ query file manually or configure an existing SQL++ query. Make sure you include the required header information from the example before your SQL++ query.

Add a new semantic search as a tool to your agent to return content from a semantic search against a [Vector Search index](../../cloud/vector-search/vector-search.md). To create a semantic search tool, you must have:

* A bucket, scope, and collection on a Capella operational cluster that contains vector embeddings. For more information about buckets, scopes, and collections, see [Buckets, Scopes, and Collections](../../cloud/clusters/data-service/about-buckets-scopes-collections.md).
* A Vector Search index that includes the document field that contains your vector embeddings. For more information about how to create a Vector Search index, see [Create a Search Vector Index in Quick Mode](../../cloud/vector-search/create-vector-search-index-ui.md).
* The name of the embedding model used to create the vector embeddings in that field.

To add a new semantic search tool, use the Agent Catalog’s `add` command:

```console
agentc add
Record Kind (python_function, sqlpp_query, semantic_search, http_request, prompt): semantic_search
Now building a new tool / prompt file. The output will be saved to: $PROJECT_PATH

# Your semantic search name must be written in snake case.
Name: my_semantic_search

Description: Find product descriptions that are closely related to a collection of tags.

# The bucket, scope, and collection where you created your Vector Search index.
Bucket: my-bucket
Scope: my-scope
Collection: my-collection

# The name of the Vector Search index
Index Name: my-vector-search-index

# The name of the field that holds your vector embeddings
Vector Field: vector

# The name of the field to use for your tool's output results
Text Field: output_text

# The name of the embedding meal you used to generate the vector embeddings in your Vector Search index.
Embedding Model: sentence-transformers/all-MiniLM-L12-v2
Semantic search tool written to: $PROJECT_PATH\my_semantic_search.yaml
```

The Agent Catalog command-line tool creates a new `.yaml` file with your chosen semantic search name inside your project directory. The YAML file comes with some placeholders and comments to help you get started:

```yaml
record_kind: semantic_search

# The name of the query must be a valid Python identifier - the name cannot include spaces.
name: my_semantic_search

# The description will be used in the docstring for this search's generated Python function.
description: >
    Find product descriptions that are closely related to a collection of tags.

# The inputs used to build a comparable representation for a semantic search.
# Inputs are described using a JSON object that follows the JSON schema standard.
# This field is mandatory, and will be used to build a Pydantic model.
# See https://json-schema.org/learn/getting-started-step-by-step for more info.
input: >
   <<< Replace me with your input type! >>>

# As a supplement to the tool similarity search, users can optionally specify search annotations.
# The values of these annotations MUST be strings (e.g., not 'true', but '"true"').
# This field is optional, and does not have to be present.
# annotations:
#   gdpr_2016_compliant: "false"
#   ccpa_2019_compliant: "true"

# The "secrets" field defines search keys that will be used to query a "secrets" manager.
# Note that these values are NOT the secrets themselves, rather they are used to lookup secrets.
secrets:

  # All Couchbase tools (e.g., semantic search, SQL++) must specify conn_string, username, and password.
  - couchbase:
      conn_string: CB_CONN_STRING
      username: CB_USERNAME
      password: CB_PASSWORD

# Couchbase semantic search tools always involve a vector search.
vector_search:

  # A bucket, scope, and collection must be specified.
  # Semantic search across multiple collections is currently not supported.
  bucket: my-bucket
  scope: my-scope
  collection: my-collection

  # All semantic search operations require that a (FTS) vector index is built.
  # In the future, we will relax this constraint.
  index: my-vector-search-index

  # The vector_field refers to the field the vector index (above) was built on.
  # In the future, we will relax the constraint that an index exists on this field.
  vector_field: vector

  # The text_field is the field name used in the tool output (i.e., the results).
  # In the future, we will support multi-field tool outputs for semantic search.
  text_field: output_text

  # The embedding model used to generate the vector_field.
  # This embedding model field value is directly passed to sentence transformers.
  # In the future, we will add support for other types of embedding models.
  embedding_model: sentence-transformers/all-MiniLM-L12-v2
```

Add a new HTTP request as an agent tool to return operations from an [OpenAPI specification](https://spec.openapis.org/oas/v3.1.1.html). HTTP request tools let your agent use external services. Create one HTTP request tool for each endpoint you want your agent to use.

You must have an existing OpenAPI specification in JSON or YAML format, available in your project or hosted on a URL.

To add a new HTTP request tool, use the Agent Catalog’s `add` command:

```console
agentc add
Record Kind (python_function, sqlpp_query, semantic_search, http_request, prompt): http_request
Now building a new tool / prompt file. The output will be saved to: $PROJECT_PATH
Type: http_request

# Your http_request will not be assigned a name like the other tool types. Enter a name to populate the filename only.
Filename: my_http_request

# Do not include the path in your OpenAPI spec filename. 
OpenAPI Filename [NO PATH]: webhook-example.json
HTML request tool written to: $PROJECT_PATH\my_http_request.yaml
```

The Agent Catalog command-line tool creates a new `.yaml` file with your chosen filename inside your project directory. The YAML file comes with some placeholders and comments to help you get started:

```yaml
record_kind: http_request

# As a supplement to the tool similarity search, users can optionally specify search annotations.
# The values of these annotations MUST be strings (e.g., not 'true', but '"true"').
# This field is optional, and does not have to be present.
# annotations:
#   gdpr_2016_compliant: "false"
#   ccpa_2019_compliant: "true"

open_api:
  filename: webhook-example.json

  # Which OpenAPI operations should be indexed as tools are specified below.
  # This field is mandatory, and each operation is validated against the spec on index.
  operations:

    # All operations must specify a path and a method.
    # 1. The path corresponds to an OpenAPI path object.
    # 2. The method corresponds to GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS/TRACE.
    # See https://swagger.io/specification/#path-item-object for more information.
    - path: <<< Replace me with a path! >>>
      method: <<< Replace me with a method! >>>
```

Add a new prompt to specify tools, instructions, or context to guide your AI agent’s behavior, without the use of additional formatting or templating.

Author your prompts in separate `.prompt` files, instead of embedding them directly in your code.

To add a new prompt, you can use the Agent Catalog’s `add` command:

```console
agentc add
Record Kind (python_function, sqlpp_query, semantic_search, http_request, prompt): prompt
Now building a new tool / prompt file. The output will be saved to: $PROJECT_PATH
Type: prompt

# Your raw prompt name must be written in snake case.
Name: my_prompt

Description: This prompt provides instructions for how to find routes between airports.
Raw prompt written to: $PROJECT_PATH\my_prompt.prompt
```

The Agent Catalog command-line tool creates a new `.prompt` file with your chosen name inside your project directory. The prompt file comes with some placeholders and comments to help you get started:

```prompt
---
record_kind: prompt

# The name of the prompt must be a valid Python identifier - the name cannot include spaces.
name: my_prompt

# The description will be used indirectly when running semantic searches for prompts.
description: >
    This prompt provides instructions for how to find routes between airports.

# As a supplement to the description similarity search, users can optionally specify search annotations.
# The values of these annotations MUST be strings (e.g., not 'true', but '"true"').
# This field is optional, and does not have to be present.
# annotations:
#  organization: "sequoia"

# A prompt is _generally_ (more often than not) associated with a small collection of tools.
# This field is used at provider time to search the catalog for tools.
# This field is optional, and does not have to be present.
# tools:
#   # Tools can be specified using the same parameters found in Provider.get_tools_for.
#   # For instance, we can condition on the tool name...
#   - name: "find_indirect_routes"
#
#   # ...the tool name and some annotations...
#   - name: "find_direct_routes"
#     annotations: gdpr_2016_compliant = "true"
#
#   # ...or even a semantic search via the tool description.
#   - query: "finding flights by name"
#     limit: 2

# Below the '---' represents the prompt in its entirety.
---
<<< Replace me with your prompt! >>>
```

#### [](#add-existing-tool)Add Existing Tools or Prompts to the Agent Catalog

If you have existing agent code that you want to integrate with the Agent Catalog, you need to add specific metadata or decorators to your code.

* Python Function
* SQL++ Query
* HTTP Request
* Prompt

If you have an existing Python tool that you want to add to the Agent Catalog, add `agentc` to your imports and add the `@agentc.catalog.tool` decorator to your tool definition:

```python
import my_framework_1
import agentc

# Add the decorator to make sure your tool is indexed by the Agent Catalog
@agentc.catalog.tool
def my_tool_1(arg_1: int, arg_2: int):
    """a good description"""
    ...
```

To add an existing SQL++ query, you must include YAML metadata in a multi-line C-style comment at the top of your file:

```sqlpp
/*
# The name of the tool must be a valid Python identifier (e.g., no spaces).
# This field is mandatory, and will be used as the name of a Python function.
name: example_sqlpp_query_name

# A description for the function bound to this tool.
# This field is mandatory, and will be used in the docstring of a Python function.
description: >
    Fill me in with a description of this query.

# The inputs used to resolve the named parameters in the SQL++ query below.
# Inputs are described using a JSON object (given as a string) OR a YAML object that follows the JSON schema standard.
# This field is mandatory, and will be used to build a Pydantic model.
# See https://json-schema.org/learn/getting-started-step-by-step for more info.
input:
    type: object
    properties:
      source_airport:
        type: string
      destination_airport:
        type: string

# The outputs used describe the structure of the SQL++ query result.
# Outputs are described using a JSON object (given as a string) OR a YAML object that follows the JSON schema standard.
# This field is mandatory, and will be used to build a Pydantic model.
# We recommend using the 'INFER' command to build a JSON schema from your query results.
# See https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/infer.html.
# In the future, this field will be optional (we will INFER the query automatically for you).
# output: >
#     {
#       "type": "array",
#       "items": {
#         "type": "object",
#         "properties": {
#           "airlines": {
#             "type": "array",
#             "items": { "type": "string" }
#           },
#           "layovers": {
#             "type": "array",
#             "items": { "type": "string" }
#           },
#           "from_airport": { "type": "string" },
#           "to_airport": { "type": "string" }
#         }
#       }
#     }

# The "secrets" field defines search keys that will be used to query a "secrets" manager.
# Note that these values are NOT the secrets themselves, rather they are used to lookup secrets.
# Users must specify these variables at runtime as environment variables OR explicitly through a Catalog instance.
secrets:
    # All Couchbase tools (e.g., semantic search, SQL++) must specify conn_string, username, and password.
    - couchbase:
        conn_string: CB_CONN_STRING
        username: CB_USERNAME
        password: CB_PASSWORD
        # certificate: CB_CERTIFICATE
*/
```

HTTP requests must use an [OpenAPI specification](https://spec.openapis.org/oas/v3.1.1.html) and include a `record_kind: http_request` at the start of their YAML definition:

```yaml
#
# The following file is a template for a set of HTTP request tools.
#
record_kind: http_request

# As a supplement to the tool similarity search, users can optionally specify search annotations.
# The values of these annotations MUST be strings (e.g., not 'true', but '"true"').
# This field is optional, and does not have to be present.
annotations:
  gdpr_2016_compliant: "false"
  ccpa_2019_compliant: "true"

# HTTP requests must be specified using an OpenAPI spec.
open_api:

  # The path relative to the tool-calling code.
  # The OpenAPI spec can either be in JSON or YAML.
  filename: path_to_openapi_spec.json

  # A URL denoting where to retrieve the OpenAPI spec.
  # The filename or the url must be specified (not both).
  # url: http://url_to_openapi_spec/openapi.json

  # Which OpenAPI operations should be indexed as tools are specified below.
  # This field is mandatory, and each operation is validated against the spec on index.
  operations:

    # All operations must specify a path and a method.
    # 1. The path corresponds to an OpenAPI path object.
    # 2. The method corresponds to GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS/TRACE.
    # See https://swagger.io/specification/#path-item-object for more information.
    - path: /users/create
      method: post
    - path: /users/delete/{user_id}
      method: delete
```

Prompts must set the `record_kind` as `prompt`, and provide a name and description. The prompt itself must be a string or a YAML object:

```prompt
# To signal to Agent Catalog that this file is a prompt, the 'record_kind' field must be set to 'prompt'.
record_kind: prompt

# The name of the prompt must be a valid Python identifier (e.g., no spaces).
# This field is mandatory, and will be used when searching for prompts by name.
name: endpoint_finding_node

# A description of where this prompt is used.
# This field is mandatory, and will be used (indirectly) when performing semantic search for prompts.
description: >
  All inputs required to assemble the endpoint-finding node.

# As a supplement to the description similarity search, users can optionally specify search annotations.
# The values of these annotations MUST be strings (e.g., not 'true', but '"true"').
# This field is optional, and does not have to be present.
annotations:
  framework: "langgraph"

# The output type (expressed in JSON-schema) associated with this prompt.
# See https://json-schema.org/understanding-json-schema for more information.
# This field is commonly supplied to an LLM to generate structured responses.
# This field is optional, and does not have to be present.
output:
  title: Endpoints
  description: The source and destination airports for a flight / route.
  type: object
  properties:
    source:
      type: string
      description: "The IATA code for the source airport."
    dest:
      type: string
      description: "The IATA code for the destination airport."
  required: [source, dest]

# The main content of the prompt.
# This field is mandatory and must be specified as a string OR a YAML object.
content:
  agent_instructions: >
    Your task is to find the source and destination airports for a flight.
    The user will provide you with the source and destination cities.
    You need to find the IATA codes for the source and destination airports.
    Another agent will use these IATA codes to find a route between the two airports.
    If a route cannot be found, suggest alternate airports (preferring airports that are more likely to have routes
    between them).

  output_format_instructions: >
    Ensure that each IATA code is a string and is capitalized.
```

### [](#index-publish)Index and Publish New Tools and Prompts to the Agent Catalog

> [!TIP]
> If you do not want the Agent Catalog to index your agent code, create an `.agentcignore` file and add the files or filename patterns that you want the Agent Catalog to ignore.

After you have written new tools or prompts or prepared existing tools and prompts, you must index them in the Agent Catalog. Indexing creates a JSON index file in your local project that contains information about your tools and prompts.

When you publish, you send these JSON index files to the Couchbase cluster configured in your environment variables, where you can [Use the Agent Catalog Tools and Prompts Hub](tools-prompts-hub.md).

The Tools and Prompts Hub and the Agent Catalog rely on Git for versioning and source control for your tools and prompts. It’s important to push your agent project to Git, and index your tools and prompts often.

To index and publish your tools or prompts:

1. Create a new commit in Git for all changes in your project. Before you index any tools or prompts, you must make sure that your working directory in Git is clean.  
> [!TIP]  
> Run `git status` to check the current status of your working directory in Git.
2. To index all tools and prompts contained in a single directory, in your command prompt, run the following command:  
```console  
agentc index $PATH_TO_TOOL_OR_PROMPT_DIRECTORY  
```  
The Agent Catalog creates a new directory, `.agent-catalog`, that can contain 2 files:

  * `tool-catalog.json`, which contains the index for the tools found in the directory you specified.
  * `prompt-catalog.json`, which contains the index for the prompts found in the directory you specified.  
  If you want to index only the tools in a directory, use the following command:  
  ```console  
  agentc index $PATH_TO_TOOL_OR_PROMPT_DIRECTORY --tools --no-prompts  
  ```  
  If you want to index only the prompts in a directory, use the following command:  
  ```console  
  agentc index $PATH_TO_TOOL_OR_PROMPT_DIRECTORY --prompts --no-tools  
  ```
3. To publish your entire Agent Catalog to your Couchbase cluster, in your command prompt, run the following command:  
```console  
agentc publish --bucket $BUCKET_NAME  
```  
If your cluster has more than 1 bucket and you do not set the `--bucket` flag, the Agent Catalog prompts you to choose a specific bucket.  
If your publish was successful, the Agent Catalog creates a new scope, `agent_catalog`, with the following collections:

  * If you used the `tool` flag:

    * `tool_catalog` for any indexed tools
    * `tool_metadata` for related tool metadata
  * If you used the `prompt` flag:

    * `prompt_catalog` for any indexed prompts
    * `prompt_metadata` for related prompt metadata
  * If you did not use the `tool` or `prompt` flag, the Agent Catalog uploads all catalog and metadata files to their appropriate collections under `agent_catalog`.  
  The Agent Catalog updates this scope and its collections every time you run the `agentc publish` command on your project.

> [!TIP]
> Remember to reindex and publish your tools and prompts as they change in your project.
> 
> If your tools and prompts change after your first index and publish command, you can also set Agent Catalog to automatically index and publish your catalog when you run `git commit` in your project. Add the `--add-hook-for` flag when you run `agentc init` in your project, to install the available Git hooks.
> 
> For example, to automatically index and publish items in the `my-agent` folder while running `git commit`:
> 
> ```console
> agentc init --add-hook-for my-agent
> ```

#### [](#index-and-publish-programmatically-using-the-agentc-cmd-module)Index and Publish Programmatically Using The agentc.cmd Module

You can also use the `agentc` command-line tool programmatically by importing the `agentc.cmd` module, and using the `index` and `publish` methods:

```python
from agentc_cli.cmd import cmd_index, cmd_publish
from agentc_core.config import Config

# Index the directory named tools. Index only tools, not prompts.
cmd_index(
       source_dirs=["tools"],
       kinds=["tools"],
       dry_run=False
)

# Publish the local catalog of tools to the travel-sample bucket on a Couchbase cluster running on localhost.
config = Config(bucket="travel-sample", username="Administrator", password="password", conn_string="localhost")
cmd_publish(
       kind=["tools"]
)
```

### [](#call)Call Tools and Prompts From Your Agent

> [!TIP]
> The code samples in this section are only partial code samples, to show you the specific code you need to add to your own agent. Click **View on GitHub** to view the full example code and view the necessary imports and other information.

To call a tool or prompt from your agent’s code, call the `catalog.find()` method. For example, to search for a tool:

```python
        tool_search = catalog.find("tool", name="search_vector_database")
```

Or, to search for a prompt:

```python
        hotel_prompt = catalog.find("prompt", name="hotel_search_assistant")
```

By default, the Agent Catalog starts the search process for your `.agent_catalog` directory inside the current working directory.

You can search by:

* Using a semantic search against your indexed tools and prompts, through the `query=` parameter if the Search Service is deployed on your cluster. For example:  
```python  
tool_search = catalog.find(kind="tool", query="Find a trip planning tool")  
```
* Using a direct search against your indexed tools and prompts, through the `name=` parameter. For example:  
```python  
my_prompt = catalog.find(kind="prompt", name="summarize_article_instructions")  
# You can also specify a catalog_id value to search a specific version of your catalog  
results = catalog.find(kind="prompt", query="Trip planner", catalog_id="37aa520")  
```

You can adjust the results of either search type with the `limit=` and `annotations=` parameters. You must add a properly formatted `annotations` section to your tool or prompt definition to use the `annotations=` parameter.

For example, after using the `catalog.find()` method example, you could define your tools under a new variable:

```python
        tools = [
            Tool(
                name=tool_search.meta.name,
                description=tool_search.meta.description,
                func=tool_search.func,
            ),
        ]
```

Then, you could add the tools as part of a programmatically created prompt:

```python
        custom_prompt = PromptTemplate(
            template=hotel_prompt.content.strip(),
            input_variables=["input", "agent_scratchpad"],
            partial_variables={
                "tools": "\n".join(
                    [f"{tool.name}: {tool.description}" for tool in tools]
                ),
                "tool_names": ", ".join([tool.name for tool in tools]),
            },
        )
```

To pass the tools and prompts to your agent, you could use the `AgentExecutor` constructor with a defined ReAct agent:

```python
        agent = create_react_agent(llm, tools, custom_prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            handle_parsing_errors=handle_parsing_error,  # Use custom error handler
            max_iterations=2,  # STRICT: 1 tool call + 1 Final Answer only
            early_stopping_method="force",  # Force stop
            return_intermediate_steps=True,  # For better debugging
        )

        return agent_executor, application_span
```

For more information about working with `Catalog` instances and functions in your agent code, see the [agent-catalog documentation](https://couchbaselabs.github.io/agent-catalog/api.html#agentc.catalog.Catalog).

> [!TIP]
> If you want to define your tools so the results of tool calls are logged to the Agent Catalog, see [Log the Results of Tool Calls](agent-tracer/add-spans-callbacks.md#tool-results).

### [](#delete)Clean or Delete Data From Agent Catalog

If you need to:

* Delete a specific version of your Agent Catalog
* Delete local Agent Catalog data
* Delete agent activity data

Use the `agentc clean` command to delete data.

For example, if you wanted to delete all tool, prompt, and metadata entries from the Agent Catalog with versions `GS53S` and `14dFDD`:

```console
agentc clean --catalog-id GS53S -cid 14dFDD
```

`--catalog-id` and `-cid` are equivalent.

You can also specify:

* A specific bucket (`--bucket $BUCKET_NAME`)
* Whether to delete data on your Couchbase cluster (`--db`)
* Whether to delete local data (`--local`)
* Whether to delete only prompts (`--prompts --no-tools`) or only tools (`--tools --no-prompts`)

For more information about the different options for the `agentc clean` command, run `agentc clean --help` or see the [agent-catalog documentation](https://couchbaselabs.github.io/agent-catalog/cli.html#clean-command).

## [](#next-steps)Next Steps

After you have started your agent development and integrated the Agent Catalog, [use the Agent Tracer to monitor agent activity](agent-tracer/agent-tracer.md).