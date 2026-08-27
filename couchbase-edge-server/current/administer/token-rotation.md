---
title: Rotate Replication Credentials Without Restart
description: Configure Couchbase Edge Server to load JWT replication credentials
  from a file path, enabling credential rotation without restarting the server.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/administer/pages/token-rotation.adoc
  xref: xref:couchbase-edge-server:administer:token-rotation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/administer/token-rotation.html)

# Rotate Replication Credentials Without Restart

Configure Couchbase Edge Server to read JWT replication credentials from a file path instead of embedding them inline. This allows you to rotate credentials without restarting Couchbase Edge Server.

## [](#prerequisites)Prerequisites

* Couchbase Edge Server {version} or later.
* JWT-based authentication configured between Couchbase Edge Server and the upstream Sync Gateway or Capella App Services instance.
* The JWT token file accessible at a path on the host running Couchbase Edge Server, for example via a Kubernetes secret mounted as a volume.

## [](#configure-a-file-path-for-the-jwt-token)Configure a File Path for the JWT Token

In the replication configuration, set `auth.openid_token` to an object with a `path` property containing the file path of the JWT token. This is the file-based form of `openid_token`. The existing behavior of passing the token as an inline string remains unchanged.

```json
{
  "replications": [
    {
      "source": "travel-sample",
      "target": "wss://remote-sync-gateway/travel-sample",
      "continuous": true,
      "auth": {
        "openid_token": {
          "path": "/path/to/jwt-token"
        }
      }
    }
  ]
}
```

Couchbase Edge Server loads the token from the specified path each time a replication starts. When the token file is updated, the new token is used the next time the replication restarts.

## [](#enable-automatic-reconnection-on-token-change)Enable Automatic Reconnection on Token Change

By default, Couchbase Edge Server does not disconnect an active replication when the token file changes. This avoids disrupting an in-progress sync when a token is rotated.

To configure Couchbase Edge Server to detect token file changes and automatically reconnect active replications with the updated token, enable proactive token detection in the replication configuration.

```json
{
  "replications": [
    {
      "source": "travel-sample",
      "target": "wss://remote-sync-gateway/travel-sample",
      "continuous": true,
      "auth": {
        "openid_token": {
          "path": "/path/to/jwt-token"
        },
        "reconnect_on_token_change": true
      }
    }
  ]
}
```

When `reconnect_on_token_change` is `true`, Couchbase Edge Server monitors the token file for changes. When a change is detected, Couchbase Edge Server disconnects the active replication and reconnects using the updated token.

> [!NOTE]
> Replications configured via the REST API are not monitored for token file changes. When using REST API-managed replications, an external agent is responsible for stopping and restarting the replication with updated credentials.

## [](#next-steps)Next Steps

* To configure replication settings, see [Remote Sync with App Services / Sync Gateway](../sync/remote-sync.md).
* To manage replications via the REST API, see [Manage Replication with Edge Server](../rest-based-access/replication.md).