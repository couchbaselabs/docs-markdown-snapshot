[View original HTML](/operator/2.7/tutorial-sync-gateway.html)

> Connect the Couchbase Sync Gateway to a Couchbase cluster 

|  | Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Sync Gateway is a synchronization server that is responsible for secure data synchronization and routing between Couchbase Lite-enabled clients and Couchbase Server. It is an integral component of the [Couchbase Mobile](../../sync-gateway/current/index.md) platform.

This tutorial defines best practices for deploying Sync Gateway on Kubernetes. It covers basic connectivity between Sync Gateway and a Couchbase Cluster deployed by the Autonomous Operator.

## [](#prerequisites)Prerequisites

* A Couchbase Server cluster deployed and running. While it is _recommended_ that Couchbase Server is deployed on Kubernetes, it is _not required_. It is possible to deploy Sync Gateway on Kubernetes and connect it to a Couchbase Server cluster that is not on Kubernetes. However, this guide and all of its instructions assume that Couchbase Server is deployed on Kubernetes using the Autonomous Operator.

## [](#configuring-sync-gateway)Configuring Sync Gateway

Sync Gateway is configured with a configuration file within its container. The configuration contains sensitive data such as usernames, passwords, and TLS private keys. We therefore should define the configuration as a secret. Create a `sync-gateway-config.yaml` file with the relevant configuration variables. An example is shown below:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: sync-gateway
stringData:
  config.json: |-
    {
      "logging": {
        "console": {
          "enabled": true, (1)
          "log_level": "info", (2)
          "log_keys": [
            "*"
          ]
        }
      },
      "databases": {
        "cb-example": { (3)
          "server": "couchbase://cb-example-srv.my-namespace?network=default", (4)
          "bucket": "default", (5)
          "username": "Administrator", (6)
          "password": "password", (7)
          "users": {
            "GUEST": {
              "disabled": false,
              "admin_channels": [
                "*"
              ]
            }
          },
          "allow_conflicts": false,
          "revs_limit": 20,
          "enable_shared_bucket_access": true
        }
      }
    }
```

| **1** | logging.console.enabled enables logging to the console. This is especially relevant on Kubernetes where applications are expected to log to standard out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | logging.console.log\_level defines what messages are printed. For most use cases info is sufficient, however debug may provide additional information that can aid in problem determination.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **3** | databases.cb-example is the name of a database connection. The database name is arbitrary. In this instance we have named it after the CouchbaseCluster resource it references.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **4** | databases.cb-example.server defines the connection string of the Couchbase Server instance that Sync Gateway will connect to. The connection string may be determined in the same way as for [client SDKs](howto-client-sdks.md). The connection string in the example — couchbase://cb-example-srv.my-namespace — assumes that Sync Gateway and Couchbase Server are running on the same Kubernetes cluster. If we examine each part of the string: couchbase (as opposed to couchbases) specifies that the connection is over plain text and not secured by TLS cb-example is the name of the Couchbase cluster \-srv specifies that the connection utilizes DNS SRV lookup to [discover](howto-client-sdks.md#dns-based-addressing) Couchbase cluster pods running the Data Service ?network=default instructs Sync Gateway to [explicitly select](howto-client-sdks.md#client-explicit-network-selection) the internal network addresses of Couchbase cluster pods. _Requires Sync Gateway 2.8.2 or higher; otherwise omit this parameter._ my-namespace is the namespace in which the Couchbase cluster is deployed. The server property can technically accept connection endpoints as defined in the Sync Gateway [documentation](../../sync-gateway/current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-server). However, many of these connection endpoints are not recommended (some not even supported) when connecting to Couchbase Server deployments that are managed by the Autonomous Operator. In particular, there are [limitations when using exposed features](concept-couchbase-networking.md#sync-gateway-exposed-features-limitations) that affect which connection methods can be used with certain versions of Sync Gateway. |
| **5** | databases.cb-example.bucket defines the metadata.name to connect to and use to store mobile data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **6** | databases.cb-example.username defines the user that will be used to connect to the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **7** | databases.cb-example.password defines the user password that will be used to connect to the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

If the configuration file is named `sync-gateway-config.yaml`, the command to deploy it would be:

```console
$ kubectl create -f sync-gateway-config.yaml
```

### [](#enabling-tls-connectivity-to-couchbase-server)Enabling TLS Connectivity to Couchbase Server

TLS is fully supported between Sync Gateway and Couchbase Server. This includes [server-side TLS or mutual TLS](concept-tls.md).

Your Sync Gateway configuration can be modified to allow use of TLS as follows:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: sync-gateway
stringData:
  config.json: |-
    {
      "databases": {
        "cb-example": {
            "cacertpath": "/etc/sync_gateway/ca.pem", (1)
            "certpath": "/etc/sync_gateway/cert.pem", (2)
            "keypath": "/etc/sync_gateway/key.pem", (3)
        }
      }
    }
  ca.pem: |- (4)
    -----BEGIN CERTIFICATE-----
    MIIDSzCCAjOgAwIBAgIUDsYnaG+RFwhtoz9hSMwyzfoxOCcwDQYJKoZIhvcNAQEL
    ...
  cert.pem: |- (5)
    -----BEGIN CERTIFICATE-----
    MIIDXDCCAkSgAwIBAgIRAOUsHgVlGyJbvOIYuxD90x4wDQYJKoZIhvcNAQELBQAw
    ...
  key.pem: |- (6)
    -----BEGIN PRIVATE KEY-----
    MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDLaRvd8BxDBsPc
    ...
```

Certificates have been truncated for brevity.

| **1** | databases.cb-example.cacertpath defines where the CA certificate will be read from. This path is related to the deployment volume mount as described in [Deploying Sync Gateway](#deploying-sync-gateway) and the file name as described in this Secret.                              |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | **Mutual TLS Only:** databases.cb-example.certpath defines where the client certificate chain will be read from. This path is related to the deployment volume mount as described in [Deploying Sync Gateway](#deploying-sync-gateway) and the file name as described in this Secret. |
| **3** | **Mutual TLS Only:** databases.cb-example.keypath defines where the client key will be read from. This path is related to the deployment volume mount as described in [Deploying Sync Gateway](#deploying-sync-gateway) and the file name as described in this Secret.                |
| **4** | The ca.pem secret is the CA certificate. The name of this secret data item defines the file name as used by databases.cb-example.cacertpath in the Sync Gateway configuration.                                                                                                        |
| **5** | **Mutual TLS Only:** The cert.pem secret is the client certificate chain. The name of this secret data item defines the file name as used by databases.cb-example.certpath in the Sync Gateway configuration.                                                                         |
| **6** | **Mutual TLS Only:** The key.pem secret is the client key. The name of this secret data item defines the file name as used by databases.cb-example.keypath in the Sync Gateway configuration.                                                                                         |

If the configuration file is named `sync-gateway-tls.yaml`, the command to deploy it would be:

```console
$ kubectl apply -f sync-gateway-tls.yaml
```

### [](#configure-an-rbac-user-for-sync-gateway)Configuring an RBAC User for Sync Gateway

If not using client certificate authentication, secure the system further by using a limited role to access Couchbase Server. In doing so, the scope of operations that can be performed in the event that the Sync Gateway configuration is compromised is limited. The RBAC user corresponding to Sync Gateway can be manually configured as specified in the Sync Gateway [Getting Started Guide](#sync-gateway::get-started-prepare.adoc#configure-server).

Alternatively, you can take advantage of the [Couchbase user RBAC management](concept-user-rbac.md) capability introduced in Autonomous Operator 2.0\. With this method, the Autonomous Operator takes care of creating the relevant Sync Gateway user and binds it to a specified role. The following subsections assume that you will be using this feature.

#### [](#enabling-rbac-management)Enabling RBAC Management

RBAC security management on the Couchbase cluster defaults to `false`. Therefore, you’ll need to enable it by setting [couchbaseclusters.spec.security.rbac.managed](resource/couchbasecluster.md#couchbaseclusters-spec-security-rbac-managed) to true:

```yaml
security:
  rbac:
    managed: true
```

|  | Enabling RBAC management by the Autonomous Operator will remove any RBAC users that were manually created on the cluster. Therefore, you will need to specify the relevant users and role bindings for those RBAC users if you want to continue using those identities after enabling RBAC management. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

#### [](#creating-a-sync-gateway-rbac-user)Creating a Sync Gateway RBAC User

First, define a secret for the `sync-gateway` user that contains a password:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: sync-gateway
data:
  password: cGFzc3dvcmQ= (1)
```

| **1** | This example password is literally the encoded form of the word password. The correctly encoded form can be generated on a "UNIX-like" command line terminal with echo -n 'password' \| base64. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

If the configuration file is named `sync-gateway-rbac-user.yaml`, the command to deploy it would be:

```console
$ kubectl apply -f sync-gateway-rbac-user.yaml
```

This creates a sync gateway user with the specified password.

#### [](#role-binding-of-sync-gateway-user)Role Binding of Sync Gateway User

Next, define the `sync-gateway` user and bind it to a group that allows it the "application access" role as defined by Couchbase Server. The Autonomous Operator will create the required user and group on any Couchbase cluster that selects that user.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseUser
metadata:
  name: sync-gateway
  labels:
    cluster: my-cluster (1)
spec:
  authDomain: local (2)
  authSecret: sync-gateway (3)
---
apiVersion: couchbase.com/v2
kind: CouchbaseGroup
metadata:
  name: sync-gateway
spec:
  roles:
  - name: mobile_sync_gateway (4)
    bucket: default (5)
---
apiVersion: couchbase.com/v2
kind: CouchbaseRoleBinding
metadata:
  name: sync-gateway
spec:
  subjects:
  - kind: CouchbaseUser
    name: sync-gateway
  roleRef:
    kind: CouchbaseGroup
    name: sync-gateway
```

| **1** | The CouchbaseUser is labeled so it can be explicitly selected by a specific cluster. This is the recommended method of deployment as defined in the [label selection concepts](concept-label-selection.md).                                                       |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The CouchbaseUser uses the local authentication domain, meaning that a password will be locally installed on the Couchbase cluster for authentication.                                                                                                            |
| **3** | The CouchbaseUser references the secret we previously created so that the Autonomous Operator can associate the sync-gateway user with its password.                                                                                                              |
| **4** | The CouchbaseGroup that the sync-gateway user will be a member of needs the mobile\_sync\_gateway role.                                                                                                                                                           |
| **5** | The CouchbaseGroup that the sync-gateway user will be a member of only requires access to a single bucket. We therefore further limit scope to only enable modification of the default bucket. By default this would be set to \* granting access to all buckets. |

If the configuration file is named `sync-gateway-user-rolebinding.yaml`, the command to deploy it would be:

```console
$ kubectl apply -f sync-gateway-user-rolebinding.yaml
```

#### [](#configure-sync-gateway-with-the-rbac-user)Configure Sync Gateway with the RBAC User

Finally, to enable Sync Gateway to use the `sync-gateway` user, we’ll need to modify the configuration that we previously defined in [Configuring Sync Gateway](#configuring-sync-gateway):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: sync-gateway
stringData:
  config.json: |-
    {
      "databases": {
        "cb-example": {
          "bucket": "default", (1)
          "username": "sync-gateway", (2)
          "password": "password" (3)
        }
      }
    }
```

| **1** | The databases.cb-example.bucket attribute must match the bucket granted access to in the CouchbaseGroup.          |
| ----- | ----------------------------------------------------------------------------------------------------------------- |
| **2** | The databases.cb-example.username attribute must match the CouchbaseUser resource’s name.                         |
| **3** | The databases.cb-example.password attribute must match the plain-text password associated with the CouchbaseUser. |

If the configuration file is named `sync-gateway.yaml`, the command to deploy the configuration changes would be:

```console
$ kubectl apply -f sync-gateway.yaml
```

## [](#deploying-sync-gateway)Deploying Sync Gateway

Sync Gateway is a simple stateless application, and therefore does not require any application-specific controller like the Autonomous Operator. The following is a typical `Deployment` resource configuration for Sync Gateway:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sync-gateway
spec:
  replicas: 1 (1)
  selector:
    matchLabels:
      app: sync-gateway
  template:
    metadata:
      labels:
        app: sync-gateway
    spec:
      containers:
      - name: sync-gateway
        image: couchbase/sync-gateway:2.8.3-enterprise (2)
        volumeMounts:
        - name: config
          mountPath: /etc/sync_gateway (3)
          readOnly: true
        ports: (4)
        - name: http-api
          containerPort: 4984
        - name: http-metrics
          containerPort: 4986
        resources: (5)
          requests:
            cpu: 1
            memory: 1Gi
          limits:
            cpu: 2
            memory: 2Gi
        env:
        - name: GOMAXPROCS (6)
          value: "1"
      volumes:
      - name: config
        secret:
          secretName: sync-gateway (7)
```

| **1** | spec.replicas defines how many Sync Gateway pods to create. As Sync Gateway is stateless, this attribute can be modified to horizontally scale the deployment as needs require.                                                                                                                                                                                                                                                                                                                            |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | spec.template.spec.containers\[\].image defines the container image to deploy. Version 2.8.2 or higher is recommended as it has the fewest number of [network limitations](concept-couchbase-networking.md#sync-gateway-exposed-features-limitations).                                                                                                                                                                                                                                                     |
| **3** | spec.template.spec.containers\[\].volumeMounts\[\].mountPath mounts the configuration secret in the correct location. By default the Sync Gateway container will try to load configuration from /etc/sync\_gateway/config.json, and this is how the Secret and Deployment are configured.                                                                                                                                                                                                                  |
| **4** | spec.template.spec.containers\[\].ports\[\] defines the Sync Gateway ports. The sync-gateway port is required for Couchbase Mobile to connect to, this can be load balanced and exposed via a service, load-balancer or ingress. The metrics port is optional, and provides integration with Prometheus.                                                                                                                                                                                                   |
| **5** | spec.template.spec.containers\[\].resources allows the a pod’s resource requirements to be configured. We highly recommend that this is configured to ensure fair scheduling and access to the required resources. The actual values are dependent on your actual workload, and the ones depicted are an example only.                                                                                                                                                                                     |
| **6** | spec.template.spec.containers\[\].env allows environment variables to the passed to Sync Gateway. Particular attention should be paid to GOMAXPROCS and this defines the number of CPUs that Sync Gateway can use. This is directly related to the resources defined previously. If you have allocated 4 CPUs, you should set the maximum number of CPUs to 4 also. The limits should be above this number to allow for any overheads, as Kubernetes will terminate pods who exceed their resource limits. |
| **7** | spec.template.spec.volumes\[\].secret.secretName references the [Sync Gateway configuration](#configuring-sync-gateway) Secret that is mounted in the Sync Gateway container.                                                                                                                                                                                                                                                                                                                              |

Deploy the Sync Gateway cluster from the specified deployment controller file. If the above configuration is in a file named `sync-gateway.yaml`, the command to deploy it would be:

```console
$ kubectl apply -f sync-gateway.yaml
```

If successful, the equivalent of the following output will be returned:

```console
deployment.extensions "sync-gateway" created
```

You can check the status of the deployment with the following command:

```console
$ kubectl get deployments sync-gateway
```

If successful, a listing of the Sync Gateway pods that were deployed is returned. In the sample output below, 2 out of 2 requested Sync Gateway pods up and running:

```console
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
sync-gateway   2/2     2            2           24d
```

## [](#next-steps)Next Steps

At this stage, the Sync Gateway cluster is configured to communicate with Couchbase Server. You can now move on to [connecting Couchbase Lite clients](tutorial-sync-gateway-clients.md).

## [](#templates)Templates

Template files are provided in the Autonomous Operator binary distribution available at [couchbase.com/downloads](https://www.couchbase.com/downloads). These template files are provided as **evaluation examples** — they should be modified to suit production deployments.

* `sync-gateway.yaml`: Sample Deployment Controller for Sync Gateway using RBAC for server connectivity. This template creates a sync gateway RBAC user per procedures outlined in the previous section [Configuring an RBAC User for Sync Gateway](#configure-an-rbac-user-for-sync-gateway).
* `couchbase-custer.yaml`: Sample `CouchbaseCluster` custom resource deployment to be used with the Autonomous Operator.

|  | The couchbase-custer.yaml template has RBAC management set to false by default. So before you deploy the Sync Gateway cluster using the sync-gateway.yaml template, you must enable RBAC management as specified in the previous section [Configuring an RBAC User for Sync Gateway](#configure-an-rbac-user-for-sync-gateway). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | Red Hat OpenShift users will need to modify the provided template to reference an image pull secret. This must grant permission to pull container images from the Red Hat Container Registry. Refer to [Install the Operator on OpenShift](install-openshift.md) for details. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#further-reading)Further Reading

* [Sync Gateway Documentation](../../sync-gateway/current/index.md)
* [Exposing Sync Gateway to Couchbase Lite Clients](tutorial-sync-gateway-clients.md)