from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pss

plainText = input("Enter encryption text: ")
keyPath = input("Enter the path of the private key: ")

key = RSA.import_key(open(keyPath).read())
h = SHA256.new(plainText.encode('utf-8'))
sign = pss.new(key).sign(h)

print(sign.hex())


