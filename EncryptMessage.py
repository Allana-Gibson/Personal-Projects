from cryptography.fernet import Fernet

#First get the key from the imported file
file = open('key.file', 'rb')
key = file.read()
file.close()

#this will encode the message
message = "Hello! This is my secret message"
encoded = message.encode() #this converts the message to bytes

#this will encrypt the message
f = Fernet(key)
encrypted = f.encrypt(encoded)
print (encrypted)

# saves encrypted message into file
file = open('encrypted.message', 'wb')
file.write(encrypted)
file.close()
