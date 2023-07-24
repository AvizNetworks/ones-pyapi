
# Day2 operations Example

```py
from client import FMClient
import json
```

## Setting Up connection
```py
conn = FMClient(url = "http://10.x.x.x:port_number") #usually port_number will be 8787
```

## Calling methods
### Get Controller version
```py
print("Controller Version ->")
result = conn.get_controller_version()
```

### Get Intent Status
result = conn.get_intent_status()


### Get management operation status of images
payload can be single IP, or list of IPs
```py
payload = ["10.4.4.61"]

status =  conn.get_image_mgmnt_status(payload)
print(json.dumps(status, indent= 4))
```

### Reboot a device
Only single ip should be pass at a time
```py
result = conn.reboot(payload)
```

### Get controller version
```py
result = conn.controller_fm_version()
```

### ZTP enable / Image Upgrade
To Trigger the ZTP, it take one more device IPs as input
```py
payload = ["10.x.x.2", "10.x.x.3"] 
result = conn.ztp_enable(payload) # list of IPs
```

### Custom Image upgrade
To Trigger custom Image upgrade request
```py
payload_for_image_upgrade = [{"ip":"10.x.x.3","pathToImage":"http://10.x.x.x:8192/path_of_file/filename.bin"}]
result = conn.custom_image_upgrade(payload_for_image_upgrade)
```

### Get Config Difference
To get the data to show in config diff in UI
```py
payload_for_config_diff = { "ip": "10.4.4.66"}
result = conn.get_config_diff(payload_for_config_diff)
```

 ### Please Note - 
 Day1Fm and Day2FM calls are not asynchronus, we need to wait unitl the one API call completed successfully or Not.
 It is recommend to run **get_image_mgmnt_status()** after each calls, It will return values for **device_action** feild, 
 On the basis of status field, we get the status of an Image 

 - device_action = 0    **Failed**
 - device_action = 1    **Device is Free, can take any action**
 - device_action = 2    **image management operations in progress (custom/zip)**
 - device_action = 3    **reboot is in progress**

