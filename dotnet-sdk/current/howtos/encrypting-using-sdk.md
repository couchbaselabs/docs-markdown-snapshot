---
title: Encrypting Your Data
description: A practical guide for getting started with Field-Level Encryption,
  showing how to encrypt and decrypt JSON fields using the .NET SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.9/modules/howtos/pages/encrypting-using-sdk.adoc
  xref: xref:dotnet-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/howtos/encrypting-using-sdk.html)

# Encrypting Your Data

> A practical guide for getting started with Field-Level Encryption, showing how to encrypt and decrypt JSON fields using the .NET SDK. 

For a high-level overview of this feature, see the [Field-Level Encryption discussion doc](../concept-docs/encryption.md).

> [!TIP]
> Native Encryption at Rest
> 
> Server 8.x (and new Capella Operational clusters) offer [encryption at rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md). It's a comprehensive way of encrypting all data in a non-ephemeral bucket, as well as logs, configuration data, and audit data. However, you may prefer the relative simplicity of key management in Field Level Encryption for use cases where there are a limited number of data to be encrypted.

## [](#package)Packaging

The Couchbase .NET SDK works together with the [.NET Couchbase Encryption](https://github.com/couchbase/dotnet-couchbase-encryption) library to provide support for encryption and decryption of JSON fields. This library makes use of the cryptographic algorithms available on your platform, and provides a framework for implementing your own crypto components.

> [!NOTE]
> The encryption code is packaged as an optional library and is subject to the Couchbase [License](https://www.couchbase.com/LA03012021) and [Enterprise Subscription License](https://www.couchbase.com/ESLA08042020) agreements. To use the encryption library, you have to explicitly include this dependency in your project configuration. Refer to the [dependencies section](#maven-coordinates).

## [](#requirements)Requirements

* Couchbase .NET SDK version `3.1.3` or later.
* .NET Couchbase Encryption version `2.0.0` or later.

## [](#nuget-package)NuGet Package

```xml
<PackageReference Include="Couchbase.Extensions.Encryption" Version="2.0.0" />
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

Sensitive fields of your data classes can be annotated with `EncryptedField`. Let's use this class as an example:

```csharp
public class Employee
{
    [EncryptedField(KeyName = "test-key")]
    public bool IsReplicant { get; set; }
}
```

Now let's create an employee record and save it to Couchbase:

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

Now let's read the employee record using data binding:

```csharp
using var getResult2 = await collection.GetAsync(id, options => options.Transcoder(encryptedTranscoder))
    .ConfigureAwait(false);

var readItBack = getResult2.ContentAs<Employee>();
Console.WriteLine(readItBack.IsReplicant);
```

This prints `true`.

## [](#creating-encryption-keys)Creating Encryption Keys

The AEAD\_AES\_256\_CBC\_HMAC\_SHA512 algorithm included in this library uses encryption keys that are 64 bytes long.

Here's an example that shows how to create a suitable encryption key:

```csharp
var keyBytes = new Span<byte>(new byte[64]);
RandomNumberGenerator.Fill(keyBytes);

var keyRing = new Keyring(new IKey[]
{
    new Key("my-key", keyBytes.ToArray())
});
```

And here's how to use it to create a `Keyring` for use with Couchbase Field-Level Encryption:

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

SDK 2.x reached end-of-life long ago, but should you have fields encrypted by SDK 2.x, and the need to read them from SDK 3.x, then follow the steps in the [archived documents](https://docs-archive.couchbase.com/dotnet-sdk/3.4/howtos/encrypting-using-sdk.html#migration-from-sdk2).

> [!IMPORTANT]
> The encryption algorithms used by SDK 2 are deprecated, and are no longer used for encrypting new data. Do not rely on the security of outdated encryption algorithms.