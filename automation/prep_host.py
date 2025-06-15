# Import required modules
import subprocess
from termcolor import colored

#Update OS and Packages
def update_apt():
    response = input("Step 1 of 3: Run APT Update/Upgrade on this machine? [Y/n]")
    if response == "Y":
        print(colored("Step 1 of 3: Updating and upgrading machine, please wait...", "white"))
        process = subprocess.run(["yes | sudo apt update && yes | sudo apt upgrade"], shell=True, capture_output=True, text=True)
        print(colored((process.stderr), "red"))
    else:
        print(colored("***Skipping APT Update/Upgrade***", "green"))

#Update Searchsploit Database
def update_searchsploit():
    print(colored("Step 2 of 3: Updating Searchsploit database, please wait...", "white"))
    process = subprocess.run(["searchsploit -u"], shell=True, capture_output=True, text=True)
    print(colored((process.stderr), "red"))

# Update Locate Database
def update_locate():
    print(colored("Step 3 of 3: Updating Locate database, please wait...", "white"))
    process = subprocess.run(["sudo updatedb"], shell=True, capture_output=True, text=True)
    print(colored((process.stderr), "red"))

# Main
if __name__ == "__main__":
    update_apt()
    update_searchsploit()
    update_locate()
    print(colored("***Host prep complete!***", "green"))
