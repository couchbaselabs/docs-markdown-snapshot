---
title: Install the Agent Memory Plug-in for Hermes
description: Install the Agent Memory plug-in for Hermes Agent, configure its
  connection to your Agent Memory server, and use its memory tools.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/develop/pages/install-hermes-agent-mem.adoc
  xref: xref:agent-mem:develop:install-hermes-agent-mem.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/develop/install-hermes-agent-mem.html)

# Install the Agent Memory Plug-in for Hermes

> Install the Agent Memory plug-in for Hermes Agent, configure its connection to your Agent Memory server, and use its memory tools. 

This guide installs the Agent Memory plug-in for [Hermes Agent](https://github.com/NousResearch/hermes-agent), activates it, and configures its connection to your Agent Memory server. For background on how the plug-in behaves, see [Agent Memory Plug-in for Hermes Agent](hermes-agent-mem.md).

> [!TIP]
> If you're switching from another Hermes memory provider, see [Switch from Another Hermes Memory Provider](#switching-providers).

## [](#prerequisites)Prerequisites

* A running Agent Memory server, version 1.1.0 or later, and its base URL. For more information, see [Get Started with Managed Agent Memory](../get-started/get-started-agent-mem-managed.md) or [Get Started with Self-Managed Agent Memory](../get-started/get-started-agent-mem.md).
* A working Hermes installation with a model already configured. For more information, see [LLM and Model Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers) in the Hermes documentation.
* [Python 3.12](https://www.python.org/downloads/) or later, for the plug-in's installer.

## [](#install)Install and Activate

1. Install the plug-in:  
```console  
pip install "couchbase-agent-memory[hermes]"  
```
2. Install the plug-in into Hermes:  
```console  
agentmemory-hermes install  
```  
This command copies the plug-in into `$HERMES_HOME/plugins/couchbase-agentmemory/` and makes sure you can import `couchbase-agent-memory` from Hermes' own Python environment. This matters because `pipx` and `uv` installs run Hermes in an interpreter separate from wherever you ran `pip install`. The installer detects this and installs it into Hermes' environment automatically.
3. Activate the plug-in as memory provider for Hermes:  
```console  
hermes config set memory.provider couchbase-agentmemory  
```
4. Turn off Hermes' built-in memory, so Agent Memory is the only long-term memory. Without this, the model can keep saving facts to the built-in memory it already knows, alongside Agent Memory.  
```console  
hermes config set memory.memory_enabled false  
hermes config set memory.user_profile_enabled false  
```  
> [!IMPORTANT]  
> Turn off both flags together. On Hermes 0.19.x, turning off only 1 leaves stale built-in-memory guidance in the system prompt, pointing at a tool that's now half-disabled.  
> [!CAUTION]  
> Do not use `hermes tools disable memory` for this as it turns off the plug-in's own tools, not just Hermes' built-in memory.
5. Configure the connection to your Agent Memory server:  
```console  
hermes memory setup  
```
6. From the provider menu, select `couchbase-agentmemory`.
7. Add your Agent Memory server's base URL and, if your server requires authentication, a token. For more information, see [Authentication](#authentication).
8. Verify the plug-in is active:  
```console  
hermes memory status  
```  
A working installation reports:  
```none  
Provider:  couchbase-agentmemory  
couchbase-agentmemory config:  
  token: not configured  
Plugin:    installed ✓  
Status:    available ✓  
```  
> [!NOTE]  
> On Hermes 0.19.x, this header also prints `Built-in: always active`, even if you turned off Hermes' built-in memory in the previous step. That line is cosmetic. The flags still take effect, and no `MEMORY.md` or `USER.md` file is written.

## [](#configuration)Configuration

Configuration comes from environment variables. A `$HERMES_HOME/agentmemory.json` file overrides them. The `hermes memory setup` wizard writes that file for you.

| Environment variable             | JSON key            | Required | Default     | Description                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------- | ------------------- | -------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AGENTMEMORY\_BASE\_URL           | base\_url           | Yes      | None        | Your Agent Memory server's base URL, for example: http://localhost:8080. On Managed Agent Memory, use your Agent Memory server endpoint.                                                                                                                                                                                                                                                                         |
| AGENTMEMORY\_JWT\_TOKEN          | token               | No       | None        | Bearer token. On Managed Agent Memory, use your Agent Memory API key token. On a self-managed server, use a JWT from your identity provider, or leave unset when your server runs with authentication off. If your server has authorization enabled, the token's role must be ams\_rw or higher. For more information, see [Configure RBAC for Self-Managed Agent Memory](../security/config-agent-mem-rbac.md). |
| AGENTMEMORY\_USER\_ID            | user\_id            | No       | hermes-user | Memory scope. When running Hermes as a gateway, leaving this unset scopes memory per sender automatically. Setting a value merges every sender into 1 pool instead. For more than 1 person on the same machine, see [Running Multiple Users](#running-multiple-users). Changing this value alone does not isolate people.                                                                                        |
| AGENTMEMORY\_VERIFY\_SSL         | verify\_ssl         | No       | true        | Verify TLS certificates against the server.                                                                                                                                                                                                                                                                                                                                                                      |
| AGENTMEMORY\_VERBOSE             | verbose             | No       | false       | When enabled, the plug-in's logs print to the Hermes terminal, prefixed \[agentmemory\].                                                                                                                                                                                                                                                                                                                         |
| AGENTMEMORY\_RECALL\_ANNOTATIONS | recall\_annotations | No       | None        | Annotation filter applied to every recall. See [Narrow Recall for Every Search](#annotations-and-recall-scoping).                                                                                                                                                                                                                                                                                                |

### [](#authentication)Configure Authentication

The plug-in sends its token as a bearer token. The `hermes memory setup` wizard labels its secret-token field as `API key / local`. This wizard writes the token to `~/.hermes/.env` as `AGENTMEMORY_JWT_TOKEN=<your token>`.

Configure the token for your deployment.

* Managed
* Self-Managed

1. Add the IP address of the machine where Hermes runs to your server's allowed IP addresses.
2. Set the token to an Agent Memory API key token with the Write or Admin access level.
3. Set the base URL to your Agent Memory server endpoint.

For more information, see [Allow Access and Connect](../managed/deploy-agent-mem-managed.md#connect).

* If your server runs with authentication off, such as on a local machine or a trusted network, leave the token blank. If the server uses a self-signed or internal CA certificate, set `AGENTMEMORY_VERIFY_SSL` to `false`.
* If your server has OIDC authentication on, obtain a JWT from your identity provider and set it as the token. For more information about setting up OIDC authentication, see [Configure Authentication for Self-Managed Agent Memory](../security/config-agent-mem-auth.md).

> [!TIP]
> To see if the current token has expired, run `hermes memory status`.

The plug-in re-reads the token from disk on every request, so rotating it takes effect on the next call with no Hermes restart required.

### [](#annotations-and-recall-scoping)Narrow Recall for Every Search

The plug-in automatically tags every memory it writes with context from Hermes. For the list of annotation keys and what they mean, see [Annotations](hermes-agent-mem.md#annotations). By default, recall spans all of a user's memories regardless of annotations.

1. To narrow the recall, set `recall_annotations` to an annotation filter that applies to every automatic recall and every search tool call:

```json
// $HERMES_HOME/agentmemory.json
{
  "base_url": "http://localhost:8080",
  "recall_annotations": { "source": "agent" }
}
```

You can also set this with the `AGENTMEMORY_RECALL_ANNOTATIONS` environment variable, as a JSON object string.

> [!IMPORTANT]
> `recall_annotations` combines multiple keys with AND, not OR. A memory must match every key and value pair for recall. It's also an exact-match filter applied to every recall, including automatic prompt injection. Any memory stored before you set the filter, or missing the tagged field, is excluded from then on.

`recall_annotations` is not a tenant-isolation boundary. Use separate `user_id` values and Hermes profiles for multiple users, as described in [Running Multiple Users](#running-multiple-users).

A malformed filter recalls everything rather than blocking recall entirely.

### [](#per-call-facets)Narrow Recall for a Single Search

The model can narrow a single [agentmemory\_search](hermes-agent-mem.md#tools) call with the `source`, `platform`, and `channel_type` arguments. For example, it can restrict a search to messages sent on Slack. If an operator has already fixed one of these keys with `recall_annotations`, the plug-in removes that argument from the model's tool schema for this deployment, since setting it would only be silently overridden.

For the full list of tools, see [Tools Exposed to the Model](hermes-agent-mem.md#tools).

## [](#running-multiple-users)Run Multiple Users with Hermes Profiles

Changing `AGENTMEMORY_USER_ID` alone does not isolate 2 people using the same machine. The supported pattern is 1 Hermes profile per person. A profile is a fully separate home directory with its own built-in memory, sessions, and configuration. A new profile inherits nothing, so repeat the model configuration and the plug-in installation for it.

1. Create the profile:  
```console  
hermes profile create user-b  
```
2. Give the profile a model:  
```console  
hermes -p user-b setup  
```
3. Install the plug-in into this profile's home directory:  
```console  
HERMES_HOME=~/.hermes/profiles/user-b agentmemory-hermes install  
```
4. Activate and configure this profile's Agent Memory connection, using its distinct `user_id`:  
```console  
hermes -p user-b config set memory.provider couchbase-agentmemory  
hermes -p user-b memory setup  
```  
> [!IMPORTANT]  
> If you turned off Hermes' built-in memory for the default profile in [Install and Activate](#install), you need to do this for each new profile.  
```console  
hermes -p user-b config set memory.memory_enabled false  
hermes -p user-b config set memory.user_profile_enabled false  
```
5. Verify, then chat as this profile:  
```console  
hermes -p user-b memory status  
hermes -p user-b  
```

Gateway identities, such as separate Telegram or Slack senders, are isolated within a profile automatically when `AGENTMEMORY_USER_ID` is left unset. Hermes passes each sender's id to the plug-in as its `user_id`, so each sender gets a separate memory pool. Hermes' built-in memory remains shared across every sender within 1 profile.

## [](#switching-providers)Switch from Another Hermes Memory Provider

Hermes supports only 1 external memory provider in the `memory.provider` setting.

1. Before switching from another provider, turn off or uninstall your previous provider following its own instructions. Leftover configuration for a provider that's no longer active can otherwise appear in `hermes memory status`.
2. Use the same procedure as a new install in [Install and Activate](#install).

> [!IMPORTANT]
> Memory content does not carry over between providers. Your previous provider's stored memories remain on its own backend.

## [](#troubleshooting)Troubleshooting

If `hermes memory status` reports `not available`

Run `agentmemory-hermes status`. If it reports `couchbase-agent-memory` missing from Hermes' environment, run the printed command to install it there. Also confirm `AGENTMEMORY_BASE_URL` is set, as an environment variable or in `agentmemory.json`. `hermes memory status` lists it under `Missing:` if it's not set.

If the plug-in reports `not installed` under a profile or custom `HERMES_HOME`

The installer copies the plug-in into whatever `HERMES_HOME` is set in the shell you run it from. Re-run it scoped to the correct home, for example:

```console
HERMES_HOME=~/.hermes/profiles/<name> agentmemory-hermes install
```

If `hermes -p <profile>` does not chat, or reports model errors

A fresh profile has no model configuration. Configure a model with `hermes -p <profile> setup`, as described in [Running Multiple Users](#running-multiple-users).

If the installer cannot locate the Hermes interpreter on Windows

The installer's automatic detection needs a parseable launcher script, which Windows Hermes installs do not always have. Install `couchbase-agent-memory` manually instead, replacing `<hermes python>` with the path to the Python interpreter Hermes itself runs on:

```console
<hermes python> -m pip install couchbase-agent-memory
```

If `hermes memory status` shows a token you never configured

Another source is exporting `AGENTMEMORY_JWT_TOKEN`. `hermes memory status` names which source is in effect, for example the environment, `.env`, or `agentmemory.json`. Remove the entry there. On a server with authentication off, the server ignores any token you send, so this is cosmetic until you enable authentication.

If a tool call fails with `AgentMemory is not configured`

The server was unreachable at startup, or the token had already expired, and the error message names the cause. Check that the base URL is correct and the server is reachable, and run `hermes memory status` to check the token. No Hermes restart is needed. If you fix the base URL or token, the next turn applies it automatically. If the server itself was down, recovery can take up to a couple of minutes, and the error stays `AgentMemory is not configured` the whole time rather than changing to `AgentMemory is temporarily unavailable`.

If a tool call fails with `AgentMemory is temporarily unavailable`

This happens after repeated server failures. Calls pause automatically and resume within a couple of minutes once the server is healthy again.

If writes fail with `Insufficient permissions. Required role: ams_rw or higher`, but recall still works

Your Agent Memory server, not the plug-in, enforces this. Its authorization feature rejected the token because its role does not grant write access. On Managed Agent Memory, generate an API key with the Write or Admin access level. On self-managed Agent Memory, get a token with the `ams_rw` role or higher from your identity provider. For the minimum role each operation requires, see [Minimum Role by Operation](../security/config-agent-mem-rbac.md#route-reference).

If you stored a fact but a search does not find it

Extraction is asynchronous. Wait for the memory to reach `ready` status, typically a matter of seconds. To see each memory's current status, use `agentmemory_list`. For more information, see [Tools Exposed to the Model](hermes-agent-mem.md#tools).

If a 1-shot `hermes -z "…​"` turn is missing from memory

1-shot capture is best-effort, because Hermes exits as soon as it replies. The turn is handed to a background worker, which may not finish before the process exits. This is more likely if the turn included tool calls. Use interactive chat instead when every turn must be captured.

If a Hermes upgrade breaks plug-in discovery or hooks

Hermes' plug-in interface can change between releases. Re-run `agentmemory-hermes install` after updating Hermes.

## [](#uninstall)Uninstall

1. To uninstall the Agent Memory plug-in for Hermes, run the following:  
```console  
agentmemory-hermes uninstall  
hermes memory off  
```  
Use `hermes memory off`, not `hermes config set memory.provider builtin`. Hermes has no provider by that name and reports the plug-in as not installed if you set it.
2. If you turned off Hermes' built-in memory, as described in [Install and Activate](#install), turn it back on:  
```console  
hermes config set memory.memory_enabled true  
hermes config set memory.user_profile_enabled true  
```

## [](#next-steps)Next Steps

* [Agent Memory Plug-in for Hermes Agent](hermes-agent-mem.md)
* [Configure Authentication for Self-Managed Agent Memory](../security/config-agent-mem-auth.md)
* [Develop with the Agent Memory SDK](develop-agent-mem.md)