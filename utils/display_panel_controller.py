from .I2C_LCD_driver import lcd

class DisplayPanelController:

    # LCD Address
    I2CBUS = 0
    ADDRESS = 0x27
    mylcd = None

    def __init__(self, address, i2cbus):
        self.ADDRESS = address
        self.I2CBUS = i2cbus
        #self.mylcd = lcd()

    def show(self, line1="", line2=""):
        #self.clear_screen()
        print("{0}\n{1}".format(line1, line2))

    def clear_screen(self):
        print("")
