from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice

class MotorController:

    MOTOR_FORWARD = 0
    MOTOR_REVERSE = 0
    MOTOR_PWM = 0
    MOTOR_SPEED = 0.5
    my_name = ""
    IS_MOVING = False
    my_motor_drive_speed = None
    my_motor_forward = None
    my_motor_reverse = None

    def __init__(self, name, motor_forward_pin, motor_reverse_pin, motor_pwm_pin, motor_speed = 0.5):
    
        self.my_name = name
        self.MOTOR_FORWARD = motor_forward_pin
        self.MOTOR_REVERSE = motor_reverse_pin
        self.MOTOR_PWM = motor_pwm_pin
        self.MOTOR_SPEED = motor_speed

        self.my_motor_drive_speed = PWMOutputDevice(self.MOTOR_PWM, True, 0, 1000)
        self.my_motor_forward = DigitalOutputDevice(self.MOTOR_FORWARD)
        self.my_motor_reverse = DigitalOutputDevice(self.MOTOR_REVERSE)

    def drive_motor(self, direction='f'):
        
        self.stop_motor()

        if direction == 'f':
            self.my_motor_forward.value = True
        elif direction == 'r':
            self.my_motor_reverse.value = True
        
        self.my_motor_drive_speed = self.MOTOR_SPEED
        
        self.IS_MOVING = True


    def stop_motor(self):
        self.my_motor_forward.value = False
        self.my_motor_reverse.value = False
        self.my_motor_drive_speed = 0
        self.IS_MOVING = False
