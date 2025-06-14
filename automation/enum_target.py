# Import required modules
import re

# Global variables defined by prompts
ip_address = None

# Get and store IP address from prompt
def get_ip_address();
  global ip_address
  while True;
        target_ip = input("Enter the target IP address: ").strip()

        # Basic validation for IP address or hostname format
        ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        hostname_pattern = re.compile(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        if ip_pattern.match(target_ip) or hostname_pattern.match(target_ip):
            target_ip_global = target_ip # Store the valid IP in the global variable
            print(f"\nIP address '{target_ip_global}' has been stored globally.")
            break
        else:
            print("Invalid IP address or hostname format. Please try again.")
