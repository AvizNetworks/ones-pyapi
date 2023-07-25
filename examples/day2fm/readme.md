
# Day2 Operations example

This illustration demonstrates various day 2 operations such as backup&restore, compare config, image upgrade, reboot a device etc.
## Importing ONES Fabric Manager Agent

```py
from client import FMClient
import json
```

## Setting Up connection
```py
conn = FMClient(url = "http://10.x.x.x:<port_number>") #usually <port_number> will be 8787
```

### Backup on Config
```py
payload = [{"ip":"10.x.x.1","label":"test_backup"}]
result = conn.backup_on_config(payload)
```

### Get all backups
```py
payload = ["10.x.x.12","10.x.x.11"]
result = conn.backups(payload)
```

### Restore Config
```py
payload = [
    {"ip":"10.x.x.12","timestamp":"USERINPUT"},
    {"ip":"10.x.x.11","timestamp":"USERINPUT"}
]
result = conn.restore_config(payload)
```

### Custom Image upgrade
To Trigger custom Image upgrade request
```py
payload_for_image_upgrade = [{"ip":"10.x.x.3","pathToImage":"http://10.x.x.x:8192/path_of_file/filename.bin"}]
result = conn.custom_image_upgrade(payload_for_image_upgrade)
```


### ZTP enable / Image Upgrade
To Trigger the ZTP, it take one more device IPs as input
```py
payload = ["10.x.x.2", "10.x.x.3"] 
result = conn.ztp_enable(payload) # list of IPs
```


### Get Config Difference
To get the data to show in config diff in UI
```py
payload_for_config_diff = { "ip": "109.x.x.x6"}
result = conn.get_config_diff(payload_for_config_diff)
```

### Get Controller version
```py
print("Controller Version ->")
result = conn.get_controller_version()
```

### Get management operation status of images
payload can be single IP, or list of IPs
```py
payload = ["10.x.x.x1"]

status =  conn.get_image_mgmnt_status(payload)
print(json.dumps(status, indent= 4))
```


### Reboot a device
Only single ip should be pass at a time
```py
payload = ["10.x.x.x1"]
result = conn.reboot(payload)
```

### Get controller / Fabric Manager version
```py
result = conn.controller_fm_version()
```

 ### Note - 
 The API calls  Day2FM are synchronous, meaning we have to wait for one API call to complete successfully or fail before proceeding. To ensure proper synchronization, it is advisable to call the **function get_image_mgmnt_status()** after each API call. This function will provide the values for the **device_action** field, which, in turn, will allow us to determine the status of an image based on the status field.

 - device_action = 0    **Failed**
 - device_action = 1    **Device is Free, can take any action**
 - device_action = 2    **image management operations in progress (custom/zip)**
 - device_action = 3    **reboot is in progress**

