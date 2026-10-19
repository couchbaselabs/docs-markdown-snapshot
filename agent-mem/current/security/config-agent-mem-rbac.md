---
title: Configure RBAC for Self-Managed Agent Memory
description: Restrict operations on a self-managed Agent Memory server to 3
  fixed roles carried in your identity provider's tokens.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/security/pages/config-agent-mem-rbac.adoc
  xref: xref:agent-mem:security:config-agent-mem-rbac.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/security/config-agent-mem-rbac.html)

# Configure RBAC for Self-Managed Agent Memory

> Restrict operations on a self-managed Agent Memory server to 3 fixed roles carried in your identity provider's tokens. 

By default, Agent Memory authenticates callers but does not authorize them. This means that any valid token can reach every operation, including deleting a user or downloading diagnostic logs. Enabling authorization restricts each operation to a minimum role, so a token must carry a sufficient role to reach it. To learn about the Agent Memory's Role-Based Access Control model, see [Security and Access Control](../about-agent-mem.md#authorization).

## [](#prerequisites)Prerequisites

* You have configured authentication for Agent Memory. For more information, see [Configure Authentication for Self-Managed Agent Memory](config-agent-mem-auth.md).
* You have administrative access to your identity provider to create roles and assign them to service accounts.

## [](#procedure)Procedure

To configure Role-Based Access Control (RBAC) for Agent Memory, use the following steps:

1. Create 3 roles in your identity provider: `ams_ro`, `ams_rw`, and `ams_admin`.  
> [!IMPORTANT]  
> The steps to create and assign a role vary by provider. For more information, see your identity provider's documentation.
2. Assign the appropriate role to each service account or client that calls Agent Memory.  
Assigning a role does not require issuing a new credential. Access tokens are short-lived, so the client picks up its new role the next time it fetches a token.  
For more information about which role each operation requires, see [Minimum Role by Operation](#route-reference).
3. Verify the role reaches a newly issued token before enabling enforcement:

  1. Run the following:  
  ```console  
  echo $TOKEN | cut -d'.' -f2 | base64 --decode 2>/dev/null | jq  
  ```  
  > [!TIP]  
  > The `base64` decode flag varies by platform: `-d` on Linux, `-D` on earlier versions of macOS. You can also use a CLI tool such as [jwt-cli](https://github.com/mike-engel/jwt-cli) to decode the token locally, or paste it into [jwt.io](https://jwt.io/) to inspect its claims. Avoid pasting a live production token into any third-party website; use a non-production token instead.
  2. In the output, find the field at your configured `OIDC_ROLES_CLAIM` path and confirm it includes 1 of `ams_ro`, `ams_rw`, or `ams_admin`.  
  The claim path defaults to `realm_access.roles`, which is the convention for Keycloak. If your identity provider places roles elsewhere, set `OIDC_ROLES_CLAIM` to match. For more information, see [Self-Managed Agent Memory Environment Variable Reference](../reference/config-agent-mem-env.md).
4. Add the following environment variable to the `.env` file in your Agent Memory project directory:  
```bash  
AGENTMEMORY_AUTHZ_ENABLED=true  
```
5. Use `docker compose` to recreate the Agent Memory container to apply the new environment variable:  
> [!CAUTION]  
> This command briefly interrupts the Agent Memory service. In-flight requests fail until the new container is ready.  
```console  
docker compose up -d --force-recreate agentmemory-server  
```

## [](#route-reference)Minimum Role by Operation

Each of the following operations lists its minimum role. A token with `ams_rw` also reaches everything `ams_ro` reaches, and a token with `ams_admin` reaches everything.

| Area                   | Operation                                                                                                                                                                      | Minimum Role     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| Users                  | GET /users/{user\_id}                                                                                                                                                          | ams\_ro          |
| Users                  | GET /users/{user\_id}/sessions                                                                                                                                                 | ams\_ro          |
| Users                  | GET /users (list, with optional name and metadata filters)                                                                                                                     | ams\_admin       |
| Users                  | POST /users PUT /users/{user\_id} PUT /users/{user\_id}/ttl DELETE /users/{user\_id}                                                                                           | ams\_rw          |
| Sessions               | GET /users/{user\_id}/sessions/{session\_id}                                                                                                                                   | ams\_ro          |
| Sessions               | POST /users/{user\_id}/sessions PUT /users/{user\_id}/sessions/{session\_id} POST /users/{user\_id}/sessions/{session\_id}/end DELETE /users/{user\_id}/sessions/{session\_id} | ams\_rw          |
| Memory                 | POST …​/memory/search GET /users/{user\_id}/memory                                                                                                                             | ams\_ro          |
| Memory                 | POST …​/memory PUT …​/memory/{block\_id} DELETE …​/memory                                                                                                                      | ams\_rw          |
| Prompts                | GET /prompts GET /prompts/{prompt\_id} GET /prompts/{prompt\_id}/versions                                                                                                      | ams\_ro          |
| Prompts                | POST /prompts PUT /prompts/{prompt\_id} PUT /prompts/{prompt\_id}/archive DELETE /prompts/{prompt\_id}                                                                         | ams\_admin       |
| Logs                   | GET /logs/collect                                                                                                                                                              | ams\_admin       |
| Health and diagnostics | GET /health/couchbase GET /health/models GET /health/async-batch-processor GET /health/async-batch-processor-stats GET /health/memory                                          | ams\_ro          |
| Health and diagnostics | GET /health GET /metrics                                                                                                                                                       | Public: no token |

### [](#operation-notes)Operation Notes

`GET /users` vs. `GET /users/{user_id}`

`GET /users` is admin-gated because its filters can return every user sharing a name or metadata value. `GET /users/{user_id}` requires only `ams_ro` because it discovers nothing. The caller must already hold the ID, and a wrong guess returns `404`.

`DELETE /users/{user_id}`

Deletion is gated at `ams_rw`, not `ams_admin`, because in most deployments the agent runtime that creates users also needs to delete them. The operation is irreversible and there is no soft delete. If your security model requires tighter control over user deletion, gate it at the identity-provider level by limiting agent runtime tokens to `ams_rw` and reserving `ams_admin` for a separate service account used only for delete workflows.

`/prompts` mutations

All mutations require `ams_admin` because prompts are a global configuration that steers extraction for every ingestion.

`GET /logs/collect`

Requires `ams_admin` because the diagnostic bundle carries server logs, configuration snapshots, and cluster information.

## [](#troubleshooting)Troubleshooting

| Symptom                                                                                                                                       | Cause                                                                                                                                                                                                     | Solution                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Startup logs the following warning: Authorization is DISABLED (AGENTMEMORY\_AUTHZ\_ENABLED=false) — every authenticated token has full access | [Authentication](config-agent-mem-auth.md) is on, but AGENTMEMORY\_AUTHZ\_ENABLED is not set to true.                                                                                                     | Expected until you finish this procedure. Set AGENTMEMORY\_AUTHZ\_ENABLED=true once you have assigned roles.                  |
| "Insufficient permissions" (403) on some operations, not all                                                                                  | The token carries a recognized role, but it's not a high enough for this specific operation.                                                                                                              | Assign ams\_ro, ams\_rw, or ams\_admin in your identity provider. The response message names the role the operation requires. |
| 403 on every operation                                                                                                                        | Authorization is on, but the token does not carry a role that Agent Memory recognizes.                                                                                                                    | Confirm OIDC\_ROLES\_CLAIM points at the claim that actually carries the roles in your tokens.                                |
| 403 on every operation, including with no token                                                                                               | AGENTMEMORY\_AUTHZ\_ENABLED=true, but authentication is disabled. The fallback identity used when authentication is off carries no roles, so it does not satisfy the minimum role on any gated operation. | Enable authentication, or set AGENTMEMORY\_AUTHZ\_ENABLED=false.                                                              |

## [](#next-steps)Next Steps

* [Agent Memory for Persistent Memory Storage](../about-agent-mem.md)
* [Configure Authentication for Self-Managed Agent Memory](config-agent-mem-auth.md)
* [Self-Managed Agent Memory Environment Variable Reference](../reference/config-agent-mem-env.md)
* [Develop with the Agent Memory SDK](../develop/develop-agent-mem.md)