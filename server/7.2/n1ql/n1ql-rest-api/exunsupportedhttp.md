[View original HTML](/server/7.2/n1ql/n1ql-rest-api/exunsupportedhttp.html)

For a REST method type that is not supported

Request

```sh
curl -v http://localhost:8093/query/service -X PUT \
     -d 'statement=SELECT name FROM `travel-sample`.inventory.hotel LIMIT 1' \
     -u Administrator:password
```

Response

```console
HTTP/1.1 405 Method Not Allowed
```