---
title: Sample Application
description: Discover how to program interactions with the Couchbase Server via
  the data, query, and search services -- using the Travel Sample Application
  with the built-in Travel Sample data Bucket.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.4/modules/hello-world/pages/sample-application.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.4@python-sdk:hello-world:sample-application.adoc[]
---

[View original HTML](/python-sdk/4.4/hello-world/sample-application.html)

# Sample Application

> Discover how to program interactions with the Couchbase Server via the data, query, and search services — using the Travel Sample Application with the built-in Travel Sample data Bucket. 

## [](#quick-start)Quick Start

Fetch the [Couchbase Python SDK travel-sample Application REST Backend](https://github.com/couchbaselabs/try-cb-python) from github:

```console
git clone https://github.com/couchbaselabs/try-cb-python.git
cd try-cb-python
```

With [Docker](https://docs.docker.com/get-docker/) installed, you should now be able to run a bare-bones copy of Couchbase Server, load the travel-sample, add indexes, install the sample-application and its frontend, all by running a single command:

```console
docker-compose --profile local up
```

## [](#using-the-sample-app)Using the Sample App

![Travel Sample Register](../../../sdk/current/shared/_images/Travel-Sample-Register.png) 

Give yourself a username and password and click **Register**.

You can now try out searching for flights, booking flights, and searching for hotels. You can see which Couchbase SDK operations are being executed by clicking the red bar at the bottom of the screen:

![Couchbase Query Bar](../../../sdk/current/shared/_images/Couchbase-Query-Bar.png) 

## [](#sample-app-overview)Sample App Overview

The sample application runs 3 docker containers which contain the following:

* The frontend — a Vue web app which communicates with the backend via an API.
* The backend — a Python web app which contains the SDK code to communicate with Couchbase Server.
* The database — a one node cluster containing the travel sample Bucket and reqisite indexes.

![travel sample app overview](../../../sdk/current/shared/_images/travel-sample-app-overview.png) 

The API implements a different endpoint for each of the app’s features. You can explore the API here in read-only mode, or once you are running the application, at the `localhost:8080/apidocs` endpoint.

## [](#data-model)Data Model

See the [Travel App Data Model](../ref/travel-app-data-model.md) reference page for more information about the sample data set used.

## [](#application-backend)Application Backend

The backend code shows the Couchbase Python SDK in action with Data(K/V), Query, and Search services. These elements are each plugged together with Couchbase Server to implement the API needed by the frontend of the application.

For line by line explanations of the backend code, refer to the `travel.py` file in the `try-cb-python` repository.

### [](#api-structural-overview)API Structural Overview

Flask and Swagger implement the API endpoints. When starting the backend, the following code:

1. Initializes the Flask web application.
2. Updates the API configuration.
3. Sets the template to define the security schemes and result schemas.
4. Creates the API component to tie the endpoints to.
5. Restricts the API to only accept requests with content types and authorization headers.

```python
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SWAGGER'] = {
    'openapi': '3.0.3',
    'title': 'Travel Sample API',
    'version': '1.0',
    'description': 'A sample API for getting started with Couchbase Server and the SDK.',
    'termsOfService': ''
}

swagger_template = {
    "components": {
        "securitySchemes": {
            "bearer": {
            ...
            }
        },
        "schemas": {
        ...
        }
    }
}

api = Blueprint("api", __name__)

CORS(app, headers=['Content-Type', 'Authorization'])
```

A function defines each endpoint. The Flask `route` wrapper defines which URL triggers the function. For instance, the URL `localhost:8080/` triggers the following function:

```python
@app.route('/')
def index():
    ...
```

Besides the default endpoint, each of the endpoint functions are inside a `SwaggerView` class. This class is purely to group related endpoints together inside the Swagger API docs page, and has no direct effect on the endpoints:

```python
class AirportView(SwaggerView):
    """Airport class for airport objects in the database"""
```

Each endpoint begins with a docstring that Swagger uses to generate the documentation for that endpoint. The code samples on this page omit the body of these docstrings for brevity.

For more information regarding the web app and API definition, see the [Flask](https://flask.palletsprojects.com/en/2.3.x/) and [Flasgger](https://github.com/flasgger/flasgger) documentation.

### [](#connecting-to-couchbase)Connecting to Couchbase

The backend expects several parameters when invoked:

* The cluster connection string — this is either a Capella endpoint, or a node IP address.
* The URI scheme — `couchbases` for Capella, and `couchbase` for a local server.
* The username — `cbdemo` for Capella, and `Administrator` for a local server.
* The password — `Password123!` for Capella, and `password` for a local server.

```python
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--cluster', help='Connection String i.e. localhost', default='db')
parser.add_argument('-s', '--scheme', help='couchbase or couchbases', default='couchbase')
parser.add_argument('-a', '--connectargs', help="?any_additional_args", default="")
parser.add_argument('-u', '--user', help='User with access to bucket')
parser.add_argument('-p', '--password', help='Password of user with access to bucket')

args = parser.parse_args()

if not args.cluster:
  raise ConnectionError("No value for CB_HOST set!")

if ("couchbases://" in args.cluster) or ("couchbase://" in args.cluster):
    CONNSTR = f"{args.cluster}{args.connectargs}"
else:
    CONNSTR = f"{args.scheme}://{args.cluster}{args.connectargs}"
        
authenticator = PasswordAuthenticator(args.user, args.password)
print("Connecting to: " + CONNSTR)

# ...
# API endpoints
# ...

def connect_db():
    print(CONNSTR, authenticator)
    cluster = Cluster(CONNSTR, ClusterOptions(authenticator))
    bucket = cluster.bucket('travel-sample')
    return cluster, bucket

if __name__ == "__main__":
    cluster, bucket = connect_db()
    app.register_blueprint(api, url_prefix="/api")
    swagger = Swagger(app, template=swagger_template)
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=False)
```

See [Managing Connections](../howtos/managing-connections.md#connection-strings) for more information about connecting the Python SDK to Couchbase.

### [](#user-login)User Login

The first thing the user needs to do when using the application is to either log in, or register an account. Multiple endpoints implement this capability, so a SwaggerView class organizes these endpoints together:

```python
class TenantUserView(SwaggerView):
    """Class for storing user related information for a given tenant"""
```

The application has two different tenants that store data in two different tenant scopes:

* CB Travel uses `tenant_agent_00`
* Behind the Sofa Bookings uses `tenant_agent_01`

To avoid having two nearly identical sets of endpoints for each tenant, the application uses a variable section `<tenant>` in the URL to specify the tenant. The signup code for both tenants is therefore defined at the single endpoint `/tenants/<tenant>/user/signup`:

```python
@api.route('/tenants/<tenant>/user/signup', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def signup(tenant):
    """Signup a new user
    ...
    """
```

The request body consists of a JSON object with two fields: `username` and `password`. The application tries a K/V insert into the users collection within the scope provided by the frontend. The document key is the username, and the value is a JSON object of the form:

{
  'username':<username>,
  'password':<password>
}

> [!NOTE]
> The document key is a lowercase version of the provided username — this means that different usernames can refer to the same document. For example, if a user signs up with the username `Douglas Reynholm`, a different user can’t sign up with the username `douglas reynholm`, as both resolve to the same document key.

See [Data Operations](../howtos/kv-operations.md) for more information about K/V operations.

```python
requestBody = request.get_json()
user = requestBody['user']
password = requestBody['password']

userDocumentKey = lowercase(user)

agent = lowercase(tenant)
scope = bucket.scope(agent)
users = scope.collection('users')

queryType = f"KV insert - scoped to {scope.name}.users: document "

try:
    users.insert(userDocumentKey, {'username': user, 'password': password})
    responseJSON = jsonify(
        {'data': {'token': genToken(user)}, 'context': [queryType + user]})
    response = make_response(responseJSON)
    return response, 201

except DocumentExistsException:
    print(f"User {user} item already exists", flush=True)
    return abortmsg(409, "User already exists")
except Exception as e:
    print(e)
    return abortmsg(500, "Failed to save user", flush=True)
```

To perform a login, the frontend provides the username and password given by the user in the same JSON format as the `signup` endpoint. As the username is the document key, the application doesn’t need to retrieve the entire document, only the password field. The application uses a [Sub-Document](../howtos/subdocument-operations.md) operation to perform a `GET` on this one field. This password is then compared against the given username.

```python
@api.route('/tenants/<tenant>/user/login', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def login(tenant):
    """Login an existing user for a given tenant agent
    ...
    """
    requestBody = request.get_json()
    user = requestBody['user']
    providedPassword = requestBody['password']

    userDocumentKey = lowercase(user)

    agent = lowercase(tenant)
    scope = bucket.scope(agent)
    users = scope.collection('users')

    queryType = f"KV get - scoped to {scope.name}.users: for password field in document "

    try:
        documentPassword = users.lookup_in(userDocumentKey, (
            SD.get('password'),
        )).content_as[str](0)

        if documentPassword != providedPassword:
            return abortmsg(401, "Password does not match")

    except DocumentNotFoundException:
        print(f"User {user} item does not exist", flush=True)
    except AmbiguousTimeoutException or UnAmbiguousTimeoutException:
        print("Request timed out - has Couchbase stopped running?", flush=True)
    else:
        return jsonify({'data': {'token': genToken(user)}, 'context': [queryType + user]})

    return abortmsg(401, "Failed to get user data")
```

### [](#querying-flight-information)Querying Flight Information

The `flightPaths` endpoint takes a source and destination airport name, and a departure date. It returns a list of matching flight routes:

```python
class FlightPathsView(SwaggerView):
    """ FlightPath class for computed flights between two airports FAA codes"""

    @api.route('/flightPaths/<fromLoc>/<toLoc>', methods=['GET', 'OPTIONS'])
    @cross_origin(supports_credentials=True)
    def flightPaths(fromLoc, toLoc):
        """
        Return flights information, cost and more for a given flight time and date
        ...
        """
```

Key/value operations aren’t sufficient to service a complex request like searching for flight information. The Query Service provides this capability with minimal complexity.

> [!NOTE]
> You may recall that the web application provides both outbound and return flights. The frontend provides this information by making two separate requests to the backend, with the `<fromLoc>` and `<toLoc>` variable sections of the URL switched.

A single query can’t provide this information without significant complexity, as the route document schema doesn’t include the airport names:

```json
{
  "id": 10000,
  "type": "route",
  "airline": "AF",
  "airlineid": "airline_137",
  "sourceairport": "TLV",
  "destinationairport": "MRS",
  "stops": 0,
  "equipment": "320",
  "schedule": [{
    "day": 0,
    "utc": "10:13:00",
    "flight": "AF198"
  },
  ...
  {
    "day": 6,
    "utc": "07:00:00",
    "flight": "AF496"
  }],
  "distance": 2881.617376098415
}
```

Therefore an initial query fetches the `faa` field from the corresponding documents in the airport collection:

```python
queryType = "SQL++ query - scoped to inventory: "
context = []

faaQueryPrep = "SELECT faa as fromAirport FROM `travel-sample`.inventory.airport \
                WHERE airportname = $1 \
                UNION SELECT faa as toAirport FROM `travel-sample`.inventory.airport \
                WHERE airportname = $2"

faaResults = cluster.query(faaQueryPrep, fromLoc, toLoc)

flightPathDict = {}
for result in faaResults:
    flightPathDict.update(result)

queryFrom = flightPathDict['fromAirport']
queryTo = flightPathDict['toAirport']

context.append(queryType + faaQueryPrep)
```

The routes are now queried. [UNNEST](../../../server/7.6/n1ql/n1ql-language-reference/unnest.md) flattens the schedule list, and a [JOIN](../../../server/7.6/n1ql/n1ql-language-reference/join.md) on the airline collection gets the airline name from the airline id:

```python
routeQueryPrep = "SELECT a.name, s.flight, s.utc, r.sourceairport, r.destinationairport, r.equipment \
                FROM `travel-sample`.inventory.route AS r \
                UNNEST r.schedule AS s \
                JOIN `travel-sample`.inventory.airline AS a ON KEYS r.airlineid \
                WHERE r.sourceairport = $fromfaa AND r.destinationairport = $tofaa AND s.day = $dayofweek \
                ORDER BY a.name ASC;"

flightDay = convdate(request.args['leave'])
routeResults = cluster.query(routeQueryPrep, 
                             fromfaa=queryFrom, 
                             tofaa=queryTo, 
                             dayofweek=flightDay)

routesList = []
for route in routeResults:
    route['price'] = math.ceil(random() * 500) + 250
    routesList.append(route)

context.append(queryType + routeQueryPrep)

response = make_response(jsonify({"data": routesList, "context": context}))
return response
```

### [](#auto-completing-airport-names)Auto-Completing Airport Names

Users may not recognize an airport by the name stored in the database. For example, Los Angles Intl is commonly known by its FAA code, LAX. To avoid this mismatch, the frontend auto-completes potential airport names as the user is typing.

The airports endpoint takes a string, and returns potential airport names. The application modifies the query based on whether it thinks the provided string is a partial airport name, or FAA code:

* The endpoint presumes an FAA code if the string is 3 characters long. In this case, the query searches for a document with a matching FAA code, returning the corresponding airport name.
* Otherwise, it presumes the string is a partial airport name. The query uses the [POSITION](../../../server/7.6/n1ql/n1ql-language-reference/stringfun.md#fn-str-position) function to match the partial airport name to the start of the `airportname` field.

```python
class AirportView(SwaggerView):
    """Airport class for airport objects in the database"""
    @api.route('/airports', methods=['GET', 'OPTIONS'])
    @cross_origin(supports_credentials=True)
    def airports():
        """Returns list of matching airports and the source query
        ...
        """

        queryType = "SQL++ query - scoped to inventory: "
        partialAirportName = request.args['search']

        queryPrep = "SELECT airportname FROM `travel-sample`.inventory.airport WHERE "
        sameCase = partialAirportName == partialAirportName.lower() or partialAirportName == partialAirportName.upper() #bool

        if sameCase and len(partialAirportName) == 3:
            queryPrep += "faa=$1"
            queryArgs = [partialAirportName.upper()]
        elif sameCase and len(partialAirportName) == 4:
            queryPrep += "icao=$1"
            queryArgs = [partialAirportName.upper()]
        else:
            queryPrep += "POSITION(LOWER(airportname), $1) = 0"
            queryArgs = [partialAirportName.lower()]

        results = cluster.query(queryPrep, *queryArgs)
        airports = [x for x in results]

        context = [queryType + queryPrep]

        response = make_response(jsonify({"data": airports, "context": context}))
        return response
```

### [](#booking-flights)Booking Flights

The frontend handles the cart, so adding flights doesn’t affect the database. Only when the user clicks **Buy** are flights booked.

The `updateflights` endpoint adds a flight booking to the database. The frontend provides the flight details in the request body, and the user and tenant in the URL. The endpoint first creates a booking document in the bookings collection of the corresponding tenant. This document contains the flight details provided to the frontend by the `flightPaths` endpoint:

```json
{
  "destinationairport": "JFK",
  "equipment": "76W 764",
  "flight": "AF453",
  "name": "Air France",
  "price": 371,
  "sourceairport": "LHR",
  "utc": "08:00:00",
  "date": "05/17/2023"
}
```

The document key for this booking is a random 36 character string.

```python
@api.route('/tenants/<tenant>/user/<username>/flights', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def updateflights(tenant, username):
    """Book a new flight for a user
    ...
    """
    agent = lowercase(tenant)
    user = lowercase(username)

    scope = bucket.scope(agent)
    users = scope.collection('users')
    bookings = scope.collection('bookings')

    queryType = f"KV update - scoped to {scope.name}.users: for bookings field in document "

    # HTTP token authentication
    bearer = request.headers['Authorization']
    if not auth(bearer, username):
        return abortmsg(401, 'Username does not match token username: ' + username)

    try:
        flightData = request.get_json()['flights'][0]
        flightID = str(uuid.uuid4())
        bookings.upsert(flightID, flightData)

    except Exception as e:
        print(e, flush=True)
        return abortmsg(500, "Failed to add flight data")
```

However, this booking document isn’t associated with the user who booked it. Therefore the endpoint performs a [Sub-Document](../howtos/subdocument-operations.md) operation on the `bookings` field in the given user’s document to add the booking document’s key:

```python
try:
    users.mutate_in(user, (SD.array_append('bookings', flightID, create_parents=True),))
    resultJSON = {'data': {'added': [flightData]},
                  'context': [queryType + user]}
    return make_response(jsonify(resultJSON))

except DocumentNotFoundException:
    return abortmsg(401, "User does not exist")
except Exception:
    return abortmsg(500, "Couldn't update flights")
```

> [!NOTE]
> If the booking document insert succeeds, but the update to the user document fails, the endpoint returns an internal server error to the frontend. However, the stray booking document remains the database. In a production environment it is good practice to add handling code to remove this stray document.

### [](#viewing-booked-flights)Viewing Booked Flights

The user can also view their flights after they have booked them. The `getflights` endpoint takes a user, and returns details on each flight they have booked.

First, the endpoint performs a [Sub-Document](../howtos/subdocument-operations.md) operation to retrieve the `bookings` field.

If the user hasn’t booked any flights, there is no `bookings` field. However, if the application tries a lookup on this non-existent field, the operation still succeeds, but reading these results causes a `PathNotFoundException`. To avoid handling this exception, the lookup contains both a `get` and an `exists` operation. The endpoint can then verify the path exists before attempting to read the results:

```python
@api.route('/tenants/<tenant>/user/<username>/flights', methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def getflights(tenant, username):
    """List the flights that have been reserved by a user
    ...
    """
    agent = lowercase(tenant)

    scope = bucket.scope(agent)
    users = scope.collection('users')
    flights = scope.collection('bookings')

    # HTTP token authentication
    bearer = request.headers['Authorization']
    if not auth(bearer, username):
        return abortmsg(401, 'Username does not match token username: ' + username)
    
    try:
        userDocumentKey = lowercase(username)

        lookupResult = users.lookup_in(
          userDocumentKey,
          [
            SD.get('bookings'),
            SD.exists('bookings')
          ])
        
        bookedFlightKeys = []
        if lookupResult.exists(1):
            bookedFlightKeys = lookupResult.content_as[list](0)
```

The endpoint can now iterate over the booking keys, performing `GET` requests for the flight details:

```python
    rows = []
    for key in bookedFlightKeys:
        rows.append(flights.get(key).content_as[dict])

    queryType = f"KV get - scoped to {scope.name}.users: for {len(bookedFlightKeys)} bookings in document "
    response = make_response(jsonify({"data": rows, "context": [queryType + userDocumentKey]}))
    return response

except DocumentNotFoundException:
    return abortmsg(401, "User does not exist")
```

### [](#searching-for-hotels)Searching for Hotels

The user can also search for hotels. The `hotels` endpoint uses the [Search queries](../howtos/full-text-searching-with-sdk.md) to find the details of hotels that match given search terms. The frontend provides two search terms:

* Location-this could refer to a country, city, or even an exact address.
* Description-this could be anything from a name to a keyword.

Since multiple fields could match these terms, the endpoint uses a conjunction query containing multiple match queries:

```python
@api.route('/hotels/<description>/<location>/', methods=['GET'])
@cross_origin(supports_credentials=True)
def hotels(description, location):
    # Requires FTS index called 'hotels-index'
    """Find hotels using full text search
    ...
    """
    queryPrep = FT.ConjunctionQuery()
    if location != '*' and location != "":
        queryPrep.conjuncts.append(
            FT.DisjunctionQuery(
                FT.MatchPhraseQuery(location, field='country'),
                FT.MatchPhraseQuery(location, field='city'),
                FT.MatchPhraseQuery(location, field='state'),
                FT.MatchPhraseQuery(location, field='address')
            ))

    if description != '*' and description != "":
        queryPrep.conjuncts.append(
            FT.DisjunctionQuery(
                FT.MatchPhraseQuery(description, field='description'),
                FT.MatchPhraseQuery(description, field='name')
            ))

    # Attempting to run a compound query with no sub-queries will result in
    # a 'NoChildrenException'.

    if len(queryPrep.conjuncts) == 0:
        queryType = "FTS search rejected - no search terms were provided"
        response = {'data': [], 'context': [queryType]}
        return jsonify(response)

    searchRows = cluster.search_query('hotels-index', 
                                      queryPrep, 
                                      SearchOptions(limit=100))
```

The result of a search query is an iterable containing `SearchRow` objects. Each row represents a match in one document. It doesn’t contain the document data, instead just the matching string and metadata. This metadata includes the document key, so a sub-document operation retrieves the fields needed by the frontend.

```python
allResults = []
addressFields = ['address', 'city', 'state', 'country']
dataFields = ['name', 'description']

scope = bucket.scope('inventory')
hotel_collection = scope.collection('hotel')

for hotel in searchRows:

    hotelFields = hotel_collection.lookup_in(
        hotel.id, [SD.get(x) for x in [*addressFields, *dataFields]])

    # Concatenates the first 4 fields to form the address. 
    hotelAddress = []
    for x in range(len(addressFields)):
        try:
            hotelAddress.append(hotelFields.content_as[str](x))
        except DocumentNotFoundException:
            pass
    hotelAddress = ', '.join(hotelAddress)

    hotelData = {}
    for x, field in enumerate(dataFields):
        try:    
            hotelData[field] = hotelFields.content_as[str](x+len(addressFields))
        except DocumentNotFoundException:
            pass
        
    hotelData['address'] = hotelAddress
    allResults.append(hotelData)

queryType = f"FTS search - scoped to: {scope.name}.hotel within fields {','.join([*addressFields, *dataFields])}"
response = {'data': allResults, 'context': [queryType]}
return jsonify(response)
```

## [](#next-steps)Next Steps

* Sign up for a [Capella account](#cloud:ROOT:index.adoc) and deploy a free operational cluster to get started with Couchbase the easy way.
* Read more about interacting with the Couchbase services used in this example — [Data (K/V)](../howtos/kv-operations.md), [Sub-Document](../howtos/subdocument-operations.md), [Query](../howtos/n1ql-queries-with-sdk.md), and [Search](../howtos/full-text-searching-with-sdk.md).
* Discover [Distributed ACID Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md) from the Python SDK, for cases where several documentations (such as combined flight and hotel bookings) must succeed together.