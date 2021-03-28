from machine import Pin
import utime
import pitches
import timer

# Motor class allowing non-blocking control
class Motor:
  def __init__(self, gpio_step):
    # Static state
    self.is_on = False
    self.last_step_ticks = utime.ticks_us()
    self.step_delay_us = 99999
    self.duration_ms = 0
    self.timer = timer.Timer()

    # Hardware init
    self.pin_step = Pin(gpio_step, Pin.OUT)
    self.pin_step.low()

  # Update the state, pitch, and delay for this motor
  def update(self, event):
    self.is_on = event.is_on
    self.pitch = event.pitch
    self.duration_ms = (event.off_at - event.on_at) * 1000
    self.timer.reset()

    if self.is_on == True:
      freq_hz = pitches.get_delay(self.pitch)
      self.step_delay_us = 1000000 / freq_hz

  # Every main program loop, see if a step is needed
  def tick(self):
    self.timer.tick()

    # Duration elapsed?
    if self.timer.get_ms_now() > self.duration_ms:
      self.is_on = False

    # Take a step
    now = utime.ticks_us()
    if (utime.ticks_diff(now, self.last_step_ticks)) > self.step_delay_us:
      self.last_step_ticks = now

      if self.is_on == True:
        self.pin_step.high()
        self.pin_step.low()
