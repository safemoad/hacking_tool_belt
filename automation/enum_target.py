# Import required modules
import re

# System defined variables
RHOST = ""

# Get and store IP address from prompt
def get_RHOST():
  global RHOST
  while True:
        target_response = input("Enter the target IP address (e.g., 192.168.1.1 or example.com): ")

        # Basic validation for IP address or hostname format
        ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        hostname_pattern = re.compile(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        if ip_pattern.match(target_response) or hostname_pattern.match(target_response):
            RHOST = target_response
            print(f"Target '{RHOST}' acquired!")
            break
        else:
            print("Invalid IP address or hostname format. Please try again.")

# NMAP Target
def nmap_target():
      print(f"Initiating NMAP scan on: '{RHOST}'")
  
# Main
if __name__ == "__main__":
  get_RHOST()
  nmap_target()
