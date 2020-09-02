from utils import RoasterConfig, ButtonController, ThermocoupleController, DisplayPanelController, RelayController, MotorController
import RPi.GPIO as GPIO
import time

class RoastMaster:

    RUNNING = False 
    was_running = False
    config = None 
    start_button = None
    stop_button = None
    heating = None
    drive_motor = None
    therm = None
    show_idle = True

    def __init__(self, config_file_loc):
        
        # Bring up roaster components
        print("Loading Config")
        self.config = RoasterConfig(config_file_loc)

        #This will blow up until the device is actually hooked up
        self.display = DisplayPanelController(self.config.LCD_ADDRESS, self.config.LCD_BUS_NUMBER)

        # Setup Roaster Components
        self.start_button = ButtonController(self.config.START_BUTTON_PIN, self.handle_start_press)
        self.stop_button = ButtonController(self.config.STOP_BUTTON_PIN, self.handle_stop_press)
        self.heating = RelayController(self.config.HEATING_ELEMENT_PIN)
        self.drive_motor = MotorController("drive_motor", self.config.MOTOR_FORWARD_PIN, self.config.MOTOR_REVERSE_PIN, self.config.MOTOR_PWM_PIN, self.config.MOTOR_SPEED)
        self.blower_motor = RelayController(self.config.BLOWER_RELAY_PIN)
        self.therm = ThermocoupleController()

    def handle_stop_press(self):
        self.display.show("Stopped")
        self.RUNNING = False

    def handle_start_press(self):
        self.display.show("Initializing")
        self.RUNNING = True 
        self.show_idle = True
   
    # Colby's Coolness Sequence TBD
    def cool_down(self):
        self.heating.power_off()
        for i in range(1, int(self.config.COOL_TIME_SEC)):
            self.show_status("Cooling Down...")
            time.sleep(1)
        
        self.drive_motor.stop_motor()
        self.blower_motor.power_off()


    def show_status(self, message):
        self.display.show(message[0:16],
                "T:{0:.1f}f H:{1:d} M:{2:d}".format(self.therm.read_temp_f(), self.heating.IS_ON, self.drive_motor.IS_MOVING) 
        )
    def run_roaster(self):

        try:


            while True:

                if self.RUNNING == True:
                    
                    self.was_running = True

                    # TEMP & HEATING STATE
                    temp = self.therm.read_temp_f()

                    if temp > self.config.ROAST_TEMP and self.heating.IS_ON == True:
                        self.heating.power_off()
                    elif temp < self.config.ROAST_TEMP and self.heating.IS_ON == False:
                        self.heating.power_on()

                    # MOTOR STATE
                    if self.drive_motor.IS_MOVING == False:
                        self.drive_motor.drive_motor()
                    if self.blower_motor.IS_ON == False:
                        self.blower_motor.power_on()

                    # Display Status
                    self.show_status("Running...")

                elif self.RUNNING == False and self.was_running == True:
                    self.was_running = False
                    self.cool_down()
                    self.show_idle = True
                elif self.RUNNING == False and self.was_running == False and self.show_idle == True:
                    self.display.show("Press Start Btn")
                    self.show_idle = False


                time.sleep(1)

    
        except KeyboardInterrupt:
            self.show_status("Shutting Down...")
            self.heating.power_off()
            self.drive_motor.stop_motor()
            self.blower_motor.power_off()
            self.display.clear_screen()

        finally:
            self.RUNNING = False

if __name__ == "__main__":
    # Run the main loop for the roaster
    roaster = RoastMaster('/home/pi/coffee_roaster/config.json')
    roaster.run_roaster()
    GPIO.cleanup()
