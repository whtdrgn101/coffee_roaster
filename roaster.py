from utils import RoasterConfig, HeatingElementController, MotorController, ThermocoupleController, DisplayPanelController

def run_roaster():

    print("Loading Config")
    config = RoasterConfig()

    heating = HeatingElementController(config.HEATING_ELEMENT_PIN)
    heating.power_on()
    heating.power_off()

    drive_motor = MotorController("DRIVE", config.MOTOR_FORWARD_PIN, config.MOTOR_REVERSE_PIN)
    drive_motor.drive_motor("r", "h")
    
    blower_motor = MotorController("BLOWER", config.BLOWER_FORWARD_PIN, config.BLOWER_REVERSE_PIN)
    blower_motor.drive_motor("r", "h")

    therm = ThermocoupleController()
    print("Temp: {0}c".format(therm.read_temp_c()))
    print("Temp: {0}f".format(therm.read_temp_f()))

    #This will blow up until the device is actually hooked up
    display = DisplayPanelController(config.LCD_BUS_NUMBER, config.LCD_ADDRESS)


if __name__ == "__main__":
    run_roaster()
