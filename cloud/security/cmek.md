---
title: Use Customer-Managed Encryption Keys (CMEK)
description: Capella encrypts cluster volumes at rest. You can move control of
  the keys from Couchbase to your own key management system (KMS).
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/security/pages/cmek.adoc
pubDate: 2026-02-24T03:43:07.775Z
link: xref:cloud:security:cmek.adoc[]
---

[View original HTML](/cloud/security/cmek.html)

# Use Customer-Managed Encryption Keys (CMEK)

> Capella encrypts cluster volumes at rest. You can move control of the keys from Couchbase to your own key management system (KMS). 

By default, all clusters in Couchbase Capella use your cluster’s cloud provider KMS to encrypt cluster volumes at rest. Instead of using this Couchbase-managed solution, you can create your own encryption keys for data at rest using customer-managed encryption keys (CMEK). By managing your encryption keys, you control their configuration, rotation cycles, geographic storage location, and can directly revoke them.

> [!NOTE]
> Backups and CMEK
> 
> Customer-managed encryption keys for bucket backups are not available at this time. To manage your encryption keys for a bucket backup, you can run your backup outside Capella. If you use CMEK on your cluster for encryption at rest, Capella encrypts your [cluster backups](../clusters/cloud-snapshots.md) with the same key used to encrypt your cluster storage.
> 
> You cannot use CMEK for Azure cluster backups with [cross-region copies](../clusters/cloud-snapshots.md#cross-region). Only AWS clusters support encrypting cross-region backup copies with CMEK.
> 
> Do not delete a Key Management System (KMS) Key ID until any cluster backups using that Key ID have expired. If you delete the Key ID, your backup becomes unusable. Encryption Key IDs must be enabled and available to restore an encrypted backup to a Capella cluster.

## [](#key-management-provider-support)Key Management Provider Support

Capella supports the following customer key management providers for encryption at rest:

* [AWS Key Management Service](https://aws.amazon.com/kms/)
* [GCP Cloud Key Management](https://cloud.google.com/security/products/security-key-management?hl=en)
* [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault)

Capella supports both the Standard and Premium tier of Azure Key Vault, including Managed Hardware Security Module (HSM) keys. If you want to use a firewall with your Azure Key Vault and Capella Azure CMEK, [contact Couchbase Capella Support](../support/manage-support.md).

Azure keys can be created at the organization level or the project level in Capella. You cannot use project-level keys with AWS or GCP.

Couchbase recommends using 1 key per cluster and not sharing keys across clusters.

CMEK is available to clusters using the [Enterprise plan](../support/support.md#support-levels).

## [](#configure-capella-to-use-customer-key-management)Configure Capella to Use Customer Key Management

To use CMEK on Capella, you must:

1. Complete the [Prerequisites](#prerequisites) for your cloud service provider.
2. [Enable Customer-Managed Encryption Keys on Capella](#enable-cmek), based on the instructions for your specific cloud service provider.
3. [Add a Customer-Managed Encryption Key](#add-cmek).
4. [Create a Cluster Using a Customer-Managed Encryption Key](#create-cluster) or [Apply a Customer-Managed Encryption Key to an Existing Cluster](#apply-to-cluster).

You must add and manage your keys through the Management API. Through the Management API, you can:

* Enable CMEK for a specific cloud service provider.
* Add a customer-managed encryption key.
* Get the details of a key based on its ID.
* Get a list of keys created in an organization.
* Rotate a key to replace an existing key with a new one.
* Delete an existing key.
* Associate a key with a cluster to enable encryption.
* Disassociate a key with a cluster.

For the details and requirements of each call, see the [Management API Reference](../management-api-reference/index.md). If you’re new to the Management API, see [Get Started with the Management API](../management-api-guide/management-api-start.md).

### [](#prerequisites)Prerequisites

* AWS
* GCP
* Azure (Organization)
* Azure (Project)

* You have a [Management API key](../management-api-guide/management-api-start.md#generate-management-api-keys) with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role.  
You cannot complete the full process to enable and use AWS CMEK without the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role. Other Management API key roles can only access some AWS CMEK features. For permission details for specific CMEK features, see the [Management API Reference](../management-api-reference/index.md).
* You have:

  * A symmetric encryption key in AWS KMS that’s in the same region as your cluster.
  * The unique Capella AWS account ID that’s associated with your organization. Get this account ID by making a [GET - Get Cloud Accounts](../management-api-reference/index.md#tag/CMEK/operation/getCloudAccounts) call to the Couchbase Capella Management API.  
  Use this account ID when adding CMEK to other AWS clusters in your organization.
  * A key policy with the following permissions:

    * [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API%5FDescribeKey.html)
    * [GenerateDataKeyWithoutPlainText](https://docs.aws.amazon.com/kms/latest/APIReference/API%5FGenerateDataKeyWithoutPlaintext.html)
    * [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API%5FDecrypt.html)
    * [ReEncrypt\*](https://docs.aws.amazon.com/kms/latest/APIReference/API%5FReEncrypt.html)
    * [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API%5FCreateGrant.html) with the `kms:GrantIsForAWSResource` condition set to the Capella AWS account ID associated with your organization.
    * The principal set to the Capella AWS account ID that’s associated with your organization.  
      Example  
      ```json  
      {  
                  "Sid": "Allow use of the key",  
                  "Effect": "Allow",  
                  "Principal": {  
                      "AWS": "arn:aws:iam::<capella-account-id>:root"  
                  },  
                  "Action": [  
                      "kms:DescribeKey",  
                      "kms:GenerateDataKeyWithoutPlainText",  
                      "kms:Decrypt",  
                      "kms:ReEncrypt*"  
                  ],  
                  "Resource": "*"  
              },  
              {  
                  "Sid": "Allow attachment of persistent resources",  
                  "Effect": "Allow",  
                  "Principal": {  
                      "AWS": "arn:aws:iam::<capella-account-id>:root"  
                  },  
                  "Action": "kms:CreateGrant",  
                  "Resource": "*",  
                  "Condition": {  
                      "Bool": {  
                          "kms:GrantIsForAWSResource": "true"  
                      }  
                  }  
              }  
      ```  
      > [!TIP]  
      > For more information about cross-account KMS encryption key access, see [Creating KMS keys that other accounts can use](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html#cross-account-console).
  * The Amazon Resource Name (ARN) of your KMS encryption key.

* You have a [Management API key](../management-api-guide/management-api-start.md#generate-management-api-keys) with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role.  
You cannot complete the full process to enable and use GCP CMEK without the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role. Other Management API key roles can only access some GCP CMEK features. For permission details for specific CMEK features, see the [Management API Reference](../management-api-reference/index.md).
* You have:

  * A symmetric encryption key in GCP KMS.
  * The Key Version Resource ID of your GCP KMS encryption key.
  * The unique Capella Google service account ID that’s associated with your organization. Get this account ID by making a [GET - Get Cloud Accounts](../management-api-reference/index.md#tag/CMEK/operation/getCloudAccounts) call to the Couchbase Capella Management API.  
  Use this service account ID when adding CMEK to other GCP clusters in your organization.
  * A service account on the key with the following permissions:

    * [Cloud KMS CryptoKey Encrypter/Decrypter](https://cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter)
    * The principal set to the Capella Google service account ID that’s associated with your organization.  
      Add the principal to your key in the following format:  
      rc-cluster-admin@<gcp-capella-project>.iam.gserviceaccount.com  
      Replace `<gcp-capella-project>` with the value of `"gcp-capella-project"` from the [GET - Get Cloud Accounts](../management-api-reference/index.md#tag/CMEK/operation/getCloudAccounts) Management API call.

* You have a [Management API key](../management-api-guide/management-api-start.md#generate-management-api-keys) with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role.  
You cannot complete the full process to enable and use Azure CMEK in your organization without the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role. Other Management API key roles can only access some organization-level Azure CMEK features. For permission details for specific CMEK features, see the [Management API Reference](../management-api-reference/index.md).
* You have:

  * A Key Vault created in the same Azure region as your Azure cluster. For more information about how to create a Key Vault, see [the Azure documentation](https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal#create-a-vault).
  * A symmetric RSA encryption key in your Azure Key Vault. The key must be 2048-bit, 3072-bit, or 4096-bit.  
  For more information about how to create a key in Azure Key Vault, see [the Azure documentation](https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-configure-new-account?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal#add-a-key).
  * Your **Key Identifier** URI, which you can view when you view details for a key on the Azure portal.

* You have a [Management API key](../management-api-guide/management-api-start.md#generate-management-api-keys) with 1 of the following roles:

  * [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner)
  * [Project Owner](../projects/project-roles.md#project-owner-role)
  * [Project/Cluster Manager](../projects/project-roles.md#project-cluster-manager-role)
* You have:

  * A Key Vault created in the same Azure region as your Azure cluster. For more information about how to create a Key Vault, see [the Azure documentation](https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal#create-a-vault).
  * A symmetric RSA encryption key in your Azure Key Vault. The key must be 2048-bit, 3072-bit, or 4096-bit.  
  For more information about how to create a key in Azure Key Vault, see [the Azure documentation](https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-configure-new-account?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal#add-a-key).
  * Your **Key Identifier** URI, which you can view when you view details for a key on the Azure portal.

### [](#enable-cmek)Enable Customer-Managed Encryption Keys on Capella

To use CMEK on Capella, you need to enable customer-managed keys for your specific cloud service provider by making a call to the [PUT - Enable CMEK for Cloud Services Provider](../management-api-reference/index.md#tag/CMEK/operation/enableCMEK) or [PUT - Enable Azure CMEK For Project](../management-api-reference/index.md#tag/CMEK/operation/enableCMEKAzureProject) endpoint.

> [!NOTE]
> If have not yet deployed a cluster with AWS or GCP in your organization, and want to use customer managed-encryption keys for a new cluster, you need to enable customer managed-encryption keys for your cloud service provider, first.
> 
> If you have already deployed a cluster with AWS or GCP, you do not need to enable CMEK for that cloud service provider.
> 
> You must always enable customer-managed keys if you want to use a customer-managed key for Azure clusters.

Using CMEK on Azure requires additional configuration after enabling customer-managed keys. You must also choose whether you want to enable CMEK and use keys at the project level or the organization level. You can choose to use both.

Enabling Azure CMEK at the organization level does not automatically enable Azure CMEK in your projects. If you want to separate your organization keys from project keys, or your project keys from other projects, you must enable Azure CMEK in each project.

Enabling Azure CMEK in a project does not enable Azure CMEK for an entire organization.

* AWS
* GCP
* Azure (Organization)
* Azure (Project)

* `$ORGID` is the organization ID.
* `$TOKEN` is the API key token.  
HTTP Request  
```sh  
curl --request POST \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/cmek/providers" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
    "cloudProvider": "aws"  
  }'  
```

* `$ORGID` is the organization ID.
* `$TOKEN` is the API key token.  
HTTP Request  
```sh  
curl --request POST \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/cmek/providers" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
    "cloudProvider": "gcp"  
  }'  
```

To use CMEK on Azure, you need to get and configure Capella’s Azure CMEK application in your Azure tenant:

1. Enable CMEK for your organization:

  * `$ORGID` is the organization ID.
  * `$TOKEN` is the API key token.  
  HTTP Request  
  ```sh  
  curl --request PUT \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/cmek/providers" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
      "cloudProvider": "azure"  
    }'  
  ```
2. Get your Azure CMEK application ID by making a [GET - Get Azure Application ID](../management-api-reference/index.md#tag/CMEK/operation/getAzureApplicationID) call to the Couchbase Capella Management API:

  * `$ORGID` is the organization ID.
  * `$TOKEN` is the API key token.  
  HTTP Request  
  ```sh  
  curl --request GET \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/cmekAzureApplication" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \  
  ```  
  HTTP Response  
  ```sh  
  {  
      "id": "$AZURE_APP_ID"  
  }  
  ```
3. Create a service principal in your Azure tenant by running the following command in the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-lts), replacing `$AZURE_APP_ID` with the response from the previous API call:  
```console  
az ad sp create --id $AZURE_APP_ID  
```
4. Do 1 of the following:

  1. If you’re using Azure Role-Based Access Control for your keys, assign the [Key Vault Crypto Service Encryption User](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide?tabs=azure-portal#azure-built-in-roles-for-key-vault-data-plane-operations) role to this application ID as a service principal in your Key Vault’s Access Control (IAM).  
  For more information about how to assign roles in Azure, see [the Azure documentation](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).
  2. If you’re using a Vault access policy, assign the following **Key Permissions** in your access policy and assign them to the service principal:

    * **Key Management Operations > Get**
    * **Cryptographic Operations > Unwrap Key**
    * **Cryptographic Operations > Wrap Key**  
      For more information about how to create a Key Vault access policy, see [the Azure documentation](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal).

To use CMEK on Azure, you need to get and configure Capella’s Azure CMEK application in your Azure tenant, for each project where you want to use CMEK:

1. Enable CMEK for your project:

  * `$ORGID` is the organization ID.
  * `$PROJID` is the project ID where you want to enable Azure CMEK.
  * `$TOKEN` is the API key token.  
  HTTP Request  
  ```sh  
  curl --request PUT \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/projects/$PROJID/cmek/providers" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
      "cloudProvider": "azure"  
    }'  
  ```
2. Get your Azure CMEK application ID by making a [GET - Get Azure Application ID For Project](../management-api-reference/index.md#tag/CMEK/operation/getAzureApplicationIDForProject) call to the Couchbase Capella Management API:

  * `$ORGID` is the organization ID.
  * `$PROJID` is the project ID where you enabled Azure CMEK.
  * `$TOKEN` is the API key token.  
  HTTP Request  
  ```sh  
  curl --request GET \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/projects/$PROJID/cmekAzureApplication" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \  
  ```  
  HTTP Response  
  ```sh  
  {  
      "id": "$AZURE_APP_ID"  
  }  
  ```
3. Create a service principal in your Azure tenant by running the following command in the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-lts), replacing `$AZURE_APP_ID` with the response from the previous API call:  
```console  
az ad sp create --id $AZURE_APP_ID  
```
4. Do 1 of the following:

  1. If you’re using Azure Role-Based Access Control for your keys, assign the [Key Vault Crypto Service Encryption User](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide?tabs=azure-portal#azure-built-in-roles-for-key-vault-data-plane-operations) role to this application ID as a service principal in your Key Vault’s Access Control (IAM).  
  For more information about how to assign roles in Azure, see [the Azure documentation](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).
  2. If you’re using a Vault access policy, assign the following **Key Permissions** in your access policy and assign them to the service principal:

    * **Key Management Operations > Get**
    * **Cryptographic Operations > Unwrap Key**
    * **Cryptographic Operations > Wrap Key**  
      For more information about how to create a Key Vault access policy, see [the Azure documentation](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal).
5. (Optional) Repeat the process for any other projects where you want to use Azure CMEK.

### [](#add-cmek)Add a Customer-Managed Encryption Key

To add a customer-managed encryption key, make a [POST - Create Key Metadata](../management-api-reference/index.md#tag/CMEK/operation/postCMEKMetadata) or [POST - Create Azure Key Metadata For Project](../management-api-reference/index.md#tag/CMEK/operation/postCMEKAzureMetadataForProject) call to the Capella Management API. For example:

* AWS
* GCP
* Azure (Organization)
* Azure (Project)

* `$ORGID` is the organization ID.
* `$TOKEN` is the API key token.
* `$ARN` is the Amazon Resource Name (ARN) of the KMS encryption key.
* `$CMEKID` is the Capella ID of the customer-managed encryption key.  
HTTP Request  
```sh  
curl --request POST \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/cmek" \
  --header "Authorization: Bearer $apiKeySecret" \
  --header 'Content-Type: application/json' \
  --data '{  
  "name": "Key name",  
  "description": "Description of the key",  
  "config": {  
	  "arn": "$ARN"  
	  }  
  }'  
```  
HTTP Response  
```sh  
{  
    "id": "$cmekId"  
}  
```

* `$ORGID` is the organization ID.
* `$TOKEN` is the API key token.
* `$RESOURCE_NAME` is the Key Version Resource ID of your GCP KMS encryption key.
* `$CMEKID` is the Capella ID of the customer-managed encryption key.  
HTTP Request  
```sh  
curl --request POST \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/cmek" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
  "name": "Key name",  
  "description": "Description of the key",  
  "config": {  
	  "resourceName": "$RESOURCE_NAME"  
	  }  
  }'  
```  
HTTP Response  
```sh  
{  
    "id": "$CMEKID"  
}  
```

If you [enabled Azure CMEK](#enable-cmek) at the organization level, use the following endpoint and API call, where:

* `$ORGID` is the organization ID.
* `$TOKEN` is the API key token.
* `$KEY_IDENTIFIER_URI` is your **Key Identifier** URI, which you can view by clicking your key name in your key vault on the Azure portal. Your URI must include your key name and key version.
* `$REGION` is the region where your Azure cluster and Key Vault are deployed.
* `$CMEKID` is the Capella ID of the customer-managed encryption key.  
HTTP Request  
```sh  
curl --request POST \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/cmek" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
  "name": "Key name",  
  "description": "Description of the key",  
  "config": {  
	  "keyLocation": "$KEY_IDENTIFIER_URI",  
    "region": "$REGION"  
	  }  
  }'  
```  
HTTP Response  
```sh  
{  
    "id": "$CMEKID"  
}  
```

If you [enabled Azure CMEK](#enable-cmek) at the project level, use the following endpoint and API call, where:

* `$ORGID` is the organization ID.
* `$PROJID` is the project ID where you enabled Azure CMEK and want to create a new key.
* `$TOKEN` is the API key token.
* `$KEY_IDENTIFIER_URI` is your **Key Identifier** URI, which you can view by clicking your key name in your key vault on the Azure portal. Your URI must include your key name and key version.
* `$REGION` is the region where your Azure cluster and Key Vault are deployed.
* `$CMEKID` is the Capella ID of the customer-managed encryption key.  
HTTP Request  
```sh  
curl --request POST \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/projects/$PROJID/cmek" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
  "name": "Key name",  
  "description": "Description of the key",  
  "config": {  
	  "keyLocation": "$KEY_IDENTIFIER_URI",  
    "region": "$REGION"  
	  }  
  }'  
```  
HTTP Response  
```sh  
{  
    "id": "$CMEKID"  
}  
```

### [](#create-cluster)Create a Cluster Using a Customer-Managed Encryption Key

After adding a customer-managed encryption key, you can use this key when creating new clusters with the Management API. Do this by adding the `cmekId` field with the Capella ID of the customer-managed encryption key to the payload when creating a cluster.

For more information, see [POST - Create Cluster](../management-api-reference/index.md#tag/Clusters/operation/postCluster).

### [](#apply-to-cluster)Apply a Customer-Managed Encryption Key to an Existing Cluster

To apply a customer-managed encryption key to an existing cluster, make a [POST - Associate Key with Cluster](../management-api-reference/index.md#tag/CMEK/operation/AssociateCMEK) call to the Capella Management API. This call needs:

* Your organization ID.
* The ID of the project where you created your cluster.
* The ID of the cluster you want to apply the encryption to.
* The CMEK ID—​the Capella ID of the customer-managed encryption key you’re using.

> [!TIP]
> The CMEK ID is in the response when you [add a new key](#add-cmek), and you can retrieve it by making a [GET - List Key Metadata](../management-api-reference/index.md#tag/CMEK/operation/getKeyMetadataList) or [GET - List Azure Key Metadata for Project](../management-api-reference/index.md#tag/CMEK/operation/getAzureKeyMetadataListForProject) call to the Capella Management API.

When the POST - Associate Key with Cluster call is successful, the cluster [rebalances](../clusters/scale-database.md#rebalance) to encrypt the existing data with the customer-provided key. Rebalancing does not cause any downtime.

You can confirm that your cluster is using the encryption key by making a [GET - Get Cluster](../management-api-reference/index.md#tag/Clusters/operation/getCluster) call and finding `cmekId` in the response.

## [](#key-rotation)Key Rotation

> [!WARNING]
> Do not use key rotation in AWS or GCP. KMS encryption key expiry is not supported through AWS or GCP. Only rotate keys out of Capella and remove them from your AWS or GCP key management provider once your cluster has a new KMS encryption key. If a customer-managed encryption key becomes unavailable, the related cluster experiences availability issues and data loss.
> 
> For clusters on Azure, you can do an in-place rotation of your key in Azure Key Vault, instead of rotating your key through Capella. See [Update Your Key Version in Azure Key Vault](#azure-update-key).

Capella cannot rotate customer-managed encryption keys. You must do this using the Capella Management API.

To rotate your customer-managed encryption keys:

1. Create a new KMS encryption key in your cloud service provider.
2. Do 1 of the following:

  1. For AWS, GCP, and organization-level Azure, make a [PUT - Rotate Key](../management-api-reference/index.md#tag/CMEK/operation/rotateCMEKKey) call to the Capella Management API with the resource name of your new KMS encryption key.
  2. For project-level Azure, make a [PUT - Rotate Azure Key For Project](../management-api-reference/index.md#tag/CMEK/operation/rotateAzureKeyMetadataForProject) call to the Capella Management API with the resource name of your new KMS encryption key.  
  After associating a new key with your cluster, Capella rebalances all nodes in that cluster. Rebalancing does not cause any downtime. Only remove the old key from your key management provider once your cluster is using the new KMS encryption key.

For example, to rotate your customer-managed encryption key:

* AWS
* GCP
* Azure (Organization)
* Azure (Project)

* `$ORGID` is the organization ID.
* `$CMEKID` is the Capella ID of the customer-managed encryption key you want to rotate.
* `$TOKEN` is the API key token.
* `$ARN` is the Amazon Resource Name (ARN) of the KMS encryption key.  
HTTP Request  
```sh  
curl --request PUT \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/cmek/$CMEKID" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
  "config": {  
	  "arn": "$ARN"  
	  }  
  }'  
```

* `$ORGID` is the organization ID.
* `$CMEKID` is the Capella ID of the customer-managed encryption key you want to rotate.
* `$TOKEN` is the API key token.
* `$RESOURCE_NAME` is the Key Version Resource ID of your GCP KMS encryption key.  
HTTP Request  
```sh  
curl --request PUT \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/cmek/$CMEKID" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
  "config": {  
	  "resourceName": "$RESOURCE_NAME"  
	  }  
  }'  
```

> [!NOTE]
> You can do an in-place rotation of your key in Azure Key Vault, instead of rotating your key through Capella. See [Update Your Key Version in Azure Key Vault](#azure-update-key).

* `$ORGID` is the organization ID.
* `$CMEKID` is the Capella ID of the customer-managed encryption key you want to rotate.
* `$TOKEN` is the API key token.
* `$KEY_IDENTIFIER_URI` is your **Key Identifier** URI, which you can view by clicking your key name in your key vault on the Azure portal. Your URI must include your key name and key version.
* `$REGION` is the region where your Azure cluster and Key Vault are deployed.  
HTTP Request  
```sh  
curl --request PUT \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/cmek/$CMEKID" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
  "config": {  
	  "keyLocation": "$KEY_IDENTIFIER_URI",  
    "region": "$REGION"  
	  }  
  }'  
```

> [!NOTE]
> You can do an in-place rotation of your key in Azure Key Vault, instead of rotating your key through Capella. See [Update Your Key Version in Azure Key Vault](#azure-update-key).

* `$ORGID` is the organization ID.
* `$PROJID` is the project ID.
* `$CMEKID` is the Capella ID of the customer-managed encryption key you want to rotate.
* `$TOKEN` is the API key token.
* `$KEY_IDENTIFIER_URI` is your **Key Identifier** URI, which you can view by clicking your key name in your key vault on the Azure portal. Your URI must include your key name and key version.
* `$REGION` is the region where your Azure cluster and Key Vault are deployed.  
HTTP Request  
```sh  
curl --request PUT \
  --url "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/projects/$PROJID/cmek/$CMEKID" \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{  
  "config": {  
	  "keyLocation": "$KEY_IDENTIFIER_URI",  
    "region": "$REGION"  
	  }  
  }'  
```

You can rotate customer-managed encryption keys once every 30 days. Contact Couchbase Support if you need to rotate keys earlier.

### [](#azure-update-key)Update Your Key Version in Azure Key Vault

If you’re using CMEK on Azure clusters, you can do an in-place rotation of your key in Azure Key Vault and generate a new version of your key. Capella will automatically handle the new key version.

To manually update the key version for your Azure clusters:

1. Log in to the [Azure Portal](https://portal.azure.com).
2. Go to **Key Vault**.
3. In your list of keys, click the key you want to update to a new version.
4. Click **New Version**.

Azure Key Vault generates a new version of your selected key. Capella starts using the new version of your key within 1 hour.

For more information about how to automatically configure key version updates in your Key Vault, see [the Microsoft Azure documentation](https://learn.microsoft.com/en-us/azure/key-vault/keys/how-to-configure-key-rotation).

## [](#see-also)See Also

* [Security Best Practices](security.md)
* [Management API Reference](../management-api-reference/index.md)