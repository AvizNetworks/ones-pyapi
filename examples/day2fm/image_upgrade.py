from client import FMClient

conn = FMClient(url = "http://10.x.x.x:port_number") 
payload_for_image_upgrade = [{"ip":"10.x.x.3","pathToImage":"http://10.x.x.x:8192/path_of_file/filename.bin"}]
result = conn.custom_image_upgrade(payload_for_image_upgrade)
