from ones.client import ONESClient

client = ONESClient(
    url="https://your-instance/",
    username="your_username",
    password="your_password"
)

client.connect()

# Device Interfaces
interfaces = client.inventory.device_interfaces(device_address="xx.xx.xx.xx.xx.xx")
print("Device Interfaces:", interfaces) 

# Device Peripherals
peripherals = client.inventory.device_peripherals(device_address="xx.xx.xx.xx.xx.xx")
print("Device Peripherals:", peripherals)

# Device Info
device_info = client.inventory.device_info(device_address="xx.xx.xx.xx.xx.xx")
print("Device Info:", device_info)

# Device Firmware
firmware = client.inventory.device_firmware(device_address="xx.xx.xx.xx.xx.xx")
print("Device Firmware:", firmware)

# Link Info
link_info = client.inventory.link_info(device_address="xx.xx.xx.xx.xx.xx")
print("Link Info:", link_info)  

# minizip test
minizip = client.inventory.minizip_test()
print("Minizip Test:", minizip)

# Interface Flaps
interface_flaps = client.inventory.interface_flaps(
    start_time="2026-03-23 02:09:36",
    end_time="2026-03-24 11:09:36",
    limit=10
)
print("Interface Flaps:", interface_flaps)

# Interface Mega
interface_mega = client.inventory.interface_mega()
print("Interface Mega:", interface_mega)

# NIC Info
nic_info = client.inventory.nic_info(device_address="xx.xx.xx.xx.xx.xx")
print("NIC Info:", nic_info)        

# Device Details
device_details = client.inventory.device_details(device_address="xx.xx.xx.xx.xx.xx")
print("Device Details:", device_details)

# Inventory Details Orchestration
inv_details_orchest = client.inventory.inv_details_orchest()
print("Inventory Details Orchestration:", inv_details_orchest)


# Device YAML Files
device_yaml_files = client.inventory.device_yaml_files()
print("Device YAML Files:", device_yaml_files)  

# Mini Inventory
mini_inventory = client.inventory.mini_inventory()
print("Mini Inventory:", mini_inventory)


