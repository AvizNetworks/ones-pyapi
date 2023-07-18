import requests
from .excpetions import OnesClientExpection
from .constants import *
import logging
import json


def request_handler(url, endpoint_name, access_token, error_msg):
    try:
        url = url + endpoint_name
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            res = response.json()
            print(json.dumps(res, indent=4))
            return True
        else:
            logging.error(err)
            raise OnesClientExpection(error_msg)

    except Exception as err:
        logging.error(err)
        raise OnesClientExpection(error_msg)


def request_handler_with_payload(url, endpoint_name, access_token, error_msg, payload):
    try:
        url = url + endpoint_name
        headers = {"Authorization": access_token, "Content-Type": "application/json"}
        response = requests.post(url, headers=headers, json=payload, verify=False)
        if response.status_code == 200:
            res = response.json()
            print(json.dumps(res, indent=4))
            return True
        else:
            logging.error(error_msg)
            raise OnesClientExpection(error_msg)

    except Exception as err:
        logging.error(err)
        raise OnesClientExpection(err)


def request_handler_with_query_params(url, endpoint_name, access_token, error_msg, params):

    try:
        url = url + endpoint_name 
        headers = {"Authorization": access_token, "Content-Type": "application/json"}

        # This is for making query url as per our current Backend structure
        if endpoint_name == "/api/inventory/Devices/device":
            params = params
        else:
            params = json.dumps(params)
            params = "filter=" + params

        response = requests.get(url, headers=headers, params=params, verify=False)
        
        if response.status_code == 200:
            res = response.json()
            print(json.dumps(res, indent=4))
            return True
        else:
            logging.error(error_msg)
            raise OnesClientExpection(error_msg)

    except Exception as err:
        logging.error(err)
        raise OnesClientExpection(err)