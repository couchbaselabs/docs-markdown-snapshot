[View original HTML](/go-sdk/2.10/howtos/encrypting-using-sdk.html)

> A practical guide for getting started with Field-Level Encryption, showing how to encrypt and decrypt JSON fields using the Go SDK. 

For a high-level overview of this feature, see [Field Level Encryption](../concept-docs/encryption.md).

## [](#package)Packaging

The Go SDK works together with the [Go Couchbase Encryption](https://github.com/couchbase/gocbencryption) library to provide support for encryption and decryption of JSON fields. This library makes use of the cryptographic algorithms available on your platform, and provides a framework for implementing your own crypto components.

|  | The encryption code is packaged as an optional library and is subject to the Couchbase [License](https://www.couchbase.com/LA03012021) and [Enterprise Subscription License](https://www.couchbase.com/ESLA08042020) agreements. To use the encryption library, you have to explicitly include this dependency in your project configuration. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

To get started with the Go encryption library you can fetch it using:

```console
$ go get github.com/couchbase/gocbencryption/v2.0.0
```

## [](#configuration)Configuration

The Go Field-Level Encryption library works on the principle of `Encrypters` and `Decrypters` which can be packaged within a `Provider`, as well as a custom [Transcoder](transcoders-nonjson.md). `Encrypters` and `Decrypters` are registered with a `CryptoManager` and are then used at serialization/deserialization time to encrypt and decrypt annotated fields.

Here we’ll go through an example of setting up and using the Go Field-Level Encryption library.

To begin we need to create a couple of keys, you should **not** use the `InsecureKeyring` other than for evaluation purposes and should keep your keys secure.

```golang
	keyB := []byte{0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
		0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
		0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c, 0x2d, 0x2e, 0x2f,
		0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x3f, 0x3f, 0x3f, 0x3f, 0x3d, 0x3e, 0x3f,
	}
	key1 := gocbfieldcrypt.Key{
		ID:    "mykey",
		Bytes: keyB,
	}
	key2 := gocbfieldcrypt.Key{
		ID:    "myotherkey",
		Bytes: keyB,
	}

	// Create an insecure keyring and add two keys.
	keyring := gocbfieldcrypt.NewInsecureKeyring()
	keyring.Add(key1)
	keyring.Add(key2)
```

Now that we have keys we can create a `Provider` (here we use the `AeadAes256CbcHmacSha512` algorithm which is the default supplied by the library). The `Provider` gives us a way to easily create multiple encrypters for the same algorithm but different keys. At this point we also create `CryptoManager` and register our encrypters and decrypters with it.

```golang
	// Create a provider.
	// AES-256 authenticated with HMAC SHA-512. Requires a 64-byte key.
	provider := gocbfieldcrypt.NewAeadAes256CbcHmacSha512Provider(keyring)

	// Create the manager and add the providers.
	mgr := gocbfieldcrypt.NewDefaultCryptoManager(nil)

	// We need to create and then register encrypters.
	// The keyID here is used by the encrypter to lookup the key from the store when encrypting a document.
	// The key.ID returned from the store at encryption time is written into the data for the field to be encrypted.
	// The key ID that was written is then used on the decrypt side to find the corresponding key from the store.
	keyOneEncrypter := provider.EncrypterForKey(key1.ID)

	// We register the providers for both encryption and decryption.
	// The alias used here is the value which corresponds to the "encrypted" field annotation.
	err := mgr.RegisterEncrypter("one", keyOneEncrypter)
	if err != nil {
		panic(err)
	}

	err = mgr.RegisterEncrypter("two", provider.EncrypterForKey(key2.ID))
	if err != nil {
		panic(err)
	}

	// We don't need to add a default encryptor but if we do then any fields with an
	// empty encrypted tag will use this encryptor.
	err = mgr.DefaultEncrypter(keyOneEncrypter)
	if err != nil {
		panic(err)
	}

	// We only set one decrypter per algorithm.
	// The crypto manager will work out which decrypter to use based on the `alg` field embedded in the field data.
	// The decrypter will use the key embedded in the field data to determine which key to fetch from the key store for decryption.
	err = mgr.RegisterDecrypter(provider.Decrypter())
	if err != nil {
		panic(err)
	}
```

Now we can create a `Transcoder` using our `CryptoManager`. Once created we need to register the `Transcoder` with the SDK.

```golang
	// Create our transcoder, not setting a base transcoder will cause it to fallback to the
	// SDK JSON transcoder.
	transcoder := gocbfieldcrypt.NewTranscoder(nil, mgr)

	// Register the encryption transcoder with the SDK.
	opts := gocb.ClusterOptions{
		Authenticator: authenticator,
		Transcoder:    transcoder,
	}
	cluster, err := gocb.Connect("localhost", opts)
	if err != nil {
		panic(err)
	}
```

## [](#usage)Usage

Once an encryption transcoder has been registered then encryption/decryption will be performed on annotated fields transparently.

Sensitive fields in your data classes can be "annotated" using the `encrypted` tag. For example:

```golang
type PersonAddress struct {
	HouseName  string `json:"houseName" encrypted:"one"`
	StreetName string `json:"streetName"`
}

type Person struct {
	FirstName string          `json:"firstName"`
	LastName  string          `json:"lastName"`
	Password  string          `json:"password" encrypted:"one"`
	Addresses []PersonAddress `json:"address" encrypted:"two"`

	Phone string `json:"phone" encrypted:"two"`
}
```

Now let’s create a person document and save it to Couchbase:

```golang
	bucket := cluster.Bucket("travel-sample")
	collection := bucket.Scope("inventory").Collection("airport")

	person := Person{
		FirstName: "Barry",
		LastName:  "Sheen",
		Password:  "bang!",
		Addresses: []PersonAddress{
			{
				HouseName:  "my house",
				StreetName: "my street",
			},
			{
				HouseName:  "my other house",
				StreetName: "my other street",
			},
		},
		Phone: "123456",
	}

	_, err = collection.Upsert("p1", person, nil)
	if err != nil {
		panic(err)
	}
```

You can get the document as a `map[string]interface{}` to verify the fields were encrypted:

```golang
	res, err := collection.Get("p1", nil)
	if err != nil {
		panic(err)
	}

	var resData map[string]interface{}
	err = res.Content(&resData)
	if err != nil {
		panic(err)
	}

	fmt.Printf("%+v\n", resData)
```

Because decoding as a `map` does not decrypt anything, the expected output is something like:

```none
map[
    address:map[
        encrypted$houseName:map[alg:AEAD_AES_256_CBC_HMAC_SHA512 ciphertext:Uh1WE0VSkjZoc4x9xITQ0sHm1eGqJszzv7/YuvLapGOjmSHj3+DNsTYKylKyhZMeDW6zosmm+F7qV+OO6+1WFg== kid:mykey]
        streetName:my street
    ]
    encrypted$password:map[alg:AEAD_AES_256_CBC_HMAC_SHA512 ciphertext:C2l9bJKjnDpgaOUh4R0+SKAPE8WjFoxR8BvIolpB9w467yEspmZmqXcTCHkFk29O1F8sac9V9asb1lWS0ZgI3w== kid:mykey]
    firstName:Barry
    lastName:Sheen
    encrypted$phone:map[alg:AEAD_AES_256_CBC_HMAC_SHA512 ciphertext:N2HpOioi3bm4Q9s0H4aon9NX1QO+7ZKs4DkEfy2ExeuVrMCfb14wrq3kpN7BfOOWo7YnFUt/kx/xgJEv2cOFDw== kid:myotherkey]
]
```

Now let’s read the person document using the data binding.

```golang
	personRes, err := collection.Get("p1", nil)
	if err != nil {
		panic(err)
	}

	var personResData Person
	err = personRes.Content(&personResData)
	if err != nil {
		panic(err)
	}

	fmt.Printf("%+v\n", personResData)
```

The output is now:

```none
{FirstName:Barry LastName:Sheen Password:bang! Address:{HouseName:my house StreetName:my street} Phone:123456}
```

## [](#migration-from-sdk1)Migrating from SDK 1

|  | SDK 1 cannot read fields encrypted by SDK 2\. |
|  | --------------------------------------------- |

It’s inadvisable to have both the old and new versions of your application active at the same time. The simplest way to migrate is to do an offline upgrade during a scheduled maintenance window. For an online upgrade without downtime, consider a [blue-green deployment](https://en.wikipedia.org/wiki/Blue-green%5Fdeployment).

SDK 2 requires additional configuration to read fields encrypted by SDK 1\. The rest of this section describes how to configure Field-Level Encryption in SDK 2 for backwards compatibility with SDK 1.

### [](#configure-field-name-prefix)Changing the field name prefix

In SDK 1, the default prefix for encrypted field names was `__crypt_`. This caused problems for Couchbase Sync Gateway, which does not like field names to begin with an underscore. In SDK 2, the default prefix is `encrypted$`.

For compatibility with SDK 1, you can configure the `CryptoManager` to use the old `__crypt_` prefix:

```golang
	mgr := gocbfieldcrypt.NewDefaultCryptoManager(&gocbfieldcrypt.DefaultCryptoManagerOptions{
		EncryptedFieldPrefix: "__crypt",
	})
```

Alternatively, you can [rename the existing fields using a SQL++ statement](https://forums.couchbase.com/t/replacing-field-name-prefix/28786).

|  | In SDK 1, only top-level fields could be encrypted. SDK 2 allows encrypting fields at any depth. If you decide to rename the existing fields, make sure to do so _before_ writing any encrypted fields below the top level, otherwise it may be difficult to rename the nested fields using a generic SQL++ statement. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#configure-legacy-decrypters)Enabling decrypters for legacy algorithms

The encryption algorithms used by SDK 1 are deprecated, and are no longer used for encrypting new data. To enable decrypting fields written by SDK 1, register the legacy decrypters with the `CryptoManager`:

```golang
	// NewLegacyAes256CryptoDecrypter takes a function parameter so that the single decrypter can support multiple
	// keys. The function accepts a public key name and returns the corresponding private key name.
	decrypter := gocbfieldcrypt.NewLegacyAes256CryptoDecrypter(keyring, func(s string) (string, error) {
		if s == "mykey" {
			return "myhmackey", nil
		}

		return "", errors.New("unknown key")
	})
	err := mgr.RegisterDecrypter(decrypter)
	if err != nil {
		panic(err)
	}
```