import asyncio
import aiohttp
import argparse
from pysmartthings import SmartThings

parser = argparse.ArgumentParser(description='Interact with SmartThings switch devices.')

# Adding arguments
parser.add_argument('--key', required=True, help='API key')
parser.add_argument('--deviceid', required=True, help='The ID of the device.')
parser.add_argument('--action', required=True, choices=['get', 'set'], help='Action to perform (get or set the device status)')
parser.add_argument('--command', help='Command to send to the device (on or off, required if action is set)', choices=['on', 'off'])

# Parse arguments
args = parser.parse_args()

key = args.key
device_id = args.deviceid
action = args.action
command = args.command

if action == 'set' and not command:
    parser.error("--command is required when action is 'set'")

async def get_switch_status(device):
    """Get the status of a switch device."""
    if 'switch' in device.capabilities:
        await device.status.refresh()
        return device.status.switch
    return None

async def set_switch_status(device, command):
    """Send a command (on or off) to a switch device."""
    if command in ['on', 'off']:
        await device.command('main', 'switch', command)
        return f"Switch turned {command}"
    return "Invalid command"

async def main():
    async with aiohttp.ClientSession() as session:
        api = SmartThings(session, key)
        
        devices = await api.devices()
        device = next((d for d in devices if d.device_id == device_id), None)

        if device is None:
            print(f"Failed to find device with ID {device_id}")
            return

        if 'switch' in device.capabilities:
            if action == 'get':
                status = await get_switch_status(device)
                print(f"Device: {device.label}, Status: {status}")
            elif action == 'set':
                result = await set_switch_status(device, command)
                print(result)
        else:
            print(f"Device with ID {device_id} is not a switch.")

asyncio.run(main())
