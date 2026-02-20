---
title: Deploy Couchbase Server Using AWS Marketplace
description: Couchbase partners with Amazon to provide a packaged solution on
  AWS Marketplace.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/cloud/pages/couchbase-aws-marketplace.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:cloud:couchbase-aws-marketplace.adoc[]
---

[View original HTML](/server/current/cloud/couchbase-aws-marketplace.html)

# Deploy Couchbase Server Using AWS Marketplace

> Couchbase partners with Amazon to provide a packaged solution on AWS Marketplace. This solution is based on Amazon CloudFormation templates that incorporate the latest features and best practices for deploying Couchbase Server on Amazon Web Services. 

Couchbase Server on AWS Marketplace provides one of the fastest and easiest ways to get up and running on Amazon Web Services (AWS). At the core of this experience are Amazon CloudFormation templates that are developed in close collaboration with Amazon in order to adopt the latest features and best practices. Amazon Machine Images (AMIs) also provide the information required to launch an instance of a virtual server in AWS, thus making it easier and faster to deploy Couchbase Server without having to create and manage schemas, or normalize, shard, and tune the database.

Couchbase is available through AWS Marketplace with hourly pricing, or through a Bring Your Own License (BYOL) model.

## [](#before-you-begin)Before You Begin

* You need an AWS account. If you don’t have one, [sign up](https://aws.amazon.com/) for one before proceeding.
* You should review the [best practices](couchbase-cloud-deployment.md#aws-best-practices) for deploying Couchbase Server on AWS.

## [](#deploying-couchbase-server)Deploying Couchbase Server

> [!IMPORTANT]
> The CloudFormation templates are provided as a starting point and may be customized as needed.

1. Log in to your account on the [Amazon Web Services Marketplace](https://aws.amazon.com/marketplace/), search for `Couchbase` and select Couchbase Enterprise Edition. Alternately, you can click [here](https://aws.amazon.com/marketplace/pp/prodview-zy5g2wqmqdyzw) to go to the Couchbase Server product page directly.
2. The Couchbase Server product page provides a quick overview of the product offering and useful links. Click **Continue to Subscribe**.  
![aws marketplace couchbase ee](_images/aws/deploying/aws-marketplace-couchbase-ee.png)
3. On the Subscribe to this software screen, accept the terms and conditions for this software.  
![aws marketplace couchbase ee subscription public terms](_images/aws/deploying/aws-marketplace-couchbase-ee-subscription-public-terms.png)
4. Once your request is processed, you’ll be able to proceed by clicking **Continue to Configuration**.  
![aws marketplace couchbase terms conditions](_images/aws/deploying/aws-marketplace-couchbase-terms-conditions.png)
5. Configure the software by selecting CloudFormation Template from the **Fulfillment option** drop down. You can also customize the Couchbase Server version and the region where the software will be deployed. Then click **Continue to Launch**.  
![aws marketplace couchbase ee configure 5](_images/aws/deploying/aws-marketplace-couchbase-ee-configure-5.png)
6. Review your configuration and then choose Launch CloudFormation from the **Choose Action** drop down to launch your configuration through the AWS CloudFormation console.  
![aws marketplace couchbase ee launch action](_images/aws/deploying/aws-marketplace-couchbase-ee-launch-action.png)
7. You will be redirected to the AWS CloudFormation Console where you must create a stack. A stack is a group of related resources that you manage as a single unit.

  1. In the **Specify template** section, choose the template source as the `Amazon S3 URL` and then click **Next**.  
  ![aws marketplace couchbase ee create stack select template](_images/aws/deploying/aws-marketplace-couchbase-ee-create-stack-select-template.png)
  2. In the **Specify stack details page**Enter the stack name  
  ![aws marketplace couchbase ee stack stackname](_images/aws/deploying/aws-marketplace-couchbase-ee-stack-stackname.png)
  3. Enter the **Network Configuration/Access** parameters, specifically the VPC where you would like to deploy the software, list of subnets, CIDR range to permit ssh access to the EC2 instances where the software is installed and the key-value pair to access the EC2 instances.  
  ![aws marketplace couchbase ee stack stack networkconfiguration](_images/aws/deploying/aws-marketplace-couchbase-ee-stack-stack-networkconfiguration.png)
  4. Enter the **Core Server Configuration** parameters. Other than specifying the database user name and password, you can choose to use the default values defined in the AWS CloudFormation template or edit them.  
  > [!NOTE]  
  > The user name and password will be required to log in to the Couchbase Server Web Console later.  
  ![aws marketplace couchbase ee stack stack coreinstanceconfiguration](_images/aws/deploying/aws-marketplace-couchbase-ee-stack-stack-coreinstanceconfiguration.png)
8. Optionally, if you plan to set up Couchbase Multi-Dimensional Scaling, you can customize the parameters in the **Multi-Dimension Scaling Configuration** section.
9. Then click **Next**.
10. Optionally, in the **Configure stack options** page, you can specify tags for resources and other options in your stack and the required permissions. Click **Next**.  
![aws marketplace couchbase ee create stack options](_images/aws/deploying/aws-marketplace-couchbase-ee-create-stack-options.png)
11. Acknowledge that AWS CloudFormation may create IAM resources that provide entities access to make changes to your AWS account and click **Create**.  
![aws marketplace couchbase ee create stack review options ack](_images/aws/deploying/aws-marketplace-couchbase-ee-create-stack-review-options-ack.png)
12. The stack creation takes about 10 minutes to complete and the status is displayed on the screen. After the process is completed, you should see a `CREATE_COMPLETE` status.  
![aws marketplace couchbase ee create stack complete](_images/aws/deploying/aws-marketplace-couchbase-ee-create-stack-complete.png)

## [](#logging-in)Logging in to Your Couchbase Cluster

After the deployment is completed, you can explore the resources created from the AWS EC2 dashboard.

![aws console ec2 dashboard](_images/aws/logging-in/aws-console-ec2-dashboard.png) 

Click **Instances(running)** under Resources to view the running instances of Couchbase Server. You can select a particular instance to view details such as the instance ID, state, IPv4 Public IP, and so on.

![aws console ec2 instances](_images/aws/logging-in/aws-console-ec2-instances.png) 

1. This step describes how to log in to the Couchbase Server Web Console.

  1. From the AWS EC2 console, select a running Couchbase Server Instance and copy the IPv4 Public IP.  
  ![aws console ec2 couchbase server instance public ip](_images/aws/logging-in/aws-console-ec2-couchbase-server-instance-public-ip.png)
  2. Open a browser tab and enter the copied IPv4 Public IP along with port 8091 as _<ipv4-public-ip>:8091_ to open the Couchbase Server Web Console.
  3. Enter the database administrator user name and password you configured when creating the stack to sign in.  
  ![aws couchbase ee login](_images/aws/logging-in/aws-couchbase-ee-login.png)
  4. Once you log in successfully, you can see the status of your Couchbase Server cluster on the dashboard.  
  ![aws couchbase web console dashboard](_images/aws/logging-in/aws-couchbase-web-console-dashboard.png)  
  Click the **Servers** tab to explore the sever nodes that have been created.  
  ![aws couchbase web console servers](_images/aws/logging-in/aws-couchbase-web-console-servers.png)