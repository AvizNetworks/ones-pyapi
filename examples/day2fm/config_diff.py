from client import FMClient

payload_for_config_diff = { "ip": "109.x.x.x6"}
result = conn.get_config_diff(payload_for_config_diff)