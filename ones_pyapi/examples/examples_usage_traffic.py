
from ones.client import ONESClient

client = ONESClient(
    url="https://your-instance/",
    username="your_username",
    password="your_password"
)

client.connect()



# 1. is_interf_pfc_enabled
resp1 = client.traffic.is_interf_pfc_enabled(device_address="xx.xx.xx.xx.xx.xx", ifname="Ethernet1")
print("is_interf_pfc_enabled:", resp1)

# 2. traffic_list
resp2 = client.traffic.traffic_list(device_address="xx.xx.xx.xx.xx.xx")
print("traffic_list:", resp2)

# 3. get_interface_details
resp3 = client.traffic.get_interface_details(
    device_address="xx.xx.xx.xx.xx.xx",
    hostname="switch1",
    ipaddress="192.168.1.1",
    layer="L2",
    time_bucket="5m",
    window_size=10,
    license_="standard"
)
print("get_interface_details:", resp3)

# 4. interface_details
resp4 = client.traffic.interface_details(
    from_date="2024-06-01T00:00:00Z",
    to_date="2024-06-02T00:00:00Z",
    window_size=10,
    device_address="xx.xx.xx.xx.xx.xx",
    active_tab="tab1",
    ifname="Ethernet1"
)
print("interface_details:", resp4)

# 5. traffic_mega
resp5 = client.traffic.traffic_mega(
    from_date="2024-06-01T00:00:00Z",
    to_date="2024-06-02T00:00:00Z",
    window_size=10,
    device_address="xx.xx.xx.xx.xx.xx",
    active_tab="tab1",
    ifname="Ethernet1"
)
print("traffic_mega:", resp5)

# 6. priority_mapping
resp6 = client.traffic.priority_mapping(device_address="xx.xx.xx.xx.xx.xx", ifname="Ethernet1")
print("priority_mapping:", resp6)

