from utils import RoasterConfig, HeatingElementController, MotorController, ButtonController, ThermocoupleController, DisplayPanelController
import RPi.GPIO as GPIO
import time

class RoastMaster:

    RUNNING = False 
    config = None 
    start_button = None
    stop_button = None
    heating = None
    drive_motor = None
    therm = None

    def __init__(self, config_file_loc):
        
        # Bring up roaster components
        print("Loading Config")
        self.config = RoasterConfig(config_file_loc)

        #This will blow up until the device is actually hooked up
        self.display = DisplayPanelController(self.config.LCD_BUS_NUMBER, self.config.LCD_ADDRESS)


        # Setup Roaster Components
        self.start_button = ButtonController(self.config.START_BUTTON_PIN, self.handle_start_press)
        self.stop_button = ButtonController(self.config.STOP_BUTTON_PIN, self.handle_stop_press)
        self.heating = HeatingElementController(self.config.HEATING_ELEMENT_PIN)
        self.drive_motor = MotorController("DRIVE", self.config.MOTOR_FORWARD_PIN, self.config.MOTOR_REVERSE_PIN)
        self.blower_motor = MotorController("BLOWER", self.config.BLOWER_FORWARD_PIN, self.config.BLOWER_REVERSE_PIN)
        self.therm = ThermocoupleController()


    def handle_stop_press(self):
        self.display.show("Stopped")
        self.RUNNING = False

    def handle_start_press(self):
        self.display.show("Starting")
        self.RUNNING = True 

    def run_roaster(self):

        try:

            self.display.show("Press Start Button")

            while True:

                if self.RUNNING == True:

                    # TEMP & HEATING STATE
                    temp = self.therm.read_temp_f()

                    if temp > self.config.ROAST_TEMP and self.heating.IS_ON == True:
                        self.heating.power_off()
                    elif temp < self.config.ROAST_TEMP and self.heating.IS_ON == False:
                        self.heating.power_on()

                    # MOTOR STATE
                    if self.drive_motor.IS_MOVING == False:
                        self.drive_motor.drive_motor("f")
                    if self.blower_motor.IS_MOVING == False:
                        self.blower_motor.drive_motor("f")

                    # Display Status
                    self.display.show("Temp: {0}f".format(temp))

                time.sleep(1)

    
        except KeyboardInterrupt:
            self.display.show("Shutting down")
            self.heating.power_off()
            self.drive_motor.stop_motor()
            self.blower_motor.stop_motor()

        finally:
            self.RUNNING = False

if __name__ == "__main__":
    # Run the main loop for the roaster
    roaster = RoastMaster('/home/pi/coffee_roaster/config.json')
    roaster.run_roaster()
    GPIO.cleanup()
