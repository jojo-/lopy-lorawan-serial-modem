# A Simple Lora Serial Modem
#
# Version 0.1
#
# Note: To register the LoPy on TTI, see
# - https://docs.pycom.io/gettingstarted/registration/lora/ttn/
# - https://docs.pycom.io/tutorials/networks/lora/lorawan-otaa/
#
# Authors: J. Barthelemy

from EasyLoraConnect import EasyLoraConnect
from network import LoRa
from machine import UART
import struct
import pycom
import machine
import os

try:
    print("Connecting to LoRa")    
    pycom.rgbled(0x7f0000) # red
    lora = EasyLoraConnect()    
    pycom.rgbled(0x007f00) # green
    print("Connected")
    
    uart = UART(1, 115200) # to change with the correct pin numbers!
    uart.init(115200, bits=8, parity=None, stop=1)
    os.dupterm(None)
    
    uart.readline()
    while True:
        payload = uart.readline()
        if payload is not None:
            pycom.rgbled(0x7f7f00) # yellow
            lora.send(payload)    
            pycom.rgbled(0x007f00) # green

except Exception as e:
    print("Error...")
    print(e)
    print("Resetting the board...")
    machine.reset()
