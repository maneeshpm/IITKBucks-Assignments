## Assignment 7: Server to exhibit threading capacities and thread control using requests

- Contains two endpoints `/start` and `/result`.
- `/start` receives json data in a POST request as `{"data": <string>}` and starts a thread which tries to mine for a nonce value for that perticular string.
- `/result` receives get request and returns jsonified version of the result nonce, -1 otherwise.

#### Running the code
```
maneesh@edith ~/Assignment6$ python3 app.py
```
Making a post requst on `/start`
```
maneesh@edith ~/Assignment6$ echo '{"data":"maneesh"}' | http localhost:8787/start
HTTP/1.0 200 OK
Content-Length: 7
Content-Type: text/html; charset=utf-8
Date: Wed, 27 May 2020 07:50:38 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

MINING!
```
