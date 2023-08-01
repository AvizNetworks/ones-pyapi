# Secured APIs for NetOps Monitoring

This provides 3rd party or customer tools integration with the ONES API SDK in python which underlying uses the REST interfaces provided by the ONES application 

## Telemetry Examples
This is how we can use telemetry apis and use its value for further process.

```py
# Importing module
from restclient.telemetry.client import ONESClient 
```


## Initializing client 
```py
conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")
```
## Login and AccessToken generation
```py
conn.connect() 
```

##  Calling Methods

Please Note, You can pass device_address or ip_address, both will work.

### Hardware Info
```py
print("Hardware Info")
print(conn.get_hardware_info())
```

### Roles
```py
print("Roles")
print(conn.get_roles())
```

### SWITCH_SKUs
```py
print("SWITCH_SKUs")
print(conn.get_switch_skus())
```

### ASICS_INFO
```py
print("ASICS_INFO")
print(conn.get_asics_info())
```

### AGENT_IFNO.
```py
print("AGENT_IFNO.")
print(conn.get_agent_version())
```

### NOS_VERSION.
```py
print("NOS_VERSION.")
print(conn.get_nos_version())
```

### LINUX_INFO.
```py
print("LINUX_INFO.")
print(conn.get_linux_version())
```

### ONIE_VERSION.
```py
print("ONIE_VERSION.")
print(conn.get_onie_version())
```

### CABLING_INFO.
```py
print("CABLING_INFO.")
print(conn.get_cabling_info())
```

### Device_Interfaces.
```py
print("Device_Interfaces.")
payload = {
  "filter": {
    "deviceAddress": "0c:xx:xx:xx:xx:x0"
  }
}
print(conn.get_device_interfaces(payload))
```

### Device_Peripherals
```py
print("Device_Peripherals")
query_params = {"deviceAddress": "0c:xx:xx:xx:xx:x0"}
print(conn.get_device_peripherals(query_params))
```

### NETWORK_TOPOLOGY_INFO!!
```py
print("NETWORK_TOPOLOGY_INFO!!.")
print(conn.get_network_topology())
```

### CPU_UTILIZATION
```py
print("CPU_UTILIZATION")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_cpu_utilization(query_params))
```

### MEMORY_UTILIZATION
```py
print("MEMORY_UTILIZATION")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_memory_utilization(query_params))
```

### CPU_CORE_TEMPERATURE
```py
print("CPU_CORE_TEMPERATURE")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_cpu_core_temperaure(query_params))
```

### PSU_TEMPERATURE
```py
print("PSU_TEMPERATURE")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_psu_temperature(query_params))
```

### PSU_VOLTAGE
```py
print("PSU_VOLTAGE")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_psu_voltage(query_params))
```

### PSU_CURRENT
```py
print("PSU_CURRENT")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_psu_current(query_params))
```

### FAN_SPEED
```py
print("FAN_SPEED")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_fan_speed(query_params))
```

### PSU_POWER
```py
print("PSU_POWER")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_psu_power(query_params))
```

### HEALTH_SERVICES_CPU
```py
print("HEALTH_SERVICES_CPU")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_health_services_cpu(query_params))
```

### HEALTH_SERVICES_MEMORY
```py
print("HEALTH_SERVICES_MEMORY")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_health_services_memory(query_params))
```

### HEALTH_BGP_NEIGHBORS
```py
print("HEALTH_BGP_NEIGHBORS")
query_params = {
  "fromDate": "2023-04-04 04:54:27",
  "toDate": "2023-04-04 05:54:27",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_health_bgp_neighbors(query_params))
```

### HEALTH_TRANSCIEVERS
```py
print("HEALTH_TRANSCIEVERS")
query_params = {
  "ipAddress": "10.x.x.x",
  "ifName": "Ethernet0",
  "fromDate": "2023-06-26 10:48:55",
  "toDate": "2023-06-26 11:48:55"
}
print(conn.get_health_trancievers(query_params))
```

### HEALTH_RUNNING_SERVICES
```py
print("HEALTH_RUNNING_SERVICES")
query_params = {
  "fromDate": "2023-05-12 11:55:24",
  "toDate": "2023-05-12 12:55:24",
  "deviceAddress": "10.x.x.x"
}
print(conn.get_health_running_services(query_params))
```

### TRAFFIC_UTIL
```py
print("TRAFFIC_UTIL")
query_params = {
    "fromDate": "2023-04-04 04:54:27",
    "toDate": "2023-04-04 05:54:27",
    "deviceAddress": "10.x.x.x",
    "ifname": "Ethernet0"
}
print(conn.get_traffic_util(query_params))
```

### TRAFFIC_COUNTERS
```py
print("TRAFFIC_COUNTERS")
query_params = {
    "fromDate": "2023-04-04 04:54:27",
    "toDate": "2023-04-04 05:54:27",
     "deviceAddress" : "10.x.x.x",
    "ifname" : "Ethernet0"
}
print(conn.get_traffic_counters(query_params))
```

### FAULTY_PSUs.
```py
print("FAULTY_PSUs.")
print(conn.get_faulty_psus())
```

### FAULTY_FANS.
```py
print("FAULTY_FANS.")
print(conn.get_faulty_fans())
```

### LINK_FLAPS.
```py
print("LINK_FLAPS.")
query_params = {
  "time": "5 minutes",
  "limit": "10"
}
print(conn.get_link_flaps(query_params))
```




