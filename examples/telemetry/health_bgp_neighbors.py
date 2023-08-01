from restclient.telemetry.client import ONESClient 

conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")

print("HEALTH_BGP NEIGHBORS")
query_params = {
  "fromDate" : "2023-04-04 04:54:27",
  "toDate" : "2023-04-04 05:54:27",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_health_bgp_neighbors(query_params))