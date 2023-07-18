"""
Copyright (c) 2023, Aviz Networks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

connect = "/api/user/login"
hardware_info = "/api/inventory/hardwareMega"

# Inventory Endpoints
roles = "/api/inventory/Roles"
switch_skus = "/api/inventory/SwitchSKUs"
asics = "/api/inventory/ASICs"
agent_version = '/api/inventory/AgentsVersion'
nos_version = '/api/inventory/NOSVersion'
linux_version = '/api/inventory/LinuxVersion'
onie_version = '/api/inventory/ONIEVersion'
cabling = '/api/inventory/Cabling'
device_interfaces = "/api/inventory/Devices/interfaces"
device_peripherals = "/api/inventory/Devices/peripherals"
device_info_endpoint = "/api/inventory/Devices/device"

# Topology Endpoints
network_topology = "/api/Topologies/graphV2"

# Health Endpoints
faulty_psus = "/api/health/faultypsus"
faulty_fans = "/api/health/faultyfans"
link_flaps = "/api/health/linkflaps"
cpu_utilization = "/api/health/cpuutil"
memory_utilization = "/api/Health/memutil"
cpu_core_temperaure = "/api/health/cpucoretemp"
fan_speed = "/api/Health/fanspeed"
psu_temperature = "/api/health/psutempperature"
psu_voltage = "/api/health/psuvoltage"
psu_current = "/api/health/psucurrent"
psu_power = "/api/health/psupower"
health_services_cpu= "/api/health/servicescpu"
health_services_memory = "/api/health/servicesmemory"
health_bgp_neighbors = "/api/health/bgpnbrs"
health_transcievers = "/api/health/links/transceivers"
health_running_services = "/api/health/servicesrunning"

# Traffic Endpoints
traffic_util = "/api/Traffic/util"
traffic_counters = "/api/Traffic/counters"

