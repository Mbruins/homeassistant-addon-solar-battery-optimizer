import json
import argparse

def load_config(path):
    data = json.loads(open(path).read())
    return {
        "latitude": data["latitude"],
        "longitude": data["longitude"],
        "forecast_days": data["forecast_days"],
        "tibber_token": data["tibber_token"],
        "battery_entities": data["battery_entities"],
        "envoy_entity": data["envoy_entity"],
        "solar_entity": data["solar_panel_entity"],
        "night_start": data["night_start"],
        "night_end": data["night_end"]
    }

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    return parser.parse_args()
