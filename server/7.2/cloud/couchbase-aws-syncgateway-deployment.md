---
title: Deploy Couchbase Sync Gateway Using AWS Marketplace
description: Couchbase partners with Amazon to provide a packaged solution on
  AWS Marketplace.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cloud/pages/couchbase-aws-syncgateway-deployment.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/cloud/couchbase-aws-syncgateway-deployment.html)

# Deploy Couchbase Sync Gateway Using AWS Marketplace

> Couchbase partners with Amazon to provide a packaged solution on AWS Marketplace. This solution is based on Amazon CloudFormation templates that incorporate the latest features and best practices for deploying Couchbase Server on Amazon Web Services. 

Couchbase Sync Gateway on AWS Marketplace provides one of the fastest and easiest ways to get up and running on Amazon Web Services (AWS). At the core of this experience are Amazon CloudFormation templates that are developed in close collaboration with Amazon in order to adopt the latest features and best practices. Amazon Machine Images (AMIs) also provide the information required to launch an instance of a virtual server in AWS, thus making it easier and faster to deploy Couchbase Sync Gateway without having to create and manage schemas, or normalize, shard, and tune the database.

Couchbase Sync Gateway is available through AWS Marketplace with hourly pricing, or through a Bring Your Own License (BYOL) model.

## [](#prerequisites)Prerequisites

* You need an AWS account. If you don’t have one, [sign up](https://aws.amazon.com/) for one before proceeding.
* You should review the [best practices](couchbase-cloud-deployment.md#aws-best-practices) for deploying Couchbase Server on AWS.
* A Couchbase Server cluster deployed and running. You need the Cluster DNS or IP address where the server is running, the Couchbase username, Couchbase password. You also need the name of the bucket configured to use with Couchbase Sync Gateway.
* If you have deployed the Couchbase cluster via the AWS Marketplace experience, you can get the Cluster DNS/IP from this [step](couchbase-aws-marketplace.md#logging-in). Follow the steps documented [here](#sync-gateway::get-started-prepare.adoc#step-1create-a-bucket) to configure the server to work with Couchbase Sync Gateway. The main steps are setting up the bucket, setting up an RBAC user, and ensuring that the network access is set up correctly.

## [](#deploying-couchbase-sync-gateway)Deploying Couchbase Sync Gateway

> [!IMPORTANT]
> The CloudFormation templates are provided as a starting point and may be customized as needed.

1. Log in to your account on the [Amazon Web Services Marketplace](https://aws.amazon.com/marketplace/), search for `Couchbase` and select Couchbase Sync Gateway. Alternately, you can click [here](https://aws.amazon.com/marketplace/pp/prodview-dy76bh5kmehws) to go to the Couchbase Sync Gateway product page directly.
2. The Couchbase Sync Gateway product page provides a quick overview of the product offering and useful links. Click **Continue to Subscribe**.  
![aws marketplace Sync Gateway Continue to Subscribe](_images/aws/deploying/aws-marketplace-Sync-Gateway-Continue-to-Subscribe.png)
3. On the Subscribe to this software screen, accept the terms and conditions for this software.  
![aws marketplace Sync Gateway Accept Terms](_images/aws/deploying/aws-marketplace-Sync-Gateway-Accept-Terms.png)
4. Once your request is processed, you’ll be able to proceed by clicking **Continue to Configuration**.  
![aws marketplace Sync Gateway Continue to Configuration](_images/aws/deploying/aws-marketplace-Sync-Gateway-Continue-to-Configuration.png)
5. Configure the software by selecting CloudFormation Template from the **Fulfillment option** drop down.  
![aws marketplace Sync Gateway Select the Fulfilment option](_images/aws/deploying/aws-marketplace-Sync-Gateway-Select-the-Fulfilment-option.png)
6. You can also customize the Couchbase Server version and the region where the software will be deployed. Then click **Continue to Launch**.  
![aws marketplace Sync Gateway Select CloudFormation as Fulfillment option](_images/aws/deploying/aws-marketplace-Sync-Gateway-Select-CloudFormation-as-Fulfillment-option.png)
7. Review your configuration and then choose Launch CloudFormation from the **Choose Action** drop down to launch your configuration through the AWS CloudFormation console. Then click **Launch**.  
![aws marketplace Sync Gateway Launch](_images/aws/deploying/aws-marketplace-Sync-Gateway-Launch.png)
8. You will be redirected to the AWS CloudFormation Console where you must create a stack. A stack is a group of related resources that you manage as a single unit.

  1. In the **Specify template** section, choose the template source as the `Amazon S3 URL` and then click **Next**.  
  ![aws marketplace Sync Gateway Create Stack](_images/aws/deploying/aws-marketplace-Sync-Gateway-Create-Stack.png)
  2. In the **Specify stack details page**Enter the stack name  
  ![aws marketplace Sync Gateway Specify Stack Details Stack Name](_images/aws/deploying/aws-marketplace-Sync-Gateway-Specify-Stack-Details-Stack-Name.png)
  3. Enter the **Network Configuration/Access** parameters, specifically the VPC where you would like to deploy the software, list of subnets (make sure to choose at least two subnets in two different Availability Zones), CIDR range to permit ssh access to the EC2 instances where the software is installed, and the key-value pair to access the EC2 instances.  
  ![aws marketplace Sync Gateway Create Stack Parameters](_images/aws/deploying/aws-marketplace-Sync-Gateway-Create-Stack-Parameters.png)
  4. Enter the **Sync Gateway Configuration** parameters. The instance count, the SyncGateway version, and the AWS Instance Type for the Sync Gateway nodes.  
  ![aws marketplace Sync Gateway Configuration during Stack Creation](_images/aws/deploying/aws-marketplace-Sync-Gateway-Configuration-during-Stack-Creation.png)
  5. Enter the information for **Couchbase Server Configuration**, the Cluster DNS/IP, the Couchabse Username and Password, and the Couchbase bucket to use with Sync Gateway.  
  ![aws marketplace Sync Gateway Couchbase Configuration](_images/aws/deploying/aws-marketplace-Sync-Gateway-Couchbase-Configuration.png)
  6. In the **Other parameters** select the Sync Gateway disk type.  
  ![aws marketplace Sync Gateway Other Parameters](_images/aws/deploying/aws-marketplace-Sync-Gateway-Other-Parameters.png)
  7. Then click **Next**.
9. Optionally, in the **Configure stack options** page, you can specify tags for resources and other options in your stack and the required permissions. Click **Next**.  
![aws marketplace Sync Gateway Configure Stakc Options](_images/aws/deploying/aws-marketplace-Sync-Gateway-Configure-Stakc-Options.png)
10. Acknowledge that AWS CloudFormation may create IAM resources that provide entities access to make changes to your AWS account and click **Create**.  
![aws marketplace Sync Gateway create stack review options ack](_images/aws/deploying/aws-marketplace-Sync-Gateway-create-stack-review-options-ack.png)
11. The stack creation takes about 10 minutes to complete and the status is displayed on the screen. After the process is completed, you should see a `CREATE_COMPLETE` status.  
![aws marketplace Sync Gateway create stack complete](_images/aws/deploying/aws-marketplace-Sync-Gateway-create-stack-complete.png)

## [](#logging-in)Validating the Couchbase Sync Gateway

After the deployment is completed, you can explore the Sync Gateway resources created from the AWS EC2 dashboard.

![aws console ec2 dashboard Sync Gateway](_images/aws/logging-in/aws-console-ec2-dashboard-Sync-Gateway.png) 

1. Click **Load Balancers** tab in the EC2 service  
![aws console Sync Gateway ec2 load balancers](_images/aws/logging-in/aws-console-Sync-Gateway-ec2-load-balancers.png)
2. Copy the DNS name from the Description  
![aws console Sync Gateway load balancers dns](_images/aws/logging-in/aws-console-Sync-Gateway-load-balancers-dns.png)
3. Paste the DNS name with port 4984 into the browser to validate  
![aws Sync Gateway Validate](_images/aws/logging-in/aws-Sync-Gateway-Validate.png)