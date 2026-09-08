# Notes on iiRDS

A technical-writing peer flagged iiRDS (tekom's "intelligent information
Request and Delivery Standard", `http://iirds.tekom.de/iirds#`) as another
overarching technical-documentation vocabulary, alongside the SKOS and
schema.org already used here. This is a record of evaluating it against
`relations/` and `concepts/` — reference only, not a design decision. It
partly answers the open question in README's "What this is not" section
("whether SKOS and schema.org are the full extent of third-party ontology
adoption"), without resolving it in either direction: iiRDS is a real,
relevant standard, but there's no actionable case for pulling it in against
today's corpus.

## What iiRDS is

Namespace `http://iirds.tekom.de/iirds#`, current release 1.2 (Nov 2023),
maintained by the iiRDS Consortium under CC BY-ND 4.0. Around 150 classes and
80 properties, deliberately restricted to RDF/RDFS (the spec says an
extension using OWL DL would not be iiRDS-compliant). It's built for the
content-*delivery* pipeline: information units, renditions, packages,
document/topic types, audience qualifications, party roles/responsibilities,
authoring lifecycle status, product-variant targeting for delivery, part-of
component trees.

## How it relates to SKOS and schema.org

**SKOS: reused, but only its labeling layer, not its data model.** iiRDS's
own RDF/XML vocabulary file (`iirds-skos.rdf`) declares its ~150 classes and
~80 properties as plain `rdf:Class`/`rdf:Property`, then documents each one
with `skos:prefLabel`, `skos:definition`, `skos:altLabel`, `skos:hiddenLabel`
(bilingual EN/DE). It does **not** model its classes as
`skos:Concept`/`skos:ConceptScheme`, and hierarchy (e.g. component trees)
uses iiRDS-specific properties like `has-component`, not `skos:broader`. So
"iiRDS includes SKOS" is true only in the narrow sense that SKOS's annotation
properties are the dictionary format iiRDS wrote its own terms in — it is not
built on the SKOS concept-scheme model the way this POC's own `concepts/`
layer is (e.g. `concepts/cluster-access-credential-type.jsonld`, typed
directly as `skos:ConceptScheme`).

**schema.org: mentioned, not integrated.** The spec lists schema.org
alongside Dublin Core/vCard as a "related initiative" in a
historical/context section, with no subclassing or subproperty relationship.
External mapping in general is done via `rdfs:seeAlso` — the same
reuse-not-mint tool this POC already uses for `relations/see-also.json`.

**Net effect:** iiRDS sits *beside* SKOS and schema.org, not over or under
them. Adopting it wouldn't remove any existing SKOS/schema.org usage here.

## Checked against `relations/` — no strong substitution case

`relations/` are explicitly "minted because no existing vocabulary fit" (per
README) and mostly encode Couchbase product-*behavior* facts — RBAC,
protocols, memory quotas, index behavior, version gating. iiRDS is oriented
at content-*packaging* facts — a different axis. The plausible near-matches
were checked specifically:

- **`requires-role` / `requires-server-role` / `requires-capella-role` /
  `requires-privilege` vs. iiRDS `Role` / `PartyRole` / `has-party-role`** —
  false friend. iiRDS's Role/PartyRole are about *who a document's audience
  is* ("set of connected behaviors, privileges, and obligations associated
  with a party" for authoring/audience targeting), not RBAC/API access
  control. This is the same word-overload trap `requires-role.json`'s own
  note already documents happening *within* Couchbase's own docs (Sync
  Gateway's `requireRole()` sync-function check vs. Server RBAC role vs.
  Capella role — 38 misfiled records in round 13). iiRDS would add a fourth,
  incompatible sense of "role" if pulled in carelessly.
- **`deprecated-in` / `removed-in` / `retained-for-legacy-compatibility` vs.
  iiRDS `ContentLifeCycleStatus` / `ContentLifeCycleStatusValue`** — false
  friend. The actual enum values in iiRDS's RDF file are `InPreparation`,
  `InReview`, `Reviewed`, `Approved`, `Released`, `Withdrawn`, `Deleted` —
  that's an *authoring/publishing workflow* status (is this topic still in
  draft or already released), not a *product feature's*
  deprecation/removal history. Not a fit for these three predicates.
- **`is-variant-of` vs. iiRDS `ProductVariant`** — also not a fit, for a
  different reason. `is-variant-of.json`'s own note defines it as a
  feature/dialect-family relation (e.g. Analytics SQL++ vs. N1QL), not a
  product-SKU/edition relation. iiRDS's `ProductVariant` /
  `relates-to-product-variant` describes named product SKUs for content
  targeting, conceptually closer to `requires-edition` — but no page
  evidence currently needs that framing, so this is a "worth knowing about"
  observation, not an actionable gap.
- **Genuinely fitting but not-yet-needed**, if the POC ever extends into
  content-packaging metadata: `iirds:Qualification` /
  `relates-to-qualification` (audience prerequisite-skill statements, e.g. a
  guide's "Prerequisites" section naming required DBA experience — distinct
  from an RBAC role requirement, and nothing in `relations/` currently
  expresses this) and `iirds:DocumentType` / `TopicType` / `has-topic-type`
  (DITA-like topic typing — concept/task/reference — that could one day
  enrich `pages/*.jsonld` records alongside `schema:TechArticle`). Neither
  has a current extraction to back it, so neither is actionable today under
  the project's own recurrence/competency-question discipline.

## Bottom line

iiRDS is a real, relevant standard for technical documentation, and it does
partly incorporate SKOS (for labeling, not modeling) the way the peer
described. But checked against this POC's actual corpus, it doesn't have an
actionable substitution or supplement case today: the two vocabularies are
answering different questions (product-behavior facts vs. content-packaging
facts), and the two terms that look like matches by name (`Role`,
lifecycle status) mean something different in iiRDS than they do here.

This note is reference only — the "reuse real vocabulary where it genuinely
fits" checklist in `linked-data-reconcile`'s SKILL.md deliberately does not
list iiRDS alongside `rdfs:seeAlso`/`skos:Concept`/`schema:TechArticle`,
since nothing in the corpus currently needs it and adding it there would
imply reconciliation should be checking for it on every round.
