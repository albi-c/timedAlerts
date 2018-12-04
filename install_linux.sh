#!/bin/sh

BASEDIR=$(dirname "$0")

echo "Installing timedAlerts..."

echo "Copying $BASEDIR/check_alerts_loop.py to $HOME/bin/check_alerts_loop"

cp $BASEDIR/check_alerts_loop.py $HOME/bin/check_alerts_loop
chmod 755 $HOME/bin/check_alerts_loop

echo "Copying $BASEDIR/set_timed_alert.py to $HOME/bin/set_timed_alert"

cp $BASEDIR/set_timed_alert.py $HOME/bin/set_timed_alert
chmod 755 $HOME/bin/set_timed_alert

if grep -Fxq "check_alerts_loop" $HOME/.bash_profile; then
	echo "check_alerts_loop already in $HOME/.bash_profile"
else
	echo "Adding check_alerts_loop to $HOME/.bash_profile"
	
	cp $HOME/.bash_profile $HOME/.bash_profile_backup
	echo "check_alerts_loop&" >> $HOME/.bash_profile
fi

echo "Installed!"
