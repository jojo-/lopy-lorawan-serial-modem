import config
import time
import socket
import machine
import binascii
import ubinascii
from network import LoRa

class EasyLoraConnect(object):
    '''A simplistic class to connect and transmit data over LoRaWAN'''

    def __init__(self):
        '''Constructor'''
        self.lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.AS923, tx_retries=config.N_TX, device_class=LoRa.CLASS_A)

        lora = LoRa()
        print("DevEUI: %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))

        self._join_lora()

    def _join_lora(self, force=False):
        '''Joining TTI'''        

        counter = 0

        if not self.lora.has_joined() or force:

            # create an OTA authentication params
            app_eui = binascii.unhexlify(config.APP_EUI.replace(' ',''))
            app_key = binascii.unhexlify(config.APP_KEY.replace(' ',''))

            # join a network using OTAA if not previously done
            self.lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)            

            # wait until the module has joined the network
            while not self.lora.has_joined():
                time.sleep(2.5)
                counter = counter + 1
                if counter >= config.MAX_TRY:
                    machine.reset()            

    def send(self, payload):
        '''Sending data over LoraWan'''

        # create a LoRa socket
        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

        # set the LoRaWAN data rate
        s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.DATA_RATE)

        # make the socket blocking
        s.setblocking(True)

        # send the data
        s.send(payload)

        # closing the socket and saving the LoRa state
        s.close()
