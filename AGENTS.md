# AGENTS.md

## Project

Raspberry Pi Pico experimentation repo. Mix of MicroPython and potentially C/C++ SDK projects.

## Structure

- `projects/` — individual experiments, each in its own folder
- `lib/` — shared MicroPython modules
- `docs/` — notes, datasheets, references

## Conventions

- MicroPython is the default language unless a project explicitly uses the C SDK
- Each project folder should be self-contained (own README if non-trivial)
- Pin assignments go in comments or constants at the top of each script
- Target board: Raspberry Pi Pico (RP2040) unless noted otherwise

## Hardware Context

When writing code for the Pico, remember:
- GPIO pins are 0-28 (GP0-GP28)
- Built-in LED is on GPIO 25 (Pico) or controlled via CYW43 on Pico W
- ADC channels: GP26 (ADC0), GP27 (ADC1), GP28 (ADC2), plus internal temp sensor on ADC4
- I2C default: I2C0 on GP0 (SDA) / GP1 (SCL), I2C1 on GP2 (SDA) / GP3 (SCL)
- SPI default: SPI0 on GP16-GP19, SPI1 on GP10-GP13
- UART default: UART0 on GP0 (TX) / GP1 (RX), UART1 on GP4 (TX) / GP5 (RX)
