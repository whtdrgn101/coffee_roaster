from utils import RoasterConfig, HeatingElementController, MotorController, ThermocoupleController, DisplayPanelController
import RPi.GPIO as GPIO
import time

def run_roaster():

    # All GPIO commands will be done by PIN number
    GPIO.setmode(GPIO.BCM)

    # Bring up roaster components
    print("Loading Config")
    config = RoasterConfig()
    heating = HeatingElementController(config.HEATING_ELEMENT_PIN)
    #This will blow up until the device is actually hooked up
    #display = DisplayPanelController(config.LCD_BUS_NUMBER, config.LCD_ADDRESS)
    drive_motor = MotorController("DRIVE", config.MOTOR_FORWARD_PIN, config.MOTOR_REVERSE_PIN)
    blower_motor = MotorController("BLOWER", config.BLOWER_FORWARD_PIN, config.BLOWER_REVERSE_PIN)
    therm = ThermocoupleController()

    try:

        #Drive and blower motor is always on
        drive_motor.drive_motor("r", "h")
        blower_motor.drive_motor("r", "h")

        while True:

            if therm.read_temp_f() > 425:
                heating.power_off()
            else:
                heating.power_on()

            print("Temp: {0}c {1}f".format(therm.read_temp_c(), therm.read_temp_f()))
            time.sleep(1)

    
    except KeyboardInterrupt:
        print("Shutting down")
        heating.power_off()
        drive_motor.stop_motor()
        blower_motor.stop_motor()

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    # Run the main loop for the roaster
    run_roaster()
