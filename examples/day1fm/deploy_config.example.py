from client import FMClient

conn = FMClient(url = "http://10.x.x.2:8787")

file = "path of YAML file"
result = conn.day1_intent_ovd_template(file)