#!/bin/sh

BASEDIR=$(dirname "$0")

echo "Installing timedAlerts..."

echo "Copying $BASEDIR/check_alerts_loop.py to $HOME/bin/check_alerts_loop"

cp $BASEDIR/check_alerts_loop.py $HOME/bin/check_alerts_loop
chmod 755 $HOME/bin/check_alerts_loop

echo "Copying $BASEDIR/set_timed_alert.py to $HOME/bin/set_timed_alert"

cp $BASEDIR/set_timed_alert.py $HOME/bin/set_timed_alert
chmod 755 $HOME/bin/set_timed_alert

echo "Copying $BASEDIR/talerts_linux.sh to $HOME/bin/talerts"

cp $BASEDIR/talerts_linux.sh $HOME/bin/talerts
chmod 755 $HOME/bin/talerts

echo "Installed!"
echo ""
echo "Usage:"
echo "    talerts loop|add options"
echo ""
echo 'write into "terminal talerts loop &" to start alerts loop on login'
