---
title: MVP Architecture
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/android/develop/mvp-architecture.adoc
  xref: xref:tutorials:mobile-travel-tutorial:android/develop/mvp-architecture.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/android/develop/mvp-architecture.html)

# MVP Architecture

## [](#the-model-view-presenter-pattern)The Model-View-Presenter pattern

In our app, we follow the MVP pattern, separating the internal data model, from a passive view through a presenter that handles the logic of our application and acts as the conduit between the model and the view.

![android mvp model](../../_images/android-mvp-model.png) 

In the Android Studio project, the code is structured by feature. You can select the **Android** option in the left navigator to view the files by package.

![android left navigator](../../_images/android-left-navigator.png) 

Each package contains 3 different files:

* `Activity`: This is where all the view logic resides.
* `Presenter`: This is where all the business logic resides to fetch and persist data to a web service or the embedded Couchbase Lite database.
* `Contract`: An interface that the `Presenter` and `Activity` implement.

Throughout this tutorial, we will walkthrough the code in the various presenters to showcase different features of the Couchbase Lite API:

* `BookmarksPresenter.java`
* `HotelsPresenter.java`
* `SearchFlightPresenter.java`
* `BookingsPresenter.java`.