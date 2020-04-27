# Coffee Roaster Project

## Summary
This project contains the microcontroller code to drive a DIY coffee roaster project.  The main goal was to write code that is easy to understand, maintain, and allows for a degree of configurability for sebsequent versions of the coffee roaster as improvements are made.

## File Organization

### roaster.py
This file is the main driver of the microcontroller.  It uses the classes in the utils/ folder to control the components of the coffee roaster.

### config.json
This file contains all of the configuration data for the microcontroller.  It includes GPIO ping specifications as well as timing values and other default settings.

### utiles folder
Each component in the coffee roaster that needs controlled by microcontroller becomes a class within this folder.  Any interaction between the components is controlled via the main roaster.py module so no classes reference each other excepting where there is an additional driver file for specific components like the "LCD Panel"

## References

* [MAX31856 Thermocouple Control](https://learn.adafruit.com/adafruit-max31856-thermocouple-amplifier/python-circuitpython)
* [L298 Motor Controller](https://maker.pro/raspberry-pi/tutorial/how-to-control-a-dc-motor-with-an-l298-controller-and-raspberry-pi)
* [Project Documentation](https://docs.google.com/document/d/1oHwVflQFp4IHgEQ_DVCQFsYltsm2OGass9z3PHarOX0/edit?usp=sharing)
