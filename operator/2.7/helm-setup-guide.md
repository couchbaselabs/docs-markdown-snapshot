---
title: Helm Deployment
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/helm-setup-guide.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.7@operator::helm-setup-guide.adoc[]
---

[View original HTML](/operator/2.7/helm-setup-guide.html)

# Helm Deployment

> Use the official Couchbase Helm Chart to deploy multiple components, including the Autonomous Operator, Admission Controller, Couchbase clusters, and Sync Gateway. 

[Helm](https://helm.sh/) is a tool that streamlines the installation and management of applications on Kubernetes platforms. The official Couchbase Helm Chart can help you easily set up the Couchbase Autonomous Operator and deploy Couchbase clusters.

This page describes how to use the Couchbase Helm Chart to create various deployments of the Autonomous Operator, Admission Controller, Couchbase clusters, and Sync Gateway.

The Couchbase Helm Chart is primarily intended to make it easy to deploy with the defaults to get a working system in an empty cluster. For more complex scenarios, make sure to refer to the operator documentation as well, particularly the [operator architecture](concept-operator.md) and [reference architecture](reference-reference-architecture.md).

A particular use case that is complex is upgrading so make sure to cover all the [Autonomous Operator upgrade](howto-operator-upgrade.md) and [Couchbase Server upgrade](concept-upgrade.md) sections.

The recommendation, for more complex scenarios, is to manage the operator directly rather than relying on Helm to do it as the operator provides a lot more direct control and this approach simplifies the upgrade process.

> [!IMPORTANT]
> The official Couchbase Helm Chart may only be used with Enterprise Edition products, such as Couchbase Server Enterprise Edition and Sync Gateway Enterprise Edition.

## [](#install-helm)Install Helm

[Helm 3.1+](https://github.com/helm/helm/releases%29) is required when installing the official Couchbase Helm Chart.

Follow Helm’s [official steps](https://helm.sh/docs/intro/install/) for installing `helm` on your particular operating system.

## [](#add-the-chart-repository)Add the Chart Repository

Before you can start using the Couchbase Helm Chart, you’ll need to add the chart repository to your `helm` installation:

```console
helm repo add couchbase https://couchbase-partners.github.io/helm-charts/
```

Finish by updating the repository index:

```console
helm repo update
```

## [](#install-the-couchbase-helm-chart)Install the Couchbase Helm Chart

Use the following commands to install the default Couchbase Helm Chart. The default chart deploys the Autonomous Operator, the Admission Controller, and a Couchbase cluster.

* Kubernetes
* OpenShift

```console
helm install <my-release> --set cluster.name=<cluster-name> couchbase/couchbase-operator
```

1. Create an image pull secret for retrieving images from the Red Hat Container Catalog:  
```console  
oc create secret docker-registry rh-catalog \
  --docker-server=registry.connect.redhat.com \
  --docker-username=<rhel-username> \
  --docker-password=<rhel-password> \
  --docker-email=<docker-email>  
```
2. Create a file named `openshift_values.yaml` with the following [custom override values](#custom-installation):  
```yaml  
couchbaseOperator:  
  image:  
    repository: registry.connect.redhat.com/couchbase/operator  
    tag: 2.7.0  
  imagePullSecrets:
  - rh-catalog  
admissionController:  
  image:  
    repository: registry.connect.redhat.com/couchbase/admission-controller  
    tag: 2.7.0  
  imagePullSecrets:
  - rh-catalog  
cluster:  
   image: registry.connect.redhat.com/couchbase/server:7.6.0-1  
```
3. Install the chart using the custom override values:  
```console  
helm install <my-release> -f openshift_values.yaml couchbase/couchbase-operator  
```

Installing the default chart provides a quick way to try out using the Autonomous Operator for managing Couchbase Server on Kubernetes platforms. However, for more involved development and production use-cases, you will need to customize the installation to better your needs.

## [](#custom-installation)Customize the Installation

The Couchbase Helm Chart can be installed as-is for previewing Autonomous Operator functionality. However, customizing the installation with your own configuration will be necessary for production environments.

Customizing the chart installation allows you to do two things:

1. Specify which components will be deployed
2. Configure the deployed components

The Couchbase Helm Chart is capable of installing and configuring the Autonomous Operator, Admission Controller, Couchbase cluster, and Sync Gateway. Enabling and configuring each component is accomplished by [overriding](https://helm.sh/docs/chart%5Ftemplate%5Fguide/values%5Ffiles/) the default values in the Couchbase Helm Chart’s [values.yaml file](helm-couchbase-config.md).

There are two methods for specifying overrides during chart installation: `--values` and `--set`.

* \--values
* \--set

The `--values` option is the preferred method because it allows you to keep your overrides in a YAML file, rather than specifying them all on the command line.

1. Create a YAML file and add your overrides to it.  
Here’s an example called `myvalues.yaml`:  
```yaml  
couchbaseOperator:  
  imagePullPolicy: Always  
```
2. Specify your overrides file when you install the chart:  
```console  
helm install my-release --values myvalues.yaml couchbase/couchbase-operator  
```  
The values in your overrides file (`myvalues.yaml`) will override their counterparts in the chart’s `values.yaml` file. Any values in `values.yaml` that weren’t overridden will keep their defaults.

If you only need to make minor customization, you can specify them on the command line by using the `--set` option. For example:

```console
helm install my-release --set cluster.servers.default.size=5 couchbase/couchbase-operator
```

This would translate to the following in the `values.yaml` of the chart:

```yaml
cluster:
  servers:
    default:
      size: 5
```

Any values in `values.yaml` that weren’t overridden will keep their defaults.

> [!IMPORTANT]
> As stated above, Helm works by override-only, with the chart providing various defaults. If you want to override a whole key in the chart, or replace it with another key, then you must _explicitly disable the default_ in addition to adding the new one.
> 
> For example, a default bucket is created unless you configure one or otherwise set `buckets: null` in the values file or `buckets=null` on the command line. Likewise, the default server configuration will always be created unless you set `servers.default` to `null`.
> 
> For additional information, refer to the Helm documentation on [deleting a default key](https://helm.sh/docs/chart%5Ftemplate%5Fguide/values%5Ffiles/#deleting-a-default-key).

### [](#selective-deployment)Selective Deployment

In many cases you may only want to install a single component, such as a Couchbase cluster, or an instance of Sync Gateway. Specific components may be enabled/disabled by overriding the default values in the `install` section of the chart:

```yaml
# Select what to install
install:
  # install the couchbase operator
  couchbaseOperator: true
  # install the admission controller
  admissionController: true
  # install couchbase cluster
  couchbaseCluster: true
  # install sync gateway
  syncGateway: false
```

For example, if you wanted to have a Helm release that exclusively managed the Autonomous Operator and Admission Controller, then you would override the value for `couchbaseCluster` with a value of `false`, leaving only `couchbaseOperator: true` and `admissionController: true`, and all others `false`. Likewise, if you already had the Autonomous Operator and Admission Controller deployed in your environment, and you just wanted to deploy a Couchbase cluster, then you would override the values for `couchbaseOperator` and `admissionController` with a value of `false`, leaving only `couchbaseCluster: true`, and all others `false`.

Even though the Couchbase Helm Chart has full configuration parameters for each component, if a component is disabled in the `install` section, then that component’s configuration parameters are ignored.

### [](#users)Users

By default, when creating a custom user, the corresponding Group resource is automatically created and bound.

```yaml
users:
  developer:
    # When autobind is 'true' then the user is
    # created and automatically bound to a group named 'developer'.
    autobind: true
    # password to use for user authentication
    # (alternatively use authSecret)
    password: password
    # optional secret to use containing user password
    authSecret:
    # domain of user authentication
    authDomain: local
    # roles attributed to group
    roles:
      - name: bucket_admin
        bucket: default
```

To manually configure the corresponding Group resource, set `users.<name>.autobind` to `false` and specify the `groups` and `rolebindings` resources.

## [](#deploying-sync-gateway)Deploying Sync Gateway

Sync Gateway is disabled by default in the Couchbase Helm Chart. To install the chart with Sync Gateway _enabled_, you will need to [customize the installation](#custom-installation) to include it:

```console
helm install mobile --set install.syncGateway=true couchbase/couchbase-operator
```

By default, Sync Gateway is only exposed to the internal Kubernetes network with a `ClusterIP` service. To change the type of service that is used to expose Sync Gateway, you can specify an override for `syncGateway.exposeServiceType` during installation:

```console
helm install mobile --set install.syncGateway=true --set syncGateway.exposeServiceType=LoadBalancer couchbase/couchbase-operator
```

For more information about using Sync Gateway with the Autonomous Operator, you can refer to the [Sync Gateway Tutorial](tutorial-sync-gateway.md).

## [](#deploy-production)Production Considerations

### [](#tls-encryption)TLS Encryption

Production deployments should enable TLS to encrypt traffic between the Autonomous Operator and the Couchbase cluster. TLS certificates can be auto-generated, or provided by the user.

#### [](#auto-generated-certificates)Auto-Generated Certificates

Install the chart with `tls` enabled:

```console
helm install my-release --set tls.generate=true couchbase/couchbase-operator
```

The Autonomous Operator will create the certificates and then configure them as Kubernetes Secrets for the cluster.

> [!NOTE]
> There is an issue ([K8S-1900](https://issues.couchbase.com/browse/K8S-1900)) that may cause a certificate error when using the Helm chart to upgrade the Autonomous Operator:
> 
> certificate cannot be verified for zone
> 
> This issue is caused by the certificate not having the necessary subject alternative names (SANs) required by the new version of the Autonomous Operator.
> 
> To resolve this issue, start by regenerating the Secrets from the new chart version:
> 
> ```console
> helm template my-release --values values.yaml couchbase/couchbase-operator > secrets.yaml
> ```
> 
> The `secrets.yaml` file that is created by the command above will now contain the Kubernetes Secret definitions for the cluster. Remove anything else from the file other than the Secrets with the `-operator-tls` and `-server-tls` suffixes for your release. Now update the Secrets in Kubernetes with the new ones:
> 
> ```console
> kubectl apply -f secrets.yaml
> ```
> 
> The Autonomous Operator should now pick up the new certificates and proceed through the upgrade process.

#### [](#bring-your-own-certificates)Bring Your Own Certificates

Create a file named `tls_values.yaml` with the following [custom override values](#custom-installation) for the Couchbase Helm Chart:

```yaml
cluster:
   tls:
     static:
       operatorSecret: tls-operator-secret
       serverSecert: my-tls-server-secret
```

Install the chart using the custom override values.

```console
helm install my-release -f tls_values.yaml couchbase/couchbase-operator
```

### [](#deploying-multiple-chart-instances-releases)Deploying Multiple Chart Instances (Releases)

The example installation commands on this page assume the default namespace is used (these commands don’t specify the `-n` option). This is important to note because the Couchbase Helm Chart deploys both the Autonomous Operator and the Admission Controller by default, _and these components should not be deployed more than once in the same namespace_.

_The Admission Controller should only be deployed once per Kubernetes cluster_ as indicated in [Selective Deployment](#selective-deployment) and in the [operator architecture](concept-operator.md#dynamic-admission-controller). To prevent deployment of the Admission Controller by the Couchbase Helm Chart, you can set the `install.admissionController=false` parameter either in the values file or on the command line:

```console
helm install my-release --set install.admissionController=false couchbase/couchbase-operator
```

If you install the default Couchbase Helm Chart multiple times in the same namespace, then you’ll end up with multiple instances of the Autonomous Operator and the Admission Controller, which will cause errors in your deployments.

In addition, the example installation commands on this page also specify `my-release` as the name for the [chart release](https://helm.sh/docs/glossary/#release). If you plan to use Helm to install multiple instances (releases) of the Couchbase Helm Chart, you should consider giving each release a unique name to help you more easily identify the resources that are associated with each release.

If you want Helm to generate a name for you, you can run any of the example installation commands on this page using the `-g` option instead of the name parameter:

```console
helm install -g couchbase/couchbase-operator
```

### [](#chart-versions)Chart Versions

> [!IMPORTANT]
> It is **not** recommended to install different versions of the Couchbase Helm Chart in the same Kubernetes cluster.

The `helm install` command will always pull the highest version of a chart. To list the versions of the Couchbase Helm Chart that are available for installation, you can use the `helm search` command:

```console
helm search hub couchbase
```

```console
NAME                        	                      CHART VERSION	APP VERSION	DESCRIPTION
https://hub.helm.sh/charts/couchbase/couchbase-...	2.1.0        	2.1.0      	A Helm chart to deploy the Couchbase Autonomous...
```

Here, the `CHART VERSION` is **2.1.0**, and the `APP VERSION` (the Autonomous Operator version) is **2.1.0**.

To install a specific version of the Couchbase Helm Chart chart, include the `--version` argument during installation:

```console
helm install my-release --version 2.1.0 couchbase/couchbase-operator
```

> [!NOTE]
> If you’re having trouble finding or installing a specific version of a chart, use the `helm repo update` command to ensure that you have the latest list of charts.