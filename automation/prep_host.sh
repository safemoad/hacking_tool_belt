#! /usr/bin/bash

# Update OS and Packages
read -n 1 -p 'Step 1 of 3: Run APT Update/Upgrade on this machine? [Y/n] ' response
  if [ "$response" == "Y" ] 
    then
      echo ''
      echo 'Step 1 of 3: Updating and upgrading machine, please wait... ' && yes | sudo apt update > /dev/null 2>&1 && yes | sudo apt upgrade > /dev/null 2>&1
    else
      echo ''
      echo '***Skipping APT Update/Upgrade*** '
    fi

# Update Searchsploit Database
echo 'Step 2 of 3: Updating Searchsploit database, please wait... '
searchsploit -u > /dev/null 2>&1

# Update Locate Database
echo 'Step 3 of 3: Updating Locate database, please wait... '
sudo updatedb > /dev/null 2>&1

# Finished
echo '***Host prep complete!*** '
