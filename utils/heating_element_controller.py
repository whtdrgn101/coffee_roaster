class HeatingElementController:

    POWER_CONTROL_PIN = 0

    def __init__(self, control_pin):
        self.POWER_CONTROL_PIN = control_pin

    def power_on(self):
        print("BURN!!!")
        #Do something

    def power_off(self):
        print("CHILL MAN")
        #Do something
