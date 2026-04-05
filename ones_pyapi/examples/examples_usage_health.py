from ones.client import ONESClient

client = ONESClient(
    url="https://your-instance/",
    username="your_username",
    password="your_password"
)

client.connect()

# Device List
devices = client.health.device_list()
print("Devices:", devices)

# Device Info
info = client.health.device_info(
    from_date="2026-03-23 00:56:30",
    to_date="2026-03-24 09:56:30",
    window_size="1 hour",
    device_address="xx.xx.xx.xx.xx.xx"
)
print("Device Info:", info)

# Mega API
mega = client.health.mega(
    from_date="2026-03-23 12:05:44",
    to_date="2026-03-24 12:05:44",
    window_size="1 day",
    device_address="xx.xx.xx.xx.xx.xx"
)
print("Mega:", mega)

# Top CPU Consuming Services
top_services = client.health.top_cpu_consuming_services(
    device_address="xx.xx.xx.xx.xx.xx"
)

print("Top CPU Consuming Services:", top_services)

# Fabric Wise Health
fabric_health = client.health.fabric_wise_health()
print("Fabric Wise Health:", fabric_health)