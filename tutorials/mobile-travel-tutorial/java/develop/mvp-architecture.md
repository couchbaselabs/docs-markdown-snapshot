---
title: MVP Architecture
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/java/develop/mvp-architecture.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:tutorials:mobile-travel-tutorial:java/develop/mvp-architecture.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/java/develop/mvp-architecture.html)

# MVP Architecture

## [](#the-model-view-presenter-pattern)The Model-View-Presenter pattern

In our app, we follow the MVP pattern, separating the internal data model, from a passive view through a presenter that handles the logic of our application and acts as the conduit between the model and the view. The v

![java login label](../../_images/java-login-label.png) 

In the project, the code is structured by feature. In _IntelliJ IDEA_ project navigator, your can view the project structure

![java left navigator](../../_images/java-left-navigator.png) 

* `view`: This is where all the view logic resides. For example, the `FlightSearchController` is responsible for the view where one searches for flights.
* `Presenters`: Despite the name, files labelled as `Controllers` are actually `Presenters`. This is where all the business logic resides to fetch and persist data to a web service or the embedded Couchbase Lite database. Views know about the Presenters but presenter doesn’t know about the view. The view just subscribes to updates to the presenter’s model. Views get their presenters via Dependency Injection, as per standard MVP architecture.
* `Model`: The model layer handles the interactions with Couchbase Lite and acts as the DAO layer.

Throughout this tutorial, we will walkthrough the code in the various presenters to showcase different features of the Couchbase Lite API:

* `BookmarksPresenter.java`
* `HotelsPresenter.java`
* `SearchFlightPresenter.java`
* `BookingsPresenter.java`.