#!/bin/bash

# Open Notepad with Wine
wine notepad.exe &

# Store the process ID (PID) of the Notepad process
notepad_pid=$!

# Function to type 'x' using xdotool
type_x() {
    while true; do
        xdotool type 'x'
        sleep 1
    done
}

# Run the typing function in the background
type_x &

# Wait for Notepad to finish (you may need to manually close Notepad)
wait $notepad_pid

