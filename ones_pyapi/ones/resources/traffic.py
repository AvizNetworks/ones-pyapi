from .base import BaseResource

class TrafficResource(BaseResource):
    BASE = "/api/traffic"

    def is_interf_pfc_enabled(self, device_address, ifname):
        filters = {
            "deviceAddress": device_address,
            "ifname": ifname
        }
        return self._get(f"{self.BASE}/is-interf-pfc-enabled", filters=filters)

    def traffic_list(self, device_address="all"):
        filters = {
            "deviceAddress": device_address
        }
        return self._get(f"{self.BASE}/trafficList", filters=filters)

    def get_interface_details(self, device_address, hostname, ipaddress, layer, time_bucket, window_size, license_):
        filters = {
            "deviceAddress": device_address,
            "hostname": hostname,
            "ipaddress": ipaddress,
            "layer": layer,
            "timeBucket": time_bucket,
            "windowSize": window_size,
            "license": license_
        }
        return self._get(f"{self.BASE}/getInterfaceDetails", filters=filters)

    def interface_details(self, from_date, to_date, window_size, device_address, active_tab, ifname):
        filters = {
            "fromDate": from_date,
            "toDate": to_date,
            "windowSize": window_size,
            "deviceAddress": device_address,
            "activeTab": active_tab,
            "ifname": ifname
        }
        return self._get(f"{self.BASE}/interfaceDetails", filters=filters)

    def traffic_mega(self, from_date, to_date, window_size, device_address, active_tab, ifname):
        filters = {
            "fromDate": from_date,
            "toDate": to_date,
            "windowSize": window_size,
            "deviceAddress": device_address,
            "activeTab": active_tab,
            "ifname": ifname
        }
        return self._get(f"{self.BASE}/trafficMega", filters=filters)

    def priority_mapping(self, device_address, ifname):
        filters = {
            "deviceAddress": device_address,
            "ifname": ifname
        }
        return self._get(f"{self.BASE}/priorityMapping", filters=filters)