/**
 * Blink the onboard LED — Pico hello world (C++ SDK).
 */

#include "pico/stdlib.h"

// Onboard LED is on GPIO 25 (standard Pico, not Pico W)
constexpr uint LED_PIN = 25;

int main() {
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    while (true) {
        gpio_put(LED_PIN, true);
        sleep_ms(500);
        gpio_put(LED_PIN, false);
        sleep_ms(500);
    }
}
