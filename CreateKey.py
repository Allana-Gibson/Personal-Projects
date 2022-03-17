# this script creates the key to encrypt and decrypt with

from cryptography.fernet import Fernet
key = Fernet.generate_key() #this generates a random key each time its called
print(key)

# so we need to write the key to a file so we use the same one each time
file = open('key.file', 'wb')
file.write(key) #key is a byte and it stores it into a file
file.close()
