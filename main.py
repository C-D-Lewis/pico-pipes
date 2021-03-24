from machine import Pin
import utime

class Motor:
  def __init__(self, gpio_step, gpio_dir):
    # Static state
    self.is_on = False
    self.last_step_us = utime.ticks_us()
    self.pin_step = Pin(gpio_step, Pin.OUT)
    self.pin_dir = Pin(gpio_dir, Pin.OUT)

    # Hardware init
    self.pin_dir.low()
    self.pin_step.low()

    # TODO: Calculate base state
    self.set_pitch(44)

  def set_pitch(self, pitch):
    self.pitch = pitch
    self.delay_us = 1000

  def update(self):
    now = utime.ticks_us()
    if (now - self.last_step_us) > self.delay_us:
      self.last_step_us = now
      # print('step')

      self.pin_step.high()
      utime.sleep_us(10)
      self.pin_step.low()

motor_1 = Motor(2, 3)

timeline = [
  { 'at': 1, 'pitch': 44 },
]

# Program loop
def loop():
  playhead = utime.ticks_us()

  while True:
    motor_1.update()

loop()
