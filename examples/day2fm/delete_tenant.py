from restclient.orchestration.client import FMClient
import logging
import re

def valid_tenant_name(tenant_name):
    if not (3 <= len(tenant_name) <= 45):
        return False
    pattern = re.compile(r'^[A-Za-z][A-Za-z0-9_-]*$')
    return bool(pattern.fullmatch(tenant_name))

conn = FMClient(url = "http://10.x.x.x:8787")

fabric_name = input("Enter Fabric Name: ")
tenant_name = input("Enter Tenant Name: ")
if not valid_tenant_name(tenant_name):
    raise ValueError("Invalid tenant name. It must be 3-45 characters long, start with a letter, and contain only letters, numbers, underscores and hyphens.")

try:
    result = conn.delete_tenant(fabric_name, tenant_name)
    print(result)
except Exception as e:
    logging.error(str(e))