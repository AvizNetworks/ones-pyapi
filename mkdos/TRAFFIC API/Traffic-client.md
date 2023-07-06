### get_traffic_util
``` py
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
### get_traffic_counters
``` py
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

