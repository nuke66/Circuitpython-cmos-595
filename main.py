""" 
CircuitPython example hooking up CMOS 74HC595 SIPO to give you 8 digital outputs.  You can daisy
chain multiple units to give you move outputs.

In this case I used an Adafruit ItsyBitsy M4 but your more likely to use it on a 
board with limited pins like the Trinket M0

cmos 595     pin   Itsybitsy M4
-----------+-----+------------
serial in    14      D9
latch        12      D7
clock        11      D5

OE           13      Gnd
MR           10      Vcc
"""
import time
import board
import digitalio
import simpleio

# set up clock, data, and latch pins
data = digitalio.DigitalInOut(board.D9)
data.direction = digitalio.Direction.OUTPUT
latch = digitalio.DigitalInOut(board.D7)
latch.direction = digitalio.Direction.OUTPUT
clk = digitalio.DigitalInOut(board.D5)
clk.direction = digitalio.Direction.OUTPUT

ff = 0  # flip flop
while True:
    ff = 1-ff
    if (ff==1):
       byte = 255
    else:
        byte = 0

    # write to 595 chip
    latch.value = False
    simpleio.shift_out(data, clk, byte) 
    print("sending: {0:#010b} {0}".format(byte),end="\n")
    latch.value = True
    time.sleep(0.25)