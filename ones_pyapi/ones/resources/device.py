from .base import BaseResource

class DeviceResource(BaseResource):
    BASE = "/api/devices"

    def get_links(self):
        return self._get(f"{self.BASE}/links")

    def get_transceiver_info(self, filters):
        return self._get(f"{self.BASE}/transceiverInfo", filters=filters)

    def get_transceiver_mega(self, from_date, to_date, window_size, device_address, active_tab, ifname):
        filters = {
            "fromDate": from_date,
            "toDate": to_date,
            "windowSize": window_size,
            "deviceAddress": device_address,
            "activeTab": active_tab,
            "ifname": ifname
        }
        return self._get(f"{self.BASE}/transceiverMega", filters=filters)

    def get_transceiver_details(self, device_address, name):
        filters = {
            "deviceAddress": device_address,
            "name": name
        }
        return self._get(f"/api/Device/transceiverDetails", filters=filters)

    def get_device_list_telemetry_version_and_fm_version(self):
        return self._get(f"/api/Device/deviceListTelemetryVersionAndFMVersion")

    def get_interfaces(self):
        return self._get(f"/api/Device/interfaces")

    def get_gpu_list(self):
        return self._get(f"/api/Device/gpulist")

    def get_docker_containers(self):
        return self._get(f"/api/Device/docker-containers")

    def get_gpu_stats(self):
        return self._get(f"/api/Device/gpu-stats")

    def get_image_management_status(self, ip_address):
        return self._get(f"/api/device/imageManagementStatus", filters={"ipAddress": ip_address})