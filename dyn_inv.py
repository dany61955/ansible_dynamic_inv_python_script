#!/usr/bin/env python

import sys

# Define your IP subnets and ranges here
subnets_and_ranges = [
    "192.168.1.0/24",
    "10.0.0.0/8"
]

# Generate inventory dynamically
inventory = {
    "all": {
        "hosts": []
    }
}

for subnet_or_range in subnets_and_ranges:
    # Logic to generate hosts within the subnet or range
    # You can use IP address manipulation libraries like ipaddress in Python
    # For simplicity, we'll just add the subnet or range itself
    inventory["all"]["hosts"].append(subnet_or_range)

# Output the inventory as JSON
print(json.dumps(inventory))
