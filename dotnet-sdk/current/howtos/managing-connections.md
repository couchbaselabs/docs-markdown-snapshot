[View original HTML](/dotnet-sdk/current/howtos/managing-connections.html)

> This section describes how to connect the .NET SDK to a Couchbase cluster. It contains best practices as well as information about TLS/SSL and other advanced connection options. 

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to a Couchbase Server cluster is represented by a `Cluster` object. A `Cluster` provides access to Buckets, Scopes, and Collections, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to call `Cluster.ConnectAsync()` with a [connection string](#connection-strings), username, and password:

```csharp
var cluster = await Cluster.ConnectAsync("couchbase://your-ip", "Administrator", "password");
var bucket =  await cluster.BucketAsync("travel-sample");
var collection = bucket.DefaultCollection();

// You can access multiple buckets using the same Cluster object.
var anotherBucket = await cluster.BucketAsync("travel-sample");

// You can access collections other than the default
// if your version of Couchbase Server supports this feature.
var inventory = bucket.Scope("inventory");
var airline = inventory.Collection("airline");

// For a graceful shutdown, disconnect from the cluster when the program ends.
await cluster.DisposeAsync();
```

|  | If you are connecting to a version of Couchbase Server earlier than 6.5, it will be more efficient if the addresses are those of data (KV) nodes. You will in any case, with 6.0 and earlier, need to open a \`Bucket instance before connecting to any other HTTP services (such as _Query_ or _Search_. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

In a production environment, your connection string should include the addresses of multiple server nodes in case some are currently unavailable. Multiple addresses may be specified in a connection string by delimiting them with commas:

```csharp
var cluster = await Cluster.ConnectAsync("192.168.56.101,192.168.56.102", "Administrator", "password");
```

|  | You do not need to include the address of every node in the cluster. The client fetches the full address list from the first node it is able to contact. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#connection-strings)Connection Strings

A Couchbase connection string is a comma-delimited list of IP addresses and/or hostnames, optionally followed by a list of parameters.

The parameter list is just like the query component of a URI; name-value pairs have an equals sign (`=`) separating the name and value, with an ampersand (`&`) between each pair. Just as in a URI, the first parameter is prefixed by a question mark (`?`).

Simple connection string with one seed node

127.0.0.1

Connection string with two seed nodes

nodeA.example.com,nodeB.example.com

Connection string with two parameters

127.0.0.1?network=external&timeout.kv_timeout=1000

This last connection string with parameters is equivalent to connecting with ClusterOptions:

```csharp
var cluster = await Cluster.ConnectAsync(
    "127.0.0.1",
    new ClusterOptions
    {
        UserName = "Administrator",
        Password = "password",
        NetworkResolution = NetworkResolution.External,
        KvTimeout = TimeSpan.FromSeconds(1)
    }
);
```

Currently, as of .NET SDK Version 3.0.2 there is only partial mapping of query parameters to options properties. This will change in future versions and the entire list of mappings will be found in the [Client Settings reference](../ref/client-settings.md).

A connection string may optionally be prefixed by either `"couchbase://"` or `"couchbases://"`. If `"couchbases://"` is used, the client will use secure connections (TLS/SSL) if a valid certificate is configured or you can use the `ClusterOptions.EnableTls` flag.

## [](#connection-lifecycle)Connection Lifecycle

Most of the high-level classes in the .NET SDK are designed to be safe for concurrent use by multiple threads. You will get the best performance if you share and reuse instances of `Cluster`, `Bucket`, `Scope`, and `Collection`, all of which are thread-safe.

We recommend creating a single `Cluster` instance when your application starts up, and sharing this instance throughout your application. If you know at startup time which buckets, scopes, and collections your application will use, we recommend obtaining them from the `Cluster` at startup time and sharing those instances throughout your application as well.

Before your application stops, gracefully shut down the client by calling the `Dispose` method of each `Cluster` you created. In older applications this can be done in Application\_Start and Application\_End in your Global.asax file. For newer applictions we suggest using Dependency Injection and Startup.cs file.

## [](#connection-di)Dependency Injection

There is a special .NET Core style Dependency Injection (DI) framework for Cluster and Buckets. It simplifies cluster configuration, lifetime management, and bucket injection. You can find it on NuGet.org: [NuGet package](https://www.nuget.org/packages/Couchbase.Extensions.DependencyInjection/). Or using the NuGet Package Manager, add the dependency directly to your project:

|  | Install-Package Couchbase.Extensions.DependencyInjection -Version 3.2.0 |
|  | ----------------------------------------------------------------------- |

### [](#adding-couchbase-to-the-services-collection)Adding Couchbase To The Services Collection

The easiest way to get started in a Web application is to use the `ConfigureService` method in the Services.cs:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();

    services.AddCouchbase(Configuration.GetSection("Couchbase"));
    services.AddCouchbaseBucket<INamedBucketProvider>("");
}
```

### [](#injecting-couchbase-buckets)Injecting Couchbase Buckets

To get a couchbase bucket, simply inject `IBucketNamedProvider` and call `GetBucketAsync`. Be sure that you don’t dispose the IBucket, it’s a singleton that will be reused through the application.

```csharp
public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly INamedBucketProvider _provider;

    public HomeController(ILogger<HomeController> logger, INamedBucketProvider provider)
    {
        _logger = logger;
        _provider = provider;
    }

    public async Task<IActionResult> IndexAsync()
    {
        var bucket = await _provider.GetBucketAsync();
        //do some work

        return View();
    }
}
```

### [](#simplifying-injecting-bucket-names)Simplifying Injecting Bucket Names

```csharp
public interface IMyBucketProvider : INamedBucketProvider
{
}
```

To further simplify dependency injection, you can setup to inject specific buckets. First, create an interface for each bucket that inherits from `INamedBucketProvider`. This interface must be public and left empty.

You can then configure your bucket interfaces during IServiceCollection setup.

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();

    services.AddCouchbase(Configuration.GetSection("Couchbase"));
    services.AddCouchbaseBucket<IMyBucketProvider>("my-bucket");
}
```

The interface you created can now be injected into controllers or business logic, and the `GetBucketAsync` method will return the specified bucket. You are no longer required to know the name of the bucket in the controller, improving separation of concerns in your application.

```csharp
public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly IMyBucketProvider _provider;

    public HomeController(ILogger<HomeController> logger, IMyBucketProvider provider)
    {
        _logger = logger;
        _provider = provider;
    }

    public async Task<IActionResult> IndexAsync()
    {
        var bucket = await _provider.GetBucketAsync();
        //do some work

        return View();
    }
}
```

### [](#injecting-the-couchbase-cluster)Injecting the Couchbase Cluster

If you wish to inject the Couchbase Cluster, you just need to add the IClusterProvider as a parameter to your constructor or the method that you will be calling:

```csharp
public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly IClusterProvider _provider;

    public HomeController(ILogger<HomeController> logger, IClusterProvider provider)
    {
        _logger = logger;
        _provider = provider;
    }

    public async Task<IActionResult> IndexAsync()
    {
        var cluster= await _provider.GetClusterAsync();
        //do some work

        return View();
    }
}
```

Once you have done this you can use Cluster level services like Query and Analytics in your code.

### [](#shutdown)Shutdown

During application shutdown it’s best to close the Couchbase connections gracefully. You can do this using the `ICouchbaseLifetimeService`.\` For Asp.Net Core, you can call this service from the `ApplicationStopped` cancellation token of `IHostApplicationLifetime`.

```csharp
public void Configure(IApplicationBuilder app, IWebHostEnvironment env, IHostApplicationLifetime applicationLifetime)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }

    app.UseRouting();

    app.UseAuthorization();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapControllers();
    });

    
     applicationLifetime.ApplicationStopped.Register(async () =>
        {
            await app.ApplicationServices.GetRequiredService<ICouchbaseLifetimeService>().CloseAsync()
                .ConfigureAwait(false);
        }
    );
}
```

## [](#ssl)Secure Connections

Couchbase Server Enterprise Edition and Couchbase Capella support full encryption of client-side traffic using Transport Layer Security (TLS). That includes key-value type operations, queries, and configuration communication. Make sure you have the Enterprise Edition of Couchbase Server, or a Couchbase Capella account, before proceeding with configuring encryption on the client side.

|  | Prior to .NET SDK 3.7.2, the SDK sets ClusterOptions.ForceIpAsTargetHost to true by default, which means it will send the IP as the target host during TLS authentication. This will cause a certificate name mismatch. As a workaround, for .NET SDK 3.7.1 and earlier, you need to set ClusterOptions.ForceIpAsTargetHost to false for the above to work. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#couchbase-capella)Couchbase Capella

The .NET SDK bundles Capella’s standard root certificate by default. This means you don’t need any additional configuration to enable TLS — simply use `couchbases://` in your connection string (but see the **IMPORTANT** notice, above, if you are running SDK 3.7.1 or earlier).

|  | Capella’s root certificate is **not** signed by a well known CA (Certificate Authority). However, as the certificate is bundled with the SDK when using .NET 6.0 or later, it is trusted by default. .NET Framework clients will have to add it to the Windows certificate store. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#couchbase-server)Couchbase Server

As of SDK 3.4, if you connect to a Couchbase Server cluster with a root certificate issued by a trusted CA (Certificate Authority), you no longer need to configure this in the `ClusterOptions`.

The cluster’s root certificate just needs to be issued by a CA whose certificate is in your system trust store. This includes well known CAs (e.g., GoDaddy, Verisign, etc…​), plus any other CA certificates that you wish to add.

You can still provide a certificate explicitly if necessary:

1. Get the CA certificate from the cluster and save it in a text file.
2. Enable encryption on the client side and point it to the file containing the certificate.

It is important to make sure you are transferring the certificate in an encrypted manner from the server to the client side, so either copy it through SSH or through a similar secure mechanism.

If you are running on `localhost` and just want to enable TLS for a development machine, just copying and pasting it suffices — _so long as you use `127.0.0.1` rather than `localhost` in the connection string_. This is because the certificate will not match the name _localhost_. Setting `TLSSkipVerify` is a workaround if you need to use `couchbases://localhost`.

Navigate in the admin UI to **Settings** **Cluster** and copy the input box of the TLS certificate into a file on your machine (which we will refer to as cluster.cert). It looks similar to this:

-----BEGIN CERTIFICATE-----
MIICmDCCAYKgAwIBAgIIE4FSjsc3nyIwCwYJKoZIhvcNAQEFMAwxCjAIBgNVBAMT
ASowHhcNMTMwMTAxMDAwMDAwWhcNNDkxMjMxMjM1OTU5WjAMMQowCAYDVQQDEwEq
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzz2I3Gi1XcOCNRVYwY5R
................................................................
mgDnQI8nw2arBRoseLpF6WNw22CawxHVOlMceQaGOW9gqKNBN948EvJJ55Dhl7qG
BQp8sR0J6BsSc86jItQtK9eQWRg62+/XsgVCmDjrB5owHPz+vZPYhsMWixVhLjPJ
mkzeUUj/kschgQ0BWT+N+pyKAFFafjwFYtD0e5NwFUUBfsOyQtYV9xu3fw+T2N8S
itfGtmmlEfaplVGzGPaG0Eyr53g5g2BgQbi5l5Tt2awqhd22WOVbCalABd9t2IoI
F4+FjEqAEIr1mQepDaNM0gEfVcgd2SzGhC3yhYFBAH//8W4DUot5ciEhoBs=
-----END CERTIFICATE-----

The next step is to enable encryption and import the certificate.

```csharp
var cluster = await Cluster.ConnectAsync(new ClusterOptions
    {
        EnableTls = true
    }
    .WithConnectionString("couchbase://127.0.0.1")
    .WithCredentials("Administrator", "password"));
```

#### [](#importing-the-certificate-into-windows)Importing the Certificate into Windows

For development, do the following steps to install the certificate:

1. Open Notepad or your favorite text editor using "Run as administrator".
2. Copy the contents of the certificate into the editor.
3. Save as type "All files" and specify the ".crt" file extension.
4. Right click on the file after saving it and click "Install Certificate".
5. Select "Current User" or "Local Machine" depending upon who you want to access the certificate.
6. Select "Next" and then store it as "Trusted Root Certificate Authority".

#### [](#importing-the-certificate-into-macos)Importing the Certificate into MacOS

1. Copy the certificate into a text file with the extension ".crt".
2. Double click on the file and add it to "system" and approve with your password or fingerprint.
3. Double click on the file and expand the "trust" area, mark it as trusted instead of system default.
4. Exit and approve.

#### [](#importing-the-certificate-into-gnulinux)Importing the Certificate into GNU/Linux

Although different distributions differ slightly in the details of their certificate handling, they will be similar to one of the two patterns below. Refer to your distribution’s documentation for precise instructions.

* Debian and Ubuntu
* RHEL and CentOS

```console
$ cd /usr/local/share/ca-certificates/
```

Name a sub-directory to hold the Couchbase certificate:

```console
$ mkdir couchbase-cert
```

```console
$ cp /path/to/my-certificate.crt couchbase-cert/
```

Ensure that the permissions are correct

```console
$ chmod 755 couchbase-cert ; chmod 644 couchbase-cert/my-certificate.crt
```

Update ca-certificates configuration to include the newly imported certificate

```console
sudo dpkg-reconfigure ca-certificates
```

Commit the changes

```console
$ sudo update-ca-certificates
```

```console
$ sudo cp my-certificate.crt /etc/pki/ca-trust/source/anchors/
```

```console
$ sudo update-ca-trust extract
```

#### [](#certificate-verification)Certificate Verification

If you want to verify it’s actually working, you can use a tool like **tcpdump**. For example, an unencrypted upsert request looks like this (using `sudo tcpdump -i lo0 -A -s 0 port 11210`):

E..e..@.@.............+......q{...#..Y.....
.E...Ey........9........................id{"key":"value"}

After enabling encryption, you cannot inspect the traffic in cleartext (same upsert request, but watched on port 11207 which is the default encrypted port):

E.....@.@.............+....Z.'yZ..#........
..... ...xuG.O=.#.........?.Q)8..D...S.W.4.-#....@7...^.Gk.4.t..C+......6..)}......N..m..o.3...d.,.	...W.....U..
.%v.....4....m*...A.2I.1.&.*,6+..#..#.5

## [](#using-dns-srv-records)Using DNS SRV records

As an alternative to specifying multiple hosts in your program, you can get the actual bootstrap node list from a DNS SRV record. For Capella, where you only have one endpoint provided, it’s good practice to always enable DNS-SRV on the client.

The following steps are necessary to make it work:

1. Set up your DNS server to respond properly from a DNS SRV request.
2. Enable it on the SDK and point it towards the DNS SRV entry.

### [](#setting-up-the-dns-server)Setting up the DNS Server

Capella gives you DNS-SRV by default — these instructions are for self-managed clusters, where you are responsible for your own DNS records.

Your DNS server zone file should be set up like this, with one row for each bootstrap (KV, a.k.a. Data Service) node:

; Service.Protocol.Domain	TTL	Class	Type	Priority	Weight	 Port	Target
_couchbases._tcp.example.com.	3600	IN	SRV	0		0	 11207	node1.example.com.
_couchbases._tcp.example.com.	3600	IN 	SRV	0		0	 11207	node2.example.com.
_couchbases._tcp.example.com.	3600	IN 	SRV	0		0	 11207	node3.example.com.

The first line comment is not needed in the record, we are showing the column headers here for illustration purposes. The myriad complexities of DNS are beyond the scope of this document, but note that SRV records must point to an A record, not a `CNAME`.

The order in which you list the nodes — and any value entered for `Priority` or `Weight` — will be ignored by the SDK. Nevertheless, best practice here is to set them to `0`, avoiding ambiguity.

Also note, the above is for connections using TLS. Should you be using an insecure connection (in testing or development, or totally within a firewalled environment), then your records would look like:

_couchbase._tcp.example.com.  3600  IN  SRV  0  0  11210  node1.example.com.
_couchbase._tcp.example.com.  3600  IN  SRV  0  0  11210  node2.example.com.
_couchbase._tcp.example.com.  3600  IN  SRV  0  0  11210  node3.example.com.

### [](#specifying-dns-srv-for-the-sdk)Specifying DNS-SRV for the SDK

* The connection string must be to a single hostname, with no explicit port specifier, pointing to the DNS SRV entry — `couchbases://example.com`.
* DNS-SRV must be enabled in the [client settings](../ref/client-settings.md).

DNS SRV bootstrapping is enabled by default in the .NET SDK. In order to make the SDK use the SRV records, you need to pass in the hostname from your records (here `example.com`):

```csharp
var cluster = await Cluster.ConnectAsync(new ClusterOptions
    {
        EnableTls = true
    }
    .WithConnectionString("couchbases://[YOUR DNS CONNECTION STRING]")
    .WithCredentials("Administrator", "password"));
```

If the DNS SRV records could not be loaded properly you’ll get the exception logged and the given host name will be used as a A record lookup.

    [INF] Error trying to retrieve DNS SRV entries. (addddf06)
    DnsClient.DnsResponseException: Query 63320 => _couchbase._tcp.10.143.200.101 IN SRV on 2001:4860:4860::8888:53 failed with an error.

Also, if you pass in more than one node, DNS SRV bootstrap will not be initiated and regular bootstrapping will occur.

## [](#waiting-for-bootstrap-completion)Waiting for Bootstrap Completion

Depending on the environment and network latency, bootstrapping the SDK fully might take a little longer than the default key-value timeout of 2.5 seconds, so you may see timeouts during bootstrap. To prevent those early timeouts from happening, you can use the `waitUntilReady` method.

If you are working at the _Cluster_ level, then add to the `cluster()` in the [earlier example](#connecting-to-a-cluster):

```csharp
var cluster = await Cluster.ConnectAsync("your-ip", "Administrator", "password");
await cluster.WaitUntilReadyAsync(TimeSpan.FromSeconds(10));
var bucket = await cluster.BucketAsync("travel-sample");
var collection = bucket.DefaultCollection();
```

Or more fully:

```csharp
public class ClusterExample
{
    public async Task ExecuteAsync()
    {
        var cluster = await Cluster.ConnectAsync("your-ip", "Administrator", "password");
        await cluster.WaitUntilReadyAsync(TimeSpan.FromSeconds(10));
        var bucket = await cluster.BucketAsync("travel-sample");
        var collection = bucket.DefaultCollection();
        //..
    }
}
```

If you are working at the _Bucket_ level, then the [Bucket-level waitUntilReady](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.IBucket.html#Couchbase%5FIBucket%5FWaitUntilReadyAsync%5FTimeSpan%5FCouchbase%5FDiagnostics%5FWaitUntilReadyOptions%5F) does the same as the Cluster-level version, _plus_ it waits for the K-V (data) sockets to be ready.

```csharp
public class ClusterExample2
{
    public async Task ExecuteAsync()
    {
        var cluster = await Cluster.ConnectAsync("your-ip", "Administrator", "password");
        var bucket = await cluster.BucketAsync("travel-sample");
        await bucket.WaitUntilReadyAsync(TimeSpan.FromSeconds(10));
        var collection = bucket.DefaultCollection();
        //..
    }
}
```

Other timeout issues may occur when using the SDK located geographically separately from the Couchbase Server cluster — this is [not recommended](../project-docs/compatibility.md#network-requirements). See the [Cloud section](#working-in-the-cloud) below for some suggestions of settings adjustments.

For most use cases, connecting client software using a Couchbase SDK to the [Couchbase Capella service](#cloud:ROOT:index.adoc) is similar to connecting to an on-premises Couchbase Cluster. The use of DNS-SRV, Alternate Address, and TLS is covered above.

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options). More details on connecting your client code to Couchbase Capella can be found [in the Cloud docs](#cloud:clouds:connect.adoc#connecting-from-sdk-cli-or-cbsh).

### [](#troubleshooting-connections-to-cloud)Troubleshooting Connections to Cloud

Some DNS caching providers (notably, home routers) can’t handle an SRV record that’s large — if you have DNS-SRV issues with such a set-up, reduce your DNS-SRV to only include three records. \[_For development only, not production._\]. Our [Troubleshooting Cloud Connections](troubleshooting-cloud-connections.md) page will help you to diagnose this and other problems — as well as introducing the SDK doctor tool.

## [](#additional-resources)Additional Resources

* Our [Authentication](sdk-authentication.md) page covers connecting with LDAP and Certificate Authentication.
* Connecting from SDK to Couchbase Server is best done wih both being in the same LAN-like environment or Cloud _Availability Zone_. This is not always possible at the development stage, where you may be using a local laptop for SDK development against a [Couchbase Capella](https://docs.couchbase.com/cloud/index.html) instance, so help is available for timeout issues in such unsupported configurations in our [Troubleshooting Cloud Connections](troubleshooting-cloud-connections.md) page.