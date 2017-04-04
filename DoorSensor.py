__author__ = 'jayman555 + alex'

import time
import datetime
import os
import subprocess
import serial

# I chose these filenames because they are so similar I want someone to get confused
statistics_fn = "door_stats.txt"
door_state_fn = serial.Serial("/dev/ttyUSB0");
open_state = b'\x01'
closed_state = b'\x00'

def start_recording():
    previous_state = "closed"
    while True:
        serial_val = door_state_fn.read()
        if serial_val == open_state:
            door_state = "open"
        elif serial_val == closed_state:
            door_state = "closed"

        # UPDATE THE WEBSITE
        update_command = "Nope"

        os.system(update_command)

        # Dump the door state to a file for analysis later
        timestamp = time.time()
        pretty_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y %H:%M:%S")
        statistics_file = open(statistics_fn, "a")
        statistics_file.write(pretty_timestamp + ", " + door_state + "\n")
        statistics_file.close()

if __name__ == "__main__":
    start_recording()
