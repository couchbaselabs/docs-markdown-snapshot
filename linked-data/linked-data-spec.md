# JSON-LD on Couchbase Docs site

I'd like to look at adding JSON-LD metadata to this repo, which contains an export of the Couchbase docs site.

We'd like to eventually get a graph that maps:

* each article in this export
* the concepts that they are related to
* using standard ontologies where possible
* but defining a limited number of Couchbase specific ontologies where needed

## Avoiding the ontology committee paralysis

We are not tring to model Couchbase in excruciating detail.
That's an admirable goal, but here, we're looking for a Good Enough mapping, that will be help us do useful things.

In particular, I want to be able to answer this sort of competency question:

* What versions and editions support this feature?
* What SDK methods perform the same operations?
* Which privileges are required?
* Which service implements this operation?
* What replaced this deprecated setting?
* Which examples apply to Capella only?
* What changed between Server 7.6 and 8.0?

And to support this kind of use-case:

* Generate a list of "related pages" for a page for contextual navigation
* Get a list of key concepts, to generate a Glossary of interesting terms
* Draft a list of synonyms of key terms, for improving our Algolia search configuration

Any concept, or ontological relationship should only be added if it can be mapped to a useful competency question.

## A first pass

We could start with around 100 documents, drawn primarily from the
server/current/ and cloud/ trees, focusing on a starter topic, such as
indexing.

As the pages are already linked with Markdown xrefs, we could of course
bring in pages from other areas, especially where doing so lets us test
the competency questions we've collated.

We could create a top-level directory in this repo called /linked-data or
similar in which to store pages about e.g. concepts, products, and ontologies.

We should also document, in Markdown, a summary of the 3rd party ontologies
we've used, and what competency questions we're using (from the initial list,
and ones that we discover during the process).

### Technical notes

The /current/ versions map on the website to the same URL as the latest version:
e.g. these 2 pages are identical:

  https://docs.couchbase.com/server/current/getting-started/start-here.html
  https://docs.couchbase.com/server/8.0/getting-started/start-here.html

You'd assume therefore that these markdown summaries were also identical:

  https://docs.couchbase.com/server/current/getting-started/start-here.md
  https://docs.couchbase.com/server/8.0/getting-started/start-here.md

but that is currently broken, oops, sorry.
I'll deal with that (it'll be an nginx or Cloudfront tweak).
In the meantime, treat them as identical, and log any technical concerns: if we need to
normalize these to the versioned number in future, we'll handle that.

## Some thoughts about updating

Once we have a POC, we could think about updating every time this snapshot is updated.
Obviously at this point, the ontologies should be considered more stable.
An LLM should now update only content as standard.
To modify any ontology, they would raise a PR, which would justify the change to a human
reviewer "This new mapping would answer competency question X, and I notice that pages 
P,Q,R,S are currently working around it using a suboptimal notation."
