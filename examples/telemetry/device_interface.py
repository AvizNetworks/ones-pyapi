from restclient.telemetry.client import ONESClient 

conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")


print("Device_Interfaces.")
payload  =  {
  "filter": {
    "deviceAddress": "0c:xx:xx:xx:xx:x0"
  }
}
print(conn.get_device_interfaces(payload))