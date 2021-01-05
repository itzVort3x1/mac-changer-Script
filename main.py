#!/usr/bin/env python3
import subprocess

interface = input("interface > ")
mac_address = input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + mac_address)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac_address, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig", shell=True)