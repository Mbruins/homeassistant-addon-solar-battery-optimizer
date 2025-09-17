import asyncio
import os
from aiohttp import ClientSession, WSMsgType

class HAAPI:
    def __init__(self, token=None):
        self.url = os.getenv("HASS_URL", "http://supervisor/core")
        self.token = token

    async def call_service(self, domain, service, data):
        url = f"{self.url}/api/services/{domain}/{service}"
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        async with ClientSession() as session:
            await session.post(url, json=data, headers=headers)

    async def get_states(self, entity_id):
        url = f"{self.url}/api/states/{entity_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        async with ClientSession() as session:
            resp = await session.get(url, headers=headers)
        return await resp.json()
