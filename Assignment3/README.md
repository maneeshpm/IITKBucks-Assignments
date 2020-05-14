## Assignment 3: Generating A Transaction File

- Program to create a binary file from the trasactiond data. The inputs are: `number of inputs` followed by `transaction id`, `index of output` and `signature` for each input. Then `number of outputs` followed by `number of coins` and `public key path` for each output.
- The file `classes` host the classes `Txn`, `Inp`, `Output`. They have the function `getTxnData()`, `getBinaryInput()` and `getBinaryOutput()` to generate a blob of the data it holds.
- The input and output data are stored on `Inp` and `Output` objects respectively. The `Txn` object houses an array of such `Inp` and `Output`.
- Transaction data is generated as a blob `[number of inputs][total input data][number of outputs][total output data]` using the `getTxnData()` function of `Txn` object and is stored in a `<hash of transaction data>.dat` file.
#### Running the code
```
python3 txn.py
```
Give the inputs on prompt.
Eg.
```
maneesh@edith: ~/Assignment$ python3 txn.py
Enter the number of inputs: 1
==================== Input #0 ====================
Enter Transaction id: 00008374f186f612a600b0f87fddb98c6d615776f3d988d2c4a8d519295ae073
Enter index of output: 0
Enter the signature: ae233d7d85aa1c9d190f59bdf600442e10d709eae9745ee2e65ca11ac43e95ff2f457317c6cb04d61e57f8f4739f432a42d4c81e6a7c10b077252258b816de982c61309f82118937612985bdb8c9aa236abb57fa48a7488902b775d48f018a2532e6217da33a372b3b8605e1dd7768e7f9321f91cdeaf4ac76517f02e38d190af767e169bbc31c92e8c8c1529cd2a963bad56344b0fb0997a9fa55755f0a06403513e9563ed568fcb235c0647583303f417b0998577bc2e8d43495eef6fddc5eb5e0f4962cdac4aec01299cbd6739da239d950d9f5b043f319f1209a5cf66f8fd848a860370474b156c718a09a3a771c5e97f527a06f4b3859b11e7f2e382fbc

Enter the number of outputs: 1
===================== Output #0 =======================
Enter the number of coins: 20
Enter the path of the key: public.pem

c90fcb62aac3469554903447e21e9fa0c8eb93c9353b830cf72a0b0682d02c54.dat created successfully!
```