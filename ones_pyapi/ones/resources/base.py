# ones/resources/base.py

import json


class BaseResource:
    def __init__(self, transport):
        self.transport = transport

    def _get(self, path, filters=None):
        params = None
        if filters:
            params = {"filter": json.dumps(filters)}
        return self.transport.request("GET", path, params=params)

    def _post(self, path, payload=None):
        return self.transport.request("POST", path, json=payload)

    def _put(self, path, payload=None):
        return self.transport.request("PUT", path, json=payload)

    def _delete(self, path):
        return self.transport.request("DELETE", path)
    