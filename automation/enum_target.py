# Import required modules
import re
import subprocess
from termcolor import colored

# User defined variables
nmap_options = "-Pn -p- -sV -sC -oA"
ffuf_options = "-ic -ac -c"
directory_wordlist = "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt"
subdomain_wordlist = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt"

# System defined variables
RHOST = ""

# Create directory for enumeration output
def make_dir():
    process = subprocess.run([f"mkdir {RHOST}"], shell=True, capture_output=True, text=True)
    print(colored((process.stderr), "red"))
    
# Get and store target from prompt
def get_RHOST():
    global RHOST
    while True:
        response = input("Enter the target IP address (e.g., 192.168.1.1 or example.com):")

        # Basic validation for IP address or hostname format
        ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        hostname_pattern = re.compile(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        if ip_pattern.match(response) or hostname_pattern.match(response):
            RHOST = response
            print(colored(f"Target '{RHOST}' acquired!", "green"))
            break
        else:
            print(colored("Invalid IP address or hostname format. Please try again.", "red"))

# Create directory for enumeration output
def make_dir():
    process = subprocess.run([f"mkdir {RHOST}"], shell=True, capture_output=True, text=True)
    print(colored((process.stderr), "red"))

# NMAP Target
def nmap_target():
    print(colored(f"Initiating NMAP scan on: '{RHOST}', please wait...", "yellow"))
    process = subprocess.run([f"nmap {nmap_options} {RHOST}/{RHOST} {RHOST}"], shell=True)
  
# Main
if __name__ == "__main__":
  get_RHOST()
  make_dir()
  nmap_target()
  print(colored(f"***Target enumeration complete!***\nEnumeration output files saved to the '{RHOST}' directory.", "green"))
