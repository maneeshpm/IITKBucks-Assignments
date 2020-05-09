## Assignment 2: Digital Signature Validation
Program to validate a digital signature. 
- The file `keyGen.py` generates a public-private key pair for RSA asymmetric encryption. 
- The file `signer.py` takes a `private.pem` key and a `plainText` to sign as an input and generates the signature after performing an `SHA256` hash on the plainText. The encryption method is RSA with PSS padding. Outputs the hex of the signature.
- The file `varifier.py` takes the signature, the `plainText` and the `public.pem` key as the input and varifies if the signature is valid by comparing the decrypted signature with `plainText`.   
#### Running the code
Test 1: Giving an authentic signature corresponding to the input `digital signature`

```
python3 signer.py
Enter the public key: public.pem
Enter the encrypted text: 193aad5cadffe3356c6b79d544de50d7e160a69d4b9d884531b7791fb6cde125ce696f9b55527708399eb1f9e2697d40bb489abc24269e0ee77d39314cfe9ee170be631b3323638f0bc252209ad7a8dbf8f20455436e6da07c3beeab1118c959eb71f97969a720c5bfbe0caac859e63bf98d7759ef9fe4678f53e49f3ba6edd992b1ee79531801ecb2526662bdd785f54ae18acc921fcc67fdf1bd3b0ba00f0af053f6cdf5af40c65fa5846f25c645f5e7feaa3d81189230c32c64530a0bf134a5ab90bbd576e7cbc11d68a8a4ebfca50f16093a373c53a5a8e242241ca631785c7eeeea7b1207fb1a45f8c4756a391dbbbc2c12b4abe0930ae7b07831872e4c
Enter the unencrypted text: digital signature

Signature valid!

```
Test 2: Giving an unauthentic signature(corresponding to the input `digital tempered`)

```
python3 varifier.py
Enter the public key: public.pem
Enter the encrypted text: ae233d7d85aa1c9d190f59bdf600442e10d709eae9745ee2e65ca11ac43e95ff2f457317c6cb04d61e57f8f4739f432a42d4c81e6a7c10b077252258b816de982c61309f82118937612985bdb8c9aa236abb57fa48a7488902b775d48f018a2532e6217da33a372b3b8605e1dd7768e7f9321f91cdeaf4ac76517f02e38d190af767e169bbc31c92e8c8c1529cd2a963bad56344b0fb0997a9fa55755f0a06403513e9563ed568fcb235c0647583303f417b0998577bc2e8d43495eef6fddc5eb5e0f4962cdac4aec01299cbd6739da239d950d9f5b043f319f1209a5cf66f8fd848a860370474b156c718a09a3a771c5e97f527a06f4b3859b11e7f2e382fbc
Enter the unencrypted text: digital signature

Validation failed!
```



