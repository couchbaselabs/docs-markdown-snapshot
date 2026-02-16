[View original HTML](/tutorials/mobile-travel-tutorial/csharp/develop/pre-built-database.html)

## [](#starting-with-prebuilt-database)Starting with Prebuilt Database

In this section, you will learn how to bundle a pre-built Couchbase Lite database in an application. It can be a lot more efficient to bundle static or semi-static content database in your application and install it on the first launch. Even if some of the content changes on the server after you create the app, the app’s first pull replication will bring the database up to date. Here, you will use a pre-built database that contains only airport and hotel documents. The code below moves the pre-built database from the bundled location to the platform default directory defined by Couchbase.

**Open the file**`LoginModel.cs` and navigate to the `StartSessionAsync` method.

This method first checks if a database file already exists. If it doesn’t exist it loads the database according to the logic for the platform (UWP from the Assets folder, iOS from the main bundle, Android from Assets)

[DatabaseManager.csharp](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/dotnet/TravelSample/TravelSample.Core/Models/LoginModel.cs#L54)

```{param-language}
 if (!Database.Exists(DbName, userFolder)) {
    // Load prebuilt database to path
    var copier = Service.Provider.GetService<IDatabaseSeedService>();
    await copier.CopyDatabaseAsync(userFolder);

    db = new Database(DbName, options);
    CreateDatabaseIndexes(db);
}
```

Try it out

1. Log into the Travel Sample Mobile app as “demo” user and password as “password”
2. Tap on "+\`" button to make a flight reservation
3. In the “From” airport textfield, enter “San”
4. Confirm that the first item in the dropdown list of "San Diego Intl"

|  | This is not currently functioning in Xamarin iOS since the custom drop down view has not been implemented |
|  | --------------------------------------------------------------------------------------------------------- |

The screen recording is for UWP app.

![uwp prebuilt](https://raw.githubusercontent.com/couchbaselabs/mobile-travel-sample/master/content/assets/uwp_prebuilt.gif) 

Figure 1\. Flight Dropdown List