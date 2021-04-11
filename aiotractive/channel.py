import json


class Channel:
    CHANNEL_URL = "https://channel.tractive.com/3/channel"

    def __init__(self, api):
        self._api = api

    async def listen(self):
        async with self._api.session.request(
            "POST", self.CHANNEL_URL, headers=await self._api.auth_headers()
        ) as response:
            async for data, _ in response.content.iter_chunks():
                event = json.loads(data)
                if event["message"] == "keep-alive":
                    continue
                yield event
