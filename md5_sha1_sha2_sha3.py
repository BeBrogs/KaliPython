#!usr/bin/python

import pdb
import hashlib
#Importing hashing library contains SECURE hash & message algorithm for MD5/RFC-1321 SHA1 224 256 384 512

#Taking something to hash

toHash = input ("Please enter what you want to hash: \n")

#Cracked
md5 = hashlib.md5()
md5.update(toHash.encode()) #Passing encoded toHash to our dic 
print ("\nYour input in MD5 hash: \nHexDigest: \n" + str(md5.hexdigest())) #Hex Digesting str fed
print ("Digest: \n" + str(md5.digest()))

#Cracked
mySha1 = hashlib.sha1()
mySha1.update(toHash.encode())
print ("\n\nIn SHA1: \n"+ str(mySha1.hexdigest()))
print ("Digest: \n" + str(mySha1.digest()))


#SHA2 - Common hashes, secure for now - likely to be broken - matter of time
mySha224 = hashlib.sha224()
mySha224.update(toHash.encode())
print ("\n\nIn SHA224: \n" +str(mySha224.hexdigest()))
print ("Digest: \n" + str(mySha224.digest()))

mySha256 = hashlib.sha256()
mySha256.update(toHash.encode())
print ("\n\nIn SHA265: \n" +str(mySha256.hexdigest())) 
print ("Digest: \n" + str(mySha256.digest()))

mySha384 = hashlib.sha384()
mySha384.update(toHash.encode())
print ("\n\nIn SHA384: \n" + str(mySha384.hexdigest()))
print("Digest: \n" + str(mySha384.digest()))

mySha512 = hashlib.sha512()
mySha512.update(toHash.encode())
print ("\n\nIn SHA512: \n" + str(mySha512.hexdigest()))
print ("Digest: \n" + str(mySha512.digest()))

#SHA3 - introduced by NIST as backup plan for when SHA2 Cracks w/ sponge function different from sha 2 & 1
#mySHA3_256 = hashlib.sha3_256()
#mySHA3_256.update(toHash.encode())
#print ("\n\nSHA3-256" + str(mySHA3_256.hexdigest()))
#print ("Digest: \n" + str(mySHA3_256.digest()))
