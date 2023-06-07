# Loading env variables
from dotenv import load_dotenv
load_dotenv()

# Loading neccessary modules
import os
import sys
import logging

# Using relative path for importing files from
# Multiple location
sys.path.append("..")
from OnesClient.client import ONESClient

"""
    This is the testing client for checking the working of SDK.
    Step - 1 Creating ONESClient called my_client
    Step - 2 Calling connect function for login and extablishing a connecting
            with ONSS APIs
    Step -3 Calling get_hardware_info, it will return all details related to
            Device, roles, skus, regions and ASICs
"""

logging.debug("Running Program")
print("Connecting with client")
my_client = ONESClient(
    url=os.getenv("API_ENDPOINT"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
)

print("Login...")
my_client.connect()
print("Login Successfully..")

print("getting Hardware Details...")
my_client.get_hardware_info()
