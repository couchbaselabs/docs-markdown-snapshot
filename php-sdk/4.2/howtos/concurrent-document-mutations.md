---
title: Concurrent Document Mutations
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/howtos/pages/concurrent-document-mutations.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.2@php-sdk:howtos:concurrent-document-mutations.adoc[]
---

[View original HTML](/php-sdk/4.2/howtos/concurrent-document-mutations.html)

# Concurrent Document Mutations

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

```php
function incrementVisitCount(Collection $collection, string $userId) {
    $maxRetries = 10;
    for ($i = 0; $i < $maxRetries; $i++) {
        // Get the current document contents
        $res = $collection->get($userId);

        // Increment the visit count
        $user = $res->content();
        $user["visit_count"]++;

        try {
            // Attempt to replace the document using CAS
            $opts = new ReplaceOptions();
            $opts->cas($res->cas());
            $collection->replace($userId, $user, $opts);
        } catch (CasMismatchError $ex) {
            continue;
        }

        // If no errors occured during the replace, we can exit our retry loop
        return;
    }
    printf("Replace failed after %d attempts\n", $maxRetries);
}
```

Sometimes more logic is needed when performing updates, for example, if a property is mutually exclusive with another property; only one or the other can exist, but not both.

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

```php
    $res = $collection->getAndLock($userId, 2 /* seconds */);
    $lockedCas = $res->cas();

    /* // an example of simply unlocking the document:
     * $collection->unlock($userId, $lockedCas);
     */

    // Increment the visit count
    $user = $res->content();
    $user["visit_count"]++;

    $opts = new ReplaceOptions();
    $opts->cas($lockedCas);
    $collection->replace($userId, $user, $opts);
```

The handler will unlock the item either via an explicit unlock operation (`unlock`) or implicitly via modifying the item with the correct CAS.

If the item has already been locked, the server will respond with CasMismatch which means that the operation could not be executed temporarily, but may succeed later on.