import aiohttp
import asyncio

async def fetch(client):
    async with client.get('https://github.com/') as response:
        # print(type(response))
        return await response.text()

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as client:
        response = await fetch(client)
        print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
