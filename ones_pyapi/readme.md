# ones_pyapi

[![PyPI version](https://badge.fury.io/py/ones_pyapi.svg)](https://badge.fury.io/py/ones_pyapi)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Client Initialization](#client-initialization)
- [API Reference](#api-reference)
    - [User API](#user-api)
    - [BGP API](#bgp-api)
    - [Control Plane API](#control-plane-api)
    - [Fabric Manager API](#fabric-manager-fm-api)
    - [Health API](#health-api)
    - [Inventory API](#inventory-api)
    - [Misc API](#misc-api)
    - [Traffic API](#traffic-api)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Simple and intuitive API client for Datacenter NetOps
- Supports **Day 1** (provisioning) and **Day 2** (lifecycle) operations for SONiC-based switches
- Organized resources for users, health, inventory, BGP, control plane, and more
- Custom exception handling for robust error management
- Comprehensive test suite and example usage scripts
- Designed for extensibility and clarity in modern Python projects

---

## Installation

```bash
pip install ones_pyapi
```

---

## Quick Start

```python
from ones.client import ONESClient

client = ONESClient(
        url="https://your-instance/",
        username="your_username",
        password="your_password"
)

client.connect()

# List all users
print(client.user.list())

# Check fabric-wide health
print(client.health.fabric_wise_health())

# List inventory items
print(client.inventory.mini_inventory())
```

---

## Project Structure

```
ones_sdk/
│
├── ones/                     # Main package
│   ├── client.py             # Main entry point
│   ├── transport.py          # HTTP layer
│   ├── exceptions.py         # Custom errors
│   ├── constants.py          # Endpoints and paths
│   ├── resources/            # API resource groups
│   │   ├── user.py
│   │   ├── health.py
│   │   ├── inventory.py
│   │   ├── bgp.py
│   │   ├── control_plane.py
│   │   ├── fm.py
│   │   ├── misc.py
│   │   └── traffic.py
│   ├── utils/                # Helper utilities
│   │   └── parser.py
│   └── models/               # Data models (optional)
│       └── user.py
│
├── tests/                    # Test suite
├── examples/                 # Usage examples
├── requirements.txt
├── setup.py / pyproject.toml
└── README.md
```

---

## Client Initialization

All examples in this document use the following client setup:

```python
from ones.client import ONESClient

client = ONESClient(
        url="https://your-instance/",
        username="your_username",
        password="your_password"
)

client.connect()
```

---

## API Reference

### User API

```python
# List all users
print(client.user.list())
```

---

### BGP API

> **BGP (Border Gateway Protocol)** is the routing protocol used to exchange routing information between network devices (e.g., SONiC switches). These APIs provide visibility into BGP sessions, neighbors, and telemetry data.

```python
# List all BGP entries
bgp_list = client.bgp.bgp_list()
print("BGP List:", bgp_list)

# List BGP neighbors for a device
neighbors = client.bgp.neighbor_list(
        device_address="xx:xx:xx:xx:xx:xx",
        vrf="default"
)
print("Neighbor List:", neighbors)

# Aggregated BGP protocol telemetry over a time window
protocol_mega = client.bgp.protocol_mega(
        from_date="2026-03-23 10:09:36",
        to_date="2026-03-23 11:09:36",
        window_size="1 hour",
        device_address="xx:xx:xx:xx:xx:xx",
        vrf="default"
)
print("Protocol Mega:", protocol_mega)

# Aggregated BGP neighbor telemetry over a time window
protocol_neighbor_mega = client.bgp.protocol_neighbor_mega(
        from_date="2026-03-23 10:09:36",
        to_date="2026-03-23 11:09:36",
        window_size="1 hour",
        device_address="xx:xx:xx:xx:xx:xx",
        vrf="default"
)
print("Protocol Neighbor Mega:", protocol_neighbor_mega)

# BGP protocols for a specific IP
protocol_bgps = client.bgp.protocols_bgp(ip_address="x.x.x.x")
print("Protocol BGPs:", protocol_bgps)

# VLAN to BGP mapping
vlan_mapping = client.bgp.vlan_mapping(device_address="xx:xx:xx:xx:xx:xx")
print("VLAN Mapping:", vlan_mapping)
```

---

### Control Plane API

> **Control Plane** refers to the part of a network switch responsible for signaling, routing decisions, and protocol management. These APIs expose the following features:
>
> | Feature | Description |
> |---------|-------------|
> | **VLAN** | Virtual LAN segmentation |
> | **MCLAG** | Multi-Chassis Link Aggregation Group for redundancy |
> | **LACP** | Link Aggregation Control Protocol for bonding ports |
> | **VRRP** | Virtual Router Redundancy Protocol for gateway failover |

```python
# VLAN info
vlan_info = client.control_plane.vlan()
print("VLAN Info:", vlan_info)

# MCLAG info
mclag_info = client.control_plane.mclag()
print("MCLAG Info:", mclag_info)

# LACP info
lacp_info = client.control_plane.lacp()
print("LACP Info:", lacp_info)

# VRRP info
vrrp_info = client.control_plane.vrrp()
print("VRRP Info:", vrrp_info)
```

---

### Fabric Manager (FM) API

> | Operation Type | Description |
> |----------------|-------------|
> | **Day 1** | Initial provisioning and configuration — defining intents, validating, and deploying to SONiC switches |
> | **Day 2** | Ongoing lifecycle management — backups, restores, patches, and config drift monitoring |

#### Day 1 — Fabric & Intent Management

```python
# List all fabrics
fabrics = client.fm.listFabric()
print("Fabrics:", fabrics)

# Upload an intent (initial desired state)
client.fm.uploadIntent({"fabricId": "fab1", "intent": "..."})

# Validate the uploaded intent before applying
client.fm.validateIntent({"fabricId": "fab1"})

# Check validation results
validation = client.fm.getIntentValidation(fabricId="fab1")
print("Validation:", validation)

# Apply the intent to provision the fabric
client.fm.applyIntent({"fabricId": "fab1"})

# Check provisioning status
status = client.fm.getIntentStatus(fabricId="fab1")
print("Intent Status:", status)
```

#### Day 2 — Config Lifecycle Management

```python
# Backup current device configuration
backup = client.fm.backupConfig({
        "data": [{"ip": "xx.xx.xx.xx", "label": "my-backup"}]
})
print("Backup Config:", backup)

# Diff current config against last known good state
diff = client.fm.diffConfig(fabricId="fab1")
print("Config Diff:", diff)

# Restore a previously backed-up configuration
client.fm.restoreConfig({"fabricId": "fab1", "backupId": "bkp123"})

# Commit pending configuration changes
client.fm.commitConfig({"fabricId": "fab1"})

# Check config operation status
config_status = client.fm.getConfigStatus(fabricId="fab1")
print("Config Status:", config_status)
```

#### Device Operations

```python
# List devices in a fabric
devices = client.fm.listDevice(fabricId="fab1")
print("Devices:", devices)

# Reboot a device
client.fm.rebootDevice({"deviceId": "dev1"})

# Upgrade device firmware
client.fm.upgradeDevice({"deviceId": "dev1", "version": "4.2.0"})
```

#### Tenant Management

```python
# Add a tenant (logical network partition)
client.fm.addTenant({"fabricId": "fab1", "tenantName": "tenant-a"})

# List tenants
tenants = client.fm.listTenant(fabricId="fab1")
print("Tenants:", tenants)
```

#### Job Tracking

```python
# List all async jobs
jobs = client.fm.listJobs()
print("Jobs:", jobs)

# Get status of a specific job
job_status = client.fm.getJobStatus(jobId="job-001")
print("Job Status:", job_status)
```

---

### Health API

> These APIs provide telemetry and health metrics for SONiC-managed network devices, including CPU usage, interface states, and fabric-wide health summaries.

```python
# List all managed devices
devices = client.health.device_list()
print("Devices:", devices)

# Device health info over a time range
info = client.health.device_info(
        from_date="2026-03-23 00:56:30",
        to_date="2026-03-24 09:56:30",
        window_size="1 hour",
        device_address="xx:xx:xx:xx:xx:xx"
)
print("Device Info:", info)

# Aggregated health telemetry over a time window
mega = client.health.mega(
        from_date="2026-03-23 12:05:44",
        to_date="2026-03-24 12:05:44",
        window_size="1 day",
        device_address="xx:xx:xx:xx:xx:xx"
)
print("Mega:", mega)

# Top CPU-consuming services on a device
top_services = client.health.top_cpu_consuming_services(
        device_address="xx:xx:xx:xx:xx:xx"
)
print("Top CPU Consuming Services:", top_services)

# Fabric-wide health summary
fabric_health = client.health.fabric_wise_health()
print("Fabric Wise Health:", fabric_health)
```

---

### Inventory API

> Inventory APIs expose hardware and software details of SONiC devices, including interfaces, NICs, peripherals, firmware versions, and link topology.

```python
# Device interfaces
interfaces = client.inventory.device_interfaces(device_address="xx:xx:xx:xx:xx:xx")
print("Device Interfaces:", interfaces)

# Device peripherals (PSU, fans, etc.)
peripherals = client.inventory.device_peripherals(device_address="xx:xx:xx:xx:xx:xx")
print("Device Peripherals:", peripherals)

# Device info
device_info = client.inventory.device_info(device_address="xx:xx:xx:xx:xx:xx")
print("Device Info:", device_info)

# Firmware version
firmware = client.inventory.device_firmware(device_address="xx:xx:xx:xx:xx:xx")
print("Device Firmware:", firmware)

# Link topology info
link_info = client.inventory.link_info(device_address="xx:xx:xx:xx:xx:xx")
print("Link Info:", link_info)

# Interface flap events (useful for diagnosing instability)
interface_flaps = client.inventory.interface_flaps(
        start_time="2026-03-23 02:09:36",
        end_time="2026-03-24 11:09:36",
        limit=10
)
print("Interface Flaps:", interface_flaps)

# Aggregated interface telemetry
interface_mega = client.inventory.interface_mega()
print("Interface Mega:", interface_mega)

# NIC info
nic_info = client.inventory.nic_info(device_address="xx:xx:xx:xx:xx:xx")
print("NIC Info:", nic_info)

# Full device details
device_details = client.inventory.device_details(device_address="xx:xx:xx:xx:xx:xx")
print("Device Details:", device_details)

# Orchestration inventory details
inv_details_orchest = client.inventory.inv_details_orchest()
print("Inventory Details (Orchestration):", inv_details_orchest)

# YAML config files per device
device_yaml_files = client.inventory.device_yaml_files()
print("Device YAML Files:", device_yaml_files)

# Condensed inventory summary
mini_inventory = client.inventory.mini_inventory()
print("Mini Inventory:", mini_inventory)
```

---

### Misc API

> Miscellaneous APIs expose global platform settings and feature flags.

```python
# Check if Fabric Manager is enabled
is_fm_enabled = client.misc.is_fm_enabled()
print("Is FM Enabled:", is_fm_enabled)

# World map topology data
world_map_data = client.misc.world_map_data()
print("World Map Data:", world_map_data)

# Check if AI assistant is enabled
is_ai_assistant_enabled = client.misc.is_ai_assistant_enabled()
print("Is AI Assistant Enabled:", is_ai_assistant_enabled)

# Retrieve illustrator YAML (topology visualization config)
illustrator_yaml = client.misc.get_illustrator_yaml()
print("Illustrator YAML:", illustrator_yaml)

# List regions
region_list = client.misc.region_list()
print("Region List:", region_list)

# Telemetry preferences
telemetry_preferences = client.misc.telemetry_preferences()
print("Telemetry Preferences:", telemetry_preferences)
```

---

### Traffic API

> Traffic APIs provide interface-level traffic telemetry for SONiC switches, including **PFC (Priority Flow Control)** — a lossless Ethernet mechanism used in data center networks to prevent buffer overflow on specific traffic priorities.

```python
# Check if PFC is enabled on an interface
pfc_status = client.traffic.is_interf_pfc_enabled(
        device_address="xx:xx:xx:xx:xx:xx",
        ifname="Ethernet1"
)
print("PFC Enabled:", pfc_status)

# List traffic profiles
traffic_list = client.traffic.traffic_list(device_address="xx:xx:xx:xx:xx:xx")
print("Traffic List:", traffic_list)

# Interface details with layer and licensing context
interface_details = client.traffic.get_interface_details(
        device_address="xx:xx:xx:xx:xx:xx",
        hostname="switch1",
        ipaddress="192.168.1.1",
        layer="L2",
        time_bucket="5m",
        window_size=10,
        license_="standard"
)
print("Interface Details:", interface_details)

# Detailed interface telemetry over a time range
interface_details_range = client.traffic.interface_details(
        from_date="2024-06-01T00:00:00Z",
        to_date="2024-06-02T00:00:00Z",
        window_size=10,
        device_address="xx:xx:xx:xx:xx:xx",
        active_tab="tab1",
        ifname="Ethernet1"
)
print("Interface Details (Time Range):", interface_details_range)

# Aggregated traffic telemetry
traffic_mega = client.traffic.traffic_mega(
        from_date="2024-06-01T00:00:00Z",
        to_date="2024-06-02T00:00:00Z",
        window_size=10,
        device_address="xx:xx:xx:xx:xx:xx",
        active_tab="tab1",
        ifname="Ethernet1"
)
print("Traffic Mega:", traffic_mega)

# QoS priority mapping for an interface
priority_mapping = client.traffic.priority_mapping(
        device_address="xx:xx:xx:xx:xx:xx",
        ifname="Ethernet1"
)
print("Priority Mapping:", priority_mapping)
```

---

## Testing

```bash
pytest tests/
```

---

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Ensure all tests pass before submitting a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Links

- [PyPI Package](https://pypi.org/project/ones_pyapi/)
- [GitHub Repository](https://github.com/AvizNetworks/ones-pyapi)

---

&copy; 2026 Aviz Networks. All rights reserved.

For questions, support, or feature requests, please [open an issue](https://github.com/AvizNetworks/ones-pyapi/issues) or contact the maintainers via [GitHub](https://github.com/AvizNetworks/ones-pyapi).
