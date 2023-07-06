## Calling Methods For Health APIs

#### FAULTY_PSUs
``` py
print("....................FAULTY_PSUs.....................")
print(conn.get_faulty_psus())
print("....................FAULTY_PSUSs.....................")
```
#### FAULTY_FANS
``` py
print("....................FAULTY_FANS.....................")
print(conn.get_faulty_fans())
print("....................FAULTY_FANS.....................")
```
#### LINK_FLAPS
```py
print("....................LINK_FLAPS.....................")
query_params= {
  "time" : "5 minutes",
  "limit" : "10"
}
print(conn.get_link_flaps(query_params))
print("....................LINK_FLAPS.....................")
```
#### CPU_UTILIZATION
``` py
print("....................CPU_UTILIZATION....................")
query_params =  {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_cpu_utilization(query_params))
print("....................CPU_UTILIZATION.....................")
```
#### MEMORY_UTILIZATION
```py
print("....................MEMORY_UTILIZATION....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_memory_utilization(query_params))
print("....................MEMORY_UTILIZATION.....................")
```
#### CPU_CORE_TEMPERATURE
``` py
print("....................CPU_CORE_TEMPERATURE....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_cpu_core_temperaure(query_params))
print("....................CPU_CORE_TEMPERATURE.....................")
```
#### PSU_TEMPERATURE
``` py
print("....................PSU_TEMPERATURE....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_psu_temperature(query_params))
print("....................PSU_TEMPERATURE....................")
```
#### PSU_VOLTAGE
``` py
print("....................PSU_VOLTAGE....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_psu_voltage(query_params))
print("....................PSU_VOLTAGE....................")
```
#### PSU_CURRENT
``` py
print("....................PSU_CURRENT....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_psu_current(query_params))
print("....................PSU_CURRENT....................")
```
#### FAN_SPEED
``` py
print("....................FAN_SPEED....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_fan_speed(query_params))
print("....................FAN_SPEED....................")
```
#### PSU_POWER
``` py
print("....................PSU_POWER....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_psu_power(query_params))
print("....................PSU_POWER....................")
```
#### HEALTH_SERVICES_CPU
``` py
print("....................HEALTH_SERVICES_CPU....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_health_services_cpu(query_params))
print("....................HEALTH_SERVICES_CPU....................")
```
#### HEALTH_SERVICES_MEMORY
``` py
print("....................HEALTH_SERVICES_MEMORY....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_health_services_memory(query_params))
print("....................HEALTH_SERVICES_MEMORY....................")
```
#### HEALTH_BGP_NEIGHBORS
``` py
print("....................HEALTH_BGP NEIGHBORS....................")
query_params = {
  "fromDate" : "2023-04-04 04:54:27",
  "toDate" : "2023-04-04 05:54:27",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_health_bgp_neighbors(query_params))
print("....................HEALTH_BGP_NEIGHBORS....................")
```
#### HEALTH_TRANSCIEVERS
```py
print("....................HEALTH_TRANSCIEVERS....................")
query_params = {
  "ipAddress" : "10.4.4.55",
  "ifName" : "Ethernet0",
  "fromDate" : "2023-06-26 10:48:55",
  "toDate" : "2023-06-26 11:48:55"
}
print(conn.get_health_trancievers(query_params))
print("....................HEALTH_TRANSCIEVERS....................")
```
#### HEALTH_RUNNING_SERVICES
``` py
print("....................HEALTH_RUNNING_SERVICES....................")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.4.4.55"
}
print(conn.get_health_running_services(query_params))
print("....................HEALTH_RUNNING_SERVICES....................")
```