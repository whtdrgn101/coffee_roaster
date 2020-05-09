from .I2C_LCD_driver import lcd

class DisplayPanelController:

    # LCD Address
    I2CBUS = 0
    ADDRESS = 0x20
    mylcd = None

    def __init__(self, address, i2cbus):
        self.ADDRESS = address
        self.I2CBUS = i2cbus
        self.mylcd = lcd(self.ADDRESS, self.I2CBUS)

    def show(self, line1="", line2=""):
        self.clear_screen()
        self.mylcd.lcd_display_string(line1, 1)
        self.mylcd.lcd_display_string(line2, 2)
        print("{0}\n{1}".format(line1, line2))

    def clear_screen(self):
        self.mylcd.lcd_clear()
