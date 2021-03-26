import gc
print("initial mem_free: {}".format(gc.mem_free()))

# Order: track, is_on, pitch, at
import build
print("w/build mem_free: {}".format(gc.mem_free()))

from machine import Pin
import motor
import timer
print("all imports mem_free: {}".format(gc.mem_free()))

# Event class handling a row from the build table
class Event:
  def __init__(self, blob):
    self.track = blob[0]
    self.is_on = blob[1]
    self.pitch = blob[2]
    self.at = blob[3]

  def __str__(self):
    return "track: {0} is_on: {1} pitch: {2} at: {3}".format(self.track, self.is_on, self.pitch, self.at)

motor_0 = motor.Motor(2, 3)
timer = timer.Timer()

# Program loop
def main():
  print("main start mem_free: {}".format(gc.mem_free()))

  # First note
  event_index = 0
  current_event = Event(build.timeline[event_index])
  motor_0.update(current_event.is_on, current_event.pitch)

  while True:
    timer.tick()
    motor_0.tick()

    # Time for next note?
    if timer.get_ms_now() > (current_event.at * 1000):
      event_index += 1

      # For now, ignore next event which is the same is_on (i.e: mutiple notes)
      next_event = Event(build.timeline[event_index + 1])
      if current_event.is_on != next_event.is_on:
        current_event = Event(build.timeline[event_index])
      # print(str(current_event))

      # Update motors
      motor_0.update(current_event.is_on, current_event.pitch)

main()
