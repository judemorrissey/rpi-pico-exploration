# rpi-pico-exploration

Experimenting with the Raspberry Pi Pico — learning GPIO, sensors, displays, and whatever else looks fun.

## Hardware

- Raspberry Pi Pico (RP2040)
<!-- Add your specific board variant (Pico W, Pico 2, etc.) and peripherals as you acquire them -->

## Getting Started

### MicroPython

1. Download the latest MicroPython UF2 from [micropython.org/download/RPI_PICO](https://micropython.org/download/RPI_PICO)
2. Hold BOOTSEL while plugging in the Pico — it mounts as a USB drive
3. Drag the `.uf2` file onto the drive — it reboots into MicroPython
4. Connect via serial (e.g. Thonny, `mpremote`, or `screen /dev/tty.usbmodem* 115200`)

### C/C++ SDK

1. Install the [Pico SDK](https://github.com/raspberrypi/pico-sdk) and toolchain (`cmake`, `arm-none-eabi-gcc`)
2. Set `PICO_SDK_PATH` environment variable
3. Each project gets its own `CMakeLists.txt` — see [pico-examples](https://github.com/raspberrypi/pico-examples) for reference

## Project Structure

```
projects/         — individual experiment folders
  blink/          — e.g. your first LED blink
  ...
docs/             — datasheets, pinouts, notes
lib/              — shared MicroPython libraries / modules
```

## Useful Links

- [Pico Datasheet (RP2040)](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)
- [MicroPython Docs](https://docs.micropython.org/en/latest/)
- [Pico SDK Docs](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html)
- [Pico Pinout](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)

## License

[Unlicense](LICENSE) — public domain.
