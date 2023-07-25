# Day 1 Orchestration Example

```py
from client import FMClient
```

## Setting Up connection
```py
conn = FMClient(url = "http://10.x.x.x:port_number") 
#usually port_number will be 8787
```

# Deploy Config 
This API will take a YAML template as input to automatically generate the network configuration for the following deployments, validate the same and apply to make the data center fabric Operational with single click.
- BGP IP CLOS
- BGP IP CLOS with MC LAG 
- Layer 2 VXLAN with MCLAG
- Layer 2 VXLAN with BGP-EVPN
- VXLAN + EVPN Symmetric IRB
- VXLAN + EVPN Asymmetric IRB


```py
# Deploy Config
file = "path of YAML file"
result = conn.day1_intent_ovd_template(file)
```

# Intent Status
```py
result = conn.get_intent_status()
```

 ### Please Note - 
 Day1 orchestration calls are not asynchronus, we need to wait unitl the one API call completed successfully or Not.
 Use **get_intent_status()** status and perform further operations (Day 2 Operations) accordingly.
