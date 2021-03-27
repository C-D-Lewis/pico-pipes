from machine import Pin
import utime
import pitches

# Motor class allowing non-blocking control
class Motor:
  def __init__(self, gpio_step):
    # Static state
    self.is_on = False
    self.last_step_ticks = utime.ticks_us()
    self.delay_us = 99999

    # Hardware init
    self.pin_step = Pin(gpio_step, Pin.OUT)
    self.pin_step.low()

  # Update the state, pitch, and delay for this motor
  def update(self, event):
    self.is_on = event.is_on
    self.pitch = event.pitch

    if self.is_on == True:
      freq_hz = pitches.get_delay(self.pitch)
      self.delay_us = 1000000 / freq_hz

  # Every main program loop, see if a step is needed
  def tick(self):
    now = utime.ticks_us()

    if (utime.ticks_diff(now, self.last_step_ticks)) > self.delay_us:
      self.last_step_ticks = now

      if self.is_on == True:
        self.pin_step.high()
        self.pin_step.low()
