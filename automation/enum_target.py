# Import required modules
import re
import os
import sys
import subprocess

# Global variables defined by prompts
target = None

# Get and store IP address from prompt
def get_target_ip():
  global target
  while True;
        target_response = input("Enter the target IP address (e.g., 192.168.1.1 or example.com): ")

        # Basic validation for IP address or hostname format
        ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        hostname_pattern = re.compile(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        if ip_pattern.match(target_ip) or hostname_pattern.match(target_ip):
            target = target_response
            print(f"\nIP address '{target}' has been stored globally.")
            break
        else:
            print("Invalid IP address or hostname format. Please try again.")

# Print current target
def print():
  print("Your current nmap target is " + target)

# Main
if __name__ == "__main__":
  print()
