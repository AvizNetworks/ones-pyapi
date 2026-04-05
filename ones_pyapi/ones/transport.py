# ones/transport.py

import requests
import logging
from .exceptions import OnesClientException


class Transport:
    def __init__(self, base_url, token=None, timeout=10, verify=False):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout
        self.verify = verify

        self.session = requests.Session()

    def set_token(self, token):
        self.token = token

    def request(self, method, path, params=None, json=None):
        url = f"{self.base_url}{path}"

        print(f"REQUEST: {method} {url}")

        headers = {"Content-Type": "application/json"}

        if self.token:
            headers["Authorization"] = self.token   # keep as-is (your backend expects this)

        try:
            resp = self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                timeout=self.timeout,
                verify=self.verify,
            )

            if resp.status_code not in (200, 201):
                logging.error(f"Request failed: {method} {url} - Status: {resp.status_code} - Response: {resp.text}")
                return None

            try:
                return resp.json()
            except Exception:
                logging.error(f"No JSON data returned: {resp.text}")
                return None   # or {} if you prefer

        except Exception as e:
            logging.error(e)
            raise OnesClientException(str(e))