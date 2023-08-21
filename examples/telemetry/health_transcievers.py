from restclient.telemetry.client import ONESClient 

conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")

conn.connect()

print("HEALTH_TRANSCIEVERS")
query_params = {
  "ipAddress" : "10.x.x.x",
  "ifName" : "Ethernet0",
  "fromDate" : "2023-06-26 10:48:55",
  "toDate" : "2023-06-26 11:48:55"
}
print(conn.get_health_trancievers(query_params))