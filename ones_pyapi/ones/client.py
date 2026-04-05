# ones/client.py

import requests
from .transport import Transport
from .resources.user import UserResource
from .resources.health import HealthResource
from .resources.inventory import InventoryResource
from .resources.traffic import TrafficResource
from .resources.bgp import BGPResource
from .resources.control_plane import ControlPlaneResource  
from .resources.misc import MiscResource
from .resources.device import DeviceResource
from .resources.fm import FMResource

class ONESClient:
    def __init__(self, url, username=None, password=None):
        self.url = url
        self.username = username
        self.password = password

        self.transport = Transport(base_url=url)

        # attach resources
        self.user = UserResource(self.transport)

        # attach health
        self.health = HealthResource(self.transport)

        # attch inventory
        self.inventory = InventoryResource(self.transport)

        # attach traffic
        self.traffic = TrafficResource(self.transport)

        # attach BGP
        self.bgp = BGPResource(self.transport)

        # attch control plane
        self.control_plane = ControlPlaneResource(self.transport)

        # attach misc
        self.misc = MiscResource(self.transport)

        #attach device
        self.device = DeviceResource(self.transport)

        # Attach FM 
        self.fm = FMResource(self.transport)

    def connect(self):
        import requests

        resp = requests.post(
            f"{self.url}/api/user/login",
            json={
                "username": self.username,
                "password": self.password,
                "extendedExpiry": False
            },
            verify=False
        )

        print("STATUS:", resp.status_code)
        print("RAW RESPONSE:", resp.text)   # 👈 VERY IMPORTANT

        if resp.status_code != 200:
            raise Exception(resp.text)

        try:
            data = resp.json()
        except Exception:
            raise Exception(f"Invalid JSON response: {resp.text}")

        token = data["data"]["token"]
        self.transport.set_token(token)