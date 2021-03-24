from machine import Pin
import utime

# Relationship between MIDI pitch number (note) and frequency (Hz)
# https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
pitch_lookup = {
  127: 12543.85,  # G9
  126: 11839.82,  # F#9/Gb9
  125: 11175.3,   # F9
  124: 10548.08,  # E9
  123: 9956.06,   # D#9/Eb9
  122: 9397.27,   # D9
  121: 8869.84,   # C#9/Db9
  120: 8372.02,   # C9
  119: 7902.13,   # B8
  118: 7458.62,   # A#8/Bb8
  117: 7040,      # A8
  116: 6644.88,   # G#8/Ab8
  115: 6271.93,   # G8
  114: 5919.91,   # F#8/Gb8
  113: 5587.65,   # F8
  112: 5274.04,   # E8
  111: 4978.03,   # D#8/Eb8
  110: 4698.64,   # D8
  109: 4434.92,   # C#8/Db8
  108: 4186.01,   # C8
  107: 3951.07,   # B7
  106: 3729.31,   # A#7/Bb7
  105: 3520,      # A7
  104: 3322.44,   # G#7/Ab7
  103: 3135.96,   # G7
  102: 2959.96,   # F#7/Gb7
  101: 2793.83,   # F7
  100: 2637.02,   # E7
  99: 2489.02,    # D#7/Eb7
  98: 2349.32,    # D7
  97: 2217.46,    # C#7/Db7
  96: 2093,       # C7
  95: 1975.53,    # B6
  94: 1864.66,    # A#6/Bb6
  93: 1760,       # A6
  92: 1661.22,    # G#6/Ab6
  91: 1567.98,    # G6
  90: 1479.98,    # F#6/Gb6
  89: 1396.91,    # F6
  88: 1318.51,    # E6
  87: 1244.51,    # D#6/Eb6
  86: 1174.66,    # D6
  85: 1108.73,    # C#6/Db6
  84: 1046.5,     # C6
  83: 987.77,     # B5
  82: 932.33,     # A#5/Bb5
  81: 880,        # A5
  80: 830.61,     # G#5/Ab5
  79: 783.99,     # G5
  78: 739.99,     # F#5/Gb5
  77: 698.46,     # F5
  76: 659.26,     # E5
  75: 622.25,     # D#5/Eb5
  74: 587.33,     # D5
  73: 554.37,     # C#5/Db5
  72: 523.25,     # C5
  71: 493.88,     # B4
  70: 466.16,     # A#4/Bb4
  69: 440,        # A4 concert pitch
  68: 415.3,      # G#4/Ab4
  67: 392,        # G4
  66: 369.99,     # F#4/Gb4
  65: 349.23,     # F4
  64: 329.63,     # E4
  63: 311.13,     # D#4/Eb4
  62: 293.66,     # D4
  61: 277.18,     # C#4/Db4
  60: 261.63,     # C4 (middle C)
  59: 246.94,     # B3
  58: 233.08,     # A#3/Bb3
  57: 220,        # A3
  56: 207.65,     # G#3/Ab3
  55: 196,        # G3
  54: 185,        # F#3/Gb3
  53: 174.61,     # F3
  52: 164.81,     # E3
  51: 155.56,     # D#3/Eb3
  50: 146.83,     # D3
  49: 138.59,     # C#3/Db3
  48: 130.81,     # C3
  47: 123.47,     # B2
  46: 116.54,     # A#2/Bb2
  45: 110,        # A2
  44: 103.83,     # G#2/Ab2
  43: 98,         # G2
  42: 92.5,       # F#2/Gb2
  41: 87.31,      # F2
  40: 82.41,      # E2
  39: 77.78,      # D#2/Eb2
  38: 73.42,      # D2
  37: 69.3,       # C#2/Db2
  36: 65.41,      # C2
  35: 61.74,      # B1
  34: 58.27,      # A#1/Bb1
  33: 55,         # A1
  32: 51.91,      # G#1/Ab1
  31: 49,         # G1
  30: 46.25,      # F#1/Gb1
  29: 43.65,      # F1
  28: 41.2,       # E1
  27: 38.89,      # D#1/Eb1
  26: 36.71,      # D1
  25: 34.65,      # C#1/Db1
  24: 32.7,       # C1
  23: 30.87,      # B0
  22: 29.14,      # A#0/Bb0
  21: 27.5,       # A0
}

class Motor:
  def __init__(self, gpio_step, gpio_dir):
    # Static state
    self.is_on = False
    self.last_step_us = utime.ticks_us()
    self.pin_step = Pin(gpio_step, Pin.OUT)
    self.pin_dir = Pin(gpio_dir, Pin.OUT)
    self.update(False, 60)

    # Hardware init
    self.pin_dir.low()
    self.pin_step.low()

  def update(self, is_on, pitch):
    if pitch not in pitch_lookup:
      return

    # Turn 'off'
    self.is_on = is_on
    if not self.is_on:
      self.delay_us = 999999999
      self.pitch = 0
      return

    freq_hz = round(pitch_lookup[pitch])
    self.delay_us = 1000000 / freq_hz
    self.pitch = pitch

  def tick(self):
    now = utime.ticks_us()
    if (now - self.last_step_us) > self.delay_us:
      self.last_step_us = now

      self.pin_step.high()
      utime.sleep_us(5)
      self.pin_step.low()

motor_1 = Motor(2, 3)

timeline = [
  { 'at': 1, 'is_on': True, 'pitch': 60 },
  { 'at': 2, 'is_on': True, 'pitch': 65 },
  { 'at': 3, 'is_on': True, 'pitch': 70 },
  { 'at': 4, 'is_on': False, 'pitch': 0 },
]

# Program loop
def main():
  start_time = utime.time()

  # First note
  event_index = 0
  current_event = timeline[event_index]
  motor_1.update(current_event['is_on'], current_event['pitch'])

  while True:
    motor_1.tick()

    # Time for next note?
    playhead = utime.time()
    if (playhead - start_time ) > current_event['at']:
      event_index += 1
      current_event = timeline[event_index]
      print(current_event)

      # Update motors
      motor_1.update(current_event['is_on'], current_event['pitch'])

main()
