from ones.client import ONESClient
client = ONESClient(
    url="https://your-instance/",
    username="your_username",
    password="your_password"
)

client.connect()


# Example usage of DeviceResource methods
links = client.device.get_links()
print("Links:", links)


transceiver_mega = client.device.get_transceiver_mega(
    from_date="2024-06-01T00:00:00Z",
    to_date="2024-06-02T00:00:00Z",
    window_size=10,
    device_address="example_device_address",
    active_tab="example_active_tab",
    ifname="example_ifname"
)

print("Transceiver Mega:", transceiver_mega)

transceiver_details = client.device.get_transceiver_details(
    device_address="example_device_address",
    name="example_name"
)
print("Transceiver Details:", transceiver_details)      

device_list_telemetry_version_and_fm_version = client.device.get_device_list_telemetry_version_and_fm_version()
print("Device List Telemetry Version and FM Version:", device_list_telemetry_version_and_fm_version)

interfaces = client.device.get_interfaces()
print("Interfaces:", interfaces)

gpu_list = client.device.get_gpu_list()
print("GPU List:", gpu_list)

docker_containers = client.device.get_docker_containers()
print("Docker Containers:", docker_containers)
gpu_stats = client.device.get_gpu_stats()
print("GPU Stats:", gpu_stats)
image_management_status = client.device.get_image_management_status(ip_address="example_ip_address")
print("Image Management Status:", image_management_status)
