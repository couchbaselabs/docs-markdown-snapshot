[View original HTML](/cloud/reference/gcp.html)

> Couchbase Capella supports deploying clusters onto Google Cloud Platform (GCP). 

Couchbase Capella provides fully managed Couchbase Server clusters that can be deployed onto GCP. This page describes the various regions and configurations that are available to you when using Capella with GCP.

## [](#supported-regions)Supported Regions

Couchbase Capella’s fully managed DBaaS supports the following GCP regions.

* ✔ [App Services](#app-services:index.adoc) are supported in this region.

* Americas
* Europe
* Middle East and Africa
* Asia Pacific

| GCP Region                  | App Services? | Location                 |
| --------------------------- | ------------- | ------------------------ |
| **us-east1**                | **✔**         | US East (South Carolina) |
| **us-east4**                | **✔**         | US East (N. Virginia)    |
| **us-east5**                |               | US East (Columbus)       |
| **us-west1**                | **✔**         | US West (Oregon)         |
| **us-west2**                |               | US West (Los Angeles)    |
| **us-west3**                | **✔**         | US West (Utah)           |
| **us-west4**                | **✔**         | US West (Nevada)         |
| **us-central1**             | **✔**         | US Central (Iowa)        |
| **us-south1**               |               | US South (Dallas)        |
| **northamerica-northeast1** | **✔**         | Canada (Montréal)        |
| **northamerica-northeast2** |               | Canada (Toronto)         |
| **southamerica-east1**      | **✔**         | Brazil (São Paulo)       |
| **southamerica-west1**      |               | Chile (Santiago)         |

| GCP Region            | App Services? | Location    |
| --------------------- | ------------- | ----------- |
| **europe-west1**      | **✔**         | Belgium     |
| **europe-west2**      | **✔**         | London      |
| **europe-west3**      | **✔**         | Frankfurt   |
| **europe-west4**      | **✔**         | Netherlands |
| **europe-west6**      | **✔**         | Zurich      |
| **europe-west8**      |               | Milan       |
| **europe-west9**      |               | Paris       |
| **europe-central2**   |               | Warsaw      |
| **europe-north1**     | **✔**         | Finland     |
| **europe-southwest1** |               | Madrid      |

| GCP Region        | App Services? | Location     |
| ----------------- | ------------- | ------------ |
| **me-west1**      |               | Tel Aviv     |
| **me-central2**   | **✔**         | Dammam       |
| **africa-south1** |               | Johannesburg |

| GCP Region               | App Services? | Location  |
| ------------------------ | ------------- | --------- |
| **asia-east1**           | **✔**         | Taiwan    |
| **asia-east2**           | **✔**         | Hong Kong |
| **asia-northeast1**      | **✔**         | Tokyo     |
| **asia-northeast2**      |               | Osaka     |
| **asia-northeast3**      | **✔**         | Seoul     |
| **asia-south1**          | **✔**         | Mumbai    |
| **asia-south2**          |               | Delhi     |
| **asia-southeast1**      | **✔**         | Singapore |
| **asia-southeast2**      | **✔**         | Jakarta   |
| **australia-southeast1** | **✔**         | Sydney    |
| **australia-southeast2** |               | Melbourne |

## [](#zones)Zones

Each GCP region contains a number of independent zones. These consist of 1 or more discrete data centers that are isolated from failures in other zones. Capella can automatically distribute cluster nodes across multiple zones in a region for the highest availability. Every cluster in Capella is deployed with a minimum of 3 [nodes](#nodes). Except for free tier operational clusters, which deploy with only 1 node.

The **Multiple Zones** option is the default when creating clusters using the Developer Pro or Enterprise [Support Plans](../billing/billing.md#support-plans).

|  | The option to deploy across multiple GCP zones is only available for clusters that use the Developer Pro or Enterprise Support Plans. Clusters using the Basic Support Plan deploy all nodes to the same zone. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#configuration-options)Configuration Options

Clusters deployed onto GCP have several configuration options that allow you to customize clusters to fit your requirements.

### [](#nodes)Nodes

|  | As they’re intended for evaluation purposes only, free tier operational clusters only include 1 node. |
|  | ----------------------------------------------------------------------------------------------------- |

Clusters have a minimum of 3 nodes and a maximum of 27.

Clusters consist of Service Groups that include the Couchbase services deployed and system resources. Each Service Group has a node quantity to represent the number of nodes in the cluster with that configuration. Individual Service Groups can have between 2 and 27 nodes but cannot collectively exceed 27\. The Service Group that includes the [Data Service](../clusters/data-service/data-service.md) requires at least 3 nodes.

### [](#compute-and-memory)Compute and Memory

Capella provides the following compute configurations for clusters deployed onto Google Cloud.

__Table 1\. Google Cloud Compute Engine configurations__
| vCPU                        | Memory |
| --------------------------- | ------ |
| 2 vCPUs\[[1](#footnote-1)\] | 8 GB   |
| 4 vCPUs                     | 16 GB  |
| 4 vCPUs                     | 32 GB  |
| 8 vCPUs                     | 16 GB  |
| 8 vCPUs                     | 32 GB  |
| 8 vCPUs                     | 64 GB  |
| 16 vCPUs                    | 32 GB  |
| 16 vCPUs                    | 64 GB  |
| 16 vCPUs                    | 128 GB |
| 32 vCPUs                    | 128 GB |
| 32 vCPUs                    | 256 GB |
| 36 vCPUs                    | 72 GB  |
| 48 vCPUs                    | 96 GB  |
| 48 vCPUs                    | 192 GB |
| 48 vCPUs                    | 384 GB |
| 64 vCPUs                    | 256 GB |
| 64 vCPUs                    | 512 GB |
| 72 vCPUs                    | 144 GB |

\[[1](#gcp-configurations)\] Available for [free tier](https://cloud.couchbase.com/sign-up) and paid single node operational clusters.

### [](#storage-size)Storage Size

Capella clusters deployed onto Google Cloud Platform use SSD persistent disks (PD-SSD). These are suited for high-performance cluster needs that require lower latency and more IOPS than standard persistent disks provide.

The amount of storage available per node in your cluster is configurable from a minimum of 50 GB.

|  | Free tier operational clusters include 8 GB of data storage. |
|  | ------------------------------------------------------------ |

Clusters deployed on GCP support disk auto-expansion. For details, see [Storage Auto-Expansion](../clusters/scale-database.md#Storage-Auto-Expansion).

### [](#storage-speed)Storage Speed

Storage speed is measured in IOPS (input/output operations per second) that the cluster performs. Persistent disk speed is determined by the disk size and cannot be customized on its own. PD-SSDs receive 30 read and 30 write IOPS per GB provisioned, for an overall 60 IOPS per GB.

To increase the read and write performance of the disk, increase the storage size. For example, the default 50 GB storage has a maximum read speed of 1500 IOPS and a maximum write speed of 1500 IOPS. Increasing the storage to 100 GB increases the maximum read speed to 3000 IOPS and the maximum write speed to 3000 IOPS.

## [](#see-also)See Also

* [GCP Regions and Zones](https://cloud.google.com/compute/docs/regions-zones)
* [GCP storage performance limits](https://cloud.google.com/compute/docs/disks/performance#performance%5Flimits)

### [](#next-steps)Next Steps

To create or modify a Couchbase Capella cluster deployed onto GCP, see the following pages:

* [Create a cluster](../clusters/create-database.md)
* [Modify a cluster](../clusters/modify-database.md)