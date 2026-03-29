"""Blink the onboard LED in Morse code — A-Z then 0-9, looping."""

from machine import Pin
from time import sleep, ticks_ms, ticks_diff
import rp2

LED_PIN = 25

# Timing (seconds)
DOT = 0.15
DASH = 0.45
ELEMENT_GAP = 0.15   # between dots/dashes within a character
CHAR_GAP = 2.0       # pause between characters

MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
}

SEQUENCE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

led = Pin(LED_PIN, Pin.OUT)


def bootsel_pressed():
    return rp2.bootsel_button() == 1


def sleep_or_reset(seconds):
    """Sleep for the given duration, but return True immediately if BOOTSEL is pressed."""
    start = ticks_ms()
    while ticks_diff(ticks_ms(), start) < seconds * 1000:
        if bootsel_pressed():
            led.value(0)
            return True
        sleep(0.01)
    return False


def startup_blink():
    led.value(1)
    sleep(1.0)
    led.value(0)
    sleep(1.0)


while True:
    startup_blink()

    reset = False
    for char in SEQUENCE:
        if reset:
            break
        pattern = MORSE[char]
        for i, symbol in enumerate(pattern):
            led.value(1)
            if sleep_or_reset(DASH if symbol == "-" else DOT):
                reset = True
                break
            led.value(0)
            if i < len(pattern) - 1:
                if sleep_or_reset(ELEMENT_GAP):
                    reset = True
                    break
        if not reset:
            if sleep_or_reset(CHAR_GAP):
                reset = True
