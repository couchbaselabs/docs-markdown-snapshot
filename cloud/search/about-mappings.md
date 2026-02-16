[View original HTML](/cloud/search/about-mappings.html)

> The Search Service has distinct mapping types for collections, objects, and fields in a Search index. 

Mappings control the specific documents and fields that you can return in a [Search query](run-searches.md).

You can create the following types of mappings:

* [Collection Mappings](#collections)
* [Object Mappings](#objects)
* [Child Field Mappings](#fields)
* [XATTRs Mappings](#xattrs)

When you create a new mapping, you need to choose whether you want a [Static or Dynamic Mapping](#static-vs-dynamic).

## [](#collections)Collection Mappings

The mapping for a collection is also called a type mapping.

A type mapping includes or excludes specific documents in a collection from an index. A document must match the collection and document type set by a type mapping to be included in a Search index.

You can also choose to control the type of a document by [setting a type identifier](set-type-identifier.md). A type identifier is an optional configuration that tells the Search Service how to interpret a document’s type. Only documents that pass the filter from your type identifier can be included in your Search index under a specific type mapping, and potentially returned in search results.

Type mappings can be [Static mappings](#static) or [Dynamic mappings](#dynamic). Add [Object Mappings](#objects) and [Child Field Mappings](#fields) to make a collection type mapping a static mapping.

For more information about how to create a type mapping, see [Create a New Mapping or Type Mapping](create-type-mapping.md).

### [](#collection-type-mapping-names)Collection Type Mapping Names

The Search Service uses periods (`.`) to separate collection names from [type identifiers](customize-index.md#type-identifiers). If you add a period to the name of your collection type mapping, the Search Service would interpret anything after the period as a filter value.

For example, if you wanted to include the following document in your Search index, with a `type` value of `shorthair`:

```json
{
  "type": "shorthair",
  "name": "British Shorthair",
  "category": "shorthaired",
  "origin": {
    "country": "United Kingdom",
    "region": "Great Britain"
  },
  "physicalCharacteristics": {
    "coatLength": "short",
    "coatTexture": "dense",
    "commonColors": [
      "blue",
      "black",
      "white",
      "cream",
      "silver"
    ],
    "eyeColors": [
      "copper",
      "gold",
      "blue",
      "green"
    ],
    "averageWeightKg": {
      "male": 6.5,
      "female": 5.0
    }
  },
  "temperament": [
    "calm",
    "affectionate",
    "independent",
    "gentle"
  ],
  "energyLevel": "moderate",
  "intelligence": "high",
  "lifespanYears": {
    "min": 12,
    "max": 17
  },
  "careRequirements": {
    "groomingFrequency": "weekly",
    "sheddingLevel": "moderate",
    "healthNotes": [
      "prone to obesity if overfed",
      "can be predisposed to hypertrophic cardiomyopathy"
    ]
  },
  "goodWith": {
    "children": true,
    "otherCats": true,
    "dogs": true
  },
  "description": "The British Shorthair is a sturdy, round-faced cat known for its plush coat and easygoing personality. It is affectionate without being overly demanding and adapts well to indoor living."
}
```

If you used a collection type mapping called `cat.breeds` and used the default **JSON type field** type identifier, the Search Service would only include documents that had a value of `breeds` in their `type` field. That means that the British Shorthair document would not match the type mapping, and would not be included in the Search index.

## [](#objects)Object Mappings

Use an object mapping to add a nested JSON object from your documents to your Search index.

For example, you would use an object mapping to add the `origin` object and its child fields to your Search index:

```json
{
  "type": "shorthair",
  "name": "British Shorthair",
  "category": "shorthaired",
  "origin": {
    "country": "United Kingdom",
    "region": "Great Britain"
  },
```

Like [Collection Mappings](#collections), object mappings can be [static](#static) or [dynamic](#dynamic). You can add [Child Field Mappings](#fields) to make an object mapping a static type mapping.

### [](#object-names)Object Names

Avoid using an object name that contains a period (`.`) in a Search index object mapping.

The Search Service uses periods to maintain object and child field relationships after flattening. For example, the `country` and `region` fields inside the `origin` object would be represented as `origin.country` and `origin.region` inside your Search index:

```json
{
  "type": "shorthair",
  "name": "British Shorthair",
  "category": "shorthaired",
  "origin": {
    "country": "United Kingdom",
    "region": "Great Britain"
  },
```

If you created a mapping for a field called `origin.country` as well as a `country` field mapping inside the `origin` object, the Search Service creates a single field index for both fields. If you tried to query `origin.country` in a Search query with an analyzer, the Search Service would fail to pick the right analyzer for the `origin.country` field because of the 2 overlapping mappings. This can cause undesired or unexpected search results.

To avoid issues with overlapping field and object names in a Search index, do not use periods (`.`) in your JSON document field or object names.

## [](#fields)Child Field Mappings

Use a child field mapping to add a specific document field from your documents to your Search index.

A child field mapping can exist at the top-level of your document hierarchy and be created directly under a [collection type mapping](#collections), or it can exist as a nested field underneath an [object mapping](#objects) or [XATTRs mapping](#xattrs).

Use a child field mapping to turn a parent mapping into a static mapping.

For example, you could create a child field mapping for the `type`, `name`, and `category` fields underneath the collection type mapping for this document. You could also create a child field mapping under the object mapping for the `origin` object for the `country` and `region` fields:

```json
{
  "type": "shorthair",
  "name": "British Shorthair",
  "category": "shorthaired",
  "origin": {
    "country": "United Kingdom",
    "region": "Great Britain"
  },
```

Just like [Object Names](#object-names), to avoid undesired results in your Search queries, avoid using periods (`.`) in your child field names. See [Object Names](#object-names) for examples and an explanation.

## [](#xattrs)XATTRs Mappings

|  | You can only use XATTRs mappings in the Advanced Mode editor. |
|  | ------------------------------------------------------------- |

Extended Attributes (XATTRs) mappings add fields and metadata from your document’s XATTRs and let you query them inside a Search index.

XATTRs mappings can be [static](#static) or [dynamic](#dynamic), based on whether you add [Child Field Mappings](#fields).

Just like [Object Names](#object-names) and [Child Field Mappings](#fields), to avoid undesired results in your Search queries, avoid using periods (`.`) in the names of fields in your document metadata. See [Object Names](#object-names) for examples and an explanation.

## [](#static-vs-dynamic)Choosing a Static or Dynamic Mapping

Each mapping type can be either **static** or **dynamic**:

Static mappings

When your data fields are stable and unlikely to change, use a static type mapping to add and define only specific fields from a matching document type to an index. If you’re unsure about your document structure and how it might change, use [Dynamic mappings](#dynamic), instead.

For example, you could create a static type mapping to only include the contents of the `description` field from the `cats` collection in your Search index, as a text field with an `en` analyzer.

Add [Child Field Mappings](#fields) to a [collection type mapping](#collections), [object mapping](#objects), or [XATTRs mapping](#xattrs) to make it static.

Dynamic mappings

When you do not know the structure of your data fields ahead of time, use a dynamic type mapping to add all available fields from a matching document type, collection, or JSON object to an index. If your document structure is more stable and unlikely to change, use [Static mappings](#static) to get the best results from the Search Service.

For example, you could create a dynamic type mapping to include all documents from a `cats` collection in your Search index, or include all fields under the `careRequirements` object from a document schema.

## [](#see-also)See Also

* [Set a Document Filter](set-type-identifier.md)
* [Create a New Mapping or Type Mapping](create-type-mapping.md)