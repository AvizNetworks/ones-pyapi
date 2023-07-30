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