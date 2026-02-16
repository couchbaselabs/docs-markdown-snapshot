[View original HTML](/cloud/terraform/index.html)

> Use Terraform Provider to deploy and manage your clusters with declarative configuration. 

The Capella Terraform Provider is a powerful way of programmatically managing Capella API keys, users, organizations, projects, clusters, buckets, and other resources. Although the Capella UI is a great way of trying out Couchbase, for ease of deployment an Infrastructure-as-Code (IaC) approach offers advantages in defining your Capella deployment in a human-readable file, for re-using, versioning, sharing across departments, and automating away repetitive admin tasks.

## [](#before-you-start)Before You Start

You will need the following to get going:

* A recent version of [Terraform](https://developer.hashicorp.com/terraform/install) — 1.5.2 or newer.
* Go 1.2.1 or newer.

See the [compatibility page](terraform-compatibility.md) for a list of supported architectures and Operating Systems.

## [](#using-the-capella-terraform-provider)Using the Capella Terraform Provider

For authentication with the Couchbase Capella Provider a [V4 API key](../management-api-guide/management-api-start.md#understand-management-api-keys) must be generated. This API key is then used for authenticating the Terraform Provider.

Full instructions to get up and running are given in the [Capella Provider repo](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/README.md#using-the-provider). The Provider can be downloaded from the [Terraform Registry](https://registry.terraform.io/providers/couchbasecloud/couchbase-capella/latest).

The list of supported resources and schema definitions are detailed [in the Resources folder](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/tree/main/docs/resources).

### [](#example-usage)Example Usage

To get started, see the [Provider Example Configs](https://github.com/couchbasecloud/terraform-provider-capella/tree/main/examples):

* [Retrieve organization details in Capella](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/examples/organization):  
Couchbase Capella uses an ordered hierarchy to help you keep all of your data organized and securely accessible. The entity at the top of the hierarchy is called an organization. Everything you do in Capella — whether it’s creating a cluster or managing billing — happens within the scope of an [organization](../organizations/organizations.md).
* [Create and manage users](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/examples/user):  
Users have roles within an [organization](#organization:manage-organization-users.adoc), and within [individual projects](../projects/manage-project-users.md#project-users-summary).
* [Create and manage API Keys](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/examples/apikey):  
Every API key is associated with an allowed IP Address list, and one or more organization roles, which determine the [privileges that the API key has](../management-api-guide/management-api-start.md#understand-management-api-keys) within the organization.
* [Create & manage projects](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/examples/project):  
Within organizations, [projects](../projects/projects.md) are used to organize and manage groups of Couchbase clusters. An organization can contain any number of projects, and a project can contain any number of clusters.
* [Create & manage Capella clusters (clusters)](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/examples/cluster):  
The Cluster is the individual instance of a [Couchbase Database](../clusters/databases.md), spanning one or more nodes on your Cloud Service Provider, and containing the Data Service, and any other services which you choose to deploy. Within this sits the hierarchy of bucket, scope, collection, and document.
* [Retrieve cluster certificate details](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/examples/certificate):  
Retrive the certificate details for a Capella cluster; list the certificate details based on the cluster ID and authentication access token.
* [Manage cluster credential](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/examples/database%5Fcredential):  
Cluster credentials are separate from organization roles and project roles. A [cluster credential](../clusters/manage-database-users.md#about-database-credentials) is specific to a cluster and consists of a cluster access name, secret, and a set of bucket and scope access levels. It’s required for applications to remotely authenticate on a cluster and access bucket data.
* [Create & manage allowlists](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/examples/allowlist):  
More than one [allowlist](../security/security.md#access-management) gives extra security across testing, development, and deployment infrastructure, and different projects.
* [Create & manage buckets](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/blob/main/examples/bucket):  
The [buckets](../clusters/data-service/about-buckets-scopes-collections.md#buckets) is the top-level storage container for data in a Capella cluster.
* [Configure App Services](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/tree/main/examples/appservice):  
Create and manage [App Services](#app-services:index.adoc) in Capella.
* [Configure Bucket Backup & Restore](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/tree/main/examples/backup):  
Create and manage [Backups](../clusters/backup-restore.md) in Capella.

## [](#further-reading)Further Reading

* [Capella Terraform Provider repo](https://github.com/couchbasecloud/terraform-provider-couchbase-capella/tree/main) — contains docs and examples
* [Provider docs at Terraform Registry](https://registry.terraform.io/providers/couchbasecloud/couchbase-capella/latest/docs)
* [Terraform language docs](https://developer.hashicorp.com/terraform/language)