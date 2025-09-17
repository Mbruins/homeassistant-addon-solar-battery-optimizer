import asyncio
from config import load_config, parse_args
from tibber_client import TibberClient
from solar_client import SolarClient
from ha_api import HAAPI
from scheduler import Scheduler

async def main():
    args = parse_args()
    cfg = load_config(args.config)

    # Initialize clients
    tibber = TibberClient(cfg["tibber_token"])
    solar = SolarClient(cfg["latitude"], cfg["longitude"])
    ha = HAAPI(token=open("/data/token").read().strip())

    # Fetch forecasts
    prices = await tibber.get_price_forecast(cfg["forecast_days"])
    solar_forecast = await solar.get_solar_forecast(cfg["forecast_days"])

    # Read battery states
    batteries = []
    for entity in cfg["battery_entities"]:
        state = await ha.get_states(entity)
        batteries.append({"entity": entity, "soc": float(state["state"])})

    # Compute optimal charge times
    slots = Scheduler.compute_charge_slots(
        solar_forecast, prices, batteries, cfg["night_start"], cfg["night_end"]
    )

    # Schedule charges on top slots
    for time, score in slots[: len(batteries) * cfg["forecast_days"]]:
        await ha.call_service("battery", "set_charge_schedule", {
            "entity_id": cfg["battery_entities"][0],
            "start_time": time.isoformat(),
            "duration": 3600
        })

if __name__ == "__main__":
    asyncio.run(main())
