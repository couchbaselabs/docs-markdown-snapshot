[View original HTML](/cloud/billing/manage-billing.html)

> Manage and audit billing information for your organization and clusters. 

|  | If you do not have a Couchbase Capella account, see [Create an Account and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------- |

You can [view your billing and usage information](#access-billing) for Couchbase Capella from your organization’s **Billing** tab.

To upgrade from a free tier operational plan to a paid Support Plan, see [Upgrade Your Account](upgrade-account.md).

To change the Support Plan for your operational cluster, see [Change a Cluster’s Plan and Support Timezone](change-support-plan.md).

## [](#prerequisites)Prerequisites

To manage billing information in your organization, you must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role.

## [](#billing-contact)Update Your Billing Contact Information

If you use Couchbase Capella Credits, Couchbase sends invoices and other billing-related notifications to your organization’s billing contact. The billing contact is different from a user with the [Organization Owner](../organizations/manage-organizations.md) role.

To update your billing contact information, contact [Couchbase Sales](https://info.couchbase.com/Capella-Contact.html).

|  | If you use a credit card to pay for your Capella usage, Couchbase sends invoices and billing notifications to the [Organization Owner](../organizations/manage-organizations.md) that added that credit card to your organization. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#update-default-cc)Update Your Default Credit Card

You can update your default credit card at any time to change which card Couchbase bills for your organization’s usage. For more information about how Capella manages billing with credit cards, see [Credit Card Payments](billing.md#credit-cards).

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Billing** **Saved Cards**.
3. On any saved credit card, click **More Options (⋮)** **Set as Default**.
4. Confirm that you want to change your default credit card.
5. Click **Change Default Card**.

## [](#edit-saved-cc)Edit a Saved Credit Card

You can edit the details for a saved credit card, such as the expiration date or billing address, at any time.

You can add up to 5 saved credit cards to your organization. Only the card set as your default credit card will be billed for your Capella usage.

To update the details for a credit card saved in your organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Billing** **Saved Cards**.
3. On any saved credit card, click **More Options (⋮)** **Edit**.
4. Edit the details for your saved card.
5. (Optional) To set the card as your default credit card, click **Save as your default credit card**.
6. Click **Save**.

## [](#add-saved-cc)Add a New Saved Credit Card

You can add up to 5 saved credit cards to your organization. If you want to add more than 5 saved credit cards, you have to [delete a saved credit card](#delete-saved-cc), first.

Only the card set as your default credit card will be billed for your Capella usage. For more information about how Capella manages billing with credit cards, see [Credit Card Payments](billing.md#credit-cards).

To add another saved credit card to your organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Billing** **Saved Cards**.
3. Click **Add New Card**.
4. Enter the required details for your new credit card.
5. (Optional) To set the card as your default credit card, click **Save as your default credit card**.
6. Click **Add Card**.

## [](#delete-saved-cc)Delete a Saved Credit Card

You can delete a saved credit card to remove it from your organization.

If you want to delete your default credit card, you must have another credit card that you can use as the default saved to your account.

If you delete a credit card but still have outstanding usage charges on your account, Couchbase keeps your credit card information until the next billing cycle completes to process your final payment.

To delete a saved credit card from your organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Billing** **Saved Cards**.
3. On any saved credit card, click **More Options (⋮)** **Delete**.
4. Confirm that you want to delete your saved credit card.  
If you’re deleting your default credit card, you must select a new default credit card.
5. Click **Delete Credit Card** or **Delete Default Card**.

## [](#see-also)See Also

* [About Billing Alerts](about-billing-alerts.md)
* [Manage Billing Alerts](manage-billing-alerts.md)
* [Manage Your Billing](billing.md)
* [View Capella Usage and Invoices](usage-invoices.md)
* [Upgrade Your Account](upgrade-account.md)