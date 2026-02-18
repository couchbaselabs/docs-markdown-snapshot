---
title: Custom Filters
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-custom-filters.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-custom-filters.html)

# Custom Filters

Custom filters can be viewed and modified from the index’s configuration page under the Index Settings section. Any custom filters that are configured for the current index can be viewed by expanding the Custom Filters panel. If no custom filters have been configured for the index, the Custom Filters panel will be empty.

## [](#add-custom-filter)Add Custom Filter

To add a custom filter to a Full Text Index via the Couchbase Capella UI, the following permissions are required:

You must have the `Project View` privileges for the project that contains the cluster.

You must have a database user associated with your organization’s user account. The database user must have Read/Write permissions for the bucket on which the index was created.

The 'Custom Filters' panel shows no existing custom filters.

The following four options are provided:

### [](#character-filter)Character Filter

Adds a new character filter to the list of those available. The new filter becomes available for inclusion in custom-created analyzers.

Left-click the **\+ Add Character Filter**. It displays the **Custom Character Filter** dialog:

![fts custom character filter dialog initial](_images/fts-custom-character-filter-dialog-initial.png) 

The following interactive fields are provided:

* **Name**: A suitable, user-defined name for the new character filter.
* **Type**: The type of filtering to be performed. Available options can be accessed from the pull-down menu to the right of the field. (Currently, only `regexp` is available.)
* **Regular Expression**: The specific _regular expression_ that the new character filter is to apply. Character-strings that match the expression will be affected; others will not.
* **Replacement**: The replacement text that will be substituted for each character-string match returned by the regular expression. If no replacement text is specified, the matched character-string will be omitted.

The following completed fields define a character filter for deleting leading whitespace:

![fts custom character filter dialog filled](_images/fts-custom-character-filter-dialog-filled.png) 

When saved, the new character filter is displayed on its own row, with options for further editing and deleting:

![fts custom filters panel new character filter](_images/fts-custom-filters-panel-new-character-filter.png) 

### [](#tokenizer)Tokenizer

Adds a new tokenizer to the list of those available.

The new tokenizer becomes available for inclusion in custom-created analyzers.

Left-click the **\+ Add Tokenizer**. It displays the **Custom Tokenizer** dialog:

![fts custom filters tokenizer dialog initial](_images/fts-custom-filters-tokenizer-dialog-initial.png) 

The following interactive fields are provided:

* **Name**: A suitable, user-defined name for the new tokenizer.
* **Type**: The process used in tokenizing. Available options can be accessed from the pull-down menu to the right of the field. (Currently, `regexp` and `exception` are available.)
* **Regular Expression**: The specific _regular expression_ used by the tokenizing process.

The following completed fields define a tokenizer that removes uppercase characters:

![fts custom filters tokenizer dialog completed](_images/fts-custom-filters-tokenizer-dialog-completed.png) 

When saved, the new tokenizer is displayed on its own row, with options for further editing and deleting:

![fts custom filters panel new tokenizer](_images/fts-custom-filters-panel-new-tokenizer.png) 

### [](#token-filter)Token filter

Adds a new token filter to the list of those available. The new token filter becomes available for inclusion in custom-created analyzers.

Left-click the **\+ Add Token Filter**. It displays the **Custom Token Filter** dialog:

![fts custom filters token filter dialog initial](_images/fts-custom-filters-token-filter-dialog-initial.png) 

The following interactive fields are provided:

* **Name**: A suitable, user-defined name for the new token filter.
* **Type**: The type of post-processing to be provided by the new token filter. The default is `length`, which creates tokens whose minimum number of characters is specified by the integer provided in the **Min** field and whose maximum by the integer provided in the **Max**. Additional post-processing types can be selected from the pull-down menu at the right of the field:  
![fts custom filters token filter types](_images/fts-custom-filters-token-filter-types.png)  
> [!NOTE]  
> The type-selection determines which interactive fields appear in the **Custom Token Filter** dialog, following **Name** and **Type**. The pull-down menu displays a list of available types. For descriptions, see the section [Token Filters](fts-index-analyzers.md#Token-Filters), on the page [Understanding Analyzers](fts-index-analyzers.md#Understanding-Analyzers).
* **Min**: The minimum length of the token, in characters. Note that this interactive field is displayed for the `length` type, and may not appear, or be replaced, when other types are specified. The default value is 3.
* **Max**: The maximum length of the token, in characters. Note that this interactive field is displayed for the `length` type and may not appear, or be replaced when other types are specified. The default value is 255.

The following completed fields define a token filter that restricts token-length to a minimum of 3, and a maximum of 255 characters:

![fts custom filters token filter dialog complete](_images/fts-custom-filters-token-filter-dialog-complete.png) 

When saved, the new token filter is displayed on its own row, with options for further editing and deleting:

![fts custom filters panel new token filter](_images/fts-custom-filters-panel-new-token-filter.png) 

### [](#wordlist)Wordlist

Adds a list of words to be removed from the current search.

Left-click the **\+ Add Word List**. It displays the **Custom Word List** dialog

![fts custom wordlist dialog initial](_images/fts-custom-wordlist-dialog-initial.png) 

To create a custom word list, first, type a suitable name into the **Name** field. Then, add words by typing each individually into the field that bears the placeholder text, `word to be added`.

After each word has been added, left-click on the **\+ Add** button, on the lower-right. The word is added to the central **Words** panel.

Continue adding as many words as are required.

For example:

![fts custom wordlist dialog complete](_images/fts-custom-wordlist-dialog-complete.png) 

To remove a word, select the word within the **Words** panel and left-click on the **Remove** button.

To save, left-click on **Save**. The new word list is displayed on its own row, with options for further editing and deleting:

![fts custom filters panel new word list](_images/fts-custom-filters-panel-new-word-list.png)