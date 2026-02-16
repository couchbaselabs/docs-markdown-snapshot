[View original HTML](/server/7.2/tutorials/java-tutorial/install-couchbase-java-sdk.html)

> In this tutorial, you’re going to create a skeleton application for interacting with the student database you created previously. 

## [](#prerequisites)Prerequisites

Java is a fairly popular programming language these days, so we’re going to use it to build our student/course application. To keep things as light as possible (this is a tutorial, after all), we’re not going to worry about building a web front end or REST service, just a few methods to read/write our documents to the database.

You will need a few things installed on your machine before you begin:

* The Java Software Development Kit (version 8+)
* Apache Maven (version 3+)

|  | [SDKMan](https://sdkman.io/) is the easiest way to install and manage JDKs and Maven on your host machine. |
|  | ---------------------------------------------------------------------------------------------------------- |

## [](#set-up)Set up

Create the following directory structure on your machine:

📂 ~ (your home directory)
  📂 student
    📂 src
      📂 main
        📂 java

Create a new file in the directory called `pom.xml` in the `student` directory. The pom file should be populated as follows:

pom.xml

```xml
Unresolved include directive in modules/tutorials/pages/java-tutorial/install-couchbase-java-sdk.adoc - include::java-sdk:student:example$pom.xml[]
```

| **1** | The dependencies section lists all the libraries required to build the application. In our case, we only need the Couchbase client SDK (version 3.2.1, in this case). |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

📂 ~ (your home directory)
  📂 student
  📃 pom.xml ⬅ here!
  📂 src
    📂 main
      📂 java

You can test the setup is correct by opening a terminal window and changing to the `student` directory. Run the build script to pull in all the dependencies.

```sh
mvn install
```

## [](#next-steps)Next steps

You’re now ready to write your [first Couchbase application](creating-the-students-collection.md).