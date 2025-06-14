#! /usr/bin/bash

# Update VM
echo 'Updating and upgrading VM..."
sudo apt update  > /dev/null 2>&1 && sudo apt safe-upgrade  > /dev/null 2>&1

# Update Searchsploit
echo 'Updating Searchsploit..."
searchsploit -u > /dev/null 2>&1

# Update Locate Database
echo 'Updating Locate database..."
sudo updatedb
