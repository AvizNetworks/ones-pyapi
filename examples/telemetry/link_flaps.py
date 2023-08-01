from restclient.telemetry.client import ONESClient 

conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")

print("LINK_FLAPS.")
query_params= {
  "time" : "5 minutes",
  "limit" : "10"
}
print(conn.get_link_flaps(query_params))