[View original HTML](/server/7.2/fts/fts-advanced.html)

Advanced settings can be specified in the **Advanced** panel. When opened, the Advanced panel appears as follows:

![fts advanced panel](_images/fts-advanced-panel.png) 

The Advanced panel provides the following options:

## [](#default-type)Default Type

The default type for documents in the selected bucket or scope and collection. The default value for this field is `default`.

## [](#default-analyzer)Default Analyzer

This is the default analyzer to be used. The default value is `standard`.

The default analyzer is applicable to all the text fields across type mappings unless explicitly overridden.

It is the _standard_ analyzer in which analysis is done by the means of the Unicode tokenizer, the to\_lower token filter, and the stop token filter.

## [](#default-datetime-parser)Default Date/Time Parser

This is the default date/time parser to be used.

The default datetime parser is applicable to all the datetime fields across the type mappings unless explicitly overridden.

The default value is `dateTimeOptional`.

## [](#default-field)Default Field

Indexed fields need to have this option selected to support `include in _all`, where \_all is the composite field.

The default value is `_all`.

## [](#store-dynamic-fields)Store Dynamic Fields

This option, when selected, ensures the inclusion of field content in returned results. Otherwise, the field content is not included in the result.

## [](#index-dynamic-fields)Index Dynamic Fields

This option, When selected, ensures that the dynamic fields are indexed. Otherwise, the dynamic fields are not indexed.

## [](#docvalues-for-dynamic-fields)DocValues for Dynamic Fields

This option, When selected, ensures that the values of the dynamic fields are included in the index. Otherwise, the dynamic field values are not included in the index.