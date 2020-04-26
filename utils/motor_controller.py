class MotorController:

    MOTOR_CONTROL_PIN = 0

    def __init__(self, control_pin):
        self.MOTOR_CONTROL_PIN = control_pin

    def drive_motor(self, direction='f', speed='m'):
        print("Driving motor {0} at speed {1}".format(direction, speed))
