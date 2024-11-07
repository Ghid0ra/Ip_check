import json
import subprocess
import re
from logging import exception

from mako.compat import exception_as

ips = input("Give file path : ")
api = '' #Enter Your API Key Here

#Function to loop through file and check the ips listed in it.
def ipcheck():
    try:
        with open(ips, 'r') as file:
            print('\n')
            for line in file:
                ip = line.strip()
                cmd = subprocess.run(f"curl ipinfo.io/{ip}?token={api}", shell=True, capture_output=True, text=True,
                                     check=True)
                parse = json.loads(cmd.stdout)
                print(parse["org"])
    except IOError:
        print('Error : File not found')

#prompt to change api key
key = input('Do you want to change the API key? Y/N? :')
if re.findall(r'y', key, re.IGNORECASE):
    #get the new api key and run the code
    new_api= input("Enter the new API Key : ")
    try:
        with open(ips, 'r') as file:
            print('\n')
            for line in file:
                ip = line.strip()
                cmd = subprocess.run(f"curl ipinfo.io/{ip}?token={new_api}", shell=True, capture_output=True, text=True,
                                     check=True)
                parse = json.loads(cmd.stdout)
                print(parse["org"])
    except IOError:
        print('Error : File not found')

# run the ips in the file with old api
elif re.findall(r'n', key, re.IGNORECASE):
    ipcheck()
