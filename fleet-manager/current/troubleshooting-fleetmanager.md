---
title: Troubleshooting and FAQs
description: Find answers to common Couchbase Fleet Manager questions, and fix
  issues with telemetry, cluster visibility, portal access, sign-in, users,
  cluster tagging, and subscriptions.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Fleet Manager
    version: "1.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-fleetmanager/edit/main/modules/ROOT/pages/troubleshooting-fleetmanager.adoc
  xref: xref:fleet-manager::troubleshooting-fleetmanager.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/fleet-manager/current/troubleshooting-fleetmanager.html)

# Troubleshooting and FAQs

> Find answers to common Couchbase Fleet Manager questions, and fix issues with telemetry, cluster visibility, portal access, sign-in, users, cluster tagging, and subscriptions. 

## [](#overview)Overview

This page covers issues that you can fix yourself from the Fleet Manager portal or your own environment. If an issue is not listed, or the steps here do not fix it, [contact Couchbase Support](../../server/current/introduction/contact-couchbase.md).

## [](#how-telemetry-works)How Telemetry Reaches Fleet Manager

Most issues on this page make sense once you know how telemetry reaches Fleet Manager.

* Each monitored cluster runs a Local Telemetry Collector, which ships with the Couchbase Server.
* The collector pushes usage snapshot to Fleet Manager approximately every 2 hours. Fleet Manager never polls your clusters and never stores cluster credentials.
* The collector finds Fleet Manager through the fixed hostname `couchbase.fleetmanager.internal`, over TLS on port 443\. To start telemetry collection, create a DNS record that maps this hostname to your Fleet Manager host.

When a cluster does not report, first check the cluster side. Check its version and setup, then check the DNS and the network path to Fleet Manager.

Does Fleet Manager send data to Couchbase? 

No. Fleet Manager runs entirely inside your network, and it never sends telemetry to Couchbase. It works in air-gapped networks.

Fleet Manager collects only infrastructure usage data, such as node counts and CPU cores. It never reads your documents, keys, or queries.

## [](#telemetry)Telemetry

Why is no telemetry visible even after 2 hours? 

Collectors report every 2 hours, so a new cluster can take up to 2 hours to appear. If you see nothing after that, check the following causes in order.

1. **No clusters are reporting telemetry.**Installing Fleet Manager does not add a cluster. The portal shows an empty fleet until at least 1 of your Couchbase Server clusters reports to it.
2. **The cluster runs an unsupported version.**Only Couchbase Server 7.6.12 and 8.0.3+ include the Local Telemetry Collector. Earlier versions never report, whatever your DNS or network settings.
3. **The cluster is not initialized.**A new Couchbase Server node waits at the setup wizard until you create a cluster. Finish the cluster setup in the Couchbase Server Web Console.
4. **DNS does not resolve `couchbase.fleetmanager.internal`, or resolves to the wrong address.**This is the most common setup failure.
5. **Fleet Manager is not published on host port 443.**The Collector always connects on port 443\. If you started the container with a different host port, such as `-p 8888:443`, the Collector cannot reach it.
6. **The network blocks port 443.**You can still configure or resolve DNS even when a firewall or security group blocks the connection.
7. **The cluster's clock is out of sync.**Fleet Manager rejects snapshots with a timestamp more than 1 hour in the future. If a cluster's clock runs ahead of the Fleet Manager host, that cluster never appears. Use Network Time Protocol (NTP) to keep the clocks on your cluster nodes and the Fleet Manager host in sync.
8. **The first report was rejected.**A new cluster sometimes sends its first report before it has a cluster UUID. In such cases, the Fleet Manager rejects the report. The next report succeeds, but arrives hours after the previous report. To skip the wait, restart a node in the cluster to trigger a new report.

Check that the cluster nodes and the Fleet Manager host use NTP.

## [](#cluster-visibility)Cluster Visibility

Why do some clusters appear in the portal and others do not? 

Each cluster reports on its own. If 1 cluster appears and another does not, something differs between them. Check these causes for each missing cluster:

| Cause                                                                          | Why it happens                                                                   | What to do                                                                                                         |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Unsupported Couchbase Server version.                                          | Only 7.6.12 and 8.0.3+ include the collector.                                    | Check the version and upgrade if needed.                                                                           |
| Cluster not initialized.                                                       | An uninitialized node has no cluster UUID and sends no reports.                  | Finish the cluster setup.                                                                                          |
| DNS does not resolve couchbase.fleetmanager.internal from the cluster's nodes. | The cluster cannot find Fleet Manager.                                           | Check DNS from every cluster node and make sure the private DNS zone is reachable.                                 |
| Port 443 blocked between the cluster and the Fleet Manager.                    | The cluster finds the Fleet Manager but cannot connect.                          |                                                                                                                    |
| Fleet Manager not published on host port 443.                                  | Collectors always connect on port 443.                                           | To change the reporting port, [contact Couchbase Support](../../server/current/introduction/contact-couchbase.md). |
| Cluster clock out of sync.                                                     | Fleet Manager rejects snapshots with a timestamp more than 1 hour in the future. | Use NTP on the cluster nodes and the Fleet Manager host.                                                           |
| New cluster, first report not sent yet.                                        | Reports arrive every 2 hours.                                                    | Wait 2 hours, or restart a node to trigger a report.                                                               |

To see why a specific cluster fails to report, search its Couchbase Server logs for telemetry messages.

```console
grep -i telemetry /opt/couchbase/var/lib/couchbase/logs/*.log
```

> [!NOTE]
> When the collector cannot reach Fleet Manager, it logs at `info` level. A lack of errors does not mean the collector is working.

Which Couchbase Server versions report to the Fleet Manager? 

Fleet Manager 1.0 supports clusters that run Couchbase Server 7.6.12 or Server 8.0.3+. Upgrade every cluster you want to track to a supported version.

Fleet Manager lists Enterprise and Couchbase Server Community Edition clusters in your inventory, but does not count them towards your subscription.

Fleet Manager 1.0 does not support Sync Gateway, Couchbase Autonomous Operator, or Capella clusters.

How to check that DNS is set up. 

Collectors look for Fleet Manager at `couchbase.fleetmanager.internal`. Create 1 DNS record, an A record or a CNAME, that points the hostname to your Fleet Manager host. This 1 record serves your whole fleet, and you do not need to configure each cluster. You might need your network administrator to add the record.

Point the record to an address that your clusters can reach. This is the IP address of the machine that runs the Fleet Manager container. Do not use the container's internal Docker IP address, for example `172.17.0.4`. Other machines cannot reach this address.

`.internal` is not a public top-level domain, hence create the record in a private DNS zone that every monitored cluster can use. For example, on AWS Route 53, create a private hosted zone named `fleetmanager.internal` and attach it to the VPC that your clusters run in. Then turn on DNS support and DNS hostnames for that VPC.

To test DNS, run the following command on a node in the missing cluster:

```console
dig +short couchbase.fleetmanager.internal
```

The command must return the IP address of the Fleet Manager host. If it does not return any IP address, the node cannot resolve the hostname. Check that the record exists and that the node's network can use that DNS zone.

Can Fleet Manager run on a port other than 443? 

You can open the portal on another port, but collectors cannot report to it. Collectors always connect to `couchbase.fleetmanager.internal` on port 443, and you cannot change this port yourself.

When you start the container, map host port 443 to container port 443 with `-p 443:443`. If you started the container with another host port, such as `-p 8888:443`, stop the container. Then start it again with `-p 443:443`, and keep the same volumes so that you keep your data.

If you must use another port, [contact Couchbase Support](../../server/current/introduction/contact-couchbase.md).

DNS resolves, but the cluster still does not report telemetry. 

DNS resolution alone is not enough. Every node in the cluster must also be able to connect to the Fleet Manager on TCP port 443.

To test the connection, run the following command on a node in the missing cluster.

```console
$ nc -vz -w 10 couchbase.fleetmanager.internal 443
```

* If the command reports that the connection succeeded, the node can reach Fleet Manager.
* If the command times out or if the connection is refused, a firewall or security group blocks the connection. Allow inbound TCP 443 to Fleet Manager from your clusters' networks.
* If `nc` is not installed on the node, ask your network administrator to test the connection.

Why is a cluster's Last seen time out of date? 

The **Last seen** column on the **Clusters** page shows when Fleet Manager last received a snapshot from each cluster. If the time is more than 4 hours, the cluster stops reporting.

## [](#portal-access)Portal Access

What if the Fleet Manager portal does not open? 

Fleet Manager runs as a container that includes both the portal and its own Couchbase Server. If either process stops, the container stops. Check the following in the mentioned order.

1. **The container is running.**Run `docker ps`. If the `FleetManager` container is not listed, read its logs with `docker logs FleetManager`.  
```console  
$ docker logs FleetManager  
```  
Common causes are:

  * You set only 1 of `FM_TLS_CERT` and `FM_TLS_KEY`. Set both, or neither.
  * You passed an invalid `--log-level` value. Use 1 of the following values:

    * `debug`
    * `info`
    * `warn`
    * `error`
    * `fatal`
  * The container's `ulimit` settings are too low for the Couchbase Server. Use the `ulimit` settings from the installation instructions.
2. **Port 443 is published.**The container must publish port 443 with `-p 443:443`. The portal and telemetry load both use this port.
3. **You use the correct URL.**Open `<https://<FLEET%5FMANAGER%5FHOST>/>`, and use `https`, not `http`. If you mapped a host port other than 443, add it to the URL, such as `<https://<FLEET%5FMANAGER%5FHOST>:8888/>`. Collectors still need port 443.
4. **The network can reach the host.**Check your Virtual Private Network (VPN), proxy, and firewall settings.

If the portal loads but every page returns an error, the internal Couchbase Server instance may have stopped. [Contact Couchbase Support](../../server/current/introduction/contact-couchbase.md).

Why does the browser show a certificate warning? 

If you do not supply a TLS certificate, Fleet Manager generates a self-signed certificate the first time it starts. Browsers do not trust self-signed certificates.

To remove the warning, mount a certificate that your organization trusts, and set both the `FM_TLS_CERT` and `FM_TLS_KEY` environment variables.

## [](#login)Login and Passwords

Why must the administrator password be changed before using Fleet Manager? 

The first `admin` account uses a temporary password, which is the same on every installation and is published in this documentation. To protect your installation, Fleet Manager makes you change it.

When you first log in as `admin`, Fleet Manager asks you for a new password. After you change it, Fleet Manager opens the `Overview` page. Change the password after installation, before anyone else can reach the portal.

Local users that an administrator adds also choose a new password the first time they log in.

Why does the Fleet Manager reject a new password? 

Fleet Manager uses the Couchbase Server password policy. Your password must:

* Be at least 12 characters long.
* Contain at least 1 uppercase letter.
* Contain at least 1 lowercase letter.
* Contain at least 1 digit.
* Contain at least 1 special character.

Why does Fleet Manager ask a new user to set a new password? 

This is expected. When an administrator adds a local user, the password they set is temporary. Fleet Manager asks the new user to choose their own password the first time they sign in. The new password must meet the rules.

Why can't the user sign in? 

Check the following:

* **Your username and password are correct.**Passwords are case-sensitive.
* **You use the correct account type.**Lightweight Directory Access Protocol (LDAP) users log in with their LDAP credentials.
* **An administrator has added you to Fleet Manager.**A valid LDAP login is not enough on its own. An administrator must also add you to the **Users** list and assign you a role.
* **The LDAP server is available.**If LDAP is unavailable, no LDAP user can sign in. An administrator can still log in with the local `admin` account.

Why was the user logged out? 

Fleet Manager ends the session if there is no activity for 30 minutes, or 8 hours after logging in. Each request resets the 30-minute idle timer.

## [](#users-access)Users and Access

New user cannot be added. 

Fleet Manager has 2 roles:

| Role   | Access                                                                      |
| ------ | --------------------------------------------------------------------------- |
| Admin  | Full read/write access including user management, audit, and configuration. |
| Viewer | Read-only access. No access to users, audit, or configuration.              |

To add a user, select **Users** from the side menu, and click **\+ Add User**. If you cannot add a user, check the following:

* **You have the Admin role.**Viewers cannot see the **Users** page or manage users. Ask an administrator to add the user for you, or to change your role.
* **The username is unique.**Each username must be unique in your Fleet Manager installation.
* **You chose the correct identity source.**Choose **Local Account** Identity Source for a user that Fleet Manager manages. Choose **LDAP** Identity Source for a user in your LDAP directory, and make sure LDAP is set up first.
* **The password meets the policy.**

Why can LDAP users not log in? 

LDAP login needs 2 things: the LDAP must be set up, and each LDAP user must have a Fleet Manager role. Check the following:

1. **LDAP is turned on.**Select **Users** from the side menu, click **Configure LDAP**, and click the **Enable LDAP user authentication**.
2. **The LDAP host is correct.**Check the hostname or IP address of your LDAP server. Ask your system administrator if you're not sure.
3. **Fleet Manager can reach the LDAP server.**Check that no firewall blocks the connection between the Fleet Manager host and the LDAP server.
4. **The user has a Fleet Manager role.**LDAP checks the user's password, but Fleet Manager decides what the user can do. An administrator must add the user on the **Users** page, with the LDAP identity source and a role.

If any of these checks fails, login fails even for a user whose LDAP credentials are valid.

Fleet Manager 1.0 does not support 'single sign on' (SSO) or OpenID Connect (OIDC).

What if LDAP is unavailable and nobody can log in? 

Log in with the local `admin` account. This account works even when LDAP is unavailable, which makes it your break-glass account. Fleet Manager records every use of it in the audit trail.

Keep the `admin` password somewhere safe for this reason.

## [](#cluster-tagging)Cluster Tagging

What if the **Tag Cluster** button is not visible? 

The **Tag Cluster** button is shown when the following conditions are true:

* At least 1 Couchbase Server Enterprise Edition cluster is not tagged.
* You have the Admin role. Viewers cannot tag clusters.
* You have not dismissed the banner in the browser session.

You can always tag a cluster from the **Clusters** page. Select the cluster, and click **Edit tagging**.

Do clusters need to be tagged? 

Tagging is not required, but it's recommended. The environment type you set decides which subscription a cluster counts against.

If you do not set an environment type, Fleet Manager uses the highest classification in your active subscriptions. Fleet Manager ranks classifications in the following order, from highest to lowest:

1. Production
2. Backup
3. Development
4. Test

**Cluster name** and **Business unit** help you find and group clusters, and do not affect usage.

## [](#subscriptions)Subscriptions

Why doesn't the subscription document load? 

To upload a subscription document, go to **Subscriptions** **Subscriptions**, and click **Replace Subscription**. When the document is valid, Fleet Manager shows its subscription details before you confirm. If the details do not appear, Fleet Manager has rejected the file.

The upload fails if any of the following is true:

| Cause                                                                                              | Solution                                                                                                                       |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| The file is not valid JSON, such as after an edit that leaves a missing bracket or a duplicate key | Upload the file as Couchbase sent it. Fleet Manager does not accept base64-encoded files.                                      |
| The file is larger than 1 MiB                                                                      | Ask your account manager or Couchbase Support for a corrected file.                                                            |
| The file has the wrong schema version                                                              | The file must use schemaVersion v1. Ask your account manager or Couchbase Support for a current file.                          |
| The file contains no subscriptions                                                                 | The file must contain at least 1 subscription. Ask your account manager or Couchbase Support for a corrected file.             |
| A start date comes after its end date                                                              | Each subscription's startAt must not come after its endAt. Ask your account manager or Couchbase Support for a corrected file. |
| A classification or support level value is not valid                                               | These fields accept only fixed values. Ask your account manager or Couchbase Support for a corrected file.                     |
| You do not have the Admin role                                                                     | Ask an administrator to upload the file.                                                                                       |

You cannot enter subscription details by hand in the portal. You must upload the file.

Why did the earlier subscriptions disappear after an upload? 

**Replace Subscription** replaces your whole subscription document. It does not add to it.

Make sure the new document contains every subscription you want to track. If a subscription is missing, ask Couchbase for a document that includes all of your subscriptions, and upload it again.

Why does Fleet Manager show a subscription alert? 

Fleet Manager compares your running clusters with your subscription document. It alerts you when you run Couchbase services outside your subscriptions, such as when your usage exceeds a subscription limit.

Before you act on an alert, check that the numbers are correct.

Why doesn't the usage match the subscription? 

Most differences come from how Fleet Manager counts usage, not from a calculation error. Check the following in order:

1. **A cluster does not report telemetry.**Fleet Manager counts only clusters that report telemetry. If a cluster does not report, its nodes are not shown under usage. For example, a cluster that runs an unsupported version never reports.
2. **A cluster has the wrong environment type.**Fleet Manager counts each node against the subscription that matches its environment type, support level, and instance size. A Test cluster counts against a Test subscription, not against a Production subscription. To change the type, select the cluster on the **Clusters** page, and click **Edit tagging**.
3. **A node is larger than your subscription allows.**If a node's logical cores or RAM exceed the instance size of every matching subscription, Fleet Manager counts it as **Not entitled**.
4. **Backup-only nodes count as 0.**Nodes that run only the Backup Service do not count towards your usage. They still appear in the inventory.
5. **Community Edition nodes do not count.**Fleet Manager lists Couchbase Server Community Edition nodes in your inventory, but leaves them out of your usage.
6. **Cores are logical cores.**Fleet Manager uses logical cores, which include hyper-threads, to match a node to an instance size. A node with 8 physical cores matches as 16 cores.
7. **Containers report their limits.**For containerized nodes, the collector reports the container's CPU and memory limits, not the host's specs.
8. **Usage lags behind recent changes.**Clusters report every 2 hours, so recent changes take up to 2 hours to appear.

## [](#contact-support)Contact Couchbase Support

Your Couchbase Server Enterprise Edition support contract covers Fleet Manager. If the steps on this page do not fix the issue, [contact Couchbase Support](../../server/current/introduction/contact-couchbase.md).

Include a Fleet Manager log bundle with your request. Fleet Manager does not upload logs automatically, because it can run in an air-gapped network.

Partial redaction replaces user names, hostnames, and addresses in known log fields with tokens. So share the bundle only with Couchbase Support.