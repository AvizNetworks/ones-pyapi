from restclient.telemetry.client import ONESClient

conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")


conn.connect()
query_params = {
  "ipAddress": "10.x.x.x"
}

print(conn.get_ipv6_utilization(query_params))
