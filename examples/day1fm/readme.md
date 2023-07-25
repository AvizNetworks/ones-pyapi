# Day 1 Orchestration Example

This illustration demonstrates the deployment of the configuration using an intent-based YAML template, while also offering a practical instance of checking the status of the intent operation.

## Importing ONES Fabric Manager Agent

```py
from client import FMClient
```

## Setting Up connection
```py
conn = FMClient(url = "http://10.x.x.x:<port_number>") 
#usually <port_number> will be 8787
```

## Deploy Config 
This method takes Yaml file as input, and shall be used by the fabric manager to orchestrate the network. There are pre-validated templates for various data center fabric deployments using SONiC. Yaml templates can be found [here](https://github.com/AvizNetworks/ones-pyapi/tree/master/examples/day1fm/yaml-templates)

- BGP IP CLOS
- BGP IP CLOS with MC LAG 
- Layer 2 VXLAN with MCLAG
- Layer 2 VXLAN with BGP-EVPN
- VXLAN + EVPN Symmetric IRB
- VXLAN + EVPN Asymmetric IRB


```py
# Deploy Config
file = "<Path of Yaml file>"
result = conn.day1_intent_ovd_template(file)
```
[Yaml Templates](https://github.com/AvizNetworks/ones-pyapi/tree/master/examples/day1fm/yaml-templates)

## Intent Status
Show Generic Status - Retrieve Generic Intent Status for provisioning on sonic enabled fabric switches . This restful API allows network  operators  to  get the status of orchestration progress on a specific switch in sonic fabric  enrolled with ONES application.
```py
result = conn.get_intent_status()
```

 ### Note - 
 Day 1 orchestration calls are synchronous. We need to await the command's completion status, determined using **get_intent_status()**, before proceeding with any subsequent commands.
