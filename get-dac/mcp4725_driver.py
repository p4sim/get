import RPi.GPIO as gpio
import time
import smbus


class MCP4725:
    def __init__(self,dynamic_range,address=0x61,verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range



    def set_number(self, number):
        if not isinstance(number,int):
            print ("На вход ЦАП можно подавать только целые числа")

        if not (0<= number <=4095):
            print("Число выходит за разрядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        #if self.verbose:
            #print (f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self,voltage):
        return self.set_number(int(float(voltage)/self.dynamic_range * 4095))
    
    def deinit(self):
        self.bus.close()



if __name__ == "__main__":
    try:
        dac = MCP4725(5.20, 0x61, True)

        while True:
            try:
                a = input()
                dac.set_voltage(a)
            except ValueError:
                print("error")

    finally:
        dac.deinit()

