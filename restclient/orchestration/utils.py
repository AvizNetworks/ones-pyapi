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
from .exceptions import FMClientExpection
from .constants import *
import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

EXPECTED_APP_ERRORS = {400, 404, 409}

def handle_api_response(response, error_msg):
    try:
        try:
            content = response.json()
        except ValueError:
            content = response.text.strip()
            
        if response.status_code in [200, 201]:
            return content

        elif response.status_code in EXPECTED_APP_ERRORS:
            msg = content.get("message", content) if isinstance(content, dict) else content
            logging.error(f"{error_msg}")
            return {"status": response.status_code, "message": msg }
        else:
            # Unexpected HTTP status
            logging.error(f"Request failed: {response.status_code}")
            raise FMClientExpection(f"{error_msg} (HTTP {response.status_code})")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        raise FMClientExpection(f"{error_msg}: Unexpected error")
    
def get_request_handler(url, endpoint, error_msg, params=None):
    try:
        url = url + endpoint
        headers = {
            "Content-Type": "application/json",
        }

        if params:
            response = requests.get(url, headers=headers, params=params, verify=False, timeout=10)
        else:
            response = requests.get(url, headers=headers, verify=False, timeout=30)
        return handle_api_response(response,error_msg)
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        raise FMClientExpection(f"{error_msg}: Unexpected error")
    
    except Exception as err:
        # logging.error(err)
        raise FMClientExpection(error_msg)
    

def post_request_handler(url, endpoint, error_msg, payload):
    try:
        url = url + endpoint
        headers= {
            'Content-Type': 'application/json; charset=utf-8',
        }
        response = requests.post(url, headers=headers, json= payload, verify= False)
        return handle_api_response(response,error_msg)
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        raise FMClientExpection(f"{error_msg}: Unexpected error")

def patch_request_handler(url, endpoint, error_msg, payload):
    try:
        url = url + endpoint
        headers= {
            'Content-Type': 'application/json; charset=utf-8',
        }
        response = requests.patch(url, headers=headers, json= payload, verify= False)
        return handle_api_response(response,error_msg)
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        raise FMClientExpection(f"{error_msg}: Unexpected error")
    
    except Exception as err:
        logging.error(err)
        return FMClientExpection(error_msg)

def delete_request_handler(url, endpoint, error_msg):
    try:
        url = url + endpoint
        headers= {
            'Content-Type': 'application/json; charset=utf-8',
        }
        response = requests.delete(url, headers=headers, verify= False)
        return handle_api_response(response,error_msg)
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        raise FMClientExpection(f"{error_msg}: Unexpected error")
    
    except Exception as err:
        logging.error(err)
        return FMClientExpection(error_msg)