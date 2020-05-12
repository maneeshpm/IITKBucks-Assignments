from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_PSS

keyPath = input("Enter the public key: ")
signHex = str(input("Enter the encrypted text: "))
plainText = input("Enter the unencrypted text: ")

publicKey = RSA.import_key(open(keyPath).read())
h = SHA256.new(plainText.encode('utf-8'))
verifier = PKCS1_PSS.new(publicKey)


if verifier.verify(h,bytes.fromhex(signHex)):
    print("\nSignature valid!")
else:
    print("\nValidation failed!")
