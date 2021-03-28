import gc
print("initial mem_free: {}".format(gc.mem_free()))

from machine import Pin
import motor
import timer
gc.collect()
print("post imports gc mem_free: {}".format(gc.mem_free()))

INPUT_PATH = './midi.csv'

# Event class handling a row from the build table
class Event:
  def __init__(self, row):
    self.track = int(row[0])
    self.is_on = int(row[1]) == 1
    self.pitch = int(row[2])
    self.on_at = float(row[3])
    self.off_at = float(row[4])

  def __str__(self):
    return "track: {0} is_on: {1} pitch: {2} on_at: {3} off_at: {4}".format(self.track, self.is_on, self.pitch, self.on_at, self.off_at)

motor_0 = motor.Motor(2)
motor_1 = motor.Motor(3)
timer = timer.Timer()

# Assign next event to a motor that isn't doing anything
def assign_event(event):
  if not motor_0.is_on:
    print('0 {}'.format(event))
    motor_0.update(event)
  elif not motor_1.is_on:
    print('1 {}'.format(event))
    motor_1.update(event)
  else:
    print('X {}'.format(event))

# Program loop
def main():
  print("main start mem_free: {}".format(gc.mem_free()))

  # Load CSV file line by line
  with open(INPUT_PATH, 'r') as file:
    # Skip CSV headers
    file.readline()

    # Pre-load first note
    next_event = Event(file.readline().rstrip('\n').split(','))

    while True:
      timer.tick()
      motor_0.tick()
      motor_1.tick()

      # Time for next note?
      if timer.get_ms_now() > (next_event.on_at * 1000):
        # print(str(next_event))

        # Set track on appropriate motor
        if next_event.track == 0:
          motor_0.update(next_event)
        elif next_event.track == 1:
          motor_1.update(next_event)

        # Or find a motor not doing anything
        # assign_event(next_event)

        # Load next row
        next_row = file.readline()
        if not next_row:
          print('fin')
          return

        next_event = Event(next_row.rstrip('\n').split(','))

main()
