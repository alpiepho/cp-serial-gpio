
Porting the simple golang project ot run a set of LEDs (go-serial-gpio)...mainly because the breadboard is still attached.  Really want to experiment with CircuitPython and Blinka on RaspberryPi.

Setting up Blinka with the following:

https://pypi.org/project/Adafruit-Blinka/


From page:

To install in a virtual environment in your current project:

mkdir project-name && cd project-name
python3 -m venv .env
source .env/bin/activate
pip3 install Adafruit-Blinka

Might need:

https://askubuntu.com/questions/1290037/error-while-installing-rpi-gpio-as-error-command-errored-out-with-exit-status


export CFLAGS=-fcommon

pip3 install RPi.GPIO

