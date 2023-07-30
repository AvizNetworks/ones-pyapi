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
