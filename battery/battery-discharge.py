import struct
import smbus
import sys

state_charge = (3.622, 3.832, 4.043, 4.182, 4.21)
state_discharge = (4.15, 3.74751, 3.501, 3.35, 2.756)
state_charging = False;
v_current = 0;
v_old = 0;
capacity = 0;

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

v_old = readVoltage(bus)
v_current = v_old

if (v_current > state_discharge[0]):
	capacity = 100
elif ((v_current < state_discharge[0]) and (v_current >= state_discharge[1])):
	capacity = (state_discharge[0] - v_current) /((state_discharge[0] - state_discharge[1]) / 33) + 75
elif ((v_current < state_discharge[1]) and (v_current >= state_discharge[2])):
	capacity = (state_discharge[1] - v_current) / ((state_discharge[1] - state_discharge[2]) / 33) + 50
elif ((v_current < state_discharge[2]) and (v_current >= state_discharge[3])):
	capacity = (state_discharge[2] - v_current) / ((state_discharge[2] - state_discharge[3]) / 25) + 25
elif ((v_current < state_discharge[3]) and (v_current >= state_discharge[4])):
	capacity = (state_discharge[3] - v_current) / ((state_discharge[3] - state_discharge[4]) / 25)
else:
	capacity = 0

print ("Voltage:%5.2fV" % readVoltage(bus))
print ("Battery:%5i%%" % capacity)

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
