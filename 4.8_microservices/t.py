import requests
import aiohttp
import asyncio
import sys
# result = requests.get("http://127.0.0.1:8081/fal")
# print(result.text)

policy = asyncio.WindowsSelectorEventLoopPolicy()
asyncio.set_event_loop_policy(policy)

conn = aiohttp.TCPConnector()


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8081/fal") as resp:
            print(resp.status)
            print(await resp.text())

asyncio.run(main())
