[View original HTML](/efcore-provider/current/entity-framework-core-configuration.html)

> Couchbase EFCore configuration choices 

The EF Core Couchbase DB provider ties directly into [.NET Core Dependency Injection (DI)](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection) via the [Couchbase Dependency Injection Library](https://docs.couchbase.com/dotnet-sdk/current/howtos/managing-connections.html#connection-di).

## [](#configuring-using-iservicecollection)Configuring using IServiceCollection

For most applications dependencies are injected into the .NET Service Container during application startup, often in the class file that contains the `Main()` method:

```csharp
builder.Services.AddDbContext<SchoolContext>(options=> options
    .UseCouchbase(new ClusterOptions()
    .WithCredentials("Administrator", "password")
    .WithConnectionString("couchbase://localhost"),
        couchbaseDbContextOptions =>
        {
            couchbaseDbContextOptions.Bucket = "universities";
            couchbaseDbContextOptions.Scope = "contoso";
        }));
```

In this example from the [Contoso University Sample application](https://github.com/couchbaselabs/couchbase-efcore-provider/tree/main/samples/ContosoUniversity), the EF Core Couchbase DB Provider is configured in the [Program.cs](https://github.com/couchbaselabs/couchbase-efcore-provider/blob/main/samples/ContosoUniversity/Program.cs) file. This accomplishes two things:

1. inject the dependency on the Couchbase SDK and
2. inject the dependency on the EF Core Couchbase Provider into the application for the `SchoolContext`, which is a `DbContext`.

## [](#configuring-using-dbcontext-onconfiguring)Configuring using DbContext.OnConfiguring

The EF Core Couchbase DB Provider can also be configured on a per DbContext level. To do this, override the DbContext.OnConfiguring method and add inject the Couchbase SDK and Provider:

```csharp
protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        var loggingFactory = LoggerFactory.Create(builder => builder.AddConsole());
        options.UseCouchbase(new ClusterOptions()
                .WithCredentials("Administrator", "password")
                .WithConnectionString("couchbase://localhost")
                .WithLogging(loggingFactory),
            couchbaseDbContextOptions =>
            {
                couchbaseDbContextOptions.Bucket = "Blogging";
                couchbaseDbContextOptions.Scope = "MyBlog";
            });
    }
```

You can see an example of this in the [CouchbaseGettingStarted](https://github.com/couchbaselabs/couchbase-efcore-provider/tree/main/samples/CouchbaseGettingStarted)example on [Model.cs](https://github.com/couchbaselabs/couchbase-efcore-provider/blob/main/samples/CouchbaseGettingStarted/Model.cs#L13) class.

## [](#couchbase-sdk-options)Couchbase SDK options

Configuring the SDK is largely the same for EF Core Couchbase DB Provider. The SDK’s configuration is handled by the ClusterOptions.cs class. More details of the ClusterOptions class can be found in the [main SDK documentation](../../dotnet-sdk/current/ref/client-settings.md).

## [](#ef-core-couchbase-db-provider-options)EF Core Couchbase DB Provider options

The [CouchbaseDbContextOptionsBuilder](https://github.com/couchbaselabs/couchbase-efcore-provider/blob/main/src/Couchbase.EntityFrameworkCore/Infrastructure/CouchbaseDbContextOptionsBuilder.cs) handles configuration options specific to the provider.

## [](#controlling-json-casing)Controlling JSON casing

By default the SDK uses Camel casing for JSON serialization. While this can be changed via the Serializer settings, we suggest you stick to the default unless you have a specific reason to change it.

## [](#controlling-querying-casing)Controlling Querying Casing

SQL++ is based upon JSON, thus is case sensitive both from the Query perspective and the query output. What this means is that your Keyspaces (Bucket, Scopes, and Collections), the SQL++ query casing, and your entities must have consistent casing.

You can control the casing of your entities using standard `NewtonSoft.JsonProperty` and or `System.Text.Json.JsonPropertyName` attributes, by the property or field names themselves and by using the `Column` attribute.

The generated SQL++ casing can be controlled via the [EFCore.NamingConventions](https://www.nuget.org/packages/EFCore.NamingConventions) library:

```csharp
dotnet add package EFCore.NamingConventions --version 8.0.3
```

Which is added as part of configuration of the EF Core Couchbase DB Provider:

```csharp
optionsBuilder.UseCouchbase(_clusterOptions, couchbaseDbContextOptions =>
{
    couchbaseDbContextOptions.Bucket = "travel-sample";
    couchbaseDbContextOptions.Scope = "inventory";
});
optionsBuilder.UseCamelCaseNamingConvention();
```

[Documentation](https://github.com/efcore/EFCore.NamingConventions) for EFCore.Naming Conventions is located in the GitHub repo. Of interest is the section on [supported naming conventions](https://github.com/efcore/EFCore.NamingConventions?tab=readme-ov-file#supported-naming-conventions).

|  | The casing of the queries that EF Core generates much match the casing of the JSON stored in Couchbase. The reason is because JSON is case sensitive and if they do not match, the queries will not return the expected results. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |