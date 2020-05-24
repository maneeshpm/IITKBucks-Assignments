## Assignment 5: Program to find Nonce and timestamp given block data

- Takes `index`, `parentHash`,`target` and path of block body binary file.
- Then it tries to find a combination of timestamp and nonce number that yields a header hash less than the target.

#### Running the code
```
python3 findHeader.py
```
Give the inputs on prompt.
Eg.

```
maneesh@edith ~/Assignment5$ python3 findHeader.py
Enter the Index: 5
Enter parent hash: 2b21ef8ab698e7daf03ccf0110acb4d844fabb5b9513221285f96593d4d4a573
Enter target: 0000000F00000000000000000000000000000000000000000000000000000000
Enter path of body file: 015.dat
Finding nonce... 
Nonce found!
Nonce = 127412161, Timestamp=1590258649.921928, Hash=0000000300e80bd99cee6039df1969e4f242743797359807ac60a0238b795bbb
Time elapsed = 4m 51s
```
More runs
```
maneesh@edith ~/Assignment5$ python3 findHeader.py
Enter the Index: 5
Enter parent hash: 2b21ef8ab698e7daf03ccf0110acb4d844fabb5b9513221285f96593d4d4a573
Enter target: 0000000F00000000000000000000000000000000000000000000000000000000
Enter path of body file: 015.dat
Finding nonce... 
Nonce found!
Nonce = 77264434, Timestamp=1590297867.035814, Hash=0000000d88f8ac3cf921dde55c8bd8629ac1cf88b042b968e8ed3e94db99229c
Time elapsed = 3m 0s
```
```
maneesh@edith ~/Assignment5$ python3 findHeader.py
Enter the Index: 5
Enter parent hash: 2b21ef8ab698e7daf03ccf0110acb4d844fabb5b9513221285f96593d4d4a573
Enter target: 0000000f00000000000000000000000000000000000000000000000000000000
Enter path of body file: 015.dat
Finding nonce... 
Nonce found!
Nonce = 225909499, Timestamp=1590299482.788736, Hash=000000057e25841ba981c911f526e79c95a703fac1cfdc342dee649b12090776
Time elapsed = 8m 51s
````