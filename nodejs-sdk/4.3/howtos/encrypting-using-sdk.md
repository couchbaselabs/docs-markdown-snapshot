---
title: Encrypting Your Data
description: A practical guide for getting started with Field-Level Encryption,
  showing how to encrypt and decrypt JSON fields using the Node.js SDK.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.3/modules/howtos/pages/encrypting-using-sdk.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:4.3@nodejs-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.3/howtos/encrypting-using-sdk.html)

# Encrypting Your Data

> A practical guide for getting started with Field-Level Encryption, showing how to encrypt and decrypt JSON fields using the Node.js SDK. 

For a high-level overview of this feature, see our [Encryption](../concept-docs/encryption.md) page.

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

> [!WARNING]
> SDK API 2 (used in Node.js SDK 2._x_) cannot read fields encrypted by SDK API 3 (used in Node.js SDK 3._x_ and 4._x_). Learn more about [migrating from SDK API 2 to SDK API 3](../project-docs/migrating-sdk-code-to-3.n.md).

It’s inadvisable to have both the old and new versions of your application active at the same time. The simplest way to migrate is to do an offline upgrade during a scheduled maintenance window. For an online upgrade without downtime, consider a [blue-green deployment](https://en.wikipedia.org/wiki/Blue-green%5Fdeployment).

SDK API 3 requires additional configuration to read fields encrypted by SDK API 2\. The rest of this section describes how to configure Field-Level Encryption in SDK API 3 for backwards compatibility with SDK API 2.

### [](#changing-the-field-name-prefix)Changing the field name prefix

In SDK API 2, the default prefix for encrypted field names was `__crypt_`. This caused problems for Couchbase Sync Gateway, which does not like field names to begin with an underscore. In SDK API 3, the default prefix is `encrypted$`.

For compatibility with SDK API 2, you can configure the `CryptoManager` to use the old `__crypt_` prefix:

```javascript
const mgr = new crypto.DefaultCryptoManager({
  encryptedFieldPrefix: '__crypt_',
})
```

Alternatively, you can [rename the existing fields using a SQL++ (formerly N1QL) statement](https://forums.couchbase.com/t/replacing-field-name-prefix/28786).

> [!WARNING]
> In SDK API 2, only top-level fields could be encrypted. SDK API 3 allows encrypting fields at any depth. If you decide to rename the existing fields, make sure to do so _before_ writing any encrypted fields below the top level, otherwise it may be difficult to rename the nested fields using a generic SQL++ statement.

### [](#enabling-decrypters-for-legacy-algorithms)Enabling decrypters for legacy algorithms

The encryption algorithms used by SDK API 2 are deprecated, and are no longer used for encrypting new data. To enable decrypting fields written by SDK API 2, register the legacy decrypters with the `CryptoManager`:

```javascript
  const decrypter = new legacyaesdecrypter.LegacyAes256Decrypter(
    insecureKeyring,
    (publicKey) => {
      if (publicKey == 'mykey') {
        return 'myhmackey'
      }

      throw Error('unknown key')
    }
  )

  mgr.registerDecrypter(decrypter)
```