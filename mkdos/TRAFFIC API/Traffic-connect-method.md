## Calling Methods For Traffic APIs

#### TRAFFIC_UTIL
``` py
print("....................TRAFFIC_UTIL....................")
query_params = {
    "fromDate" : "2023-04-04 04:54:27",
    "toDate" : "2023-04-04 05:54:27",
    "deviceAddress" : "10.4.4.55",
    "ifname" : "Ethernet0"
}
print(conn.get_traffic_util(query_params))
print("....................TRAFFIC_UTIL....................")
```
#### TRAFFIC_COUNTERS
``` py
print("....................TRAFFIC_COUNTERS....................")
query_params = {
    "fromDate" : "2023-04-04 04:54:27",
    "toDate" : "2023-04-04 05:54:27",
    "deviceAddress" : "10.4.4.55",
    "ifname" : "Ethernet0"
}
print(conn.get_traffic_counters(query_params))
print("....................TRAFFIC_COUNTERS....................")
```
