---
title: Create a Database
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/mobile-training-todo/edit/tutorials/content/modules/todo-app/pages/develop/java/create-database.adoc
  xref: xref:tutorials:todo-app:develop/java/create-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/todo-app/develop/java/create-database.html)

# Create a Database

In this lesson you'll be introduced to Couchbase Lite, our embedded NoSQL database. You'll learn how to create a new embedded database and optionally use databases pre-packaged in your application.

## [](#requirements)Requirements

* Android Studio 2.2
* Android SDK 24
* Android Build Tools 24.0.3
* JDK 8
* ⚠️ Docker and x86 Android emulators are [not compatible](http://stackoverflow.com/questions/37397810/android-studio-unable-to-run-avd) (i.e cannot run simultaneously on the same machine). Make sure Docker isn't running in the background when deploying the application to an x86 Android emulator.

## [](#getting-started)Getting Started

Download the [Android Studio project](../../%5Fattachments/project.zip).

## [](#create-a-new-database)Create a new database

The entrypoint in the Couchbase Lite SDK is the [Manager](https://docs.couchbase.com/couchbase-lite/1.4/java.html#manager) class. There is no limit to how many databases can be created or opened on the device. You can think of a database as a namespace for documents and several databases can be used in the same app (one database per user of the app is a common pattern). The code below creates an empty database.

```java
// This code can be found in Application.java
// in the openDatabase(username, key, newKey) method
String dbname = username;
DatabaseOptions options = new DatabaseOptions();
options.setCreate(true);

if (mEncryptionEnabled) {
    options.setEncryptionKey(key);
}

Manager manager = null;
try {
    manager = new Manager(new AndroidContext(getApplicationContext()), Manager.DEFAULT_OPTIONS);
} catch (IOException e) {
    e.printStackTrace();
}
try {
    database = manager.openDatabase(dbname, options);
} catch (CouchbaseLiteException e) {
    e.printStackTrace();
}
```

Here you're using the `openDatabaseNamed` method where the database is the user currently logged in and `options.create` is set to `true`.

> [!NOTE]
> You can ignore the encryption flag. Database encryption will be covered in the [Adding Security](#java/adding-security.adoc) lesson.

### [](#try-it-out)Try it out

1. Build and run.
2. Create a new list on the application's 'Task lists' screen.
3. The task list is persisted to the database.

![image40](../../_images/image40.png)

![image40xa](../../_images/image40xa.png)

![image40w](../../_images/image40w.png)

![image40a](../../_images/image40a.png)

## [](#using-the-pre-built-database)Using the pre-built database

In this section, you will learn how to bundle a pre-built Couchbase Lite database in an application. It can be a lot more efficient to bundle a database in your application and install it on the first launch. Even if some of the content changes on the server after you create the app, the app's first pull replication will bring the database up to date. Here, you will use a pre-built database that contains a list of groceries. The code below moves the pre-built database from the bundled location to the application directory.

```java
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

```java
// This code can be found in CoreApp.cs
// in the InstallPrebuildDB() method
var db = AppWideManager.GetExistingDatabase(todo);
if(db == null) {
    try {
        using(var asset = typeof(CoreApp).Assembly.GetManifestResourceStream(todo.zip)) {
            AppWideManager.ReplaceDatabase(todo, asset, false);
        }
    } catch(Exception e) {
        Debug.WriteLine($Cannot replicate the database: {e});
    }
}
```

```java
// This code can be found in Application.java
// in the installPrebuiltDb() method
if (!mUsePrebuiltDb) {
    return;
}

try {
    manager = new Manager(new AndroidContext(getApplicationContext()), Manager.DEFAULT_OPTIONS);
} catch (IOException e) {
    e.printStackTrace();
}
try {
    database = manager.getExistingDatabase(todo);
} catch (CouchbaseLiteException e) {
    e.printStackTrace();
}
if (database == null) {
    try {
        ZipUtils.unzip(getAssets().open(todo.zip), manager.getContext().getFilesDir());
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

The prebuilt database is installed using the database replacement API only if there isn't any existing database called 'todo'. Since you created an empty database called 'todo' in the previous step you must first remove the existing database.

### [](#try-it-out-2)Try it out

1. Open **AppDelegate.swift** and set the `kUsePrebuiltDb` constant to `true`.  
```java  
let kUsePrebuiltDb = true  
```
2. Build and run (⚠️ don't forget to delete the app first).
3. A Groceries list will now be visible on the Lists screen. Click on it to see the tasks.  
![image45](../../_images/image45.gif)
4. Open **CoreApp.cs** and navigate to the `CoreAppStart.CreateHint()` method.
5. Change the `usePrebuiltDB` on the return value of the function to `true`.  
```c#  
retVal.usePrebuiltDB = true;  
```
6. Build and run (⚠️ don't forget to delete the app first).
7. A Groceries list will now be visible on the Lists screen. Click on it to see the tasks.  
![image45w](../../_images/image45w.gif)

**iOS** **Android**

1. Open **Application.java** and set the `mUsePrebuiltDb` constant to true.
2. Build and run (⚠️ don't forget to delete the app first).
3. A Groceries list will now be visible on the Lists screen. Click on it to see the tasks.

> [!NOTE]
> Refer to the [Database](https://docs.couchbase.com/couchbase-lite/1.4/java.html#database) guide to learn how to create **pre-built** databases.

##### [](#conclusion)Conclusion

Well done! You've completed this lesson on creating a database. In the next lesson you will learn how to write and query documents from the database. Feel free to share your feedback, findings or ask any questions on the forums.