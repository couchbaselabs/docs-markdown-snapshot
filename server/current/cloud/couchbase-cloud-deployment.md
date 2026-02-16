[View original HTML](/server/current/cloud/couchbase-cloud-deployment.html)

> Couchbase Server is designed to run in the most popular cloud and container environments. Deploy Couchbase in the cloud for its unique data model flexibility, elastic scalability, high performance, and 24x365 availability. 

|  | Couchbase provides container images as a convenience to deploy our software and the only component in them that is supported for patches, including security fixes, is the Couchbase software itself. Customers who wish to have higher levels of control of the container image are encouraged to build a container image to their needs. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

| Platform                    | Documentation                                                                           |
| --------------------------- | --------------------------------------------------------------------------------------- |
| Amazon Web Services (AWS)   | [Deployment Methods](#aws-deployment-methods) [Best Practices](#aws-best-practices)     |
| Microsoft Azure             | [Deployment Methods](#azure-deployment-methods) [Best Practices](#azure-best-practices) |
| Google Cloud Platform (GCP) | [Deployment Methods](#gcp-deployment-methods) [Best Practices](#gcp-best-practices)     |
| Kubernetes and OpenShift    | [Deployment Methods](#k8s-deployment-methods)                                           |
| Docker                      | [Deployment Methods](#docker-deployment-methods)                                        |

## [](#amazon-web-services-aws)Amazon Web Services (AWS)

### [](#aws-deployment-methods)Deployment Methods

Manual Deployment

* [AWS Marketplace](couchbase-aws-marketplace.md)  
The AWS Marketplace provides one of the simplest methods for deploying and licensing Couchbase Server on AWS VMs.
* [AWS CloudFormation Templates](https://github.com/couchbase-partners/amazon-cloud-formation-couchbase)  
Couchbase provides several CloudFormation templates on GitHub to assist with deploying Couchbase Server on AWS.
* [Terraform](couchbase-aws-marketplace.md)  
Deploy Couchbase Server on AWS using a set of fully-featured, open source Terraform modules that define an ideal set of infrastructure components.

Orchestrated Deployment

* [Kubernetes (EKS and Unmanaged)](#operator:ROOT:install-eks.adoc)  
Use the Couchbase Autonomous Operator to deploy and manage Couchbase Server on Amazon Elastic Kubernetes Service (EKS) or open source Kubernetes clusters running in AWS.
* [Red Hat OpenShift](../../../operator/current/install-openshift.md)  
Use the Couchbase Autonomous Operator to deploy and manage Couchbase Server on OpenShift clusters running in AWS.

### [](#aws-best-practices)Best Practices

The recommendations in this section are based on internal testing performed by Couchbase on Amazon Elastic Compute Cloud (EC2). Many of these recommendations are incorporated into the AWS Marketplace offering by default.

Compute

* Use Amazon [EBS–optimized](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) instances.  
While any such node works well with Couchbase, some may be more cost effective. `r4` and `m4` machines are the most commonly used. For the majority of deployments, `m4.xlarge` provides a good balance of price and performance.
* [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) are recommended instead of stand alone instances, as it improves reliability and simplifies the addition and removal of nodes.
* The Couchbase concept of a [Server Group](../learn/clusters-and-availability/groups.md) maps closely to an [Availability Zone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html). You should deploy nodes across all available Availability Zones and then create a Couchbase Server Group per Availability Zone.

Storage

* EBS `gp3` and EBS `io1` are recommended.  
The persistence of EBS offers a significant advantage. For most deployments, EBS `gp3` provides a good balance of performance and cost.

|  | It is not recommended to exceed 1 TB for data drives. Large drives can lead to overly dense nodes that suffer from long rebuild times. It’s usually preferable to scale horizontally instead. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
* SSD [instance stores](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) are a viable storage option for Couchbase Server, and are both performant and side-step "noisy neighbor" issues that can potentially plague EBS. However, the instance store is ephemeral, expensive, and not encrypted, and therefore is not typically recommended.

Network

* DNS is recommended for most deployments. They perform very well, are extremely cost effective, and are resilient to failure.
* For deployments where nodes may be stopped and started, you could use an Elastic IP (EIP). However, EIPs add significant management complexity, and for that reason are not recommended for most deployments.
* [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) provide 10G network, which is preferable. However, they make using an Auto Scaling group more difficult because nodes will not be automatically spread across Availability Zones.

Security

* You should configure a [security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) that closes off [unused ports](../install/install-ports.md). This configuration can be further secured by specifying CIDR blocks to whitelist XDCR and client connectivity. It’s also recommended to restrict access to intra-cluster communication ports to the security group.
* Use of Secret Manager is recommended for storage of Couchbase Server credentials. Secret manager enables secure access for applications to [retrieve](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) database credentials. Secret manager also provides mechanisms for [rotating](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) your secrets automatically. Secret manager can also be configured to rotate secrets from within a [private VPC](https://aws.amazon.com/premiumsupport/knowledge-center/rotate-secrets-manager-secret-vpc/)If Couchbase Server is deployed by the AWS Marketplace Cloud Formation Template, admin credentials will be stored in a Secret Manager Secret.
* Disk encryption is recommended, and is [available for EBS disks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html). Disk encryption can be enabled account-wide by default and is recommended. If Couchbase Server is deployed by the AWS Marketplace Cloud Formation Template, the data disk will be encrypted.
* If using Couchbase Sync Gateway, it’s recommended that you secure the admin interface for access from `127.0.0.1` only. This can be configured using the Sync Gateway [configuration file](../../../sync-gateway/current/configuration/configuration-properties-legacy.md).

## [](#microsoft-azure)Microsoft Azure

### [](#azure-deployment-methods)Deployment Methods

Manual Deployment

* [Azure Marketplace](couchbase-azure-marketplace.md)  
The Azure Marketplace provides one of the simplest methods for deploying and licensing Couchbase Server on Azure VMs.
* [Azure Resource Manager Templates](https://github.com/couchbase-partners/azure-resource-manager-couchbase)  
Couchbase provides several Azure Resource Manager templates on GitHub to assist with deploying Couchbase Server on Azure.

Orchestrated Deployment

* [Kubernetes (AKS and Unmanaged)](#operator:ROOT:install-aks.adoc)  
Use the Couchbase Autonomous Operator to deploy and manage Couchbase Server on Azure Kubernetes Service (AKS) or open source Kubernetes clusters running in Azure.
* [Red Hat OpenShift](../../../operator/current/install-openshift.md)  
Use the Couchbase Autonomous Operator to deploy and manage Couchbase Server on OpenShift clusters running in Azure.

### [](#azure-best-practices)Best Practices

The recommendations in this section are based on internal testing performed by Couchbase on Azure Virtual Machines. Many of these recommendations are incorporated into the Azure Marketplace offering by default.

Compute

* Use instances that support Azure [Premium Storage](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/disks-types).  
While any such node works well with Couchbase, some may be more cost effective. `DS v3`, `ES v3`, `FS`, and `GS` machines are the most commonly used. For the majority of deployments, `DS14 v2` provides a good balance of price and performance.
* It’s recommended that you use [virtual machine scale sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview) (VMSS) instead of stand-alone VMs since they improve reliability and simplify the addition and removal of nodes.
* The current model for resilience is based on [availability sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability) that are made up of fault domains and upgrade domains. Virtual machine scale sets default to configuring 5 fault domains, each with their own upgrade domain. It’s recommended that you configure a [Server Group](../learn/clusters-and-availability/groups.md) for each fault domain.

Storage

* Azure [Premium Storage](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/disks-types) is recommended for data drives.  
Ephemeral drives present a risk of data loss. Standard Storage is based on spinning magnetic disks (HDD) and is sufficient for OS disks, but it does not perform well enough for most database applications. The older Azure storage account mechanism should also be avoided for OS and data disks, as it has a higher potential for bottlenecks and is more complex.

|  | It is not recommended to exceed 1 TB for data drives. Large drives can lead to overly dense nodes that suffer from long rebuild times. It’s usually preferable to scale horizontally instead. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
* Microsoft recommends disabling Premium Storage caching for mixed read/write workloads like Couchbase.

Network

* The recommended setup is to attach a public IP to each node. The public IP can be used to connect application drivers and replicate across geographies with XDCR.  
You should configure each Couchbase node with the public DNS. Because the public DNS resolves to a NAT-based IP, it’s recommended that you add a record to `/etc/hosts` on each node to resolve its public DNS to `127.0.0.1`. This allows Couchbase to bind to the IP underlying the public DNS.  
Traffic between public IPs in Azure is routed over the Azure backbone, which has very high bandwidth. This means that traffic is limited by the network cap of a VM.
* Other network setups like [VPN gateway](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways) and [ExpressRoute](https://docs.microsoft.com/en-us/azure/expressroute/expressroute-introduction) are not recommended. Microsoft seems to intend VPN gateways for client to server connections, not high performance clustered applications like Couchbase. ExpressRoute is a very expensive option that may work well for some on-prem/Azure hybrid solutions; but for general use, including Azure to Azure XDCR communication, it is not recommended.

Security

* You should configure a [security group](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) that closes off [unused ports](../install/install-ports.md). This configuration can be further secured by specifying CIDR blocks to whitelist XDCR and client connectivity. It’s also recommended to restrict access to intra-cluster communication ports to the security group.
* Disk encryption is recommended, and is [available for managed disks that use Premium Storage](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption).
* If using Couchbase Sync Gateway, it’s recommended that you secure the admin interface for access from `127.0.0.1` only. This can be configured using the Sync Gateway [configuration file](#sync-gateway:refer/config-properties.adoc).

## [](#google-cloud-platform-gcp)Google Cloud Platform (GCP)

### [](#gcp-deployment-methods)Deployment Methods

Manual Deployment

* [GCP Marketplace](couchbase-gcp-cloud-launcher.md)  
The GCP Marketplace provides one of the simplest methods for deploying and licensing Couchbase Server on GCP VMs.
* [GCP Deployment Manager Templates](https://github.com/couchbase-partners/google-deployment-manager-couchbase)  
Couchbase provides several GCP Deployment Manager templates on GitHub to assist with deploying Couchbase Server on GCP.

Orchestrated Deployment

* [Kubernetes (GKE and Unmanaged)](#operator:ROOT:install-gke.adoc)  
Use the Couchbase Autonomous Operator to deploy and manage Couchbase Server on Google Kubernetes Engine (GKE) or open source Kubernetes clusters running in GCP.
* [Red Hat OpenShift](../../../operator/current/install-openshift.md)  
Use the Couchbase Autonomous Operator to deploy and manage Couchbase Server on OpenShift clusters running in GCP.

### [](#gcp-best-practices)Best Practices

The recommendations in this section are based on internal testing performed by Couchbase on Google Compute Engine (GCE). Many of these recommendations are incorporated into the GCP Marketplace offering by default.

Compute

* GCE offers both pre-defined and custom [machine types](https://cloud.google.com/compute/docs/machine-types).  
For the majority of deployments, `n1-highmem-16` provides a good balance of price and performance.
* It’s recommended to deploy GCE nodes via a [managed instance group](https://cloud.google.com/compute/docs/instance-groups/) (MIG) as it improves reliability and simplifies the addition and removal of nodes. You can set up the MIG to place nodes across [zones](https://cloud.google.com/compute/docs/regions-zones/) in a round robin fashion. For most installs this will be sufficient. Ideally you should configure Couchbase [Server Groups](../learn/clusters-and-availability/groups.md) to map to zones.

Storage

* `pd-ssd` is recommended for the vast majority of deployments. It often outperforms ephemeral storage as it is network-bound and offers persistence that ephemeral does not.

|  | It is not recommended to exceed 1.7 TB for pd-ssd data drives. Large drives can lead to overly dense nodes that suffer from long rebuild times. It’s usually preferable to scale horizontally instead. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Network

* It’s recommended to configure nodes with their private DNS record. This is because the Google network is globally flat, allowing private IPs to be routed around the world without need for VPN or leased line solutions. (Though, when connecting with another cloud or an on-premises cluster in a hybrid scenario, VPN or leased lines are still required.)

|  | It’s not possible to configure a node with its public IP address because that IP is NAT-based and Couchbase cannot bind to it. GCP does not provide public DNS records for the public IPs. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Security

* You should configure a [firewall rule](https://cloud.google.com/vpc/docs/firewalls) that closes off [unused ports](../install/install-ports.md). This configuration can be further secured by specifying CIDR blocks to whitelist XDCR and client connectivity. It’s also recommended to restrict access to intra-cluster communication ports to the security group.
* Disk encryption is recommended.
* If using Couchbase Sync Gateway, it’s recommended that you secure the admin interface for access from `127.0.0.1` only. This can be configured using the Sync Gateway [configuration file](../../../sync-gateway/current/configuration/configuration-properties-legacy.md).

## [](#kubernetes-and-openshift)Kubernetes and OpenShift

The [Couchbase Autonomous Operator](../../../operator/current/overview.md) provides a native integration of Couchbase Server with Kubernetes and Red Hat OpenShift. It enables you to automate the management of common Couchbase tasks such as the configuration, creation, scaling, and recovery of Couchbase clusters.

### [](#k8s-deployment-methods)Deployment Methods

See [Couchbase Autonomous Operator](../../../operator/current/prerequisite-and-setup.md).

## [](#docker)Docker

Official Docker images for Couchbase Server are available on [Docker Hub](https://hub.docker.com/%5F/couchbase).

### [](#docker-deployment-methods)Deployment Methods

Manual Deployment

* [Basic Docker Installation](../install/getting-started-docker.md)