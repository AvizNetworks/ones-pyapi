from restclient.orchestration.client import FMClient
import logging

conn = FMClient(url = "http://10.x.x.x:8787")

fabric_name = input("Enter Fabric Name: ")

try:
    result = conn.list_tenants(fabric_name)
    print(result)
except Exception as e:
    logging.error(str(e))