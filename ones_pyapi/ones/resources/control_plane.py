from .base import BaseResource

class ControlPlaneResource(BaseResource):
    BASE = "/api/Control-plane" 

    def vxlan(self):
        return self._get(f"{self.BASE}/vxlan")

    def mclag(self):
        return self._get(f"{self.BASE}/mclag")
    
    def lacp(self):
        return self._get(f"{self.BASE}/lacp")
    
    def vrrp(self):
        return self._get(f"{self.BASE}/vrrp")
    
    def vlan(self):
        return self._get(f"{self.BASE}/vlan")
