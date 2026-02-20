---
title: Troubleshooting
description: This page addresses errors you might come across when following the
  Student Record System tutorial.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/tutorials/pages/java-tutorial/tutorial-troubleshooting.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:tutorials:java-tutorial/tutorial-troubleshooting.adoc[]
---

[View original HTML](/server/current/tutorials/java-tutorial/tutorial-troubleshooting.html)

# Troubleshooting

> This page addresses errors you might come across when following the Student Record System tutorial. 

**Authentication error**

If you get an authentication error when running Maven commands in your console, confirm that the username and password in your Java file matches the username and password you used when setting up the Couchbase cluster in your browser.

If they do not match, you can edit the Java file to add the correct username or password and try compiling and running the Maven command again.

**IP address error**

If you get a `DnsSrvLookupFailedEvent` error to specify your IP address in your console, go to your Java file and replace `localhost` with the IP address of your local Couchbase cluster in your browser.

**Other build errors**

For any other build errors in your console, run `mvn install` and try the original command again.