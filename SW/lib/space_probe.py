# Platform specific libraty for mini satelite (SATEA) project
from machine import Pin, ADC
import time

class StatusLight:
    def __init__(self):
        self.led = Pin("LED", Pin.OUT)
        for i in range(4):
            self.led.toggle()
            time.sleep(0.1)
        self.led.off()
    def on(self):
        self.led.on()
    def off(self):
        self.led.off()
    def toggle(self):
        self.led.value(not self.led.value())
    
class Battery:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity # mAh

    def voltage(self):
        adc = ADC(28)
        return adc.read_u16() * 3.3 / 32767 # 12-bit ADC to 16 bit but connected to 0.5 voltage divider
    def percentage(self):
        # 3,6V is 0% and 4,2V is 100%
        return (self.voltage() > 3.6) * (self.voltage() - 3.6) / (4.2 - 3.6) * 100
    def capacity(self):
         # 3,6V is 0% and 4,2V is 100% with 360mAh battery
        return (self.voltage() > 3.6) * (self.voltage() - 3.6) / (4.2 - 3.6) * self.battery_capacity
    
class InternalSensors:
    def __init__(self):
        self.temp_sensor = ADC(4)
        self.vsys_voltage = ADC(3)
    def sys_temperature(self):
        return 27 - (self.temp_sensor.read_u16() * 3.3 / 65535 - 0.706) / 0.001721
    def sys_voltage(self):
        return self.vsys_voltage.read_u16() * 3.3 * 3 / 65535 # 0.33 voltage divider
    
class Pins:
    # Pin definitions
    PA0: int = 8
    PA1: int = 9
    PA2: int = 14
    PA3: int = 15
    PA4: int = 26
    PA5: int = 6
    PA6: int = 7
    PA7: int = 1

    PB0: int = 16
    PB1: int = 17
    PB2: int = 18
    PB3: int = 19
    PB4: int = 27
    PB5: int = 10
    PB6: int = 11
    PB7: int = 12

    ADC0: int = 0
    ADC1: int = 1

    def __init__(self):
        pass