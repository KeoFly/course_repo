from time import time
import requests
import asyncio
import aiohttp

def get_html(link):
    r = requests.get(link)
    text = r.text
    
start = time()
get_html("https://www.google.ru")
get_html("https://www.google.ru")
get_html("https://www.google.ru")
get_html("https://www.google.ru")
print(time() - start)

async def get_html_async(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            data = await response.text()

start = time()
urls = [get_html_async("https://www.google.ru") for url in range(5)]
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.gather(*urls))
print(time() - start)