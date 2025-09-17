import aiohttp
import datetime

class SolarClient:
    def __init__(self, lat, lon):
        self.api_url = "https://api.solarforecast.io/v1/forecast"
        self.lat, self.lon = lat, lon

    async def get_solar_forecast(self, days):
        end = datetime.datetime.utcnow() + datetime.timedelta(days=days)
        params = {
            "lat": self.lat,
            "lon": self.lon,
            "end": end.isoformat() + "Z"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, params=params) as resp:
                data = await resp.json()
        # Return list of {time, irradiance}
        return data["hourly"]
