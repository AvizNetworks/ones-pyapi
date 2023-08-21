## Health


### Importing module
```py
# Importing module
from restclient.telemetry.client import ONESClient 
```


### Initializing client 
```py
conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")
conn.connect() 
```

###  Calling Methods

Please Note, You can pass device_address or ip_address, both will work.


<b>Timeseries data for CPU utilization for a given device. </b>

```py
print("CPU_UTILIZATION")
query_params =  {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_cpu_utilization(query_params))
```

<b>Timeseries data for Memory utilization for a given device. </b>

```py
print("MEMORY_UTILIZATION")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_memory_utilization(query_params))
```

<b>Timeseries data for CPU cores temprature for a given device. </b>

```py
print("CPU_CORE_TEMPERATURE")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_cpu_core_temperaure(query_params))
```

<b>Timeseries data  of the temperature of PSUs for a given device. </b>

```py
print("PSU_TEMPERATURE")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_psu_temperature(query_params))
``` 

<b>Timeseries data of voltage readings on PSU for a given device. </b>

```py
print("PSU_VOLTAGE")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_psu_voltage(query_params))
```

<b> Timeseries data of current readings on PSU for a given device. </b>

```py
print("PSU_CURRENT")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_psu_current(query_params))
```

<b>Timeseries data for speed across all fans related to a device. </b>

```py
print("FAN_SPEED")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_fan_speed(query_params))
```


<b> Timeseries data of power readings on PSU for a given device. </b>

```py
print("PSU_POWER")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_psu_power(query_params))
```

<b>Timeseries data for CPU utilization across services for a given device </b>

```py
print("HEALTH_SERVICES_CPU")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_health_services_cpu(query_params))
```

<b>Timeseries data for Memory utilization across services for a given device </b>

```py
print("HEALTH_SERVICES_MEMORY")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_health_services_memory(query_params))
```

<b>Timeseries data of count of up and down status for bgp neighbours.</b>

```py
print("HEALTH_BGP NEIGHBORS")
query_params = {
  "fromDate" : "2023-04-04 04:54:27",
  "toDate" : "2023-04-04 05:54:27",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_health_bgp_neighbors(query_params))
```

<b>Timeseries data for transceiver connected to selected port. ( Rx/Tx power, temperature & Voltage).</b>

```py
print("HEALTH_TRANSCIEVERS")
query_params = {
  "ipAddress" : "10.x.x.x",
  "ifName" : "Ethernet0",
  "fromDate" : "2023-06-26 10:48:55",
  "toDate" : "2023-06-26 11:48:55"
}
print(conn.get_health_trancievers(query_params))
```

<b>Timeseries data of number of services running for a given device. </b>

```py
print("HEALTH_RUNNING_SERVICES")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_health_running_services(query_params))
```
