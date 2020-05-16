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
Enter path of the dat file: 010.dat

Transaction ID: 92a7c6d00b98e7824efe0a61bed2c9c7bbe7d787a15ff7dd8117bded3b74654d


Number of inputs: 4

	Input #1:

		Transaction ID: cbbee9817ab2585079ce0490369ea016808df2349a736a2ae19db4247cc9b96e
		Index: 5
		Length of signature: 60
		Signature: b6d95526a41a9504680b4e7c8b763a1b1d49d4955c8486216325253fec738dd7a9e28bf921119c160f0702448615bbda08313f6a8eb668d20bf50598

	Input #2:

		Transaction ID: 87f3c67cf22746e995af5a25367951baa2ff6cd471c483f15fb90badb37c5821
		Index: 87332
		Length of signature: 40
		Signature: 81855ad8681d0d86d1e91e00167939cb6694d2c422acd208a0072939487f6999eb9d18a44784045d

	Input #3:

		Transaction ID: 5968ba216897e9a2b3e0cefffab0d58084375e8978104df614d73b4a90fba436
		Index: 0
		Length of signature: 40
		Signature: 335b2e97aac2bd15fae04162adde96a511fabd9261425c3e945c3fbc1f270cdb734fd216d73d9196

	Input #4:

		Transaction ID: acb47cb9fbd8916648dd30b45f32facdd2d10922875e26689512c010960d9fa0
		Index: 31
		Length of signature: 60
		Signature: 20f05332caaf4699cdcbfff00ca530121dfe2ad49169678e88dbbc4b68c9e1c66b926bcc518e2568aa80c9c31e8faa3f00918061753771f14a34f364


Number of outputs: 2

	Output #1:

		Number of coins: 999999999
		Length of public key: 451
		Public key: -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4/Vst50I4qckOJatgJlL
AM9ozcAAoy1PBmz4fdEPbLuQidwIPTN6xCG14/osGTEh/Ys1Pis9teiV5VZ9f1eh
91GZIYpTpRVuviGR0qoacz7z86Sru37guWtSEhy2dxbzrsJoUpK7lhGtx3ZKFwH8
PvBHHf8kSMH+jA0V6mGWoseemcYWuJI8ZhLUUxjgnA1R/cTbwHq2OLAUe9+C9XGB
H+uAGlyBwji8LaWsPaVLFTEIcp7ljnmXOTmgW3XfJlnFSfb/CXEc4Q8jRf3H3V5i
MeuKtlPxndAKvCRNNl9P1vW5OWI9ls8wJkxNWsP84A+Pbw1F7wtJ/7jcA/LK4plo
7QIDAQAB
-----END PUBLIC KEY-----


	Output #2:

		Number of coins: 1
		Length of public key: 451
		Public key: -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAt9aR/chfSX6H/VjSTh97
LyrafCSrZTQe72pHkzZG9gInSNTRAufyCqR4f+qVPo7pBGOWFH7nFznYL6+7aL2w
kd5v1AJ1S759x4t2FIbUum3cGh8tsLic7tCGouRa/4+bJCfgaWmwg7d98oK1O3nY
Yrt5212KBg2fj51G4GnjiQQSWRtMi2AympYxL7vESHm9z4Uq6fFgtJOdq/S/T4WZ
jkEzL9VXwyX1OVSoU7M3yKIPNrllFizst3k0jI1FUPNSNMOQkifUQnKLgvPXYCRF
tlnLydWSQMt0t5NfAY8VABTkCiNot6Do7+abiyZngEFdz2JK8e0TyXe7td4X43SM
mwIDAQAB
-----END PUBLIC KEY-----

```