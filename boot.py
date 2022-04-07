# Lora Serial Modem
#
# Boot script

from network import WLAN
import pycom

# deactivate wifi
if pycom.wifi_on_boot:
    wlan = WLAN()
    wlan.deinit()
    pycom.wifi_on_boot(False)

# disabling the heartbeat
pycom.heartbeat(False)
