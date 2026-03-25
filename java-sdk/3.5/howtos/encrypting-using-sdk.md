---
title: Encrypting Your Data
description: A practical guide for getting started with Field-Level Encryption,
  showing how to encrypt and decrypt JSON fields using the Java SDK.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.5/modules/howtos/pages/encrypting-using-sdk.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.5@java-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.5/howtos/encrypting-using-sdk.html)

# Encrypting Your Data

> A practical guide for getting started with Field-Level Encryption, showing how to encrypt and decrypt JSON fields using the Java SDK. 

For a high-level overview of this feature, see [Field Level Encryption](../concept-docs/encryption.md).

## [](#package)Packaging

The Couchbase Java SDK works together with the [Java Couchbase Encryption](https://github.com/couchbase/java-couchbase-encryption) library to provide support for encryption and decryption of JSON fields. This library makes use of the cryptographic algorithms available on your platform, and provides a framework for implementing your own crypto components.

> [!NOTE]
> The encryption code is packaged as an optional library and is subject to the Couchbase [License](https://www.couchbase.com/LA03012021) and [Enterprise Subscription License](https://www.couchbase.com/ESLA08042020) agreements. To use the encryption library, you have to explicitly include this dependency in your project configuration. Refer to the [dependencies section](#maven-coordinates).

## [](#requirements)Requirements

* Couchbase Java SDK version `3.0.5` or later.
* Java Couchbase Encryption version `3.0.0` or later.

## [](#maven-coordinates)Maven Coordinates

```xml
<dependency>
    <groupId>com.couchbase.client</groupId>
    <artifactId>couchbase-encryption</artifactId>
    <version>${version}</version>
</dependency>
```

See the [GitHub repository tags](https://github.com/couchbase/java-couchbase-encryption/tags) for the latest version.

### [](#optional-dependencies)Optional Dependencies

To reduce the footprint of this library, some of its dependencies are optional. Using certain features requires adding additional dependencies to your project.

HashiCorp Vault Transit integration requires [Spring Vault](https://docs.spring.io/spring-vault/docs/current/reference/html/):

```xml
<dependency>
    <groupId>org.springframework.vault</groupId>
    <artifactId>spring-vault-core</artifactId>
    <version>2.3.2</version>
</dependency>
```

## [](#configuration)Configuration

To enable Field-Level Encryption, supply a `CryptoManager` when [configuring the Java SDK’s ClusterEnvironment](managing-connections.md#cluster-environment).

```java
KeyStore javaKeyStore = KeyStore.getInstance("MyKeyStoreType");
FileInputStream fis = new java.io.FileInputStream("keyStoreName");
char[] password = { 'a', 'b', 'c' };
javaKeyStore.load(fis, password);
Keyring keyring = new KeyStoreKeyring(javaKeyStore, keyName -> "swordfish");

// AES-256 authenticated with HMAC SHA-512. Requires a 64-byte key.
AeadAes256CbcHmacSha512Provider provider = AeadAes256CbcHmacSha512Provider.builder().keyring(keyring).build();

CryptoManager cryptoManager = DefaultCryptoManager.builder().decrypter(provider.decrypter())
    .defaultEncrypter(provider.encrypterForKey("myKey")).build();

Cluster cluster = Cluster.connect("localhost",
    ClusterOptions.clusterOptions("username", "password")
        .environment(env -> env.cryptoManager(cryptoManager)));
```

## [](#usage)Usage

Two modes of operation are available:

* Transparent encryption/decryption during Jackson data binding.
* Manual field editing using `JsonObjectCrypto`.

### [](#data-binding-example)Data Binding Example

Sensitive fields of your data classes can be annotated with `@Encrypted`. Let’s use this class as an example:

```java
public class Employee {
  @Encrypted
  private boolean replicant;

  // alternatively you could annotate the getter or setter
  public boolean isReplicant() {
    return replicant;
  }

  public void setReplicant(boolean replicant) {
    this.replicant = replicant;
  }
}
```

Now let’s create an employee record and save it to Couchbase:

```java
Employee employee = new Employee();
employee.setReplicant(true);
collection.upsert("employee:1234", employee); // encrypts the "replicant" field
```

You can get the document as a `JsonObject` to verify the field was encrypted:

```java
JsonObject encrypted = collection.get("employee:1234").contentAsObject(); // does not decrypt anything

System.out.println(encrypted);
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

```java
Employee readItBack = collection.get("employee:1234").contentAs(Employee.class); // decrypts the "replicant" field

System.out.println(readItBack.isReplicant());
```

This prints `true`.

#### [](#using-a-custom-objectmapper)Using a custom ObjectMapper

The code that enables encryption/decryption during data binding is packaged as a Jackson module called `EncryptionModule`. You can register this module with any Jackson `ObjectMapper`.

You’ll need to do this if you want to supply your own customized ObjectMapper for the Java SDK to use when serializing documents. Here’s how to configure the cluster environment to use a custom JSON serializer backed by your own ObjectMapper with support for Field-Level Encryption:

```java
// CryptoManager cryptoManager = createMyCryptoManager();
KeyStore javaKeyStore = KeyStore.getInstance("MyKeyStoreType");
FileInputStream fis = new java.io.FileInputStream("keyStoreName");
char[] ksPassword = { 'a', 'b', 'c' };
javaKeyStore.load(fis, ksPassword);
Keyring keyring = new KeyStoreKeyring(javaKeyStore, keyName -> "swordfish");

// AES-256 authenticated with HMAC SHA-512. Requires a 64-byte key.
AeadAes256CbcHmacSha512Provider provider = AeadAes256CbcHmacSha512Provider.builder().keyring(keyring).build();
CryptoManager cryptoManager = DefaultCryptoManager.builder().decrypter(provider.decrypter())
    .defaultEncrypter(provider.encrypterForKey("myKey")).build();

ObjectMapper mapper = new ObjectMapper();
mapper.registerModule(new JsonValueModule()); // for JsonObject
mapper.registerModule(new EncryptionModule(cryptoManager));

// Here you can register more modules, add mixins, enable features, etc.

Cluster cluster = Cluster.connect(connectionString,
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env
            .cryptoManager(cryptoManager)
            .jsonSerializer(JacksonJsonSerializer.create(mapper))
        ));
```

### [](#jsonobjectcrypto)JsonObjectCrypto

If you need more control of which fields get decrypted, or if you prefer working with the Couchbase `JsonObject` tree model, you can use a `JsonObjectCrypto` instance to read and write encrypted field values of a `JsonObject`.

```java
JsonObject document = JsonObject.create();
JsonObjectCrypto crypto = document.crypto(collection);

crypto.put("locationOfBuriedTreasure", "Between palm trees");

// This displays the encrypted form of the field
System.out.println(document);

collection.upsert("treasureMap", document);

JsonObject readItBack = collection.get("treasureMap").contentAsObject();
JsonObjectCrypto readItBackCrypto = crypto.withObject(readItBack);
System.out.println(readItBackCrypto.getString("locationOfBuriedTreasure"));
```

### [](#reading-unencrypted-fields)Reading Unencrypted Fields

From Java SDK 3.2.1, the `@Encrypted` annotation can now be used to migrate an existing field from unencrypted to encrypted. If you annotate a field with:

```java
@Encrypted(migration = Encrypted.Migration.FROM_UNENCRYPTED)
```

then either encrypted or unencrypted values will be accepted during deserialization (without the latter causing error). See the [API docs](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/encryption/annotation/Encrypted.html).

> [!CAUTION]
> Encryption means that document fields have been authenticated. Enabling this feature bypasses that protection, and so this should only be used in strictly limited circumstances, such as the migration from an unencrypted to an encrypted field.

## [](#creating-encryption-keys)Creating Encryption Keys

The AEAD\_AES\_256\_CBC\_HMAC\_SHA512 algorithm included in this library uses encryption keys that are 64 bytes long.

Here’s an example that shows how to create a Java key store file containing a suitable encryption key:

```java
KeyStore keyStore = KeyStore.getInstance("JCEKS");
keyStore.load(null); // initialize new empty key store

// Generate 64 random bytes
SecureRandom random = new SecureRandom();
byte[] keyBytes = new byte[64];
random.nextBytes(keyBytes);

// Add a new key called "my-key" to the key store
KeyStoreKeyring.setSecretKey(keyStore, "my-key", keyBytes, "protection-password".toCharArray());

// Write the key store to disk
try (OutputStream os = new FileOutputStream("MyKeystoreFile.jceks")) {
  keyStore.store(os, "integrity-password".toCharArray());
}
```

And here’s how to use that file to create a `Keyring` for use with Couchbase Field-Level Encryption:

```java
KeyStore keyStore = KeyStore.getInstance("JCEKS");
try (InputStream is = new FileInputStream("MyKeystoreFile.jceks")) {
  keyStore.load(is, "integrity-password".toCharArray());
}

KeyStoreKeyring keyring = new KeyStoreKeyring(keyStore, keyName -> "protection-password");
```

## [](#migration-from-sdk2)Migrating from SDK 2

> [!WARNING]
> SDK 2 cannot read fields encrypted by SDK 3\.

It’s inadvisable to have both the old and new versions of your application active at the same time. The simplest way to migrate is to do an offline upgrade during a scheduled a maintenance window. For an online upgrade without downtime, consider a [blue-green deployment](https://en.wikipedia.org/wiki/Blue-green%5Fdeployment).

SDK 3 requires additional configuration to read fields encrypted by SDK 2\. The rest of this section describes how to configure Field-Level Encryption in SDK 3 for backwards compatibility with SDK 2.

### [](#configure-field-name-prefix)Changing the field name prefix

In SDK 2, the default prefix for encrypted field names was `__crypt_`. This caused problems for Couchbase Sync Gateway, which does not like field names to begin with an underscore. In SDK 3, the default prefix is `encrypted$`.

For compatibility with SDK 2, you can configure the `CryptoManager` to use the old `__crypt_` prefix:

```java
CryptoManager cryptoManager = DefaultCryptoManager.builder()
    .encryptedFieldNamePrefix("__crypt_")
    // other config...
    .build();
```

Alternatively, you can [rename the existing fields](https://forums.couchbase.com/t/replacing-field-name-prefix/28786) using a [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) statement.

> [!WARNING]
> In SDK 2, only top-level fields could be encrypted. SDK 3 allows encrypting fields at any depth. If you decide to rename the existing fields, make sure to do so _before_ writing any encrypted fields below the top level, otherwise it may be difficult to rename the nested fields using a generic SQL++ statement.

### [](#configure-legacy-decrypters)Enabling decrypters for legacy algorithms

The encryption algorithms used by SDK 2 are deprecated, and are no longer used for encrypting new data. To enable decrypting fields written by SDK 2, register the legacy decrypters when configuring the `CryptoManager`:

```java
CryptoManager cryptoManager = DefaultCryptoManager.builder()
    .legacyAesDecrypters(keyring, encryptionKeyName -> "MySigningKeyName")
    .legacyRsaDecrypter(keyring, publicKeyName -> "MyPrivateKeyName")
    // other config...
    .build();
```

> [!NOTE]
> The legacy decrypters require a mapping function. For AES, this function accepts an encryption key name and returns the corresponding signing key name. For RSA, this function accepts a public key name and returns the corresponding private key name.