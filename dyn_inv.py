#!/usr/bin/env python3

import ipaddress
import json

def generate_inventory(subnets):
    inventory = {"all": {"hosts": []}}

    for subnet in subnets:
        network = ipaddress.ip_network(subnet)
        for host in network.hosts():
            inventory["all"]["hosts"].append(str(host))

    return inventory

def main():
    # List of IP subnets and ranges
    subnets = [
        "192.168.1.0/24",
        "10.0.0.0/16",
        "172.16.0.0/20"
        # Add more subnets here if needed
    ]

    inventory = generate_inventory(subnets)
    print(json.dumps(inventory, indent=4))

if __name__ == "__main__":
    main()
