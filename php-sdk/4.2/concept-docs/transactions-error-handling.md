---
title: Error Handling
description: Handling transaction errors with Couchbase.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/concept-docs/pages/transactions-error-handling.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.2@php-sdk:concept-docs:transactions-error-handling.adoc[]
---

[View original HTML](/php-sdk/4.2/concept-docs/transactions-error-handling.html)

# Error Handling

> Handling transaction errors with Couchbase. 

Unresolved include directive in modules/concept-docs/pages/transactions-error-handling.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

## [](#transaction-errors)Transaction Errors

Unresolved include directive in modules/concept-docs/pages/transactions-error-handling.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/transactions-error-handling.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/transactions-error-handling.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

### [](#full-error-handling-example)Full Error Handling Example

Pulling all of the above together, this is the suggested best practice for error handling:

```php
try {
  $result = $cluster->transactions()->run(
    function (TransactionAttemptContext $ctx) use ($collection, $costOfItem) {
      // ... transactional code here ...
    }
  );

  // The transaction definitely reached the commit point. Unstaging
  // the individual documents may or may not have completed

  if (!$result->unstagingComplete) {
    // In rare cases, the application may require the commit to have
    // completed.  (Recall that the asynchronous cleanup process is
    // still working to complete the commit.)
    // The next step is application-dependent.
  }
} catch (\Couchbase\Exception\TransactionFailedException $e) {
  echo "Transaction did not reach commit point\n";
} catch (\Couchbase\Exception\TransactionCommitAmbiguousException $e) {
  echo "Transaction possibly committed\n";
}
```