import RPi.GPIO as GPIO

class ButtonController:

    def __init__(self, pin, cbk):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=lambda x: cbk(), bouncetime=500)
