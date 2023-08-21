## Capacity

<b> Import Client </b>

```py
from restclient.telemetry.client import ONESClient 
```

<b> Initialize client </b>

```py
conn = ONESClient("https://10.x.x.x:443", "username", "password")

conn.connect()
```

<b>Capacity based on the latest telemetry for ipv4_routes used and available. </b>

```py
query_params = {
  "ipAddress": "10.x.x.x"
}

res = conn.get_ipv4_utilization(query_params)
```

<b>Capacity based on the latest telemetry for ipv6_routes used and available. </b>

```py
query_params = {
  "ipAddress": "10.x.x.x"
}

res = conn.get_ipv6_utilization(query_params)
```

<b>Number of Total ACL capacity and it's usage in percentage</b>

```py
query_params = {
  "ipAddress": "10.x.x.x"
}

res = conn.get_acl_utilization(query_params)
```