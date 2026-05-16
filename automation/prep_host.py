# Import required modules
import subprocess
from termcolor import colored

# Update OS and Packages
def update_apt():
    response = input("Step 1 of 3: Run APT Update/Upgrade on this machine? [Y/n]")
    if response == "Y":
        print(colored("Step 1 of 3: Updating and upgrading machine, please wait...", "yellow"))
        process = subprocess.run(["sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y"], shell=True)
    else:
        print(colored("***Skipping APT Update/Upgrade***", "green"))

# Configure SSH
def configure_ssh():
    response = input("Step 2 of 3: Enable SSH on this machine? [Y/n]")
    if response == "Y": 
        print(colored("Step 2 of 3: Configuring SSH, please wait...", "yellow")) 
        process = subprocess.run(["sudo systemctl enable ssh && sudo systemctl start ssh"], shell=True)
        process = subprocess.run(["sudo ufw enable && sudo ufw allow in on eth0 to any port 22"], shell=True)
    else:        
        print(colored("***Skipping SSH Setup***", "green"))

# Configure Service Ports
def configure_services():
    response = input("Step 3 of 3: Configure Service Ports (http:8000 and nc:9001) on this machine? [Y/n]")
    if response == "Y":
        while True:
            process = subprocess.run(["ip addr | grep 'tun0'"], shell=True, capture_output=True, text=True)
            if process.stdout.strip() == "":
                input("HTB VPN NOT DETECTED: Connect to HTB Network and try again.")
            else:
                break
        print(colored("Step 3 of 3: Configuring Service Ports, please wait...", "yellow"))
        process = subprocess.run(["sudo ufw enable && sudo ufw allow in on tun0 to any port 8000 && sudo ufw allow in on tun0 to any port 9001"], shell=True)
    else:        
        print(colored("***Skipping Port Setup***", "green"))

# Main
if __name__ == "__main__":
    update_apt()
    configure_ssh()
    configure_services()
    print(colored("***Host prep complete!***", "green"))
