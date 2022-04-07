# Lora Serial Modem Settings

# credentials
APP_EUI = '0000000000000000'                    # JoinEUI in TTI 
APP_KEY = '000000000000000AAAAAAAAAAAAAAAAA'    # AppKey in TTI (Application setting)

# max number of connection attemps to TTN
MAX_TRY = 10

# number of packets to be transmit with the same data  (retries)
# default is 3
N_TX = const(3)

# data rate used to send message via LoRaWAN:
# 1 (slowest - longest range) to 4 (fastest - smallest range)
DATA_RATE = const(2)
