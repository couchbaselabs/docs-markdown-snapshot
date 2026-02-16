[View original HTML](/app-services/app-endpoints/connect-apps-to-endpoint.html)

Couchbase provides Couchbase Lite: an embedded, NoSQL JSON-document Style database for your mobile apps.

You can use Couchbase Lite as a standalone embedded database within your mobile apps, or with Couchbase Capella’s App Endpoints to provide a complete cloud to edge synchronized solution. Couchbase Lite runs on the following platforms:

* [Swift (iOs, macOS)](../../couchbase-lite/current/swift/gs-install.md)
* [Kotlin (Android)](../../couchbase-lite/current/android/kotlin.md)
* [Java (Android](../../couchbase-lite/current/android/gs-install.md))
* [.Net (Desktop, Xamarin)](../../couchbase-lite/current/csharp/gs-install.md)
* [C (Desktop, Mobile, Embedded)](../../couchbase-lite/current/c/gs-install.md)
* [Java (Desktop)](../../couchbase-lite/current/java/gs-install.md)
* [Obj-C (iOS, macOS)](../../couchbase-lite/current/objc/gs-install.md)
* [Javascript](#couchbase-lite:javascript:quickstart.adoc)

## [](#setting-up-the-connection)Setting up the Connection

You must configure your App Endpoint before your mobile application can connect to it.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name or expand and select the organization where you want to work with App Services.
  2. Click your current project name or search for the project where you want to work with App Services.
2. Go to **App Services**.
3. Select your App Service from the list.
4. Go to **App Endpoint**.
5. Click **Create App Endpoint**.
6. From the App Services screen, select an App Service, and click the **App Endpoints** tab.  
In the **App Endpoints** page, select an App Service Endpoint.  
You can find the connection configuration screen within the **connect** tab of your App Endpoint.  
From here, you can configure the App Endpoint connection settings:  
Public Connection  
You create this setting when you create the App Endpoint. This is the address which your mobile application uses to connect to the endpoint.  
Public Certificate  
The public certificate is a trusted Certificate Authority (CA) signed certificate. You can copy or download the endpoint’s SSL public certificate to bundle into your mobile application.  
You can download your public certificate, but Couchbase recommends against pinning your certificate to your App. Pinning your certificate can increase maintenance overhead and downtime risks.

|  | Capella rotates the certificate yearly. If you have pinned the certificate, you’ll have to update your app to use the new certificate when the old one expires. If you have [email notifications turned on](../../cloud/clusters/monitoring/alerts.md#get-alerts-through-email), Capella sends you an email notification starting 1 month before the certficate expires. To update your app with the new certificate ahead of the scheduled expiration, contact Support. If however, you do not pin the certificate, your app continues to operate after certificate rotation with no downtime and no action required. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Endpoint for Admin Access to the database

To ensure your service is as secure as possible, the App Endpoint uses a separate URL for executing [REST API administration functions](../references/rest%5Fapi%5Fadmin.md).

Manage Credentials for user administration and metrics access

Set up credentials for accessing the endpoint’s administration and metrics functions.

1. Click the **Go to Admin Credentials for App Services →** link to view the `Manage Credentials` screen.
2. Fill in the **User Name** field

  1. Your username must be unique within the App Service.
3. Fill in the **Password** field according to the following criteria:

  1. A minimum of eight characters including one uppercase, one lowercase, a number and a special character.
4. Specify which App Endpoints the user with admin credentials has admin privileges over.

  1. You can select specific App Endpoints from the list menu or click to apply the admin credential to all current and future App Endpoints within the App Service.
5. Click **Create Admin Credential**:

Allowed IP Addresses

You must register any IP that requires a connection to the endpoint.

Click **Go to Allowed IP Addresses >**.

Click **\+ Add Allowed IP**.

You can fill in the allowed IP address, or click **Add Current IP Address** to fill in the IP address of the machine you’re using.

You can also press **Allow Access from Anywhere** to allow access to your endpoint from any location.

For example, you can add an expiry date to the entry to allow temporary access to the endpoint for testing.

## [](#syncing-data-to-a-client-application)Syncing Data to a Client Application

Once you have configured the App Service, your client application can start synchronizing data using calls to the Couchbase API.

In this example, first open the local database for syncing from the Capella App Service.

The client application uses the address of the endpoint to sync its local databases. The App Endpoint address can be found under the `Connect` tab of App Endpoint configuration (See [\[locate-app-endpoint-connection-tab\]](#locate-app-endpoint-connection-tab)).

```swift
let db = try! Database(name: "travel-sample")

guard let targetURL = URL(string: "wss://gaoca1lnIxwdumid.apps.endpoint.com:4984/test-endpoint")
else {
    fatalError("Invalid URL")
}
```

Now create a configuration linking the local database to the App Endpoint. Set the sync to run bidirectionally.

The authenticator takes the username and password set up when the App Endpoint’s user was created (See [Create App Users](../security/create-user.md)).

```swift
let targetEndpoint = URLEndpoint(url: targetURL)

var config = ReplicatorConfiguration(database: db, target: targetEndpoint)
config.replicatorType = .pushAndPull
config.continuous = false

config.authenticator = BasicAuthenticator(
    username: "test-user",
    password: "password")
```

Finally, start syncing.

```swift
let replicator = Replicator.init(config: config)
replicator.start()
```