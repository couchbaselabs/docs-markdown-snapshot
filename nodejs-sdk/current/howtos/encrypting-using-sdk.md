---
title: Encrypting Your Data
description: A practical guide for getting started with Field-Level Encryption,
  showing how to encrypt and decrypt JSON fields using the Node.js SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.7/modules/howtos/pages/encrypting-using-sdk.adoc
  xref: xref:nodejs-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/current/howtos/encrypting-using-sdk.html)

# Encrypting Your Data

> A practical guide for getting started with Field-Level Encryption, showing how to encrypt and decrypt JSON fields using the Node.js SDK. 

For a high-level overview of this feature, see our [Encryption](../concept-docs/encryption.md) page.

> [!TIP]
> Native Encryption at Rest
> 
> Server 8.x (and new Capella Operational clusters) offer [encryption at rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md). It's a comprehensive way of encrypting all data in a non-ephemeral bucket, as well as logs, configuration data, and audit data. However, you may prefer the relative simplicity of key management in Field Level Encryption for use cases where there are a limited number of data to be encrypted.

## [](#packaging)Packaging

The Node.js SDK works together with the [Node Couchbase Encryption](https://github.com/couchbase/node-couchbase-encryption) library to provide support for encryption and decryption of JSON fields. This library makes use of the cryptographic algorithms available on your platform, and provides a framework for implementing your own crypto components.

> [!NOTE]
> The encryption code is packaged as an optional library and is subject to the Couchbase [License](https://www.couchbase.com/LA03012021) and [Enterprise Subscription License](https://www.couchbase.com/ESLA08042020) agreements. To use the encryption library, you have to explicitly include this dependency in your project configuration.

To get started with the Node encryption library you can fetch it using:

```console
$ npm i cbfieldcrypt
```

## [](#configuration)Configuration

The Node.js Field-Level Encryption library works on the principle of `Encrypters` and `Decrypters` which can be packaged within a `Provider`, as well as a custom [Transcoder](transcoders-nonjson.md). `Encrypters` and `Decrypters` are registered with a `CryptoManager` and are then used at serialization/deserialization time to encrypt and decrypt fields.

Here we'll go through an example of setting up and using the Node Field-Level Encryption library.

To begin we need to create a couple of keys, you should **not** use the `InsecureKeyring` other than for evaluation purposes and should keep your keys secure.

```javascript
Unresolved include directive in modules/howtos/pages/encrypting-using-sdk.adoc - include::example$fle.js[]
```

Now that we have keys we can create a `Provider` (here we use the `AeadAes256CbcHmacSha512` algorithm which is the default supplied by the library). The `Provider` gives us a way to easily create multiple encrypters for the same algorithm but different keys. At this point we also create `CryptoManager` and register our encrypters and decrypters with it.

```javascript
Unresolved include directive in modules/howtos/pages/encrypting-using-sdk.adoc - include::howtos:example$fle.js[]
```

## [](#usage)Usage

Sensitive fields in your data classes can be encrypted by using a `CryptoSchema`. For example:

```javascript
Unresolved include directive in modules/howtos/pages/encrypting-using-sdk.adoc - include::howtos:example$fle.js[]
```

Now let's create a person document and save it to Couchbase:

```javascript
Unresolved include directive in modules/howtos/pages/encrypting-using-sdk.adoc - include::howtos:example$fle.js[]
```

You can get the document to verify the fields were encrypted:

```javascript
Unresolved include directive in modules/howtos/pages/encrypting-using-sdk.adoc - include::howtos:example$fle.js[]
```

The expected output is something like:

```json
{
  firstName: 'Barry',
  lastName: 'Sheen',
  'encrypted$password': {
    alg: 'AEAD_AES_256_CBC_HMAC_SHA512',
    kid: 'mykey',
    ciphertext: 'iO2fCmlRqY5D55j8MemFwhMDIAQ33j8XRpcpFANSXmI7HHmlHUopfu7plkH1K128XDDIbLtcaIM9yghmYNXoYA=='
  },
  'encrypted$addresses': {
    alg: 'AEAD_AES_256_CBC_HMAC_SHA512',
    kid: 'mykey',
    ciphertext: '2T+W+xXVw6TnJJV5fOxpG7WMo26qScROtqc7qjkoSpPrhe4mrCOxfFBFSg8xDzIB/gG+jlWQp8zDWYGIbRVnnoL+sWINdL7Rr7x228fDGjQ4Cu2heqmBkCHueQusuFx1pxo1TLtrUomtqLZB46G3s4WOeg5T4Z9vRfbSwOu9ryf2LVo8rsWf05Vhz5901celbK5L8uX/+HcSULoG2f1C2Qkd5bV/P9ZaO7I9duaUbA0='
  },
  'encrypted$phone': {
    alg: 'AEAD_AES_256_CBC_HMAC_SHA512',
    kid: 'mykey',
    ciphertext: 'M7ao4qp/8t4TKjmHU51xLNSa2h0ydiLfSvzauSfNDfnL/vAxOyYgNsvxMmbX33vMnD6BUe+zGCSo3v8C6fwM7g=='
  }
}
```

Now let's decrypt the person document and output the result.

```javascript
Unresolved include directive in modules/howtos/pages/encrypting-using-sdk.adoc - include::howtos:example$fle.js[]
```

The output is now:

```json
{
  "firstName": "Barry",
  "lastName": "Sheen",
  "password": "bang!",
  "addresses": [
    {
      "houseName": "my house",
      "street": [
        {
          "firstLine": "my street",
          "secondLine": "my second line"
        }
      ]
    },
    {
      "houseName": "my other house"
    }
  ],
  "phone": "123456"
}
```

## [](#migrating-from-2)Migrating from SDK API 2

SDK 2.x reached end-of-life long ago, but should you have fields encrypted by SDK 2.x, and the need to read them from SDK 4.x (or 3.x), then follow the steps in the [archived documents](https://docs-archive.couchbase.com/java-sdk/3.4/howtos/encrypting-using-sdk.html#migration-from-sdk2).

> [!IMPORTANT]
> The encryption algorithms used by SDK 2 are deprecated, and are no longer used for encrypting new data. Do not rely on the security of outdated encryption algorithms.