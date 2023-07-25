from client import FMClient
import json

conn = FMClient(url = "http://10.x.x.2:8787")

# Taking Backup at config
payload = [{"ip":"10.x.x.1","label":"test_backup"}]
result = conn.backup_on_config(payload)

# Get all backups
payload = ["10.x.x.12","10.x.x.11"]
result = conn.backups(payload)

# Restore any backup as per timestamp
payload = [
    {"ip":"10.x.x.12","timestamp":"USERINPUT"},
    {"ip":"10.x.x.11","timestamp":"USERINPUT"}
]
result = conn.restore_config(payload)
