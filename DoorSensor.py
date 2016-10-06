__author__ = 'jayman555'

#import RPi.GPIO as GPIO
import time
import datetime
import random
import os
import subprocess

# I chose these filenames because they are so similar I want someone to get confused
statistics_fn = "door_stats.txt"
door_state_fn = "door_state.txt"
door_pin = 2


def start_recording():
    previous_state = "closed"
    while True:
        # Get the door state
        door_state = bool(random.getrandbits(1)) # GPIO.input(door_pin)
        door_state = "open" if door_state else "closed"

        # Overwrite the door state in the file, only if its changed
        if previous_state != door_state:
            door_state_file = open(door_state_fn, "w")
            door_state_file.write(door_state)
            door_state_file.close()

            # UPDATE THE WEBSITE
            update_command = "curl -k https://cs.club.anu.edu.au/files/doorstate/set.php\?key\=PHO9nofEfXdUMLnu7ReSoRgpDgOTwgY\&state\={0}".format(door_state)
            # subprocess.call(['curl', '-k', update_command], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            # subprocess.call(['curl', '-k', update_command])
            os.system(update_command)

            # Dump the door state to a file for analysis later
            timestamp = time.time()
            pretty_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y %H:%M:%S")
            statistics_file = open(statistics_fn, "a")
            statistics_file.write(pretty_timestamp + ", " + door_state + "\n")
            statistics_file.close()

        previous_state = door_state

        # Try again later pal
        time.sleep(5.0)

if __name__ == "__main__":
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(2, GPIO.IN)
    start_recording()
