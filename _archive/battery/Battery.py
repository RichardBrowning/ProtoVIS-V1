
    
import struct
import smbus
import sys

state_charge = (3.622, 3.832, 4.043, 4.182, 4.21)
state_discharge = (4.15, 3.74751, 3.501, 3.35, 2.756)

class Battery:
    def __init__(self):
        self.bus = smbus.SMBus(1)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
        self.v_current = readVoltage(bus)
        self.capacity = 0
        self.charging = false
        

    def readVoltage(self):
        #"This function returns as float the voltage from the Raspi UPS Hat via the provided SMBus object"
        address = 0x36
        read = self.bus.read_word_data(address, 2)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        voltage = swapped * 78.125 /1000000
        return voltage


    def readCapacity(self):
        #"This function returns as a float the remaining capacity of the battery connected to the Raspi UPS Hat via the provided SMBus object"
        address = 0x36
        read = self.bus.read_word_data(address, 4)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        capacity = swapped/256
        return capacity

    def getBatteryCapacity(self):
        self.v_current = readVoltage(bus)
        capacity = 0
        if (self.charging):
            if (self.v_current > state_charge[4]):
                capacity = 100
            elif ((self.v_current < state_charge[4]) and (self.v_current >= state_charge[3])):
                capacity = (self.v_current - state_charge[3]) / ((state_charge[4] - state_charge[3]) / 25) + 75
            elif ((self.v_current < state_charge[3]) and (self.v_current >= state_charge[2])):
                capacity = (self.v_current - state_charge[2]) / ((state_charge[3] - state_charge[2]) / 25) + 50
            elif ((self.v_current = readVoltage(bus) < state_charge[2]) and (self.v_current >= state_charge[1])):
                capacity = (self.v_current - state_charge[1]) / ((state_charge[2] - state_charge[1]) / 25) + 25
            elif ((self.v_current = readVoltage(bus) < state_charge[1]) and (self.v_current >= state_charge[0])):
                capacity = (self.v_current - state_charge[0]) / ((state_charge[1] - state_charge[0]) / 25)
            else:
                capacity = 0
        else:
            if (self.v_current > state_discharge[0]):
                capacity = 100
            elif ((self.v_current < state_discharge[0]) and (self.v_current >= state_discharge[1])):
                capacity = (state_discharge[0] - self.v_current) /((state_discharge[0] - state_discharge[1]) / 33) + 75
            elif ((self.v_current < state_discharge[1]) and (self.v_current >= state_discharge[2])):
                capacity = (state_discharge[1] - self.v_current) / ((state_discharge[1] - state_discharge[2]) / 33) + 50
            elif ((self.v_current < state_discharge[2]) and (self.v_current >= state_discharge[3])):
                capacity = (state_discharge[2] - self.v_current) / ((state_discharge[2] - state_discharge[3]) / 25) + 25
            elif ((self.v_current < state_discharge[3]) and (self.v_current >= state_discharge[4])):
                capacity = (state_discharge[3] - self.v_current) / ((state_discharge[3] - state_discharge[4]) / 25)
            else:
                capacity = 0
        return capacity


    def printCapacity(self):
        print ("Voltage:%5.2fV" % self.readVoltage(bus))
        print ("Battery:%5i%%" % self.capacity)
        # draw battery 
        # n -> 
        n = int(round(readCapacity(bus) / 10));
        print ("----------- ")
        sys.stdout.write('|')
        for i in range(0,n):
            sys.stdout.write('#')
        for i in range(0,10-n):
            sys.stdout.write(' ')
        sys.stdout.write('|+\n')
        print ("----------- ")
        if readCapacity(bus) == 100:
            print ("Battery FULL")
        if readCapacity(bus) < 20:
            print ("Battery LOW")
