"""Blink the onboard LED — Pico hello world (MicroPython)."""

from machine import Pin
from time import sleep

# Onboard LED is on GPIO 25 (standard Pico, not Pico W)
LED_PIN = 25

led = Pin(LED_PIN, Pin.OUT)

while True:
    led.toggle()
    sleep(0.5)
