from ones.client import ONESClient

client = ONESClient(
    url="https://your-instance/",
    username="your_username",
    password="your_password"
)

client.connect()


# Add methofs for above calls
is_fm_enabled = client.misc.is_fm_enabled()
print("Is FM Enabled:", is_fm_enabled)

world_map_data = client.misc.world_map_data()
print("World Map Data:", world_map_data)

is_ai_assistant_enabled = client.misc.is_ai_assistant_enabled()
print("Is AI Assistant Enabled:", is_ai_assistant_enabled)

illustrator_yaml = client.misc.get_illustrator_yaml()
print("Illustrator YAML:", illustrator_yaml)

region_list = client.misc.region_list()
print("Region List:", region_list)

telemetry_preferences = client.misc.telemetry_preferences()
print("Telemetry Preferences:", telemetry_preferences)
