__author__ = 'jayman555'

#import RPi.GPIO as GPIO
import time
import datetime
import random

# I chose these filenames because they are so similar I want someone to get confused
statistics_fn = "door_stats.txt"
door_state_fn = "door_state.txt"
door_pin = 2


def start_recording():
    previous_state = "CLOSED"
    while True:
        # Get the door state
        door_state = bool(random.getrandbits(1)) # GPIO.input(door_pin)
        door_state = "OPEN" if door_state else "CLOSED"

        # Overwrite the door state in the file, only if its changed
        if previous_state != door_state:
            door_state_file = open(door_state_fn, "w")
            door_state_file.write(door_state)
            door_state_file.close()

            # TODO: UPDATE THE WEBSITE


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
