# Adafruit Shopping List

Weather station starter kit + prototyping supplies.

## Parts

| Part | Price | Link |
|---|---|---|
| Pico 2 W with Header | $8.00 | https://www.adafruit.com/product/6315 |
| BME680 breakout (Stemma QT) | $18.95 | https://www.adafruit.com/product/3660 |
| 2.13" Monochrome e-ink display | $22.50 | https://www.adafruit.com/product/4197 |
| Pico breadboard (Monk Makes) | $4.95 | https://www.adafruit.com/product/5422 |
| Silicone jumper wires (30pc) | $9.95 | https://www.adafruit.com/product/5837 |
| Stemma QT to male headers cable | $0.95 | https://www.adafruit.com/product/4209 |
| Tactile button assortment | ~$2.50 | TBD — look for 6mm tactile pushbuttons |
| Piezo buzzer (PS1240) | $1.50 | https://www.adafruit.com/product/160 |

**Estimated total: ~$70 + shipping**

## Notes

- Pico 2 W "with Header" saves soldering, $1 more than headerless
- BME680 instead of BME280 (out of stock) — adds gas/air quality sensing
- E-ink display uses SPI (5-6 wires), not I2C — still straightforward on breadboard
- Stemma QT cable connects BME680 to breadboard via header pins
- Buttons: basic tactile pushbuttons, wire one leg to a GPIO and the other to GND, use Pin.PULL_UP in code
- Stock checked 2026-03-29, may change
