from client import FMClient

conn = FMClient(url = "http://10.x.x.2:8787")

result = conn.get_intent_status()
