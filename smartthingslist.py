import asyncio
import aiohttp
import argparse
from pysmartthings import SmartThings

parser = argparse.ArgumentParser(description='List devices in a SmartThings location.')

# Adding arguments
parser.add_argument('--location', required=True, help='Name of the location')
parser.add_argument('--key', required=True, help='API key')

# Parse arguments
args = parser.parse_args()

location_name = args.location
key = args.key

async def main():
    async with aiohttp.ClientSession() as session:
        api = SmartThings(session, key)
        locations = await api.locations()
        if len(locations) == 0:
            print("no locations for that API key")
        location_id = next(loc.location_id for loc in locations if loc.name == location_name)
        
        print ("location_id: ", location_id)

        devices = await api.devices()
        if len(devices) == 0:
            print("no devices for that API key")
        for device in devices:
            if 'NUC' in device.label:
                print("found device: ", device.device_id, device.name, device.label)
            
asyncio.run(main())