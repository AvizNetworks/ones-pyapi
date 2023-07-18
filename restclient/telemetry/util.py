"""
Copyright (c) 2023, Aviz Networks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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