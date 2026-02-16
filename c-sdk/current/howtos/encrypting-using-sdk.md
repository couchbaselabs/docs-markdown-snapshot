[View original HTML](/c-sdk/current/howtos/encrypting-using-sdk.html)

> Fields within a document can be securely encrypted by the SDK, to support FIPS-140-2 compliance. 

Field Level Encryption is normally carried out at a higher level than _libcouchbase_ (LCB). It is not available directly in LCB.

If this is a requirement, we suggest considering a migration to the [C++](../../../cxx-sdk/current/hello-world/overview.md) SDK, which includes [Field Level Encryption](../../../cxx-sdk/current/howtos/encrypting-using-sdk.md).

Alternately, take a look at Capella Operational and self-managed Couchbase Server’s [Native Encryption at Rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md) feature.