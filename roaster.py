from utils import HeatingElementController, MotorController, ThermocoupleController, DisplayPanelController

HEATING_ELEMENT_CONTROL_PIN = 12
DISPLAY_I2CBUS = 1
DISPLAY_ADDRESS = 0x27


def run_roaster():
    heating = HeatingElementController(HEATING_ELEMENT_CONTROL_PIN)
    heating.power_on()
    heating.power_off()

    motor = MotorController()
    motor.drive_motor("r", "h")

    therm = ThermocoupleController()
    print(therm.read_temp_c())
    print(therm.read_temp_f())

    display = DisplayPanelController(DISPLAY_I2CBUS, DISPLAY_ADDRESS)


if __name__ == "__main__":
    run_roaster()
