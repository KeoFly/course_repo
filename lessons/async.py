import asyncio
import aiohttp

async def get_data(url):
    print(f"Start: {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(len(data))

urls = ["https://www.google.ru", "https://yandex.ru"]

jobs = [get_data(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*jobs))