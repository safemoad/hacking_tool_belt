#! /usr/bin/bash

# Update VM
echo 'Updating and upgrading VM...'
sudo apt update && sudo apt safe-upgrade

# Update Searchsploit
echo 'Updating Searchsploit database...'
searchsploit -u > /dev/null 2>&1

# Update Locate Database
echo 'Updating Locate database...'
sudo updatedb
