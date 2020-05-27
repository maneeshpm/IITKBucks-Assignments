## Assignment 6: Server to maintain a distributed list

- Contains two endpoints `/add` and `/list`.
- `/add` receives json data in a POST request as `{"key": <integer key>, "value":<string value>}` and adds it to a dictionary as `{key:"value"}` pair. It then broadcasts POST requests to all the `peer` in the list of peers on their `/add` endpoint. If the key is already present, the request is ignored.
- `list` receives get request and returns jsonified version of the dictionary.

#### Running the code
```
maneesh@edith ~/Assignment6$ python3 server.py
```
Assuming the servers in the peers list are active, we now make POST request on `/add`.
```
maneesh@edith ~/Assignment6$ echo '{"key": 1, "value":"testval"}' | http localhost:8787/add
HTTP/1.0 200 OK
Content-Length: 155
Content-Type: text/html; charset=utf-8
Date: Wed, 27 May 2020 07:50:38 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

SET {1 : "testval"}
SENT {1 : "testval"} TO http://localhost:8786/add, STATUS = 200, OK
SENT {1 : "testval"} TO http://localhost:8785/add, STATUS = 200, OK

```
Making a GET request on `/list`
```
maneesh@edith ~/Assignment6$ http localhost:8787/list
HTTP/1.0 200 OK
Content-Length: 21
Content-Type: application/json
Date: Wed, 27 May 2020 07:51:11 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

{
    "1": "testval"
}

```
