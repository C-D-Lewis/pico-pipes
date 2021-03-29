from utime import ticks_us, ticks_diff

# Timer to handle number of ms since program start
class Timer:
  def __init__(self):
    self.ticks_start = ticks_us()
    self.time_now_ms = 0

  # Every program loop
  def tick(self):
    if (ticks_diff(ticks_us(), self.ticks_start) > 1000):
      self.time_now_ms += 1
      self.ticks_start = ticks_us()

  # Get milliseconds passed
  def get_ms_now(self):
    return self.time_now_ms

  # Rest the timer
  def reset(self):
    self.time_now_ms = 0