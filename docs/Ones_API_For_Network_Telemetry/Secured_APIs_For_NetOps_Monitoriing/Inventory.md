## Inventory

<b>Import Client </b>

```py
from restclient.telemetry.client import ONESClient 
```

<b Initialize client </b

```py
conn = ONESClient("https://10.x.x.x:443", "username", "password")

conn.connect()
```

### Device Info
<p>Get list of devices based on specific filters (SKU, Vendor, ASIC)</p>

```py
res = conn.get_hardware_info()
```

### Get Roles
<p>Count of devices in different roles i.e., Leaf/Spine/etc., </p>

```py
res = conn.get_roles()
``` 

### Switch SKUs
<p>Get a count & percentage distribution of Switch SKU's across fabric. </p>

```py
res = conn.get_switch_skus()
```

### Get ASICs
<p>Get a count & percentage distribution of Asic's across fabric. </p>

```py
res = conn.get_asics_info()
``` 


### Agent Versions
<p>Get a count & percentage distribution of ONES's agent version(Telemetry and Orchestrator) across fabric. </p>

```py
res = conn.get_agent_version()
```

### NOS Versions
<p>Get a count & percentage distribution of device's NOS versions across fabric. </p>

```py
res = conn.get_nos_version()
```

### Linux Versions
<p>Get a count & percentage distribution of device's kernel versions across fabric. </p>

```py
res = conn.get_linux_version()
```

### ONIE Versions
<p>Get a count & percentage distribution of device's ONIE's versions accross fabric. </p>

```py
res = conn.get_onie_version()
```

### Cables
<p>Get a count & percentage distribution & count of Cables used across fabric, also lists count of cables needed for unused port. </p>

```py
res = conn.get_cable_info()
``` 


### Device Peripherals
<p>Provides device's Fan and PSU hardware information. </p>

```py
query_params = {"deviceAddress": "0c:xx:xx:xx:xx:x0"}
res = conn.get_device_peripherals(query_params)
```

### Device Interfaces
<p>Provides Interface information e.g., name, alias, transcievers specific details, etc. of a device </p>

```py
payload = {
  "filter": {
    "deviceAddress": "0c:xx:xx:xx:xx:x0"
  }
}
res = conn.get_device_interfaces(payload)
```








