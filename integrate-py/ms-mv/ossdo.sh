#!/bin/bash
while true;
do
    osascript -e 'tell application "Google Chrome" to reload (tabs of window 1 whose URL contains "google.ca")'
    sleep 10
    echo "Reloaded"
done

