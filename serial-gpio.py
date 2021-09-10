import time
import board
import digitalio

numbers = [
    board.D17,
    board.D27,
    board.D22,
    board.D23,
    board.D24,
    board.D5,
    board.D25,
    board.D6,
    board.D12,
    board.D13,
]

leds = []


def ledsInit():
    global leds
    leds = []
    for i, num in enumerate(numbers):
        leds.append(digitalio.DigitalInOut(num))
        leds[i].direction = digitalio.Direction.OUTPUT


def ledsSet(value):
    for _, led in enumerate(leds):
        led.value = value


loops = 0
while True:
    print("Initialize All: ", loops)
    ledsInit()
    ledsSet(False)
    time.sleep(0.5)

    for i, led in enumerate(leds):
        led.value = True
        time.sleep(0.5)

    loops = loops + 1

print("Program finished executing")
