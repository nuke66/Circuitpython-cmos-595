""" 
CircuitPython example hooking up CMOS 74HC595 SIPO to give you 8 digital outputs.  You can daisy
chain multiple units to give you move outputs.

In this case I used an Adafruit ItsyBitsy M4 but your more likely to use it on a 
board with limited pins like the Trinket M0

cmos 595         pin   Itsybitsy M4
----------------+-----+------------
serial in         ?      D?
clock             ?      D?
latch             ?      D?

"""

import time
import board
import digitalio
import simpleio

# set up clock, data, and latch pins
clk = digitalio.DigitalInOut(board.D3)
clk.direction = digitalio.Direction.OUTPUT
data = digitalio.DigitalInOut(board.D2)
data.direction = digitalio.Direction.INPUT
latch = digitalio.DigitalInOut(board.D0)
latch.direction = digitalio.Direction.OUTPUT

# insert a small pause after keypress
def qpause():
    time.sleep(0.2)

while True:
    latch.value = False
    #rs = not(rs)
    #rs= simpleio.shift_in(data, clk) 
    #print("output: {0:#010b} {0}".format(rs),end="")
    latch.value = True

    time.sleep(0.05)