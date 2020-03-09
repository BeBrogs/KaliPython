#!usr/bin/python

import pdb
import hashlib
#Importing hashing library contains SECURE hash & message algorithm >

#Taking something to hash

toHash = input ("Please enter what you want to hash: \n")

 
#Cracked
md5 = hashlib.md5()
md5.update(toHash.encode()) #Passing encoded toHash to our dic 
print ("\nYour input in MD5 hash: \nHexDigest: \n" + str(md5.hexdige>
print ("Digest: \n" + str(md5.digest()))
 
#Digest is the binary hash, hexdigest is the string hash
 
#Cracked
mySha1 = hashlib.sha1()
mySha1.update(toHash.encode())
print ("\n\nIn SHA1: \n"+ str(mySha1.hexdigest()))
print ("Digest: \n" + str(mySha1.digest()))


print ("\n\nSHA2 Hashes: ")
#SHA2 - Common hashes, secure for now - likely to be broken - matter>
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

                                                         print ("\n\nSHA3 Hashes: ")
#SHA3 - introduced by NIST as backup plan for when SHA2 Cracks w/ sp>
#SHA3 is unlikely to be broken anytime soon
mySHA3_256 = hashlib.sha3_256()
mySHA3_256.update(toHash.encode())
print ("\n\nSHA3-256: \n" + str(mySHA3_256.hexdigest()))
print("Digest: \n" + str(mySHA3_256.digest()))


mySHA3_512 = hashlib.sha3_512()
mySHA3_512.update(toHash.encode())
print ("\n\nSHA3-512: \n" + str(mySHA3_512.hexdigest()))
print("Digest: \n" + str(mySHA3_512.digest()))

#ElFin

