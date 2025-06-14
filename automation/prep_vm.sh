#! /usr/bin/bash

# Update VM and Packages
read -n 1 -p 'Step 1 of 3: Run APT Update/Upgrade on this machine? [Y/n] ' response
  if [ "$response" != "Y" ] 
    then 
      echo ''
      echo 'Step 1 of 3: Skipping APT Update/Upgrade '
    fi
  if [ "$response" == "Y" ] 
    then
      echo 'Step 1 of 3: Updating and upgrading VM, please wait... ' && yes | sudo apt update && yes | sudo apt upgrade
    fi

# Update Searchsploit Database
echo 'Step 2 of 3: Updating Searchsploit database, please wait... '
searchsploit -u #> /dev/null 2>&1

# Update Locate Database
echo 'Step 3 of 3: Updating Locate database, please wait... '
sudo updatedb > /dev/null 2>&1
