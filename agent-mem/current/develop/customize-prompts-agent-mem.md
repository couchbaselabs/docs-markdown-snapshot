---
title: Customize Extraction and Summarization Prompts
description: Register named, versioned prompts to steer what Agent Memory
  extracts and summarizes from a memory block.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/develop/pages/customize-prompts-agent-mem.adoc
  xref: xref:agent-mem:develop:customize-prompts-agent-mem.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/develop/customize-prompts-agent-mem.html)

# Customize Extraction and Summarization Prompts

> Register named, versioned prompts to steer what Agent Memory extracts and summarizes from a memory block. 

By default, Agent Memory extracts and summarizes every memory block using the same fixed system prompt, no matter your application. The prompt registry lets you register your own reusable extraction instructions, such as `look for billing disputes` or `look for product issues and resolution steps`, and reference them when you create or update a memory block. Use the SDK's [add\_memory()](develop-agent-mem.md#store-memory) and [update\_memory()](develop-agent-mem.md#update-memory) methods, or call the [Add Memory Blocks](../agent-memory-api-reference/rest-api.md#tag/Memory/operation/add%5Fmemory%5Fusers<em>user%5Fid</em>sessions<em>session%5Fid</em>memory%5Fpost) and [Update Memory Block](../agent-memory-api-reference/rest-api.md#tag/Memory/operation/update%5Fmemory%5Fusers<em>user%5Fid</em>sessions<em>session%5Fid</em>memory<em>block%5Fid</em>put) REST operations directly.

> [!NOTE]
> This page shows SDK examples throughout. For the equivalent REST API requests and responses, see [Agent Memory API Reference](../agent-memory-api-reference/rest-api.md).

## [](#prerequisites)Prerequisites

* You have a running Agent Memory server with version 1.1.0 or later. For setup instructions, see [Get Started with Managed Agent Memory](../get-started/get-started-agent-mem-managed.md) or [Get Started with Self-Managed Agent Memory](../get-started/get-started-agent-mem.md).
* You have the access you need to register, update, archive, or purge prompts:

  * On Managed Agent Memory, use an API key with the Admin access level. An API key with the Read access level can list and get prompts.
  * On Self-Managed Agent Memory with authorization enabled, use a token that carries the `ams_admin` role. A token with the `ams_ro` role can list and get prompts.
* You have installed the [Agent Memory Python SDK](https://pypi.org/project/couchbase-agent-memory/) and initialized an `AgentMemoryClient`. For more information, see [Initialize the Client](develop-agent-mem.md#initialize-the-client).
* You have an existing user and session. To learn how to create both, see [Store and Retrieve Memory](../get-started/get-started-agent-mem.md#store-and-retrieve-memory).

## [](#register-and-use-a-custom-prompt)Register and Use a Custom Prompt

1. Register a prompt with `create_prompt()`:

  * The `prompt_id` field is the only identifier and you cannot rename it later.
  * The `prompt` field holds the actual extraction instructions text.
  * The `description` field is a mandatory field and assists with discovery when listing registered prompts.
  * The `annotations` field is optional and, like `description`, is metadata on the prompt's current state only, not on individual versions.  
```python  
prompt = client.create_prompt(  
    prompt_id="support_tickets",  
    prompt="Extract only numeric data points, including: dates, quantities, percentages, and amounts. Discard all non-numeric information.",  
    description="Use for support ticket extraction, focusing on order numbers, issues, and resolution steps",  
    annotations={"team": "support"},  
)  
print(prompt.current_vid, prompt.version_count)  # 0, 1  
```  
Agent Memory checks the `prompt` field for disallowed content when you register it. See [Prompt Text Validation](#prompt-text-validation) for what it rejects, and [Prompt Field Limits](#limits) for size limits on each field.
2. Use `prompt_id` in `add_memory()` to steer extraction.  
Agent Memory extracts every block created in the following call using the prompt you registered in the previous step:  
```python  
from agentmemory import ChatMessage  
response = session.add_memory(  
    messages=[  
        ChatMessage(  
            user_content="My order #123 hasn't shipped.",  
            assistant_content="I'll look into that.",  
        )  
    ],  
    prompt_id="support_tickets",  
    async_processing=False,  # wait so extraction has already run when the call returns  
)  
```  
Agent Memory validates `prompt_id` before doing any embedding or database work. An unresolvable or archived `prompt_id` rejects the call.  
Leave out `prompt_vid` to always extract with the current version of the prompt. If you want to lock a block to 1 immutable version of the prompt, see [Pin a Prompt to a Specific Version](#pin-a-prompt-to-a-specific-version).  
> [!IMPORTANT]  
> `prompt_id` requires semantic extraction for the call. Passing `prompt_id` together with `context_required=False` or leaving out `context_required` entirely causes a validation error.

## [](#pin-a-prompt-to-a-specific-version)Pin a Prompt to a Specific Version

When you pin a prompt, it always extracts with that specific wording even if you later update the prompt. Version numbering starts at `0`, so version `0` is the text set at registration and version `1` is the text set by the first update.

1. To pin a prompt, call `add_memory()` with the `prompt_vid` version number.  
In this example, `prompt_vid=1` pins the block to the text created by the prompt's first update. See [Update a Prompt](#update-a-prompt) for how updating a prompt creates a new version:  
```python  
session.add_memory(  
    facts=["Customer escalated to a supervisor."],  
    prompt_id="support_tickets",  
    prompt_vid=1,  
)  
```

## [](#update-a-prompt)Update a Prompt

When you need to change a prompt's instructions, you have the option to update it. Updating a prompt creates a new, immutable version. A block pinned to a specific `prompt_vid` is never affected by the update. A late-bound block, a block with no pinned version, picks up the new text the next time it's processed. A block that already reached `ready` status is not processed again, so it keeps the text it already extracted with. Updating either the `description` or `annotations` field never creates a new prompt version, since only the `prompt` text itself is versioned.

1. To update a prompt, call `update_prompt()` with the new `prompt` text:  
```python  
updated = client.update_prompt(  
    "support_tickets",  
    prompt="Focus on billing disputes and refund policy exceptions.",  
)  
print(updated.current_vid, updated.version_count)  # 1, 2  
```

> [!IMPORTANT]
> In this example, any queued block that references `support_tickets` without a pinned `prompt_vid` now extracts with this new text the next time it's processed.

## [](#retire-a-prompt)Retire a Prompt

You can retire a prompt by archiving it or purging it.

Archive

This option uses a soft, 1-way flag and does not delete anything. Agent Memory rejects any new calls that reference the archived `prompt_id`/`prompt_vid`, but any block that's already in flight when you archive a prompt still resolves and extracts normally. Archiving the whole `prompt_id` permanently reserves it, so you can never register a `prompt_id` that you previously archived.

Purge

A hard, irreversible delete. Purging the whole `prompt_id` removes it and every version, and frees `prompt_id` for reuse. Purging a single version removes just that version and does not free `prompt_id`, leaving the other versions unchanged.

> [!IMPORTANT]
> A block that was already in flight when its reference gets purged falls back to the base extraction prompt rather than failing.

1. Retire a prompt with `archive_prompt()` or `purge_prompt()`:  
```python  
# Archive: keeps history, blocks future use, permanently reserves the prompt_id  
client.archive_prompt("support_tickets", vid="all")  
# Or archive just 1 version, blocking only new pins to that exact version  
client.archive_prompt("support_tickets", vid=0)  
# Purge: removes it entirely, frees the prompt_id for reuse  
client.purge_prompt("support_tickets", vid="all")  
# Or purge just 1 version, leaving the rest of the history untouched  
client.purge_prompt("support_tickets", vid=0)  
```  
`vid` accepts `"all"` for the whole prompt, or a non-negative integer for a specific version.

> [!NOTE]
> Retiring current versions
> 
> Both options to retire a prompt take a required scope argument: `vid="all"` for the whole prompt, or a specific version number. When using either method to retire a specific prompt version, you cannot retire the current version. Attempting to do so causes a `ConflictError`. To retire the current version, first update the prompt so that it uses a new version and then target the old version number.

## [](#switch-or-clear-a-blocks-prompt)Switch or Clear a Block's Prompt

`update_memory()` accepts the same `prompt_id`/`prompt_vid` fields as `add_memory()`, to change which prompt an already-created memory block uses. What `prompt_id` does depends on what you pass:

| Pass this                                             | Result                                                                                                                                                                                        |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| prompt\_id="default"                                  | Clears the block's prompt reference, so it falls back to the base extraction prompt. Agent Memory does not check the registry.                                                                |
| A registered prompt\_id (optionally with prompt\_vid) | Switches the block to that prompt. Agent Memory validates it the same way as on add\_memory(). If it does not resolve, Agent Memory rejects the whole call and it leaves the block unchanged. |

1. Switch or clear a block's prompt with `update_memory()`:  
```python  
# Switch this block to a different registered prompt  
session.update_memory(block_id="block_abc", prompt_id="support_tickets")  
# Switch and pin to a specific version at the same time  
session.update_memory(block_id="block_abc", prompt_id="support_tickets", prompt_vid=1)  
# Clear this block back to the default extraction prompt  
session.update_memory(block_id="block_abc", prompt_id="default")  
```

Changing a block's `prompt_id` or `prompt_vid` triggers the same reprocessing as editing the block's content, even if the block never had a prompt reference before. Reprocessing re-runs extraction under the new prompt and produces a new summary. It does not change the block's embedding. The embedding is derived from the block's original message or fact content, not from the prompt or the extracted summary, so it only changes if you also update that content.

## [](#get-and-list-prompts)Get and List Prompts

Inspect the registry with `get_prompt()`, `list_prompts()`, and `list_prompt_versions()`:

```python
# Current state of a prompt
current = client.get_prompt("support_tickets")

# One specific historical version
v0 = client.get_prompt("support_tickets", vid=0)

# List registered prompts, paginated
prompts = client.list_prompts(limit=50, offset=0)
print(f"{prompts.count} of {prompts.total} prompts")

# List one prompt's version history, paginated
versions = client.list_prompt_versions("support_tickets", limit=50, offset=0)
for v in versions.versions:
    print(v.vid, v.is_current, v.archived)
```

> [!TIP]
> `count` on a paginated response is the number of items in that page, not the total collection size. Use `total` for the collection size.

## [](#limits)Prompt Field Limits

`create_prompt()` and `update_prompt()` enforce the following size and format limits on each field:

| Field       | Limit                               | Notes                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| prompt\_id  | 128 characters, ^\[a-zA-Z0-9\_-\]+$ | Must be globally unique. Registering a duplicate, an archived prompt\_id, or a prompt\_id that's currently mid-purge raises ConflictError. See PROMPT\_ALREADY\_PURGING in [Handle Errors](#handle-errors) for the mid-purge case. The value default is reserved and cannot be registered. It's the sentinel update\_memory() uses to clear a block's prompt. |
| prompt      | 4000 characters (\~1000 tokens)     | The extraction instructions. See [Prompt Text Validation](#prompt-text-validation) for what this text cannot contain.                                                                                                                                                                                                                                         |
| description | 200 characters                      | Mandatory. A short, human-written summary of what the prompt is for. To help with discovery, it's shown in list\_prompts(). No fixed template exists.                                                                                                                                                                                                         |

## [](#prompt-text-validation)Prompt Text Validation

Agent Memory injects registered prompt text directly into the extraction system prompt, so it treats that text as untrusted input. `create_prompt()` and `update_prompt()` reject known-bad patterns at registration, before the prompt is saved.

Agent Memory also checks the same rules again every time it resolves a prompt for use. This closes the gap where a value that reached the registry some other way, such as a direct database write, could otherwise reach the model unchecked.

Registration rejects prompt text containing:

* Control characters and invisible or zero-width Unicode characters.
* Text that attempts to forge section headers from the extraction system prompt.
* Long runs of delimiter-style characters, such as a row of dashes or equals signs.
* Chat-template control tokens or role markers.

## [](#handle-errors)Handle Errors

As well as the error categories in [Handle Errors](develop-agent-mem.md#handle-errors), the prompt registry can return the following error codes:

| Error code                         | HTTP status | Meaning                                                                                                                                  |
| ---------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| PROMPT\_NOT\_FOUND                 | 404         | prompt\_id does not resolve. It was never registered, or was purged.                                                                     |
| PROMPT\_ALREADY\_EXISTS            | 409         | prompt\_id is already registered.                                                                                                        |
| PROMPT\_ERROR                      | 500         | Generic prompt operation failure.                                                                                                        |
| PROMPT\_VERSION\_NOT\_FOUND        | 404         | prompt\_vid does not resolve for the given prompt\_id.                                                                                   |
| PROMPT\_EXTRACTION\_DISABLED       | 400         | prompt\_id/prompt\_vid was provided but semantic extraction is disabled for this call.                                                   |
| PROMPT\_ID\_ARCHIVED               | 409         | The whole prompt\_id has been archived and can no longer be referenced or re-created.                                                    |
| PROMPT\_ALREADY\_ARCHIVED          | 409         | The whole prompt\_id is already archived.                                                                                                |
| PROMPT\_VERSION\_ARCHIVED          | 409         | The specific prompt\_vid has been archived and can no longer be pinned to.                                                               |
| PROMPT\_VERSION\_ALREADY\_ARCHIVED | 409         | The specific prompt\_vid is already archived.                                                                                            |
| PROMPT\_CURRENT\_VERSION\_PURGE    | 409         | The version you tried to purge is the prompt's current version. Update the prompt to a new version first, or purge the whole prompt.     |
| PROMPT\_CURRENT\_VERSION\_ARCHIVE  | 409         | The version you tried to archive is the prompt's current version. Update the prompt to a new version first, or archive the whole prompt. |
| PROMPT\_ALREADY\_PURGING           | 409         | A whole-prompt purge is already in progress for this prompt\_id. Wait for it to finish before retrying the operation.                    |

## [](#next-steps)Next Steps

* [Develop with the Agent Memory SDK](develop-agent-mem.md)
* [Agent Memory API Reference](../agent-memory-api-reference/rest-api.md)