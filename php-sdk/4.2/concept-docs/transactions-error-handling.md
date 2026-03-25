---
title: Error Handling
description: Handling transaction errors with Couchbase.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/concept-docs/pages/transactions-error-handling.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:4.2@php-sdk:concept-docs:transactions-error-handling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.2/concept-docs/transactions-error-handling.html)

# Error Handling

> Handling transaction errors with Couchbase. 

Couchbase transactions will attempt to resolve many errors for you, through a combination of retrying individual operations and the application’s lambda. This includes some transient server errors, and conflicts with other transactions.

## [](#transaction-errors)Transaction Errors

There can be situations where total failure is indicated to the application via errors. These situations include:

* Any error thrown by a transaction lambda, either deliberately or through an application logic bug.
* Attempting to insert a document that already exists.
* Calling `ctx.get()` on a document key that does not exist (if the resultant error is not caught).

Once one of these errors occurs, the current attempt is irrevocably failed (though the transaction may retry the lambda to make a new attempt). It is not possible for the application to catch the failure and continue (with the exception of `ctx.get()` raising an error). Once a failure has occurred, all other operations tried in this attempt (including commit) will instantly fail.

Transactions, as they are multi-stage and multi-document, also have a concept of partial success or failure. This is signalled to the application through the `TransactionResult.unstagingComplete` property, described later.

There are three errors that transactions can raise to an application:

* `TransactionFailedException`
* `TransactionExpiredException`
* `TransactionCommitAmbiguousException`

### [](#transactionfailedexception-and-transactionexpiredexception)TransactionFailedException and TransactionExpiredException

The transaction definitely did not reach the commit point. `TransactionFailedException` indicates a fast-failure whereas `TransactionExpiredException` indicates that retries were made until the timeout was reached, but this distinction is not normally important to an application and generally `TransactionExpiredException` does not need to be handled individually.

Either way, an attempt will have been made to rollback all changes. This attempt may or may not have been successful, but the results of this will have no impact on the protocol or other actors. No changes from the transaction will be visible, both to transactional and non-transactional actors.

#### [](#handling)Handling

Generally, debugging exactly why a given transaction failed requires review of the logs, so it is suggested that the application log these on failure. The application may want to try the transaction again later. Alternatively, if transaction completion time is not a priority, then transaction timeouts (which default to 15 seconds) can be extended across the board through `TransactionsConfiguration`.

This will allow the protocol more time to get past any transient failures (for example, those caused by a cluster rebalance). The tradeoff to consider with longer timeouts, is that documents that have been staged by a transaction are effectively locked from modification from other transactions, until the timeout has been reached.

Note that the timeout is not guaranteed to be followed precisely. For example, if the application were to do a long blocking operation inside the lambda (which should be avoided), then timeout can only trigger after this finishes. Similarly, if the transaction attempts a key-value operation close to the timeout, and that key-value operation times out, then the transaction timeout may be exceeded.

### [](#transactioncommitambiguousexception)TransactionCommitAmbiguousException

Each transaction has a 'single point of truth' that is updated atomically to reflect whether it is committed.

However, it is not always possible for the protocol to become 100% certain that the operation was successful, before the transaction expires. This potential ambiguity is unavoidable in any distributed system; a classic example is a network failure happening just after an operation was sent from a client to a server. The client will not get a response back and cannot know if the server received and executed the operation.

The ambiguity is particularly important at the point of the atomic commit, as the transaction may or may not have reached the commit point. Couchbase transactions will raise `TransactionCommitAmbiguousException` to indicate this state. It should be rare to receive this error.

If the transaction had in fact successfully reached the commit point, then the transaction will be fully completed ("unstaged") by the asynchronous cleanup process at some point in the future. With default settings this will usually be within a minute, but whatever underlying fault has caused the `TransactionCommitAmbiguousException` may lead to it taking longer.

If the transaction had not in fact reached the commit point, then the asynchronous cleanup process will instead attempt to roll it back at some point in the future.

#### [](#handling-2)Handling

This error can be challenging for an application to handle. As with `TransactionFailedException` it is recommended that it at least writes any logs from the transaction, for future debugging. It may wish to retry the transaction at a later point, or extend transactional timeouts (as detailed above) to give the protocol additional time to resolve the ambiguity.

### [](#transactionresult-unstagingcomplete)TransactionResult.unstagingComplete

This boolean flag indicates whether all documents were able to be unstaged (committed).

For most use-cases it is not an issue if it is false. All transactional actors will still read all the changes from this transaction, as though it had committed fully. The cleanup process is asynchronously working to complete the commit, so that it will be fully visible to non-transactional actors.

The flag is provided for those rare use-cases where the application requires the commit to be fully visible to non-transactional actors, before it may continue. In this situation the application can raise an error here, or poll all documents involved until they reflect the mutations.

If you regularly see this flag false, consider increasing the transaction timeout to reduce the possibility that the transaction times out during the commit.

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