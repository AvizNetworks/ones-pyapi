# Telemetry API documentation

## ONES Client

[See in github](https://github.com/AvizNetworks/ones-pyapi/blob/master/restclient/telemetry/client.py)

```python
class ONESClient(object):
    def __init__(self, username=None, password=None, url=None):
        self.username = username
        self.password = password
        self.url = url
        self.access_token = None
```

### connect()
```py
def connect(self):
        """
            This method will use to make connection
            with Ones API,
            It will use user, url,password, and  Authentication API
        """
        try:
            url = self.url + connect

            payload = {"username": self.username, "password": self.password}

            payload = json.dumps(payload)
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                url, data=payload, headers=headers, verify=False
            )
            if response.status_code == 200:
                temp = response.json()
                access_token = temp["data"]["token"]
                logging.debug(access_token)
                self.access_token = access_token

            else:
                logging.error("Something went wrong")

        except Exception as err:
            logging.error(f"Error -> ${err}")
            raise OnesClientExpection()
```

### get_hardware_info()
```py
 def get_hardware_info(self):
        """
            This function will return all Hardware Info
            Includes the following Details
            Devices, Regions, SwitchSKUs, Role and ASICs
        """
        try:
            url = self.url + hardware_info
            headers = {
                "Authorization": self.access_token,
                "Content-Type": "application/json",
            }
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                res = response.json()
                print(json.dumps(res, indent=4))
                return True
            else:
                raise OnesClientExpection(HARDWARE_INFO_ERROR)

        except Exception as err:
            logging.error(f"Error -> ${err}")
            raise OnesClientExpection(HARDWARE_INFO_ERROR)
```

### get_roles()
```py
def get_roles(self):
        """
        This function will return all existings roles
                Spine
                SuperSpine
                Tor
                Leaf
        """
        try:
            url = self.url + roles
            headers = {
                "Authorization": self.access_token,
                "Content-Type": "application/json",
            }
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                res = response.json()
                print(json.dumps(res, indent=4))
                return True
        except Exception as err:
            logging.error(err)
            raise OnesClientExpection(ROLES_ERROR)
```


### get_switch_skus()
```py
def get_switch_skus(self):
        """
        Return all switch SKUs
        """
        request_handler(self.url, switch_skus, self.access_token, None)
```
.. note::
    [request_handlers]("Ones_API_For_Network_Telemetry/Secured_APIs_For_NetOps_Monitoriing/API_Documentation/request_handlers.md")


### get_asics_info()
```py
 def get_asics_info(self):
    """
    Return all ASICs info
    """
    request_handler(self.url, asics, self.access_token, None)
```


### get_agent_version()
```py
def get_agent_version(self):
    """
    Return Agent version
    """
    request_handler(self.url, agent_version, self.access_token, None)
```

### get_nos_version()
```py
def get_nos_version(self):
    """
    Return NOS version
    """
    request_handler(self.url, nos_version, self.access_token, None)
```

### get_linux_version()
```py
def get_linux_version(self):
    """
    Return linux version
    """
    request_handler(self.url, linux_version, self.access_token, None)
```

### get_onie_version()
```py
def get_onie_version(self):
    """
    Return ONIE version
    """
    request_handler(self.url, onie_version, self.access_token, None)
```

### get_cabling_info()
```py
def get_cabling_info(self):
    """
    Return cabling INFO
    """
    request_handler(self.url, cabling, self.access_token, None)
```

### get_device_interfaces()
```py
def get_device_interfaces(self, arg1):
    """
    Payload -> "filter": {
                "deviceAddress": "0c:29:ef:ce:92:20"
            }
    Output -> List of interfaces of a device
    """
    request_handler_with_payload(self.url, device_interfaces, self.access_token, None, arg1)
```


### get_device_peripherals()
```py
def get_device_peripherals(self, arg1):
    """
    query_params -> "filter": {
                {
                "deviceAddress" : "0c:29:ef:ce:92:20"
                }
        }
    Output -> List of peripherals
    """
    request_handler_with_query_params(self.url, device_peripherals, self.access_token, None, arg1)
```

### get_device_info()
```py
def get_device_info(self,arg1):
    """
    query_params -> {"ipAddress": "10.4.4.61"}
    Output -> List of device info
    """
    request_handler_with_query_params(self.url, device_info_endpoint, self.access_token,None, arg1)
```


### get_network_topology()
```py    
def get_network_topology(self):
    """
    Output -> List of device info
    """
    request_handler(self.url, network_topology, self.access_token,None)
```

### get_faulty_psus()
```py
def get_faulty_psus(self):
    """
    output -> list of devices and connections
    """
    request_handler(self.url, faulty_psus,self.access_token, None)
```

###  get_faulty_fans()
```py
def get_faulty_fans(self):
    """
    Return Fan List
    """
    request_handler(self.url, faulty_fans, self.access_token, None)
```
    
###  get_link_flaps()
```py
def get_link_flaps(self, arg1):
    """
    Return interface status
    """
    request_handler_with_query_params(self.url, link_flaps, self.access_token, None, arg1)
```

### get_cpu_utilization
```py
def get_cpu_utilization(self, arg1):
    """
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, cpu_utilization, self.access_token, None, arg1)
```
    
### get_memory_utilization(query_params)

```py
def get_memory_utilization(self, arg1):
    """
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, memory_utilization, self.access_token, None, arg1)
```

### get_cpu_core_temperaure(query_params)
```py
def get_cpu_core_temperaure(self, arg1):
    """
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, cpu_core_temperaure, self.access_token, None, arg1)
```

### get_psu_temperature(query_params)
```py
def get_psu_temperature(self, arg1):
    """ 
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, psu_temperature, self.access_token, None, arg1)
```
    
### get_psu_voltage(query_params)
```py
def get_psu_voltage(self, arg1):
    """ 
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params ( self.url, psu_voltage, self.access_token, None, arg1)
```

###  get_psu_current(query_params)
```py
def get_psu_current(self, arg1):
    """ 
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, psu_current, self.access_token, None, arg1)
```


### get_fan_speed(query_params)
```py
def get_fan_speed(self, arg1):
    """ 
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, fan_speed, self.access_token, None, arg1)
```
    
### get_psu_power(query_params)
```py
def get_psu_power(self, arg1):
    """ 
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        " deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, psu_power, self.access_token, None, arg1)
```
    
### get_health_services_cpu(query_params)
```py
def get_health_services_cpu(self, arg1):
    """ 
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, health_services_cpu, self.access_token, None, arg1)
```


###  get_health_services_memory(query_params) 
```py
def get_health_services_memory(self, arg1):
    """ 
    query_params -> {
        "fromDate" : "2023-05-12 11:55:24",
        "toDate" : "2023-05-12 12:55:24",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, health_services_memory, self.access_token, None, arg1)
```
    

### get_health_bgp_neighbors(query_params)
```py
def get_health_bgp_neighbors(self, arg1):
    """ 
    query_params -> {
        "fromDate" : "2023-04-04 04:54:27",
        "toDate" : "2023-04-04 05:54:27",
        "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, health_bgp_neighbors, self.access_token, None, arg1)
```


###  get_health_trancievers(query_params)
```py
def get_health_trancievers(self, arg1):
    """ 
    query_params -> {
        "ipAddress" : "10.4.4.55",
        "ifName" : "Ethernet0",
        "fromDate" : "2023-06-26 10:48:55",
        "toDate" : "2023-06-26 11:48:55"
    }
    """    
    request_handler_with_query_params(self.url, health_transcievers, self.access_token, None, arg1)
```
    

###  get_health_running_services(query_params)
```py
def get_health_running_services(self, arg1):
    """ 
    query_params -> {
                "fromDate" : "2023-05-12 11:55:24",
                "toDate" : "2023-05-12 12:55:24",
                "deviceAddress" : "10.4.4.55"
    }
    """
    request_handler_with_query_params(self.url, health_running_services, self.access_token, None, arg1)
```


### get_traffic_util(query_params)
```py
def get_traffic_util(self, arg1):
    """ 
    query_params -> "filter" : {
        {
            "fromDate" : "2023-04-04 04:54:27",
            "toDate" : "2023-04-04 05:54:27",
            "deviceAddress" : "10.4.4.55",
            "ifname" : "Ethernet0"
        }
    }
    """
    request_handler_with_query_params(self.url, traffic_util, self.access_token, None, arg1)
```


### get_traffic_counters(query_params)
```py
def get_traffic_counters(self, arg1):
    """ 
    query_params -> "filter" : {
        {
            "fromDate" : "2023-04-04 04:54:27",
            "toDate" : "2023-04-04 05:54:27",
            "deviceAddress" : "10.4.4.55",
            "ifname" : "Ethernet0"
        }
    }
    """
    request_handler_with_query_params(self.url, traffic_counters, self.access_token, None, arg1)
```
    
.. note::
    [request_handlers]("Ones_API_For_Network_Telemetry/Secured_APIs_For_NetOps_Monitoriing/API_Documentation/request_handlers.md")
        
