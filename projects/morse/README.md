# Morse Code Blinker

Blinks the onboard LED through the alphabet (A-Z) and digits (0-9) in Morse code, looping forever.

## Usage

Upload `main.py` to the Pico root. On boot:
1. 1-second LED blink (startup indicator)
2. 1-second pause
3. Morse sequence begins

Press BOOTSEL to restart from the beginning at any time.

## Future iterations

- Piezo buzzer to play dit/dah tones alongside the LED
- Display to show the current character being blinked (OLED, segmented, or LCD — TBD)
