from client import FMClient
import json

# Setting Up connection
conn = FMClient(url = "http://10.x.x.2:8787")
result = conn.get_controller_version()

# result = conn.get_intent_status()


payload = ["10.x.x.2"]

status =  conn.get_image_mgmnt_status(payload)
print(json.dumps(status, indent= 4))
# result = conn.reboot(payload)



result = conn.ztp_enable(payload) # list of IPs

result = conn.controller_fm_version()

payload = ["10.x.x.2", "10.x.x.3"] 

result = conn.get_image_mgmnt_status(payload)
"""
    # [{'old_image': '', 'device_action': '1', 'new_image': '', 'ip': '10.x.x.2', 'last_upgraded':
    # None, 'verification_status': '', 'last_reload': None, 'config_status': '', 'logs': ''}]
    # For 10.x.x.3 , data not available
"""

payload_for_image_upgrade = [{"ip":"10.x.x.3","pathToImage":"http://10.x.x.x:8192/path_of_file/filename.bin"}]
result = conn.custom_image_upgrade(payload_for_image_upgrade) #[{"ip":"10.x.x.3","pathToImage":"http://10.x.x.x:8192/path_of_file/filename.bin/home/tarun/ztp/sonic-mellanox-kuldip.bin"}]

payload_for_config_diff = { "ip": "10.4.4.66"}
result = conn.get_config_diff(payload_for_config_diff)

# Calling BGP operation

file = "<Path of Yaml file>"
flag = True 
result = conn.bgp_operation(config_file_path=file, diff_flag=flag)


# UPLOAD 
file = "<Path of Yaml file>"
result = conn.day1_intent_ovd_template(file)


#RMA

payload = [{"ip":"10.x.x.1","label":"test_backup"}]
result = conn.backup_on_config(payload)


payload = ["10.x.x.12","10.x.x.11"]
result = conn.backups(payload)

payload = [
    {"ip":"10.x.x.12","timestamp":"USERINPUT"},
    {"ip":"10.x.x.11","timestamp":"USERINPUT"}
]
result = conn.restore_config(payload)



