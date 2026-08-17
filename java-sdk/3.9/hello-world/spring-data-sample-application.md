---
title: Spring Data Sample Application
description: Discover how to program interactions with Spring Data and Couchbase
  via the Data, Query, and Search services.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.9/modules/hello-world/pages/spring-data-sample-application.adoc
  xref: xref:3.9@java-sdk:hello-world:spring-data-sample-application.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.9/hello-world/spring-data-sample-application.html)

# Spring Data Sample Application

> Discover how to program interactions with Spring Data and Couchbase via the Data, Query, and Search services. 

## [](#quick-start)Quick Start

Fetch the [Couchbase Java SDK travel-sample Application REST Backend](https://github.com/couchbaselabs/try-cb-spring) from github:

```console
git clone https://github.com/couchbaselabs/try-cb-spring.git
cd try-cb-spring
```

With [Docker](https://docs.docker.com/get-docker/) installed, you should now be able to run a bare-bones copy of Couchbase Server, load the travel-sample, add indexes, install the sample-application and its frontend, all by running a single command:

```console
docker-compose --profile local up
```

## [](#running-the-code-against-your-own-development-couchbase-server)Running the code against your own development Couchbase server.

For Couchbase Server 8.0, make sure that you have at least one node each of data; query; index; and search. For a development box, mixing more than one of these on a single node (given enough memory resources) is perfectly acceptable.

If you have yet to install Couchbase Server in your development environment [start here](../../../server/current/getting-started/do-a-quick-install.md).

Then load up the Travel Sample Bucket, using either the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui)or the [command line](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-cli). You will also need to [create a Search Index](#8.0@server:fts:fts-searching-from-the-ui.adoc#create-an-index) — Query indexes are taken care of by the Sample Bucket.

See the README at <https://github.com/couchbaselabs/try-cb-spring> for full details of how to run and tweak the Java SDK travel-sample app.

## [](#using-the-sample-app)Using the Sample App

![Travel Sample Register](../../../sdk/current/shared/_images/Travel-Sample-Register.png) 

Give yourself a username and password and click **Register**.

You can now try out searching for flights, booking flights, and searching for hotels. You can see which Couchbase SDK operations are being executed by clicking the red bar at the bottom of the screen:

![Couchbase Query Bar](../../../sdk/current/shared/_images/Couchbase-Query-Bar.png) 

## [](#sample-app-backend)Sample App Backend

The backend code shows Couchbase Java SDK in action with Query and Search, but also how to plug together all of the elements and build an application with Couchbase Server, the Java SDK and Spring Data. Look at `TenantUser.java` to see some of the pieces necessary in most applications, such as the TenantUser `@Service`:

```java
@Service
public class TenantUser {

  private final TokenService jwtService;
  private final UserRepository userRepository;
  private final BookingRepository bookingRepository;

  public TenantUser(TokenService tokenService, UserRepository userRepository, BookingRepository bookingRepository) {
    this.jwtService = tokenService;
    this.userRepository = userRepository;
    this.bookingRepository = bookingRepository;
  }
```

You may have noticed that we make use of Spring Data Couchbase repositories in the `TenantUser` class. You can see an example of how a repository is defined in `UserRepository.java`:

```java
@Repository("userRepository")
@Collection("users")
@ScanConsistency(query = QueryScanConsistency.REQUEST_PLUS)
public interface UserRepository extends CouchbaseRepository<User, String>, DynamicProxyable<UserRepository> {

}
```

Using the Spring Data Couchbase repository allows us to reduce boilerplate in our code and add a layer of abstraction to our cluster interactions.

Creating a user shows the typical security concerns, with salted password hashes, as well as the advantages of using Spring Data Couchbase to `save` the username into the database using the `userRepository` we mentioned previously:

```java
public Result<Map<String, Object>> createLogin(final String tenant, final String username, final String password,
		DurabilityLevel expiry) {
	UserRepository userRepository = this.userRepository.withScope(tenant);
	String passHash = BCrypt.hashpw(password, BCrypt.gensalt());
	User user = new User(username, passHash);
	UpsertOptions options = UpsertOptions.upsertOptions();
	if (expiry.ordinal() > 0) {
		options.durability(expiry);
	}
	String queryType = String.format("KV insert - scoped to %s.users: document %s", tenant, username);
	try {
		userRepository.withOptions(options).save(user);
		Map<String, Object> data = JsonObject.create().put("token", jwtService.buildToken(username)).toMap();
		return Result.of(data, queryType);
	} catch (Exception e) {
		throw new AuthenticationServiceException("There was an error creating account");
	}
}
```

Here, the _flights_ array, containing the flight IDs, is converted to actual objects:

```java
List<Map<String, Object>> results = new ArrayList<Map<String, Object>>();
    for (String flightId : flights) {
      Optional<Booking> res;
      try {
        res = bookingRepository.findById(flightId);
      } catch (DocumentNotFoundException ex) {
        throw new RuntimeException("Unable to retrieve flight id " + flightId);
      }
      Map<String, Object> flight = res.get().toMap();
      results.add(flight);
    }

    String queryType = String.format("KV get - scoped to %s.user: for %d bookings in document %s", tenant,
        results.size(), username);
    return Result.of(results, queryType);
  }
```

## [](#data-model)Data Model

See the [Travel App Data Model](../ref/travel-app-data-model.md) reference page for more information about the sample data set used.