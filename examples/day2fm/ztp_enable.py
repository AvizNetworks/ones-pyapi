from client import FMClient
import json

conn = FMClient(url = "http://10.x.x.x:<port_number>") 
payload = ["10.x.x.2", "10.x.x.3"] 
result = conn.ztp_enable(payload) 
