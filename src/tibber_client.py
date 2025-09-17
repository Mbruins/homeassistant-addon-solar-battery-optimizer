import aiohttp
import datetime

class TibberClient:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.tibber.com/v1-beta/gql"

    async def get_price_forecast(self, days):
        query = """
        {
          viewer {
            homes {
              currentSubscription {
                priceInfo {
                  today { total, startsAt }
                  tomorrow { total, startsAt }
                }
              }
            }
          }
        }
        """
        headers = {"Authorization": f"Bearer {self.token}"}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_url, json={"query": query}, headers=headers) as resp:
                result = await resp.json()
        price_data = []
        for day in ["today", "tomorrow"][:days]:
            for p in result["data"]["viewer"]["homes"][0]["currentSubscription"]["priceInfo"][day]:
                price_data.append({
                    "time": p["startsAt"],
                    "price": p["total"]
                })
        return price_data
