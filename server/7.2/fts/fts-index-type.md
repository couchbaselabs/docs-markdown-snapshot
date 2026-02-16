[View original HTML](/server/7.2/fts/fts-index-type.html)

The **Index Type** interface provides a drop-down menu from which the appropriate index type can be selected:

![fts index type interface](_images/fts-index-type-interface.png) 

Following options are available:

* **Version 5.0 (Moss)** is the standard form of index to be used in test, development, and production. This version is deprecated.
* **Version 6.0 (Scorch)** reduces the size of the index-footprint on disk and provides enhanced performance for indexing and mutation-handling

|  | The type of an index is saved in its JSON definition, which can be previewed in the _Index Definition Preview panel_, at the right-hand side. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#example)Example

Version 5.0 contained the following value for the store attribute:

```Javascript
"store": {
  "kvStoreName": "mossStore"
},
```

Version 6.0 and later contains a different value:

```javascript
"store": {
  "kvStoreName": "",
  "indexType": "scorch"
},
```