# Importing neccessery modules
import os
import logging
import json
import requests


# Loading Environment Variables
from dotenv import load_dotenv
load_dotenv()


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
            cert_file = os.getenv("CERT_FILE_PATH")
            url = self.url + "/api/user/login"

            payload = {"username": self.username, "password": self.password}

            payload = json.dumps(payload)
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                url, data=payload, headers=headers, verify=cert_file
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
            return {"msg": "Something went wrong"}

    def get_hardware_info(self):
        """
            This function will return all Hardware Info
            Includes the following Details
            Devices, Regions, SwitchSKUs, Role and ASICs
        """
        try:
            cert_file = os.getenv("CERT_FILE_PATH")
            url = self.url + "/api/inventory/hardwareMega"
            headers = {
                "Authorization": self.access_token,
                "Content-Type": "application/json",
            }
            response = requests.get(url, headers=headers, verify=cert_file)
            if response.status_code == 200:
                res = response.json()
                print(json.dumps(res, indent=4))
                return True
            else:
                print(response.status_code)
                return False

        except Exception as err:
            logging.error(f"Error -> ${err}")
            return False
