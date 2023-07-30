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