#! /usr/bin/bash

# Update VM
echo 'Step 1 of 3: Updating and upgrading VM, please wait...'
yes | sudo apt update > /dev/null 2>&1 && yes | sudo apt safe-upgrade > /dev/null 2>&1 

# Update Searchsploit
echo 'Step 2 of 3: Updating Searchsploit database, please wait...'
searchsploit -u > /dev/null 2>&1

# Update Locate Database
echo 'Step 3 of 3: Updating Locate database, please wait...'
sudo updatedb
