import gc
print("initial mem_free: {}".format(gc.mem_free()))

from machine import Pin
import motor
import timer
gc.collect()
print("post imports gc mem_free: {}".format(gc.mem_free()))

# Event class handling a row from the build table
class Event:
  def __init__(self, row):
    self.track = int(row[0])
    self.is_on = int(row[1]) == 1
    self.pitch = int(row[2])
    self.at = float(row[3])

  def __str__(self):
    return "track: {0} is_on: {1} pitch: {2} at: {3}".format(self.track, self.is_on, self.pitch, self.at)

motor_0 = motor.Motor(2, 3)
timer = timer.Timer()

# Program loop
def main():
  print("main start mem_free: {}".format(gc.mem_free()))

  # Load CSV file line by line
  with open('./timeline.csv', 'r') as file:
    current_row = file.readline().rstrip('\n').split(',')
    next_row = file.readline().rstrip('\n').split(',')

    # First note
    current_event = Event(current_row)
    next_event = Event(next_row)
    motor_0.update(current_event.is_on, current_event.pitch)

    while True:
      timer.tick()
      motor_0.tick()

      # Time for next note?
      if timer.get_ms_now() > (next_event.at * 1000):
        # Update motors
        current_event = next_event
        motor_0.update(current_event.is_on, current_event.pitch)
        print(str(current_event))

        # Load next row
        next_row = file.readline().rstrip('\n').split(',')
        next_event = Event(next_row)

main()
