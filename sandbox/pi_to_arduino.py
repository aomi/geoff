import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

while True:
    writeNumber(1)
    print("Initianting protocol 1")
    time.sleep(1)
    iterations = readNumber()
    
    writeNumber(2)
    print("Initializing protocol 2")
    time.sleep(1)
    remainder = readNumber()
    
    phValue = iterations*256+remainder
    print("Ph is %i", phValue)
