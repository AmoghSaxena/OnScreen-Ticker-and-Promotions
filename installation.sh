#!/bin/bash

### TO FIND THE PATH OF LOCATION
TMPE=$( realpath "$0"  )
cd $(dirname "$TMPE") && cd ../

echo "INSTALLING VIRTUAL ENV"
sudo apt install -y virtualenv pkg-config python3-dev
INSTALL_LOCATION_VENV=$(pwd)/venv
echo $INSTALL_LOCATION_VENV

sleep 1s

### SETTING UP VIRTUAL ENV
virtualenv -p python3 $INSTALL_LOCATION_VENV

sleep 1s

### ACTIVATING VIRTUAL ENV
echo "SETTING UP VIRTUAL ENV"
source $(pwd)/venv/bin/activate
cd $(dirname "$TMPE")

### CHECKING VIRTUAL ENV
which python | grep -i '/venv/bin/python' &> /dev/null
if [[ $? == 0 ]]; then
   echo "VIRTUAL ENV SET!"
   if [[ $(python -c 'import sys; print(sys.version_info[:][0])') > 2 ]]; then
	  echo "PYTHON VERSION 3+ CONTINUE TO INSTALLING DEPENDECIES"
	  echo "INSTALLING PYTHON MODULES"
	  pip install pip --upgrade
	  pip install pygame==2.1.0
	  pip install moviepy==1.0.3
	else
	  echo "IMPROPER VERISON OF PYTHON FOUND IN VIRTUAL ENV"
  fi
else
  echo "VIRTUAL ENV NOT ACTIVATED! > EXIT FROM INSTALLATION"
fi

