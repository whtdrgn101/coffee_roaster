from .I2C_LCD_driver import lcd

class DisplayPanelController:

    # LCD Address
    I2CBUS = 0
    ADDRESS = 0x27
    mylcd = None

    def __init__(self, address, i2cbus):
        self.ADDRESS = address
        self.I2CBUS = i2cbus
        self.mylcd = lcd()

    def display_string(self, display):
        self.clear_screen()
        print(display)

    def clear_screen(self):
        print("## CLEARING SCREEN ##")
