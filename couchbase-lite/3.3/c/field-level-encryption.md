---
title: Field Level Encryption
description: Client-side Field Level Encryption on Couchbase Lite C Clients
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/c/pages/field-level-encryption.adoc
  xref: xref:3.3@couchbase-lite:c:field-level-encryption.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/c/field-level-encryption.html)

# Field Level Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

> [!CAUTION]
> Community Edition
> 
> * The push replicator will detect encryptable values inside a document. It will fail to replicate unencrypted encryptable values with a crypto error.
> * The pull replicator will **not** detect encryptable values inside pulled documents. The document will be saved as it was received. This **may** include Server SDK encrypted fields

## [](#overview)Overview

Couchbase Lite for C 3.0.0 supports client-side, field-Level encryption on replications, allowing applications to encrypt/decrypt sensitive fields in documents using an encryption framework of choice.

Using the new client-side encryption capability, Couchbase Lite C applications can designate selected fields for encryption and have the client automatically handle the encryption and-or decryption at property level during the replication.

Only clients with access to the correct encryption keys can decrypt and read the protected data.

The client-side encryption is compatible with the Couchbase server SDK field-level encryption format — see, for example, <https://docs.couchbase.com/python-sdk/current/concept-docs/encryption.html#format>

## [](#encryptable-type)Encryptable Type

The API includes a `CBLEncryptable` type, representing an encryptable value to be automatically encrypted/decrypted the replicator — see [Example 1](#ex-encryptable-type).

You declare properties requiring encryption by the replicator, as a dictionary with the structure shown in [Example 1](#ex-encryptable-type).

Example 1\. Encryptable-type Dictionary Structure

```c
{
  "@type": "encryptable",
  “value” : <Decrypted Value>
} (1)

{
  "@type": "encryptable",
  “ciphertext”: <Encrypted Value in BASE64 String>
} (2)
```

The key for the value can be either of the following:

| **1** | Use value as the key when storing a decrypted value, which can be any type (string, number, boolean, dictionary, array or null). |
| ----- | -------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Use cyphertext as the key when storing a encrypted value, which must be a BASE-64 String.                                        |

## [](#replicator-decryption)Replicator Decryption

Pull replication detects `encryptable` values before saving them to the local database and decrypts them using the property decryption callback function — see: [Decryption](#lbl-decryption-callback) for more on the decryption callback function.

On successful decryption the replicator saves the property in encryptable dictionary format (removing the `encrypted$` prefix) — see: [Example 1](#ex-encryptable-type).

## [](#replicator-encryption)Replicator Encryption

Push replication detects `encryptable` values before pushing them to the remote database and encrypts them using the property encryption callback function — see: [Encryption](#lbl-encryption-callback).

On successful encryption the replicator transforms the property into a format compatible with Couchbase Server SDK — see: [Example 3](#ex-server-encryptable).

## [](#server-sdk-compatibility)Server SDK compatibility

Couchbase Lite's replicator ensures compatibility with Server SDK's field level. Both Push and Pull replication transform Couchbase Lite's encryptable dictionary to-and-from Server SDK Encrypted Field dictionary structure — see: [Example 3](#ex-server-encryptable).

Push replicator

* Adds the prefix `encrypted$` to the key.
* Sets the SDK'\` `alg` either to a user-specified algorithm name or the default `CB_MOBILE_CUSTOM`.
* Set the value's key as `ciphertext`
* Stores the encrypted value as a BASE64 string.  
Example 2\. Stored Encryptable  
```c  
{  
    “alg”: <User-Specified or CB_MOBILE_CUSTOM>,  
    “ciphertext” : <Encrypted Value in BASE64 String>  
}  
```

Pull replicator

* Detects encrypted encryptable values by looking for dictionary keys prefixed with "encrypted$".
* Transforms the dictionary by:

  * Removing `alg`
  * Replacing the `ciphertext` key with the `value`
  * Storing the decrypted key/value in [CBLEncryptable](#ex-encryptable-type) format

Example 3\. Server SDK Encrypted Field Structure

Server SDK's field (property) level encryption uses key mangling, by add a prefix to the field name (`encrypted$`). Its directory structure differs CBL's encryptable dictionary when serializing the encrypted fields; as shown here.

```c
{
    encrypted$mykey: {
        “alg” : “AEAD_AES_256_CBC_HMAC_SHA512”, (1)
        “kid” : “my-key-id”,
        “ciphertext”: “<BASE64-TEXT>”
    }
}
```

| **1** | Here alg identifies the encryption algorithm and is the only required field. |
| ----- | ---------------------------------------------------------------------------- |

## [](#callback-definition)Callback Definition

### [](#lbl-encryption-callback)Encryption

Provide an encryption callback function [CBLPropertyEncryptor](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#gab116a23be8bd24b86349379f370ef60c) to encrypt encryptable properties during replication.

After encryption the FLSliceResult is released and the returned value zeroed. See [Example 4](#ex-get-att) for an example encryptor callback function.

If you return a null slice the replicator will fail and log a crypto error message.

### [](#lbl-decryption-callback)Decryption

Provide a decryption callback function [CBLPropertyDecryptor](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga24a60a3d6f9816e1d32464cc31a15c0c) to decrypt any encryptable properties. After decryption the FLSliceResult is released and the returned value zeroed. See [Example 4](#ex-get-att) for an example decryptor callback function.

If you return a null slice without an error the replicator skips and saves the property as received.

If you return a null slice with an error the replicator logs the error and does not replicate the document.

Example 4\. Simple Encryption-Decryption Callback

```C
// Purpose: Declare property-level encryptor callback functions
static FLSliceResult my_cipher_function(FLSlice input) {
    FLSliceResult result = FLSliceResult_New(input.size);
    for(int i = 0; i < input.size; ++i) {
        ((uint8_t*)(result.buf))[i] = ((uint8_t*)input.buf)[i] ^ 'K';}
    return result;
}


static FLSliceResult property_encryptor(void* context, FLString docID, FLDict props, FLString path,
                                        FLSlice input, FLStringResult* algorithm, FLStringResult* keyID, CBLError* error) {
    *algorithm = FLSlice_Copy(FLSTR("MyEnc"));
    return my_cipher_function(input);
}


static FLSliceResult property_decryptor(void* context, FLString documentID, FLDict properties, FLString keyPath,
                                        FLSlice input, FLString algorithm, FLString keyID, CBLError* error) {
    return my_cipher_function(input);
}
```

## [](#callback-configuration)Callback Configuration

You register the callback function for use by declaring them in the replicator configuration using [propertyEncryptor()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#ab731bf9f140158d6967c1af645d8744a) and-or [propertyDecryptor()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#ab6a0d9e0830755d284039018a09c27d6) — see: [Example 5](#ex-callback-config)

If you do not provide an encryption callback:

* The push replicator always detects encrypted encryptable values in a document and will fail the document replication, flagging a crypto error.
* The pull replicator does **not** detect encrypted encryptables in pulled documents and will save documents as received; this could include SDK encrypted field dictionaries.

Example 5\. Simple Callback Replicator Configuration

```C
// Purpose: Declare property-level encryptor callback functions
static FLSliceResult my_cipher_function(FLSlice input) {
    FLSliceResult result = FLSliceResult_New(input.size);
    for(int i = 0; i < input.size; ++i) {
        uint8_t*)(result.buf[i] = uint8_t*)input.buf)[i] ^ 'K';}     return result; }   static FLSliceResult property_encryptor(void* context, FLString docID, FLDict props, FLString path,                                         FLSlice input, FLStringResult* algorithm, FLStringResult* keyID, CBLError* error) {     *algorithm = FLSlice_Copy(FLSTR("MyEnc";
    return my_cipher_function(input);
}


static FLSliceResult property_decryptor(void* context, FLString documentID, FLDict properties, FLString keyPath,
                                        FLSlice input, FLString algorithm, FLString keyID, CBLError* error) {
    return my_cipher_function(input);
}

    // Purpose: Show how to declare en(de)cryptors in replicator config
    // NOTE: No error handling, for brevity (see getting started)

    CBLError err{};
    FLString url = FLSTR("ws://localhost:4984/db");
    CBLEndpoint* target = CBLEndpoint_CreateWithURL(url, &err);

    CBLReplicationCollection collectionConfig;
    memset(&collectionConfig, 0, sizeof(CBLReplicationCollection));
    collectionConfig.collection = collection;

    CBLReplicatorConfiguration replConfig;
    memset(&replConfig, 0, sizeof(CBLReplicatorConfiguration));
    replConfig.collectionCount = 1;
    replConfig.collections = &collectionConfig;
    replConfig.endpoint = target;
    replConfig.propertyEncryptor = property_encryptor; (1)
    replConfig.propertyDecryptor = property_decryptor; (2)

    CBLReplicator* replicator = CBLReplicator_Create(&replConfig, &err);
    CBLEndpoint_Free(target);

    CBLReplicator_Start(replicator, false);
```

## [](#querying-encryptables)Querying Encryptables

Encrypted values can be queried — see [Example 6](#ex-query). The query result of an encryptable value is `CBLEncryptable`

CBLEncryptable exposes a _value_ property for query purposes. If this value is encrypted the query will return _MISSING_.

Example 6\. A Simple encryptable Query

```nql
SELECT  ssn,  (1)
        ssn.value  (2)
FROM db WHERE ssn.value = "123-45-6789"
```

| **1** | The returned ssn column is in the form of an encryptable dictionary                                              |
| ----- | ---------------------------------------------------------------------------------------------------------------- |
| **2** | The returned ssn.value column is the actual value, unless it is still encrypted in which case it returns MISSING |

## [](#constraints)Constraints

### [](#nesting)Nesting

In the case of nested `encryptable` types, the replicator only encrypts the outer `encryptable`.

### [](#arrays)Arrays

For compatibility with Server SDKS, encryptables are not supported within arrays.

The push replicator should detect and report an error if an encrypted property is found in an array.

### [](#blobs)Blobs

Encrypting blob's content is not supported.

Where a Blob as a Fleece dictionary is specified in the encrypted property value, only the dictionary is encrypted; **not** the blob's content.

### [](#delta-sync)Delta Sync

Delta Sync will be disabled and a warning message logged when `propertyEncryption` is configured.

### [](#brute-force-susceptibility)Brute-Force Susceptibility

Any document with simple encrypted fields (for example, fields containing a subset of values) may be brute-force computed with all possible values using the document revId. This will be fixed in a future release. In the meantime, adding an encrypted field including a nonce or random value to the document can mitigate against such brute-force computation — as shown in [Example 7](#example-brute-force-mitigation).

Example 7\. Sample brute-force mitigation code

```C
void secureRandomize(void *bytes, size_t count) {
    // This sample code uses Apple’s Common Crypto API to generate a secure random bytes.
    CCRandomGenerateBytes(bytes, count);
}
```

```C
…

auto doc = CBLDocument_CreateWithID("doc1"_sl);
FLMutableDict props = CBLDocument_MutableProperties(doc);

// Create a random bytes in base64:
uint8_t nonceBuf[64];
secureRandomize(nonceBuf, sizeof(nonceBuf));
FLValue nonceValue = FLValue_NewData({nonceBuf, sizeof(nonceBuf)});
FLSliceResult nonceBase64 = FLValue_ToJSON(nonceValue);
FLValue_Release(nonceValue);

// Create an encryptable value from the random bytes and add to the document’s property:
auto nonce = CBLEncryptable_CreateWithString({nonceBase64.buf, nonceBase64.size});
FLMutableDict_SetEncryptableValue(props, "nonce"_sl, nonce);

…

// Save doc:
CBLError error;
CHECK(CBLDatabase_SaveDocument(db, doc, &error));

// Release:
CBLDocument_Release(doc);
FLSliceResult_Release(nonceBase64);
CBLEncryptable_Release(nonce);
```

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](#c:gs-prereqs.adoc)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.