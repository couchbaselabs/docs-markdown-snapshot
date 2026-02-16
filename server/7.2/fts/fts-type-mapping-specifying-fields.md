[View original HTML](/server/7.2/fts/fts-type-mapping-specifying-fields.html)

A Full Text Index can be defined not only to include (or exclude) documents of a certain type but also to include (or exclude) specified fields within each of the typed documents.

To specify one or more fields, hover with the mouse cursor over a row in the Type Mappings panel that contains an enabled type mapping. Buttons labeled **edit** and **+** appear:

![fts type mappings ui fields buttons](_images/fts-type-mappings-ui-fields-buttons.png) 

Left-clicking on the **edit** button displays the following interface:

![fts type mappings ui edit](_images/fts-type-mappings-ui-edit.png) 

This allows the mapping to be deleted or associated with a different analyzer.

|  | FTS Indexing does not work for fields having a dot (. or period) in the field name. Users must avoid adding dot (. or period) in the field name. Like using field.name or country.name is not supported. For example, { "database.name": "couchbase"} |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

If the **only index specified fields** checkbox is checked, only fields specified by the user are included in the index.

Left-clicking on the **+** button displays a pop-up that features two options:

![fts type mappings ui field options](_images/fts-type-mappings-ui-field-options.png) 

These options are described in the following sections.

* [Add Child Mapping](fts-type-mappings-add-child-mappings.md)
* [Add Child Field](fts-type-mappings-add-child-field.md)