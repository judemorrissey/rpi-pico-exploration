/**
 * Blink the onboard LED — Pico hello world (C SDK).
 */

#include "pico/stdlib.h"

/* Onboard LED is on GPIO 25 (standard Pico, not Pico W) */
#define LED_PIN 25

int main(void) {
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    while (1) {
        gpio_put(LED_PIN, 1);
        sleep_ms(500);
        gpio_put(LED_PIN, 0);
        sleep_ms(500);
    }
}
