---
title: Create a Database
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/mobile-training-todo/edit/tutorials/content/modules/todo-app/pages/develop/swift/create-database.adoc
  xref: xref:tutorials:todo-app:develop/swift/create-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/todo-app/develop/swift/create-database.html)

# Create a Database

In this lesson you'll be introduced to Couchbase Lite, our embedded NoSQL database. You'll learn how to create a new embedded database and optionally use databases pre-packaged in your application.

## [](#requirements)Requirements

* Xcode 8 (Swift 3)

## [](#getting-started)Getting Started

Download the [Xcode project](../../%5Fattachments/project.zip).

Unzip the file and install Couchbase Lite using the install script.

```bash
$ cd xcode-project
$ ./install.sh
```

Open **Todo.xcodeproj** in Xcode. Then build run the project.

## [](#create-a-new-database)Create a new database

The entrypoint in the Couchbase Lite SDK is the [Manager](https://docs.couchbase.com/couchbase-lite/1.4/swift.html#manager) class. There is no limit to how many databases can be created or opened on the device. You can think of a database as a namespace for documents and several databases can be used in the same app (one database per user of the app is a common pattern). The code below creates an empty database.

```swift
// This code can be found in AppDelegate.swift
// in the openDatabase(username:withKey:withNewKey) method
let dbname = username
let options = CBLDatabaseOptions()
options.create = true

if kEncryptionEnabled {
    if let encryptionKey = key {
        options.encryptionKey = encryptionKey
    }
}

try database = CBLManager.sharedInstance().openDatabaseNamed(dbname, with: options)
```

Here you're using the `openDatabaseNamed` method where the database is the user currently logged in and `options.create` is set to `true`.

> [!NOTE]
> You can ignore the encryption flag. Database encryption will be covered in the [Adding Security](#swift/adding-security.adoc) lesson.

### [](#try-it-out)Try it out

1. Build and run.
2. Create a new list on the application's 'Task lists' screen.
3. The task list is persisted to the database.  
![image40](../../_images/image40.png)

## [](#using-the-pre-built-database)Using the pre-built database

In this section, you will learn how to bundle a pre-built Couchbase Lite database in an application. It can be a lot more efficient to bundle a database in your application and install it on the first launch. Even if some of the content changes on the server after you create the app, the app's first pull replication will bring the database up to date. Here, you will use a pre-built database that contains a list of groceries. The code below moves the pre-built database from the bundled location to the application directory.

```swift
// This code can be found in AppDelegate.swift
// in the installPrebuiltDb() method
guard kUsePrebuiltDb else {
    return
}

let db = CBLManager.sharedInstance().databaseExistsNamed(todo)

if (!db) {
    let dbPath = Bundle.main.path(forResource: todo, ofType: cblite2)
    do {
        try CBLManager.sharedInstance().replaceDatabaseNamed(todo, withDatabaseDir: dbPath!)
    } catch let error as NSError {
        NSLog(Cannot replace the database %@, error)
    }
}
```

The prebuilt database is installed using the database replacement API only if there isn't any existing database called 'todo'. Since you created an empty database called 'todo' in the previous step you must first remove the existing database.

### [](#try-it-out-2)Try it out

1. Open **AppDelegate.swift** and set the `kUsePrebuiltDb` constant to `true`.  
```swift  
let kUsePrebuiltDb = true  
```
2. Build and run (⚠️ don't forget to delete the app first).
3. A Groceries list will now be visible on the Lists screen. Click on it to see the tasks.  
![image45](../../_images/image45.gif)

> [!NOTE]
> Refer to the [Database](https://docs.couchbase.com/couchbase-lite/1.4/swift.html#database) guide to learn how to create **pre-built** databases.

##### [](#conclusion)Conclusion

Well done! You've completed this lesson on creating a database. In the next lesson you will learn how to write and query documents from the database. Feel free to share your feedback, findings or ask any questions on the forums.