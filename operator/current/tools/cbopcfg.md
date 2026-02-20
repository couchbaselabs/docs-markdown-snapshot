---
title: cbopcfg
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.9.x/docs/user/modules/ROOT/pages/tools/cbopcfg.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:operator::tools/cbopcfg.adoc[]
---

[View original HTML](/operator/current/tools/cbopcfg.html)

# cbopcfg

> [!IMPORTANT]
> The `cbopcfg` binary is deprecated and will be removed in a later release. Please use the [cao](cao.md) binary that features all the same sub commands.

## [](#installation)Installation

Make sure that you have downloaded the Operator [package](https://www.couchbase.com/downloads) and unpacked it.

After you unpack the download, the resulting directory will be titled something like `couchbase-autonomous-operator-kubernetes_x.x.x-linux_x86_64`.

* macOS
* Linux
* Windows

1. Open a Terminal window and go to the directory where the `cbopcfg` binary is located:  
```console  
$ cd couchbase-autonomous-operator-kubernetes_x.x.x-macos_x86_64/bin/  
```
2. Make the `cbopcfg` binary executable:  
```console  
$ chmod +x ./cbopcfg  
```
3. Move the binary into your PATH:  
```console  
$ sudo mv ./cbopcfg /usr/local/bin/cbopcfg  
```

> [!NOTE]
> On newer versions of macOS, you may encounter errors such as `cannot execute binary file` when trying to use the tools included in the Autonomous Operator package. If you encounter such an error, you’ll need to update your security settings as outlined in Apple’s [support article on macOS Gatekeeper](https://support.apple.com/en-us/HT202491). In System Preferences, click Security & Privacy, then click General. Click the lock and enter your password to make changes. Select App Store and identified developers under the header “Allow apps downloaded from.”

1. Open a command prompt and go to the directory where the `cbopcfg` binary is located:  
```console  
$ cd couchbase-autonomous-operator-kubernetes_x.x.x-linux_x86_64/bin/  
```
2. Make the `cbopcfg` binary executable:  
```console  
$ chmod +x ./cbopcfg  
```
3. Move the binary into your PATH:  
```console  
$ sudo mv ./cbopcfg /usr/local/bin/cbopcfg  
```

1. Open a command prompt and go to the directory where the `cbopcfg` binary is located:  
```console  
$ cd couchbase-autonomous-operator-kubernetes_x.x.x-windows_x86_64\bin\  
```
2. Add the `cbopcfg` binary into your PATH.

## [](#cbopcfg)cbopcfg

Couchbase Autonomous Operator configuration utility.

The cbopcfg tool is used to automate the life-cycle of the Autonomous Operator. It is responsible for creation and deletion of Autonomous Operator components. A typical installation involves installing the Couchbase custom resource definitions, then the Dynamic Admission Controller, and finally the Operator itself.

Additional details for each component are documented under each sub-command.

Alternative methods of life-cycle management are available in the form of Helm charts and the Couchbase Open Service Broker.

## [](#cbopcfg-create)cbopcfg create

Creates Couchbase Autonomous Operator components

## [](#cbopcfg-create-admission-flags)cbopcfg create admission \[flags\]

Creates the dynamic admission controller.

The DAC is designed to be deployed at the cluster scope (default). It monitors Couchbase resources as they are created and modified, accepting, or rejecting them, before they are persisted in etcd.

Use of the DAC is encouraged as it will report any configuration errors that are specific to deployment of Couchbase resources that aren’t available by default in the Kubernetes API. For example, this includes validating memory quotas are satisfiable, TLS certificates are correctly configured, and any resources referenced actually exist.

### [](#examples)Examples

```console
# Create admission controller (recommended).
cbopcfg create admission

# Create admission controller scoped to a namespace.
cbopcfg create admission --scope namespace --namespace-selector key=value

# Create admission controller with custom image and secure image registry.
cbopcfg create admission --image acme.corp/admission:1.0.0 --image-pull-secret secret-name

# Create admission controller without secret access.
cbopcfg create admission --validate-secrets=false

# Create admission controller with debug logging.
cbopcfg create admission --log-level debug
```

### [](#flags)Flags

\--cpu-limit

**Type**: quantity

**Default**: 1

CPU limit for constraining, only valid when used with --with-resources

\--cpu-request

**Type**: quantity

**Default**: 500m

CPU requested for scheduling, only valid when used with --with-resources

\--image

**Type**: string

**Default**: couchbase/admission-controller:

Operator image to use

\--image-pull-policy

**Type**: string

**Default**: IfNotPresent

Image pull policy to affect when the image is downloaded.

\--image-pull-secret

**Type**: string

Image pull secret to allow access to the operator image

\--log-level

**Type**: string

**Default**: info

Log level to generate logs at. "info", or "0", prints basic operations. "debug", or "1" prints extended information.

\--memory-limit

**Type**: quantity

**Default**: 200Mi

Memory limit for constraining, only valid when used with --with-resources

\--memory-request

**Type**: quantity

**Default**: 100Mi

Memory requested for scheduling, only valid when used with --with-resources

\--namespace-selector

**Type**: map

Required namespace selector to use when scope is set to 'namespace'. Format label=value\[,label=value\].

\--replicas

**Type**: int

**Default**: 1

The number of replicas in the deployment

\--scope

**Type**: string

**Default**: cluster

Whether to scope the Operator to a 'namespace' or to the 'cluster'.

\--validate-secrets

**Type**: bool

**Default**: true

Validates secrets referenced by Couchbase resources, and their contents e.g. TLS configuration, for validity

\--validate-storage-classes

**Type**: bool

**Default**: true

Validates storage classes referenced by Couchbase resources

\--with-resources

**Type**: bool

**Default**: false

Populates pod resource requests and limits

### [](#inherited-flags)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-create-backup-flags)cbopcfg create backup \[flags\]

Creates backup roles.

### [](#flags-2)Flags

\--iam-role-arn

**Type**: string

Adds the IAM Role ARN to the backup service account’s annotation. e.g arn:aws:iam::<ACCOUNT\_ID>:role/<IAM\_ROLE\_NAME>

### [](#inherited-flags-2)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-create-operator-flags)cbopcfg create operator \[flags\]

Creates the Couchbase Autonomous Operator.

The Operator is designed to be run at the namespace scope (default). It watches for creation of CouchbaseCluster resources in that namespace and provides automated provisioning, management and disaster recovery of Couchbase Server.

### [](#examples-2)Examples

```console
# Create operator (recommended).
cbopcfg create operator

# Create operator scoped to the cluster.
cbopcfg create operator --scope cluster

# Create operator with a custom image and secure image registry.
cbopcfg create operator --image acme.corp/operator:1.0.0 --image-pull-secret secret-name

# Create operator with debug logging.
cbopcfg create operator --log-level debug

# Create operator with extended timeouts (for slow platforms).
cbopcfg create operator --pod-creation-timeout 1h
```

### [](#flags-3)Flags

\--cpu-limit

**Type**: quantity

**Default**: 1

CPU limit for constraining

\--cpu-request

**Type**: quantity

**Default**: 500m

CPU requested for scheduling

\--image

**Type**: string

**Default**: couchbase/operator:

Operator image to use.

\--image-pull-policy

**Type**: string

**Default**: IfNotPresent

Image pull policy to affect when the image is downloaded.

\--image-pull-secret

**Type**: string

Image pull secret to allow access to the operator image.

\--log-level

**Type**: string

**Default**: info

Log level to generate logs at. "info" prints basic operations. "debug", or "1" prints extended information and API calls. "2" prints very detailed logs, including full API payloads that may contain passwords and keys.

\--memory-limit

**Type**: quantity

**Default**: 400Mi

Memory limit for constraining

\--memory-request

**Type**: quantity

**Default**: 200Mi

Memory requested for scheduling

\--optional-metric-labels

**Type**: string

Whether to add cluster uuid or cluster uuid and cluster name to prometheus metrics as labels. Allowed 'uuid-only' or 'uuid-and-name'.

\--pod-creation-timeout

**Type**: string

**Default**: 10m0s

How long to wait before declaring an error when provisioning a pod.

\--pod-delete-delay

**Type**: string

**Default**: 0s

How long to wait before performing a delete on a failed pod.

\--pod-readiness-delay

**Type**: string

**Default**: 10s

How long to wait before starting readiness probes on server pods.

\--pod-readiness-period

**Type**: string

**Default**: 20s

How long to wait between readiness probes on server pods.

\--scope

**Type**: string

**Default**: namespace

Whether to scope the Operator to a 'namespace' or to the 'cluster'.

\--separate-cluster-namespace-and-name

**Type**: bool

**Default**: true

Separates cluster name and namespace from certain metrics.

\--use-high-cardinality-metrics

**Type**: bool

**Default**: false

Adds high cardinality labels for http request metrics.

\--with-resources

**Type**: bool

**Default**: false

Populates pod resource requests and limits

### [](#inherited-flags-3)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-create-pod-flags)cbopcfg create pod \[flags\]

This command is for debug and recovery purposes only. It is intended to create a pod for a since removed pod, or a new pod when support needs to do so.

Note: The Couchbase Operator watches CouchbaseCluster resources and may immediately delete pods it considers unclustered. Pause or stop the Operator before using this command.

### [](#examples-3)Examples

```console
# Create pod scoped to the cluster with a specific index.
cbopcfg create pod --couchbase-cluster cb-example --server-class all_services --index 3

# Create pod scoped to a cluster with the next available index.
cbopcfg create pod --couchbase-cluster cb-example --server-class all_services --auto-index
```

### [](#flags-4)Flags

\--auto-index

**Type**: bool

**Default**: false

Use the persistence secret’s to generate a new pod with a new index

\--couchbase-cluster

**Type**: string

The cluster from which to create a pod definition for.

\--image

**Type**: string

The Couchbase Server image to use for the pod

\--index

**Type**: int

**Default**: 0

The index of the pod to create

\--server-class

**Type**: string

The server class from which to create a pod definition for.

### [](#inherited-flags-4)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-delete)cbopcfg delete

Deletes Couchbase Autonomous Operator components

## [](#cbopcfg-delete-admission-flags)cbopcfg delete admission \[flags\]

Deletes the dynamic admission controller.

### [](#examples-4)Examples

```console
# Delete admission controller (recommended).
cbopcfg delete admission

# Delete admission controller scoped to a namespace.
cbopcfg delete admission --scope namespace
```

### [](#flags-5)Flags

\--scope

**Type**: string

**Default**: cluster

Whether to scope the Operator to a 'namespace' or to the 'cluster'.

### [](#inherited-flags-5)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-delete-backup)cbopcfg delete backup

Deletes backup roles.

### [](#inherited-flags-6)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-delete-operator-flags)cbopcfg delete operator \[flags\]

Deletes the Couchbase Autonomous Operator.

### [](#examples-5)Examples

```console
# Delete operator (recommended).
cbopcfg delete operator

# Delete operator scoped to the cluster.
cbopcfg delete operator --scope cluster
```

### [](#flags-6)Flags

\--scope

**Type**: string

**Default**: namespace

Whether to scope the Operator to a 'namespace' or to the 'cluster'.

### [](#inherited-flags-7)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-generate)cbopcfg generate

Generates YAML manifests for various Operator components

## [](#cbopcfg-generate-admission-flags)cbopcfg generate admission \[flags\]

Generates YAML for the dynamic admission controller.

The DAC is designed to be deployed at the cluster scope (default). It monitors Couchbase resources as they are created and modified, accepting, or rejecting them, before they are persisted in etcd.

Use of the DAC is encouraged as it will report any configuration errors that are specific to deployment of Couchbase resources that aren’t available by default in the Kubernetes API. For example, this includes validating memory quotas are satisfiable, TLS certificates are correctly configured, and any resources referenced actually exist.

### [](#examples-6)Examples

```console
# Create admission controller (recommended).
cbopcfg generate admission

# Create admission controller scoped to a namespace.
cbopcfg generate admission --scope namespace --namespace-selector key=value

# Create admission controller with custom image and secure image registry.
cbopcfg generate admission --image acme.corp/admission:1.0.0 --image-pull-secret secret-name

# Create admission controller without secret access.
cbopcfg generate admission --validate-secrets=false

# Create admission controller with debug logging.
cbopcfg generate admission --log-level debug
```

### [](#flags-7)Flags

\--cpu-limit

**Type**: quantity

**Default**: 1

CPU limit for constraining, only valid when used with --with-resources

\--cpu-request

**Type**: quantity

**Default**: 500m

CPU requested for scheduling, only valid when used with --with-resources

\--image

**Type**: string

**Default**: couchbase/admission-controller:

Operator image to use

\--image-pull-policy

**Type**: string

**Default**: IfNotPresent

Image pull policy to affect when the image is downloaded.

\--image-pull-secret

**Type**: string

Image pull secret to allow access to the operator image

\--log-level

**Type**: string

**Default**: info

Log level to generate logs at. "info", or "0", prints basic operations. "debug", or "1" prints extended information.

\--memory-limit

**Type**: quantity

**Default**: 200Mi

Memory limit for constraining, only valid when used with --with-resources

\--memory-request

**Type**: quantity

**Default**: 100Mi

Memory requested for scheduling, only valid when used with --with-resources

\--namespace-selector

**Type**: map

Required namespace selector to use when scope is set to 'namespace'. Format label=value\[,label=value\].

\--replicas

**Type**: int

**Default**: 1

The number of replicas in the deployment

\--scope

**Type**: string

**Default**: cluster

Whether to scope the Operator to a 'namespace' or to the 'cluster'.

\--validate-secrets

**Type**: bool

**Default**: true

Validates secrets referenced by Couchbase resources, and their contents e.g. TLS configuration, for validity

\--validate-storage-classes

**Type**: bool

**Default**: true

Validates storage classes referenced by Couchbase resources

\--with-resources

**Type**: bool

**Default**: false

Populates pod resource requests and limits

### [](#inherited-flags-8)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-generate-backup-flags)cbopcfg generate backup \[flags\]

Generates YAML for backup jobs.

### [](#flags-8)Flags

\--iam-role-arn

**Type**: string

Adds the IAM Role ARN to the backup service account’s annotation. e.g arn:aws:iam::<ACCOUNT\_ID>:role/<IAM\_ROLE\_NAME>

### [](#inherited-flags-9)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-generate-operator-flags)cbopcfg generate operator \[flags\]

Generates YAML for the Couchbase Autonomous Operator.

The Operator is designed to be run at the namespace scope (default). It watches for creation of CouchbaseCluster resources in that namespace and provides automated provisioning, management and disaster recovery of Couchbase Server.

### [](#examples-7)Examples

```console
# Create operator (recommended).
cbopcfg generate operator

# Create operator scoped to the cluster.
cbopcfg generate operator --scope cluster

# Create operator with a custom image and secure image registry.
cbopcfg generate operator --image acme.corp/operator:1.0.0 --image-pull-secret secret-name

# Create operator with debug logging.
cbopcfg generate operator --log-level debug

# Create operator with extended timeouts (for slow platforms).
cbopcfg generate operator --pod-creation-timeout 1h
```

### [](#flags-9)Flags

\--cpu-limit

**Type**: quantity

**Default**: 1

CPU limit for constraining

\--cpu-request

**Type**: quantity

**Default**: 500m

CPU requested for scheduling

\--image

**Type**: string

**Default**: couchbase/operator:

Operator image to use.

\--image-pull-policy

**Type**: string

**Default**: IfNotPresent

Image pull policy to affect when the image is downloaded.

\--image-pull-secret

**Type**: string

Image pull secret to allow access to the operator image.

\--log-level

**Type**: string

**Default**: info

Log level to generate logs at. "info" prints basic operations. "debug", or "1" prints extended information and API calls. "2" prints very detailed logs, including full API payloads that may contain passwords and keys.

\--memory-limit

**Type**: quantity

**Default**: 400Mi

Memory limit for constraining

\--memory-request

**Type**: quantity

**Default**: 200Mi

Memory requested for scheduling

\--optional-metric-labels

**Type**: string

Whether to add cluster uuid or cluster uuid and cluster name to prometheus metrics as labels. Allowed 'uuid-only' or 'uuid-and-name'.

\--pod-creation-timeout

**Type**: string

**Default**: 10m0s

How long to wait before declaring an error when provisioning a pod.

\--pod-delete-delay

**Type**: string

**Default**: 0s

How long to wait before performing a delete on a failed pod.

\--pod-readiness-delay

**Type**: string

**Default**: 10s

How long to wait before starting readiness probes on server pods.

\--pod-readiness-period

**Type**: string

**Default**: 20s

How long to wait between readiness probes on server pods.

\--scope

**Type**: string

**Default**: namespace

Whether to scope the Operator to a 'namespace' or to the 'cluster'.

\--separate-cluster-namespace-and-name

**Type**: bool

**Default**: true

Separates cluster name and namespace from certain metrics.

\--use-high-cardinality-metrics

**Type**: bool

**Default**: false

Adds high cardinality labels for http request metrics.

\--with-resources

**Type**: bool

**Default**: false

Populates pod resource requests and limits

### [](#inherited-flags-10)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-generate-pod-flags)cbopcfg generate pod \[flags\]

This command is for debug and recovery purposes only. It is intended to generate a pod definition for a since removed pod, or a new pod when support needs to do so.

### [](#examples-8)Examples

```console
# Create pod scoped to the cluster with a specific index.
cbopcfg generate pod --couchbase-cluster cb-example --server-class all_services --index 3

# Create pod scoped to a cluster with the next available index.
cbopcfg generate pod --couchbase-cluster cb-example --server-class all_services --auto-index
```

### [](#flags-10)Flags

\--auto-index

**Type**: bool

**Default**: false

Use the persistence secret’s to generate a new pod with a new index

\--couchbase-cluster

**Type**: string

The cluster from which to create a pod definition for.

\--image

**Type**: string

The Couchbase Server image to use for the pod

\--index

**Type**: int

**Default**: 0

The index of the pod to create

\--server-class

**Type**: string

The server class from which to create a pod definition for.

### [](#inherited-flags-11)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-genspec-flags)cbopcfg genspec \[flags\]

Generates a spec file for a running Couchbase cluster

### [](#flags-11)Flags

\--cluster, -c

**Type**: string

The cluster hostname

\--password, -p

**Type**: string

Cluster admin password

\--username, -u

**Type**: string

Cluster admin username

### [](#inherited-flags-12)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-update)cbopcfg update

Updates Couchbase Autonomous Operator components

## [](#cbopcfg-update-webhook-flags)cbopcfg update webhook \[flags\]

refreshes the self signed certificate used by the validating webhook.

### [](#flags-12)Flags

\--scope

**Type**: string

**Default**: cluster

Whether to scope the Operator to a 'namespace' or to the 'cluster'.

### [](#inherited-flags-13)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use

## [](#cbopcfg-version)cbopcfg version

Prints the command version

### [](#inherited-flags-14)Inherited Flags

\--as

**Type**: string

Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

\--as-group

**Type**: stringArray

**Default**: \[\]

Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

\--as-uid

**Type**: string

UID to impersonate for the operation.

\--cache-dir

**Type**: string

**Default**: $HOME/.kube/cache

Default cache directory

\--certificate-authority

**Type**: string

Path to a cert file for the certificate authority

\--client-certificate

**Type**: string

Path to a client certificate file for TLS

\--client-key

**Type**: string

Path to a client key file for TLS

\--cluster

**Type**: string

The name of the kubeconfig cluster to use

\--context

**Type**: string

The name of the kubeconfig context to use

\--disable-compression

**Type**: bool

**Default**: false

If true, opt-out of response compression for all requests to the server

\--insecure-skip-tls-verify

**Type**: bool

**Default**: false

If true, the server’s certificate will not be checked for validity. This will make your HTTPS connections insecure

\--kubeconfig

**Type**: string

Path to the kubeconfig file to use for CLI requests.

\--namespace, -n

**Type**: string

If present, the namespace scope for this CLI request

\--request-timeout

**Type**: string

**Default**: 0

The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don’t timeout requests.

\--server, -s

**Type**: string

The address and port of the Kubernetes API server

\--tls-server-name

**Type**: string

Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

\--token

**Type**: string

Bearer token for authentication to the API server

\--user

**Type**: string

The name of the kubeconfig user to use