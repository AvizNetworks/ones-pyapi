# Importing neccessery modules
import logging
import json
import requests

# importing endpoints
from .endpoints import *

from .excpetions import OnesClientExpection
from .constants import *
from .util import request_handler, request_handler_with_payload, request_handler_with_query_params


# Loading Environment Variables
# from dotenv import load_dotenv
# load_dotenv()


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

    def get_hardware_info(self):
        """
            This function will return all Hardware Info
            Includes the following Details
            Devices, Regions, SwitchSKUs, Role and ASICs
        """
        try:
            url = self.url + hardware_info
            headers = {
                "Authorization": self.access_token,
                "Content-Type": "application/json",
            }
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                res = response.json()
                print(json.dumps(res, indent=4))
                return True
            else:
                raise OnesClientExpection(HARDWARE_INFO_ERROR)

        except Exception as err:
            logging.error(f"Error -> ${err}")
            raise OnesClientExpection(HARDWARE_INFO_ERROR)

        
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
        
    def get_switch_skus(self):
        """
        Return all switch SKUs
        """
        request_handler(self.url, switch_skus, self.access_token, None)

    def get_asics_info(self):
        """
        Return all ASICs info
        """
        request_handler(self.url, asics, self.access_token, None)

    def get_agent_version(self):
        """
        Return Agent version
        """
        request_handler(self.url, agent_version, self.access_token, None)

    def get_nos_version(self):
        """
        Return NOS version
        """
        request_handler(self.url, nos_version, self.access_token, None)

    def get_linux_version(self):
        """
        Return linux version
        """
        request_handler(self.url, linux_version, self.access_token, None)

    def get_onie_version(self):
        """
        Return ONIE version
        """
        request_handler(self.url, onie_version, self.access_token, None)

    def get_cabling_info(self):
        """
        Return cabling INFO
        """
        request_handler(self.url, cabling, self.access_token, None)

    def get_device_interfaces(self, arg1):
        """
        Payload -> "filter": {
                 "deviceAddress": "0c:29:ef:ce:92:20"
                }
        Output -> List of interfaces of a device
        """
        request_handler_with_payload(self.url, device_interfaces, self.access_token, None, arg1)

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

    def get_device_info(self,arg1):
        """
        query_params -> {"ipAddress": "10.4.4.61"}
        Output -> List of device info
        """
        request_handler_with_query_params(self.url, device_info_endpoint, self.access_token,None, arg1)

        

    
    