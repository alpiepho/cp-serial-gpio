
Porting the simple golang project ot run a set of LEDs (go-serial-gpio)...mainly because the breadboard is still attached.  Really want to experiment with CircuitPython and Blinka on RaspberryPi.

## Blinka Setup
Setting up Blinka with the following:

https://pypi.org/project/Adafruit-Blinka/


From page:

To install in a virtual environment in your current project:

mkdir project-name && cd project-name<br>
python3 -m venv .env<br>
source .env/bin/activate<br>
pip3 install Adafruit-Blinka<br>

Might need:

https://askubuntu.com/questions/1290037/error-while-installing-rpi-gpio-as-error-command-errored-out-with-exit-status


export CFLAGS=-fcommon<br>
pip3 install RPi.GPIO<br>


## Serial Monitor

- Linux permission problem
- sudo adduser $USER dialout && reboot
- screen /dev/ttyACM0 # linux
- screen /dev/tty.usbmodem144101 # mac
- screen may work better than VS Code Plugin
