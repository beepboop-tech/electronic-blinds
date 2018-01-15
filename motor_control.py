from time import sleep
import constants
import RPi.GPIO as GPIO



# GPIO setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(constants.relaypin,     GPIO.OUT)
GPIO.setup(constants.up_pin,       GPIO.OUT)
GPIO.setup(constants.up_pin,       GPIO.OUT)
GPIO.setup(constants.recieved_pin, GPIO.IN)

# The last recieved_pin value
# Initally False
current_recieved_pin_value = GPIO.LOW

def set_pin_and_wait(pin_number):
    GPIO.output(pin_number, GPIO.HIGH)

    while(GPIO.input(constants.recieved_pin) is current_recieved_pin_value):
        # Wait for the `recieved_pin` to be toggled
        pass

    GPIO.output(pin_number, GPIO.LOW)
    current_recieved_pin_value = GPIO.input(constants.recieved_pin)

def turn_stepper_on():
    GPIO.output(constants.relaypin, GPIO.HIGH)
    sleep(constants.relay_delay)

def turn_stepper_off():
    GPIO.output(constants.relaypin, GPIO.LOW)
    sleep(constants.relay_delay)

def blinds_up():
    turn_stepper_on()
    set_pin_and_wait(constants.up_pin)
    turn_stepper_off()

def blinds_down():
    turn_stepper_on()
    set_pin_and_wait(constants.down_pin)
    turn_stepper_off()
