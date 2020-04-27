import RPi.GPIO as GPIO

class MotorController:

    MOTOR_FORWARD = 0
    MOTOR_REVERSE = 0

    def __init__(self, motor_forward_pin, motor_reverse_pin):
    
        self.MOTOR_FORWARD = motor_forward_pin
        self.MOTOR_REVERSE = motor_reverse_pin

        GPIO.cleanup()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.MOTOR_FORWARD, GPIO.OUT)
        GPIO.setup(self.MOTOR_REVERSE, GPIO.OUT)

    def drive_motor(self, direction='f', speed='m'):
        
        self.stop_motor()

        if direction == 'f':
            print("MOTOR FORWARD");
            GPIO.outout(self.MOTOR_FORWARD, GPIO.HIGH)
        elif direction == 'r':
            print("MOTOR REVERSE");
            GPIO.output(self.MOTOR_REVERSE, GPIO.HIGH)


    def stop_motor(self):
        
        print("MOTOR STOP")
        GPIO.output(self.MOTOR_FORWARD, GPIO.LOW) 
        GPIO.output(self.MOTOR_REVERSE, GPIO.LOW) 
