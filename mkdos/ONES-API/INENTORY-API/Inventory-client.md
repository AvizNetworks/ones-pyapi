### Importing necessary modules
``` py
import logging
import json
import requests
```
### Importing Endpoints
``` py
from .endpoints import *

from .excpetions import OnesClientExpection
from .constants import *
from .util import request_handler, request_handler_with_payload, request_handler_with_query_params
```

### Connect ONESclient
``` py
class ONESClient(object):
    def __init__(self, username=None, password=None, url=None):
        self.username = username
        self.password = password
        self.url = url
        self.access_token = None

    def connect(self):
        """
            This method will use to make connection
            with Ones API,
            It will use user, url,password, and  Authentication API
        """
        try:
            url = self.url + connect

            payload = {"username": self.username, "password": self.password}

            payload = json.dumps(payload)
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                url, data=payload, headers=headers, verify=False
            )
            if response.status_code == 200:
                temp = response.json()
                access_token = temp["data"]["token"]
                logging.debug(access_token)
                self.access_token = access_token

            else:
                logging.error("Something went wrong")

        except Exception as err:
            logging.error(f"Error -> ${err}")
            raise OnesClientExpection()
```
#### get_device_info
``` py
 def get_device_info(self,arg1):
        """
        query_params -> {"ipAddress": "10.4.4.61"}
        Output -> List of device info
        """
        request_handler_with_query_params(self.url, device_info_endpoint, self.access_token,None, arg1)
```
#### get_device_peripherals
``` py
 def get_device_peripherals(self, arg1):
        """
        query_params -> "filter": {
                    {
                    "deviceAddress" : "0c:29:ef:ce:92:20"
                    }
            }
        Output -> List of peripherals
        """
        request_handler_with_query_params(self.url, device_peripherals, self.access_token, None, arg1)
```
#### get_device_interfaces
``` py
def get_device_interfaces(self, arg1):
        """
        Payload -> "filter": {
                 "deviceAddress": "0c:29:ef:ce:92:20"
                }
        Output -> List of interfaces of a device
        """
        request_handler_with_payload(self.url, device_interfaces, self.access_token, None, arg1)
```
#### get_device_roles
``` py
def get_roles(self):
        """
        This function will return all existings roles
                Spine
                SuperSpine
                Tor
                Leaf
        """
        try:
            url = self.url + roles
            headers = {
                "Authorization": self.access_token,
                "Content-Type": "application/json",
            }
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                res = response.json()
                print(json.dumps(res, indent=4))
                return True
        except Exception as err:
            logging.error(err)
            raise OnesClientExpection(ROLES_ERROR)
```
#### get_switch_skus
``` py
 def get_switch_skus(self):
        """
        Return all switch SKUs
        """
        request_handler(self.url, switch_skus, self.access_token, None)
```
#### get_asics_info
``` py
def get_asics_info(self):
        """
        Return all ASICs info
        """
        request_handler(self.url, asics, self.access_token, None)
```
#### get_agent_version
``` py
    def get_agent_version(self):
        """
        Return Agent version
        """
        request_handler(self.url, agent_version, self.access_token, None)
```
#### get_nos_version
``` py
def get_nos_version(self):
        """
        Return NOS version
        """
        request_handler(self.url, nos_version, self.access_token, None)
```
#### get_linux_version
``` py
def get_linux_version(self):
        """
        Return linux version
        """
        request_handler(self.url, linux_version, self.access_token, None)
```
#### get_onie_version
``` py
 def get_onie_version(self):
        """
        Return ONIE version
        """
        request_handler(self.url, onie_version, self.access_token, None)
```
#### get_cabling_info
``` py
def get_cabling_info(self):
        """
        Return cabling INFO
        """
        request_handler(self.url, cabling, self.access_token, None)
```