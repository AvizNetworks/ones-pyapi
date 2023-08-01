from restclient.telemetry.client import ONESClient 

conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")

conn.connect() 

print("SWITCH_SKUs")
print(conn.get_switch_skus())