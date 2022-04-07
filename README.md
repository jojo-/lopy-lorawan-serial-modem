# lopy-lorawan-serial-modem
Using a LoPy to transmit data via LoRaWAN received over UART 

## Requirements to use with an edge-computer

- LoPy powered via 5V and GND pin
- Data received over UART 1 (pin 4)
- Can work without a development board

## Setup

- Register the LoPy as an end device in a TTI application:
  - https://docs.pycom.io/gettingstarted/registration/lora/ttn/
  - https://docs.pycom.io/tutorials/networks/lora/lorawan-otaa/
- Update the `config.py` file with the TTI credentials: `APP_KEY` and `APP_EUI`
- Upload the code on the LoPy
- When powered on, if 
  - a green light appears: the LoPy is connected
  - a red light appears: the LoPy is not connected
  - an orangee appears: the LoPy is transmitting data

## Using with a Jetson Nano

Connect the LoPy to the Jetson's UART 

### Requirements

- System package: `python3-pip`
- Python 3 package: `serial`

### Configuration

```
sudo usermod -a -G tty $USER
sudo usermod -a -G dialout $USER
reboot
```

```
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
udevadm trigger
```

### Sample code

```
import serial
ser = serial.Serial('/dev/ttyTHS1', 115200, timeout=0.1)
ser.write('coucou'.encode('utf-8'))
```
