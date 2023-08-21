## Traffic

<b> Import Client </b>

```py
from restclient.telemetry.client import ONESClient 
```

<b> Initialize client </b>

```py
conn = ONESClient("https://10.x.x.x:443", "username", "password")

conn.connect()
```

<b>Timeseries data of Average count of In/out packets & Total count of errors & discards of Interface, for a given device.</b>

```py
query_params = {
    "fromDate": "2023-04-04 04:54:27",
    "toDate": "2023-04-04 05:54:27",
     "deviceAddress" : "10.x.x.x",
    "ifname" : "Ethernet0"
}
res = conn.get_traffic_counters(query_params)
```

<b>Timeseries data of Average count of In/out link utilization of Interface, for a given device.</b>

```py
query_params = {
    "fromDate": "2023-04-04 04:54:27",
    "toDate": "2023-04-04 05:54:27",
    "deviceAddress": "10.x.x.x",
    "ifname": "Ethernet0"
}
res = conn.get_traffic_util(query_params)
```
