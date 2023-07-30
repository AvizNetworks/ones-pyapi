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