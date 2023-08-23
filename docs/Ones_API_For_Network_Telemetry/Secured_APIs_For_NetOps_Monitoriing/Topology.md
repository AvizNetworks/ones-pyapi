## Topology

Provides entire topology (device, link & layer Information) dump. 

### NETWORK_TOPOLOGY_INFO

<b> Import Client </b>

```py
from restclient.telemetry.client import ONESClient 
```

<b> Initialize client </b>

```py
conn = ONESClient("https://10.x.x.x:443", "username", "password")

conn.connect()
```

### Topology
<p> Calling Method for getting topology dumop </p>

```py   
topology_details = conn.get_network_topology()
print(topology_details)
```
