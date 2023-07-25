from client import FMClient

conn = FMClient(url = "http://10.x.x.x:port_number")
result = conn.get_controller_version()
print(result)
