import asyncio
import aiohttp
import argparse
from pysmartthings import SmartThings
import json

parser = argparse.ArgumentParser(description='List devices in a SmartThings location.')

# Adding arguments
parser.add_argument('--location', required=True, help='Name of the location')
parser.add_argument('--key', required=True, help='API key')
parser.add_argument('--devicename', required=True, help='(part of) The name of the device. If part of the name is given, all devices matching the searchstring will be listed.')
                    
# Parse arguments
args = parser.parse_args()

location_name = args.location
key = args.key
name = args.devicename

async def main():
    async with aiohttp.ClientSession() as session:
        api = SmartThings(session, key)
        locations = await api.locations()
        if len(locations) == 0:
            print("no locations for that API key")
        location_id = next(loc.location_id for loc in locations if loc.name == location_name)

        devices = await api.devices()
        if len(devices) == 0:
            print("no devices for that API key")
        device_data = []
        for device in devices:
            if name in device.label:
                # Add device info to the list as a dictionary
                device_data.append({"name": device.label, "device_id": device.device_id})

        # Convert the list of dictionaries to a JSON string
        json_output = json.dumps(device_data, indent=4)
        print(json_output)  # Print the JSON string
            
asyncio.run(main())