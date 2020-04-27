import RPi.GPIO as GPIO 

class HeatingElementController:

    POWER_CONTROL_PIN = 0

    def __init__(self, control_pin):
        
        self.POWER_CONTROL_PIN = control_pin

        GPIO.cleanup()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.POWER_CONTROL_PIN, GPIO.OUT)

    def power_on(self):
        print("Heating Element ON")
        GPIO.output(self.POWER_CONTROL_PIN, GPIO.HIGH) 

    def power_off(self):
        print("Heating Element OFF")
        GPIO.output(self.POWER_CONTROL_PIN, GPIO.LOW) 
