## Inventory

<b> Import Client </b>

```py
from restclient.telemetry.client import ONESClient 
```

<b> Initialize client </b>

```py
conn = ONESClient("https://10.x.x.x:443", "username", "password")

conn.connect()
```

<b>Get list of devices based on specific filters (SKU, Vendor, ASIC)</b>

```py
res = conn.get_hardware_info()
```

<b>Count of devices in different roles i.e., Leaf/Spine/etc., </b>

```py
res = conn.get_roles()
``` 

<b>Get a count & percentage distribution of Switch SKU's across fabric. </b>

```py
res = conn.get_switch_skus()
```

<b>Get a count & percentage distribution of Asic's across fabric. </b>

```py
res = conn.get_asics_info()
``` 

<b>Get a count & percentage distribution of ONES's agent version(Telemetry and Orchestrator) across fabric. </b>

```py
res = conn.get_agent_version()
```

<b>Get a count & percentage distribution of device's NOS versions across fabric. </b>

```py
res = conn.get_nos_version()
```

<b>Get a count & percentage distribution of device's kernel versions across fabric. </b>

```py
res = conn.get_linux_version()
```

<b>Get a count & percentage distribution of device's ONIE's versions accross fabric. </b>

```py
res = conn.get_onie_version()
```
<b>Get a count & percentage distribution & count of Cables used across fabric, also lists count of cables needed for unused port. </b>

```py
res = conn.get_cable_info()
``` 

<b>Provides device's Fan and PSU hardware information. </b>

```py
query_params = {"deviceAddress": "0c:xx:xx:xx:xx:x0"}
res = conn.get_device_peripherals(query_params)
```
<b>Provides Interface information e.g., name, alias, transcievers specific details, etc. of a device </b>

```py
payload = {
  "filter": {
    "deviceAddress": "0c:xx:xx:xx:xx:x0"
  }
}
res = conn.get_device_interfaces(payload)
```








