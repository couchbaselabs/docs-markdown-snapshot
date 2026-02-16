[View original HTML](/cloud/tutorials/java-tutorial/tutorial-troubleshooting.html)

> This page addresses errors you might come across when following the Student Record System tutorial. 

## [](#authentication-error)Authentication Error

If you get an authentication error when running Maven commands in your console, confirm that the username and password in your Java file matches the username and password in your cluster access credentials.

If they do not match, you can edit the Java file to add the correct username or password and try compiling and running the Maven command again.

## [](#unknown-host-exception)Unknown Host Exception

If you get an `UnknownHostException` error in your console, go to your Java file and confirm that the public connection string is correct for your operational cluster.

## [](#other-build-errors)Other Build Errors

For any other build errors in your console, run `mvn install` and try the original command again.