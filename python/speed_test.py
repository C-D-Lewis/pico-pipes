import timer
import motor

motor_0 = motor.Motor(2, 3)
timer = timer.Timer()

# Program loop
def test_pitch(pitch):
  motor_0.update(True, pitch)

  while True:
    timer.tick()
    motor_0.tick()

    if timer.get_ms_now() > 2000:
      return
