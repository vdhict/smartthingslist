# Smartthingslist

This is a small script to list Smartthings devices from a certain location, filtering on a name or part of the name.

I created this script as a companion to my home-infrastructure IaaC attempt to fully automate the build of my home infrastructure.

Usage:

```shell
smartthingslist.py [-h] --location LOCATION --key KEY --devicename DEVICENAME
```

--location: The location name of the Smartthings location
--key: Smartthings API key
--devicename: (part of) the name of the device to find

Output is a json formatted list of device labels and their ID's.
