[View original HTML](/php-sdk/current/howtos/transcoders-nonjson.html)

Information on transcoders can be found in the [API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Bucket.html#method%5FsetTranscoder).

> The PHP SDK supports common JSON document requirements out-of-the-box. Custom transcoders provide support for applications needing to perform advanced operations, including supporting non-JSON data. 

The PHP SDK uses the concept of encoder and decoder functions, which are used whenever data is sent to or retrieved from Couchbase Server.

When sending data to Couchbase, the SDK passes the Object being sent to a `encoder`. The `encoder` can either reject the Object as being unsupported, or convert it into an array of bytes and a Common Flag. The Common Flag specifies whether the data is JSON, a non-JSON string, or raw binary data.

On retrieving data from Couchbase, the fetched bytes and Common Flag are passed to a `decoder`. The transcoder converts the bytes into a concrete class (the application specifies the required type) if possible.

|  | Many applications will not need to be aware of encoders and decoders, as the defaults support most standard JSON use cases. The information in this page is only needed if the application has an advanced use-case, likely involving either non-JSON data, or a requirement for a particular JSON serialization library. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#default-behaviour)Default Behaviour

`\Couchbase\defaultEncoder` uses the `json_encode` function for serializing byte arrays from concrete objects. `\Couchbase\defaultDecoder` uses the `json_decode` function for deserializing byte arrays to concrete objects.

On sending data to Couchbase, the encoder function will send Objects to its serializer to convert into a byte array. The serialized bytes are then sent to the Couchbase Server, along with a Common Flag of JSON.

On retrieving data from Couchbase, the decoder function passes the fetched byte array and Common Flag to its serializer to convert into a concrete class.

This table summarizes that information, and this more concise form will be used to describe the other transcoders included in the SDK.

| Item   | Result                | Common Flag |
| ------ | --------------------- | ----------- |
| string | Results of serializer | JSON        |
| Other  | Results of serializer | JSON        |

## [](#passthrutranscoder)PassThruTranscoder

The `\Couchbase\passThruEncoder` allows data to be sent "as is" to the server, applying no serialization. The corresponding `\Couchbase\passThruDecoder` allows data to be read "as is" from the server, applying no serialization. This can be used for reading and writing binary string data which should not have JSON serialization applied. If data is provider to the `passThruEncoder` which is not string data then encoding will fail.

| Item   | Result    | Common Flag |
| ------ | --------- | ----------- |
| string | Raw value | None        |
| Other  | Raw value | None        |

## [](#custom-transcoders)Custom Transcoders

More advanced transcoding needs can be accomplished if the application implements their own encoders and decoders.

### [](#creating-a-custom-transcoder)Creating a Custom Transcoder

Let’s look at a more complex example: storing an image. The encoder function that we will create will be able to handle both image and JSON data allowing it to be used with more than just images. When we store data with this encoder we will use our own custom Common Flags, so the data will not be compatible with other encoder/decoder functions unless they also recognise these custom flags.

First we will create the encoder function:

```php
/*
 * Lets define some custom transcoding functions.  For this example, any
 * image types that are stored will be serialized as a PNG, and all other
 * object types will be encoded as JSON.
 */
function example_encoder($value) {
    if (gettype($value) == 'resource' && get_resource_type($value) == 'gd') {
        // This is am image, lets capture the PNG data!
        ob_start();
        imagepng($value);
        $png_data = ob_get_contents();
        ob_end_clean();

        // Return our bytes and flags
        return array($png_data, CBTE_FLAG_IMG, 0);
    } else {
        // This is an arbitrary type, lets JSON encode it
        $json_data = json_encode($value);

        // Return our bytes and flags
        return array($json_data, CBTE_FLAG_JSON, 0);
    }
}
```

And now create a corresponding decoder function:

```php
function example_decoder($bytes, $flags, $datatype) {
    if ($flags == CBTE_FLAG_IMG) {
        // Recreate our image object from the stored data
        return imagecreatefromstring($bytes);
    } else if ($flags == CBTE_FLAG_JSON) {
        // Simply JSON decode
        return json_decode($bytes);
    } else {
        // Ugh oh...
        return NULL;
    }
}
```

To use these functions with some data we can do the following and our image will be seamlessly stored in Couchbase Server:

```php
/*
 * Create an image to test with
 */
$im = imagecreatetruecolor(300, 50);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 6, 10, 10,  'Couchbase Rocks!', $text_color);

/*
 * Store it in Couchbase.  This should execute our custom encoder.
 */
$options = new UpsertOptions();
$options->encoder('example_encoder'); // Could be any callable.
$collection->upsert('test_image', $im, $options);

/*
 * Now lets retreive it back, it should still be an image thanks to our
 * custom decoder.
 */
$options = new GetOptions();
$options->decoder('example_decoder'); // Could be any callable.
$image_doc = $collection->get('test_image', $options);

/*
 * Output our retrieved document to the browser with a image/png content-type.
 */
header('Content-Type: image/png');
imagepng($image_doc->content());
```

## [](#configuration)Configuration

Configuring transcoders can be done in multiple ways.

### [](#ini-file)INI file

Configuration via the ini file is done using the key `couchbase.encoder.format`. The values allowed are: \* json - will use the `\Couchbase\defaultEncoder` and `\Couchbase\defaultDecoder`\* php - will use the `\Couchbase\passThruEncoder` and `\Couchbase\passThruDecoder`

An additional field of `couchbase.decoder.json_arrays` is also available for use with the `\Couchbase\defaultDecoder`. This field specifies how JSON objects are decoded by `json_decode`:

```php
php > var_dump(json_decode('{"foo": 42}'));
php shell code:1:
class stdClass#1 (1) {
  public $foo =>
  int(42)
}
php > var_dump(json_decode('{"foo": 42}', true));
php shell code:1:
array(1) {
  'foo' =>
  int(42)
}
```

### [](#bucket)Bucket

The `encoder`/`decoder` function pair can be set on the `bucket` to apply to all bucket level operations.

```php
bucket->setTranscoder('\Couchbase\defaultEncoder', '\Couchbase\defaultDecoder')
```

### [](#operation-level)Operation level

Many operations also support specifying an encoder or decoder at the operation level.

```php
$options = new UpsertOptions();
$options->encoder('example_encoder'); // Could be any callable.
$collection->upsert('mydoc', $data, $options);

$options = new GetOptions();
$options->decoder('example_decoder'); // Could be any callable.
$image_doc = $collection->get('mydoc', $options);
```

## [](#further-reading)Further reading

* For _Common flags_, setting the data format used, see the [Data Structures reference](../ref/data-structures.md#common-flags).
* _Format flags_ for ancient SDKs are still available for compatibility, if you are porting a long-lived legacy app. See the [Legacy formats reference](../ref/data-structures.md#legacy-formats).
* If you want to work with binary documents and our Search service, you might like to take a look at <https://github.com/khanium/couchbase-fts-binary>