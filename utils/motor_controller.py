import RPi.GPIO as GPIO

class MotorController:

    MOTOR_FORWARD = 0
    MOTOR_REVERSE = 0
    my_name = ""
    IS_MOVING = False

    def __init__(self, name, motor_forward_pin, motor_reverse_pin):
    
        self.my_name = name
        self.MOTOR_FORWARD = motor_forward_pin
        self.MOTOR_REVERSE = motor_reverse_pin

        GPIO.setup(self.MOTOR_FORWARD, GPIO.OUT)
        GPIO.setup(self.MOTOR_REVERSE, GPIO.OUT)

    def drive_motor(self, direction='f'):
        
        self.stop_motor()

        if direction == 'f':
            GPIO.output(self.MOTOR_FORWARD, GPIO.HIGH)
        elif direction == 'r':
            GPIO.output(self.MOTOR_REVERSE, GPIO.HIGH)
        
        self.IS_MOVING = True


    def stop_motor(self):
        
        GPIO.output(self.MOTOR_FORWARD, GPIO.LOW) 
        GPIO.output(self.MOTOR_REVERSE, GPIO.LOW) 
        self.IS_MOVING = False
