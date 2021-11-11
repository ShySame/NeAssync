# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
from aiohttp import ClientSession
import time

SITE_1 = 'https://api.open-meteo.com/v1/forecast?latitude=51.5002&longitude=-0.1262&current_weather=True'
SITE_2 = 'https://www.metaweather.com/api/location/44418/'
SITE_3 = 'https://www.7timer.info/bin/astro.php?lon=-0.120&lat=51.5&unit=civillight&output=json&tzshift=0'


async def open_meteo(site, session):
    async with session.get(site) as r:
        status = r.status
        print(f"{site} status is {status}")
        data = await r.json()
    temp = data['current_weather']['temperature']
    await asyncio.sleep(1)
    return temp


async def meta_weather(site, session):
    async with session.get(site) as r:
        status = r.status
        print(f"{site} status is {status}")
        data = await r.json()
    temp = data['consolidated_weather'][0]['the_temp']
    await asyncio.sleep(1)
    return temp


async def timer_7(site, session):
    async with session.get(site) as r:
        status = r.status
        print(f"{site} status is {status}")
        data = await r.json(content_type='text/html')
    temp = data['dataseries'][0]['temp2m']
    await asyncio.sleep(1)
    return temp


async def main():
    async with ClientSession() as session:
        res = await asyncio.gather(open_meteo(SITE_1, session), meta_weather(SITE_2, session), timer_7(SITE_3, session))
    return round(sum(res) / len(res), 2)


if __name__ == '__main__':
    start = time.time()
    print("Start stealing")
    print(asyncio.run(main()))
    print(f"Successfully stolen in {time.time() - start} minutes")
