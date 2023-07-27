## Data Models

```sh
gnmic -a 10.4.4.61:50052 -u admin -p YourPaSsWoRd --skip-verify capabilities
gNMI version: 1.1.0
supported models:
  - openconfig-bgp, OpenConfig working group, 6.1.1
  - openconfig-if-ethernet,, OpenConfig working group, 2.12.0
  - openconfig-lldp, OpenConfig working group, 0.2.1
  - openconfig-platform-fan, OpenConfig working group, 0.1.1
  - openconfig-platform-psu, OpenConfig working group, 0.2.1
  - openconfig-platform-transceiver, OpenConfig working group, 0.8.0
  - system/processes, Aviz Networks Inc, 0.1.0
supported encodings:
  - PROTO
```

# GNMI Open Config Path Subscriptions
## System Resources 

```sh
gnmic -a 10.4.4.61::50052 -u admin -p YourPaSsWoRd --skip-verify subscribe --path “/system/processes/“ --stream-mode sample --sample-interval 10s --qos 0
```

Output:
```sh
{
  "source": "10.4.4.61:50052",
  "subscription-name": "default-1679454364",
  "timestamp": 1679454358297960118,
  "time": "2023-03-21T20:05:58.297960118-07:00",
  "updates": [
    {
      "Path": "system/processes/process[pid=47]/state/pid",
      "values": {
        "system/processes/process/state/pid": 47
      }
    },
    {
      "Path": "system/processes/process[pid=47]/state/name",
      "values": {
        "system/processes/process/state/name": "ae6a64f24a2d|syncd"
      }
    },
    {
      "Path": "system/processes/process[pid=47]/state/cpu-utilization",
      "values": {
        "system/processes/process/state/cpu-utilization": 7
      }
    },
    {
      "Path": "system/processes/process[pid=47]/state/memory-usage",
      "values": {
        "system/processes/process/state/memory-usage": 890241024
      }
    },
    {
      "Path": "system/processes/process[pid=47]/state/memory-utilization",
      "values": {
        "system/processes/process/state/memory-utilization": 5
      }
    },
    {
      "Path": "system/processes/process[pid=12]/state/pid",
      "values": {
        "system/processes/process/state/pid": 12
      }
    },
    {
      "Path": "system/processes/process[pid=12]/state/name",
      "values": {
        "system/processes/process/state/name": "cc982c3fba68|teamd"
      }
    },
    {
      "Path": "system/processes/process[pid=12]/state/cpu-utilization",
      "values": {
        "system/processes/process/state/cpu-utilization": 0
      }
    },
    {
      "Path": "system/processes/process[pid=12]/state/memory-usage",
      "values": {
        "system/processes/process/state/memory-usage": 31572623
      }
    },
    {
      "Path": "system/processes/process[pid=12]/state/memory-utilization",
      "values": {
        "system/processes/process/state/memory-utilization": 0
      }
    },
    {
      "Path": "system/processes/process[pid=41]/state/pid",
      "values": {
        "system/processes/process/state/pid": 41
      }
    }
```


## BGP control plane

```sh
gnmic -a 10.4.4.61:50052 -u admin -p YourPaSsWoRd --skip-verify subscribe --path “/network-instances/“ --stream-mode sample --sample-interval 10s --qos 0
```

Output:

```sh
{
  "source": "10.4.4.61:50052",
  "subscription-name": "default-1679454307",
  "timestamp": 1679454302398028996,
  "time": "2023-03-21T20:05:02.398028996-07:00",
  "updates": [
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/messages/received/UPDATE",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/UPDATE": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/messages/sent/UPDATE",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/sent/UPDATE": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/messages/received/NOTIFICATON",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/NOTIFICATON": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/messages/sent/NOTIFICATON",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/sent/NOTIFICATON": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/messages/received/KEEPALIVE",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/KEEPALIVE": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/messages/sent/KEEPALIVE",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/sent/KEEPALIVE": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/messages/received/ROUTEREFRESH",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/ROUTEREFRESH": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/messages/sent/ROUTEREFRESH",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/sent/ROUTEREFRESH": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/established-transitions",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/established-transitions": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/dropped-transitions",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/dropped-transitions": 0
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/local-as",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/local-as": 3003
      }
    },
    {
      "Path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=20.0.0.33]/state/last-established",
      "values": {
        "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/last-established": 0
      }
    },
```

## LLDP neighbors

```sh
gnmic -a 10.4.4.61:50052 -u admin -p YourPaSsWoRd --skip-verify subscribe --path “/lldp/interfaces/“ --stream-mode sample --sample-interval 10s --qos 0
```

Output:

```sh
{
  "source": "10.4.4.61:50052",
  "subscription-name": "default-1679454247",
  "timestamp": 1679454240385622169,
  "time": "2023-03-21T20:04:00.385622169-07:00",
  "updates": [
    {
      "Path": "lldp/interfaces/interface[name=eth0]/neighbors/neighbor[name=1095]/state/system-name",
      "values": {
        "lldp/interfaces/interface/neighbors/neighbor/state/system-name": "sonic"
      }
    },
    {
      "Path": "lldp/interfaces/interface[name=eth0]/neighbors/neighbor[name=1095]/state/system-description",
      "values": {
        "lldp/interfaces/interface/neighbors/neighbor/state/system-description": "SONiC Software Version: SONiC.4.0.3-Enterprise_Base - HwSku: DellEMC-S5248f-P-25G-DPB - Distribution: Debian 10.13 - Kernel: 4.19.0-9-2-amd64"
      }
    },
    {
      "Path": "lldp/interfaces/interface[name=eth0]/neighbors/neighbor[name=1095]/state/chassis-id",
      "values": {
        "lldp/interfaces/interface/neighbors/neighbor/state/chassis-id": "0c:d5:48:a0:00:00"
      }
    },
    {
      "Path": "lldp/interfaces/interface[name=eth0]/neighbors/neighbor[name=1095]/state/chassis-id-type",
      "values": {
        "lldp/interfaces/interface/neighbors/neighbor/state/chassis-id-type": "MAC_ADDRESS"
      }
    },
    {
      "Path": "lldp/interfaces/interface[name=eth0]/neighbors/neighbor[name=1095]/state/id",
      "values": {
        "lldp/interfaces/interface/neighbors/neighbor/state/id": "1095"
      }
    },
    {
      "Path": "lldp/interfaces/interface[name=eth0]/neighbors/neighbor[name=1095]/state/port-id",
      "values": {
        "lldp/interfaces/interface/neighbors/neighbor/state/port-id": "eth0"
      }
    },
```

## Device interfaces

```sh
gnmic -a 10.4.4.61:50052 -u admin -p YourPaSsWoRd --skip-verify subscribe --path “/interfaces/interface/“ --stream-mode sample --sample-interval 10s --qos 0
```

Output:

```sh
{
  "source": "10.4.4.61:50052",
  "subscription-name": "default-1679453426",
  "timestamp": 1679453419863002971,
  "time": "2023-03-21T19:50:19.863002971-07:00",
  "updates": [
    {
      "Path": "interfaces/interface[name=Ethernet212]/state/admin-status",
      "values": {
        "interfaces/interface/state/admin-status": "up"
      }
    },
    {
      "Path": "interfaces/interface[name=Ethernet212]/ethernet/state/port-speed",
      "values": {
        "interfaces/interface/ethernet/state/port-speed": "ETHERNET_SPEED::SPEED_100GB"
      }
    },
    {
      "Path": "interfaces/interface[name=Ethernet212]/state/oper-status",
      "values": {
        "interfaces/interface/state/oper-status": "down"
      }
    },
    {
      "Path": "interfaces/interface[name=Ethernet212]/state/fec-mode",
      "values": {
        "interfaces/interface/state/fec-mode": "INTERFACE_FEC::FEC_DISABLED"
      }
    },
    {
      "Path": "interfaces/interface[name=Ethernet212]/state/ifindex",
      "values": {
        "interfaces/interface/state/ifindex": 27
      }
    },
    {
      "Path": "interfaces/interface[name=Ethernet212]/state/mtu",
      "values": {
        "interfaces/interface/state/mtu": 9100
      }
    },
    {
      "Path": "interfaces/interface[name=Ethernet212]/state/lanes",
      "values": {
        "interfaces/interface/state/lanes": "221,222"
      }
    },
```

## Platform peripherals

```sh
gnmic -a 10.4.4.61:50052 -u admin -p YourPaSsWoRd --skip-verify subscribe --path "components/component" --stream-mode sample --sample-interval 100s --qos 0
```

Output:
```sh
{
  "source": "10.4.4.61:50052",
  "subscription-name": "default-1679453218",
  "timestamp": 1679453211742825610,
  "time": "2023-03-21T19:46:51.74282561-07:00",
  "updates": [
    {
      "Path": "components/component[name=FAN-2R]/state/removable",
      "values": {
        "components/component/state/removable": true
      }
    },
    {
      "Path": "components/component[name=FAN-2R]/state/oper-status",
      "values": {
        "components/component/state/oper-status": "COMPONENT_OPER_STATUS::ACTIVE"
      }
    },
    {
      "Path": "components/component[name=FAN-2R]/state/empty",
      "values": {
        "components/component/state/empty": false
      }
    },
```