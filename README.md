# ONES PyAPI

Aviz ONES is the industry's first multi-vendor platform which provides seamless network orchestration and monitoring capabilities. From storing the physical topology, device health, utilization and network events, it also provides network orchestration/automation for the data center fabric deployments. All this fleet-wide data is provided to the network administrators using standardized ONES APIs. ONES Provides a smooth transition for Network Admin for SONiC transition depending on the consumption model.

ONES APIs supports following interfaces
- gNMI (Secured using certificates)
- REST API (Secured using user tokens)



## Features
> Can connect with python environment and make ONES APIs operation seamlessly.
> For Developers and Network Engineers
> Supported version -> Python 3.7 and above 


## Installation
> **Download link** - https://github.com/AvizNetworks/ones-pyapi/blob/master/versions/ones-pyapi-1.0.0.tar.gz
```sh
pip install onse-pyapi-1.0.0.tar.gz
```

It has two clients.
1. Day1 and Day2 Operations (FM APIs)  - FMClient
2. APIs for NetOps Monitoring - ONESClient

### Importing client (NetOps)

```py
from restclient.telemetry.client import ONESClient 
```

### Initialize client 

```py
conn = ONESClient("https://10.x.x.x:443", "username", "password")

conn.connect()
```

Examples -
1. NetOps Monitoring API call - (link)[https://github.com/AvizNetworks/ones-pyapi/tree/master/examples/telemetry]
2. Day1 Operations - (link)[https://github.com/AvizNetworks/ones-pyapi/tree/master/examples/day1fm]
3. Day2 Operations - (link)[https://github.com/AvizNetworks/ones-pyapi/tree/master/examples/day2fm]

