#include "main.h"

const int MOTOR_1_PIN = 2;
const int MOTOR_2_PIN = 3;

////////////////////////////////////////////// Events //////////////////////////////////////////////

struct Event {
  int track;
  int pitch;
  float on_at;
  float off_at;
};

/**
 * Create Event structure.
 */
struct Event event_create(int track, int pitch, float on_at, float off_at) {
  struct Event e;
  e.track = track;
  e.pitch = pitch;
  e.on_at = on_at;
  e.off_at = off_at;

  return e;
};

////////////////////////////////////////////// Pitches /////////////////////////////////////////////

/**
 * Get frequency for a given MIDI pitch value.
 */
float pitch_get_freq(int pitch) {
  if (pitch > PITCH_TABLE_SIZE) {
    printf("Pitch not in range: %d\n", pitch);
    return 9999999;
  }

  return pitch_table[pitch];
};

////////////////////////////////////////////// Motors //////////////////////////////////////////////

struct Motor {
  int pin;
  int is_on;
  uint64_t last_step_us;
  uint64_t step_delay_us;
  uint64_t note_start_us;
  uint64_t note_duration_ms;
};

/**
 * Setup a Motor data structure.
 */
struct Motor motor_create(int pin) {
  struct Motor m;
  m.pin = pin;
  m.is_on = FALSE;
  m.last_step_us = 0;
  m.step_delay_us = 0;
  m.note_start_us = 0;
  m.note_duration_ms = 0;

  // GPIO init
  gpio_init(pin);
  gpio_set_dir(pin, GPIO_OUT);

  return m;
};

/**
 * Update a motor with a new note event.
 */
void motor_set_event(struct Motor *m, struct Event e) {
  m->is_on = TRUE;

  // TODO: Duration control
  uint64_t now_us = to_us_since_boot(get_absolute_time());
  m->note_start_us = now_us;
  m->note_duration_ms = (e.off_at - e.on_at) * 1000;

  int freq_hz = pitch_get_freq(e.pitch);
  m->step_delay_us = 880; //1000000 / freq_hz;
};

/**
 * Tick a motor.
 */
void motor_tick(struct Motor *m) {
  uint64_t now_us = to_us_since_boot(get_absolute_time());

  // Turn off?
  if (now_us - m->note_start_us > (m->note_duration_ms * 1000)) {
    m->is_on = FALSE;
  }

  // Take a step if step delay elapsed
  if (now_us - m->last_step_us > m->step_delay_us) {
    m->last_step_us = now_us;

    if (m->is_on == TRUE) {
      gpio_put(m->pin, 1);
      sleep_us(5);
      gpio_put(m->pin, 0);
    }
  }
};

//////////////////////////////////////////// Main loop /////////////////////////////////////////////

/**
 * Entry point.
 */
int main() {
  struct Motor motor1 = motor_create(MOTOR_1_PIN);

  // TODO: Wait until note start time
  sleep_ms(2000);

  struct Event e = event_create(0, 60, 5.0, 7.0);
  motor_set_event(&motor1, e);

  while (true) {
    motor_tick(&motor1);
  }
};
