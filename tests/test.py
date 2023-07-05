import sys
sys.path.append('..')
from onesclient.client import ONESClient

# Connecting to APIs

# Initializing client
conn  = ONESClient(url ='https://10.2.2.6', username="superadmin", password="Admin@123")

# Login and AccessToken generation
conn.connect() 

# Calling Methods
# print("....................HARDWARE_INFO!!.....................")
# print(conn.get_hardware_info())
# print("....................HARDWARE_INFO!!.....................")


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

print("....................NETWORK_TOPOLOGY_INFO!!.....................")
print(conn.get_network_topology())
print("....................NETWORK_TOPOLOGY_INFO!!.....................")


print("....................CPU_UTILIZATION....................")
query_params =  {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_cpu_utilization(query_params))
print("....................CPU_UTILIZATION.....................")


print("....................MEMORY_UTILIZATION....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_memory_utilization(query_params))
print("....................MEMORY_UTILIZATION.....................")


print("....................CPU_CORE_TEMPERATURE....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_cpu_core_temperaure(query_params))
print("....................CPU_CORE_TEMPERATURE.....................")


print("....................PSU_TEMPERATURE....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_psu_temperature(query_params))
print("....................PSU_TEMPERATURE....................")


print("....................PSU_VOLTAGE....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_psu_voltage(query_params))
print("....................PSU_VOLTAGE....................")


print("....................PSU_CURRENT....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_psu_current(query_params))
print("....................PSU_CURRENT....................")


print("....................FAN_SPEED....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_fan_speed(query_params))
print("....................FAN_SPEED....................")


print("....................PSU_POWER....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_psu_power(query_params))
print("....................PSU_POWER....................")


print("....................HEALTH_SERVICES_CPU....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_health_services_cpu(query_params))
print("....................HEALTH_SERVICES_CPU....................")


print("....................HEALTH_SERVICES_MEMORY....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_health_services_memory(query_params))
print("....................HEALTH_SERVICES_MEMORY....................")


print("....................HEALTH_BGP NEIGHBORS....................")
query_params = {
  "fromDate" : "2023-04-04 04:54:27",
  "toDate" : "2023-04-04 05:54:27",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_health_bgp_neighbors(query_params))
print("....................HEALTH_BGP_NEIGHBORS....................")


print("....................HEALTH_TRANSCIEVERS....................")
query_params = {
  "ipAddress" : "10.4.4.55",
  "ifName" : "Ethernet0",
  "fromDate" : "2023-06-26 10:48:55",
  "toDate" : "2023-06-26 11:48:55"
}
print(conn.get_health_trancievers(query_params))
print("....................HEALTH_TRANSCIEVERS....................")


print("....................HEALTH_RUNNING_SERVICES....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_health_running_services(query_params))
print("....................HEALTH_RUNNING_SERVICES....................")


print("....................TRAFFIC_UTIL....................")
query_params = {
    "fromDate" : "2023-04-04 04:54:27",
    "toDate" : "2023-04-04 05:54:27",
    "deviceAddress" : "10.4.4.55",
    "ifname" : "Ethernet0"
}
print(conn.get_traffic_util(query_params))
print("....................TRAFFIC_UTIL....................")


print("....................TRAFFIC_COUNTERS....................")
query_params = {
    "fromDate" : "2023-04-04 04:54:27",
    "toDate" : "2023-04-04 05:54:27",
    "deviceAddress" : "10.4.4.55",
    "ifname" : "Ethernet0"
}
print(conn.get_traffic_counters(query_params))
print("....................TRAFFIC_COUNTERS....................")

# print("....................Device_INFO....................")
# query_params  =  {"ipAddress": "10.4.4.61"}
# print(conn.get_device_info(query_params))
# print("....................Device_INFO.....................")


print("....................FAULTY_PSUs.....................")
print(conn.get_faulty_psus())
print("....................FAULTY_PSUSs.....................")


print("....................FAULTY_FANS.....................")
print(conn.get_faulty_fans())
print("....................FAULTY_FANS.....................")


print("....................LINK_FLAPS.....................")
query_params= {
  "time" : "5 minutes",
  "limit" : "10"
}
print(conn.get_link_flaps(query_params))
print("....................LINK_FLAPS.....................")


































