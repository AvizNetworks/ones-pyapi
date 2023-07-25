from client import FMClient
import json

conn = FMClient(url = "http://10.x.x.x:<port_number>")

payload = ["10.x.x.x1"]
status =  conn.get_image_mgmnt_status(payload)
print(json.dumps(status, indent= 4))