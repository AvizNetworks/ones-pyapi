## Calling Methods for Inventory APIs

#### HARDWARE_INFO
``` py
print("....................HARDWARE_INFO!!.....................")
print(conn.get_hardware_info())
print("....................HARDWARE_INFO!!.....................")
```
#### ROLES
``` py
print("....................ROLES.....................")
print(conn.get_roles())
print("....................ROLES.....................")
```
#### SWICH_SKUs
``` py
print("....................SWITCH_SKUs.....................")
print(conn.get_switch_skus())
print("....................SWITCH_SKUs.....................")
```
#### ASICS_INFO
``` py
print("....................ASICS_INFO.....................")
print(conn.get_asics_info())
print("....................ASICS_INFO.....................")
```
#### AGENT_INFO
``` py
print("....................AGENT_IFNO.....................")
print(conn.get_agent_version())
print("....................AGENT_INFO.....................")
```
#### NOS_VERSION
```py
print("....................NOS_VERSION.....................")
print(conn.get_nos_version())
print("....................NOS_VERSION.....................")
```
#### LINUX_VERSION
``` py
print("....................LINUX_INFO.....................")
print(conn.get_linux_version())
print("....................LINUX_VERSION.....................")
```
#### ONIE_VERSION
```py
print("....................ONIE_VERSION.....................")
print(conn.get_onie_version())
print("....................ONIE_VERSION.....................")
```
#### CABLING_INFO
```py
print("....................CABLING_INFO.....................")
print(conn.get_cabling_info())
print("....................CABLING_INFO.....................")
```
#### DEVICE_INTERFACES
```py
print("....................Device_Interfaces.....................")
payload  =  {
  "filter": {
    "deviceAddress": "0c:29:ef:ce:92:20"
  }
}
print(conn.get_device_interfaces(payload))
print("....................Device_Interfaces.....................")
```
#### DEVICE_PERIPHERALS
```py
print("....................Device_Peripherals....................")
query_params  =  {"deviceAddress" : "0c:29:ef:ce:92:20"}
print(conn.get_device_peripherals(query_params))
print("....................Device_Peripherals.....................")
```
#### DEVICE_INFO
``` py
print("....................Device_INFO....................")
query_params  =  {"ipAddress": "10.4.4.61"}
print(conn.get_device_info(query_params))
print("....................Device_INFO.....................")
```