import psycopg2
from get_props import prop
import datetime
import logging
from datetime import timedelta
import RPi.GPIO as GPIO

def switch_boiler(state):
    # use P1 header pin numbering convention
    GPIO.setmode(GPIO.BOARD)

    # Set up the GPIO channels - one input and one output
    GPIO.setup(22, GPIO.OUT)
    
    
    GPIO.output(22, GPIO.HIGH)