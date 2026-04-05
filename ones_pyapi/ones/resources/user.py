# ones/resources/user.py

from .base import BaseResource


class UserResource(BaseResource):
    BASE = "/api/user"

    def list(self, filters=None):
        return self._get(self.BASE, filters)

    def roles(self):
        return self._get(f"{self.BASE}/role")

    def preferences(self):
        return self._get(f"{self.BASE}/preferences")