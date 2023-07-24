# Day1 operations Example

```py
from client import FMClient
```

## Setting Up connection
```py
conn = FMClient(url = "http://10.x.x.x:port_number") 
#usually port_number will be 8787
```


# BGP operation
```py
file = "path of YAML file"
flag = True 
result = conn.bgp_operation(config_file_path=file, diff_flag=flag)
```

# Image Upload 
This API will take a YAML template as input to automatically generate the network configuration for the following deployments, validate the same and apply to make the data center fabric Operational with single click.
- BGP IP CLOS
- BGP IP CLOS with MC LAG 
- Layer 2 VXLAN with MCLAG
- Layer 2 VXLAN with BGP-EVPN
- VXLAN + EVPN Symmetric IRB
- VXLAN + EVPN Asymmetric IRB


```py
# UPLOAD 
file = "path of YAML file"
result = conn.upload_image(file)
```

 ### Please Note - 
 Day1Fm and Day2FM calls are not asynchronus, we need to wait unitl the one API call completed successfully or Not.
 It is recommend to run **get_image_mgmnt_status()** after each calls, It will return values for **device_action** feild, 
 On the basis of status field, we get the status of an Image 

 - device_action = 0    **Failed**
 - device_action = 1    **Device is Free, can take any action**
 - device_action = 2    **image management operations in progress (custom/zip)**
 - device_action = 3    **reboot is in progress**
