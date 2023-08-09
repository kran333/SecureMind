from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
# from Cryptodome.Signature import PKCS1_v1_5
# from Cryptodome.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Cryptodome import Random
# from base64 import b64encode, b64decode
hash = "SHA-256"
keysz = 1024
msg = "this is the message"
def newkeys(keysize):
   random_generator = Random.new().read
   key = RSA.generate(keysize, random_generator)
   private, public = key, key.publickey()
   return public, private

keys = newkeys(keysz)
for x in keys:
   print x.publickey()

# def importKey(externKey):
#    return RSA.importKey(externKey)
#
# def getpublickey(priv_key):
#    return priv_key.publickey()
#
# def encrypt(message, pub_key):
#    cipher = PKCS1_OAEP.new(pub_key)
#    return cipher.encrypt(message)

