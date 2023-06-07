from OnesClient.client import ONESClient


my_client = ONESClient(url='https://localhost:3002', username='superadmin', password='Admin@123')

my_client.connect()
my_client.get_hardware_info()