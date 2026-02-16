[View original HTML](/server/current/search/default-character-filters-reference.html)

> Character filters remove unwanted characters from your search input. 

You can use a [character filter](customize-index.md#character-filters) when you [create a custom analyzer](create-custom-analyzer.md). Choose a default character filter or [create your own](create-custom-character-filter.md).

The following default character filters are available:

| Character Filter    | Description                                                                                                                                                                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| asciifolding        | The analyzer converts any characters that aren’t in the Basic Latin Unicode block to their ASCII equivalent. This means the filter converts any alphabetic, numeric, or symbol characters that aren’t in the first 127 ASCII characters. For example, the character filter converts á to a. |
| html                | The analyzer removes all HTML tags from search input. For example, the character filter removes the <p> tags from indexed content, but keeps the text inside the <p> tag.                                                                                                                   |
| zero\_width\_spaces | The analyzer replaces zero-width non-joiner spaces with regular space characters. Zero-width non-joiner spaces are unicode characters that interrupt [ligatures](https://en.wikipedia.org/wiki/Ligature%5F%28writing%29)(joins between characters) in text formatting.                      |