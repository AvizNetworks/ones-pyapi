from ones.client import ONESClient

client = ONESClient(
    url="https://your-instance/",
    username="your_username",
    password="your_password"
)

client.connect()

# 1. BGP List
bgp_list = client.bgp.bgp_list()
print("BGP List:", bgp_list)

# 2. Neighbor List
neighbors = client.bgp.neighbor_list(device_address="xx.xx.xx.xx.xx.xx", vrf="default")
print("Neighbor List:", neighbors)

# 3. Protocol Mega
protocol_mega = client.bgp.protocol_mega(
    from_date="2026-03-23 10:09:36",
    to_date="2026-03-23 11:09:36",
    window_size="1 hour",
    device_address="xx.xx.xx.xx.xx.xx",
    vrf="default"
)
print("Protocol Mega:", protocol_mega)      

# 4. Protocol Neighbor Mega
protocol_neighbor_mega = client.bgp.protocol_neighbor_mega(
    from_date="2026-03-23 10:09:36",
    to_date="2026-03-23 11:09:36",  
    window_size="1 hour",
    device_address="xx.xx.xx.xx.xx.xx",
    vrf="default"
)
print("Protocol Neighbor Mega:", protocol_neighbor_mega)

protocol_bgps = client.bgp.protocols_bgp(ip_address="x.x.x.x")
print("Protocol Map:", protocol_bgps)

vlan_mapping = client.bgp.vlan_mapping(device_address="xx.xx.xx.xx.xx.xx")
print("VLAN Mapping:", vlan_mapping)






