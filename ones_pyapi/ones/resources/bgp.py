from .base import BaseResource

class BGPResource(BaseResource):
    BASE = "/api/bgps"

    # Handlers
    def bgp_list(self):
        return self._get(f"{self.BASE}/list")

    def neighbor_list(self, device_address, vrf):
        filters = {
            "deviceAddress": device_address,
            "vrf": vrf
        }

        return self._get(f"{self.BASE}/neighborList", filters=filters)
    
    def protocol_mega(self, from_date, to_date, window_size, device_address, vrf):
        filters = {
            "fromDate": from_date,
            "toDate": to_date,
            "windowSize": window_size,
            "deviceAddress": device_address,
            "vrf": vrf
        }

        return self._get(f"{self.BASE}/protocolMega", filters=filters)
    
    def protocol_neighbor_mega(self, from_date, to_date, window_size, device_address, vrf):
        filters = {
            "fromDate": from_date,
            "toDate": to_date,
            "windowSize": window_size,
            "deviceAddress": device_address,
            "vrf": vrf
        }

        return self._get(f"{self.BASE}/protocolNeighborMega", filters=filters)
    

    def protocols_bgp(self, ip_address):
        filters = {
            "ipAddress": ip_address
        }

        return self._get(f"{self.BASE}/Protocols/bgp", filters=filters)
    

    def vlan_mapping(self, device_address):
        filters = {
            "deviceAddress": device_address
        }

        return self._get(f"{self.BASE}/vlanMapping", filters=filters)

    def mclag_grid(self, device_address, domain_id, window_size):
        filters = {
            "deviceAddress": device_address,
            "domainId": domain_id,
            "windowSize": window_size
        }

        return self._get(f"{self.BASE}/mclag-grid", filters=filters)
    
    def lacp_grid(self, device_address, port_channel, window_size):
        filters = {
            "deviceAddress": device_address,
            "portChannel": port_channel,
            "windowSize": window_size
        }

        return self._get(f"{self.BASE}/lacp-grid", filters=filters)

    def vtep_health_grid(self, device_address, remote_vtep_ip, window_size):
        filters = {
            "deviceAddress": device_address,
            "windowSize": window_size
        }

        return self._get(f"{self.BASE}/vtep-health-grid", filters=filters)