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