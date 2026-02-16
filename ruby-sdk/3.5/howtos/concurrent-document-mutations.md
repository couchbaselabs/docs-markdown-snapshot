[View original HTML](/ruby-sdk/3.5/howtos/concurrent-document-mutations.html)

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

```ruby
max_retries = 10
max_retries.times do
  # get the current document contents
  get_result = collection.get("user-id")

  # increment a count on the user
  content = get_result.content
  content["visitCount"] += 1

  begin
    options = Collection::ReplaceOptions.new
    options.cas = get_result.cas
    collection.replace("user-id", content, options)
    break
  rescue Error::CasMismatch
    # ignore CAS mismatch and try again
    # note: any other exception will break the loop
  end
end
```

Sometimes more logic is needed when performing updates, for example, if a property is mutually exclusive with another property; only one or the other can exist, but not both.

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

Unresolved include directive in modules/howtos/pages/concurrent-document-mutations.adoc - include::7.5@sdk:shared:partial$cas.adoc\[\]

```ruby
# lock for two seconds
get_and_lock_result = collection.get_and_lock("user-id", 2)
locked_cas = get_and_lock_result.cas

# an example of simply unlocking the document:
# collection.unlock("user-id", locked_cas)

options = Collection::ReplaceOptions.new
options.cas = get_and_lock_result.cas
collection.replace("user-id", "new value", options)
```

The handler will unlock the item either via an explicit unlock operation (`unlock`) or implicitly via modifying the item with the correct CAS.

If the item has already been locked, the server will respond with CasMismatch which means that the operation could not be executed temporarily, but may succeed later on.