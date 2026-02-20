---
title: Create a VPC Peering Connection with AWS
description: Use this procedure to create a VPC Peering connection between
  Capella hosted with AWS and your application's VPC on AWS.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clouds/pages/vpc-peering/peer-aws.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clouds:vpc-peering/peer-aws.adoc[]
---

[View original HTML](/cloud/clouds/vpc-peering/peer-aws.html)

# Create a VPC Peering Connection with AWS

> Use this procedure to create a VPC Peering connection between Capella hosted with AWS and your application’s VPC on AWS. 

## [](#prerequisites)Prerequisites

To configure Couchbase Capella VPC peering with AWS, you need the following:

* One of the following Capella roles:

  * [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner)
  * [Project Owner](../../projects/project-roles.md#project-owner-role)
* The [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) installed and configured.

You must also preconfigure your AWS VPC by completing the following steps:

1. In AWS, enable **DNS hostnames** for the VPC:  
![Enable DNS hostnames for the VPC.](../_images/pn1-dns-hostname.png)
2. In AWS, enable **DNS resolution** for the VPC:  
![Enable DNS resolution for the VPC.](../_images/pn2-dns-res.png)
3. Make sure the CIDR block specified when creating your cluster does not overlap with the application VPC CIDR block. You can retrieve the CIDR block for a cluster [using the public API](../../management-api-reference/index.md#clusters/v3show).

## [](#procedure)Procedure

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to create a new private network.
3. Click **Settings** **VPC Peering**.
4. Click **Set Up VPC**.
5. Confirm the prerequisites and click **Next**.
6. In Capella, fill out the Network Details fields.  
> [!TIP]  
> You can find most of the required info for these fields on the page for your chosen VPC in AWS.  
Name  
Enter a name.  
AWS Account ID  
The numeric AWS Account ID.  
Virtual Network ID  
The alphanumeric VPC ID which starts with `vpc-`.  
Available Regions  
The AWS region where your VPC is deployed.  
CIDR Block  
The AWS VPC CIDR block of network in which your application runs. This cannot overlap with your Capella CIDR Block.
7. Click **Set Up VPC**.  
Capella sets up the private network. This typically takes up to a minute. When successful, Capella adds the private network to the list of private networks. You may briefly see the cluster enter a Deploying state while Capella sets up the new connection.  
When setup is complete, you can see the new network listed.  
> [!CAUTION]  
> While the network status is Complete, there are some final steps you must carry out before you can access your Capella cluster from your VPC using VPC peering.
8. Click the name of the new private network.
9. Run the two AWS CLI commands shown in Capella.  
You must run the two AWS CLI commands to accept the peering request and link your VPC to the appropriate DNS server for hostname resolution. Once you execute these commands, their output should be similar to the following example:  
```console  
$ aws ec2 accept-vpc-peering-connection --region=us-west-2 --vpc-peering-connection-id=pcx-004adebd9bf32a24f  
```  
```console  
{  
	"VpcPeeringConnection": {  
    	"AccepterVpcInfo": {  
        	"CidrBlock": "10.0.0.0/20",  
        	"CidrBlockSet": [  
            	{  
                	"CidrBlock": "10.0.0.0/20"  
            	}  
        	],  
        	"OwnerId": "264138468394",  
        	"PeeringOptions": {  
            	"AllowDnsResolutionFromRemoteVpc": false,  
            	"AllowEgressFromLocalClassicLinkToRemoteVpc": false,  
            	"AllowEgressFromLocalVpcToRemoteClassicLink": false  
        	},  
        	"VpcId": "vpc-09af4fa45689ca44c",  
        	"Region": "us-west-2"  
    	},  
    	"RequesterVpcInfo": {  
        	"CidrBlock": "10.0.16.0/20",  
        	"CidrBlockSet": [  
            	{  
                	"CidrBlock": "10.0.16.0/20"  
            	}  
        	],  
        	"OwnerId": "689827245340",  
        	"VpcId": "vpc-091c6caeba936ac48",  
        	"Region": "us-east-1"  
    	},  
    	"Status": {  
        	"Code": "provisioning",  
        	"Message": "Provisioning"  
    	},  
    	"Tags": [],  
    	"VpcPeeringConnectionId": "pcx-004adebd9bf32a24f"  
	}  
}  
```  
```console  
$ aws route53 associate-vpc-with-hosted-zone --hosted-zone-id=Z04089311NGVVH0FO3QGG --vpc=VPCId=vpc-09af4fa45689ca44c,VPCRegion=us-west-2 --region=us-east-1  
```  
```console  
{  
	"ChangeInfo": {  
    	"Id": "/change/C0508746QOHOO1XX5BH5",  
    	"Status": "PENDING",  
    	"SubmittedAt": "2021-12-03T16:58:38.401Z",  
    	"Comment": ""  
	}  
}  
```
10. Update the route table for your application’s VPC to make sure all traffic destined for your Capella cluster is appropriately routed:

  1. Identify the route table for your application VPC:  
  ![Finding the correct route table.](../_images/pn9-route-table.png)
  2. Edit the routes of this route table to add the Capella cluster as a new route.  
  Find the CIDR block of the Capella cluster, either from the Capella UI or from `RequesterVpcInfo` in the VPC peering request output. In this example, enter `10.0.16.0/20` as the destination. The target `VpcPeeringConnectionId` is `pcx-004adebd9bf32a24f` in this example.  
  ![Entering destination and target.](../_images/pn10-target.png)
11. If your VPC has any outbound security groups that limit outbound traffic to specific IPs, then you must also add the CIDR block for your Capella cluster to the outbound security group.

## [](#next-steps)Next Steps

* [Verify VPC Peering Connectivity](verify-troubleshoot.md)