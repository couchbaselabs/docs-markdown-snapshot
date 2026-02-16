[View original HTML](/server/7.2/fts/fts-type-mappings-add-child-field-include-term-vectors.html)

When checked, term vectors are included. When unchecked, term vectors are not included.

Term vectors are the locations of terms in a particular field. Certain kinds of functionality (such as highlighting, and phrase search) require term vectors. Inclusion of term vectors results in larger indexes and correspondingly slower index build-times.

## [](#example)Example

![fts type mappings child field termvectors](_images/fts-type-mappings-child-field-termvectors.png) 

|  | "include term vectors" indexes the array positions (locations) of the terms within the field (needed for phrase searching and highlighting). When this checkbox is checked, the resulting index will proportionately increase in size. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |