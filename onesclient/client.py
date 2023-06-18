# Importing neccessery modules
import logging
import json
import requests

# importing endpoints
from .endpoints import *

from .excpetions import OnesClientExpection
from .constants import *


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
        
