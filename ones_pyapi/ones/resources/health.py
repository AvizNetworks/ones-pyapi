# ones/resources/health.py

from .base import BaseResource


class HealthResource(BaseResource):
    BASE = "/api/health"

    def device_list(self):
        return self._get(f"{self.BASE}/DeviceList")

    def device_info(
        self,
        from_date,
        to_date,
        window_size,
        device_address,
        fan=None,
        psu=None,
        active_tab="system",
    ):
        filters = {
            "fromDate": from_date,
            "toDate": to_date,
            "windowSize": window_size,
            "deviceAddress": device_address,
            "fan": fan,
            "psu": psu,
            "activeTab": active_tab,
        }

        return self._get(f"{self.BASE}/deviceInfo", filters=filters)
    
    def mega(
        self,
        from_date,
        to_date,
        window_size,
        device_address,
    ):
        filters = {
            "fromDate": from_date,
            "toDate": to_date,
            "windowSize": window_size,
            "deviceAddress": device_address,
        }

        return self._get(f"{self.BASE}/mega", filters=filters)
    
    # GET	/health/topCpuConsumingServices	"68:21:5F:A6:61:72"

    def top_cpu_consuming_services(self, device_address):
        filters = {
            "deviceAddress": device_address
        }

        return self._get(f"{self.BASE}/topCpuConsumingServices", filters=filters)   
    
    # GET	/health/fabricWiseHealth	NULL

    def fabric_wise_health(self):
        return self._get(f"{self.BASE}/fabricWiseHealth")
    