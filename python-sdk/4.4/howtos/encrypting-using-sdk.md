---
title: Encrypting Your Data
description: A practical guide for getting started with Field-Level Encryption,
  showing how to encrypt and decrypt JSON fields using the Python SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.4/modules/howtos/pages/encrypting-using-sdk.adoc
  xref: xref:4.4@python-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.4/howtos/encrypting-using-sdk.html)

# Encrypting Your Data

> A practical guide for getting started with Field-Level Encryption, showing how to encrypt and decrypt JSON fields using the Python SDK. 

For a high-level overview of this feature, see [Field Level Encryption](../concept-docs/encryption.md).

## [](#package)Packaging

The Couchbase Python SDK works together with the [Python Couchbase Encryption](https://github.com/couchbase/python-couchbase-encryption) library to provide support for encryption and decryption of JSON fields. This library makes use of the cryptographic algorithms available on your platform, and provides a framework for implementing your own crypto components.

> [!NOTE]
> The encryption code is packaged as an optional library and is subject to the Couchbase [License](https://www.couchbase.com/LA03012021) and [Enterprise Subscription License](https://www.couchbase.com/ESLA08042020) agreements. To use the encryption library, you have to explicitly include this dependency in your project configuration. Refer to the [install section](#pip-install).

## [](#requirements)Requirements

* Couchbase Python SDK version `3.2.0` or later.
* Python Couchbase Encryption version `1.0.0` or later.

## [](#pip-install)Install

```bash
$ python3 -m pip install cbencryption
```

See the [GitHub repository tags](https://github.com/couchbase/python-couchbase-encryption/tags) for the latest version.

## [](#configuration)Configuration

The Python Field-Level Encryption library works on the principle of `Encrypters` and `Decrypters` which can be packaged within a `Provider`. `Encrypters` and `Decrypters` are registered with a `CryptoManager` and are then used to encrypt and decrypt specified fields.

Here we'll go through an example of setting up and using the Python Field-Level Encryption library.

To begin we need to create a couple of keys, you should **not** use the `InsecureKeyring` other than for evaluation purposes and should keep your keys secure.

```python
keyring = InsecureKeyring()
secret_key_id = "secret_key"
keyring.set_key(
    secret_key_id,
    bytes.fromhex(
        "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f"
    ),
)
secret_key1_id = "secret_key1"
keyring.set_key(
    secret_key1_id,
    bytes.fromhex(
        "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f"
    ),
)
```

Now that we have keys we can create a `Provider` (here we use the `AeadAes256CbcHmacSha512` algorithm which is the default supplied by the library). The `Provider` gives us a way to easily create multiple encrypters for the same algorithm but different keys. At this point we also create `CryptoManager` and register our encrypters and decrypters with it.

```python
# AES-256 authenticated with HMAC SHA-512. Requires a 64-byte key.
aes256_provider = AeadAes256CbcHmacSha512Provider(keyring)

# Create a CryptoManager
crypto_mgr = DefaultCryptoManager()

# Create and then register encrypters.
# The secret_key_id is used by the encrypter to lookup the key from the store when encrypting a document.
# The id of the Key object returned from the store at encryption time is written into the data for the field to be encrypted.
# The key id that was written is then used on the decrypt side to find the corresponding key from the store.
encrypter1 = aes256_provider.encrypter_for_key(secret_key_id)

# The alias used here is the value which corresponds to the "encrypted" field annotation.
try:
    crypto_mgr.register_encrypter("one", encrypter1)
    crypto_mgr.register_encrypter(
        "two", aes256_provider.encrypter_for_key(secret_key1_id)
    )

    # We don't need to add a default encryptor but if we do then any fields with an
    # empty encrypted tag will use this encryptor.
    crypto_mgr.default_encrypter(encrypter1)
except EncrypterAlreadyExistsException as ex:
    traceback.print_exc()

# Only set one decrypter per algorithm.
# The crypto manager will work out which decrypter to use based on the alg field embedded in the field data.
# The decrypter will use the key embedded in the field data to determine which key to fetch from the key store for decryption.
try:
    crypto_mgr.register_decrypter(aes256_provider.decrypter())
except DecrypterAlreadyExistsException as ex:
    traceback.print_exc()
```

## [](#usage)Usage

Once an `CryptoManager` has registered encrypters and decrypters, encryption/decryption of specified fields can be handled with helper methods. For example, the methods below take a `CryptoManager`, the document that should have specified fields encrypted/decrypted and a list of field specs specifing the needed information in order to encrypt/decrypt fields in the document.

```python
# Create a helper method to encrypt document fields
def encrypt_doc(
    crypto_mgr,  # type: "CryptoManager"
    doc,  # type: Dict
    field_specs,  # type: List[dict]
) -> dict:
    """Helper method that takes the provided field specs and encrypts the matching fields of the provided document.

    Args:
        crypto_mgr (`couchbase.encryption.CryptoManager`): The crypto manager that contains registries to application's encrypters and decrypters
        doc (Dict): The document that should have fields encrypted
        field_specs (List[dict]): List of field specs, a field spec should be a dict containing at least a 'name' field.  Can optionally
            include 'encrypter_alias' and 'associated_data' fields

    Returns:
        Dict: The provided document with encrypted fields
    """
    encrypted_doc = {}
    for k, v in doc.items():
        field_spec = next((fs for fs in field_specs if fs.get("name", None) == k), None)
        if field_spec:
            encrypted_val = crypto_mgr.encrypt(
                json.dumps(v),
                encrypter_alias=field_spec.get("encrypter_alias", None),
                associated_data=field_spec.get("associated_data", None),
            )
            encrypted_val["ciphertext"] = encrypted_val["ciphertext"].decode("utf-8")
            encrypted_doc[crypto_mgr.mangle(k)] = encrypted_val
        else:
            encrypted_doc[k] = v
    return encrypted_doc


# Create a helper method to decrypt document fields
def decrypt_doc(
    crypto_mgr,  # type: "CryptoManager"
    doc,  # type: Dict
    field_specs,  # type: List[dict]
) -> dict:
    """Helper method that takes the provided field specs and decrypts the matching fields of the provided document.

    Args:
        crypto_mgr (`couchbase.encryption.CryptoManager`): The crypto manager that contains registries to application's encrypters and decrypters
        doc (Dict): The document that should have fields encrypted
        field_specs (List[dict]): List of field specs, a field spec should be a dict containing at least a 'name' field.  Can optionally
            include 'encrypter_alias' and 'associated_data' fields

    Returns:
        Dict: The provided document with previously encrypted fields decrypted.
    """
    decrypted_doc = {}
    for k, v in doc.items():
        if not crypto_mgr.is_mangled(k):
            decrypted_doc[k] = v
        else:
            demangled_key = crypto_mgr.demangle(k)
            field_spec = next(
                (fs for fs in field_specs if fs.get("name", None) == demangled_key),
                None,
            )
            if field_spec:
                decrypted_val = crypto_mgr.decrypt(
                    v,
                    associated_data=field_spec.get("associated_data", None),
                )
                decrypted_doc[demangled_key] = json.loads(decrypted_val)
    return decrypted_doc
```

Next, create a document and a list of field specs specifying which fields in the document should be encrypted. Then, save the encrypted document returned by the encryption helper method to Couchbase.

```python
user = {
    "firstName": "Monty",
    "lastName": "Python",
    "password": "bang!",
    "address": {
        "street": "999 Street St.",
        "city": "Some City",
        "state": "ST",
        "zip": "12345",
    },
    "phone": "123456",
}

field_specs = [
    {"name": "password", "encrypter_alias": "one"},
    {"name": "address", "encrypter_alias": "two"},
    {"name": "phone"},
]

encrypted_user = encrypt_doc(crypto_mgr, user, field_specs)

collection.upsert("user::1", encrypted_user)
```

Retrieving the document from couchbase and displaying the document, as seen below, should output something like the following.

```python
result = collection.get("user::1")
print("Encrypted doc:\n{}".format(result.content_as[dict]))
```

```json
{
    "firstName": "Monty",
    "lastName": "Python",
    "encrypted$password":
    {
        "alg": "AEAD_AES_256_CBC_HMAC_SHA512",
        "kid": "secret_key",
        "ciphertext": "QnXBcTA3P1p5WFfH+2kJbrKy2iSKCwxZZgbnJzrxy1dnh2TLloBxwJZ13UFZZmtGZf2F3whTnoj/60Q9zOQvbA=="
    },
    "encrypted$address":
    {
        "alg": "AEAD_AES_256_CBC_HMAC_SHA512",
        "kid": "secret_key1",
        "ciphertext": "bt6fGSwf7buX49+ddHlVnJjLkauVRgSSF4/VdEdOlIZ7xHwtVXsQCFpvz7XqEhzQho57m5YJQWR/oC1kjQlZZMFyPaXGhS4Mku7K1x2duZucjSDxmch4fkdcm6SZsb/UE9bfLCf2F9g8oKJzrkyjlFhR4+3h8H4JtxuOn/3xpyQLoVTbHTWgO0WMDHULdLb1"
    },
    "encrypted$phone":
    {
        "alg": "AEAD_AES_256_CBC_HMAC_SHA512",
        "kid": "secret_key",
        "ciphertext": "723JCAusPFm1kaWLnOkZRjNBFMM9mCORwPntk4s/4RIOCmv0DJ4gTwEiUy8XNewvUa44MzkMG7IW5SyWB4qFZw=="
    }
}
```

Passing the document with encrypted fields to the decryption helper, as in the example below, should provide the decrypted document and the output should look something like the following.

```python
decrypted_user = decrypt_doc(crypto_mgr, result.content_as[dict], field_specs)
print("Decrypted doc:\n{}".format(decrypted_user))
```

```json
{
    "firstName": "Monty",
    "lastName": "Python",
    "password": "bang!",
    "address":
    {
        "street": "999 Street St.",
        "city": "Some City",
        "state": "ST",
        "zip": "12345"
    },
    "phone": "123456"
}
```

## [](#migration-from-sdk2)Migrating from SDK 2

> [!WARNING]
> SDK 2 cannot read fields encrypted by SDK 3\.

It's inadvisable to have both the old and new versions of your application active at the same time. The simplest way to migrate is to do an offline upgrade during a scheduled maintenance window. For an online upgrade without downtime, consider a [blue-green deployment](https://en.wikipedia.org/wiki/Blue-green%5Fdeployment).

SDK 3 requires additional configuration to read fields encrypted by SDK 2\. The rest of this section describes how to configure Field-Level Encryption in SDK 3 for backwards compatibility with SDK 2.

### [](#configure-field-name-prefix)Changing the field name prefix

In SDK 2, the default prefix for encrypted field names was `__crypt_`. This caused problems for Couchbase Sync Gateway, which does not like field names to begin with an underscore. In SDK 3, the default prefix is `encrypted$`.

For compatibility with SDK 2, you can configure the `CryptoManager` to use the old `__crypt_` prefix:

```python
prefix = "__crpyt_"
mgr = DefaultCryptoManager(encrypted_field_prefix=prefix)
```

Alternatively, you can [rename the existing fields using a SQL++ (formerly N1QL) statement](https://forums.couchbase.com/t/replacing-field-name-prefix/28786).

> [!WARNING]
> In SDK 2, only top-level fields could be encrypted. SDK 3 allows encrypting fields at any depth. If you decide to rename the existing fields, make sure to do so _before_ writing any encrypted fields below the top level, otherwise it may be difficult to rename the nested fields using a generic SQL++ statement.

### [](#configure-legacy-decrypters)Enabling decrypters for legacy algorithms

The encryption algorithms used by SDK 2 are deprecated, and are no longer used for encrypting new data. To enable decrypting fields written by SDK 3, register the legacy decrypters with the `CryptoManager`:

```python

# The register_legacy_decrypters() method takes a function parameter so that the single decrypter 
# can support multiple keys. The function accepts a public key name and returns the 
# corresponding private key name.
crypto_mgr.register_legacy_decrypters(
    keyring, lambda key: "myhmackey" if key == "mypublickey" else None
)
```