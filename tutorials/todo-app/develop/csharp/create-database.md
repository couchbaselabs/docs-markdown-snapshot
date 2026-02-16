[View original HTML](/tutorials/todo-app/develop/csharp/create-database.html)

In this lesson you’ll be introduced to Couchbase Lite, our embedded NoSQL database. You’ll learn how to create a new embedded database and optionally use databases pre-packaged in your application.

## [](#requirements)Requirements

* Visual Studio 2015+ (Windows) or Xamarin Studio 6+ (OS X)

## [](#getting-started)Getting Started

Download the [Visual Studio project](../../%5Fattachments/project.zip).

## [](#create-a-new-database)Create a new database

The entrypoint in the Couchbase Lite SDK is the [Manager](https://docs.couchbase.com/couchbase-lite/1.4/csharp.html#manager) class. There is no limit to how many databases can be created or opened on the device. You can think of a database as a namespace for documents and several databases can be used in the same app (one database per user of the app is a common pattern). The code below creates an empty database.

```csharp
// This code can be found in CoreApp.cs
// in the OpenDatabase(string, string, string) method
var encryptionKey = default(SymmetricKey);
if(key != null) {
    encryptionKey = new SymmetricKey(key);
}

var options = new DatabaseOptions {
    Create = true,
    EncryptionKey = encryptionKey
};

Database = AppWideManager.OpenDatabase(dbName, options);
if(newKey != null) {
    Database.ChangeEncryptionKey(new SymmetricKey(newKey));
}
```

Here you’re using the `openDatabaseNamed` method where the database is the user currently logged in and `options.create` is set to `true`.

|  | You can ignore the encryption flag. Database encryption will be covered in the [Adding Security](#csharp/adding-security.adoc) lesson. |
|  | -------------------------------------------------------------------------------------------------------------------------------------- |