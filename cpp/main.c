#include "main.h"

const uint MOTOR_1_PIN = 2;
const uint MOTOR_2_PIN = 3;

/**
 * Get frequency for a given MIDI pitch value.
 */
float get_pitch_freq(uint16_t pitch) {
  if (pitch > PITCH_TABLE_SIZE) {
    printf("Pitch not in range: %d\n", pitch);
    return 9999999;
  }

  return pitch_table[pitch];
};

/**
 * Tick motor 1
 */
void motor_1_tick(uint delay_us) {
  gpio_put(MOTOR_1_PIN, 1);
  sleep_us(5);
  gpio_put(MOTOR_1_PIN, 0);

  // TODO - use a timer instead for multi motors
  sleep_us(delay_us);
};

/**
 * Entry point.
 */
int main() {
  // GPIO init
  gpio_init(MOTOR_1_PIN);
  gpio_init(MOTOR_2_PIN);
  gpio_set_dir(MOTOR_1_PIN, GPIO_OUT);
  gpio_set_dir(MOTOR_2_PIN, GPIO_OUT);

  uint freq_hz = get_pitch_freq(70);
  uint delay_us = 1000000 / freq_hz;

  while (true) {
    motor_1_tick(delay_us);
  }
}
