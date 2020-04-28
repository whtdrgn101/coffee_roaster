from utils import RoasterConfig, HeatingElementController, MotorController, ThermocoupleController, DisplayPanelController, ButtonController
import RPi.GPIO as GPIO
import time

def run_roaster():

    RUNNING = True

    def handle_stop_press():
        RUNNING = False

    def handle_start_press():
        RUNNING = True 

    # All GPIO commands will be done by PIN number
    GPIO.setmode(GPIO.BCM)

    #This will blow up until the device is actually hooked up
    #display = DisplayPanelController(config.LCD_BUS_NUMBER, config.LCD_ADDRESS)

    # Bring up roaster components
    print("Loading Config")
    config = RoasterConfig()

    # Setup Roaster Components
    start_button = ButtonController(config.START_BUTTON_PIN, handle_start_press)
    stop_button = ButtonController(config.STOP_BUTTON_PIN, handle_stop_press)
    heating = HeatingElementController(config.HEATING_ELEMENT_PIN)
    drive_motor = MotorController("DRIVE", config.MOTOR_FORWARD_PIN, config.MOTOR_REVERSE_PIN)
    blower_motor = MotorController("BLOWER", config.BLOWER_FORWARD_PIN, config.BLOWER_REVERSE_PIN)
    therm = ThermocoupleController()

    try:

        while True:

            if RUNNING == True:

                # TEMP & HEATING STATE
                temp = therm.read_temp_f()

                if temp > config.ROAST_TEMP and heating.IS_ON == True:
                    heating.power_off()
                elif temp < config.ROAST_TEMP and heating.IS_ON == False:
                    heating.power_on()

                # MOTOR STATE
                if drive_motor.IS_MOVING == False:
                    drive_motor.drive_motor("f")
                if blower_motor.IS_MOVING == False:
                    blower_motor.drive_motor("f")

                # Display Status
                print("Temp: {0}c {1}f".format(therm.read_temp_c(), therm.read_temp_f()))
                time.sleep(1)

            else:
                print("Press Start Button")
                time.sleep(1)

    
    except KeyboardInterrupt:
        print("Shutting down")
        heating.power_off()
        drive_motor.stop_motor()
        blower_motor.stop_motor()

    finally:
        RUNNING = False
        GPIO.cleanup()

if __name__ == "__main__":
    # Run the main loop for the roaster
    RUNNING = False
    run_roaster()
