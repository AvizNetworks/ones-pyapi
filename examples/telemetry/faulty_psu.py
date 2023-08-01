from restclient.telemetry.client import ONESClient 

conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")

print("FAULTY_PSUs.")
print(conn.get_faulty_psus())