from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pss

keyPath = input("Enter the public key: ")
signHex = str(input("Enter the encrypted text: "))
plainText = input("Enter the decrypted text: ")

publicKey = RSA.import_key(open(keyPath).read())
h = SHA256.new(plainText.encode('utf-8'))
varifier = pss.new(publicKey)

try:
    varifier.verify(h, bytes.fromhex(signHex))
    print("Signature valid!")
except(ValueError, TypeError):
    print("Validation failed!")
