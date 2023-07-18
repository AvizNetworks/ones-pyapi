## get_network_topology

``` py
def get_network_topology(self):
        """
        Output -> List of devices and connections
        """
        request_handler(self.url,network_topology, self.access_token, None )
```