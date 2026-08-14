# Candidate FAQs (draft, mechanically generated)

14 candidates generated from 801 relation instances across the current extractions/ tree (145 pages, 3 rounds). See generate_candidates.py's docstring for scope and caveats.

**None of these are verified or ready to publish.** Each answer is a verbatim evidence quote captured at extraction time, not checked against the current live page. Treat this as a demonstration of what a full pass could surface, not a content deliverable.

## What privilege do I need to use Authentication?

> Couchbase uses Role Base Access Control (RBAC), and has since Server 5.0 was released. For a general overview of Couchbase-Server authorization, see [Authorization]. For a list of available roles and corresponding privileges, see [Roles].

Grounded in: `extractions/java-sdk/howtos/sdk-authentication.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/what-privilege-do-i-need-to-use-authentication`

## What privilege do I need to use Create Index?

> To perform query index operations, the provided user must either be an _Admin_ or assigned the _Query Manage Index_ role. See the [Roles](../../../server/current/learn/security/roles.md#query-manage-index) page for more information.

Grounded in: `extractions/java-sdk/howtos/provisioning-cluster-resources.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/what-privilege-do-i-need-to-use-create-index`

## Does Client Settings require Enterprise Edition, or is it available in Community Edition too?

> Set this to `true` to encrypt all communication between the client and server using TLS. This feature requires the Enterprise Edition of Couchbase Server.

Grounded in: `extractions/java-sdk/ref/client-settings.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/does-client-settings-require-enterprise-edition-or-is-it-available-in-`

## Does Certificate Authentication require Enterprise Edition, or is it available in Community Edition too?

> Couchbase Server supports the use of X.509 certificates to authenticate clients (only available in the Enterprise Edition, not the Community Edition).

Grounded in: `extractions/java-sdk/howtos/sdk-authentication.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/does-certificate-authentication-require-enterprise-edition-or-is-it-av`

## Which version introduced Full Text Searching With SDK?

> Note that this feature is only supported with Couchbase Server 7.0 or later. [Collections in Search queries]

Grounded in: `extractions/java-sdk/howtos/full-text-searching-with-sdk.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/which-version-introduced-full-text-searching-with-sdk`

## Which version introduced Scoped Vs Global Search Indexes?

> This is because the Search Service supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

Grounded in: `extractions/java-sdk/howtos/full-text-searching-with-sdk.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/which-version-introduced-scoped-vs-global-search-indexes`

## Can I use Create Bucket with Cluster Access Credentials?

> You cannot execute this statement using cluster access credentials.

Grounded in: `extractions/cloud/n1ql/n1ql-language-reference/createbucket.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/can-i-use-create-bucket-with-cluster-access-credentials`

## Can I use Revoke with Cluster Access Credentials?

> You cannot execute this statement using cluster access credentials.

Grounded in: `extractions/cloud/n1ql/n1ql-language-reference/revoke.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/can-i-use-revoke-with-cluster-access-credentials`

## Should I use Ldap Authentication or Certificate Authentication?

> If LDAP is enabled, Couchbase Server will only allow PLAIN sasl authentication which by default, for good security, the SDK will not allow ... the secure solution is [to use TLS](managing-connections.md#ssl).

Grounded in: `extractions/java-sdk/howtos/sdk-authentication.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/should-i-use-ldap-authentication-or-certificate-authentication`

## Should I use View Queries With SDK or Sqlpp Queries With SDK?

> Views are the only service which does not benefit from Multi-Dimensional Scaling, and is rarely the best choice over, say, [our Query service](sqlpp-queries-with-sdk.md) if you are starting a fresh application.

Grounded in: `extractions/java-sdk/howtos/view-queries-with-sdk.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/should-i-use-view-queries-with-sdk-or-sqlpp-queries-with-sdk`

## Are User and RBAC User related?

> Sync Gateway users and roles have no relationship to Couchbase Server's RBAC (Role-based Access Control) users. They are created and operate solely within the Sync Gateway ecosphere to govern access to replication data and to the Public API.

Grounded in: `extractions/sync-gateway/access-control/access-control-concepts.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/are-user-and-rbac-user-related`

## What's the difference between All Documents Channel and All Channels Wildcard?

> This channel should not be confused with the use of the All Channels Wildcard in access grants.

Grounded in: `extractions/sync-gateway/access-control/access-control-concepts.json` (1 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/what-s-the-difference-between-all-documents-channel-and-all-channels-w`

## What Capella role do I need to use Hyperscale Vector Index?

> Your account must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner), [Project Owner](../projects/project-roles.md#project-owner-role), or [Data Writer](../projects/project-roles.md#project-cluster-data-reader-writer) role to be able to create an index.

Grounded in: `extractions/cloud/vector-index/hyperscale-vector-index.json` (3 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/what-capella-role-do-i-need-to-use-hyperscale-vector-index`

## What Capella role do I need to use Composite Vector Index?

> Your account must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner), [Project Owner](../projects/project-roles.md#project-owner-role), or [Data Writer](../projects/project-roles.md#project-cluster-data-reader-writer) role to be able to create an index.

Grounded in: `extractions/cloud/vector-index/composite-vector-index.json` (3 instance(s)) - `https://docs.couchbase.com/ld/candidate-faqs/what-capella-role-do-i-need-to-use-composite-vector-index`

