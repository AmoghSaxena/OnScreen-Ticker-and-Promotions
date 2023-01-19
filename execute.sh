#!/bin/bash

export DISPLAY=:0.0
TMPE=$( realpath "$0"  )
cd $(dirname "$TMPE") && cd ../
source $(pwd)/venv/bin/activate

cd $(dirname "$TMPE")
which python

echo "+ SETTING UP VIRTUAL ENV"
python -V

echo "+ SETTING UP CONFIGURATIONS FOR THE PROGRAM..."
eval "python config_init.py"

echo "+ CHECKING STATIC TICKER STATUS"

# FOR CHECING THE SLEEP TIME
TIME_SLEEP=$(cat ticker_setup.json | grep time_interval | awk '{print $2}'|cut -d , -f1)

wmctrl -r :ACTIVE: -b toggle,above


# FOR STATIC TICKER
TICKER_STATIC=$(cat $(dirname "$TMPE")/config.json | grep static_ticker_condition | awk '{print $2}'|cut -d , -f1)

if [[ $TICKER_STATIC = "true" ]]; then
	eval "python ticker_gtk.py &"
fi

echo "+ CHECKING MAIN TICKER STATUS"

# FOR MAIN TICKER
TICKER_MAIN=$(cat $(dirname "$TMPE")/config.json | grep main_ticker_condition | awk '{print $2}'|cut -d , -f1)
if [[ $TICKER_MAIN = "true" ]]; then
  eval "echo + CHECKING OPTIONAL TICKER STATUS"

  # FOR OPTIONAL TICKER
  TICKER_MAIN_OPTIONAL=$(cat $(dirname "$TMPE")/config.json | grep optional_ticker_condition | awk '{print $2}'|cut -d , -f1)
  if [[ $TICKER_MAIN_OPTIONAL = "true" ]]; then
    eval "python ticker_main.py 1 &"
    eval "sleep 0.2s"
#    eval "sleep s"
  fi

  eval "python ticker_main.py 2 &"
fi

# FOR MOVING TICKER
TICKER_MOVING=$(cat ticker_setup.json | grep moving_ticker_condition | awk '{print $2}'|cut -d , -f1)
if [[ $TICKER_MOVING = "true" ]]; then
  eval "sleep 1s"
	eval "python ticker_animated.py &"
fi


sleep $TIME_SLEEP

bash $(dirname "$TMPE")/stopticker