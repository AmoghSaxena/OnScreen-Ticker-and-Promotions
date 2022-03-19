#!/bin/bash

### TO FIND THE PATH OF LOCATION
TMPE=$( realpath "$0"  )
cd $(dirname "$TMPE") && cd ../

echo "INSTALLING VIRTUAL ENV"
sudo apt install -y virtualenv pkg-config libcairo2-dev python3-dev gcc libgirepository1.0-dev python3-gi gobject-introspection gir1.2-gtk-3.0
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
	  sudo apt install -y python3-dev gcc libgirepository1.0-dev python3-gi gobject-introspection gir1.2-gtk-3.0
	  echo "INSTALLING PYTHON MODULES"
	  pip install pip --upgrade
	  pip install pygame==2.1.0
	  pip install moviepy==1.0.3
	  pip install colorama==0.4.4
	  pip install PyGObject==3.42.0
	else
	  echo "IMPROPER VERISON OF PYTHON FOUND IN VIRTUAL ENV"
  fi
else
  echo "VIRTUAL ENV NOT ACTIVATED! > EXIT FROM INSTALLATION"
fi

