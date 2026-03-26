---
title: Field Level Encryption from the SDK
description: The Field Level Encryption library enables encryption and
  decryption of JSON fields, to support FIPS-140-2 compliance.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.3/modules/howtos/pages/encrypting-using-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cxx-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/howtos/encrypting-using-sdk.html)

# Field Level Encryption from the SDK

> The Field Level Encryption library enables encryption and decryption of JSON fields, to support FIPS-140-2 compliance. 

> [!TIP]
> Native Encryption at Rest
> 
> Server 8.x (and new Capella Operational clusters) offer [encryption at rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md). It's a comprehensive way of encrypting all data in a non-ephemeral bucket, as well as logs, configuration data, and audit data. However, you may prefer the relative simplicity of key management in Field Level Encryption for use cases where there are a limited number of data to be encrypted.

For a high-level overview of this feature, see [Field Level Encryption](../concept-docs/encryption.md).

## [](#package)Packaging

The Couchbase C++ SDK works together with the [C++ Couchbase Encryption](https://github.com/couchbase/couchbase-cxx-encryption) library to provide support for encryption and decryption of JSON Object fields. This library makes use of the cryptographic algorithms available on the OpenSSL or BoringSSL libraries linked to the C++ SDK, and provides a framework for implementing your own crypto components.

> [!NOTE]
> The encryption code is packaged as an optional library and is subject to the Couchbase [License](https://www.couchbase.com/LA03012021) and [Enterprise Subscription License](https://www.couchbase.com/ESLA08042020) agreements. To use the encryption library, you have to explicitly include this dependency in your project configuration.

To get started with the C++ Field Level Encryption library you can fetch it, for example, using [CPM.cmake](https://github.com/cpm-cmake/CPM.cmake):

```cmake
CPMAddPackage(
  NAME
  couchbase_cxx_encryption
  GIT_TAG
  ${version}
  VERSION
  ${version}
  GITHUB_REPOSITORY
  "couchbase/couchbase-cxx-encryption")
```

### [](#requirements)Requirements

* Couchbase C++ SDK version `1.2.0` or later.
* C++ Couchbase Encryption version `1.0.0` or later.

## [](#configuration)Configuration

To enable Field-Level Encryption, supply a `couchbase::crypto::manager` when [configuring the C++ SDK's couchbase::cluster\_options](managing-connections.md#cluster-environment).

```c++
// Supply the crypto manager when connecting to the cluster.
auto options = couchbase::cluster_options(user_name, password).crypto_manager(manager);
auto [connect_err, cluster] = couchbase::cluster::connect(connection_string, options).get();
```

## [](#usage)Usage

Two modes of operation are available out of the box using the provided `couchbase::crypto::default_transcoder`:

* Transparent encryption/decryption by defining which fields are to be encrypted for a custom document type.
* Manually specifying fields to be encrypted using `couchbase::crypto::document`.

> [!NOTE]
> Only fields of JSON Objects can be encrypted.

### [](#custom-document-type-example)Custom document type example

Sensitive fields of your data classes can be enumerated in an `encrypted_fields` static `std::vector<couchbase::crypto::encrypted_field>`. For each field, the name of the field, as it appears in the serialized JSON document, and optionally an encrypter alias should be specified.

```c++
struct person {
    struct address {
        std::string street;
        std::string city;
        std::string state;
        std::string zip;
    };

    std::string first_name;
    std::string last_name;
    std::string password;
    address address;
    std::string phone_number;

    // Define the fields that should be encrypted, with the paths they will appear with in the
    // serialized JSON document. If no encrypter alias is specified, the field will be encrypted
    // with the default encrypter.
    static const inline std::vector<couchbase::crypto::encrypted_field> encrypted_fields{
        { /* .field_path = */ { "password" }, /* .encrypter_alias = */ { "my-other-encrypter" } },
        { /* .field_path = */ { "address", "street" },
          /* .encrypter_alias = */ { "my-encrypter" } },
        { /* .field_path = */ { "address", "zip" } },
        { /* .field_path = */ { "phone" } },
    };
};
```

Now let's create a `person` document and save it to Couchbase:

> [!IMPORTANT]
> Remember to use a crypto transcoder, such as `couchbase::crypto::default_transcoder`, when field encryption is required.

```c++
auto collection = cluster.bucket(bucket_name).scope(scope_name).collection(collection_name);

const auto person1 = person{
    /* .first_name = */ "John",
    /* .last_name = */ "Doe",
    /* .password = */ "password123",
    /* .address = */
    {
      /* .street = */ "999 Street St.",
      /* .city = */ "Some City",
      /* .state = */ "ST",
      /* .zip = */ "12345",
    },
    /* .phone_number = */ "12345678",
};

// To encrypt the document a crypto transcoder (such as the provided
// `crypto::default_transcoder`) must be used. The crypto transcoder uses the crypto manager
// specified via the cluster options to encrypt the fields that were specified.
const auto [err, upsert_res] =
  collection.upsert<couchbase::crypto::default_transcoder>("person-1", person1).get();
if (err) {
    fmt::println("Failed to upsert the document {}", err);
}
```

You can get the document as a `tao::json::value` and the default JSON transcoder to verify the field was encrypted:

```c++
const auto [err, get_res] = collection.get("person-1").get();
if (err) {
    fmt::println("Failed to get the document {}", err);
}

// Decoding the content with a standard non-crypto transcoder will return the encrypted
// document
const auto encrypted_document = get_res.content_as<tao::json::value>();
fmt::println("{}", tao::json::to_string(encrypted_document, 2));
```

Because the default JSON transcoder does not decrypt anything, the expected output is something like:

```json
{
  "address": {
    "city": "Some City",
    "encrypted$street": {
      "alg": "AEAD_AES_256_CBC_HMAC_SHA512",
      "ciphertext": "dYo1KbbRTcvC3RgLh7slLaNXjSBT8BZ8tXVGHHbw1yi5r2OtiYmm5tagoOE61L6loCNUOqB5nr4ikDAeZb9ljSJBmIRB6p7ik29tt0MrvX8=",
      "kid": "my-key"
    },
    "encrypted$zip": {
      "alg": "AEAD_AES_256_CBC_HMAC_SHA512",
      "ciphertext": "4gMGy74p3xicKxLnRq2kiZjwolBeidA53oiQy+FLIhPUA93O7f+SiwcHBX5eWcu114O6dX2NOvq6ScIRGFwMhQ==",
      "kid": "my-key"
    },
    "state": "ST"
  },
  "encrypted$password": {
    "alg": "AEAD_AES_256_CBC_HMAC_SHA512",
    "ciphertext": "HKXofQdg7ghNM2htiMTzwWbcRRWCrKUApK202tAv8kQOENRsFlxCntM7EsJmnGTui8zYHNGbJcC+5kxDXw+XVA==",
    "kid": "my-other-key"
  },
  "encrypted$phone": {
    "alg": "AEAD_AES_256_CBC_HMAC_SHA512",
    "ciphertext": "JE5URIugqSEp9Yp56/lje4MpHOZyXHVX6V+/AcIndfJ9XmZCPGL9olXUdT2b0mFgnGXO8I6phJTfnTBpdqmh4Q==",
    "kid": "my-key"
  },
  "first_name": "John",
  "last_name": "Doe"
}
```

Now let's read the `person` document using the crypto transcoder:

```c++
// Decoding the content with the crypto transcoder will decrypt the encrypted fields.
const auto decrypted_person =
  get_res.content_as<person, couchbase::crypto::default_transcoder>();
fmt::println("{}", decrypted_person);
```

This outputs the decrypted contents of the document:

```console
First name:   John
Last name:    Doe
Password:     password123
Address:      999 Street St., Some City, ST, 12345
Phone number: 12345678
```

### [](#couchbasecryptodocument-example)`couchbase::crypto::document` example

If you need more control of which fields get decrypted, or if you prefer working with generic JSON types (such as `tao::json::value`), you can use a `couchbase::crypto::document` instance and manually specify which fields to encrypt.

First, create a `couchbase::crypto::document<tao::json::value>` instance and specify the fields to encrypt. Then upsert the document to Couchbase:

```c++
tao::json::value content{
    { "num", 20 },
    { "message", "This is a secret!" },
};

const auto crypto_doc =
  couchbase::crypto::document<tao::json::value>::from(std::move(content))
    .with_encrypted_field({ "message" }, "my-encrypter");

const auto [err, upsert_res] =
  collection.upsert<couchbase::crypto::default_transcoder>("my-crypto-doc", crypto_doc)
    .get();
if (err) {
    fmt::println("Failed to upsert the document {}", err);
}
```

As before, you can get the document as a `tao::json::value` and the default JSON transcoder to verify the field was encrypted:

```c++
const auto [err, get_res] = collection.get("my-crypto-doc").get();
if (err) {
    fmt::println("Failed to get the document {}", err);
}

// Decoding the content with a standard non-crypto transcoder will return the encrypted
// document
const auto encrypted_document = get_res.content_as<tao::json::value>();
fmt::println("{}", tao::json::to_string(encrypted_document, 2));
```

This outputs the encrypted content of the document:

```c++
{
  "encrypted$message": {
    "alg": "AEAD_AES_256_CBC_HMAC_SHA512",
    "ciphertext": "DOdagMvAi8gE4LcNx++z8ghSavOL/WYQ5MlcHkVtzgT9MfZJB/brTdW14Ja851jZOD2GYt3mRJbM1nGIvU+iSYLcgPi45cMwvilqVI+2TiA=",
    "kid": "my-key"
  },
  "num": 20
}
```

Now let's read the document using the crypto transcoder:

```c++
// Decoding the content with the crypto transcoder will decrypt the encrypted fields.
const auto decrypted_document =
  get_res.content_as<tao::json::value, couchbase::crypto::default_transcoder>();
fmt::println("{}", tao::json::to_string(decrypted_document, 2));
```

This outputs the decrypted of the document:

```json
{
  "message": "This is a secret!",
  "num": 20
}
```

## [](#further-reading)Further Reading

* For a more detailed description of the C++ Encryption library's API, and additional examples, see the [API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-encryption-1.0.0/index.html).