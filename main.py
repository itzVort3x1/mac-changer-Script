#!/usr/bin/env python3
import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")

parser.parse_args()

interface = input("interface > ")
mac_address = input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + mac_address)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])