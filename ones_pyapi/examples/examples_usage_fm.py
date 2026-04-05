
from ones.client import ONESClient

client = ONESClient(
    url="https://your-instance/",
    username="your_username",
    password="your_password"
)

client.connect()



# Testing FM Backup Config API
check =client.fm.backupConfig({
    "data": [
        {
            "ip": "xx.xx.xx.xx",
            "label": "ss"
        }
    ]
})

print(check)


