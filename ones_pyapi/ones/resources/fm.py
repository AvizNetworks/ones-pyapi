from .base import BaseResource


class FMResource(BaseResource):
    BASE = "/api/config"

    # =====================================
    # FABRIC APIs
    # =====================================
    def listFabric(self):
        return self._get(f"{self.BASE}/listFabric")

    def getFabric(self, fabricId):
        return self._get(f"{self.BASE}/getFabric", filters={"fabricId": fabricId})

    def createFabric(self, payload):
        return self._post(f"{self.BASE}/createFabric", payload)

    def deleteFabric(self, payload):
        return self._post(f"{self.BASE}/deleteFabric", payload)

    def updateFabric(self, payload):
        return self._patch(f"{self.BASE}/updateFabric", payload)

    # =====================================
    # INTENT APIs (DAY-1)
    # =====================================
    def uploadIntent(self, payload):
        return self._post(f"{self.BASE}/uploadIntent", payload)

    def validateIntent(self, payload):
        return self._post(f"{self.BASE}/validateIntent", payload)

    def getIntentValidation(self, fabricId):
        return self._get(
            f"{self.BASE}/getIntentValidation",
            filters={"fabricId": fabricId}
        )

    def applyIntent(self, payload):
        return self._post(f"{self.BASE}/applyIntent", payload)

    def getIntentStatus(self, fabricId):
        return self._get(
            f"{self.BASE}/getIntentStatus",
            filters={"fabricId": fabricId}
        )

    # =====================================
    # CONFIG APIs (DAY-2)
    # =====================================
    def backupConfig(self, payload):
        return self._post(f"{self.BASE}/backupConfig", payload)

    def restoreConfig(self, payload):
        return self._post(f"{self.BASE}/restoreConfig", payload)

    def replaceConfig(self, payload):
        return self._post(f"{self.BASE}/replaceConfig", payload)

    def diffConfig(self, fabricId):
        return self._get(
            f"{self.BASE}/diffConfig",
            filters={"fabricId": fabricId}
        )

    def commitConfig(self, payload):
        return self._post(f"{self.BASE}/commitConfig", payload)

    def getConfigStatus(self, fabricId):
        return self._get(
            f"{self.BASE}/getConfigStatus",
            filters={"fabricId": fabricId}
        )

    # =====================================
    # DEVICE APIs
    # =====================================
    def listDevice(self, fabricId):
        return self._get(
            f"{self.BASE}/listDevice",
            filters={"fabricId": fabricId}
        )

    def getDevice(self, deviceId):
        return self._get(
            f"{self.BASE}/getDevice",
            filters={"deviceId": deviceId}
        )

    def rebootDevice(self, payload):
        return self._post(f"{self.BASE}/rebootDevice", payload)

    def upgradeDevice(self, payload):
        return self._post(f"{self.BASE}/upgradeDevice", payload)

    def replaceDevice(self, payload):
        return self._post(f"{self.BASE}/replaceDevice", payload)

    # =====================================
    # TENANT APIs
    # =====================================
    def addTenant(self, payload):
        return self._post(f"{self.BASE}/addTenant", payload)

    def deleteTenant(self, payload):
        return self._post(f"{self.BASE}/deleteTenant", payload)

    def listTenant(self, fabricId):
        return self._get(
            f"{self.BASE}/listTenant",
            filters={"fabricId": fabricId}
        )

    # =====================================
    # JOB APIs
    # =====================================
    def listJobs(self):
        return self._get(f"{self.BASE}/listJobs")

    def getJobStatus(self, jobId):
        return self._get(
            f"{self.BASE}/getJobStatus",
            filters={"jobId": jobId}
        )

    # =====================================
    # GENERIC FALLBACK (KEEP THIS)
    # =====================================
    def customGET(self, path, filters=None):
        return self._get(path, filters=filters)

    def customPOST(self, path, payload=None):
        return self._post(path, payload)

    def customPATCH(self, path, payload=None):
        return self.transport.request("PATCH", path, json=payload)