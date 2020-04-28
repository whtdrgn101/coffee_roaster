import RPi.GPIO as GPIO

class ButtonController:

    def __init__(self, pin, callback):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=callback, bouncetime=300)
