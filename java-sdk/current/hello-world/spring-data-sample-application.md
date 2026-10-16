---
title: Spring Data Sample Application
description: Discover how to program interactions with Spring Data and Couchbase
  via the Data, Query, and Search services.
pubDate: 2026-10-16T07:26:40.932Z
meta:
  component:
    title: Java SDK
    version: "3.13"
  topic_type: tutorial
antora:
  editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.13/modules/hello-world/pages/spring-data-sample-application.adoc
  xref: xref:java-sdk:hello-world:spring-data-sample-application.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/current/hello-world/spring-data-sample-application.html)

# Spring Data Sample Application

> Discover how to program interactions with Spring Data and Couchbase via the Data, Query, and Search services. Discover how to program interactions with Couchbase via the Data, Query, and Search services. 

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

For this quickstart, we use three collections, `airport`, `airline` and `routes` that contain sample airports, airlines and airline routes respectively. The routes collection connects the airports and airlines as seen in the figure below. We use these connections in the quickstart to generate airports that are directly connected and airlines connecting to a destination airport. Note that these are just examples to highlight how you can use SQL++ queries to join the collections.

![travel-sample data model](ref:image$travel_sample_data_model.png)