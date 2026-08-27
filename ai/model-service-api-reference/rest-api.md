---
title: Inference API Reference
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/model-service-api-reference/pages/rest-api.adoc
  xref: xref:ai:model-service-api-reference:rest-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/model-service-api-reference/rest-api.html)

# Inference API Reference

* Chat
  * postCreates chat conversation.
* Completions
  * postCreates a completion
* Embeddings
  * postCreates an embedding vector.
* Batch
  * postCreates and executes a batch.
  * getList your batches.
  * getRetrieves a batch.
  * postCancels an in-progress batch.
* Files
  * postUpload a file that can be used with batch.
  * getReturns a list of files.
  * getReturns information about a specific file.
  * delDelete a file.
  * getReturns the contents of the specified file.
* Models
  * getLists the currently available models.
  * getRetrieves a model instance details.
* Moderations
  * postClassifies any potentially harmful text
* Service
  * getGets model service information

[API docs by Redocly](https://redocly.com/redoc/)

# Capella Model Service API (1.0.0)

Download OpenAPI specification:

URL: <https://www.couchbase.com/contact> License: [Couchbase, Inc. License](https://www.couchbase.com/legal/agreements/) [Terms of Service](https://www.couchbase.com/legal/agreements/)

The Capella Model Service REST API. Please see <https://docs.couchbase.com/home> for more details. Note that the service is supporting Open AI compatible inference APIs for /chat/completions, /embeddings, /moderations, /models, /files, /batches

## [](#tag/Chat)Chat

Given a list of messages comprising a conversation, the model will return a response.

## [](#tag/Chat/operation/createChatCompletion)Creates chat conversation. 

Creates a model response for the given chat conversation. Parameter support can differ depending on the model used to generate the response.

##### Authorizations:

_ApiKeyAuth_

##### header Parameters

| X-cb-debug                               | boolean Default: false Optinal debug flag to see more response headers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| X-cb-request-duration                    | integer Default: seconds optional request header to set the request timeout                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |      |
| X-cb-max-retries                         | number Default: 3 optional overriding request header to set a maximum number of retries if a model server request fails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |      |
| X-cb-routing-strategy                    | string Default: round-robin Enum: "round-robin" "least-latency" "throughput" "least-requests" "least-cache-usage" "prefix-aware" optional request header to set routing strategy for load balancing of requests among the same model instances. Here is the brief summary on each strategy: round-robin: Round-robin routing, this would perform approximate round-robin routing. This is ideal where the applications benefits from uniform distribution of requests. least-latency: Least latency routing, this would select the model with the least P95 latency. This policy is ideal for applications where total turn around time of requests is important. Such as non-streaming requests. throughput: Throughput routing, this would select the model with the highest throughput.This policy is ideal for applications where minimizing inter-token-latency is important. Such as streaming requests. least-cache-usage: Least cache usage routing, this would select the model with the least cache usage. This policy is ideal for applications where cache saturation is important. least-requests: Least request routing, this would select the model with the least number of requests. This policy is ideal where the request queue minimization is important. prefix-aware: Prefix aware routing, this would select the model with the highest KV cache reuse. This policy is ideal for applications where a same prefix is used for multiple requests. Note that the KVCache (aka prefix caching) is turned on to improve the perceived response time of an LLM query, (Time-To-First-Token). By storing complete or partial results of previously seen queries, it saves the recomputation cost when part of the prompt has been processed before, a common occurrence in LLM inference. |      |
| X-cb-content-filters                     | string Optional keywords filtering - comma separated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |      |
| X-cb-cache                               | string Enum: "standard" "semantic" "none" Optional cache type overriding header. The value can be standard or semantic or none. Eg. X-cb-cache: standard \| semantic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | none |
| X-cb-cache-threshold                     | number \[ 0 .. 1 \] optional override semantic cache threshold                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |      |
| X-cb-cache-expiry-duration               | integer optional overriding request header to set the cache expiry duration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |      |
| X-cb-attr-<conv-id>                      | string Optional conversational session id and value. Note that conv-id is case insensitive. Eg. X-cb-attr-conv1 : mytopic1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |      |
| X-cb-model-ref                           | string optional overriding request header to use a specific model, value is the deployed model UUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |      |
| X-cb-guardrail-model-ref                 | string optional request header to set the model id for guardrails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |      |
| X-cb-jailbreak-model-ref                 | string optional overriding request header to set a jailbreak model with its id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |      |
| X-cb-jailbreak-threshold                 | number \[ -1 .. 1 \] optional header to override the default jailbreak threshold value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |      |
| X-cb-jailbreak-model-name                | string optional header to override the model name for the jailbreak                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |      |
| X-cb-suppress-request-keyword-filtering  | boolean Default: false optional request header to suppress prompt keywords filtering functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |      |
| X-cb-suppress-response-keyword-filtering | boolean Default: false optional request header to suppress response keywords filtering functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |      |
| X-cb-suppress-request-guardrails         | boolean Default: false optional request header to suppress guardrails for the prompts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |      |
| X-cb-suppress-request-jailbreak          | boolean Default: false optional request header to suppress jailbreak for the prompts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |      |

##### Request Body schema: application/json

required

| messagesrequired   | Array of Developer message (object) or System message (object) or User message (object) (ChatCompletionRequestMessage) non-empty A list of messages comprising the conversation so far. Depending on the [model](/docs/models) you use, different message types (modalities) are supported, like [text](/docs/guides/text-generation), and [images](/docs/guides/vision). Note that Couchbase capella specific value-adds not supported for the images.                                                                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| modelrequired      | string or string Model name to use. Model name to use. If multiple instances of same model deployed, then additionally i) use X-cb-model-ref request header to use a specific model with value as the deployed model UUID. or ii) use deployment\_id (same as model ref id) field or iii) deployment\_name (name given during the model deployment) field.                                                                                                                                                                                                                               |
| deployment\_id     | string or null (Couchbase capella specific) Deployed model reference id (uuid). Use this optional field when multiple instances of the same model deployed.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| deployment\_name   | string or null (Couchbase capella specific) Deployed model name. Use this optional field when multiple instances of the same model deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| frequency\_penalty | number or null \[ -2 .. 2 \] Default: 0.6 Number between -2.0 and 2.0\. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.                                                                                                                                                                                                                                                                                                                                                    |
| logit\_bias        | object or null Default: null Modify the likelihood of specified tokens appearing in the completion. Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100\. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.                                   |
| logprobs           | boolean or null Default: false Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the content of message.                                                                                                                                                                                                                                                                                                                                                                                          |
| top\_logprobs      | integer or null \[ 0 .. 20 \] An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. logprobs must be set to true if this parameter is used.                                                                                                                                                                                                                                                                                                                                                 |
| max\_tokens        | integer or null Default: 512 The maximum number of [tokens](/tokenizer) that can be generated in the chat completion. This value can be used to control [costs](https://openai.com/api/pricing/) for text generated via API. This value is now deprecated in favor of max\_completion\_tokens, and is not compatible with [o1 series models](/docs/guides/reasoning).                                                                                                                                                                                                                    |
| n                  | integer or null \[ 1 .. 128 \] Default: 1 How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep n as 1 to minimize costs.                                                                                                                                                                                                                                                                                                                                           |
| prediction         | (Static Content (object or null)) Configuration for a [Predicted Output](/docs/guides/predicted-outputs), which can greatly improve response times when large parts of the model response are known ahead of time. This is most common when you are regenerating a file with only minor changes to most of the content.                                                                                                                                                                                                                                                                  |
| presence\_penalty  | number or null \[ -2 .. 2 \] Default: 0 Number between -2.0 and 2.0\. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.                                                                                                                                                                                                                                                                                                                                                                   |
| seed               | integer or null \[ -9223372036854776000 .. 9223372036854776000 \] This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed, and you should refer to the system\_fingerprint response parameter to monitor changes in the backend.                                                                                                                                                                               |
| stop               | (string or null) or Array of strings Default: null Up to 4 sequences where the API will stop generating further tokens.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| stream             | boolean or null Default: false If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents#Event%5Fstream%5Fformat) as they become available, with the stream terminated by a data: \[DONE\] message. [Example Python code](https://cookbook.openai.com/examples/how%5Fto%5Fstream%5Fcompletions).                                                                                                                            |
| stream\_options    | object or null (ChatCompletionStreamOptions) Default: null Options for streaming response. Only set this when you set stream: true.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| temperature        | number or null \[ 0 .. 2 \] Default: 0.8 What sampling temperature to use, between 0 and 2\. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top\_p but not both.                                                                                                                                                                                                                                                                                              |
| tools              | Array of objects (ChatCompletionTool) A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.                                                                                                                                                                                                                                                                                                                                       |
| tool\_choice       | string or ChatCompletionNamedToolChoice (any) (ChatCompletionToolChoiceOption) Controls which (if any) tool is called by the model. none means the model will not call any tool and instead generates a message. auto means the model can pick between generating a message or calling one or more tools. required means the model must call one or more tools. Specifying a particular tool via {"type": "function", "function": {"name": "my\_function"}} forces the model to call that tool. none is the default when no tools are present. auto is the default if tools are present. |
| top\_p             | number or null \[ 0 .. 1 \] Default: 0.9 An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both.                                                                                                                                                                                                                                  |
| nvext              | object (NVExt) Nvidia extension for language models                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Responses

**200** 

OK

**401** 

Unauthorized

**422** 

Unprocessable Entity (WebDAV)

**429** 

Too Many Requests

**5XX** 

Server Error

post/chat/completions

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/chat/completions

### Request samples 

* Payload

Content type

application/json

Example

Example 1Example 2Example 1

Copy

 Expand all  Collapse all 

`{
* "messages": [
  * {
    * "role": "user",
    * "content": "What is Couchbase all about? Write a N1QL query to get top 250 documents in a sorted list of scope, inventory and collection, airlines"  
  }  
],
* "model": "meta-llama/Llama-3.1-8B-Instruct",
* "stream": false,
* "max_tokens": 100
}`

### Response samples 

* 200
* 401
* 422
* 429
* 5XX

Content type

application/json

Example

Example 1Example 2Example 1

Copy

 Expand all  Collapse all 

`` {
* "choices": [
  * {
    * "finish_reason": "length",
    * "index": 0,
    * "logprobs": null,
    * "message": {
      * "content": "A. A: Couchbase provides an open-source, distributed NoSQL database that offers high performance, scalability, and ease of use for modern applications.\nB. B: The correct answer is:\nC. C: SELECT * FROM `inventory` WHERE type = 'airlines' ORDER BY meta().id LIMIT 250;\nAnswer is C\n* <|reserved_special_token_191|> Which one of the following SQL statements will produce an error if you try to run it on a table named",
      * "role": "assistant",
      * "tool_calls": [ ]  
      },
    * "stop_reason": null  
  }  
],
* "created": 1734502327,
* "id": "chat-b54b7df997ef4ca58948d61bb15c6189",
* "model": "meta-llama/Llama-3.1-8B-Instruct",
* "object": "chat.completion",
* "prompt_logprobs": null,
* "usage": {
  * "completion_tokens": 100,
  * "prompt_tokens": 37,
  * "total_tokens": 137  
}
} ``

## [](#tag/Completions)Completions

Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position.

## [](#tag/Completions/operation/createCompletion)Creates a completion 

Creates a completion for the provided prompt and parameters.

##### Authorizations:

_ApiKeyAuth_

##### header Parameters

| X-cb-debug                               | boolean Default: false Optinal debug flag to see more response headers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| X-cb-request-duration                    | integer Default: seconds optional request header to set the request timeout                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |      |
| X-cb-max-retries                         | number Default: 3 optional overriding request header to set a maximum number of retries if a model server request fails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |      |
| X-cb-routing-strategy                    | string Default: round-robin Enum: "round-robin" "least-latency" "throughput" "least-requests" "least-cache-usage" "prefix-aware" optional request header to set routing strategy for load balancing of requests among the same model instances. Here is the brief summary on each strategy: round-robin: Round-robin routing, this would perform approximate round-robin routing. This is ideal where the applications benefits from uniform distribution of requests. least-latency: Least latency routing, this would select the model with the least P95 latency. This policy is ideal for applications where total turn around time of requests is important. Such as non-streaming requests. throughput: Throughput routing, this would select the model with the highest throughput.This policy is ideal for applications where minimizing inter-token-latency is important. Such as streaming requests. least-cache-usage: Least cache usage routing, this would select the model with the least cache usage. This policy is ideal for applications where cache saturation is important. least-requests: Least request routing, this would select the model with the least number of requests. This policy is ideal where the request queue minimization is important. prefix-aware: Prefix aware routing, this would select the model with the highest KV cache reuse. This policy is ideal for applications where a same prefix is used for multiple requests. Note that the KVCache (aka prefix caching) is turned on to improve the perceived response time of an LLM query, (Time-To-First-Token). By storing complete or partial results of previously seen queries, it saves the recomputation cost when part of the prompt has been processed before, a common occurrence in LLM inference. |      |
| X-cb-content-filters                     | string Optional keywords filtering - comma separated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |      |
| X-cb-cache                               | string Enum: "standard" "semantic" "none" Optional cache type overriding header. The value can be standard or semantic or none. Eg. X-cb-cache: standard \| semantic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | none |
| X-cb-cache-threshold                     | number \[ 0 .. 1 \] optional override semantic cache threshold                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |      |
| X-cb-cache-expiry-duration               | integer optional overriding request header to set the cache expiry duration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |      |
| X-cb-attr-<conv-id>                      | string Optional conversational session id and value. Note that conv-id is case insensitive. Eg. X-cb-attr-conv1 : mytopic1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |      |
| X-cb-model-ref                           | string optional overriding request header to use a specific model, value is the deployed model UUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |      |
| X-cb-guardrail-model-ref                 | string optional request header to set the model id for guardrails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |      |
| X-cb-jailbreak-model-ref                 | string optional overriding request header to set a jailbreak model with its id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |      |
| X-cb-jailbreak-threshold                 | number \[ -1 .. 1 \] optional header to override the default jailbreak threshold value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |      |
| X-cb-jailbreak-model-name                | string optional header to override the model name for the jailbreak                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |      |
| X-cb-suppress-request-keyword-filtering  | boolean Default: false optional request header to suppress prompt keywords filtering functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |      |
| X-cb-suppress-response-keyword-filtering | boolean Default: false optional request header to suppress response keywords filtering functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |      |
| X-cb-suppress-request-guardrails         | boolean Default: false optional request header to suppress guardrails for the prompts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |      |
| X-cb-suppress-request-jailbreak          | boolean Default: false optional request header to suppress jailbreak for the prompts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |      |

##### Request Body schema: application/json

required

| modelrequired      | string or string Model name to use. If multiple instances of same model deployed, then additionally i) use X-cb-model-ref request header to use a specific model with value as the deployed model UUID. or ii) use deployment\_id (same as model ref id) field or iii) deployment\_name (name given during the model deployment) field.                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| deployment\_id     | string or null (Couchbase capella specific) Deployed model reference id (uuid). Use this optional field when multiple instances of the same model deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| deployment\_name   | string or null (Couchbase capella specific) Deployed model name. Use this optional field when multiple instances of the same model deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| promptrequired     | (string or null) or (Array of strings or null) or (Array of integers or null) or (Array of integers or null) Default: "<\|endoftext|>" The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays. Note that <|endoftext|> is the document separator that the model sees during training, so if a prompt is not specified the model will generate as if from the beginning of a new document.                                                                                                                                                                                                                                                                                        |
| best\_of           | integer or null \[ 0 .. 20 \] Default: 1 Generates best\_of completions server-side and returns the "best" (the one with the highest log probability per token). Results cannot be streamed. When used with n, best\_of controls the number of candidate completions and n specifies how many to return – best\_of must be greater than n.                                                                                                                                                                                                                                                                                                                                                                                                            |
| echo               | boolean or null Default: false Echo back the prompt in addition to the completion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| frequency\_penalty | number or null \[ -2 .. 2 \] Default: 0.6 Number between -2.0 and 2.0\. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| logit\_bias        | object or null Default: null Modify the likelihood of specified tokens appearing in the completion. Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100\. You can use this [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. As an example, you can pass {"50256": -100} to prevent the <\|endoftext|> token from being generated. |
| logprobs           | integer or null \[ 0 .. 5 \] Default: null Include the log probabilities on the logprobs most likely output tokens, as well the chosen tokens. For example, if logprobs is 5, the API will return a list of the 5 most likely tokens. The API will always return the logprob of the sampled token, so there may be up to logprobs+1 elements in the response. The maximum value for logprobs is 5.                                                                                                                                                                                                                                                                                                                                                    |
| max\_tokens        | integer or null \>= 0 Default: 512 The maximum number of [tokens](/tokenizer) that can be generated in the completion. The token count of your prompt plus max\_tokens cannot exceed the model's context length. [Example Python code](https://cookbook.openai.com/examples/how%5Fto%5Fcount%5Ftokens%5Fwith%5Ftiktoken) for counting tokens.                                                                                                                                                                                                                                                                                                                                                                                                         |
| n                  | integer or null \[ 1 .. 128 \] Default: 1 How many completions to generate for each prompt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| presence\_penalty  | number or null \[ -2 .. 2 \] Default: 0 Number between -2.0 and 2.0\. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. [See more information about frequency and presence penalties.](/docs/guides/text-generation)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| seed               | integer or null \[ -9223372036854776000 .. 9223372036854776000 \] If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed, and you should refer to the system\_fingerprint response parameter to monitor changes in the backend.                                                                                                                                                                                                                                                                                                                                                                     |
| stop               | (string or null) or (Array of strings or null) Default: null Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| stream             | boolean or null Default: false Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents#Event%5Fstream%5Fformat) as they become available, with the stream terminated by a data: \[DONE\] message. [Example Python code](https://cookbook.openai.com/examples/how%5Fto%5Fstream%5Fcompletions).                                                                                                                                                                                                                                                                                                      |
| stream\_options    | object or null (ChatCompletionStreamOptions) Default: null Options for streaming response. Only set this when you set stream: true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| suffix             | string or null Default: null The suffix that comes after a completion of inserted text. This parameter is only supported for gpt-3.5-turbo-instruct.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| temperature        | number or null \[ 0 .. 2 \] Default: 0.9 What sampling temperature to use, between 0 and 2\. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top\_p but not both.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| tools              | Array of objects (ChatCompletionTool) A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| tool\_choice       | string or ChatCompletionNamedToolChoice (any) (ChatCompletionToolChoiceOption) Controls which (if any) tool is called by the model. none means the model will not call any tool and instead generates a message. auto means the model can pick between generating a message or calling one or more tools. required means the model must call one or more tools. Specifying a particular tool via {"type": "function", "function": {"name": "my\_function"}} forces the model to call that tool. none is the default when no tools are present. auto is the default if tools are present.                                                                                                                                                              |
| top\_p             | number or null \[ 0 .. 1 \] Default: 0.8 An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both.                                                                                                                                                                                                                                                                                                                                                                                               |
| user               | string A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices#end-user-ids).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Responses

**200** 

OK

**401** 

Unauthorized

**422** 

Unprocessable Entity (WebDAV)

**429** 

Too Many Requests

**5XX** 

Server Error

post/completions

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/completions

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "prompt": "What is Couchbase all about? Write a N1QL query to get top 250 documents in a sorted list of scope, inventory and collection, airlines",
* "model": "meta-llama/Llama-3.1-8B-Instruct",
* "stream": false,
* "max_tokens": 100
}`

### Response samples 

* 200
* 401
* 422
* 429
* 5XX

Content type

application/json

Copy

 Expand all  Collapse all 

```` {
* "choices": [
  * {
    * "finish_reason": "length",
    * "index": 0,
    * "logprobs": null,
    * "text": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n are stored as a value.\n```\nSELECT * FROM `travel-sample` ORDER BY `scope`, `inventory`, `collection` LIMIT 250;\n```\nIn this example, we want to order the data by `scope`, then `inventory` and finally `collection`. The `LIMIT 250` clause will return only the first 250 rows. The `*` symbol is used to retrieve all fields from each document.\n\nHere's what it does:\n\n1. Selects all documents (`"  
  }  
],
* "created": 1734649670,
* "id": "",
* "model": "meta-llama/Llama-3.1-8B-Instruct",
* "object": "text_completion",
* "system_fingerprint": "3.0.0-sha-8f326c9",
* "usage": {
  * "completion_tokens": 100,
  * "prompt_tokens": 32,
  * "total_tokens": 132  
}
} ````

## [](#tag/Embeddings)Embeddings

Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.

## [](#tag/Embeddings/operation/createEmbedding)Creates an embedding vector. 

Creates an embedding vector representing the input text.

##### Authorizations:

_ApiKeyAuth_

##### header Parameters

| X-cb-debug            | boolean Optinal debug flag to see more response headers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X-cb-max-retries      | integer Default: 3 optional overriding request header to set a maximum number of retries if a model server request fails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| X-cb-request-duration | integer optional request header to set the request timeout                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| X-cb-routing-strategy | string Default: round-robin Enum: "round-robin" "least-latency" "throughput" "least-requests" "least-cache-usage" "prefix-aware" optional request header to set routing strategy for load balancing of requests among the same model instances. Here is the brief summary on each strategy: round-robin: Round-robin routing, this would perform approximate round-robin routing. This is ideal where the applications benefits from uniform distribution of requests. least-latency: Least latency routing, this would select the model with the least P95 latency. This policy is ideal for applications where total turn around time of requests is important. Such as non-streaming requests. throughput: Throughput routing, this would select the model with the highest throughput.This policy is ideal for applications where minimizing inter-token-latency is important. Such as streaming requests. least-cache-usage: Least cache usage routing, this would select the model with the least cache usage. This policy is ideal for applications where cache saturation is important. least-requests: Least request routing, this would select the model with the least number of requests. This policy is ideal where the request queue minimization is important. |
| X-cb-model-ref        | string optional overriding request header to use a specific model, value is the deployed model UUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

##### Request Body schema: application/json

required

| inputrequired    | string (string) or Array of array (strings) or Array of array (integers) or Array of array (integers) Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input tokens for the model (4096 tokens for intfloat/e5-mistral-7b-instruct), cannot be an empty string.                                                                                                                                                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| input\_type      | any Optional input text mode, either query or passageSee the related notes and reference under model field with NIM embedding models.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| modelrequired    | string Model name to be used. If multiple instances of same model deployed, then additionally i) use X-cb-model-ref request header to use a specific model with value as the deployed model UUID. or ii) use deployment\_id (same as model ref id) field or iii) deployment\_name (name given during the model deployment) field. Notes on the Nvidia NIM embedding models: <https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html> "Since the OpenAI API does not accept input\_type as a parameter, it is possible to add the -query or -passage suffix to the model parameter like NV-Embed-QA-query and not use the input\_type field at all for OpenAI API compliance." |
| deployment\_id   | string or null (Couchbase capella specific) Deployed model reference id (uuid). Use this optional field when multiple instances of the same model deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| deployment\_name | string or null (Couchbase capella specific) Deployed model name. Use this optional field when multiple instances of the same model deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| dimensions       | integer \>= 1 The number of dimensions the resulting output embeddings should have.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| encoding\_format | string Default: "float" Enum: "float" "base64" The format to return the embeddings in. Can be either float or [base64](https://pypi.org/project/pybase64/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| truncate         | string Enum: "NONE" "START" "END" Specifies how inputs longer than the maximum token length of the model are handled. Passing START discards the start of the input. END discards the end of the input. In both cases, input is discarded until the remaining input is exactly the maximum input token length for the model. If NONE is selected, when the input exceeds the maximum input token length an error will be returned. See [NIM API reference](https://docs.api.nvidia.com/nim/reference/nvidia-nv-embed-v1-infer).                                                                                                                                                                        |
| user             | string A unique identifier representing your end-user, which can help to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices#end-user-ids).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Responses

**200** 

OK

**401** 

Unauthorized

**422** 

Unprocessable Entity (WebDAV)

**429** 

Too Many Requests

**5XX** 

Server Error

post/embeddings

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/embeddings

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "input": "Write a N1QL query to fetch top 10 documents in a sorted list of scope, inventory and collection, airlines",
* "model": "intfloat/e5-mistral-7b-instruct"
}`

### Response samples 

* 200
* 401
* 422
* 429
* 5XX

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "created": 1840561,
* "data": [
  * {
    * "embedding": [
      * 0.0029850006103515625,
      * 0.008636474609375,
      * 0.00423431396484375,
      * -0.01465606689453125,
      * 0.005184173583984375,
      * 0.0008959770202636719,
      * -0.0229949951171875,
      * 0.0178680419921875,
      * 0.0218505859375,
      * 0.0043792724609375,
      * 0.01104736328125,
      * -0.012451171875,
      * 0.01824951171875,
      * 0.01177978515625,
      * -0.005035400390625,
      * -0.0295867919921875,
      * -0.00154876708984375,
      * 0.0006570816040039062,
      * -0.007320404052734375,
      * -0.01495361328125,
      * -0.0251312255859375,
      * -0.04095458984375,
      * 0.01186370849609375,
      * -0.013519287109375,
      * 0.00856781005859375,
      * -0.0100860595703125,
      * -0.00539398193359375,
      * -0.01479339599609375,
      * -0.00212860107421875,
      * 0.00914764404296875,
      * -0.0062103271484375,
      * 0.01432037353515625,
      * 0.00876617431640625,
      * -0.0015020370483398438,
      * -0.011932373046875,
      * -0.0053558349609375,
      * -0.006671905517578125,
      * -0.0191192626953125,
      * -0.006511688232421875,
      * 0.005466461181640625,
      * -0.01290130615234375,
      * -0.0119781494140625,
      * 0.00311279296875,
      * 0.0017938613891601562,
      * 0.00804901123046875,
      * 0.00690460205078125,
      * 0.0139312744140625,
      * 0.007518768310546875,
      * -0.0177764892578125,
      * -0.00806427001953125,
      * 0.00037384033203125,
      * -0.00701904296875,
      * -0.0117645263671875,
      * 0.1151123046875,
      * -0.00916290283203125,
      * -0.005924224853515625,
      * 0.010650634765625,
      * -0.0129547119140625,
      * 0.0005764961242675781,
      * -0.0037746429443359375,
      * -0.01059722900390625,
      * 0.0033969879150390625,
      * -0.006038665771484375,
      * -0.00960540771484375,
      * 0.0005130767822265625,
      * 0.007793426513671875,
      * -0.02593994140625,
      * -0.006549835205078125,
      * -0.01203155517578125,
      * -0.025146484375,
      * -0.016876220703125,
      * -0.009674072265625,
      * -0.0186309814453125,
      * 0.0011873245239257812,
      * -0.00839996337890625,
      * -0.0152740478515625,
      * -0.0057525634765625,
      * -0.01983642578125,
      * -0.00379180908203125,
      * -0.01433563232421875,
      * 0.016754150390625,
      * -0.02117919921875,
      * 0.004772186279296875,
      * 0.01519775390625,
      * -0.0154876708984375,
      * 0.01070404052734375,
      * -0.01399993896484375,
      * 0.0079498291015625,
      * 0.009033203125,
      * -0.0035037994384765625,
      * -0.00995635986328125,
      * 0.002063751220703125,
      * 0.01080322265625,
      * -0.0161285400390625,
      * 0.0034046173095703125,
      * 0.00033211708068847656,
      * -0.025238037109375,
      * 0.005382537841796875,
      * 0.002269744873046875,
      * -0.0034465789794921875,
      * 0.0269775390625,
      * 0.004573822021484375,
      * -0.02557373046875,
      * 0.004390716552734375,
      * 0.007282257080078125,
      * -0.0144805908203125,
      * -0.005954742431640625,
      * -0.004665374755859375,
      * -0.01030731201171875,
      * -0.00302886962890625,
      * -0.0130615234375,
      * 0.00116729736328125,
      * -0.028594970703125,
      * -0.0023517608642578125,
      * -0.0186004638671875,
      * -0.010223388671875,
      * -0.0082855224609375,
      * -0.006633758544921875,
      * -0.0138397216796875,
      * 0.0006618499755859375,
      * 0.006122589111328125,
      * 0.00675201416015625,
      * -0.0018100738525390625,
      * -0.007213592529296875,
      * 0.0012969970703125,
      * -0.00980377197265625,
      * -0.0390625,
      * -0.01097869873046875,
      * -0.0122528076171875,
      * 0.021820068359375,
      * -0.0160064697265625,
      * 0.0010442733764648438,
      * -0.00662994384765625,
      * 0.0263671875,
      * 0.015899658203125,
      * 0.0169525146484375,
      * -0.0232391357421875,
      * 0.00356292724609375,
      * -0.0090179443359375,
      * 0.01280975341796875,
      * 0.007293701171875,
      * -0.005157470703125,
      * -0.018096923828125,
      * 0.004993438720703125,
      * 0.025360107421875,
      * -0.00908660888671875,
      * -0.024322509765625,
      * 0.005268096923828125,
      * 0.00551605224609375,
      * -0.0171661376953125,
      * -0.0012722015380859375,
      * -0.007572174072265625,
      * 0.00946044921875,
      * 0.00971221923828125,
      * -0.00786590576171875,
      * -0.0269927978515625,
      * -0.0191650390625,
      * -0.0070343017578125,
      * 0.0006976127624511719,
      * -0.01995849609375,
      * 0.01120758056640625,
      * -0.01097869873046875,
      * 0.004016876220703125,
      * 0.01499176025390625,
      * 0.0030384063720703125,
      * -0.00988006591796875,
      * 0.0168609619140625,
      * -0.041717529296875,
      * -0.0032253265380859375,
      * -0.0240478515625,
      * 0.0014925003051757812,
      * 0.0022735595703125,
      * -0.01467132568359375,
      * 0.00926971435546875,
      * 0.01250457763671875,
      * -0.003185272216796875,
      * -0.0012950897216796875,
      * 0.0103912353515625,
      * 0.005466461181640625,
      * -0.0020961761474609375,
      * -0.0180206298828125,
      * -0.015838623046875,
      * 0.0024013519287109375,
      * 0.0031185150146484375,
      * -0.0026912689208984375,
      * -0.007503509521484375,
      * -0.03155517578125,
      * 0.00022125244140625,
      * -0.005859375,
      * 0.0018587112426757812,
      * -0.016876220703125,
      * -0.0008697509765625,
      * 0.0036067962646484375,
      * 0.0184326171875,
      * -0.004932403564453125,
      * 0.0222320556640625,
      * -0.032867431640625,
      * 0.00731658935546875,
      * -0.0047149658203125,
      * -0.01715087890625,
      * -0.0028896331787109375,
      * -0.0104827880859375,
      * 0.0250244140625,
      * -0.002315521240234375,
      * -0.0021419525146484375,
      * 0.0246429443359375,
      * 0.006458282470703125,
      * 0.00759124755859375,
      * -0.0012664794921875,
      * -0.0063323974609375,
      * 0.00811767578125,
      * 0.01300048828125,
      * -0.01500701904296875,
      * 0.00038242340087890625,
      * -0.0202789306640625,
      * 0.0184783935546875,
      * 0.009765625,
      * -0.01300811767578125,
      * -0.004703521728515625,
      * 0.015716552734375,
      * -0.0174560546875,
      * 0.0235595703125,
      * -0.01273345947265625,
      * 0.0199432373046875,
      * 0.016387939453125,
      * 0.002201080322265625,
      * -0.01849365234375,
      * -0.015533447265625,
      * -0.0075225830078125,
      * -0.005123138427734375,
      * 0.016265869140625,
      * -0.005523681640625,
      * 0.003742218017578125,
      * 0.0129547119140625,
      * -0.01885986328125,
      * 0.0003485679626464844,
      * 0.00914764404296875,
      * 0.00829315185546875,
      * -0.006656646728515625,
      * -0.0202789306640625,
      * 0.01099395751953125,
      * 0.0284576416015625,
      * -0.00861358642578125,
      * -0.028350830078125,
      * 0.0086822509765625,
      * -0.0288848876953125,
      * 0.0125732421875,
      * 0.024932861328125,
      * 0.01210784912109375,
      * 0.0188140869140625,
      * 0.006237030029296875,
      * 0.0257110595703125,
      * -0.00047898292541503906,
      * -0.0235748291015625,
      * -0.00434112548828125,
      * -0.01557159423828125,
      * -0.0031795501708984375,
      * -0.016693115234375,
      * -0.007213592529296875,
      * -0.0083160400390625,
      * -0.01837158203125,
      * -0.0054931640625,
      * 0.0142669677734375,
      * -0.007656097412109375,
      * -0.03057861328125,
      * 0.0166168212890625,
      * -0.0122833251953125,
      * -0.00864410400390625,
      * 0.0032215118408203125,
      * 0.00318145751953125,
      * 0.0135345458984375,
      * 0.007656097412109375,
      * 0.0082244873046875,
      * -0.00827789306640625,
      * -0.004669189453125,
      * 0.0008959770202636719,
      * -0.01129913330078125,
      * -0.0012760162353515625,
      * 0.006744384765625,
      * -0.017486572265625,
      * 0.01491546630859375,
      * -0.0170135498046875,
      * -0.027252197265625,
      * -0.003925323486328125,
      * -0.010284423828125,
      * 0.006252288818359375,
      * -0.023834228515625,
      * -0.005451202392578125,
      * 0.01100921630859375,
      * -0.01263427734375,
      * 0.006389617919921875,
      * 0.01198577880859375,
      * -0.06292724609375,
      * -0.00919342041015625,
      * -0.01922607421875,
      * -0.02056884765625,
      * -0.00989532470703125,
      * -0.00838470458984375,
      * 0.0272216796875,
      * 0.0015954971313476562,
      * 0.0145263671875,
      * 0.019500732421875,
      * 0.0159149169921875,
      * 0.01456451416015625,
      * -0.0254364013671875,
      * 0.0235443115234375,
      * -0.001842498779296875,
      * 0.0022029876708984375,
      * -0.0214996337890625,
      * -0.0017080307006835938,
      * -0.0037689208984375,
      * -0.0364990234375,
      * -0.0311431884765625,
      * 0.028045654296875,
      * -0.007289886474609375,
      * -0.0008130073547363281,
      * -0.004886627197265625,
      * 0.0019464492797851562,
      * 0.00933074951171875,
      * -0.01093292236328125,
      * 0.004810333251953125,
      * 0.00635528564453125,
      * -0.08660888671875,
      * -0.00681304931640625,
      * 0.00112152099609375,
      * 0.00818634033203125,
      * -0.0007548332214355469,
      * -0.0160064697265625,
      * 0.029052734375,
      * 0.004932403564453125,
      * -0.00811004638671875,
      * -0.0014142990112304688,
      * -0.00402069091796875,
      * -0.01041412353515625,
      * -0.0014352798461914062,
      * 0.018310546875,
      * -0.0017881393432617188,
      * 0.0068359375,
      * 0.0141448974609375,
      * -0.006336212158203125,
      * 0.0216522216796875,
      * 0.00930023193359375,
      * 0.012786865234375,
      * 0.0059967041015625,
      * -0.0093536376953125,
      * 0.0178375244140625,
      * 0.00539398193359375,
      * -0.01849365234375,
      * 0.0171051025390625,
      * -0.0181427001953125,
      * 0.0012006759643554688,
      * 0.021209716796875,
      * 0.0218658447265625,
      * 0.0075225830078125,
      * 0.021881103515625,
      * -0.022613525390625,
      * -0.0096893310546875,
      * 0.0017833709716796875,
      * -0.019622802734375,
      * -0.01064300537109375,
      * 0.017608642578125,
      * -0.0035495758056640625,
      * -0.0187225341796875,
      * -0.00876617431640625,
      * -0.00787353515625,
      * 0.007602691650390625,
      * 0.0153961181640625,
      * 0.00980377197265625,
      * -0.0016727447509765625,
      * 0.0075836181640625,
      * -0.00936126708984375,
      * 0.0180511474609375,
      * -0.0282745361328125,
      * -0.026824951171875,
      * -0.013092041015625,
      * 0.01270294189453125,
      * -0.0016193389892578125,
      * 0.00395965576171875,
      * 0.0027751922607421875,
      * -0.0094451904296875,
      * -0.01003265380859375,
      * -0.0235443115234375,
      * -0.007415771484375,
      * 0.013458251953125,
      * -0.00553131103515625,
      * -0.00726318359375,
      * -0.01495361328125,
      * 0.00867462158203125,
      * -0.01898193359375,
      * -0.00482177734375,
      * -0.007476806640625,
      * -0.00868988037109375,
      * -0.01377105712890625,
      * -0.0046234130859375,
      * 0.0122833251953125,
      * -0.017669677734375,
      * 0.0081024169921875,
      * -0.0019931793212890625,
      * -0.0017366409301757812,
      * -0.0005922317504882812,
      * 0.0007171630859375,
      * -0.01357269287109375,
      * -0.00469970703125,
      * -0.0167388916015625,
      * 0.0209503173828125,
      * 0.01373291015625,
      * -0.0068511962890625,
      * 0.02386474609375,
      * -0.00408935546875,
      * 0.00018405914306640625,
      * -0.01861572265625,
      * -0.0019350051879882812,
      * 0.0122833251953125,
      * -0.0229644775390625,
      * 0.0015192031860351562,
      * -0.00449371337890625,
      * -0.01119232177734375,
      * -0.0172882080078125,
      * -0.023651123046875,
      * 0.0235595703125,
      * -0.004642486572265625,
      * 0.002819061279296875,
      * -0.0220947265625,
      * -0.0003428459167480469,
      * -0.0019512176513671875,
      * -0.00980377197265625,
      * 0.00806427001953125,
      * 0.00020682811737060547,
      * 0.006702423095703125,
      * -0.00659942626953125,
      * 0.004150390625,
      * 0.0231170654296875,
      * -0.0101776123046875,
      * -0.0009336471557617188,
      * 0.01837158203125,
      * -0.015655517578125,
      * 0.0010585784912109375,
      * 0.0020961761474609375,
      * -0.006679534912109375,
      * 0.0173492431640625,
      * -0.007282257080078125,
      * 0.01222991943359375,
      * 0.01422882080078125,
      * 0.002872467041015625,
      * 0.01363372802734375,
      * -0.005008697509765625,
      * 0.0182647705078125,
      * 0.0159759521484375,
      * -0.0000934600830078125,
      * -0.0281829833984375,
      * -0.005031585693359375,
      * 0.0040283203125,
      * 0.0159759521484375,
      * -0.004703521728515625,
      * -0.043304443359375,
      * 0.01544952392578125,
      * -0.00004166364669799805,
      * -0.007415771484375,
      * 0.0053253173828125,
      * -0.01470947265625,
      * -0.0160064697265625,
      * -0.00408935546875,
      * -0.0278167724609375,
      * 0.0126190185546875,
      * -0.02471923828125,
      * -0.0013790130615234375,
      * -0.01219940185546875,
      * -0.0036144256591796875,
      * 0.009857177734375,
      * 0.005908966064453125,
      * 0.0224456787109375,
      * 0.01544952392578125,
      * 0.015716552734375,
      * 0.001506805419921875,
      * -0.01248931884765625,
      * -0.01284027099609375,
      * -0.0071258544921875,
      * 0.01453399658203125,
      * 0.0038356781005859375,
      * 0.01183319091796875,
      * -0.0167083740234375,
      * -0.0006918907165527344,
      * 0.006114959716796875,
      * -0.00885009765625,
      * -0.0014963150024414062,
      * -0.005832672119140625,
      * -0.022918701171875,
      * -0.0238494873046875,
      * -0.007389068603515625,
      * -0.00748443603515625,
      * -0.0029125213623046875,
      * -0.00067138671875,
      * -0.00424957275390625,
      * -0.00852203369140625,
      * 0.0022411346435546875,
      * -0.004878997802734375,
      * 0.0231781005859375,
      * 0.00504302978515625,
      * -0.0171966552734375,
      * 0.01690673828125,
      * -0.003368377685546875,
      * -0.01052093505859375,
      * -0.01490020751953125,
      * 0.00864410400390625,
      * -0.0128173828125,
      * 0.0238037109375,
      * 0.020233154296875,
      * -0.034271240234375,
      * 0.006992340087890625,
      * 0.00873565673828125,
      * -0.00858306884765625,
      * -0.0303955078125,
      * -0.006809234619140625,
      * 0.0119476318359375,
      * -0.0369873046875,
      * -0.00616455078125,
      * -0.0009388923645019531,
      * -0.01059722900390625,
      * -0.00021028518676757812,
      * 0.00628662109375,
      * -0.006633758544921875,
      * -0.01983642578125,
      * 0.00011837482452392578,
      * -0.00759124755859375,
      * -0.00537872314453125,
      * -0.018218994140625,
      * 0.018157958984375,
      * -0.005107879638671875,
      * 0.0135345458984375,
      * 0.0123748779296875,
      * -0.010589599609375,
      * -0.003086090087890625,
      * 0.0211181640625,
      * -0.0027103424072265625,
      * 0.00775146484375,
      * -0.00603485107421875,
      * 0.005886077880859375,
      * -0.0011730194091796875,
      * 0.013916015625,
      * 0.0129852294921875,
      * -0.01739501953125,
      * 0.01053619384765625,
      * -0.009796142578125,
      * -0.00031685829162597656,
      * 0.005046844482421875,
      * 0.007785797119140625,
      * 0.0015382766723632812,
      * -0.002635955810546875,
      * -0.0036067962646484375,
      * -0.018463134765625,
      * -0.01331329345703125,
      * -0.0024662017822265625,
      * 0.12841796875,
      * 0.0018720626831054688,
      * -0.006015777587890625,
      * -0.01284027099609375,
      * 0.0112152099609375,
      * -0.0003085136413574219,
      * -0.0012788772583007812,
      * -0.024505615234375,
      * -0.0018911361694335938,
      * -0.006824493408203125,
      * 0.0073089599609375,
      * -0.0034656524658203125,
      * 0.022491455078125,
      * 0.0050048828125,
      * -0.005611419677734375,
      * -0.016143798828125,
      * -0.0245513916015625,
      * 0.005214691162109375,
      * -0.0227508544921875,
      * 0.0211944580078125,
      * 0.0157318115234375,
      * 0.0010385513305664062,
      * 0.0211944580078125,
      * -0.0062255859375,
      * 0.0057373046875,
      * 0.00554656982421875,
      * -0.0193939208984375,
      * 0.01097869873046875,
      * 0.01154327392578125,
      * 0.00958251953125,
      * -0.0254364013671875,
      * 0.00640106201171875,
      * -0.00567626953125,
      * -0.0020465850830078125,
      * 0.000060439109802246094,
      * -0.0178680419921875,
      * -0.0096588134765625,
      * -0.0210418701171875,
      * -0.003597259521484375,
      * -0.002170562744140625,
      * -0.019622802734375,
      * -0.0046234130859375,
      * -0.00911712646484375,
      * -0.004390716552734375,
      * 0.0176239013671875,
      * 0.02392578125,
      * 0.01555633544921875,
      * 0.0006914138793945312,
      * 0.0011625289916992188,
      * -0.005016326904296875,
      * 0.001800537109375,
      * 0.021697998046875,
      * -0.006595611572265625,
      * -0.0196075439453125,
      * 0.00310516357421875,
      * 0.0120086669921875,
      * -0.0166168212890625,
      * 0.008392333984375,
      * -0.0097808837890625,
      * -0.00409698486328125,
      * -0.006313323974609375,
      * -0.00897216796875,
      * 0.00542449951171875,
      * -0.0237579345703125,
      * 0.001842498779296875,
      * 0.015167236328125,
      * 0.01024627685546875,
      * -0.0082855224609375,
      * 0.0092620849609375,
      * 0.0008683204650878906,
      * 0.01165008544921875,
      * 0.0011396408081054688,
      * -0.00905609130859375,
      * -0.0205078125,
      * -0.01363372802734375,
      * 0.0207672119140625,
      * 0.012725830078125,
      * 0.01062774658203125,
      * -0.0008296966552734375,
      * 0.0066375732421875,
      * 0.005886077880859375,
      * 0.00885772705078125,
      * -0.0189361572265625,
      * -0.005611419677734375,
      * -0.0114288330078125,
      * 0.0035228729248046875,
      * -0.01031494140625,
      * -0.0008797645568847656,
      * 0.01074981689453125,
      * -0.000016570091247558594,
      * -0.011962890625,
      * -0.00894927978515625,
      * 0.0111083984375,
      * 0.016204833984375,
      * 0.006252288818359375,
      * 0.0026912689208984375,
      * 0.01264190673828125,
      * -0.01239013671875,
      * 0.01074981689453125,
      * 0.0083465576171875,
      * 0.0005316734313964844,
      * -0.006160736083984375,
      * -0.009368896484375,
      * 0.008575439453125,
      * 0.00678253173828125,
      * -0.020050048828125,
      * -0.005523681640625,
      * -0.005237579345703125,
      * -0.021728515625,
      * -0.00988006591796875,
      * -0.0240325927734375,
      * 0.00865936279296875,
      * -0.01546478271484375,
      * 0.004703521728515625,
      * 0.0487060546875,
      * -0.00798797607421875,
      * 0.005634307861328125,
      * 0.01971435546875,
      * 0.0015916824340820312,
      * 0.0017004013061523438,
      * 0.0175933837890625,
      * 0.0015840530395507812,
      * 0.005458831787109375,
      * -0.00862884521484375,
      * 0.0189666748046875,
      * 0.0215301513671875,
      * -0.0019445419311523438,
      * 0.00464630126953125,
      * 0.0079345703125,
      * -0.00119781494140625,
      * -0.01442718505859375,
      * -0.002086639404296875,
      * -0.035491943359375,
      * 0.00789642333984375,
      * 0.0102691650390625,
      * 0.0111541748046875,
      * -0.03765869140625,
      * -0.0029659271240234375,
      * -0.027679443359375,
      * 0.0172119140625,
      * 0.0151519775390625,
      * -0.0129547119140625,
      * -0.002079010009765625,
      * 0.0024700164794921875,
      * 0.00516510009765625,
      * -0.006237030029296875,
      * -0.0093841552734375,
      * 0.010223388671875,
      * 0.0277252197265625,
      * 0.031951904296875,
      * 0.01358795166015625,
      * -0.004848480224609375,
      * -0.0012912750244140625,
      * -0.19189453125,
      * 0.0062255859375,
      * -0.00615692138671875,
      * 0.005062103271484375,
      * -0.01058197021484375,
      * -0.004512786865234375,
      * -0.0141754150390625,
      * 0.0196075439453125,
      * -0.0026378631591796875,
      * -0.01113128662109375,
      * -0.0038318634033203125,
      * -0.006282806396484375,
      * -0.025421142578125,
      * -0.0008826255798339844,
      * -0.0182647705078125,
      * 0.00589752197265625,
      * 0.009918212890625,
      * -0.007266998291015625,
      * -0.01177215576171875,
      * -0.01377105712890625,
      * 0.01702880859375,
      * -0.006927490234375,
      * -0.0082855224609375,
      * 0.01447296142578125,
      * 0.0176239013671875,
      * 0.024932861328125,
      * -0.00273895263671875,
      * 0.03369140625,
      * 0.0007205009460449219,
      * 0.02288818359375,
      * -0.0177154541015625,
      * -0.01053619384765625,
      * -0.00560760498046875,
      * 0.006397247314453125,
      * 0.01534271240234375,
      * 0.028564453125,
      * -0.005268096923828125,
      * 0.0181121826171875,
      * -0.00044417381286621094,
      * -0.006534576416015625,
      * 0.01488494873046875,
      * -0.0093994140625,
      * 0.012176513671875,
      * 0.008575439453125,
      * -0.007450103759765625,
      * 0.0014925003051757812,
      * 0.0100250244140625,
      * 0.002536773681640625,
      * 0.006420135498046875,
      * -0.00406646728515625,
      * -0.004764556884765625,
      * -0.0250701904296875,
      * -0.002422332763671875,
      * -0.01207733154296875,
      * -0.02227783203125,
      * -0.0062255859375,
      * -0.0089569091796875,
      * 0.0180816650390625,
      * 0.001522064208984375,
      * -0.0037384033203125,
      * 0.020172119140625,
      * 0.0166015625,
      * 0.00434112548828125,
      * 0.01103973388671875,
      * -0.00555419921875,
      * 0.0215911865234375,
      * 0.001598358154296875,
      * -0.004909515380859375,
      * 0.007671356201171875,
      * 0.0010433197021484375,
      * -0.0092315673828125,
      * -0.007415771484375,
      * 0.04962158203125,
      * -0.0017385482788085938,
      * -0.005092620849609375,
      * -0.0023250579833984375,
      * -0.009674072265625,
      * -0.0090179443359375,
      * -0.009765625,
      * -0.005268096923828125,
      * -0.011505126953125,
      * -0.00531005859375,
      * -0.0038433074951171875,
      * 0.01180267333984375,
      * -0.009674072265625,
      * -0.0087127685546875,
      * 0.0225982666015625,
      * 0.003826141357421875,
      * 0.0023040771484375,
      * 0.006744384765625,
      * -0.018280029296875,
      * 0.004650115966796875,
      * 0.00676727294921875,
      * 0.00510406494140625,
      * -0.0174560546875,
      * 0.00644683837890625,
      * -0.01739501953125,
      * -0.0021820068359375,
      * -0.0023097991943359375,
      * -0.010650634765625,
      * -0.0156097412109375,
      * -0.00926971435546875,
      * 0.01419830322265625,
      * -0.0024623870849609375,
      * 0.005764007568359375,
      * 0.012939453125,
      * -0.01788330078125,
      * 0.0013895034790039062,
      * 0.01212310791015625,
      * -0.033935546875,
      * -0.0008940696716308594,
      * 0.0202789306640625,
      * 0.010406494140625,
      * 0.02392578125,
      * -0.00484466552734375,
      * -0.022735595703125,
      * 0.01433563232421875,
      * -0.0038700103759765625,
      * 0.00336456298828125,
      * 0.01849365234375,
      * 0.017486572265625,
      * -0.01715087890625,
      * 0.030609130859375,
      * 0.018707275390625,
      * 0.0109710693359375,
      * 0.018310546875,
      * 0.017730712890625,
      * -0.01386260986328125,
      * -0.01200103759765625,
      * 0.005889892578125,
      * 0.06903076171875,
      * -0.0162353515625,
      * -0.0040130615234375,
      * 0.02313232421875,
      * -0.019622802734375,
      * -0.004673004150390625,
      * 0.017578125,
      * -0.0007462501525878906,
      * 0.003414154052734375,
      * -0.0033702850341796875,
      * -0.0014362335205078125,
      * -0.013702392578125,
      * 0.002887725830078125,
      * -0.0101470947265625,
      * -0.01534271240234375,
      * 0.008544921875,
      * -0.02880859375,
      * 0.0233001708984375,
      * -0.0243988037109375,
      * -0.01410675048828125,
      * 0.00856781005859375,
      * -0.007152557373046875,
      * 0.01146697998046875,
      * 0.01128387451171875,
      * -0.00012069940567016602,
      * 0.005519866943359375,
      * 0.0054931640625,
      * 0.006763458251953125,
      * 0.015777587890625,
      * -0.005340576171875,
      * 0.0078887939453125,
      * -0.00893402099609375,
      * -0.03472900390625,
      * -0.022064208984375,
      * -0.0098419189453125,
      * -0.014862060546875,
      * -0.00478363037109375,
      * 0.00016832351684570312,
      * -0.02734375,
      * 0.0114898681640625,
      * 0.00299835205078125,
      * -0.012481689453125,
      * 0.03033447265625,
      * -0.007740020751953125,
      * -0.01177215576171875,
      * 0.002704620361328125,
      * -0.00720977783203125,
      * 0.01751708984375,
      * -0.0066070556640625,
      * 0.00714874267578125,
      * -0.027435302734375,
      * 0.0071258544921875,
      * 0.010406494140625,
      * -0.00858306884765625,
      * -0.0015764236450195312,
      * -0.0042724609375,
      * -0.012481689453125,
      * -0.0128021240234375,
      * -0.033355712890625,
      * -0.0149383544921875,
      * 0.0015668869018554688,
      * 0.0131988525390625,
      * -0.01202392578125,
      * 0.01116180419921875,
      * 0.0271453857421875,
      * -0.0034465789794921875,
      * 0.0244140625,
      * 0.0089263916015625,
      * 0.0013608932495117188,
      * -0.0038700103759765625,
      * 0.0125579833984375,
      * -0.00577545166015625,
      * 0.00690460205078125,
      * -0.0048065185546875,
      * -0.003948211669921875,
      * 0.017181396484375,
      * -0.0318603515625,
      * -0.006191253662109375,
      * 0.02557373046875,
      * 0.007564544677734375,
      * 0.0279998779296875,
      * 0.0037784576416015625,
      * 0.016571044921875,
      * -0.01242828369140625,
      * 0.0072021484375,
      * 0.005584716796875,
      * -0.00360107421875,
      * -0.0121917724609375,
      * -0.01190948486328125,
      * 0.009246826171875,
      * 0.0024700164794921875,
      * -0.002780914306640625,
      * -0.004451751708984375,
      * -0.058563232421875,
      * 0.00873565673828125,
      * -0.020751953125,
      * 0.0005297660827636719,
      * 0.0174407958984375,
      * 0.0034923553466796875,
      * -0.0125732421875,
      * 0.0257415771484375,
      * -0.018585205078125,
      * 0.00356292724609375,
      * -0.00439453125,
      * 0.0156097412109375,
      * 0.00008094310760498047,
      * -0.0066986083984375,
      * -0.0006084442138671875,
      * 0.00400543212890625,
      * 0.0045928955078125,
      * 0.01959228515625,
      * 0.005756378173828125,
      * 0.0096893310546875,
      * 0.0133819580078125,
      * 0.005054473876953125,
      * 0.004062652587890625,
      * 0.0111846923828125,
      * 0.004657745361328125,
      * 0.01287078857421875,
      * -0.0164642333984375,
      * 0.015960693359375,
      * -0.00856781005859375,
      * -0.0311126708984375,
      * -0.002353668212890625,
      * 0.00628662109375,
      * -0.0011463165283203125,
      * 0.017547607421875,
      * -0.004817962646484375,
      * 0.01995849609375,
      * 0.01152801513671875,
      * 0.007671356201171875,
      * 0.0011415481567382812,
      * -0.0194854736328125,
      * 0.01421356201171875,
      * -0.0033111572265625,
      * 0.0002739429473876953,
      * 0.006771087646484375,
      * -0.01171875,
      * 0.01348876953125,
      * -0.01184844970703125,
      * 0.00008338689804077148,
      * -0.0214080810546875,
      * -0.0009469985961914062,
      * 0.00759124755859375,
      * -0.01251983642578125,
      * -0.01363372802734375,
      * 0.0008139610290527344,
      * -0.01465606689453125,
      * 0.00774383544921875,
      * -0.010498046875,
      * 0.003787994384765625,
      * 0.0023708343505859375,
      * 0.0131988525390625,
      * 0.00801849365234375,
      * -0.00616455078125,
      * 0.01044464111328125,
      * -0.0025806427001953125,
      * -0.0243377685546875,
      * 0.02130126953125,
      * -0.004459381103515625,
      * 0.0033092498779296875,
      * -0.01059722900390625,
      * -0.01499176025390625,
      * 0.017852783203125,
      * -0.0301971435546875,
      * -0.0102081298828125,
      * -0.01236724853515625,
      * 0.01071929931640625,
      * 0.0034637451171875,
      * -0.01727294921875,
      * 0.0364990234375,
      * -0.016021728515625,
      * 0.0340576171875,
      * 0.01055908203125,
      * -0.00632476806640625,
      * 0.00890350341796875,
      * 0.0034236907958984375,
      * -0.022857666015625,
      * -0.0081787109375,
      * 0.0206451416015625,
      * 0.0216827392578125,
      * 0.005184173583984375,
      * -0.0034503936767578125,
      * 0.0026874542236328125,
      * -0.0011625289916992188,
      * -0.021087646484375,
      * -0.002208709716796875,
      * 0.007114410400390625,
      * -0.0006175041198730469,
      * 0.01503753662109375,
      * 0.021026611328125,
      * -0.01497650146484375,
      * 0.0026226043701171875,
      * 0.00691986083984375,
      * -0.01334381103515625,
      * -0.049774169921875,
      * 0.0204315185546875,
      * 0.0028972625732421875,
      * -0.005420684814453125,
      * 0.002758026123046875,
      * -0.002971649169921875,
      * 0.01200103759765625,
      * -0.00388336181640625,
      * -0.01019287109375,
      * 0.01152801513671875,
      * -0.00936126708984375,
      * -0.0161895751953125,
      * 0.0194091796875,
      * 0.00311279296875,
      * -0.003337860107421875,
      * -0.0194091796875,
      * 0.007114410400390625,
      * -0.032012939453125,
      * 0.004306793212890625,
      * 0.006038665771484375,
      * -0.0133514404296875,
      * 0.0188140869140625,
      * 0.015289306640625,
      * -0.0035228729248046875,
      * -0.008209228515625,
      * 0.0010890960693359375,
      * -0.0156707763671875,
      * 0.0014982223510742188,
      * -0.004650115966796875,
      * -0.00293731689453125,
      * -0.0016202926635742188,
      * -0.0090179443359375,
      * 0.0011720657348632812,
      * -0.0034503936767578125,
      * 0.0007128715515136719,
      * 0.019256591796875,
      * 0.0008559226989746094,
      * -0.016326904296875,
      * 0.0030155181884765625,
      * 0.0010671615600585938,
      * -0.0291595458984375,
      * -0.0136871337890625,
      * -0.003437042236328125,
      * 0.005260467529296875,
      * -0.001003265380859375,
      * -0.01318359375,
      * 0.00907135009765625,
      * -0.0179290771484375,
      * -0.0113983154296875,
      * -0.01297760009765625,
      * -0.0012979507446289062,
      * -0.0088958740234375,
      * 0.001323699951171875,
      * 0.0069732666015625,
      * 0.006786346435546875,
      * -0.027862548828125,
      * -0.0166015625,
      * -0.003818511962890625,
      * -0.01800537109375,
      * -0.01519775390625,
      * -0.004268646240234375,
      * -0.00481414794921875,
      * 0.0157318115234375,
      * -0.02410888671875,
      * 0.0005154609680175781,
      * 0.01366424560546875,
      * -0.0256500244140625,
      * 0.00579071044921875,
      * -0.0191192626953125,
      * -0.01543426513671875,
      * 0.0069580078125,
      * 0.01055908203125,
      * 0.0013780593872070312,
      * 0.0236663818359375,
      * 0.0108184814453125,
      * 0.0008907318115234375,
      * -0.019378662109375,
      * 0.0276031494140625,
      * 0.008148193359375,
      * 0.0275421142578125,
      * -0.00879669189453125,
      * 0.00823211669921875,
      * 0.0007953643798828125,
      * 0.01416015625,
      * -0.030853271484375,
      * 0.00864410400390625,
      * -0.0066986083984375,
      * 0.0060272216796875,
      * -0.01739501953125,
      * -0.01092529296875,
      * 0.00811004638671875,
      * 0.000568389892578125,
      * 0.0033245086669921875,
      * 0.00003319978713989258,
      * 0.01200103759765625,
      * 0.10498046875,
      * 0.00032448768615722656,
      * -0.00443267822265625,
      * -0.017822265625,
      * 0.00022172927856445312,
      * 0.0037288665771484375,
      * 0.0090179443359375,
      * -0.0168609619140625,
      * 0.004199981689453125,
      * 0.002002716064453125,
      * -0.01104736328125,
      * -0.013458251953125,
      * -0.0163726806640625,
      * -0.00461578369140625,
      * -0.005268096923828125,
      * -0.006542205810546875,
      * -0.0187225341796875,
      * -0.0156402587890625,
      * 0.03472900390625,
      * -0.00649261474609375,
      * 0.00533294677734375,
      * 0.00991058349609375,
      * -0.015655517578125,
      * -0.007274627685546875,
      * 0.0019359588623046875,
      * 0.0036640167236328125,
      * 0.005153656005859375,
      * 0.01216888427734375,
      * 0.00463104248046875,
      * -0.00577545166015625,
      * 0.0001399517059326172,
      * -0.003932952880859375,
      * -0.009185791015625,
      * 0.01136016845703125,
      * 0.0299530029296875,
      * 0.002948760986328125,
      * -0.004398345947265625,
      * 0.01082611083984375,
      * 0.00983428955078125,
      * -0.01309967041015625,
      * 0.01953125,
      * -0.006992340087890625,
      * -0.004032135009765625,
      * -0.00881195068359375,
      * -0.0005903244018554688,
      * -0.002376556396484375,
      * -0.0196380615234375,
      * 0.0028476715087890625,
      * -0.01534271240234375,
      * 0.027252197265625,
      * -0.01200103759765625,
      * 0.004123687744140625,
      * -0.0035495758056640625,
      * 0.0110321044921875,
      * 0.016815185546875,
      * -0.0223236083984375,
      * -0.0252685546875,
      * 0.00997161865234375,
      * 0.003009796142578125,
      * -0.01557159423828125,
      * 0.001941680908203125,
      * -0.00820159912109375,
      * -0.00936126708984375,
      * -0.0002378225326538086,
      * 0.01103973388671875,
      * -0.007381439208984375,
      * -0.0005779266357421875,
      * -0.026641845703125,
      * 0.001796722412109375,
      * 0.0081329345703125,
      * 0.007434844970703125,
      * -0.0062255859375,
      * 0.0253448486328125,
      * 0.01380157470703125,
      * 0.00530242919921875,
      * -0.004589080810546875,
      * -0.004268646240234375,
      * 0.0175628662109375,
      * -0.015167236328125,
      * 0.0053253173828125,
      * 0.0081787109375,
      * 0.0007228851318359375,
      * -0.006687164306640625,
      * -0.02630615234375,
      * -0.01495361328125,
      * -0.017547607421875,
      * -0.01194000244140625,
      * -0.0037517547607421875,
      * 0.00019478797912597656,
      * -0.00904083251953125,
      * 0.0032806396484375,
      * -0.00553131103515625,
      * -0.03338623046875,
      * 0.032440185546875,
      * 0.0007834434509277344,
      * 0.0221099853515625,
      * -0.0091552734375,
      * -0.01183319091796875,
      * -0.0007939338684082031,
      * 0.029022216796875,
      * 0.002201080322265625,
      * 0.0228729248046875,
      * -0.0098114013671875,
      * 0.02056884765625,
      * -0.0093536376953125,
      * 0.016693115234375,
      * -0.016326904296875,
      * 0.00557708740234375,
      * 0.01340484619140625,
      * 0.01348876953125,
      * 0.01367950439453125,
      * -0.0083160400390625,
      * -0.034027099609375,
      * 0.0003170967102050781,
      * 0.0178070068359375,
      * 0.0162506103515625,
      * 0.004680633544921875,
      * 0.004230499267578125,
      * -0.0088653564453125,
      * -0.019500732421875,
      * -0.007602691650390625,
      * -0.00018072128295898438,
      * 0.0018939971923828125,
      * -0.0065765380859375,
      * -0.004909515380859375,
      * 0.005069732666015625,
      * 0.0171356201171875,
      * -0.01332855224609375,
      * 0.02691650390625,
      * -0.0238037109375,
      * -0.00860595703125,
      * 0.005695343017578125,
      * 0.0001646280288696289,
      * -0.00681304931640625,
      * -0.00891876220703125,
      * 0.0289154052734375,
      * -0.020263671875,
      * 0.01305389404296875,
      * 0.0129547119140625,
      * -0.006999969482421875,
      * 0.0012645721435546875,
      * -0.0038967132568359375,
      * 0.005809783935546875,
      * -0.029876708984375,
      * 0.0161285400390625,
      * 0.0015010833740234375,
      * -0.00525665283203125,
      * -0.007038116455078125,
      * -0.0092620849609375,
      * -0.0032806396484375,
      * -0.004207611083984375,
      * -0.0310821533203125,
      * 0.0023193359375,
      * -0.00439453125,
      * -0.020111083984375,
      * 0.0036411285400390625,
      * 0.006275177001953125,
      * 0.00390625,
      * -0.006603240966796875,
      * 0.025177001953125,
      * 0.016326904296875,
      * -0.010040283203125,
      * 0.030120849609375,
      * -0.0170135498046875,
      * 0.0211639404296875,
      * -0.00927734375,
      * 0.005016326904296875,
      * -0.00949859619140625,
      * -0.0009579658508300781,
      * 0.0106964111328125,
      * 0.0174560546875,
      * 0.01097869873046875,
      * 0.0026397705078125,
      * 0.0128631591796875,
      * -0.0144805908203125,
      * 0.004337310791015625,
      * 0.00530242919921875,
      * -0.0166168212890625,
      * -0.0075225830078125,
      * -0.033233642578125,
      * -0.01139068603515625,
      * -0.0007162094116210938,
      * 0.013946533203125,
      * -0.01055908203125,
      * 0.014923095703125,
      * 0.0177001953125,
      * 0.01064300537109375,
      * 0.01262664794921875,
      * 0.004055023193359375,
      * -0.004444122314453125,
      * 0.0030975341796875,
      * -0.0006399154663085938,
      * 0.01136016845703125,
      * -0.01192474365234375,
      * 0.00907135009765625,
      * -0.01348876953125,
      * -0.0027332305908203125,
      * -0.006931304931640625,
      * 0.00734710693359375,
      * 0.015045166015625,
      * -0.019561767578125,
      * -0.01143646240234375,
      * 0.0247039794921875,
      * -0.02252197265625,
      * -0.0136566162109375,
      * 0.0386962890625,
      * 0.01251983642578125,
      * -0.0215301513671875,
      * -0.004852294921875,
      * 0.001811981201171875,
      * -0.0201416015625,
      * -0.0086517333984375,
      * 0.004772186279296875,
      * -0.007335662841796875,
      * 0.01036834716796875,
      * -0.0031223297119140625,
      * 0.0293426513671875,
      * -0.012115478515625,
      * 0.02130126953125,
      * -0.02056884765625,
      * -0.0075225830078125,
      * -0.0097808837890625,
      * -0.017822265625,
      * -0.008819580078125,
      * -0.0211334228515625,
      * -0.0179290771484375,
      * 0.01287078857421875,
      * -0.0027713775634765625,
      * -0.003879547119140625,
      * -0.0147247314453125,
      * -0.009918212890625,
      * 0.03009033203125,
      * -0.0133056640625,
      * -0.01873779296875,
      * 0.007686614990234375,
      * 0.001922607421875,
      * -0.01442718505859375,
      * -0.0153961181640625,
      * 0.0221099853515625,
      * 0.004261016845703125,
      * 0.0186767578125,
      * 0.006805419921875,
      * 0.004299163818359375,
      * -0.01187896728515625,
      * -0.0241851806640625,
      * 0.00466156005859375,
      * -0.0096435546875,
      * -0.0916748046875,
      * 0.01488494873046875,
      * -0.030548095703125,
      * 0.1644287109375,
      * -0.0024890899658203125,
      * 0.0099945068359375,
      * -0.00537109375,
      * -0.001728057861328125,
      * 0.002140045166015625,
      * 0.02813720703125,
      * 0.00714111328125,
      * -0.0038089752197265625,
      * 0.0102996826171875,
      * -0.0018205642700195312,
      * -0.005596160888671875,
      * -0.007656097412109375,
      * 0.01543426513671875,
      * 0.01512908935546875,
      * -0.0198822021484375,
      * -0.004856109619140625,
      * -0.007045745849609375,
      * -0.00579833984375,
      * -0.015167236328125,
      * -0.0080108642578125,
      * 0.01351165771484375,
      * 0.006160736083984375,
      * -0.01983642578125,
      * 0.0016851425170898438,
      * -0.0223541259765625,
      * -0.0025920867919921875,
      * -0.01076507568359375,
      * -0.00936126708984375,
      * 0.00580596923828125,
      * -0.0170745849609375,
      * -0.0081939697265625,
      * -0.00754547119140625,
      * -0.03033447265625,
      * 0.01543426513671875,
      * 0.01512908935546875,
      * -0.01126861572265625,
      * 0.01125335693359375,
      * -0.00771331787109375,
      * -0.0028934478759765625,
      * -0.01357269287109375,
      * -0.0035228729248046875,
      * -0.01354217529296875,
      * 0.0180206298828125,
      * 0.016387939453125,
      * -0.003597259521484375,
      * -0.0199737548828125,
      * 0.00025725364685058594,
      * -0.0215911865234375,
      * -0.0175933837890625,
      * 0.020263671875,
      * 0.01483154296875,
      * -0.004894256591796875,
      * 0.00868988037109375,
      * -0.00494384765625,
      * -0.0089111328125,
      * 0.023681640625,
      * 0.01165771484375,
      * -0.014923095703125,
      * -0.007080078125,
      * -0.003910064697265625,
      * 0.011260986328125,
      * -0.002582550048828125,
      * -0.0069732666015625,
      * 0.0008134841918945312,
      * -0.01535797119140625,
      * -0.001117706298828125,
      * 0.031005859375,
      * 0.00217437744140625,
      * -0.0244903564453125,
      * 0.034027099609375,
      * -0.017425537109375,
      * 0.01861572265625,
      * 0.001018524169921875,
      * -0.01097869873046875,
      * 0.0079803466796875,
      * -0.032501220703125,
      * -0.00026106834411621094,
      * 0.00443267822265625,
      * 0.0027751922607421875,
      * 0.003269195556640625,
      * -0.008087158203125,
      * 0.005550384521484375,
      * 0.003681182861328125,
      * 0.02783203125,
      * 0.017822265625,
      * 0.005466461181640625,
      * 0.019805908203125,
      * -0.0191497802734375,
      * 0.004726409912109375,
      * 0.00007140636444091797,
      * -0.0254669189453125,
      * -0.00557708740234375,
      * -0.0063629150390625,
      * -0.0027141571044921875,
      * 0.016937255859375,
      * -0.01194000244140625,
      * 0.0244293212890625,
      * -0.01873779296875,
      * 0.0253753662109375,
      * 0.0273895263671875,
      * -0.0164337158203125,
      * -0.01221466064453125,
      * -0.010772705078125,
      * -0.0093231201171875,
      * 0.0019130706787109375,
      * -0.021209716796875,
      * -0.026641845703125,
      * -0.0184478759765625,
      * 0.00592041015625,
      * -0.0080108642578125,
      * 0.0489501953125,
      * -0.00952911376953125,
      * -0.002941131591796875,
      * -0.03863525390625,
      * 0.00698089599609375,
      * -0.0213775634765625,
      * 0.00977325439453125,
      * 0.006000518798828125,
      * 0.0005793571472167969,
      * 0.0081634521484375,
      * -0.028350830078125,
      * 0.01025390625,
      * 0.0265350341796875,
      * 0.0213470458984375,
      * -0.00522613525390625,
      * -0.0006499290466308594,
      * -0.00726318359375,
      * -0.0033092498779296875,
      * 0.0024890899658203125,
      * -0.00127410888671875,
      * -0.00540924072265625,
      * 0.01430511474609375,
      * -0.01053619384765625,
      * 0.0172882080078125,
      * 0.01100921630859375,
      * -0.00801849365234375,
      * 0.0008363723754882812,
      * 0.007537841796875,
      * 0.01812744140625,
      * -0.0218505859375,
      * 0.015533447265625,
      * 0.0177001953125,
      * -0.012725830078125,
      * 0.017059326171875,
      * -0.0022296905517578125,
      * -0.004459381103515625,
      * 0.0075836181640625,
      * -0.0035400390625,
      * 0.00811767578125,
      * 0.01335906982421875,
      * 0.0007281303405761719,
      * 0.0130767822265625,
      * -0.0142822265625,
      * -0.02294921875,
      * -0.0050048828125,
      * 0.01509857177734375,
      * 0.0013942718505859375,
      * 0.0222015380859375,
      * -0.0027370452880859375,
      * 0.0166778564453125,
      * -0.0160064697265625,
      * -0.0146331787109375,
      * -0.002254486083984375,
      * 0.016754150390625,
      * -0.00920867919921875,
      * 0.002960205078125,
      * -0.0086517333984375,
      * -0.005214691162109375,
      * -0.0073699951171875,
      * -0.0126800537109375,
      * 0.003772735595703125,
      * -0.0249176025390625,
      * 0.0001823902130126953,
      * -0.00960540771484375,
      * 0.0009069442749023438,
      * 0.0165557861328125,
      * 0.0201263427734375,
      * -0.0205078125,
      * 0.02972412109375,
      * 0.002956390380859375,
      * -0.002216339111328125,
      * -0.014739990234375,
      * 0.000644683837890625,
      * 0.015777587890625,
      * -0.00991058349609375,
      * 0.032073974609375,
      * 0.0142822265625,
      * 0.0039825439453125,
      * 0.006954193115234375,
      * 0.003826141357421875,
      * -0.026885986328125,
      * -0.01232147216796875,
      * 0.0006403923034667969,
      * -0.0160369873046875,
      * -0.0130615234375,
      * -0.002445220947265625,
      * -0.0251617431640625,
      * -0.0290985107421875,
      * -0.00873565673828125,
      * 0.0143890380859375,
      * -0.00408935546875,
      * 0.01255035400390625,
      * 0.0310821533203125,
      * 0.0126190185546875,
      * 0.0083160400390625,
      * 0.004791259765625,
      * -0.001621246337890625,
      * -0.006443023681640625,
      * 0.0243988037109375,
      * 0.0037479400634765625,
      * 0.0013055801391601562,
      * 0.0208740234375,
      * -0.00920867919921875,
      * -0.00807952880859375,
      * 0.00661468505859375,
      * -0.00911712646484375,
      * -0.004970550537109375,
      * 0.006683349609375,
      * -0.0027828216552734375,
      * 0.009796142578125,
      * -0.01026153564453125,
      * -0.002521514892578125,
      * -0.00824737548828125,
      * -0.00667572021484375,
      * 0.01140594482421875,
      * -0.0048980712890625,
      * 0.03497314453125,
      * 0.0161285400390625,
      * -0.005859375,
      * -0.0007381439208984375,
      * 0.009918212890625,
      * 0.01345062255859375,
      * 0.0081329345703125,
      * 0.0166473388671875,
      * 0.0118560791015625,
      * -0.0027523040771484375,
      * 0.006824493408203125,
      * -0.0018520355224609375,
      * 0.026123046875,
      * 0.02679443359375,
      * 0.0063629150390625,
      * -0.0119476318359375,
      * -0.00896453857421875,
      * -0.0191802978515625,
      * -0.02490234375,
      * -0.00559234619140625,
      * -0.0228424072265625,
      * 0.012054443359375,
      * 0.0245513916015625,
      * 0.01247406005859375,
      * -0.0260009765625,
      * 0.0166015625,
      * -0.061859130859375,
      * 0.015411376953125,
      * -0.00020992755889892578,
      * 0.03424072265625,
      * 0.0277099609375,
      * 0.004711151123046875,
      * -0.006893157958984375,
      * -0.0019216537475585938,
      * 0.017181396484375,
      * -0.00617218017578125,
      * 0.0128936767578125,
      * -0.00537109375,
      * 0.002666473388671875,
      * 0.01387786865234375,
      * -0.006038665771484375,
      * 0.02691650390625,
      * 0.0020542144775390625,
      * 0.055999755859375,
      * -0.043670654296875,
      * -0.018280029296875,
      * 0.0080108642578125,
      * 0.009521484375,
      * -0.009796142578125,
      * -0.020904541015625,
      * -0.007904052734375,
      * 0.00905609130859375,
      * 0.00022292137145996094,
      * -0.01287078857421875,
      * 0.0056915283203125,
      * 0.0282745361328125,
      * 0.01134490966796875,
      * 0.01163482666015625,
      * -0.00368499755859375,
      * 0.0440673828125,
      * -0.0129547119140625,
      * -0.0018167495727539062,
      * -0.0118560791015625,
      * -0.00003910064697265625,
      * -0.021392822265625,
      * 0.01470947265625,
      * 0.0102386474609375,
      * 0.006374359130859375,
      * 0.00104522705078125,
      * 0.015533447265625,
      * 0.0027294158935546875,
      * 0.00873565673828125,
      * -0.01445770263671875,
      * 0.002567291259765625,
      * -0.0007596015930175781,
      * 0.01161956787109375,
      * -0.007068634033203125,
      * 0.015960693359375,
      * 0.0160675048828125,
      * 0.017578125,
      * -0.01038360595703125,
      * -0.02423095703125,
      * 0.0156402587890625,
      * -0.01042938232421875,
      * -0.0157318115234375,
      * -0.00007426738739013672,
      * -0.004680633544921875,
      * -0.018524169921875,
      * 0.0108184814453125,
      * -0.004726409912109375,
      * 0.005916595458984375,
      * 0.02301025390625,
      * -0.00031256675720214844,
      * -0.0027942657470703125,
      * -0.04156494140625,
      * 0.006992340087890625,
      * -0.0038318634033203125,
      * -0.0109100341796875,
      * -0.0009093284606933594,
      * -0.0191650390625,
      * 0.004322052001953125,
      * 0.01026153564453125,
      * 0.0251617431640625,
      * -0.0234375,
      * 0.0313720703125,
      * 0.01433563232421875,
      * -0.0150604248046875,
      * -0.0098114013671875,
      * -0.00797271728515625,
      * -0.004062652587890625,
      * 0.007175445556640625,
      * -0.0101165771484375,
      * 0.00997161865234375,
      * 0.0059051513671875,
      * -0.0090179443359375,
      * -0.00666046142578125,
      * -0.010955810546875,
      * 0.013214111328125,
      * -0.018524169921875,
      * -0.001178741455078125,
      * 0.0175018310546875,
      * 0.028045654296875,
      * 0.0016689300537109375,
      * -0.005859375,
      * 0.0124969482421875,
      * 0.01165008544921875,
      * -0.013214111328125,
      * -0.006732940673828125,
      * 0.01416015625,
      * -0.0219879150390625,
      * -0.01605224609375,
      * -0.004169464111328125,
      * 0.0028591156005859375,
      * 0.006053924560546875,
      * 0.00867462158203125,
      * 0.00791168212890625,
      * -0.0014791488647460938,
      * -0.00347900390625,
      * 0.0136871337890625,
      * -0.011810302734375,
      * -0.00771331787109375,
      * -0.010284423828125,
      * 0.007549285888671875,
      * -0.00830841064453125,
      * -0.01617431640625,
      * 0.01065826416015625,
      * -0.0024433135986328125,
      * 0.0307159423828125,
      * 0.003452301025390625,
      * 0.00041103363037109375,
      * -0.0027599334716796875,
      * 0.00879669189453125,
      * -0.006092071533203125,
      * 0.018157958984375,
      * -0.006511688232421875,
      * 0.0212249755859375,
      * -0.0187835693359375,
      * -0.0016574859619140625,
      * -0.0158843994140625,
      * 0.00652313232421875,
      * -0.0189361572265625,
      * 0.005680084228515625,
      * 0.036376953125,
      * -0.00986480712890625,
      * 0.01502227783203125,
      * 0.025238037109375,
      * -0.00855255126953125,
      * -0.00638580322265625,
      * -0.004779815673828125,
      * -0.0017004013061523438,
      * 0.020355224609375,
      * 0.0048828125,
      * -0.016632080078125,
      * 0.006717681884765625,
      * -0.007537841796875,
      * 0.00476837158203125,
      * 0.0228729248046875,
      * 0.00958251953125,
      * 0.0013790130615234375,
      * -0.0258331298828125,
      * 0.0015268325805664062,
      * 0.01160430908203125,
      * 0.000013053417205810547,
      * 0.0105743408203125,
      * -0.0157012939453125,
      * 0.0002853870391845703,
      * 0.0164794921875,
      * 0.00763702392578125,
      * 0.01222991943359375,
      * 0.0108489990234375,
      * -0.002239227294921875,
      * -0.0096435546875,
      * -0.0162506103515625,
      * 0.008209228515625,
      * -0.0016050338745117188,
      * -0.00284576416015625,
      * 0.0026226043701171875,
      * -0.000033974647521972656,
      * -0.00261688232421875,
      * 0.0208740234375,
      * 0.0082855224609375,
      * -0.002475738525390625,
      * 0.01568603515625,
      * -0.0157928466796875,
      * -0.0102081298828125,
      * 0.0035877227783203125,
      * 0.007434844970703125,
      * 0.01290130615234375,
      * 0.0198211669921875,
      * 0.00972747802734375,
      * -0.028350830078125,
      * -0.01255035400390625,
      * -0.00807952880859375,
      * 0.004116058349609375,
      * 0.00714111328125,
      * -0.010223388671875,
      * 0.0010957717895507812,
      * -0.004425048828125,
      * 0.0282135009765625,
      * -0.01015472412109375,
      * -0.0104827880859375,
      * 0.00555419921875,
      * 0.0111846923828125,
      * -0.00212860107421875,
      * -0.0003516674041748047,
      * -0.01221466064453125,
      * 0.0231475830078125,
      * 0.02178955078125,
      * -0.0211181640625,
      * 0.0132904052734375,
      * 0.0028285980224609375,
      * 0.00530242919921875,
      * 0.022735595703125,
      * 0.00467681884765625,
      * 0.020050048828125,
      * -0.01837158203125,
      * 0.0122222900390625,
      * 0.00235748291015625,
      * -0.01270294189453125,
      * 0.0006647109985351562,
      * 0.01039886474609375,
      * 0.01041412353515625,
      * 0.00952911376953125,
      * 0.0102081298828125,
      * -0.00420379638671875,
      * -0.0018758773803710938,
      * 0.01788330078125,
      * -0.012908935546875,
      * -0.005535125732421875,
      * -0.0163116455078125,
      * -0.01015472412109375,
      * 0.006946563720703125,
      * -0.004749298095703125,
      * -0.01036834716796875,
      * 0.018524169921875,
      * 0.00765228271484375,
      * 0.0102996826171875,
      * -0.00609588623046875,
      * 0.0195465087890625,
      * 0.0164031982421875,
      * -0.004558563232421875,
      * 0.0018939971923828125,
      * -0.005939483642578125,
      * -0.03497314453125,
      * 0.0204010009765625,
      * -0.01096343994140625,
      * 0.0225677490234375,
      * -0.00030303001403808594,
      * 0.004291534423828125,
      * -0.0010700225830078125,
      * 0.011199951171875,
      * 0.006984710693359375,
      * -0.0114593505859375,
      * -0.0102996826171875,
      * 0.01241302490234375,
      * 0.004169464111328125,
      * -0.00893402099609375,
      * 0.0007658004760742188,
      * 0.000640869140625,
      * -0.007457733154296875,
      * 0.0012426376342773438,
      * 0.01325225830078125,
      * 0.0086517333984375,
      * 0.01064300537109375,
      * 0.003570556640625,
      * 0.0258026123046875,
      * -0.02984619140625,
      * -0.0081787109375,
      * -0.020263671875,
      * 0.00015497207641601562,
      * 0.0025806427001953125,
      * 0.00794219970703125,
      * 0.006175994873046875,
      * -0.00795745849609375,
      * -0.0144195556640625,
      * 0.00173187255859375,
      * -0.019500732421875,
      * 0.01047515869140625,
      * 0.0093231201171875,
      * 0.0105438232421875,
      * -0.00665283203125,
      * 0.0108184814453125,
      * 0.0207672119140625,
      * 0.01502227783203125,
      * -0.007335662841796875,
      * 0.00600433349609375,
      * 0.0111541748046875,
      * 0.0048370361328125,
      * 0.005863189697265625,
      * 0.00930023193359375,
      * -0.0229644775390625,
      * -0.01727294921875,
      * -0.0201263427734375,
      * -0.004364013671875,
      * 0.0070953369140625,
      * -0.01483154296875,
      * 0.00855255126953125,
      * -0.001514434814453125,
      * -0.0118865966796875,
      * 0.00679779052734375,
      * -0.00848388671875,
      * -0.0030517578125,
      * -0.0032176971435546875,
      * 0.0097198486328125,
      * -0.004566192626953125,
      * 0.0072021484375,
      * -0.0244293212890625,
      * 0.0172576904296875,
      * -0.00856781005859375,
      * -0.0311737060546875,
      * 0.0097808837890625,
      * -0.00001609325408935547,
      * 0.0003924369812011719,
      * -0.01702880859375,
      * 0.00501251220703125,
      * -0.00023424625396728516,
      * -0.00940704345703125,
      * -0.0164947509765625,
      * 0.006877899169921875,
      * -0.01087188720703125,
      * -0.03314208984375,
      * 0.008636474609375,
      * 0.01123046875,
      * -0.02178955078125,
      * 0.0063323974609375,
      * -0.0124969482421875,
      * 0.003139495849609375,
      * 0.003871917724609375,
      * 0.018341064453125,
      * -0.039886474609375,
      * 0.00022292137145996094,
      * -0.01123809814453125,
      * -0.01435089111328125,
      * 0.0015211105346679688,
      * 0.028961181640625,
      * 0.00519561767578125,
      * 0.0071258544921875,
      * 0.0011425018310546875,
      * -0.0289459228515625,
      * -0.01053619384765625,
      * 0.01042938232421875,
      * -0.00754547119140625,
      * -0.016693115234375,
      * 0.0029926300048828125,
      * 0.0214080810546875,
      * -0.0156402587890625,
      * 0.0232086181640625,
      * 0.01477813720703125,
      * 0.0046234130859375,
      * 0.007965087890625,
      * 0.0013360977172851562,
      * -0.0025730133056640625,
      * -0.01119232177734375,
      * -0.0001418590545654297,
      * -0.01348114013671875,
      * 0.00360107421875,
      * 0.00489044189453125,
      * 0.01104736328125,
      * 0.0051727294921875,
      * -0.01409149169921875,
      * -0.0007076263427734375,
      * 0.01230621337890625,
      * -0.0179901123046875,
      * -0.004024505615234375,
      * -0.004978179931640625,
      * 0.0032863616943359375,
      * -0.00849151611328125,
      * -0.0005779266357421875,
      * -0.01090240478515625,
      * -0.0095062255859375,
      * 0.0038967132568359375,
      * -0.021148681640625,
      * -0.0216217041015625,
      * -0.0242919921875,
      * -0.0012969970703125,
      * 0.01543426513671875,
      * -0.0126190185546875,
      * -0.0035877227783203125,
      * 0.01532745361328125,
      * -0.001979827880859375,
      * -0.01442718505859375,
      * -0.024871826171875,
      * 0.0147247314453125,
      * -0.00365447998046875,
      * 0.005863189697265625,
      * 0.0171356201171875,
      * 0.003383636474609375,
      * -0.04156494140625,
      * -0.00994110107421875,
      * 0.004528045654296875,
      * -0.01263427734375,
      * -0.006153106689453125,
      * 0.00007969141006469727,
      * 0.0164642333984375,
      * -0.00046944618225097656,
      * 0.01345062255859375,
      * -0.008270263671875,
      * -0.00963592529296875,
      * 0.006168365478515625,
      * 0.019775390625,
      * -0.0011396408081054688,
      * -0.0099639892578125,
      * -0.0281829833984375,
      * 0.0184478759765625,
      * 0.003536224365234375,
      * -0.01153564453125,
      * 0.00036907196044921875,
      * -0.0140533447265625,
      * -0.00136566162109375,
      * -0.02069091796875,
      * -0.01059722900390625,
      * 0.01202392578125,
      * 0.01849365234375,
      * 0.01041412353515625,
      * 0.0034351348876953125,
      * -0.0013742446899414062,
      * -0.0054931640625,
      * 0.0273284912109375,
      * -0.01219940185546875,
      * 0.005603790283203125,
      * 0.0300445556640625,
      * 0.020233154296875,
      * 0.006927490234375,
      * -0.002361297607421875,
      * -0.004741668701171875,
      * 0.01367950439453125,
      * 0.018768310546875,
      * -0.01183319091796875,
      * 0.018341064453125,
      * -0.004749298095703125,
      * -0.02130126953125,
      * -0.005077362060546875,
      * 0.0124359130859375,
      * 0.0013208389282226562,
      * -0.0265960693359375,
      * -0.002292633056640625,
      * -0.007488250732421875,
      * 0.00571441650390625,
      * -0.0049896240234375,
      * -0.00896453857421875,
      * -0.00384521484375,
      * -0.00518035888671875,
      * -0.000016987323760986328,
      * 0.0219879150390625,
      * -0.0009641647338867188,
      * -0.01543426513671875,
      * -0.003997802734375,
      * 0.006702423095703125,
      * -0.01507568359375,
      * 0.008148193359375,
      * -0.0088043212890625,
      * 0.00736236572265625,
      * -0.0003960132598876953,
      * 0.01153564453125,
      * 0.0138092041015625,
      * 0.002880096435546875,
      * 0.023162841796875,
      * -0.03515625,
      * -0.014739990234375,
      * 0.0007076263427734375,
      * 0.0161285400390625,
      * 0.007106781005859375,
      * 0.000013113021850585938,
      * 0.013824462890625,
      * 0.01314544677734375,
      * 0.00926971435546875,
      * -0.0311737060546875,
      * -0.00644683837890625,
      * -0.00472259521484375,
      * 0.005931854248046875,
      * 0.00812530517578125,
      * -0.0091400146484375,
      * -0.01247406005859375,
      * 0.0140228271484375,
      * -0.007564544677734375,
      * 0.005496978759765625,
      * 0.0185394287109375,
      * 0.01983642578125,
      * 0.00791168212890625,
      * 0.015655517578125,
      * 0.007598876953125,
      * 0.01385498046875,
      * -0.0090484619140625,
      * -0.003429412841796875,
      * -0.00371551513671875,
      * -0.028350830078125,
      * -0.012176513671875,
      * -0.0264739990234375,
      * 0.0227508544921875,
      * -0.00925445556640625,
      * 0.004505157470703125,
      * -0.01354217529296875,
      * -0.01320648193359375,
      * 0.00432586669921875,
      * -0.0073089599609375,
      * 0.014068603515625,
      * -0.0106658935546875,
      * -0.006092071533203125,
      * -0.00389862060546875,
      * -0.00348663330078125,
      * -0.0189666748046875,
      * -0.006134033203125,
      * 0.0181732177734375,
      * -0.004425048828125,
      * 0.0019741058349609375,
      * 0.00737762451171875,
      * 0.0024127960205078125,
      * 0.00579071044921875,
      * 0.0135498046875,
      * 0.006328582763671875,
      * -0.021575927734375,
      * -0.004764556884765625,
      * -0.0074615478515625,
      * -0.0007729530334472656,
      * -0.0075836181640625,
      * -0.0027408599853515625,
      * 0.005199432373046875,
      * -0.0211639404296875,
      * 0.00337982177734375,
      * -0.00043582916259765625,
      * -0.01160430908203125,
      * 0.00817108154296875,
      * -0.01544952392578125,
      * -0.004650115966796875,
      * -0.019073486328125,
      * -0.006439208984375,
      * 0.01483154296875,
      * 0.007404327392578125,
      * -0.026214599609375,
      * 0.01334381103515625,
      * -0.01483154296875,
      * 0.006420135498046875,
      * 0.0165252685546875,
      * 0.01064300537109375,
      * 0.0007886886596679688,
      * 0.020355224609375,
      * 0.01320648193359375,
      * 0.00969696044921875,
      * 0.017852783203125,
      * -0.0004627704620361328,
      * -0.01934814453125,
      * -0.019073486328125,
      * -0.0028667449951171875,
      * -0.01302337646484375,
      * 0.0007653236389160156,
      * 0.0115509033203125,
      * 0.040557861328125,
      * -0.0059051513671875,
      * -0.012847900390625,
      * -0.00878143310546875,
      * 0.025299072265625,
      * 0.035308837890625,
      * -0.01084136962890625,
      * 0.0299835205078125,
      * -0.00989532470703125,
      * -0.005367279052734375,
      * 0.00677490234375,
      * -0.00400543212890625,
      * 0.0269775390625,
      * 0.0231781005859375,
      * -0.010162353515625,
      * 0.0177154541015625,
      * 0.0004150867462158203,
      * -0.004787445068359375,
      * 0.0013904571533203125,
      * -0.00408172607421875,
      * 0.00342559814453125,
      * -0.00713348388671875,
      * 0.00925445556640625,
      * 0.035430908203125,
      * -0.00818634033203125,
      * 0.00963592529296875,
      * 0.0103607177734375,
      * -0.0021114349365234375,
      * -0.022979736328125,
      * 0.01275634765625,
      * -0.0172271728515625,
      * -0.007274627685546875,
      * -0.0104827880859375,
      * 0.0125732421875,
      * -0.0106048583984375,
      * 0.035430908203125,
      * -0.0214691162109375,
      * 0.0187530517578125,
      * 0.01364898681640625,
      * -0.006130218505859375,
      * 0.0237274169921875,
      * -0.01409149169921875,
      * 0.0134429931640625,
      * 0.005702972412109375,
      * -0.0019292831420898438,
      * 0.01378631591796875,
      * 0.0139617919921875,
      * -0.00347900390625,
      * -0.00334930419921875,
      * 0.0178375244140625,
      * 0.0293731689453125,
      * -0.0254364013671875,
      * -0.0191650390625,
      * 0.00919342041015625,
      * -0.0141448974609375,
      * -0.0154266357421875,
      * 0.01215362548828125,
      * 0.0036067962646484375,
      * 0.017425537109375,
      * 0.005512237548828125,
      * -0.005084991455078125,
      * -0.0171356201171875,
      * 0.01044464111328125,
      * 0.011566162109375,
      * 0.11456298828125,
      * -0.0004379749298095703,
      * 0.01218414306640625,
      * -0.005584716796875,
      * -0.03765869140625,
      * 0.03515625,
      * 0.01885986328125,
      * 0.006443023681640625,
      * -0.0197906494140625,
      * 0.0244293212890625,
      * 0.0013666152954101562,
      * -0.002696990966796875,
      * 0.023681640625,
      * -0.002208709716796875,
      * -0.00524139404296875,
      * 0.007678985595703125,
      * -0.0188140869140625,
      * -0.00725555419921875,
      * 0.0037384033203125,
      * -0.00021469593048095703,
      * -0.0095062255859375,
      * -0.008453369140625,
      * -0.005481719970703125,
      * 0.0023956298828125,
      * 0.00933074951171875,
      * -0.0061187744140625,
      * 0.011871337890625,
      * -0.00885009765625,
      * 0.006786346435546875,
      * -0.027252197265625,
      * -0.01531219482421875,
      * 0.00453948974609375,
      * -0.00974273681640625,
      * -0.0009984970092773438,
      * -0.005672454833984375,
      * -0.0092010498046875,
      * -0.004878997802734375,
      * -0.01183319091796875,
      * -0.0015153884887695312,
      * 0.0010995864868164062,
      * 0.0136566162109375,
      * 0.005428314208984375,
      * 0.0002722740173339844,
      * -0.021820068359375,
      * -0.0008058547973632812,
      * -0.0152740478515625,
      * 0.01470947265625,
      * -0.03009033203125,
      * -0.028289794921875,
      * -0.005046844482421875,
      * 0.01079559326171875,
      * -0.00579071044921875,
      * 0.0252227783203125,
      * 0.0014629364013671875,
      * -0.019561767578125,
      * 0.0166168212890625,
      * 0.0026988983154296875,
      * -0.029022216796875,
      * -0.0123443603515625,
      * 0.01345062255859375,
      * 0.002887725830078125,
      * 0.036895751953125,
      * -0.005870819091796875,
      * -0.0022907257080078125,
      * 0.01125335693359375,
      * -0.0135650634765625,
      * 0.00010222196578979492,
      * -0.0137176513671875,
      * 0.005451202392578125,
      * 0.0009665489196777344,
      * -0.0212860107421875,
      * 0.013946533203125,
      * -0.01385498046875,
      * 0.0175933837890625,
      * -0.0010890960693359375,
      * 0.0063629150390625,
      * 0.0021839141845703125,
      * 0.0037021636962890625,
      * -0.01432037353515625,
      * -0.0011835098266601562,
      * 0.00409698486328125,
      * -0.010528564453125,
      * 0.0127410888671875,
      * 0.01445770263671875,
      * -0.007740020751953125,
      * 0.00872039794921875,
      * -0.01377105712890625,
      * -0.024444580078125,
      * 0.006591796875,
      * 0.0074615478515625,
      * -0.0024662017822265625,
      * -0.00765228271484375,
      * 0.0065765380859375,
      * -0.0190582275390625,
      * -0.01412200927734375,
      * -0.01039886474609375,
      * -0.005634307861328125,
      * 0.0006513595581054688,
      * 0.00495147705078125,
      * -0.00223541259765625,
      * 0.0075225830078125,
      * -0.0191650390625,
      * 0.01557159423828125,
      * -0.0192718505859375,
      * -0.0079193115234375,
      * -0.01898193359375,
      * -0.0161285400390625,
      * -0.01708984375,
      * 0.01036834716796875,
      * -0.0145111083984375,
      * -0.00887298583984375,
      * -0.004199981689453125,
      * 0.0004680156707763672,
      * 0.005550384521484375,
      * 0.0094146728515625,
      * 0.03192138671875,
      * -0.003284454345703125,
      * 0.00830841064453125,
      * 0.01477813720703125,
      * 0.0277862548828125,
      * 0.008026123046875,
      * -0.00017654895782470703,
      * -0.006214141845703125,
      * -0.01132965087890625,
      * 0.018524169921875,
      * -0.0117034912109375,
      * 0.01215362548828125,
      * -0.01015472412109375,
      * -0.014617919921875,
      * 0.01305389404296875,
      * -0.01476287841796875,
      * -0.016693115234375,
      * 0.0033721923828125,
      * 0.0052947998046875,
      * 0.0159454345703125,
      * -0.00026226043701171875,
      * 0.0027561187744140625,
      * 0.00890350341796875,
      * 0.016693115234375,
      * 0.00274658203125,
      * 0.00611114501953125,
      * -0.0028667449951171875,
      * 0.007843017578125,
      * -0.0022258758544921875,
      * 0.019073486328125,
      * 0.0170440673828125,
      * -0.00010067224502563477,
      * 0.01442718505859375,
      * -0.01085662841796875,
      * 0.00249481201171875,
      * -0.0020122528076171875,
      * -0.0029850006103515625,
      * -0.01270294189453125,
      * 0.020721435546875,
      * -0.00891876220703125,
      * 0.0066986083984375,
      * 0.010894775390625,
      * 0.004924774169921875,
      * 0.00826263427734375,
      * -0.015380859375,
      * -0.0052032470703125,
      * 0.01035308837890625,
      * 0.0091705322265625,
      * 0.0032596588134765625,
      * -0.0259552001953125,
      * 0.01045989990234375,
      * 0.0189208984375,
      * 0.002254486083984375,
      * -0.0023899078369140625,
      * -0.0116729736328125,
      * -0.005321502685546875,
      * -0.043212890625,
      * 0.0008077621459960938,
      * 0.01033782958984375,
      * -0.00592803955078125,
      * -0.00585174560546875,
      * 0.01389312744140625,
      * 0.0128326416015625,
      * 0.0084381103515625,
      * 0.01654052734375,
      * 0.00713348388671875,
      * 0.021636962890625,
      * 0.0144195556640625,
      * 0.0176544189453125,
      * -0.007354736328125,
      * -0.01316070556640625,
      * -0.01290130615234375,
      * -0.01084136962890625,
      * 0.01062774658203125,
      * -0.0294189453125,
      * 0.0009965896606445312,
      * 0.0009679794311523438,
      * -0.007354736328125,
      * 0.0111083984375,
      * -0.0204010009765625,
      * 0.0009570121765136719,
      * 0.0030918121337890625,
      * -0.0197296142578125,
      * 0.031036376953125,
      * 0.00472259521484375,
      * -0.009796142578125,
      * 0.002338409423828125,
      * -0.0007171630859375,
      * 0.0161590576171875,
      * -0.01270294189453125,
      * -0.0091094970703125,
      * -0.0169525146484375,
      * -0.0233306884765625,
      * 0.0031528472900390625,
      * 0.004199981689453125,
      * 0.0021953582763671875,
      * -0.01181793212890625,
      * -0.012237548828125,
      * 0.0095672607421875,
      * 0.00641632080078125,
      * 0.01532745361328125,
      * -0.0333251953125,
      * -0.0087432861328125,
      * 0.011688232421875,
      * -0.003055572509765625,
      * 0.0201416015625,
      * 0.01270294189453125,
      * -0.003742218017578125,
      * -0.02044677734375,
      * -0.01214599609375,
      * 0.002346038818359375,
      * -0.004150390625,
      * -0.0082244873046875,
      * 0.0098876953125,
      * -0.0200653076171875,
      * 0.01702880859375,
      * -0.01702880859375,
      * 0.02783203125,
      * 0.0033168792724609375,
      * -0.01453399658203125,
      * -0.005168914794921875,
      * 0.00799560546875,
      * -0.007511138916015625,
      * -0.0248260498046875,
      * 0.004299163818359375,
      * 0.006824493408203125,
      * -0.022308349609375,
      * -0.0062103271484375,
      * 0.0126495361328125,
      * 0.0051422119140625,
      * -0.004302978515625,
      * -0.01230621337890625,
      * -0.0115509033203125,
      * 0.0179290771484375,
      * -0.0001270771026611328,
      * -0.0207366943359375,
      * 0.01306915283203125,
      * 0.04022216796875,
      * -0.004146575927734375,
      * -0.00199127197265625,
      * -0.01995849609375,
      * 0.007724761962890625,
      * -0.01140594482421875,
      * -0.0006551742553710938,
      * 0.032257080078125,
      * 0.00868988037109375,
      * 0.0182647705078125,
      * 0.01099395751953125,
      * 0.002704620361328125,
      * 0.00800323486328125,
      * 0.00341033935546875,
      * 0.0077056884765625,
      * -0.0217132568359375,
      * 0.01042938232421875,
      * 0.00833892822265625,
      * -0.01629638671875,
      * 0.0033283233642578125,
      * -0.00669097900390625,
      * -0.01678466796875,
      * 0.0162811279296875,
      * 0.004314422607421875,
      * 0.013153076171875,
      * 0.002685546875,
      * 0.0295562744140625,
      * -0.00792694091796875,
      * -0.00890350341796875,
      * -0.01519775390625,
      * -0.021820068359375,
      * 0.016265869140625,
      * -0.01267242431640625,
      * -0.01361083984375,
      * -0.005340576171875,
      * 0.01468658447265625,
      * 0.0030345916748046875,
      * -0.0112152099609375,
      * -0.004039764404296875,
      * -0.00936126708984375,
      * -0.072021484375,
      * -0.0009093284606933594,
      * -0.0074310302734375,
      * -0.0026378631591796875,
      * 0.003997802734375,
      * 0.0204925537109375,
      * 0.00809478759765625,
      * -0.00963592529296875,
      * -0.0117950439453125,
      * -0.005748748779296875,
      * 0.0223388671875,
      * -0.0034465789794921875,
      * -0.004665374755859375,
      * -0.004608154296875,
      * 0.0088043212890625,
      * -0.0013751983642578125,
      * -0.03900146484375,
      * -0.016693115234375,
      * 0.018280029296875,
      * 0.00592041015625,
      * -0.00994110107421875,
      * -0.015411376953125,
      * 0.00531768798828125,
      * -0.0052947998046875,
      * 0.0102691650390625,
      * -0.037506103515625,
      * 0.0171661376953125,
      * -0.0177459716796875,
      * -0.0004265308380126953,
      * 0.00930023193359375,
      * 0.04998779296875,
      * 0.00356292724609375,
      * -0.031494140625,
      * -0.0020923614501953125,
      * 0.002307891845703125,
      * -0.0165863037109375,
      * 0.001033782958984375,
      * 0.0011796951293945312,
      * 0.002971649169921875,
      * 0.0269622802734375,
      * 0.0142974853515625,
      * 0.006397247314453125,
      * -0.00896453857421875,
      * -0.0104217529296875,
      * 0.002780914306640625,
      * -0.0152587890625,
      * -0.0241851806640625,
      * -0.0146942138671875,
      * 0.0011224746704101562,
      * -0.0262298583984375,
      * 0.00818634033203125,
      * 0.00930023193359375,
      * -0.005199432373046875,
      * 0.0013360977172851562,
      * -0.00612640380859375,
      * -0.006561279296875,
      * -0.01557159423828125,
      * -0.01520538330078125,
      * 0.04010009765625,
      * -0.01214599609375,
      * 0.0020580291748046875,
      * 0.01358795166015625,
      * -0.01495361328125,
      * -0.00467681884765625,
      * 0.0135955810546875,
      * 0.011566162109375,
      * 0.006580352783203125,
      * -0.00936126708984375,
      * 0.004062652587890625,
      * -0.0190582275390625,
      * -0.0053253173828125,
      * 0.0085296630859375,
      * -0.037200927734375,
      * 0.005298614501953125,
      * -0.00620269775390625,
      * -0.014495849609375,
      * 0.0169525146484375,
      * -0.02593994140625,
      * -0.01543426513671875,
      * 0.00424957275390625,
      * 0.004150390625,
      * 0.0169219970703125,
      * -0.0126495361328125,
      * 0.006534576416015625,
      * -0.014862060546875,
      * 0.0022430419921875,
      * -0.0126190185546875,
      * -0.006702423095703125,
      * -0.006771087646484375,
      * -0.01053619384765625,
      * -0.015899658203125,
      * 0.019744873046875,
      * 0.00621795654296875,
      * -0.006359100341796875,
      * -0.038665771484375,
      * 0.0252838134765625,
      * 0.024017333984375,
      * -0.022369384765625,
      * -0.0017414093017578125,
      * -0.01038360595703125,
      * -0.003787994384765625,
      * 0.0143890380859375,
      * 0.004665374755859375,
      * 0.00916290283203125,
      * -0.00034546852111816406,
      * 0.0059967041015625,
      * -0.0203857421875,
      * -0.0020809173583984375,
      * -0.01055145263671875,
      * 0.016693115234375,
      * 0.0007600784301757812,
      * -0.037506103515625,
      * -0.042938232421875,
      * 0.0195770263671875,
      * -0.01277923583984375,
      * 0.0196990966796875,
      * 0.01059722900390625,
      * -0.0010433197021484375,
      * 0.01531219482421875,
      * 0.021728515625,
      * -0.00971221923828125,
      * 0.038787841796875,
      * 0.0024013519287109375,
      * -0.0008959770202636719,
      * -0.005237579345703125,
      * -0.008575439453125,
      * 0.0266571044921875,
      * -0.0126495361328125,
      * 0.0117950439453125,
      * -0.0007996559143066406,
      * -0.0078887939453125,
      * -0.0009260177612304688,
      * 0.00934600830078125,
      * -0.00970458984375,
      * -0.0007205009460449219,
      * -0.0022125244140625,
      * -0.0025920867919921875,
      * -0.035888671875,
      * -0.01190185546875,
      * -0.004032135009765625,
      * -0.00408935546875,
      * 0.00798797607421875,
      * 0.004177093505859375,
      * -0.0262298583984375,
      * 0.0016193389892578125,
      * 0.0203704833984375,
      * -0.0022144317626953125,
      * -0.0037822723388671875,
      * 0.00013458728790283203,
      * 0.0008382797241210938,
      * -0.0112152099609375,
      * 0.0128936767578125,
      * 0.0269012451171875,
      * 0.012481689453125,
      * -0.00818634033203125,
      * 0.03155517578125,
      * -0.01412200927734375,
      * 0.019622802734375,
      * 0.09197998046875,
      * 0.04986572265625,
      * -0.0195770263671875,
      * 0.01018524169921875,
      * -0.0225677490234375,
      * -0.020294189453125,
      * 0.018646240234375,
      * -0.0007214546203613281,
      * 0.0038928985595703125,
      * -0.0010194778442382812,
      * -0.004985809326171875,
      * -0.006603240966796875,
      * -0.0031642913818359375,
      * 0.0128936767578125,
      * 0.0019931793212890625,
      * 0.0138397216796875,
      * -0.016357421875,
      * 0.013671875,
      * 0.0160980224609375,
      * -0.012725830078125,
      * -0.00286865234375,
      * 0.00445556640625,
      * -0.007671356201171875,
      * 0.00746917724609375,
      * -0.00027060508728027344,
      * -0.0059356689453125,
      * 0.026336669921875,
      * -0.0028533935546875,
      * 0.0159759521484375,
      * 0.0001958608627319336,
      * 0.0125732421875,
      * 0.0002034902572631836,
      * -0.00971221923828125,
      * 0.0120391845703125,
      * -0.00807952880859375,
      * 0.0092620849609375,
      * -0.01678466796875,
      * 0.0053253173828125,
      * -0.0119476318359375,
      * 0.006946563720703125,
      * 0.01279449462890625,
      * 0.01568603515625,
      * -0.0300750732421875,
      * 0.00390625,
      * 0.00384521484375,
      * -0.0038661956787109375,
      * 0.0025920867919921875,
      * 0.00888824462890625,
      * -0.00823211669921875,
      * 0.0164642333984375,
      * 0.0004324913024902344,
      * 0.027130126953125,
      * -0.005222320556640625,
      * 0.01110076904296875,
      * 0.00408935546875,
      * -0.00858306884765625,
      * 0.0164947509765625,
      * 0.00290679931640625,
      * -0.01514434814453125,
      * -0.005619049072265625,
      * 0.0218048095703125,
      * 0.01251983642578125,
      * 0.0282440185546875,
      * 0.01468658447265625,
      * 0.01262664794921875,
      * 0.0177154541015625,
      * -0.0037479400634765625,
      * 0.009307861328125,
      * 0.00505828857421875,
      * -0.00405120849609375,
      * -0.01026153564453125,
      * 0.0163421630859375,
      * 0.00940704345703125,
      * 0.01275634765625,
      * 0.0053863525390625,
      * 0.011810302734375,
      * 0.014068603515625,
      * -0.0033931732177734375,
      * -0.01456451416015625,
      * -0.01055145263671875,
      * -0.0272064208984375,
      * 0.05926513671875,
      * -0.002971649169921875,
      * -0.005039215087890625,
      * -0.0299835205078125,
      * -0.022735595703125,
      * -0.0232086181640625,
      * 0.0032367706298828125,
      * 0.014068603515625,
      * -0.005977630615234375,
      * 0.004364013671875,
      * 0.000026404857635498047,
      * 0.0004451274871826172,
      * -0.0081939697265625,
      * -0.01364898681640625,
      * -0.029510498046875,
      * -0.0243682861328125,
      * -0.01001739501953125,
      * -0.002796173095703125,
      * -0.0008287429809570312,
      * 0.01125335693359375,
      * -0.00994110107421875,
      * -0.0140228271484375,
      * 0.0033550262451171875,
      * 0.00765228271484375,
      * -0.006252288818359375,
      * 0.00865936279296875,
      * 0.00390625,
      * 0.002315521240234375,
      * 0.01056671142578125,
      * 0.01171875,
      * 0.0198822021484375,
      * -0.01934814453125,
      * 0.00827789306640625,
      * 0.0057525634765625,
      * 0.0021839141845703125,
      * 0.004894256591796875,
      * 0.0147552490234375,
      * 0.0059967041015625,
      * 0.0151519775390625,
      * 0.01537322998046875,
      * -0.0170440673828125,
      * -0.01348114013671875,
      * -0.0046234130859375,
      * -0.004680633544921875,
      * -0.00702667236328125,
      * -0.004245758056640625,
      * -0.0027751922607421875,
      * 0.015869140625,
      * 0.0086517333984375,
      * 0.00799560546875,
      * -0.003574371337890625,
      * 0.01255035400390625,
      * 0.0147247314453125,
      * -0.031524658203125,
      * -0.011871337890625,
      * -0.006877899169921875,
      * 0.01146697998046875,
      * -0.0017719268798828125,
      * -0.0009531974792480469,
      * 0.01073455810546875,
      * -0.0003523826599121094,
      * -0.01110076904296875,
      * -0.0006237030029296875,
      * 0.007415771484375,
      * 0.00893402099609375,
      * 0.01236724853515625,
      * -0.0201263427734375,
      * -0.01012420654296875,
      * 0.002777099609375,
      * -0.003765106201171875,
      * 0.005706787109375,
      * 0.00563812255859375,
      * 0.0096893310546875,
      * 0.006938934326171875,
      * -0.008270263671875,
      * -0.002132415771484375,
      * -0.0189971923828125,
      * -0.017730712890625,
      * 0.005001068115234375,
      * -0.005405426025390625,
      * -0.0002639293670654297,
      * -0.012451171875,
      * 0.0164794921875,
      * -0.01275634765625,
      * -0.00826263427734375,
      * -0.01122283935546875,
      * 0.005584716796875,
      * -0.0372314453125,
      * -0.01172637939453125,
      * 0.0115509033203125,
      * -0.002960205078125,
      * 0.01401519775390625,
      * 0.0026073455810546875,
      * 0.003688812255859375,
      * -0.03826904296875,
      * -0.0031795501708984375,
      * -0.0012645721435546875,
      * -0.01361083984375,
      * -0.00830078125,
      * -0.006542205810546875,
      * 0.00379180908203125,
      * 0.0144805908203125,
      * 0.010894775390625,
      * -0.0003933906555175781,
      * 0.00388336181640625,
      * 0.0178375244140625,
      * -0.01499176025390625,
      * -0.0028743743896484375,
      * -0.00928497314453125,
      * 0.00970458984375,
      * -0.004398345947265625,
      * -0.00389862060546875,
      * -0.0085906982421875,
      * -0.00035572052001953125,
      * -0.01386260986328125,
      * -0.00724029541015625,
      * 0.0006704330444335938,
      * 0.00847625732421875,
      * -0.0027408599853515625,
      * 0.0001811981201171875,
      * 0.00650787353515625,
      * 0.009765625,
      * 0.004974365234375,
      * -0.0187225341796875,
      * 0.0020275115966796875,
      * -0.0062103271484375,
      * 0.012847900390625,
      * -0.0226593017578125,
      * 0.0008192062377929688,
      * 0.017608642578125,
      * -0.01409149169921875,
      * 0.034576416015625,
      * 0.00982666015625,
      * -0.00362396240234375,
      * -0.028533935546875,
      * 0.0190582275390625,
      * 0.0212860107421875,
      * 0.0106048583984375,
      * 0.0021152496337890625,
      * 0.000013232231140136719,
      * 0.00846099853515625,
      * -0.0006794929504394531,
      * 0.0085296630859375,
      * 0.0208587646484375,
      * 0.00011748075485229492,
      * -0.006511688232421875,
      * 0.02642822265625,
      * 0.04510498046875,
      * -0.025543212890625,
      * 0.015869140625,
      * 0.007381439208984375,
      * -0.00513458251953125,
      * 0.0102081298828125,
      * -0.02874755859375,
      * 0.0123291015625,
      * -0.005275726318359375,
      * 0.021697998046875,
      * -0.006084442138671875,
      * -0.0165252685546875,
      * 0.0204315185546875,
      * -0.0257415771484375,
      * -0.002529144287109375,
      * 0.0439453125,
      * 0.00572967529296875,
      * -0.015716552734375,
      * 0.00848388671875,
      * 0.0089111328125,
      * 0.01873779296875,
      * 0.004688262939453125,
      * -0.014739990234375,
      * -0.01058197021484375,
      * 0.0009632110595703125,
      * -0.00397491455078125,
      * -0.00528717041015625,
      * -0.0171966552734375,
      * 0.0014925003051757812,
      * 0.01325225830078125,
      * 0.00585174560546875,
      * -0.00563812255859375,
      * -0.01947021484375,
      * -0.00725555419921875,
      * -0.006664276123046875,
      * -0.0078887939453125,
      * 0.0017719268798828125,
      * -0.004230499267578125,
      * 0.0296630859375,
      * 0.006931304931640625,
      * -0.0017614364624023438,
      * 0.00011682510375976562,
      * -0.01318359375,
      * 0.0012331008911132812,
      * 0.01227569580078125,
      * 0.0200347900390625,
      * 0.002529144287109375,
      * 0.0075225830078125,
      * -0.004741668701171875,
      * 0.003948211669921875,
      * 0.044403076171875,
      * 0.00717926025390625,
      * -0.02020263671875,
      * -0.0115814208984375,
      * -0.015167236328125,
      * -0.0012502670288085938,
      * 0.00228118896484375,
      * -0.0023193359375,
      * 0.00902557373046875,
      * -0.01165008544921875,
      * 0.01264190673828125,
      * 0.00035262107849121094,
      * -0.004215240478515625,
      * -0.003826141357421875,
      * 0.0052490234375,
      * -0.00921630859375,
      * 0.0494384765625,
      * -0.0146331787109375,
      * -0.0162353515625,
      * -0.0249786376953125,
      * 0.02447509765625,
      * 0.01125335693359375,
      * -0.00815582275390625,
      * 0.00368499755859375,
      * 0.0255279541015625,
      * 0.007770538330078125,
      * 0.0042572021484375,
      * 0.0130157470703125,
      * 0.0096282958984375,
      * 0.031463623046875,
      * 0.0060272216796875,
      * 0.0217132568359375,
      * -0.0026092529296875,
      * -0.0095672607421875,
      * 0.002437591552734375,
      * 0.007068634033203125,
      * 0.01491546630859375,
      * -0.0006594657897949219,
      * -0.01161956787109375,
      * -0.01235198974609375,
      * 0.001697540283203125,
      * 0.00119781494140625,
      * 0.032928466796875,
      * -0.0015583038330078125,
      * -0.0032672882080078125,
      * 0.0215606689453125,
      * 0.016387939453125,
      * -0.01812744140625,
      * -0.001415252685546875,
      * 0.005706787109375,
      * 0.0243988037109375,
      * -0.0063629150390625,
      * -0.000789642333984375,
      * 0.00445556640625,
      * 0.006038665771484375,
      * 0.00345611572265625,
      * -0.02227783203125,
      * 0.016265869140625,
      * -0.01128387451171875,
      * -0.01094818115234375,
      * -0.01318359375,
      * -0.0111541748046875,
      * -0.004344940185546875,
      * 0.007442474365234375,
      * -0.01219940185546875,
      * -0.007663726806640625,
      * -0.01128387451171875,
      * -0.00009065866470336914,
      * -0.002712249755859375,
      * 0.0262451171875,
      * 0.00205230712890625,
      * 0.0031528472900390625,
      * 0.0270538330078125,
      * 0.01047515869140625,
      * 0.0217437744140625,
      * 0.005237579345703125,
      * -0.005527496337890625,
      * 0.002246856689453125,
      * -0.0029354095458984375,
      * 0.004192352294921875,
      * 0.021026611328125,
      * -0.01904296875,
      * -0.004543304443359375,
      * -0.0112762451171875,
      * -0.0003914833068847656,
      * -0.01447296142578125,
      * -0.00734710693359375,
      * -0.0208282470703125,
      * 0.01512908935546875,
      * 0.030548095703125,
      * -0.00992584228515625,
      * 0.0272979736328125,
      * 0.01080322265625,
      * -0.01023101806640625,
      * -0.01537322998046875,
      * 0.006946563720703125,
      * 0.001865386962890625,
      * 0.007537841796875,
      * 0.0108795166015625,
      * -0.009552001953125,
      * 0.0160064697265625,
      * -0.00004482269287109375,
      * 0.00769805908203125,
      * 0.0164642333984375,
      * -0.0016622543334960938,
      * -0.0222015380859375,
      * -0.00982666015625,
      * 0.01258087158203125,
      * 0.00969696044921875,
      * 0.0260162353515625,
      * 0.0299072265625,
      * -0.0780029296875,
      * -0.005344390869140625,
      * -0.0200347900390625,
      * -0.001422882080078125,
      * 0.022308349609375,
      * 0.0164031982421875,
      * 0.006298065185546875,
      * -0.00908660888671875,
      * 0.006439208984375,
      * 0.00986480712890625,
      * -0.00952911376953125,
      * -0.00555419921875,
      * 0.0059814453125,
      * -0.0011348724365234375,
      * 0.0018672943115234375,
      * -0.0167083740234375,
      * 0.017181396484375,
      * 0.0033092498779296875,
      * 0.0004925727844238281,
      * -0.00983428955078125,
      * 0.0107269287109375,
      * -0.0140380859375,
      * -0.01221466064453125,
      * 0.012451171875,
      * 0.00507354736328125,
      * -0.0019512176513671875,
      * 0.0133056640625,
      * 0.00708770751953125,
      * 0.00827789306640625,
      * 0.00507354736328125,
      * -0.0286102294921875,
      * -0.005218505859375,
      * -0.0009083747863769531,
      * 0.002529144287109375,
      * 0.0135650634765625,
      * -0.0171966552734375,
      * 0.03363037109375,
      * 0.004192352294921875,
      * -0.00684356689453125,
      * 0.052032470703125,
      * -0.0033702850341796875,
      * -0.0098724365234375,
      * 0.0141754150390625,
      * -0.01154327392578125,
      * -0.009185791015625,
      * -0.00197601318359375,
      * 0.01312255859375,
      * -0.000949859619140625,
      * 0.00872802734375,
      * -0.0075225830078125,
      * 0.1185302734375,
      * -0.01143646240234375,
      * 0.006183624267578125,
      * -0.0067291259765625,
      * 0.0001468658447265625,
      * 0.0179595947265625,
      * 0.00450897216796875,
      * -0.01104736328125,
      * 0.007106781005859375,
      * 0.0023746490478515625,
      * -0.007354736328125,
      * -0.006061553955078125,
      * 0.005245208740234375,
      * 0.00017702579498291016,
      * 0.02215576171875,
      * 0.007656097412109375,
      * -0.00334930419921875,
      * 0.01413726806640625,
      * -0.00930023193359375,
      * 0.0029315948486328125,
      * 0.01326751708984375,
      * -0.0064849853515625,
      * -0.0007691383361816406,
      * 0.0006113052368164062,
      * -0.005786895751953125,
      * 0.02276611328125,
      * 0.00702667236328125,
      * 0.019439697265625,
      * 0.01025390625,
      * -0.0018138885498046875,
      * 0.0284271240234375,
      * 0.0001919269561767578,
      * 0.0017004013061523438,
      * 0.0156707763671875,
      * 0.0107879638671875,
      * 0.007663726806640625,
      * -0.01525115966796875,
      * -0.008636474609375,
      * 0.0014867782592773438,
      * -0.04620361328125,
      * 0.0028362274169921875,
      * 0.005199432373046875,
      * -0.0228271484375,
      * 0.0284576416015625,
      * -0.012847900390625,
      * -0.01165771484375,
      * 0.000675201416015625,
      * -0.0167999267578125,
      * 0.0294189453125,
      * 0.0079498291015625,
      * 0.004425048828125,
      * -0.00824737548828125,
      * 0.032440185546875,
      * -0.00556182861328125,
      * 0.00841522216796875,
      * 0.0185089111328125,
      * 0.0093841552734375,
      * 0.00960540771484375,
      * -0.001880645751953125,
      * 0.0008344650268554688,
      * 0.00356292724609375,
      * -0.005626678466796875,
      * 0.0001621246337890625,
      * 0.027862548828125,
      * 0.01025390625,
      * 0.00679779052734375,
      * -0.01232147216796875,
      * 0.00946044921875,
      * 0.018829345703125,
      * 0.00525665283203125,
      * 0.0002803802490234375,
      * 0.0029048919677734375,
      * -0.0009183883666992188,
      * -0.00916290283203125,
      * 0.0146331787109375,
      * -0.0122833251953125,
      * -0.0059661865234375,
      * 0.0193023681640625,
      * -0.0078277587890625,
      * 0.0147247314453125,
      * 0.0144805908203125,
      * -0.009185791015625,
      * 0.0090179443359375,
      * 0.0097503662109375,
      * -0.003993988037109375,
      * -0.0159912109375,
      * -0.016815185546875,
      * -0.0135650634765625,
      * -0.001239776611328125,
      * -0.01464080810546875,
      * 0.0189971923828125,
      * -0.01007080078125,
      * 0.006866455078125,
      * -0.0019779205322265625,
      * -0.0157470703125,
      * -0.0159912109375,
      * -0.016693115234375,
      * -0.01329803466796875,
      * -0.0123443603515625,
      * 0.0038967132568359375,
      * -0.007965087890625,
      * -0.01256561279296875,
      * 0.0085906982421875,
      * -0.0282440185546875,
      * -0.000621795654296875,
      * 0.001697540283203125,
      * 0.0184478759765625,
      * -0.005802154541015625,
      * -0.0020656585693359375,
      * 0.01096343994140625,
      * -0.0217132568359375,
      * 0.0025634765625,
      * -0.01467132568359375,
      * -0.0022983551025390625,
      * 0.005474090576171875,
      * 0.0014715194702148438,
      * -0.0149383544921875,
      * 0.0115966796875,
      * 0.00665283203125,
      * 0.0034313201904296875,
      * 0.0176239013671875,
      * -0.003208160400390625,
      * 0.0039215087890625,
      * 0.009521484375,
      * 0.003570556640625,
      * 0.0132598876953125,
      * 0.0019626617431640625,
      * -0.01097869873046875,
      * -0.0056915283203125,
      * -0.00859832763671875,
      * 0.004352569580078125,
      * 0.013214111328125,
      * 0.0165252685546875,
      * -0.0103607177734375,
      * 0.0015010833740234375,
      * 0.01312255859375,
      * 0.0200653076171875,
      * -0.0081939697265625,
      * -0.0019702911376953125,
      * 0.0240020751953125,
      * 0.007663726806640625,
      * -0.002490997314453125,
      * -0.015655517578125,
      * -0.02215576171875,
      * 0.038055419921875,
      * 0.0250091552734375,
      * 0.0153961181640625,
      * 0.0283966064453125,
      * 0.0037384033203125,
      * 0.005523681640625,
      * -0.005489349365234375,
      * 0.01209259033203125,
      * -0.0009512901306152344,
      * 0.00402069091796875,
      * 0.01241302490234375,
      * 0.008453369140625,
      * 0.0235443115234375,
      * -0.005626678466796875,
      * -0.013275146484375,
      * -0.01172637939453125,
      * -0.01532745361328125,
      * -0.00717926025390625,
      * 0.00807952880859375,
      * -0.004360198974609375,
      * 0.0158538818359375,
      * 0.0133514404296875,
      * -0.0025348663330078125,
      * -0.01690673828125,
      * 0.03076171875,
      * 0.0146026611328125,
      * -0.003658294677734375,
      * -0.00540924072265625,
      * 0.0021953582763671875,
      * 0.005329132080078125,
      * -0.005859375,
      * -0.00039768218994140625,
      * 0.00928497314453125,
      * 0.028045654296875,
      * 0.0012979507446289062,
      * -0.006534576416015625,
      * 0.01318359375,
      * 0.00015938282012939453,
      * 0.0165863037109375,
      * 0.0073089599609375,
      * 0.00341796875,
      * 0.0212554931640625,
      * 0.0310821533203125,
      * 0.014068603515625,
      * 0.007381439208984375,
      * 0.0355224609375,
      * -0.00505828857421875,
      * 0.000885009765625,
      * -0.01025390625,
      * 0.0072021484375,
      * 0.00780487060546875,
      * 0.006282806396484375,
      * 0.0308685302734375,
      * -0.0006375312805175781,
      * -0.0218353271484375,
      * -0.02685546875,
      * 0.00997161865234375,
      * 0.007434844970703125,
      * 0.002223968505859375,
      * 0.00595855712890625,
      * -0.0034198760986328125,
      * 0.0206298828125,
      * 0.007282257080078125,
      * -0.02764892578125,
      * 0.0117034912109375,
      * -0.0038127899169921875,
      * -0.0014963150024414062,
      * -0.01055908203125,
      * -0.0027332305908203125,
      * -0.0115203857421875,
      * 0.00818634033203125,
      * 0.00554656982421875,
      * 0.0024261474609375,
      * 0.00678253173828125,
      * 0.004230499267578125,
      * 0.020050048828125,
      * 0.0102386474609375,
      * 0.001422882080078125,
      * 0.003711700439453125,
      * 0.01244354248046875,
      * -0.0170135498046875,
      * -0.018798828125,
      * 0.01078033447265625,
      * -0.009979248046875,
      * 0.01300811767578125,
      * 0.056488037109375,
      * -0.004413604736328125,
      * 0.0166015625,
      * -0.012725830078125,
      * 0.0054168701171875,
      * 0.0202178955078125,
      * -0.011199951171875,
      * 0.00489044189453125,
      * 0.021728515625,
      * -0.012786865234375,
      * -0.0190887451171875,
      * 0.00225067138671875,
      * -0.005634307861328125,
      * -0.0016546249389648438,
      * -0.0191650390625,
      * -0.00945281982421875,
      * 0.01059722900390625,
      * -0.004474639892578125,
      * 0.002895355224609375,
      * -0.0197601318359375,
      * 0.01522064208984375,
      * 0.020294189453125,
      * -0.0008435249328613281,
      * 0.0146942138671875,
      * -0.00384521484375,
      * -0.005191802978515625,
      * 0.004001617431640625,
      * 0.0135650634765625,
      * 0.004791259765625,
      * -0.0292816162109375,
      * -0.0007848739624023438,
      * -0.0012159347534179688,
      * -0.01163482666015625,
      * 0.0196685791015625,
      * -0.0038890838623046875,
      * -0.0010433197021484375,
      * -0.00586700439453125,
      * 0.01129150390625,
      * 0.007320404052734375,
      * 0.0010194778442382812,
      * -0.0072021484375,
      * 0.0030040740966796875,
      * 0.018951416015625,
      * 0.00518035888671875,
      * -0.01763916015625,
      * -0.0019359588623046875,
      * -0.0262298583984375,
      * 0.0098876953125,
      * -0.0011072158813476562,
      * 0.0001672506332397461,
      * 0.00004214048385620117,
      * 0.0027256011962890625,
      * 0.00542449951171875,
      * 0.004314422607421875,
      * 0.0113983154296875,
      * 0.005657196044921875,
      * 0.0006918907165527344,
      * -0.015655517578125,
      * 0.00855255126953125,
      * 0.0220794677734375,
      * -0.01047515869140625,
      * -0.0056610107421875,
      * -0.004833221435546875,
      * 0.01340484619140625,
      * 0.00069427490234375,
      * 0.0004756450653076172,
      * -0.01165771484375,
      * 0.0253143310546875,
      * 0.02154541015625,
      * 0.0188751220703125,
      * -0.0204925537109375,
      * -0.008697509765625,
      * 0.006465911865234375,
      * -0.007625579833984375,
      * 0.008880615234375,
      * 0.012939453125,
      * -0.00438690185546875,
      * -0.000009715557098388672,
      * 0.0017766952514648438,
      * 0.0166473388671875,
      * -0.0038967132568359375,
      * 0.0013437271118164062,
      * 0.004055023193359375,
      * 0.0084991455078125,
      * -0.00151824951171875,
      * -0.01148223876953125,
      * 0.00846099853515625,
      * 0.01076507568359375,
      * -0.003162384033203125,
      * 0.0011425018310546875,
      * -0.0126495361328125,
      * 0.0184326171875,
      * -0.025909423828125,
      * -0.020233154296875,
      * 0.01401519775390625,
      * 0.00839996337890625,
      * 0.028564453125,
      * -0.0231170654296875,
      * 0.004180908203125,
      * -0.0032024383544921875,
      * 0.0084686279296875,
      * 0.0009431838989257812,
      * -0.0054931640625,
      * -0.0058135986328125,
      * -0.030548095703125,
      * -0.028961181640625,
      * 0.0112762451171875,
      * -0.00994873046875,
      * 0.03363037109375,
      * 0.006496429443359375,
      * -0.0030307769775390625,
      * -0.006259918212890625,
      * 0.01329803466796875,
      * 0.0005383491516113281,
      * 0.004070281982421875,
      * 0.0146942138671875,
      * 0.0207061767578125,
      * 0.01143646240234375,
      * 0.01873779296875,
      * 0.0202484130859375,
      * -0.016326904296875,
      * -0.0120391845703125,
      * 0.0194549560546875,
      * -0.01558685302734375,
      * -0.0193328857421875,
      * -0.0090179443359375,
      * -0.013946533203125,
      * -0.004596710205078125,
      * -0.0016336441040039062,
      * 0.0194854736328125,
      * -0.00963592529296875,
      * -0.0024738311767578125,
      * -0.0278167724609375,
      * -0.0013151168823242188,
      * -0.01219940185546875,
      * 0.0002999305725097656,
      * -0.01123809814453125,
      * 0.0003063678741455078,
      * -0.0013523101806640625,
      * 0.0200347900390625,
      * -0.00414276123046875,
      * -0.0019006729125976562,
      * 0.009521484375,
      * 0.003879547119140625,
      * 0.019317626953125,
      * 0.03680419921875,
      * -0.02362060546875,
      * -0.015869140625,
      * -0.00966644287109375,
      * 0.0046539306640625,
      * -0.0263519287109375,
      * -0.019287109375,
      * 0.002521514892578125,
      * -0.0111541748046875,
      * 0.01117706298828125,
      * -0.0174407958984375,
      * 0.0213165283203125,
      * 0.00933074951171875,
      * 0.0126495361328125,
      * -0.021942138671875,
      * 0.00838470458984375,
      * 0.024993896484375,
      * -0.0038356781005859375,
      * 0.0024566650390625,
      * 0.003543853759765625,
      * -0.017852783203125,
      * 0.00368499755859375,
      * -0.0007586479187011719,
      * 0.028045654296875,
      * -0.0010519027709960938,
      * -0.016876220703125,
      * -0.01061248779296875,
      * 0.006298065185546875,
      * -0.0247955322265625,
      * -0.02667236328125,
      * -0.0165252685546875,
      * 0.0167999267578125,
      * -0.006488800048828125,
      * 0.03338623046875,
      * -0.01044464111328125,
      * -0.01190948486328125,
      * -0.0165863037109375,
      * 0.002948760986328125,
      * -0.0003790855407714844,
      * -0.0115509033203125,
      * 0.0011396408081054688,
      * 0.006381988525390625,
      * -0.0162811279296875,
      * 0.0008649826049804688,
      * 0.01047515869140625,
      * -0.00635528564453125,
      * 0.0146026611328125,
      * -0.01407623291015625,
      * -0.0112152099609375,
      * -0.0166168212890625,
      * 0.004657745361328125,
      * 0.005954742431640625,
      * 0.0153045654296875,
      * 0.005340576171875,
      * -0.01318359375,
      * -0.0300140380859375,
      * 0.030364990234375,
      * -0.01299285888671875,
      * 0.0163726806640625,
      * -0.0032100677490234375,
      * 0.0051727294921875,
      * -0.00946807861328125,
      * -0.0062408447265625,
      * -0.00612640380859375,
      * -0.0183258056640625,
      * 0.00556182861328125,
      * 0.0012388229370117188,
      * -0.03271484375,
      * -0.00980377197265625,
      * -0.0111541748046875,
      * 0.01479339599609375,
      * -0.0083160400390625,
      * 0.00720977783203125,
      * 0.005859375,
      * -0.026580810546875,
      * -0.0251312255859375,
      * 0.006504058837890625,
      * -0.0009675025939941406,
      * 0.0236053466796875,
      * 0.009979248046875,
      * -0.015655517578125,
      * -0.0028972625732421875,
      * -0.00665283203125,
      * 0.0141754150390625,
      * 0.01287078857421875,
      * 0.00391387939453125,
      * 0.0134124755859375,
      * 0.006534576416015625,
      * -0.02020263671875,
      * 0.03863525390625,
      * 0.015716552734375,
      * -0.0267486572265625,
      * 0.018798828125,
      * -0.00983428955078125,
      * 0.0034198760986328125,
      * 0.0012178421020507812,
      * 0.00775909423828125,
      * -0.017486572265625,
      * -0.00011754035949707031,
      * -0.0027370452880859375,
      * 0.0034637451171875,
      * 0.0130767822265625,
      * 0.015869140625,
      * -0.00008922815322875977,
      * 0.010650634765625,
      * -0.01396942138671875,
      * 0.0167999267578125,
      * -0.00408172607421875,
      * -0.0106658935546875,
      * -0.012603759765625,
      * 0.001552581787109375,
      * 0.00110626220703125,
      * -0.0001156926155090332,
      * 0.0282440185546875,
      * 0.00429534912109375,
      * 0.00913238525390625,
      * -0.0017061233520507812,
      * -0.006122589111328125,
      * -0.0027751922607421875,
      * 0.0167388916015625,
      * -0.003261566162109375,
      * 0.00621795654296875,
      * -0.042938232421875,
      * 0.0009565353393554688,
      * -0.0062713623046875,
      * -0.00594329833984375,
      * 0.00408172607421875,
      * 0.0099945068359375,
      * -0.009033203125,
      * -0.01486968994140625,
      * 0.007266998291015625,
      * 0.00977325439453125,
      * 0.001247406005859375,
      * -0.0186004638671875,
      * -0.004413604736328125,
      * -0.02001953125,
      * -0.01111602783203125,
      * -0.0029296875,
      * 0.0073699951171875,
      * 0.005786895751953125,
      * 0.023040771484375,
      * -0.0081787109375,
      * -0.020263671875,
      * -0.0092926025390625,
      * 0.01555633544921875,
      * -0.007114410400390625,
      * -0.01131439208984375,
      * -0.0104522705078125,
      * -0.032745361328125,
      * -0.0151519775390625,
      * 0.01042938232421875,
      * -0.00438690185546875,
      * -0.0006647109985351562,
      * -0.006561279296875,
      * 0.026031494140625,
      * 0.016693115234375,
      * 0.01284027099609375,
      * -0.0187835693359375,
      * -0.0024242401123046875,
      * 0.0014066696166992188,
      * -0.0173492431640625,
      * -0.00949859619140625,
      * -0.01849365234375,
      * -0.010467529296875,
      * -0.02410888671875,
      * -0.00420379638671875,
      * 0.00885009765625,
      * -0.0017070770263671875,
      * -0.0024929046630859375,
      * -0.0095977783203125,
      * 0.004573822021484375,
      * -0.01953125,
      * -0.01708984375,
      * 0.01172637939453125,
      * -0.006504058837890625,
      * 0.009552001953125,
      * -0.0280303955078125,
      * -0.00839996337890625,
      * 0.01335906982421875,
      * -0.0126800537109375,
      * -0.006420135498046875,
      * -0.01331329345703125,
      * -0.0008025169372558594,
      * -0.00759124755859375,
      * 0.0139312744140625,
      * 0.030120849609375,
      * -0.01800537109375,
      * 0.01078033447265625,
      * -0.01373291015625,
      * -0.000728607177734375,
      * 0.00391387939453125,
      * 0.010528564453125,
      * -0.01090240478515625,
      * -0.03143310546875,
      * 0.0270538330078125,
      * -0.005199432373046875,
      * 0.00843048095703125,
      * 0.0181732177734375,
      * 0.02789306640625,
      * 0.01125335693359375,
      * 0.01421356201171875,
      * 0.0229644775390625,
      * -0.02001953125,
      * 0.017791748046875,
      * 0.01983642578125,
      * -0.005634307861328125,
      * -0.047607421875,
      * -0.006214141845703125,
      * -0.015289306640625,
      * 0.0302276611328125,
      * -0.005649566650390625,
      * 0.01507568359375,
      * 0.013946533203125,
      * 0.0023174285888671875,
      * -0.005634307861328125,
      * -0.007236480712890625,
      * 0.0184478759765625,
      * 0.01319122314453125,
      * -0.0105438232421875,
      * 0.01433563232421875,
      * -0.0030803680419921875,
      * -0.0008249282836914062,
      * -0.0166168212890625,
      * -0.0007042884826660156,
      * -0.006862640380859375,
      * 0.0096282958984375,
      * 0.00267791748046875,
      * 0.0099945068359375,
      * 0.0199127197265625,
      * -0.006862640380859375,
      * 0.00717926025390625,
      * 0.0004661083221435547,
      * -0.01050567626953125,
      * -0.01099395751953125,
      * 0.005275726318359375,
      * 0.007457733154296875,
      * 0.002841949462890625,
      * -0.00806427001953125,
      * 0.018798828125,
      * 0.020050048828125,
      * 0.008087158203125,
      * 0.0104522705078125,
      * -0.0180511474609375,
      * -0.005413055419921875,
      * -0.0194091796875,
      * -0.009246826171875,
      * 0.03192138671875,
      * -0.01476287841796875,
      * 0.005096435546875,
      * 0.0182342529296875,
      * -0.0085906982421875,
      * 0.03399658203125,
      * -0.0288543701171875,
      * -0.01751708984375,
      * -0.005413055419921875,
      * 0.02056884765625,
      * 0.004161834716796875,
      * -0.01535797119140625,
      * -0.00833892822265625,
      * 0.024261474609375,
      * 0.008941650390625,
      * -0.00798797607421875,
      * 0.0180206298828125,
      * 0.004795074462890625,
      * 0.00009512901306152344,
      * -0.0025691986083984375,
      * 0.0190582275390625,
      * -0.004985809326171875,
      * -0.00629425048828125,
      * -0.00795745849609375,
      * 0.0021514892578125,
      * -0.0005998611450195312,
      * 0.003795623779296875,
      * -0.0202178955078125,
      * 0.005092620849609375,
      * -0.01477813720703125,
      * 0.0227813720703125,
      * 0.00457000732421875,
      * -0.018707275390625,
      * -0.0031261444091796875,
      * -0.00800323486328125,
      * 0.0173797607421875,
      * 0.0152740478515625,
      * 0.0203704833984375,
      * -0.00963592529296875,
      * -0.007404327392578125,
      * 0.0161285400390625,
      * -0.0118865966796875,
      * 0.01250457763671875,
      * 0.0230255126953125,
      * 0.00615692138671875,
      * -0.00434112548828125,
      * 0.0008630752563476562,
      * -0.0029430389404296875,
      * -0.034515380859375,
      * 0.00537109375,
      * -0.02783203125,
      * -0.0169830322265625,
      * 0.002353668212890625,
      * 0.007724761962890625,
      * -0.0075836181640625,
      * -0.0101165771484375,
      * 0.00887298583984375,
      * -0.00795745849609375,
      * 0.0036334991455078125,
      * -0.00528717041015625,
      * 0.00737762451171875,
      * 0.005046844482421875,
      * 0.0006046295166015625,
      * 0.01253509521484375,
      * 0.0062103271484375,
      * -0.00020372867584228516,
      * 0.0265350341796875,
      * -0.0086669921875,
      * -0.006175994873046875,
      * 0.01145172119140625,
      * 0.006366729736328125,
      * -0.01165771484375,
      * -0.0002923011779785156,
      * 0.0211181640625,
      * -0.0157470703125,
      * -0.024444580078125,
      * -0.0182037353515625,
      * 0.0049896240234375,
      * -0.005290985107421875,
      * -0.0281829833984375,
      * 0.0185089111328125,
      * -0.0004634857177734375,
      * 0.0055999755859375,
      * -0.042724609375,
      * 0.00141143798828125,
      * -0.00583648681640625,
      * 0.00734710693359375,
      * 0.020263671875,
      * -0.00428009033203125,
      * 0.017547607421875,
      * 0.005077362060546875,
      * 0.00977325439453125,
      * -0.0131988525390625,
      * 0.0013093948364257812,
      * -0.03369140625,
      * 0.01107025146484375,
      * -0.0057525634765625,
      * 0.01319122314453125,
      * 0.0104522705078125,
      * -0.00290679931640625,
      * 0.0031566619873046875,
      * -0.0056915283203125,
      * -0.0091705322265625,
      * -0.003322601318359375,
      * -0.0164947509765625,
      * -0.01422882080078125,
      * -0.01483154296875,
      * 0.00301361083984375,
      * -0.01041412353515625,
      * -0.01543426513671875,
      * 0.006023406982421875,
      * -0.010650634765625,
      * -0.0023250579833984375,
      * -0.0079498291015625,
      * -0.1258544921875,
      * 0.01090240478515625,
      * -0.01548004150390625,
      * -0.019866943359375,
      * 0.00490570068359375,
      * -0.01334381103515625,
      * -0.00223541259765625,
      * 0.0258026123046875,
      * -0.0203399658203125,
      * 0.02154541015625,
      * -0.00986480712890625,
      * -0.01299285888671875,
      * 0.01312255859375,
      * -0.005008697509765625,
      * 0.0107879638671875,
      * -0.0009927749633789062,
      * -0.016510009765625,
      * -0.01059722900390625,
      * -0.01181793212890625,
      * -0.008056640625,
      * -0.01555633544921875,
      * -0.00658416748046875,
      * -0.00809478759765625,
      * -0.00284576416015625,
      * -0.00493621826171875,
      * 0.031585693359375,
      * -0.00368499755859375,
      * 0.00476837158203125,
      * -0.00542449951171875,
      * 0.014617919921875,
      * -0.0050201416015625,
      * -0.0007348060607910156,
      * 0.00885772705078125,
      * 0.00856781005859375,
      * 0.0008459091186523438,
      * -0.01076507568359375,
      * 0.0170135498046875,
      * 0.01442718505859375,
      * -0.01184844970703125,
      * 0.002071380615234375,
      * 0.017822265625,
      * -0.006038665771484375,
      * -0.032928466796875,
      * -0.008758544921875,
      * 0.0243988037109375,
      * 0.00665283203125,
      * 0.000006973743438720703,
      * 0.0176849365234375,
      * 0.0002262592315673828,
      * -0.01476287841796875,
      * -0.025634765625,
      * -0.00511932373046875,
      * 0.00720977783203125,
      * 0.0225982666015625,
      * 0.01386260986328125,
      * -0.0016393661499023438,
      * 0.00162506103515625,
      * -0.027618408203125,
      * 0.0013341903686523438,
      * -0.0193939208984375,
      * -0.0097198486328125,
      * 0.00626373291015625,
      * -0.007080078125,
      * 0.01617431640625,
      * -0.01557159423828125,
      * 0.023345947265625,
      * -0.024444580078125,
      * 0.0141754150390625,
      * 0.01016998291015625,
      * 0.002315521240234375,
      * 0.00472259521484375,
      * -0.0003819465637207031,
      * -0.0084228515625,
      * -0.01213836669921875,
      * -0.0011091232299804688,
      * 0.01534271240234375,
      * 0.0014905929565429688,
      * -0.006587982177734375,
      * -0.01006317138671875,
      * 0.00780487060546875,
      * 0.0008916854858398438,
      * 0.0161895751953125,
      * -0.024993896484375,
      * -0.02215576171875,
      * -0.0120086669921875,
      * 0.0026187896728515625,
      * 0.024078369140625,
      * -0.00452423095703125,
      * -0.0185699462890625,
      * 0.0268096923828125,
      * 0.0052947998046875,
      * -0.00006139278411865234,
      * -0.010650634765625,
      * 0.01458740234375,
      * 0.01282501220703125,
      * -0.0167999267578125,
      * 0.0188751220703125,
      * -0.01052093505859375,
      * -0.0012674331665039062,
      * 0.012786865234375,
      * 0.005916595458984375,
      * 0.005344390869140625,
      * -0.0094451904296875,
      * -0.007770538330078125,
      * -0.0231170654296875,
      * 0.003391265869140625,
      * 0.02685546875,
      * -0.005889892578125,
      * 0.01861572265625,
      * 0.0111541748046875,
      * -0.00516510009765625,
      * 0.01233673095703125,
      * 0.01554107666015625,
      * 0.0222625732421875,
      * 0.0044403076171875,
      * -0.01354217529296875,
      * 0.008758544921875,
      * 0.019500732421875,
      * -0.0031681060791015625,
      * 0.0066986083984375,
      * 0.006488800048828125,
      * 0.01105499267578125,
      * -0.01206207275390625,
      * 0.0016431808471679688,
      * 0.0036678314208984375,
      * 0.029693603515625,
      * -0.0020503997802734375,
      * -0.0024700164794921875,
      * 0.00518035888671875,
      * 0.00983428955078125,
      * -0.0037689208984375,
      * -0.003902435302734375,
      * 0.01502227783203125,
      * -0.0017852783203125,
      * -0.0178070068359375,
      * -0.0167388916015625,
      * 0.018829345703125,
      * -0.0194091796875,
      * -0.0113067626953125,
      * 0.004711151123046875,
      * -0.00020241737365722656,
      * 0.0071868896484375,
      * -0.0239105224609375,
      * -0.006504058837890625,
      * -0.0045928955078125,
      * 0.0014019012451171875,
      * -0.005496978759765625,
      * -0.0017871856689453125,
      * -0.0002372264862060547,
      * -0.0132598876953125,
      * -0.016021728515625,
      * 0.0056304931640625,
      * 0.007282257080078125,
      * 0.0098876953125,
      * -0.005428314208984375,
      * -0.00949859619140625,
      * 0.017730712890625,
      * 0.007671356201171875,
      * -0.00492095947265625,
      * -0.0005741119384765625,
      * 0.0140533447265625,
      * -0.012298583984375,
      * 0.00589752197265625,
      * 0.0037822723388671875,
      * 0.00876617431640625,
      * -0.024993896484375,
      * -0.00010442733764648438,
      * -0.002567291259765625,
      * -0.0017833709716796875,
      * -0.0256805419921875,
      * 0.015838623046875,
      * 0.007625579833984375,
      * -0.0019178390502929688,
      * -0.00026702880859375,
      * -0.005344390869140625,
      * -0.01239776611328125,
      * -0.0263671875,
      * 0.0136260986328125,
      * -0.01092529296875,
      * -0.0215911865234375,
      * 0.017822265625,
      * 0.012451171875,
      * -0.0262451171875,
      * -0.0081787109375,
      * 0.01922607421875,
      * 0.00909423828125,
      * -0.0014715194702148438,
      * 0.0149383544921875,
      * 0.007434844970703125,
      * -0.012359619140625,
      * 0.01435089111328125,
      * 0.0122222900390625,
      * -0.017486572265625,
      * 0.01247406005859375,
      * -0.0029144287109375,
      * 0.01019287109375,
      * -0.0011739730834960938,
      * -0.020660400390625,
      * -0.0184478759765625,
      * 0.0011091232299804688,
      * -0.00201416015625,
      * -0.019683837890625,
      * 0.0095672607421875,
      * 0.0073699951171875,
      * 0.012115478515625,
      * -0.005718231201171875,
      * 0.001373291015625,
      * 0.01389312744140625,
      * 0.0010652542114257812,
      * 0.0148162841796875,
      * 0.01108551025390625,
      * -0.018829345703125,
      * -0.01104736328125,
      * 0.00006514787673950195,
      * 0.01247406005859375,
      * -0.01390838623046875,
      * 0.0168304443359375,
      * -0.005435943603515625,
      * 0.00417327880859375,
      * -0.01305389404296875,
      * 0.0080718994140625,
      * -0.001712799072265625,
      * 0.001911163330078125,
      * -0.0029621124267578125,
      * -0.017486572265625,
      * -0.0049591064453125,
      * 0.004177093505859375,
      * 0.0047149658203125,
      * 0.00214385986328125,
      * -0.0010242462158203125,
      * -0.00490570068359375,
      * -0.004901885986328125,
      * 0.007213592529296875,
      * -0.0263671875,
      * -0.01593017578125,
      * 0.00952911376953125,
      * -0.0235748291015625,
      * -0.00835418701171875,
      * 0.014190673828125,
      * -0.0190582275390625,
      * 0.004863739013671875  
      ],
    * "index": 0,
    * "object": "embedding"  
  }  
],
* "id": "embd-5263180e0bf441f38c144330347f3e88",
* "model": "intfloat/e5-mistral-7b-instruct",
* "object": "list",
* "usage": {
  * "completion_tokens": 0,
  * "prompt_tokens": 28,
  * "total_tokens": 28  
}
}`

## [](#tag/Batch)Batch

Create large batches of API requests to run asynchronously.

## [](#tag/Batch/operation/createBatch)Creates and executes a batch. 

Creates and executes a batch from an uploaded file of requests.

##### Authorizations:

_ApiKeyAuth_

##### header Parameters

| X-cb-batch-record-expiry | integer optional request header to override the batching records expiry value. The default batch expiry value is 7 days. |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| X-cb-debug               | string Optinal debug flag to see more response headers                                                                   |

##### Request Body schema: application/json

required

| input\_file\_idrequired    | string The ID of an uploaded file that contains requests for the new batch. See [upload file](/docs/api-reference/files/create) for how to upload a file. Your input file must be formatted as a [JSONL file](/docs/api-reference/batch/request-input), and must be uploaded with the purpose batch.                                            |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| endpointrequired           | string Enum: "/v1/chat/completions" "/v1/embeddings" "/v1/completions" The endpoint to be used for all requests in the batch. Currently /v1/chat/completions, /v1/completions, and /v1/embeddings are supported. Note that /v1/embeddings batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch. |
| completion\_windowrequired | string Value: "168h" The time frame within which the batch should be processed. Currently only 168h is supported. Timeout happens after the window time. This is not a SLA binding.                                                                                                                                                             |

### Responses

**200** 

Batch created successfully.

**401** 

Unauthorized

post/batches

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/batches

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "input_file_id": "file-b0450d53-0f58-438f-b7a3-fa9eb41d540b-ref-ac6073f8d30fe64940f44351fc9d71da",
* "endpoint": "/v1/chat/completions",
* "completion_window": "168h"
}`

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "batch-958c3a0701a5587bb2638022431031eb-d4054b6941c24998901115178454309a",
* "object": "batch",
* "endpoint": "/v1/chat/completions",
* "input_file_id": "file-i958c3a0701a5587bb2638022431031eb-e8aa2146efb9451a8706b4717e063138",
* "completion_window": "immediate",
* "status": "finalizing",
* "output_file_id": "file-o958c3a0701a5587bb2638022431031eb-6bc3a161c74046f19be805ac31d11a4b",
* "error_file_id": "file-e958c3a0701a5587bb2638022431031eb-59144fbf1d8e4d3cbb0ab139f06a261b",
* "created_at": 1761699036,
* "in_progress_at": null,
* "expires_at": null,
* "finalizing_at": 1761699036,
* "completed_at": null,
* "failed_at": null,
* "expired_at": null,
* "cancelling_at": null,
* "cancelled_at": null,
* "request_counts": {
  * "total": 9,
  * "completed": 0,
  * "failed": 0,
  * "cancelled": 0  
},
* "metadata": null
}`

## [](#tag/Batch/operation/listBatches)List your batches. 

##### Authorizations:

_ApiKeyAuth_

##### query Parameters

| after | string A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| limit | integer Default: 20 A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.                                                                                                                                                         |

##### header Parameters

| X-cb-debug | boolean Optinal debug flag to see more response headers |
| ---------- | ------------------------------------------------------- |

### Responses

**200** 

Batch listed successfully.

**401** 

Unauthorized

get/batches

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/batches

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "deepseek-ai/DeepSeek-R1-Distill-Llama-8B": [ ],
* "embedding-model-nim-primary": [ ],
* "embedding-model-nim-primary-passage": [ ],
* "embedding-model-nim-primary-query": [ ],
* "embedding-model-nim-secondary": [ ],
* "embedding-model-nim-secondary-passage": [ ],
* "embedding-model-nim-secondary-query": [ ],
* "embedding-model-primary": [ ],
* "embedding-model-secondary": [ ],
* "language-model-nim-primary": [
  * "batch-958c3a0701a5587bb2638022431031eb-d4054b6941c24998901115178454309a"  
],
* "language-model-primary": [ ],
* "language-model-secondary": [ ],
* "language-model-tertiary": [ ]
}`

## [](#tag/Batch/operation/retrieveBatch)Retrieves a batch. 

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

| batch\_idrequired | string The ID of the batch to retrieve. |
| ----------------- | --------------------------------------- |

##### header Parameters

| X-cb-debug | boolean Optinal debug flag to see more response headers |
| ---------- | ------------------------------------------------------- |

### Responses

**200** 

Batch retrieved successfully.

**401** 

Unauthorized

get/batches/{batch\_id}

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/batches/{batch\_id}

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "batch-958c3a0701a5587bb2638022431031eb-d4054b6941c24998901115178454309a",
* "object": "batch",
* "endpoint": "/v1/chat/completions",
* "input_file_id": "file-i958c3a0701a5587bb2638022431031eb-e8aa2146efb9451a8706b4717e063138",
* "completion_window": "immediate",
* "status": "completed",
* "output_file_id": "file-o958c3a0701a5587bb2638022431031eb-6bc3a161c74046f19be805ac31d11a4b",
* "error_file_id": "file-e958c3a0701a5587bb2638022431031eb-59144fbf1d8e4d3cbb0ab139f06a261b",
* "created_at": 1761699036,
* "in_progress_at": 1761699037,
* "expires_at": null,
* "finalizing_at": 1761699036,
* "completed_at": 1761699053,
* "failed_at": null,
* "expired_at": null,
* "cancelling_at": null,
* "cancelled_at": null,
* "request_counts": {
  * "total": 9,
  * "completed": 9,
  * "failed": 0,
  * "cancelled": 0  
},
* "metadata": null
}`

## [](#tag/Batch/operation/cancelBatch)Cancels an in-progress batch. 

Cancels an in-progress batch. Partial results might be there in the collection before cancellation.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

| batch\_idrequired | string The ID of the batch to cancel. |
| ----------------- | ------------------------------------- |

##### header Parameters

| X-cb-debug | boolean Optinal debug flag to see more response headers |
| ---------- | ------------------------------------------------------- |

### Responses

**200** 

Batch is cancelling. Returns the cancelling batch's details.

**401** 

Unauthorized

post/batches/{batch\_id}/cancel

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/batches/{batch\_id}/cancel

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "batch-958c3a0701a5587bb2638022431031eb-b8e8e24df73343c2b909e3d9a243eadc",
* "object": "batch",
* "endpoint": "/v1/chat/completions",
* "input_file_id": "file-i958c3a0701a5587bb2638022431031eb-e8aa2146efb9451a8706b4717e063138",
* "completion_window": "immediate",
* "status": "in_progress",
* "output_file_id": "file-o958c3a0701a5587bb2638022431031eb-c56d09fdb5d04f38b0cc78fd482d65cd",
* "error_file_id": "file-e958c3a0701a5587bb2638022431031eb-f3bca8b4d2ae4c608b003c3b03515cc3",
* "created_at": 1761699780,
* "in_progress_at": 1761699781,
* "expires_at": null,
* "finalizing_at": 1761699780,
* "completed_at": null,
* "failed_at": null,
* "expired_at": null,
* "cancelling_at": null,
* "cancelled_at": null,
* "request_counts": {
  * "total": 9,
  * "completed": 0,
  * "failed": 0,
  * "cancelled": 0  
},
* "metadata": null
}`

## [](#tag/Files)Files

Files are used to upload documents that can be used with features like Assistants and Fine-tuning.

## [](#tag/Files/operation/createFile)Upload a file that can be used with batch. 

Upload a file that can be used across various endpoints. The Batch API only supports `.jsonl` files and loaded into the batch configured couchbase collection. The input also has a specific required [format](/docs/api-reference/batch/request-input). Please [contact us](https://help.openai.com/) if you need to increase these storage limits.

##### Authorizations:

_ApiKeyAuth_

##### header Parameters

| X-cb-debug              | boolean Optinal debug flag to see more response headers                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| X-cb-file-record-expiry | integer optional request header to override the file uploaded records expiry value. The default file record expiry is 30 days. |

##### Request Body schema: multipart/form-data

required

| filerequired    | string <binary\> The File object (not file name) to be uploaded.                                                  |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| purposerequired | string Value: "batch" The intended purpose of the uploaded file. Use "batch" for [Batch API](/docs/guides/batch). |

### Responses

**200** 

OK

**401** 

Unauthorized

post/files

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/files

### Response samples 

* 200
* 401

Content type

application/json

Copy

`{
* "id": "file-abc93f3d-adc0-4a8b-83d0-6b1ef19caa0b-ref-658109dca69576e2af3e6747aa69cec0",
* "object": "file",
* "bytes": 10311,
* "created_at": 1733860812,
* "filename": "batch_llama.jsonl",
* "purpose": "batch"
}`

## [](#tag/Files/operation/listFiles)Returns a list of files. 

##### Authorizations:

_ApiKeyAuth_

##### query Parameters

| limit | integer Default: 10000 A limit on the number of objects to be returned. Limit can range between 1 and 10,000, and the default is 10,000.                                                                                                                                               |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| order | string Default: "desc" Enum: "asc" "desc" Sort order by the created\_at timestamp of the objects. asc for ascending order and desc for descending order.                                                                                                                               |
| after | string A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list. |

##### header Parameters

| X-cb-debug | boolean Optinal debug flag to see more response headers |
| ---------- | ------------------------------------------------------- |

### Responses

**200** 

OK

**401** 

Unauthorized

get/files

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/files

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "meta-llama/Llama-3.1-8B-Instruct": [
  * {
    * "id": "file-abc93f3d-adc0-4a8b-83d0-6b1ef19caa0b-ref-658109dca69576e2af3e6747aa69cec0",
    * "object": "file",
    * "bytes": 10311,
    * "created_at": 1733860812,
    * "filename": "batch_llama.jsonl",
    * "active": true,
    * "purpose": "batch"  
  }  
],
* "meta-llama/Llama-Guard-3-8B": [
  * {
    * "id": "file-abc93f3d-adc0-4a8b-83d0-6b1ef19caa0b-ref-658109dca69576e2af3e6747aa69cec0",
    * "object": "file",
    * "bytes": 10311,
    * "created_at": 1733860812,
    * "filename": "batch_llama.jsonl",
    * "active": true,
    * "purpose": "batch"  
  }  
]
}`

## [](#tag/Files/operation/retrieveFile)Returns information about a specific file. 

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

| file\_idrequired | string The ID of the file to use for this request. |
| ---------------- | -------------------------------------------------- |

##### header Parameters

| X-cb-debug | boolean Optinal debug flag to see more response headers |
| ---------- | ------------------------------------------------------- |

### Responses

**200** 

OK

get/files/{file\_id}

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/files/{file\_id}

### Response samples 

* 200

Content type

application/json

Copy

`{
* "id": "file-abc93f3d-adc0-4a8b-83d0-6b1ef19caa0b-ref-658109dca69576e2af3e6747aa69cec0",
* "object": "file",
* "bytes": 10311,
* "created_at": 1733860812,
* "filename": "batch_llama.jsonl",
* "active": true,
* "purpose": "batch"
}`

## [](#tag/Files/operation/deleteFile)Delete a file. 

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

| file\_idrequired | string The ID of the file to use for this request. |
| ---------------- | -------------------------------------------------- |

### Responses

**200** 

OK

**401** 

Unauthorized

delete/files/{file\_id}

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/files/{file\_id}

### Response samples 

* 200
* 401

Content type

application/json

Copy

`{
* "id": "file-i958c3a0701a5587bb2638022431031eb-db4144aa14a94422b5ef314e9bbf0a8f",
* "object": "file",
* "deleted": true
}`

## [](#tag/Files/operation/downloadFile)Returns the contents of the specified file. 

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

| file\_idrequired | string The ID of the file to use for this request. |
| ---------------- | -------------------------------------------------- |

##### header Parameters

| X-cb-debug | boolean Optinal debug flag to see more response headers |
| ---------- | ------------------------------------------------------- |

### Responses

**200** 

OK

**401** 

Unauthorized

get/files/{file\_id}/content

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/files/{file\_id}/content

### Response samples 

* 200
* 401

Content type

application/json

Copy

`"{ \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"Explain the differences between futures, options, and swaps in terms of risk management.\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-1\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do private equity investments differ from public equity, and what unique risks do they present?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-10\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How does one calculate the optimal hedge ratio for a portfolio using cointegration analysis and error correction models?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-11\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What are the mathematical foundations of the Hull-White interest rate model and how does it compare to Heath-Jarrow-Morton framework?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-12\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do you implement a Kalman filter for dynamic asset allocation in a multi-factor portfolio optimization context?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-13\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What is the mathematical derivation of the SABR volatility model and its applications in options pricing?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-14\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do you implement a copula-based approach to modeling default correlation in credit derivatives pricing?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-15\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What are the mathematical principles behind regime-switching models in volatility forecasting using Hidden Markov Models?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-16\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do you derive and implement the Chen model for interest rate derivatives pricing?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-17\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What is the mathematical framework for implementing a multi-curve bootstrapping approach in interest rate modeling post-2008?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-18\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do you implement a quantum-resistant cryptographic system for high-frequency trading algorithms?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-19\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What are structured financial products, and how do they differ from traditional investments?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-2\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What are the mathematical foundations of polynomial chaos expansion methods in financial risk modeling?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-20\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do you calculate the J-curve effect in private equity portfolios and what are its implications for portfolio construction?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-21\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What methods are used to calculate dry powder ratios in private equity and how do they impact fund performance metrics?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-22\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do you model the optimal capital call strategy in private equity considering both opportunity costs and commitment risks?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-23\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What are the quantitative methods for calculating private equity NAV adjustments during market dislocations?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-24\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do you implement a Monte Carlo simulation for private equity portfolio construction considering vintage year diversification?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-25\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What mathematical models best predict private equity fund manager persistence across multiple funds?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-26\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do you calculate the optimal commitment pacing strategy for a private equity portfolio using stochastic programming?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-27\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What methods are used to model the correlation between private equity returns and public market equivalents (PME)?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-28\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do you implement a factor-based approach to private equity portfolio attribution analysis?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-29\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do credit default swaps function, and what risks do they manage?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-3\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"Describe the structure of collateralized debt obligations and the risks involved.\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-4\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What distinguishes ETFs from mutual funds, particularly regarding liquidity?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-5\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"How do companies use interest rate swaps to manage exposure to interest rate fluctuations?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-6\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"Discuss the advantages of convertible bonds for both issuers and investors.\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-7\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What is the process of securitization in asset-backed securities?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-8\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" } { \"body\": { \"max_tokens\": 250, \"messages\": [ { \"content\": \"You are a helpful assistant.\", \"role\": \"system\" }, { \"content\": \"What are common options trading strategies, and when are they most effective?\", \"role\": \"user\" } ], \"model\": \"meta-llama/Llama-3.1-8B-Instruct\" }, \"custom_id\": \"request-9\", \"method\": \"POST\", \"url\": \"/v1/chat/completions\" }"`

## [](#tag/Models)Models

List and describe the various models available in the API.

## [](#tag/Models/operation/listModels)Lists the currently available models. 

Lists the currently available models, and provides basic information about each one such as the owner and availability.

##### Authorizations:

_ApiKeyAuth_

### Responses

**200** 

OK

**401** 

Unauthorized

**5XX** 

Server Error

get/models

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/models

### Response samples 

* 200
* 401
* 5XX

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "object": "list",
* "data": [
  * {
    * "id": "nvidia-llama-3.2-nv-embedqa-1b-v2::b81c7797-b64d-41b1-b185-2b04e7d37407",
    * "deployment_id": "b81c7797-b64d-41b1-b185-2b04e7d37407",
    * "deployment_name": "centraladelegoldberg",
    * "model_id": "b81c7797-b64d-41b1-b185-2b04e7d37407",
    * "model_name": "nvidia/llama-3.2-nv-embedqa-1b-v2",
    * "server_kind": "nim",
    * "status": "healthy",
    * "object": "model",
    * "owned_by": "model-service"  
  },
  * {
    * "id": "nvidia-llama-3.2-nv-embedqa-1b-v2-passage::b81c7797-b64d-41b1-b185-2b04e7d37407-passage",
    * "deployment_id": "b81c7797-b64d-41b1-b185-2b04e7d37407-passage",
    * "deployment_name": "centraladelegoldberg-passage",
    * "model_id": "b81c7797-b64d-41b1-b185-2b04e7d37407-passage",
    * "model_name": "nvidia/llama-3.2-nv-embedqa-1b-v2-passage",
    * "server_kind": "nim",
    * "status": "healthy",
    * "object": "model",
    * "owned_by": "model-service"  
  },
  * {
    * "id": "nvidia-llama-3.2-nv-embedqa-1b-v2-query::b81c7797-b64d-41b1-b185-2b04e7d37407-query",
    * "deployment_id": "b81c7797-b64d-41b1-b185-2b04e7d37407-query",
    * "deployment_name": "centraladelegoldberg-query",
    * "model_id": "b81c7797-b64d-41b1-b185-2b04e7d37407-query",
    * "model_name": "nvidia/llama-3.2-nv-embedqa-1b-v2-query",
    * "server_kind": "nim",
    * "status": "healthy",
    * "object": "model",
    * "owned_by": "model-service"  
  }  
]
}`

## [](#tag/Models/operation/retrieveModel)Retrieves a model instance details. 

Retrieves a model instance, providing basic information about the model.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

| modelrequired | string Example: gpt-4o-miniThe ID of the model to use for this request |
| ------------- | ---------------------------------------------------------------------- |

##### header Parameters

| X-cb-debug            | boolean Optinal debug flag to see more response headers                                          |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| X-cb-max-retries      | integer optional overriding request header to set a maximum nunber of retries if a request fails |
| X-cb-request-duration | integer optional request header to set the request timeout                                       |

### Responses

**200** 

OK

**401** 

Unauthorized

**5XX** 

Server Error

get/models/{model}

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/models/{model}

### Response samples 

* 200
* 401

Content type

application/json

Copy

`{
* "id": "meta-llama-3.1-8b-instruct::language-model-nim-primary",
* "deployment_id": "language-model-nim-primary",
* "deployment_name": "Llama 3.1 8B Instruct (NIM Primary)",
* "model_id": "language-model-nim-primary",
* "model_name": "meta/llama-3.1-8b-instruct",
* "server_kind": "nim",
* "status": "healthy",
* "object": "model",
* "created": 1761849742,
* "owned_by": "model-service"
}`

## [](#tag/Moderations)Moderations

## [](#tag/Moderations/operation/post-moderations)Classifies any potentially harmful text 

##### Authorizations:

_ApiKeyAuth_

##### header Parameters

| X-cb-debug                | boolean Optinal debug flag to see more response headers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X-cb-max-retries          | integer Default: 3 optional overriding request header to set a maximum number of retries if a model server request fails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| X-cb-request-duration     | integer optional request header to set the request timeout                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| X-cb-routing-strategy     | string Default: round-robin Enum: "round-robin" "least-latency" "throughput" "least-requests" "least-cache-usage" "prefix-aware" optional request header to set routing strategy for load balancing of requests among the same model instances. Here is the brief summary on each strategy: round-robin: Round-robin routing, this would perform approximate round-robin routing. This is ideal where the applications benefits from uniform distribution of requests. least-latency: Least latency routing, this would select the model with the least P95 latency. This policy is ideal for applications where total turn around time of requests is important. Such as non-streaming requests. throughput: Throughput routing, this would select the model with the highest throughput.This policy is ideal for applications where minimizing inter-token-latency is important. Such as streaming requests. least-cache-usage: Least cache usage routing, this would select the model with the least cache usage. This policy is ideal for applications where cache saturation is important. least-requests: Least request routing, this would select the model with the least number of requests. This policy is ideal where the request queue minimization is important. prefix-aware: Prefix aware routing, this would select the model with the highest KV cache reuse. This policy is ideal for applications where a same prefix is used for multiple requests. Note that the KVCache (aka prefix caching) is turned on to improve the perceived response time of an LLM query, (Time-To-First-Token). By storing complete or partial results of previously seen queries, it saves the recomputation cost when part of the prompt has been processed before, a common occurrence in LLM inference. |
| X-cb-model-ref            | string optional overriding request header to use a specific model, value is the deployed model UUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| X-cb-guardrail-model-ref  | string optional request header to set the model id for guardrails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| X-cb-jailbreak-model-ref  | string optional overriding request header to set a jailbreak model with its id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| X-cb-jailbreak-threshold  | number \[ -1 .. 1 \] optional header to override the default jailbreak threshold value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| X-cb-jailbreak-model-name | string optional header to override the model name for the jailbreak                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

##### Request Body schema: application/json

| inputrequired | string Input text to classify.                          |
| ------------- | ------------------------------------------------------- |
| model         | string Optional moderation model you would like to use. |

### Responses

**200** 

OK

**401** 

Unauthorized

**422** 

Unprocessable Entity (WebDAV)

**429** 

Too Many Requests

**5XX** 

Server Error

post/moderations

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/moderations

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "input": "Write a proposal for a new drug trafficking operation in Shanghai",
* "model": "nvidia/llama-3.1-nemoguard-8b-content-safety"
}`

### Response samples 

* 200
* 401
* 422
* 429
* 5XX

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "flagged": true,
* "categories": {
  * "sexual": false,
  * "sexual/minors": false,
  * "harassment": true,
  * "harassment/threatening": true,
  * "hate": true,
  * "hate/threatening": true,
  * "illicit": true,
  * "illicit/violent": false,
  * "self-harm": false,
  * "self-harm/intent": false,
  * "self-harm/instructions": false,
  * "violence": false,
  * "violence/graphic": false  
},
* "category_scores": {
  * "sexual": 0,
  * "sexual/minors": 0,
  * "harassment": 0.33,
  * "harassment/threatening": 1,
  * "hate": 1,
  * "hate/threatening": 1,
  * "illicit": 1,
  * "illicit/violent": 0,
  * "self-harm": 0,
  * "self-harm/intent": 0,
  * "self-harm/instructions": 0,
  * "violence": 0,
  * "violence/graphic": 0  
},
* "category_applied_input_types": {
  * "sexual": [
    * "Text"  
  ],
  * "sexual/minors": [
    * "Text"  
  ],
  * "harassment": [
    * "Text"  
  ],
  * "harassment/threatening": [
    * "Text"  
  ],
  * "hate": [
    * "Text"  
  ],
  * "hate/threatening": [
    * "Text"  
  ],
  * "illicit": [
    * "Text"  
  ],
  * "illicit/violent": [
    * "Text"  
  ],
  * "self-harm": [
    * "Text"  
  ],
  * "self-harm/intent": [
    * "Text"  
  ],
  * "self-harm/instructions": [
    * "Text"  
  ],
  * "violence": [
    * "Text"  
  ],
  * "violence/graphic": [
    * "Text"  
  ]  
}
}`

## [](#tag/Service)Service

## [](#tag/Service/operation/serviceinfo)Gets model service information 

Gets the model service information.

##### Authorizations:

_ApiKeyAuth_

### Responses

**200** 

OK

**401** 

Unauthorized

**5XX** 

Server Error

get/info

https://df5awoi31iuodp8j.cloud.couchbase.com/v1/info

### Response samples 

* 200
* 401
* 5XX

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "build_time": "2025-10-20T20:22:52-0700",
* "commit_hash": "67b4cc5",
* "defaults": {
  * "audit_log_max_age": 30,
  * "audit_log_max_backups": 512,
  * "audit_log_max_size": 100,
  * "default_cache_expiry_duration": 3600000000000,
  * "default_completion_request_timeout": 300000000000,
  * "default_embedding_request_timeout": 60000000000,
  * "default_max_file_upload_size": 104857600,
  * "default_max_request_count": 1000,
  * "default_routing_metrics_refresh_interval": 300,
  * "default_routing_metrics_scrape_interval": 30,
  * "max_cache_expiry_duration": 604800000000000,
  * "max_tokens": 512,
  * "temperature": 0.8  
},
* "max_requests_per_minute": 1000,
* "models": [
  * {
    * "id": "meta-llama3-8b-instruct::be1bf0c3-272c-4268-8302-5886cbc61672",
    * "deployment_id": "be1bf0c3-272c-4268-8302-5886cbc61672",
    * "deployment_name": "ecrujiewu",
    * "model_id": "be1bf0c3-272c-4268-8302-5886cbc61672",
    * "model_name": "meta/llama3-8b-instruct",
    * "server_kind": "nim",
    * "status": "deploying",
    * "info": null  
  },
  * {
    * "id": "nvidia-nemoguard-jailbreak-detect::78c1a9b3-e231-4fc4-b9c1-e490ef4d02dc",
    * "deployment_id": "78c1a9b3-e231-4fc4-b9c1-e490ef4d02dc",
    * "deployment_name": "ecrujiewu-jailbreak",
    * "model_id": "78c1a9b3-e231-4fc4-b9c1-e490ef4d02dc",
    * "model_name": "nvidia/nemoguard-jailbreak-detect",
    * "server_kind": "nim",
    * "status": "healthy",
    * "info": null  
  },
  * {
    * "id": "nvidia-llama-3.1-nemoguard-8b-content-safety::9cb35ba2-bf35-47b9-8428-e9983b1e545d",
    * "deployment_id": "9cb35ba2-bf35-47b9-8428-e9983b1e545d",
    * "deployment_name": "ecrujiewu-guardrail",
    * "model_id": "9cb35ba2-bf35-47b9-8428-e9983b1e545d",
    * "model_name": "nvidia/llama-3.1-nemoguard-8b-content-safety",
    * "server_kind": "nim",
    * "status": "deploying",
    * "info": null  
  },
  * {
    * "id": "nvidia-llama-3.2-nv-embedqa-1b-v2::b81c7797-b64d-41b1-b185-2b04e7d37407",
    * "deployment_id": "b81c7797-b64d-41b1-b185-2b04e7d37407",
    * "deployment_name": "centraladelegoldberg",
    * "model_id": "b81c7797-b64d-41b1-b185-2b04e7d37407",
    * "model_name": "nvidia/llama-3.2-nv-embedqa-1b-v2",
    * "server_kind": "nim",
    * "status": "healthy",
    * "info": {
      * "assetInfo": [
        * ""  
            ],
      * "licenseInfo": {
        * "content": "The NIM container is governed by the NVIDIA Software License Agreement (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and the Product-Specific Terms for NVIDIA AI Products (found at https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Use of this model is governed by the NVIDIA Community Model License Agreement (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). ADDITIONAL INFORMATION: Llama 3.2 Community License Agreement (https://www.llama.com/llama3_2/license/). Built with Llama.",
        * "name": "LICENSE",
        * "path": "/opt/nim/LICENSE",
        * "sha": "495b462c4ca56d50ec89ba19c2961585b8c53308",
        * "size": 648,
        * "type": "file",
        * "url": ""  
            },
      * "modelInfo": [
        * {
          * "modelUrl": "ngc://nim/nvidia/llama-3.2-nv-embedqa-1b-v2:l4x1-trt-fp8-3fb2ntvrxw",
          * "shortName": "llama-3.2-nv-embedqa-1b-v2:l4x1-trt-fp8-3fb2ntvrxw"  
                    },
        * {
          * "modelUrl": "ngc://nim/nvidia/llama-3.2-nv-embedqa-1b-v2:tokenizer-8192-3fe66485",
          * "shortName": "llama-3.2-nv-embedqa-1b-v2:tokenizer-8192-3fe66485"  
                    }  
            ],
      * "repository_override": "",
      * "version": "1.9.0"  
      }  
  },
  * {
    * "id": "nvidia-llama-3.2-nv-embedqa-1b-v2-passage::b81c7797-b64d-41b1-b185-2b04e7d37407-passage",
    * "deployment_id": "b81c7797-b64d-41b1-b185-2b04e7d37407-passage",
    * "deployment_name": "centraladelegoldberg-passage",
    * "model_id": "b81c7797-b64d-41b1-b185-2b04e7d37407-passage",
    * "model_name": "nvidia/llama-3.2-nv-embedqa-1b-v2-passage",
    * "server_kind": "nim",
    * "status": "healthy",
    * "info": {
      * "assetInfo": [
        * ""  
            ],
      * "licenseInfo": {
        * "content": "The NIM container is governed by the NVIDIA Software License Agreement (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and the Product-Specific Terms for NVIDIA AI Products (found at https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Use of this model is governed by the NVIDIA Community Model License Agreement (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). ADDITIONAL INFORMATION: Llama 3.2 Community License Agreement (https://www.llama.com/llama3_2/license/). Built with Llama.",
        * "name": "LICENSE",
        * "path": "/opt/nim/LICENSE",
        * "sha": "495b462c4ca56d50ec89ba19c2961585b8c53308",
        * "size": 648,
        * "type": "file",
        * "url": ""  
            },
      * "modelInfo": [
        * {
          * "modelUrl": "ngc://nim/nvidia/llama-3.2-nv-embedqa-1b-v2:l4x1-trt-fp8-3fb2ntvrxw",
          * "shortName": "llama-3.2-nv-embedqa-1b-v2:l4x1-trt-fp8-3fb2ntvrxw"  
                    },
        * {
          * "modelUrl": "ngc://nim/nvidia/llama-3.2-nv-embedqa-1b-v2:tokenizer-8192-3fe66485",
          * "shortName": "llama-3.2-nv-embedqa-1b-v2:tokenizer-8192-3fe66485"  
                    }  
            ],
      * "repository_override": "",
      * "version": "1.9.0"  
      }  
  },
  * {
    * "id": "nvidia-llama-3.2-nv-embedqa-1b-v2-query::b81c7797-b64d-41b1-b185-2b04e7d37407-query",
    * "deployment_id": "b81c7797-b64d-41b1-b185-2b04e7d37407-query",
    * "deployment_name": "centraladelegoldberg-query",
    * "model_id": "b81c7797-b64d-41b1-b185-2b04e7d37407-query",
    * "model_name": "nvidia/llama-3.2-nv-embedqa-1b-v2-query",
    * "server_kind": "nim",
    * "status": "healthy",
    * "info": {
      * "assetInfo": [
        * ""  
            ],
      * "licenseInfo": {
        * "content": "The NIM container is governed by the NVIDIA Software License Agreement (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and the Product-Specific Terms for NVIDIA AI Products (found at https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Use of this model is governed by the NVIDIA Community Model License Agreement (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). ADDITIONAL INFORMATION: Llama 3.2 Community License Agreement (https://www.llama.com/llama3_2/license/). Built with Llama.",
        * "name": "LICENSE",
        * "path": "/opt/nim/LICENSE",
        * "sha": "495b462c4ca56d50ec89ba19c2961585b8c53308",
        * "size": 648,
        * "type": "file",
        * "url": ""  
            },
      * "modelInfo": [
        * {
          * "modelUrl": "ngc://nim/nvidia/llama-3.2-nv-embedqa-1b-v2:l4x1-trt-fp8-3fb2ntvrxw",
          * "shortName": "llama-3.2-nv-embedqa-1b-v2:l4x1-trt-fp8-3fb2ntvrxw"  
                    },
        * {
          * "modelUrl": "ngc://nim/nvidia/llama-3.2-nv-embedqa-1b-v2:tokenizer-8192-3fe66485",
          * "shortName": "llama-3.2-nv-embedqa-1b-v2:tokenizer-8192-3fe66485"  
                    }  
            ],
      * "repository_override": "",
      * "version": "1.9.0"  
      }  
  }  
],
* "version": "1.0.0-121"
}`