[View original HTML](/dotnet-sdk/3.6/howtos/encrypting-using-sdk.html)

> A practical guide for getting started with Field-Level Encryption, showing how to encrypt and decrypt JSON fields using the .NET SDK. 

For a high-level overview of this feature, see the [Field-Level Encryption discussion doc](../concept-docs/encryption.md).

## [](#package)Packaging

The Couchbase .NET SDK works together with the [.NET Couchbase Encryption](https://github.com/couchbase/dotnet-couchbase-encryption) library to provide support for encryption and decryption of JSON fields. This library makes use of the cryptographic algorithms available on your platform, and provides a framework for implementing your own crypto components.

|  | The encryption code is packaged as an optional library and is subject to the Couchbase [License](https://www.couchbase.com/LA03012021) and [Enterprise Subscription License](https://www.couchbase.com/ESLA08042020) agreements. To use the encryption library, you have to explicitly include this dependency in your project configuration. Refer to the [dependencies section](#maven-coordinates). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#requirements)Requirements

* Couchbase .NET SDK version `3.1.3` or later.
* .NET Couchbase Encryption version `2.0.0-dp.1` or later.

## [](#nuget-package)NuGet Package

```xml
<PackageReference Include="Couchbase.Extensions.Encryption" Version="2.0.0-dp.1" />
```

See the [NuGet Package Page](https://www.nuget.org/packages/Couchbase.Extensions.Encryption/) for the latest version.

## [](#configuration)Configuration

To enable Field-Level Encryption, create a `CryptoManager` and supply `EncryptedFieldTranscoder` as an `Options` on the K/V operation.

```csharp
var provider =
    new AeadAes256CbcHmacSha512Provider(
        new AeadAes256CbcHmacSha512Cipher(), new Keyring(new IKey[]
        {
            new Key("test-key", GetFakeKey(64))
        }));

var cryptoManager = DefaultCryptoManager.Builder()
    .Decrypter(provider.Decrypter())
    .DefaultEncrypter(provider.Encrypter("test-key"))
    .Build();

var encryptedTranscoder = new EncryptedFieldTranscoder(cryptoManager);

var clusterOptions = new ClusterOptions()
    .WithTranscoder(encryptedTranscoder)
    .WithConnectionString("couchbase://your-ip")
    .WithCredentials("Administrator", "password");

var cluster = await Cluster.ConnectAsync(clusterOptions);
var bucket = await cluster.BucketAsync("travel-sample");
```

## [](#usage)Usage

Two modes of operation are available:

* Transparent encryption/decryption using `EncryptedFieldAttribute` on POCOs on deserialization/serialization.
* Manual field editing using `JObjectExtensions` and the `CryptoManager` itself.

### [](#data-binding-example)Data Binding Example

Sensitive fields of your data classes can be annotated with `EncryptedField`. Let’s use this class as an example:

```csharp
public class Employee
{
    [EncryptedField(KeyName = "test-key")]
    public bool IsReplicant { get; set; }
}
```

Now let’s create an employee record and save it to Couchbase:

```csharp
var collection = await bucket.DefaultCollectionAsync();

await collection.UpsertAsync(id, employee, options => { options.Expiry(TimeSpan.FromSeconds(10)); })
    .ConfigureAwait(false); //encrypts the IsReplicant field
```

You can get the document as a `JsonObject` to verify the field was encrypted:

```csharp
using var getResult1 = await collection.GetAsync(id, options => options.Transcoder(encryptedTranscoder))
    .ConfigureAwait(false);

var encrypted = getResult1.ContentAs<JObject>();
Console.WriteLine(encrypted);
```

Because `contentAsObject()` does not decrypt anything, the expected output is something like:

```json
{
  "encrypted$replicant": {
    "alg": "AEAD_AES_256_CBC_HMAC_SHA512",
    "ciphertext": "xwcxyUyZ.....",
    "kid": "myKey"
  }
}
```

Now let’s read the employee record using data binding:

```csharp
using var getResult2 = await collection.GetAsync(id, options => options.Transcoder(encryptedTranscoder))
    .ConfigureAwait(false);

var readItBack = getResult2.ContentAs<Employee>();
Console.WriteLine(readItBack.IsReplicant);
```

This prints `true`.

## [](#creating-encryption-keys)Creating Encryption Keys

The AEAD\_AES\_256\_CBC\_HMAC\_SHA512 algorithm included in this library uses encryption keys that are 64 bytes long.

Here’s an example that shows how to create a suitable encryption key:

```csharp
var keyBytes = new Span<byte>(new byte[64]);
RandomNumberGenerator.Fill(keyBytes);

var keyRing = new Keyring(new IKey[]
{
    new Key("my-key", keyBytes.ToArray())
});
```

And here’s how to use it to create a `Keyring` for use with Couchbase Field-Level Encryption:

```csharp
var provider =
    new AeadAes256CbcHmacSha512Provider(
        new AeadAes256CbcHmacSha512Cipher(), new Keyring(new IKey[]
        {
            new Key("test-key", GetFakeKey(64))
        }));

var cryptoManager = DefaultCryptoManager.Builder()
    .Decrypter(provider.Decrypter())
    .DefaultEncrypter(provider.Encrypter("test-key"))
    .Build();
```

## [](#migration-from-sdk2)Migrating from SDK 2

|  | SDK 2 cannot read fields encrypted by SDK 3\. |
|  | --------------------------------------------- |

It’s inadvisable to have both the old and new versions of your application active at the same time. The simplest way to migrate is to do an offline upgrade during a scheduled a maintenance window. For an online upgrade without downtime, consider a [blue-green deployment](https://en.wikipedia.org/wiki/Blue-green%5Fdeployment).

SDK 3 requires additional configuration to read fields encrypted by SDK 2\. The rest of this section describes how to configure Field-Level Encryption in SDK 3 for backwards compatibility with SDK 2.

### [](#configure-field-name-prefix)Changing the field name prefix

In SDK 2, the default prefix for encrypted field names was `__crypt_`. This caused problems for Couchbase Sync Gateway, which does not like field names to begin with an underscore. In SDK 3, the default prefix is `encrypted$`.

For compatibility with SDK 2, you can configure the `CryptoManager` to use the old `__crypt_` prefix:

```csharp
var cryptoManager = DefaultCryptoManager.Builder()
    .EncryptedFieldNamePrefix("__crypt_")
    //other config
    .Build();
```

Alternatively, you can [rename the existing fields using a SQL++ statement](https://forums.couchbase.com/t/replacing-field-name-prefix/28786) (formerly N1QL).

|  | In SDK 2, only top-level fields could be encrypted. SDK 3 allows encrypting fields at any depth. If you decide to rename the existing fields, make sure to do so _before_ writing any encrypted fields below the top level, otherwise it may be difficult to rename the nested fields using a generic SQL++ statement. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#configure-legacy-decrypters)Enabling decrypters for legacy algorithms

The encryption algorithms used by SDK 2 are deprecated, and are no longer used for encrypting new data. To enable decrypting fields written by SDK 2, register the legacy decrypters when configuring the `CryptoManager`:

```csharp
var cryptoManager = DefaultCryptoManager.Builder()
    .LegacyAesDecrypters(keyring, "hmacKey")
    .DefaultEncrypter(provider.Encrypter("upgrade-key"))
    .Decrypter(provider.Decrypter())
    .Build();
```

|  | The legacy decrypters require a mapping function. For AES, this function accepts an encryption key name and returns the corresponding signing key name. For RSA, this function accepts a public key name and returns the corresponding private key name. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |