[View original HTML](/app-services/security/create-app-role.html)

> App roles are used to secure applications using App Services to transfer data between the mobile applications and the Capella service. 

App Roles are defined as part of the App Services setup for each application using the gateway. By assigning these roles to a user, the functionality/data accessible by that user can be restricted within the application.

## [](#app-roles)Concept

Roles are named collections of [Channels](channels.md), where channels are organised within a linked Collection to a given Scope within your App Endpoint. They enable the grouping together of [Users](create-user.md) with similar characteristics, which makes the management of large user populations easier.

Roles are granted access to channels. Any user assigned a role can access any channels (and documents within those channels) the role has been granted access to.

As an entity, roles comprise a name and a list of channels.

Any user associated with a role inherits the right to access any of the channels in the role’s list. This provides a convenient way to associate multiple channels with multiple users.

|  | Roles have a separate namespace from users, so it’s possible to have a user and a role with the same name. |
|  | ---------------------------------------------------------------------------------------------------------- |

## [](#procedure)Procedure

1. Select your App Endpoint
2. Select the **Security** tab.
3. From the menu on the left, select **App Roles**

Now, click **\+ CREATE APP ROLE** to access the role creation screen:

![creating the app role](../_images/user-management/app-role-sc.png) 

Figure 1\. Creating a user’s App Role

Fill in the name of the role. You can also fill in the name of the channel, and then press the Return key to add it to the list of channels. Any user with this role will be able to access documents that are included in one or more of the channels. Press **CREATE APP ROLE** when you’ve finished.

For more information on channels, see [Add Security with Channels](channels.md)

![Editing the app role](../_images/user-management/edit-role.png) 

Figure 2\. Editing a user’s App Role

You can perform the following actions in the Edit App Role page:

* You can assign additional Channels to the App Role.
* You can view non-admin channels assigned to the App Role per collection by the Access Control Function.
* You can also view admin channels assigned by the Access Control Function per collection under the **Channels assigned by access control and data validation function** section.

|  | Channels created by the Access Control Function and assigned to an App Role cannot be edited or deleted by the Capella UI or Admin API. You will need to edit the Access Control Function to apply any changes. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#see-also)See Also

* [Configure Access Control and Data Validation](../app-endpoints/access-control-data-validation.md)
* [Create App Endpoints](../app-endpoints/creating-an-app-endpoint.md)
* [Advanced Settings for App Endpoints](../app-endpoints/advanced-settings.md)