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
from exceptions import FMClientExpection
from constants import *
import logging

def get_request_handler(url, endpoint, error_msg, params):
    try:
        url = url + endpoint
        headers = {
            "Content-Type": "application/json",
        }

        # Request coming with params
        if params != None:
            params = params
            response = requests.get(url, headers=headers, params=params)

        # Request coming without params
        else:
            response = requests.get(url, headers=headers, verify=False)

        res = response.json()
        return res
    
    except Exception as err:
        logging.error(err)
        raise FMClientExpection(error_msg)
    

def post_request_handler(url, endpoint, error_msg, payload):
    try:
        url = url + endpoint
        headers= {
            'Content-Type': 'application/json; charset=utf-8',
        }
        response = requests.post(url, headers=headers, json= payload, verify= False)
        res = response.json()
        return res
    
    except Exception as err:
        logging.error(err)
        return FMClientExpection(error_msg)

