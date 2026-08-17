---
title: Configure Your Free Tier App Services (Mobile sync)
description: Configure App Services to test out a mobile application with your
  free tier operational cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/get-started/configuring-app-services.adoc
  xref: xref:app-services::get-started/configuring-app-services.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/get-started/configuring-app-services.html)

# Configure Your Free Tier App Services (Mobile sync)

> Configure App Services to test out a mobile application with your free tier operational cluster. 

## [](#capella-app-services)Capella App Services

Capella App Services is a fully managed application backend designed for mobile and edge applications. You can use Capella App Services with an embedded [Couchbase Lite](../../couchbase-lite/current/index.md) database in your applications.

With Capella App Services, you can:

* Sync application data from linked collections in your App Endpoint on Capella and any mobile or edge device.
* Sync data directly between devices without a network connection to Capella App Services with [Peer-to-Peer](../../couchbase-lite/current/android/p2psync-websocket.md).
* Authenticate and manage mobile and edge users through App Services Endpoints.

## [](#prerequisites)Prerequisites

* You deployed a Couchbase Capella free tier operational cluster. For more information, see [Deploy Your Free Tier Operational Cluster](../../cloud/get-started/create-account.md#getting-started).
* Your free tier operational cluster has the `travel-sample` bucket. For more information, see [Import Data with the Capella UI](../../cloud/clusters/data-service/import-data-documents.md).
* You deployed your free tier App Services. For more information, see [Deploy Capella Free Tier App Services](../../cloud/get-started/create-account.md#app-services).
* You have a REST Client, such as [Postman](https://www.postman.com/) or [HTTPie](https://httpie.io/) installed and configured.

## [](#create-app-endpoint)Create an App Endpoint for Your Free Tier App Service

To create an App Endpoint:

1. Go to **App Services** and select the App Service you want to create an endpoint for.
2. Go to **App Endpoints** and click **Create App Endpoint**.
3. In the **App Endpoint Name** field, enter **travel-sample-appservice**.
4. In the **Linked Bucket** list, select **travel-sample**.
5. In the **Scope** list, select **inventory**.
6. Go to the **Linked Collections** table and link the **airline** collection.
7. Click **Create App Endpoint**.

If you link a large number of collections at one time, an initializing state occurs. During this phase, you can update general configuration, link, or unlink more collections, or change Auth Providers or the Access Control Function. After the linking of collections completes, the App Endpoint's status shows as **Offline**. You can resume the endpoint by selecting the desired endpoint from the **App Endpoints** menu and clicking the **Resume App Endpoint** button in App Endpoint settings.

## [](#configure-app-access)Configure the App Endpoint with an Access Control Policy

To configure access control for your new App Endpoint:

1. Go to **App Services** and select an App Service.
2. Go to **App Endpoints** and select **travel-sample-appservice**.
3. Go to **Security** **Access and Validation**.
4. Click the **airline** collection.
5. In the text editor, replace the existing text with the following JavaScript code:  
```javascript  
function (doc, oldDoc, meta) {  
  if (doc.channels) {  
      // If channels list is specified in document, assign doc to the channels  
     channel(doc.channels);  
  }  
  else {  
    // assign to public channel (which is accessible to all users)  
    channel ("!")  
  }  
}  
```
6. Click **Save**.

## [](#create-app-role)Create an App Role for the App Endpoint

To add an App Role for the App Endpoint:

1. Go to **Security** **App Roles**.
2. Click **Create App Role**.
3. In the **App Role Name** field, enter `admin`.
4. In the **Admin Channels** field of the **airline** collection, enter an asterix (\*) and press Enter.
5. Click **Save**.

## [](#create-app-user)Create an App User for the App Endpoint

To create a user for the App Endpoint:

1. Go to **Security** **App Users**.
2. Click **Create App User**.
3. In the **Create App User** page, do the following:

  1. In the **App User name** field, enter a username for the new app user.
  2. In the **Password** field, enter a password for the new app user.

    1. (Optional) Click the **Configure Access Grants** list.
    2. (Optional) In the **Assigned App Roles** field, select `admin` from the list.
    3. (Optional) In the **Assign Channels** field, enter an asterix (\*) and press Enter.
  3. Click **Create App User**.

> [!NOTE]
> App Users can inherit their assigned channels directly from roles or be specifically assigned channels on a per user basis.

## [](#access-endpoint)Connect to the App Services

Follow these steps to connect to the App Services via Couchbase Lite, Public REST API, or Admin REST API:

* Public REST API
* Couchbase Lite
* Admin REST API

You can use a REST client to connect to the App Services Public REST API.

To retrieve a document from the `travel-sample` bucket through the App Services Public REST API:

1. Go to **Connect**.
2. Select **Connect via Public REST API**.
3. Next to the **Public Endpoint** field, click **Copy**.
4. In your REST Client, create a GET request.
5. Paste the Public Connection URL and change `wss` to `https`.
6. Add `/airline_10` to the end of the URL. Your URL should look similar to `https://123456789.apps.capella.com:4984/travel-sample-appservice.inventory.airline/airline_10`.
7. Under the **Test: Fetch a Sample Document** section, enter the username and password for the [App User you created](#create-app-user).
8. Under **Keyspace**, select airline collection.
9. Send the GET request to receive the contents of the document `airline_10` as the response.

For more information about the Public REST API, see [Public REST API](../../sync-gateway/current/rest-api/rest-api.md).

Couchbase Lite is an embedded database. You can use it to embed data processing and storage in applications that run on mobile and IoT devices, allowing apps to locally store and access data without an Internet connection.

Couchbase Lite embedded apps can connect to App Endpoints and sync data with each other and the Couchbase Capella backend over a websockets-based data sync protocol.

To connect Couchbase Lite to your App Endpoint:

1. Go to **App Services** and select an App Service.
2. Go to **App Endpoints** and select **travel-sample-appservice**.
3. Go to **Connect**.
4. Select **Connect via Couchbase Lite**.
5. Next to the **Public Connection** field, click **Copy**.
6. Select **App Services Credentials** from the list to choose the credentials you want to use to connect to your Capella Cluster. To create App Services user credentials, go to [App User](#add-app-services-user).
7. Under Choose a Couchbase Lite SDK, select the SDK you're using or plan to use for your applications from the Language list.

  * [Swift (iOS, macOS)](../../couchbase-lite/current/swift/gs-install.md): Replace the `URLEndpoint` in the sample code with your App Endpoint Public Connection URL.
  * [Kotlin (Android)](../../couchbase-lite/current/android/gs-install.md): Replace the `URLEndpoint` in the sample code with your App Endpoint Public Connection URL.
  * [Java (Android)](../../couchbase-lite/current/android/gs-install.md): Replace the `URLEndpoint` in the sample code with your App Endpoint Public Connection URL.
  * [.Net (Desktop, Xamarin)](../../couchbase-lite/current/csharp/gs-install.md): Replace the `URLEndpoint` in the sample code with your App Endpoint Public Connection URL.
  * [Java (Desktop)](../../couchbase-lite/current/java/gs-install.md): Replace the `URLEndpoint` in the sample code with your App Endpoint Public Connection URL.
  * [C (Desktop, Mobile, Embedded)](../../couchbase-lite/current/c/gs-install.md): Replace the `CBLEndpoint_CreateWithURL` in the sample code with your App Endpoint Public Connection URL.

You can use a REST client to connect to the App Services Admin REST API:

1. Go to **App Services** and select an App Service.
2. Go to **App Endpoints** and click **travel-sample-appservice**.
3. Go to **Connect**.
4. Next to the **Admin Connection URL** field, click **Copy**.
5. In your REST client, create a GET request.
6. Paste the Admin Connection URL.
7. Add `/_user/` to the end of the URL. Your URL should look similar to `https://123456789.apps.capella.com:4985/travel-sample-appservice/_user/`.
8. Select **Basic Authentication**.
9. Enter the [admin credential you created](#allowed-ip-admin-cred).
10. Send the GET request to receive the [App User you created](#create-app-user) earlier.

### [](#add-app-services-user)Add an App Services User

To add a new App Services User with the App Services Admin REST API:

1. In your REST client, create a POST request.
2. Paste the Admin Connection URL.
3. Add `/_user/` to the end of the URL. Your URL should look similar to `https://123456789.apps.capella.com:4985/travel-sample-appservice/_user/`.
4. Select **Basic Authentication**.
5. Enter the [admin credential you created](#allowed-ip-admin-cred).
6. In the request body, add the following JSON code:  
```json  
{  
  "name": "demo2@example.com",  
  "password": "password",  
  "admin_channels": [  
    "string"  
  ],  
  "disabled": false  
}  
```
7. Send the POST request.
8. Go to **App Services** and select an App Service.
9. Go to **App Endpoints** and click **travel-sample-appservice**.
10. Go to **Security** **App Users** and fill in the **App Username** and **App User Password**.
11. Click **Create App User**.

For more information about the Admin REST API, see [Admin REST API](../../sync-gateway/current/rest-api/rest-api-admin.md).

### [](#admin-api)Administer App Users with the App Services REST API (Optional)

You can use the App Services Admin REST API to add new users and return a list of users.

To use the App Services Admin REST API:

* [Add an allowed IP address and create an admin credential](#allowed-ip-admin-cred)
* [Add an App Services user](#add-app-services-user)
* [Connect to the endpoint](#access-endpoint)

### [](#allowed-ip-admin-cred)Add an Allowed IP and Create an Admin Credential

To add an allowed IP address and create an admin credential:

1. Go to **App Services** and select an App Service.
2. Go to **App Endpoints** and click **travel-sample-appservice**.
3. Go to **Connect**.
4. Select **Connect via Admin REST API**.
5. Under **Allowed IP Addresses**, click **Go to Allowed IP Addresses**.
6. Click **Add Allowed IP Address**.
7. In the **Add Allowed IP** page, click **Add Allowed IP Address**.
8. In the **Add Allowed IP Address** page, you can either:

  * Click **Add Current IP Address** to populate the **Allowed IP / CIDR Block** field with your IP address.
  * Click **Allow Access from Anywhere** to allow any IP address to connect to your cluster.
  * Enter an IP address or IP address range in CIDR notation in the **Allowed IP / CIDR Block** field.
9. Select a **time to retain** from the list.
10. Click **Add Allowed IP**.
11. Go to **App Endpoints** and click **travel-sample-appservice**.
12. Go to **Connect**.
13. Under **Connect for Admin REST**, click **Manage Admin Credentials**.
14. Click **Create Admin Credential**.
15. In the **Create Admin Credential** page, do the following:

  1. In the **Username** field, enter `admin`.
  2. In the **Password** field, enter a password for the admin credential.
  3. Toggle the checkmark under **App Endpoint** to **Apply to all current and future App Endpoints within this App Service**.
  4. Click **Create Admin Credential**.

> [!CAUTION]
> You cannot change the Username and Password after creating the admin credential.