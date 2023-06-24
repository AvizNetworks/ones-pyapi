import sys
sys.path.append('..')
from onesclient.client import ONESClient

# Connecting to APIs

# Initializing client
conn  = ONESClient(url ='https://10.2.2.6', username="superadmin", password="Admin@123")

# Login and AccessToken generation
conn.connect() 

# Calling Methods
print("....................HARDWARE_INFO!!.....................")
print(conn.get_hardware_info())
print("....................HARDWARE_INFO!!.....................")


print("....................ROLES.....................")
print(conn.get_roles())
print("....................ROLES.....................")


print("....................SWITCH_SKUs.....................")
print(conn.get_switch_skus())
print("....................SWITCH_SKUs.....................")


print("....................ASICS_INFO.....................")
print(conn.get_asics_info())
print("....................ASICS_INFO.....................")


print("....................AGENT_IFNO.....................")
print(conn.get_agent_version())
print("....................AGENT_INFO.....................")


print("....................NOS_VERSION.....................")
print(conn.get_nos_version())
print("....................NOS_VERSION.....................")


print("....................LINUX_INFO.....................")
print(conn.get_linux_version())
print("....................LINUX_VERSION.....................")


print("....................ONIE_VERSION.....................")
print(conn.get_onie_version())
print("....................ONIE_VERSION.....................")


print("....................CABLING_INFO.....................")
print(conn.get_cabling_info())
print("....................CABLING_INFO.....................")


print("....................Device_Interfaces.....................")
payload  =  {
  "filter": {
    "deviceAddress": "0c:29:ef:ce:92:20"
  }
}
print(conn.get_device_interfaces(payload))
print("....................Device_Interfaces.....................")


print("....................Device_Peripherals....................")
query_params  =  {"deviceAddress" : "0c:29:ef:ce:92:20"}
print(conn.get_device_peripherals(query_params))
print("....................Device_Peripherals.....................")


print("....................Device_INFO....................")
query_params  =  {"ipAddress": "10.4.4.61"}
print(conn.get_device_info(query_params))
print("....................Device_INFO.....................")

print("....................NETWORK_TOPOLOGY_INFO!!.....................")
print(conn.get_network_topology())
print("....................NETWORK_TOPOLOGY_INFO!!.....................")




