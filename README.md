# ONES PyAPI

Aviz ONES is the industry's first multi-vendor platform which provides seamless network orchestration and monitoring capabilities. From storing the physical topology, device health, utilization and network events, it also provides network orchestration/automation for the data center fabric deployments. All this fleet-wide data is provided to the network administrators using standardized ONES APIs. ONES Provides a smooth transition for Network Admin for SONiC transition depending on the consumption model.

ONES APIs supports following interfaces
- gNMI (Secured using certificates)
- REST API (Secured using user tokens)


## Features
> Can connect with python environment and make ONES APIs operation seamlessly.
> For Developers and Network Engineers


## Installation

Please follow the below steps to install ONES PyAPI client and use Day1, Day2 and NetOPs APIs with single function call.


### Prerequisites
- python 3.9 and above
- pip 21.2.4 and above
- download ones-pyapi-1.0.0.tar.gz package from [here](https://github.com/AvizNetworks/ones-pyapi/blob/master/versions/ones-pyapi-1.0.0.tar.gz)

### Install package
```sh
pip install ones-pyapi-1.0.0.tar.gz
```
if above command not worked, tried with pip3
```sh
pip3 install ones-pyapi-1.0.0.tar.gz
```

Now you can Import and use clients, please refer below examples - 
1. NetOps Monitoring API call - [link](https://github.com/AvizNetworks/ones-pyapi/tree/master/examples/telemetry)
2. Day1 Operations - [link](https://github.com/AvizNetworks/ones-pyapi/tree/master/examples/day1fm)
3. Day2 Operations - [link](https://github.com/AvizNetworks/ones-pyapi/tree/master/examples/day2fm)


If something went wrong. or Expecting new features, let us know - [here](https://github.com/AvizNetworks/ones-pyapi/issues)
