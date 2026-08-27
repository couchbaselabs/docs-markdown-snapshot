---
title: Add Security with Channels
description: Channels and their part in data routing and access control for
  secure cloud-to-edge enterprise data synchronization.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/security/channels.adoc
  xref: xref:app-services::security/channels.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/security/channels.html)

# Add Security with Channels

> Channels and their part in data routing and access control for secure cloud-to-edge enterprise data synchronization. 

## [](#about-channels)About Channels

Channels allow you to share a cluster's documents across a large user base while retaining effective access control. They serve as a security conduit between the document and a user.

![Access Control using Channels](../_images/channels/channels-example-all.png) 

Figure 1\. Channels in Access Control

Conceptually, the channel can be considered as a tag associated with a document. Channels are assigned to documents depending on the configuration of the Access Control Function. Every document processed by the App Service can be assigned to one or multiple channels. Documents can also be assigned to no channels at all.

Channels can be applied to a `role` or a `user`:

* Role - When applied to a role, every user with said role will have access to documents within the channel.
* User - When applied to a user, only the individual user account with have access to documents within the channel.

You can associate a channel with a role or a user using any of these methods:

1. The [Admin REST API](../references/rest%5Fapi%5Fadmin.md).
2. The UI via the [Create App User page](create-user.md).
3. The [Access Control and Data Validation Function](../app-endpoints/access-control-data-validation.md).

> [!IMPORTANT]
> Channels are configured on a collection level.

## [](#overview)Overview

Every document in the cluster is assigned a list of channels it is distributed to. Every user (or role) is granted access to a list of channels. This dual-purpose is reflected in the way you use channels:

* By granting a user access to a channel, you are imposing access control.
* By assigning a document to a channel you are imposing document routing.

You typically will use channels to:

* Control who can access what
* Partition your dataset
* Enable users to access just the documents they need.
* Minimize the amount of data synced to mobile devices.

An App Service supports two types of channel:

**Admin Channels**

Admin channels are assigned statically. Admin channels can be set up through the Capella UI from the App Endpoint **Security** **App Users** **Create App User** page:

![Creating a channel from the user screen](../_images/user-management/create-app-user.png) 

Figure 2\. Creating a new channel for a user

Admin channels can also be created through the REST Admin API by calling `/{db}/_user/` endpoint, including a section in the JSON message to create the channels:

```json
{
    "name": "string",
    "password": "string",
    "admin_channels": [
        "string"
    ],
    "collection_access": {
        "scope1": {
            "collection1": {
                "admin_channels": [
                    "string"
                ]
            },
            "collection2": {
                "admin_channels": [
                    "string"
                ]
            }
        }
    },
    "email": "string",
    "disabled": false,
    "admin_roles": [
        "string"
    ]
}
```

> [!NOTE]
> Channels within the **admin\_channels** root level field are used as channels for the **\_default** collection.

The channels can also be updated through a call to update the user: `/{db}/_user/{username}`

**Other Channels**

Non-admin channels can be assigned dynamically through the App Endpoint **Security** **Access and Validation** function:

![Assigning document to channel with Javascript access control function](../_images/app-endpoint/access-control-data-validation.png) 

Figure 3\. Assigning document to channel through Access Control/JavaScript

These channels are created and allocated dynamically as documents are created and modified. Once a channel is allocated to an App User, it will be displayed under "Other Channels".

> [!IMPORTANT]
> Channels created by the Access Control Function and assigned to an App User or App Role cannot be edited or deleted by the Capella UI or Admin API. You will need to edit the Access Control Function and potentially run resync to apply changes.

## [](#see-also)See Also

* [Channels](../../sync-gateway/current/access-control/channels.md)
* [Create App Users](create-user.md)
* [Create App Roles](create-app-role.md)
* [Configure Access Control and Data Validation](../app-endpoints/access-control-data-validation.md)