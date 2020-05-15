## Assignment 3: Reading Data From A Transaction Binary File

- Program to read a transaction binary file and print the details.
- The path of the binary file is taken as input and is read byte by byte. The data being read is stored in a `Txn` object which further contain arrays of `Inp` and `Output` objects.
- The function `getTxnDetails()` prints all the details of the binary file in a neat format.

#### Running the code
```
python3 reader.py
```
Give the inputs on prompt.
Eg.
```
maneesh@edith: ~/Assignment4$ python3 reader.py
Enter path of the dat file: 4cdd8d60f816550b3b2566abbabf1446fd0a8cc68a018276656f29998d4ecfd0.dat

Transaction ID: 4cdd8d60f816550b3b2566abbabf1446fd0a8cc68a018276656f29998d4ecfd0


Number of inputs: 2

	Input #1:

		Transaction ID: 87bec4e88919cbf114e0014546b8dbef91cca4deaa74b0147d48f2b21dccee65
		Index: 0
		Length of signature: 256
		Signature: 193aad5cadffe3356c6b79d544de50d7e160a69d4b9d884531b7791fb6cde125ce696f9b55527708399eb1f9e2697d40bb489abc24269e0ee77d39314cfe9ee170be631b3323638f0bc252209ad7a8dbf8f20455436e6da07c3beeab1118c959eb71f97969a720c5bfbe0caac859e63bf98d7759ef9fe4678f53e49f3ba6edd992b1ee79531801ecb2526662bdd785f54ae18acc921fcc67fdf1bd3b0ba00f0af053f6cdf5af40c65fa5846f25c645f5e7feaa3d81189230c32c64530a0bf134a5ab90bbd576e7cbc11d68a8a4ebfca50f16093a373c53a5a8e242241ca631785c7eeeea7b1207fb1a45f8c4756a391dbbbc2c12b4abe0930ae7b07831872e4c

	Input #2:

		Transaction ID: 87bec4e88919cbf114e0014546b8dbef91cca4deaa74b0147d48f2b21dccee65
		Index: 1
		Length of signature: 256
		Signature: 193aad5cadffe3356c6b79d544de50d7e160a69d4b9d884531b7791fb6cde125ce696f9b55527708399eb1f9e2697d40bb489abc24269e0ee77d39314cfe9ee170be631b3323638f0bc252209ad7a8dbf8f20455436e6da07c3beeab1118c959eb71f97969a720c5bfbe0caac859e63bf98d7759ef9fe4678f53e49f3ba6edd992b1ee79531801ecb2526662bdd785f54ae18acc921fcc67fdf1bd3b0ba00f0af053f6cdf5af40c65fa5846f25c645f5e7feaa3d81189230c32c64530a0bf134a5ab90bbd576e7cbc11d68a8a4ebfca50f16093a373c53a5a8e242241ca631785c7eeeea7b1207fb1a45f8c4756a391dbbbc2c12b4abe0930ae7b07831872e4c


Number of outputs: 1

	Output #1:

		Number of coins: 20
		Length of public key: 450
		Public key: b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0n7WkbnP/+rlzkWXHAco\nd2gXTtQM3BUg5aN0K9zs2db2OLUCkFbww2LjWyfMXNbTHhgIVwsfqP43rapFhaVF\n3ufNPkAKQ42OvhxGgYGngtpfF7v7UEkXhNmboJugJO+lnOglz4iFGr5z4SyL78sp\nFHfjcjVJuhgUpL3lM28jS7vP/ZlB8DtUemakRH6G6daBFDK+QjZO4yUmjdahVSgO\nZnowGwd38mQZUlzMTakt+9TUdNtdHvXXNqEqDXMlgjvljuIfA8igpA+nE/T6FRe/\nUtPCn2d6Ytim3kFWQmtsp6xf3hL1aNkL2aQwd62O60i4O7HKdb7aPHG3SqvM5enz\n2wIDAQAB\n-----END PUBLIC KEY-----'

```