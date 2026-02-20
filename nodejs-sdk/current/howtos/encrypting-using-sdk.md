---
title: Encrypting Your Data
description: A practical guide for getting started with Field-Level Encryption,
  showing how to encrypt and decrypt JSON fields using the Node.js SDK.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.6/modules/howtos/pages/encrypting-using-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:nodejs-sdk:howtos:encrypting-using-sdk.adoc[]
---

[View original HTML](/nodejs-sdk/current/howtos/encrypting-using-sdk.html)

# Encrypting Your Data

> A practical guide for getting started with Field-Level Encryption, showing how to encrypt and decrypt JSON fields using the Node.js SDK. 

For a high-level overview of this feature, see our [Encryption](../concept-docs/encryption.md) page.

> [!TIP]
> Native Encryption at Rest
> 
> Server 8.x (and new Capella Operational clusters) offer [encryption at rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md). It’s a comprehensive way of encrypting all data in a non-ephemeral bucket, as well as logs, configuration data, and audit data. However, you may prefer the relative simplicity of key management in Field Level Encryption for use cases where there are a limited number of data to be encrypted.

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

Here we’ll go through an example of setting up and using the Node Field-Level Encryption library.

To begin we need to create a couple of keys, you should **not** use the `InsecureKeyring` other than for evaluation purposes and should keep your keys secure.

```javascript
  const keyBuffer = Buffer.from(
    '000102030405060708090a0b0c0d0e0f' +
      '101112131415161718191a1b1c1d1e1f' +
      '202122232425262728292a2b2c2d2e2f' +
      '303132333435363738393a3b3c3d3e3f',
    'hex'
  ) // output in string format: 123456789:;<=>?

  const key1 = new keyring.Key('mykey', keyBuffer)
  const key2 = new keyring.Key('myotherkey', keyBuffer)

  // Create an insecure keyring and add two keys.
  const insecureKeyring = new keyring.InsecureKeyring(key1, key2)
```

Now that we have keys we can create a `Provider` (here we use the `AeadAes256CbcHmacSha512` algorithm which is the default supplied by the library). The `Provider` gives us a way to easily create multiple encrypters for the same algorithm but different keys. At this point we also create `CryptoManager` and register our encrypters and decrypters with it.

```javascript
  // Create a provider.
  // AES-256 authenticated with HMAC SHA-512. Requires a 64-byte key.
  const provider = new aesprovider.AeadAes256CbcHmacSha512Provider(
    insecureKeyring
  )

  // Create the manager and add the providers.
  const mgr = new crypto.DefaultCryptoManager()

  // We need to create and then register encrypters.
  // The key ID here is used by the encrypter to lookup the key from the store when encrypting a document.
  // The key ID returned from the store at encryption time is written into the data for the field to be encrypted.
  // The key ID that was written is then used on the decrypt side to find the corresponding key from the store.
  const keyOneEncrypter = provider.encrypterForKey(key1.id)
  const keyTwoEncrypter = provider.encrypterForKey(key2.id)

  // We register the providers for both encryption and decryption.
  // The alias used here is the value which corresponds to the "encryptionKey" field property
  // in the CryptoSchema.
  mgr.registerEncrypter('one', keyOneEncrypter)
  mgr.registerEncrypter('two', keyTwoEncrypter)

  // We don't need to add a default encryptor but if we do then any fields with an
  // empty encryption key will use this encryptor.
  mgr.defaultEncrypter(keyOneEncrypter)

  // We only set one decrypter per algorithm.
  // The crypto manager will work out which decrypter to use based on the `alg` field embedded in the field data.
  // The decrypter will use the key ID embedded in the field data to determine which key to fetch from the key store for decryption
  mgr.registerDecrypter(provider.decrypter())
```

## [](#usage)Usage

Sensitive fields in your data classes can be encrypted by using a `CryptoSchema`. For example:

```javascript
// CryptoSchema is used to register which fields to apply the encryption to.
const schema = mgr.newCryptoSchema({
  fields: {
    password: {
      encryptionKey: 'one',
    },
    addresses: {
      fields: {
        houseName: {
          encryptionKey: 'one',
        },
        street: {
          fields: {
            secondLine: {
              encryptionKey: 'two',
            },
          },
        },
        attributes: {
          fields: {
            action: {
              encryptionKey: 'two',
            },
          },
        },
      },
      encryptionKey: 'two',
    },
    phone: {
      encryptionKey: '',
    },
  },
})
```

Now let’s create a person document and save it to Couchbase:

```javascript
  const person = {
    firstName: 'Barry',
    lastName: 'Sheen',
    password: 'bang!',
    addresses: [
      {
        houseName: 'my house',
        street: [
          {
            firstLine: 'my street',
            secondLine: 'my second line',
          },
        ],
      },
      {
        houseName: 'my other house',
      },
    ],
    phone: '123456',
  }

  const encryptedDoc = schema.encrypt(person)
  await collection.upsert('p1', encryptedDoc)
```

You can get the document to verify the fields were encrypted:

```javascript
const result = await collection.get('p1')
const resData = result.content
console.log(JSON.stringify(resData, null, '  '))
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

Now let’s decrypt the person document and output the result.

```javascript
const decryptedDoc = schema.decrypt(encryptedDoc)
console.log(JSON.stringify(decryptedDoc, null, '  '))
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