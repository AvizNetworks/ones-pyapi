from .base import BaseResource

class MiscResource(BaseResource):
    BASE = "/api/misc"

    def is_fm_enabled(self):
        return self._get(f"{self.BASE}/isFmEnabled")

    def world_map_data(self):
        return self._get(f"{self.BASE}/world-map-data")

    def is_ai_assistant_enabled(self):
        return self._get(f"{self.BASE}/is-ai-assistant-enabled")

    def get_illustrator_yaml(self):
        return self._get(f"{self.BASE}/get-illustrator-yaml")

    def region_list(self):
        return self._get(f"{self.BASE}/region-list")

    def telemetry_preferences(self):
        return self._get(f"{self.BASE}/telemetry-preferences")