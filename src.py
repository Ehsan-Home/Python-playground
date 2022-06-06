from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)
publicKey = keyPair.public_key().exportKey()
privateKey = keyPair.exportKey()

print("public key", publicKey.decode('ascii'))
print("private key", privateKey.decode('ascii'))