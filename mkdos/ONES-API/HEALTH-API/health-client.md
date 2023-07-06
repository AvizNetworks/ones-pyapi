### get_faulty_psus
``` py
def get_faulty_psus(self):
        """
        output -> list of devices and connections
        """
        request_handler(self.url, faulty_psus,self.access_token, None)
```
### get_faulty_fans
``` py
def get_faulty_fans(self):
        """
        Return Fan List
        """
        request_handler(self.url, faulty_fans, self.access_token, None)
```
### get_link_flaps
``` py
def get_link_flaps(self, arg1):
        """
        Return interface status
        """
        request_handler_with_query_params(self.url, link_flaps, self.access_token, None, arg1)
```
### get_cpu_utilization
``` py
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
### get_memory_utilization
``` py
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
### get_cpu_core_temperature
``` py
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
### get_psu_temperature
``` py
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
### get_psu_voltage
``` py
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
### get_psu_current
``` py
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
### get_fan_speed
``` py
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
### get_psu_power
``` py
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
### get_health_services_cpu
``` py
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
### get_health_services_memory
``` py
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
### get_bgp_neighbors
``` py
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
### get_health_transcievers
``` py
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
### get_health_running_services
``` py
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
