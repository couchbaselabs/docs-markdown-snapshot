---
title: Adding Security
editUrl: https://github.com/couchbaselabs/mobile-training-todo/edit/tutorials/content/modules/todo-app/pages/develop/java/adding-security.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/tutorials/todo-app/develop/java/adding-security.html)

# Adding Security

In this lesson you’ll learn how to add security to your Couchbase Mobile application. You’ll implement authentication and define access control, data validation, and access grant policies.

## [](#user-authentication)User Authentication

### [](#install-sync-gateway)Install Sync Gateway

Users are created with a name/password on Sync Gateway which can then be used on the Couchbase Lite replicator to authenticate as a given user. You can create users by hardcoding the user’s name/password in the configuration file. Create a new file called **sync-gateway-config.json** with the following.

```json
{
  "log": ["HTTP", "Auth"],
  "databases": {
    "todo": {
      "server": "walrus:",
      "users": {
        "user1": {"password": "pass", "admin_channels": ["user1"]},
        "user2": {"password": "pass", "admin_channels": ["user2"]},
        "mod": {"password": "pass", "admin_roles": ["moderator"]},
        "admin": {"password": "pass", "admin_roles": ["admin"]}
      },
      "roles": {
        "moderator": {},
        "admin": {}
      }
    }
  }
}
```

#### [](#try-it-out)Try it out

1. [Download Sync Gateway](http://www.couchbase.com/nosql-databases/downloads#couchbase-mobile)
2. Unzip the file and locate the executable at **\~/Downloads/couchbase-sync-gateway/bin/sync\_gateway**.
3. Start it from the command-line with the config file.  
```bash  
$ /path/to/sync_gateway sync-gateway-config.json  
```  
```swift  
PS  'C:\Program Files (x86)\Couchbase\sync_gateway.exe' sync-gateway-config.json  
```

> [!NOTE]
> The Sync Gateway service might be running on Windows which will prevent this command from succeeding with the message 'FATAL: Failed to start HTTP server on 127.0.0.1:4985: listen tcp 127.0.0.1:4985: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.' To get around this, stop the 'Couchbase Sync Gateway' service in 'services.msc'. Two users are now visible at <http://localhost:4985/%5Fadmin/db/todo/users>.

### [](#replications-with-authentication)Replications with Authentication

With Sync Gateway users defined you can now enable authentication on the Couchbase Lite replicator. The code below creates two replications with authentication.

```swift
// This code can be found in AppDelegate.swift
// in the startReplication(withUsername:andPassword:) method
pusher = database.createPushReplication(kSyncGatewayUrl)
pusher.continuous = true
NotificationCenter.default.addObserver(self, selector: #selector(replicationProgress(notification:)),
    name: NSNotification.Name.cblReplicationChange, object: pusher)

puller = database.createPullReplication(kSyncGatewayUrl)
puller.continuous = true
NotificationCenter.default.addObserver(self, selector: #selector(replicationProgress(notification:)),
                                        name: NSNotification.Name.cblReplicationChange, object: puller)

if kLoginFlowEnabled {
    let authenticator = CBLAuthenticator.basicAuthenticator(withName: username, password: password!)
    pusher.authenticator = authenticator
    puller.authenticator = authenticator
}

pusher.start()
puller.start()
```

```c#
// This code can be found in CoreApp.cs
// in the StartReplication(string, string) method
var authenticator = default(IAuthenticator);
if(username != null  password != null) {
    authenticator = AuthenticatorFactory.CreateBasicAuthenticator(username, password);
}

var db = AppWideManager.GetDatabase(username);
var pusher = db.CreatePushReplication(SyncGatewayUrl);
pusher.Continuous = true;
pusher.Authenticator = authenticator;


var puller = db.CreatePullReplication(SyncGatewayUrl);
puller.Continuous = true;
puller.Authenticator = authenticator;

pusher.Start();
puller.Start();

_pusher = pusher;
_puller = puller;
```

```java
URL url = null;
try {
    url = new URL(mSyncGatewayUrl);
} catch (MalformedURLException e) {
    e.printStackTrace();
}

pusher = database.createPushReplication(url);
pusher.setContinuous(true);

puller = database.createPullReplication(url);
puller.setContinuous(true);

if (mLoginFlowEnabled) {
    Authenticator authenticator = AuthenticatorFactory.createBasicAuthenticator(username, password);
    pusher.setAuthenticator(authenticator);
    puller.setAuthenticator(authenticator);
}

pusher.start();
puller.start();
```

The `CBLAuthenticator` class has static methods for each authentication method supported by Couchbase Lite. Here, you’re passing the name/password to the `basicAuthenticatorWithName` method. The object returned by this method can be set on the replication’s `authenticator` property.

#### [](#try-it-out-2)Try it out

1. Set `kSyncEnabled` and `kLoginFlowEnabled` to `true` in **AppDelegate.swift**.  
```swift  
let kSyncEnabled = true  
let kLoginFlowEnabled = true  
```
2. Build and run.
3. Now login with the credentials saved in the config file previously (**user1/pass**) and create a new list. Open the Sync Gateway Admin UI at <http://localhost:4985/%5Fadmin/db/todo>, the list document is successfully replicated to Sync Gateway as an authenticated user.  
![image35](../../_images/image35.png)

1. Change `LoginEnabled = false` to `LoginEnabled = true` in the `CreateHint()` method in **CoreApp.cs**  
```c#  
var retVal = new CoreAppStartHint {  
    LoginEnabled = true, // Line to change is here  
    EncryptionEnabled = false,  
    SyncEnabled = false,  
    UsePrebuiltDB = false,  
    ConflictResolution = false,  
    Username = todo  
};  
return retVal;  
```
2. Build and run.
3. Now login with the credentials saved in the config file previously (**user1/pass**) and create a new list. Open the Sync Gateway Admin UI at <http://localhost:4985/%5Fadmin/db/todo>, the list document is successfully replicated to Sync Gateway as an authenticated user.

{% include experimental-label.html %}

center-image />

1. Set `mSyncEnabled` and `mLoginFlowEnabled` to `true` in **Application.java**.  
```java  
private Boolean mSyncEnabled = true;  
private Boolean mLoginFlowEnabled = true;  
```
2. Build and run.
3. Now login with the credentials saved in the config file previously (**user1/pass**) and create a new list. Open the Sync Gateway Admin UI at <http://localhost:4985/%5Fadmin/db/todo>, the list document is successfully replicated to Sync Gateway as an authenticated user.

{% include experimental-label.html %}

center-image />

> **Note:** You can remove the local database and check if the pull replication retrieves the documents now present on Sync Gateway. Using File Explorer, type `%LOCALAPPDATA%` into the location bar and press enter, then delete the database **user1.cblite2**. Then restart the app and you’ll notice that the Today list isn’t displayed. That is, the list document wasn’t replicated from Sync Gateway to Couchbase Lite. Indeed, the document is not routed to a channel that the user has access to. **Channel** and **access** are new terms so don’t worry, we’ll cover what they mean in the next section. 

> **Note:** You can remove the local database and check if the pull replication retrieves the documents now present on Sync Gateway. On macOS, use the [SimPholders](https://simpholders.com/) utility app to quickly find the data directory of the application and delete the database called **user1** on iOS, or you can use the adb shell to navigate to the application’s data folder and delete it on Android. Then restart the app and you’ll notice that the Today list isn’t displayed. That is, the list document wasn’t replicated from Sync Gateway to Couchbase Lite. Indeed, the document is not routed to a channel that the user has access to. **Channel** and **access** are new terms so don’t worry, we’ll cover what they mean in the next section. 

## [](#access-control)Access Control

In order to give different users access to different documents, you must write a sync function. The sync function lives in the configuration file of Sync Gateway. It’s a JavaScript function and every time a new document, revision or deletion is added to a database, the sync function is called and given a chance to examine the document.

You can use different API methods to route documents to channels, grant users access to channels and even assign roles to users. Access rules generally follow the order shown on the image below: write permissions, validation, routing, read permissions.

![image15](../../_images/image15.png) 

> [!TIP]
> Open the [Access Control](#swift/adding-security.adoc) lesson in a new tab, it will be useful throughout this section.

### [](#document-types)Document Types

The Sync Function takes two arguments:

* **doc:** The current revision being processed.
* **oldDoc:** The parent revisions if it’s an update operation and `null` if it’s a create operation.

Each document type will have different access control rules associated with it. So the first operation is to ensure the document has a type property. Additionally, once a document is created, its type cannot change. The code below implements those 2 validation rules.

```javascript
function(doc, oldDoc){
  /* Type validation */
  if (isCreate()) {
    // Don't allow creating a document without a type.
    validateNotEmpty(type, doc.type);
  } else if (isUpdate()) {
    // Don't allow changing the type of any document.
    validateReadOnly(type, doc.type, oldDoc.type);
  }

  if (getType() == "task-list") {
    /* Write access */
    /* Validation */
    /* Routing */
    /* Read Access */
  }

  function getType() {
    return (isDelete() ? oldDoc.type : doc.type);
  }

  function isCreate() {
    // Checking false for the Admin UI to work
    return ((oldDoc == false) || (oldDoc == null || oldDoc._deleted)  !isDelete());
  }

  function isUpdate() {
    return (!isCreate()  !isDelete());
  }

  function isDelete() {
    return (doc._deleted == true);
  }

  function validateNotEmpty(key, value) {
    if (!value) {
      throw({forbidden: key +  is not provided.});
    }
  }

  function validateReadOnly(name, value, oldValue) {
    if (value != oldValue) {
      throw({forbidden: name +  "is read-only."});
    }
  }

  // Checks whether the provided value starts with the specified prefix
  function hasPrefix(value, prefix) {
    if (value  prefix) {
      return value.substring(0, prefix.length) == prefix
    } else {
      return false
    }
  }
}
```

As shown above, you can define inner functions to encapsulate logic used throughout the sync function. This makes your code more readable and follows the DRY principle (Don’t Repeat Yourself).

#### [](#try-it-out-3)Try it out

1. Open the Sync menu on the Admin UI <http://localhost:4985/%5Fadmin/db/todo/sync>.
2. Copy the code snippet above in the Sync Function text area.
3. Click the **Deploy To Server** button. It will update Sync Gateway with the new config but it doesn’t persist the changes to the filesystem.
4. Add two documents through the REST API. One with the `type` property and the second document without it. Notice that the user credentials (**user1/pass**) are passed in the URL.  
```bash  
curl -vX POST 'http://user1:pass@localhost:4984/todo/_bulk_docs' \
      -H 'Content-Type: application/json' \
      -d '{"docs": [{"type": "task-list", "name": "Groceries"}, {"names": "Today"}]}'  
```  
The output should be the following:  
```bash  
[  
  {  
  	"id": "e498cad0380e30a86ed5572140c94831",  
  	"rev": "1-e4ac377fc9bd3345ddf5892b509c4d79" },  
  {error:forbidden,reason:type is not provided.,status:403}  
]  
```

> [!NOTE]
> The curl executable for Windows can be found [on this page](https://curl.haxx.se/download.html)The document without a type is rejected with an error message: type property missing.

### [](#write-permissions)Write Permissions

Once you know the type of a document, the next step is to check the write permissions.

The following code ensures the user creating the list document matches with the `owner` property or is a moderator.

```javascript
/* Write Access */
var owner = doc._deleted ? oldDoc.owner : doc.owner;
try {
  // Moderators can create/update lists for other users.
  requireRole(moderator);
} catch (e) {
  // Users can create/update lists for themselves.
  requireUser(owner);
}
```

When a document is deleted the user properties are removed and the `\_deleted: true` property is added as metadata. In this case, the sync function must retrieve the type from oldDoc. In the code above, the `getType` inner function encapsulates this logic.

Similarly, the owner field is taken from oldDoc if doc is a deletion revision. The `requireUser` and `requireRole` functions are functionalities built in Sync Gateway.

#### [](#try-it-out-4)Try it out

1. Open the Sync menu on the Admin UI <http://localhost:4985/%5Fadmin/db/todo/sync>.
2. Copy the changes above in the Sync Function text area to replace the `/* Write access */` block.
3. Click the **Deploy To Server** button. It will update Sync Gateway with the new config but it doesn’t persist the changes to the filesystem.
4. Add two documents through the REST API. The request is sent as a user (**user1/pass**). One document is a list for user1 and another is a list for user2.  
```bash  
curl -vX POST 'http://user1:pass@localhost:4984/todo/_bulk_docs' \
      -H 'Content-Type: application/json' \
      -d '{docs: [{type: task-list, owner: user1}, {type: task-list, owner: user2}]}'  
```  
The response should be the following:  
```bash  
[  
  {id:8339356c8bb6d8b32477e931ce04c5c9,rev:1-39539a8ec6ddd252d6aafe1f7e3efd9a},  
  {error:forbidden,reason:wrong user,status:403}  
]  
```  
The list with user2 as the owner is rejected.

### [](#validation)Validation

After write permissions, you must ensure the document has the expected schema. There are different types of validation such as checking for the presence of a field or enforcing read-only permission on parts of a document. The code below performs various schema validation operations.

```javascript
/* Validation */
if (!isDelete()) {
  // Validate required fields.
  validateNotEmpty(name, doc.name);
  validateNotEmpty(owner, doc.owner);

  if (isCreate()) {
    // Validate that the _id is prefixed by owner.
    if (!hasPrefix(doc._id, doc.owner + .)) {
        throw({forbidden: task-list id must be prefixed by list owner});
    }
  } else {
    // Don’t allow task-list ownership to be changed.
    validateReadOnly(owner, doc.owner, oldDoc.owner);
  }
}
```

`validateNotEmpty` and `validateReadOnly` are inner functions to encapsulate common validation operations.

#### [](#try-it-out-5)Try it out

1. Open the Sync menu on the Admin UI <http://localhost:4985/%5Fadmin/db/todo/sync>.
2. Copy the changes above in the Sync Function text area to replace the `/* Validation */` block.
3. Click the **Deploy To Server** button. It will update Sync Gateway with the new config but it doesn’t persist the changes to the filesystem.

**Challenge:** Persist documents using curl until it gets persisted and Sync Gateway returns a **201 Created** status code.

### [](#routing)Routing

Once you have determined that the schema is valid you can route the document to channels. A channel is a namespace for documents specifically designed for access control. The code below routes the document to its own list channel.

```javascript
/* Routing */
// Add doc to task-list's channel.
channel(task-list. + doc._id);
channel(moderators);
```

#### [](#try-it-out-6)Try it out

1. Open the Sync menu on the Admin UI <http://localhost:4985/%5Fadmin/db/todo/sync>.
2. Copy the changes above in the Sync Function text area to replace the `/* Routing */` block.
3. Click the **Live Preview Mode** button. This mode doesn’t restart Sync Gateway but will use the updated Sync Function for testing purposes. Click the **random** button to pick a document at random and run it through the sync function again. It re-calculates the routing to channels and access grants. This time, the owner (user1) has access to its own list’s channel.
4. Both documents are saved and mapped to the corresponding channels in the Admin UI.  
![image88](../../_images/image88.png)

### [](#read-access)Read Access

The last step in writing access control rules for a document type is to allow read access to channels. The following code grants the owner and users that are moderators access to the list’s channel.

```javascript
/* Read Access */
// Grant task-list owner access to the task-list, its tasks, and its users.
access(owner, task-list. + doc._id);
access(owner, task-list. + doc._id + .users);
access(role:moderator, task-list. + doc._id);
```

#### [](#try-it-out-7)Try it out

1. Open the Sync menu on the Admin UI <http://localhost:4985/%5Fadmin/db/todo/sync>.
2. Copy the changes above in the Sync Function text area to replace the `/* Read access */` block.
3. Click the **Live Preview Mode** button. This mode doesn’t restart Sync Gateway but will use the updated Sync Function for testing purposes. Click the **random** button to pick a document at random and run it through the sync function again. It re-calculates the routing to channels and access grants. This time, the owner (user1) has access to its own list’s channel.  
![image38](../../_images/image38.png)

## [](#conclusion)Conclusion

Well done! You’ve completed this lesson on adding authentication, writing a sync function and adding database encryption. Feel free to share your feedback, findings or ask any questions on the forums.