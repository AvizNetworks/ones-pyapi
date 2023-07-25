from client import FMClient

conn = FMClient(url = "http://10.x.x.x:<port_number>")
result = conn.controller_fm_version()

