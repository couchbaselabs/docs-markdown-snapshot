---
title: Offline Upgrade of a Docker Cluster from Enterprise Analytics to
  Operational Insights
description: Learn more about the per-container procedure for an offline upgrade
  of a Docker cluster across the Enterprise Analytics to Operational Insights
  rename.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: procedure
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade-docker-cluster-offline.adoc
  xref: xref:enterprise-analytics:install:upgrade-docker-cluster-offline.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade-docker-cluster-offline.html)

# Offline Upgrade of a Docker Cluster from Enterprise Analytics to Operational Insights

> Learn more about the per-container procedure for an offline upgrade of a Docker cluster across the Enterprise Analytics to Operational Insights rename. 

Operational Insights replaces Enterprise Analytics as the product name, starting with this release. The rename changes the Docker image, from `couchbase/enterprise-analytics` to `couchbase/operational-insights`, and it also changes the install prefix inside the image, from `/opt/enterprise-analytics` to `/opt/couchbase`.

A container is never upgraded in place. Instead, you stop each Enterprise Analytics container and create an Operational Insights container that uses the same volume. Nothing in the volume is moved, copied, or edited.

The node records absolute paths under `/opt/enterprise-analytics/var` in its own configuration, and nothing can rewrite them. The Operational Insights container must therefore see the node's volume at two paths:

* At `/opt/couchbase/var`, which is where Operational Insights looks for the node's state.
* At `/opt/enterprise-analytics/var`, which is where the node's recorded paths still point.

> [!IMPORTANT]
> If you mount the volume only at `/opt/couchbase/var`, the node does not come back as itself. Depending on how far it gets, the node either fails to start, with an empty log directory, or starts with services that fail in the background while its REST interface looks healthy. If you mount nothing at `/opt/couchbase/var`, the container starts with a new, empty volume, and the node initializes itself as a new, empty node.

If you can upgrade with the cluster online, see [Upgrade an Online Docker Cluster, Full Capacity](upgrade-docker-cluster-online-full-capacity.md). That procedure does not require any special handling for the rename. Use this page only if you're upgrading with [the cluster offline](upgrade-cluster-offline.md). For nodes installed from `.rpm` or `.deb` packages, see [Offline Upgrade from Enterprise Analytics to Operational Insights](upgrade-ea-to-oi.md) instead.

## [](#prerequisites)Prerequisites

* This is a per-container procedure, and the cluster is down for its entire duration.
* Complete the cluster-level steps in [Prepare the Cluster](upgrade-cluster-offline.md#prepare-the-cluster) before you start on the first container. In a Docker cluster, run the auto-failover command in any running container:  
```console  
docker exec ea1 /opt/enterprise-analytics/bin/couchbase-cli setting-autofailover \
  -c localhost:8091 -u ${USERNAME} -p ${PASSWORD} \
  --enable-auto-failover 0  
```  
Do not skip this step. While one container is being replaced, the containers you have already upgraded are running, and they fail over a node that stays down for longer than the auto-failover timeout.
* Rolling back from Operational Insights to Enterprise Analytics is not supported.
* Do not remove an Enterprise Analytics container with `docker rm -v`, and do not run `docker volume prune` or `docker system prune --volumes` until the upgrade is complete. Each of these deletes the volume that holds the node's state, if no container still uses it.
* In the examples, the Enterprise Analytics containers are named `ea1`, `ea2`, and `ea3`. Replace `${USERNAME}` and `${PASSWORD}` with the cluster's administrator credentials.

## [](#record-the-node)Record Each Node Before You Start

Do this for every container while the cluster is still running, before you stop anything. Keep the output: you need it to create the replacement container and to verify it.

1. Note the node's UUID, its configured data path, and the name by which the cluster knows it:  
```console  
docker exec ea1 curl -s -u ${USERNAME}:${PASSWORD} http://localhost:8091/nodes/self \
  | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["nodeUUID"], d["storage"]["hdd"][0]["path"], d["hostname"])'  
```  
The output looks like this:  
fb3acd4cb9efb45df88613fb347dd98b /opt/enterprise-analytics/var/lib/couchbase/data ea1.example.com:8091  
The last value tells you how the node is addressed. If it's a hostname, such as `ea1.example.com:8091`, the node keeps its identity as long as the replacement container answers to the same hostname. If it's an IP address, such as `172.17.0.6:8091`, the replacement container must have the same IP address. See [How the Node Keeps Its Address](#addressing).
2. List the container's mounts:  
```console  
docker inspect -f '{{range .Mounts}}{{.Type}} {{if .Name}}{{.Name}}{{else}}{{.Source}}{{end}} {{.Destination}}{{println}}{{end}}' ea1  
```  
Each line shows the mount type, the volume name or host directory, and the path inside the container. A line for `/opt/enterprise-analytics/var` always exists, because the image declares it as a volume. How it appears depends on how you created the container:

| What you see                                | What it means                                                                                                                                                                                                                                     |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| volume with a 64-character hexadecimal name | An anonymous volume. You created the container without a \-v option for /opt/enterprise-analytics/var, as in the examples in [Install with Docker](getting-started-docker.md). The node's state is in this volume, and you reuse it by that name. |
| volume with a name you chose                | A named volume, from an option such as \-v ea1-var:/opt/enterprise-analytics/var.                                                                                                                                                                 |
| bind with a host directory                  | A bind mount, from an option such as \-v /srv/ea1:/opt/enterprise-analytics/var.                                                                                                                                                                  |  
The output looks like this, for a container created with a separate volume for its data directory:  
volume ea1-data /opt/enterprise-analytics/var/lib/couchbase/data  
volume 7371c0ffb3e80fba77a9efa9caf2312a55d15c2b20fdfc5dfb5041e31aa4534b /opt/enterprise-analytics/var  
Check that the data path you noted in the previous step is the destination of a mount, or sits under one. The default data path, `/opt/enterprise-analytics/var/lib/couchbase/data`, always does.  
> [!WARNING]  
> If the data path is not on any mount, the node's data lives only in the container's own filesystem, and is lost when the container is removed. Stop, and copy the data out of the container with `docker cp` before you continue.
3. Note how the container is attached to the network, and its published ports:  
```console  
docker inspect -f 'hostname={{.Config.Hostname}} domainname={{.Config.Domainname}} restart={{.HostConfig.RestartPolicy.Name}}{{range $net, $cfg := .NetworkSettings.Networks}}{{println}}network={{$net}} ip={{$cfg.IPAddress}} fixed-ip={{if $cfg.IPAMConfig}}{{$cfg.IPAMConfig.IPv4Address}}{{end}} aliases={{$cfg.Aliases}}{{end}}' ea1  
docker port ea1  
```  
Also note any other options you created the container with, such as environment variables (`-e`), resource limits, and extra mounts, for example a mounted `~/.aws` directory. The replacement container needs the same options. If you set the `CB_MASTER_PASSWORD` environment variable for encryption at rest, the replacement container must have it too.  
To keep a complete record, save the container's full description:  
```console  
docker inspect ea1 > ea1-inspect.json  
```

## [](#addressing)How the Node Keeps Its Address

The other nodes in the cluster reach a node by the hostname or IP address it was added with, which is the last value you noted in [Record Each Node Before You Start](#record-the-node). The node also checks its own address when it starts.

* **Added by hostname.**Create the replacement container on the same network, with the same `--hostname` and the same `--network-alias` values. Its IP address can change: the node is found by name. This is how the multi-node example in the image's README sets up its containers.
* **Added by IP address, on a user-defined network with a fixed IP address.**The `fixed-ip` value you noted is not empty. Create the replacement container on the same network with the same `--ip` value.
* **Added by IP address, on the default `bridge` network.**This is how the multi-node example in [Install with Docker](getting-started-docker.md) sets up its containers. The default network does not accept a fixed address, so Docker assigns one when the container starts. It reuses the address the stopped container had, as long as no other container has taken it in the meantime. Do not start any other container on the host while you replace this one, and check the replacement container's address as soon as it starts.  
If the address differs, the node refuses to start. It does not initialize itself as a new node, and the error log under `/opt/couchbase/var/lib/couchbase/logs` repeats a message like the following:  
Configured address `172.17.0.7` seems to be invalid. Will refuse to start for safety reasons.  
To recover, stop and remove the replacement container with `docker rm`, without `-v`. Then stop the container that holds the address, and create the replacement container again.

Published host ports (`-p`) play no part in the node's identity. Publish the same ports anyway, so that administrators and applications reach the cluster as before.

## [](#procedure)Procedure

Upgrade one container at a time. Verify each container, as described in [Verify Before Moving to the Next Container](#verify), before you move on to the next.

1. Stop the container:  
```console  
docker stop --time 120 ea1  
```
2. Copy the node's state aside. This deliberately excludes the bulk data and the logs. Nothing in the Docker procedure deletes the node's state, so this copy is a safeguard against removing the volume by mistake.  
For a volume, named or anonymous, run `tar` from a throwaway container that mounts the volume read-only. Replace `<volume>` with the volume name you noted, and `<ea-version>` with the version of the image the container runs:  
```console  
docker run --rm --entrypoint tar \
  -v <volume>:/ea-var:ro -v "$PWD":/backup \  
  couchbase/enterprise-analytics:<ea-version> \
  -C /ea-var/lib/couchbase -cf /backup/ea1-state.tar --exclude=./data --exclude=./logs .  
```  
For a bind mount, run `tar` on the host instead:  
```console  
tar -C <host_directory>/lib/couchbase -cf ea1-state.tar --exclude=./data --exclude=./logs .  
```  
Confirm that the copy contains the node's configuration before you continue:  
```console  
tar -tf ea1-state.tar | grep config/config.dat  
```
3. Rename the stopped container, and make sure Docker never restarts it:  
```console  
docker rename ea1 ea1-enterprise-analytics  
docker update --restart no ea1-enterprise-analytics  
```  
Keeping the stopped container keeps a record of how it was created, and keeps its volume in use, so that no prune removes it. It also frees the name `ea1` for the replacement container.  
> [!WARNING]  
> Never start the old container again. Once the replacement container is running, both containers would use the same volume at the same time.
4. Create the Operational Insights container, with the volume mounted at both paths, and with the network settings, ports, and other options you noted. For a node that was added by hostname, with an anonymous or named volume:  
```console  
docker run -d --name ea1 \
  --network <network> --hostname ea1.example.com --network-alias ea1.example.com \
  -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 \
  -v <volume>:/opt/couchbase/var \
  -v <volume>:/opt/enterprise-analytics/var \  
  couchbase/operational-insights:3.0.0  
```  
Adjust the command for your setup:

  * **Bind mount.**Mount the same host directory at both paths, for example `-v /srv/ea1:/opt/couchbase/var -v /srv/ea1:/opt/enterprise-analytics/var`.
  * **A separate volume for the data directory.**Mount it at the data path you noted, and at the matching path under `/opt/couchbase/var`, for example `-v ea1-data:/opt/enterprise-analytics/var/lib/couchbase/data -v ea1-data:/opt/couchbase/var/lib/couchbase/data`.
  * **A data path outside `/opt/enterprise-analytics/var`.**Mount its volume at exactly the same path as before.
  * **A fixed IP address.**Add `--ip` with the address you noted.
  * **The default `bridge` network.**Omit `--network`, `--hostname`, and `--network-alias`, and check the address straight away:  
  ```console  
  docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ea1  
  ```  
  The address must match the one the node was added with. If it does not, see [How the Node Keeps Its Address](#addressing).  
Do not run `node-init` or `cluster-init` on the new container. The node already belongs to the cluster.
5. Wait for the node to start. The REST interface answers within a minute or two:  
```console  
docker exec ea1 curl -s -o /dev/null -w '%{http_code}\n' \
  -u ${USERNAME}:${PASSWORD} http://localhost:8091/nodes/self  
```  
A `200` response means that the node is up. Continue with [Verify Before Moving to the Next Container](#verify).

## [](#verify)Verify Before Moving to the Next Container

Run the same check you ran at the start, and confirm the values match:

```console
docker exec ea1 curl -s -u ${USERNAME}:${PASSWORD} http://localhost:8091/nodes/self \
  | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["nodeUUID"], d["storage"]["hdd"][0]["path"], d["hostname"], d["version"])'
```

The UUID, the data path, and the node name must all match the values you noted in [Record Each Node Before You Start](#record-the-node), and the version must start with `3.0.0`. The data path still begins with `/opt/enterprise-analytics/var` if it did before: this is expected, and is the reason for the second mount.

Confirm that the data path exists in the new container:

```console
docker exec ea1 test -d "<data_path>" && echo data present
```

> [!WARNING]
> A different UUID means that the node initialized itself as a new, empty node. Stop the container immediately, and do not rebalance. The node might still look healthy. Check the mounts of the new container against the ones you noted, then remove it with `docker rm`, without `-v`, and create it again.

## [](#finish-the-upgrade)Finish the Upgrade

1. When every container has been replaced and verified, complete [Bring the Cluster Back Online](upgrade-cluster-offline.md#bring-the-cluster-back-online). In a Docker cluster, run the commands in any Operational Insights container, for example:  
```console  
docker exec ea1 /opt/couchbase/bin/couchbase-cli server-list \
  -c localhost:8091 -u ${USERNAME} -p ${PASSWORD}  
```
2. Confirm that the cluster has moved to Operational Insights 3.0\. Each node reports `3.0.0`:  
```console  
docker exec ea1 curl -s -u ${USERNAME}:${PASSWORD} http://localhost:8091/pools/default \
  | python3 -c 'import json,sys; [print(n["hostname"], n["status"], n["prodCompatVersion"]) for n in json.load(sys.stdin)["nodes"]]'  
```
3. Remove the old, stopped containers. Use `docker rm` without `-v`:  
```console  
docker rm ea1-enterprise-analytics  
```  
Keep the state copies until you're satisfied with the upgraded cluster.

> [!IMPORTANT]
> Keep both mounts for as long as the node exists. The node's recorded paths still point under `/opt/enterprise-analytics/var` after the upgrade, so any container you create for this node in future, for example to move to a later version, needs the volume at both paths, just as in this procedure.

If the node used an anonymous volume, it still does. Keep a note of the volume's name: Docker gives a new container an empty volume unless you name the existing one in `-v`.

The Operational Insights Web Console and its alerts can show the node's data disk as `/opt/enterprise-analytics/var`. This is expected.

## [](#known-limitations)Known Limitations

| Scenario                                                                                                   | Status                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Multi-version jumps, upgrading from an older Enterprise Analytics release straight to Operational Insights | Supported from every previously released version of Enterprise Analytics. The procedure does not depend on the predecessor's version.       |
| Docker Compose                                                                                             | Not yet documented. Change the image, and add the second mount to the service definition, so that both paths are served by the same volume. |
| Rollback or downgrade, from Operational Insights back to Enterprise Analytics                              | Not supported, and not validated.                                                                                                           |

## [](#see-also)See Also

* [Upgrade an Offline Cluster](upgrade-cluster-offline.md)
* [Offline Upgrade from Enterprise Analytics to Operational Insights](upgrade-ea-to-oi.md)
* [Upgrade an Online Docker Cluster, Full Capacity](upgrade-docker-cluster-online-full-capacity.md)
* [Install with Docker](getting-started-docker.md)