from cryptography.fernet import Fernet

#First get the key from the imported file
file = open('key.file', 'rb')
key = file.read()
file.close()

#Then get the encrypted message
file = open('encrypted.message', 'rb')
message = file.read()
file.close()

#This decrypts the encrypted message
f2 = Fernet(key)
decrypted = f2.decrypt(message)

#this decodes the message from byte to sting
original_message = decrypted.decode()
print(original_message)


#saves ogininal message into a file
file = open('original.message', 'wb')
file.write(decrypted)
file.close()
