import sys
sys.path.append('..')
from onesclient.client import ONESClient

# Connecting to APIs

# Initializing client
conn  = ONESClient(url ='https://10.2.2.6', username="superadmin", password="Admin@123")


# Calling Methods
print("....................HARDWARE_INFO!!.....................")
print(conn.connect())
print(conn.get_hardware_info())
print("....................HARDWARE_INFO!!.....................")


print("....................ROLES.....................")
# print(conn.connect())
print(conn.get_roles())
print("....................ROLES.....................")