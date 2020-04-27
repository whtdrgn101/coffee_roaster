import json

class RoasterConfig:

    MOTOR_FORWARD_PIN = 0
    MOTOR_REVERSE_PIN = 0
    HEATING_ELEMENT_PIN = 0
    LCD_BUS_NUMBER = 0
    LCD_ADDRESS = 0

    def __init__(self):
        #load file
        with open('config.json') as f:
            config = json.load(f)

        #parse file
        self.MOTOR_FORWARD_PIN = config["MOTOR_FORWARD_PIN"]
        self.MOTOR_REVERSE_PIN = config["MOTOR_REVERSE_PIN"]
        self.HEATING_ELEMENT_PIN = config["HEATING_ELEMENT_PIN"]
        self.LCD_BUS_NUMBER = config["LCD_BUS_NUMBER"]
        self.LCD_ADDRESS = int(config["LCD_ADDRESS"], 0)

