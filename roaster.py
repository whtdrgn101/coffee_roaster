from utils import RoasterConfig, HeatingElementController, MotorController, ThermocoupleController, DisplayPanelController

def run_roaster():
    print("Loading Config")
    config = RoasterConfig()

    heating = HeatingElementController(config.HEATING_ELEMENT_PIN)
    heating.power_on()
    heating.power_off()

    motor = MotorController(config.MOTOR_FORWARD_PIN, config.MOTOR_REVERSE_PIN)
    motor.drive_motor("r", "h")

    therm = ThermocoupleController()
    print(therm.read_temp_c())
    print(therm.read_temp_f())

    #This will blow up until the device is actually looked up
    display = DisplayPanelController(config.LCD_BUS_NUMBER, config.LCD_ADDRESS)


if __name__ == "__main__":
    run_roaster()
