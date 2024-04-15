import smbus

# I2C Controller Class
class I2CController:
    def __init__(self, address, bus_number=1):
        self.address = address
        self.bus = smbus.SMBus(bus_number)

    def send_byte(self, data):
        self.bus.write_byte(self.address, data)
        print(f"Sent {data} to I2C address {self.address}")