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
operation = input("Enter Operation (ADD/DELETE): ").strip().upper()
servers_input = input("Enter Servers (comma-separated): ")
payload = {
    "operation": operation,
   "servers": [server.strip() for server in servers_input.split(",") if server.strip()]
}

try:
    result = conn.update_tenant_gpus(fabric_name, tenant_name, payload)
    print(result)
except Exception as e:
    logging.error(str(e))