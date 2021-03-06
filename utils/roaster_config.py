import json

class RoasterConfig:

    MOTOR_FORWARD_PIN = 0
    MOTOR_REVERSE_PIN = 0
    MOTOR_PWM_PIN = 0
    MOTOR_SPEED = 0.5
    BLOWER_RELAY_PIN = 0
    HEATING_ELEMENT_PIN = 0
    START_BUTTON_PIN = 0
    STOP_BUTTON_PIN = 0
    LCD_BUS_NUMBER = 0
    LCD_ADDRESS = 0
    ROAST_TEMP = 0
    COOL_TIME_SEC = 0

    def __init__(self, config_file):
        #load file
        with open(config_file) as f:
            config = json.load(f)

        #parse file
        self.MOTOR_FORWARD_PIN = config["MOTOR_FORWARD_PIN"]
        self.MOTOR_REVERSE_PIN = config["MOTOR_REVERSE_PIN"]
        self.MOTOR_PWM_PIN = config["MOTOR_PWM_PIN"]
        self.MOTOR_SPEED = config["MOTOR_SPEED"]
        self.BLOWER_RELAY_PIN = config["BLOWER_RELAY_PIN"]
        self.HEATING_ELEMENT_PIN = config["HEATING_ELEMENT_PIN"]
        self.START_BUTTON_PIN = config["START_BUTTON_PIN"]
        self.STOP_BUTTON_PIN = config["STOP_BUTTON_PIN"]
        self.LCD_BUS_NUMBER = int(config["LCD_BUS_NUMBER"])
        self.LCD_ADDRESS = int(config["LCD_ADDRESS"], 0)
        self.ROAST_TEMP = float(config["ROAST_TEMP"])
        self.COOL_TIME_SEC = float(config["COOL_TIME_SEC"])

