---
title: Development Workflow
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-spark/edit/release/3.5/modules/ROOT/pages/dev-workflow.adoc
  xref: xref:spark-connector::dev-workflow.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/spark-connector/current/dev-workflow.html)

# Development Workflow

> Developing and Deploying Spark applications can be a challenge upfront. This section helps you through the development and deployment workflow. 

When developing a Spark application that uses external dependencies, typically there are two challenges a developer is confronted with:

* How to efficiently and quickly develop locally.
* How to reliably deploy to a production cluster.

Apart from the actual development, the biggest hurdle most of the time is the dependency management aspect. This documentation is intended to guide you through and to help you get set up as needed.

There are two ways the problem is typically approached: you can either add the dependencies to the classpath when you submit the application or you can create a big jar which contains all dependencies.

## [](#adding-the-connector-to-the-executors-classpath)Adding the Connector to the Executor's classpath

If you want to manage the dependency directly on the worker, the actual project setup is quite simple. You don't need to set up shadowing and can use a `build.sbt` like this:

```scala
name := "your-awesome-app"

organization := "com.acme"

version := "1.0.0-SNAPSHOT"

scalaVersion := "2.12.14"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "3.1.2",
  "org.apache.spark" %% "spark-sql" % "3.1.2",
  "com.couchbase.client" %% "spark-connector" % "3.1.0"
)
```

when developing the application you need to make sure that the `master` is not set, since you need to deploy it eventually to a non-local master.

```scala
object Main {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession
      .builder()
      .appName("Your Awesome App")
      // .master("local") <-- do not set the master!
      .config("spark.couchbase.connectionString", "127.0.0.1")
      .config("spark.couchbase.username", "Administrator")
      .config("spark.couchbase.password", "password")
      .getOrCreate()
  }
}
```

If you run this code from your IDE (or standalone), Spark will complain:

org.apache.spark.SparkException: A master URL must be set in your configuration
	at org.apache.spark.SparkContext.<init>(SparkContext.scala:386)

As always there are different ways to handle this, but a useful way is to set the master from a property.

One approach that is useful is to have a runnable class in the `test` (or somewhere else) directory which sets the property and then runs the application. This also has additional benefits that are discussed in the next section.

```scala
object RunLocal {
  def main(args: Array[String]): Unit = {
    System.setProperty("spark.master", "local[*]")
    Main.main(args)
  }
}
```

You can then build your application via `sbt package` on the command line and submit it to Spark via `spark-submit`. Because Couchbase distributes the connector via maven, you can include it with the `--packages` flag:

/spark/bin/spark-submit --master spark://your-spark-master:7077 --packages com.couchbase.client:spark-connector_2.12:3.1.0 /path/to/app/target/scala-2.12/your-awesome-app_2.12-1.0.0-SNAPSHOT.jar

If your environment does not have access to the internet you can use the `--jars` argument instead and grab the assembly with all the dependencies from here: [Download and API Reference](download-links.md).

## [](#deploying-a-jar-with-dependencies-included)Deploying a jar with dependencies included

The previous example showed how to add the connector during the submit phase as a dependency. If more than one dependency needs to be managed this can become hard to maintain since you also need to make sure that your `build.sbt` is always in sync with your command line parameters.

The alternative is to create a jar with batteries included that includes all dependencies in it. This requires more setup on the project side but saves you some work later on.

The `build.sbt` looks a bit different to the original version:

```scala
lazy val root = (project in file(".")).
  settings(
    name := "your-awesome-app",
    version := "1.0.0-SNAPSHOT",
    scalaVersion := "2.12.14",
    assembly / mainClass := Some("Main"),
  )

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "3.1.2" % "provided,test",
  "org.apache.spark" %% "spark-sql" % "3.1.2" % "provided,test",
  "com.couchbase.client" %% "spark-connector" % "3.1.0"
)
```

The important piece here is that the Spark dependencies are scoped to `provided` and `test`. We need this to not include Spark in the shadowed jar but still allow it to run in the IDE for development.

Also, create `project/plugins.sbt` if it doesn't exist and add:

addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "1.0.0")

The code now is similar to the previous section, but you need to make sure that the class you run in your IDE is in the test namespace so that Spark is actually included during development:

In `src/main/scala`:

```scala
object Main {

  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
      .setAppName("TravelCruncher")
      .set("com.couchbase.bucket.travel-sample", "")

    val sc = new SparkContext(conf)

    // ...
  }
}
```

Under `src/test/scala`:

```scala
object RunLocal {
  def main(args: Array[String]): Unit = {
    System.setProperty("spark.master", "local[*]")
    Main.main(args)
  }
}
```

Now instead of `sbt package` you need to use `sbt assembly` which will create the shadowed jar under \`target/scala\_2.12/your-awesome-app-assembly-1.0.0-SNAPSHOT.jar \`.

The jar can be submitted without specifying the dependencies:

/spark/bin/spark-submit --master spark://your-spark-master:7077 /path/to/app/target/scala-2.12/your-awesome-app-assembly-1.0.0-SNAPSHOT.jar