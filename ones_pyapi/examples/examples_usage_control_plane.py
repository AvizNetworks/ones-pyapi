from ones.client import ONESClient

client = ONESClient(
    url="https://your-instance/",
    username="your_username",
    password="your_password"
)

client.connect()


# VLAN
vlan_info = client.control_plane.vlan()
print("VLAN Info:", vlan_info)  

# MCLAG
mclag_info = client.control_plane.mclag()
print("MCLAG Info:", mclag_info)

# LACP
lacp_info = client.control_plane.lacp()
print("LACP Info:", lacp_info)

# VRRP
vrrp_info = client.control_plane.vrrp()
print("VRRP Info:", vrrp_info)

