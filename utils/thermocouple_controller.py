class ThermocoupleController:

    CONTROL_PIN = 0

    def __init__ (self, control_pin):
        self.CONTROL_PIN = control_pin

    def read_temp_f(self):
        return self.read_temp_c() * (9/5) + 32

    def read_temp_c(self):
        return 200
