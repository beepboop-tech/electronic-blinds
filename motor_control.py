from time import sleep
import constants
import RPI.GPIO as GPIO

# slave setup
a = ArduinoApi()
a.pinMode(constants.M1dirpin, a.OUTPUT)  # M1 direction pin
a.pinMode(constants.M1steppin, a.OUTPUT)  # M1 stepping pin
a.pinMode(constants.M2dirpin, a.OUTPUT)  # M2 direction pin
a.pinMode(constants.M2steppin, a.OUTPUT)  # M2 stepping pin

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(constants.relaypin, GPIO.OUT)


def turn_stepper_on():
    GPIO.output(constants.relaypin, GPIO.HIGH)
    sleep(constants.delayRelay)


def turn_stepper_off():
    GPIO.output(constants.relaypin, GPIO.LOW)
    sleep(constants.delayRelay)


def blinds_up(a):
    turn_stepper_on()
    a.digitalWrite(constants.M1dirpin, a.HIGH)
    a.digitalWrite(constants.M2dirpin, a.HIGH)
    for i in range(0, constants.rotations):
        a.digitalWrite(constants.M1steppin, a.HIGH)
        a.digitalWrite(constants.M2steppin, a.HIGH)
        sleep(constants.delayStep)
        a.digitalWrite(constants.M1steppin, a.LOW)
        a.digitalWrite(constants.M2steppin, a.LOW)
        sleep(2 * constants.delayStep)
    turn_stepper_off()


def blinds_down(a):
    turn_stepper_on()
    a.digitalWrite(constants.M1dirpin, a.LOW)
    a.digitalWrite(constants.M2dirpin, a.LOW)
    for i in range(0, constants.rotations):
        a.digitalWrite(constants.M1steppin, a.HIGH)
        a.digitalWrite(constants.M2steppin, a.HIGH)
        sleep(constants.delayStep)
        a.digitalWrite(constants.M1steppin, a.LOW)
        a.digitalWrite(constants.M2steppin, a.LOW)
        sleep(2 * constants.delayStep)
    turn_stepper_off()
