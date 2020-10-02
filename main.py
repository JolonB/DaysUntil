from machine import UART, Pin
import time

"""
    A
   ---
F |   | B
  | G |
   ---
E |   | C
  |   |
   ---
    D
"""


# Set up pins
A = Pin(19, mode=Pin.OUT)
B = Pin(22, mode=Pin.OUT)
C = Pin(5, mode=Pin.OUT)
D = Pin(17, mode=Pin.OUT)
E = Pin(16, mode=Pin.OUT)
F = Pin(21, mode=Pin.OUT)
G = Pin(18, mode=Pin.OUT)

segments_led = [A, B, C, D, E, F, G]

# Set all segments to off
A(0)
B(0)
C(0)
D(0)
E(0)
F(0)
G(0)


def hex_bin(hex_code: str):
    return "{0:08b}".format(int(hex_code, 16))


digits = [hex_bin('3F'), hex_bin('06'), hex_bin('5B'), hex_bin(
    '4F'), hex_bin('66'), hex_bin('6D'), hex_bin('7D'), hex_bin('07'), hex_bin('7F'), hex_bin('6F')]

# Initialise some dodgy global variables
current_value = 0
uart = UART(1, 115200, tx=25, rx=2)


def loop():
    global current_value
    if uart.any():
        val = uart.read()
        try:
            val = int(val)
        except ValueError:
            pass
        else:
            current_value = val
    set_display(current_value)
    time.sleep_ms(500)


def set_display(value):
    digit_1 = value % 10
    segments = digits[digit_1]

    for i in range(len(segments_led)):
        segments_led[i](int(segments[-i-1]))


while True:
    loop()
