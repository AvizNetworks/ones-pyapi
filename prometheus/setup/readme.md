# Steps for Integrate ONES with Prometheus

1. Copy queries.yml, prometheus.yml provided in the [repo](https://github.com/AvizNetworks/prometheus) to an appropriate folder
2. Spawn dockers using docker-compose.yml
3. This should bring up the prometheus web server at http://127.0.0.1:9090 and pull the metrics collected by ONES in few minutes
4. This utilizes ports 9090 & 9187. These ports should be available for this solution to work.
5. The data will be up in few minutes.


