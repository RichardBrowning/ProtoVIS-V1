import struct
import smbus
import sys

def readVoltage(bus):

	"This function returns as float the voltage from the Raspi UPS Hat via the provided SMBus object"
	address = 0x36
	read = bus.read_word_data(address, 2)
	swapped = struct.unpack("<H", struct.pack(">H", read))[0]
	voltage = swapped * 78.125 /1000000
	return voltage


def readCapacity(bus):
	"This function returns as a float the remaining capacity of the battery connected to the Raspi UPS Hat via the provided SMBus object"
	address = 0x36
	read = bus.read_word_data(address, 4)
	swapped = struct.unpack("<H", struct.pack(">H", read))[0]
	capacity = swapped/256
	return capacity


bus = smbus.SMBus(1)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

print ("Voltage:%5.2fV" % readVoltage(bus))

print ("Battery:%5i%%" % readCapacity(bus))




# draw battery

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
