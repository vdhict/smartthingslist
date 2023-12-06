# SmartThings Device Lister

This script lists devices in a specified location from a SmartThings account. It filters the devices based on their name or a part of their name and outputs the results in JSON format.

## Installation

Before running the script, ensure you have Python installed on your system. Additionally, you need to install the `aiohttp` and `pysmartthings` libraries. You can install these dependencies using pip:

```bash
pip install aiohttp pysmartthings
```

Or use a python virtual environment. The requirements.txt file lists the required modules.

## Usage

The script requires three command line arguments:
- `--location`: The name of the location in SmartThings.
- `--key`: Your SmartThings API key.
- `--devicename`: The name or part of the name of the device.

Run the script using the following command:

```bash
python smartthingslist.py --location "YourLocationName" --key "YourAPIKey" --devicename "DeviceName"
```

Replace `script_name.py` with the name of your script file, and provide the appropriate values for each argument.

## Example Output

When you run the script, it will output device information in a JSON format. Here's an example of what the output might look like:

```json
[
    {
        "label": "Living Room Light",
        "device_id": "12345abcde"
    },
    {
        "label": "Kitchen Sensor",
        "device_id": "67890fghij"
    }
]
```

## License

MIT license
