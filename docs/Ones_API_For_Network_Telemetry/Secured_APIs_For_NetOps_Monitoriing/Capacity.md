## Capacity

### Import Client 

```py
from restclient.telemetry.client import ONESClient 
```

### Initialize client 

```py
conn = ONESClient("https://10.x.x.x:443", "username", "password")

conn.connect()
```

### IPV4 Utilization
<p>Capacity based on the latest telemetry for ipv4_routes used and available. </p>

```py
query_params = {
  "ipAddress": "10.x.x.x"
}

res = conn.get_ipv4_utilization(query_params)
```

### IPV6 Utilization
<p>Capacity based on the latest telemetry for ipv6_routes used and available. </p>

```py
query_params = {
  "ipAddress": "10.x.x.x"
}

res = conn.get_ipv6_utilization(query_params)
```

### ACL Utilization
<p>Number of Total ACL capacity and it's usage in percentage</p>

```py
query_params = {
  "ipAddress": "10.x.x.x"
}

res = conn.get_acl_utilization(query_params)
```