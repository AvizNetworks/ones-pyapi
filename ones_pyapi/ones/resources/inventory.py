from .base import BaseResource

class InventoryResource(BaseResource):
    BASE = "/api/inventory"

    def fm_agent_version_list(self):
        return self._get(f"{self.BASE}/FMAgentVersionList")
    
    def get_inventory_roles(self):
        return self._get(f"{self.BASE}/Roles")
    
    def get_switch_skus(self):
        return self._get(f"{self.BASE}/SwitchSKUs")
    
    def get_devices(self):
        return self._get(f"{self.BASE}/Devices")
    
    def get_action_btn(self):
        return self._get(f"{self.BASE}/ActionBtn")
    
    def get_device_ip_trans(self):
        return self._get(f"{self.BASE}/DeviceIpTrans")
    
    # GET	/inventory/Devices/streaming-status-history	{  "deviceAddress" : "68:21:5F:A6:61:72",  "windowSize" : "4 hour" }
    def streaming_status_history(self, device_address, window_size):
        filters = {
            "deviceAddress": device_address,
            "windowSize": window_size
        }

        return self._get(f"{self.BASE}/Devices/streaming-status-history", filters=filters)
    

# GET	/inventory/Devices/streaming-status	{  "deviceAddress" : "68:21:5F:A6:61:72",  "windowSize" : "4 hour" }
    def streaming_status(self, device_address, window_size):
        filters = {
            "deviceAddress": device_address,
            "windowSize": window_size
        }

        return self._get(f"{self.BASE}/Devices/streaming-status", filters=filters)  
    

# GET	/inventory/Devices/qosOnly	NULL
    def qos_only(self):
        return self._get(f"{self.BASE}/Devices/qosOnly")



# GET	/inventory/Devices/count	NULL
    def device_count(self):
        return self._get(f"{self.BASE}/Devices/count")
    

# GET	/inventory/Devices/interfaces	{  "deviceAddress" : "68:21:5F:A6:4A:72" }
    def device_interfaces(self, device_address):
        filters = {
            "deviceAddress": device_address
        }

        return self._get(f"{self.BASE}/Devices/interfaces", filters=filters)
    

# GET	/inventory/Devices/peripherals	{  "deviceAddress" : "68:21:5F:A6:4A:72" }
    def device_peripherals(self, device_address):
        filters = {
            "deviceAddress": device_address
        }

        return self._get(f"{self.BASE}/Devices/peripherals", filters=filters)
    

# GET	/inventory/deviceInfo	{  "deviceAddress" : "68:21:5F:A6:4A:72" }
    def device_info(self, device_address):
        filters = {
            "deviceAddress": device_address
        }

        return self._get(f"{self.BASE}/deviceInfo", filters=filters)
    

# GET	/inventory/Devices/firmware	{  "deviceAddress" : "68:21:5F:A6:4A:72" }
    def device_firmware(self, device_address):
        filters = {
            "deviceAddress": device_address
        }

        return self._get(f"{self.BASE}/Devices/firmware", filters=filters)
    

# GET	/inventory/linkInfo	{  "deviceAddress" : "68:21:5F:A6:4A:72" }
    def link_info(self, device_address):
        filters = {
            "deviceAddress": device_address
        }

        return self._get(f"{self.BASE}/linkInfo", filters=filters)
    

# GET	/inventory/minizip-test	NULL
    def minizip_test(self):
        return self._get(f"{self.BASE}/minizip-test")
    

# GET	/inventory/interfaceFlaps	{  "startTime" : "2026-03-23 02:09:36",  "endTime" : "2026-03-24 11:09:36",  "limit" : 10 }
    def interface_flaps(self, start_time, end_time, limit):
        filters = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit
        }

        return self._get(f"{self.BASE}/interfaceFlaps", filters=filters)
    
# GET	/inventory/interfaceMega	NULL
    def interface_mega(self):
        return self._get(f"{self.BASE}/interfaceMega")
    
# GET	/inventory/nic-info	{  "deviceAddress" : "68:21:5F:A6:61:72" }
    def nic_info(self, device_address):
        filters = {
            "deviceAddress": device_address
        }

        return self._get(f"{self.BASE}/nic-info", filters=filters)
    
# GET	/inventory/device-details	{  "deviceAddress" : "68:21:5F:A6:61:72" }
    def device_details(self, device_address):
        filters = {
            "deviceAddress": device_address
        }

        return self._get(f"{self.BASE}/device-details", filters=filters)
    
# GET	/inventory/inv-details-orchest	NULL
    def inv_details_orchest(self):
        return self._get(f"{self.BASE}/inv-details-orchest")
    
# GET	/inventory/device-yaml-files	NULL
    def device_yaml_files(self):
        return self._get(f"{self.BASE}/device-yaml-files")
    
# GET	/inventory/mini-inventory	NULL
    def mini_inventory(self):
        return self._get(f"{self.BASE}/mini-inventory")