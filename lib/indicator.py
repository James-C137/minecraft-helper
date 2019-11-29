import mouse

SHAKE_SPEED = 0.05
MOVE_SPEED = 0.05

def show(state):
  if (state):
    true()
  else:
    false()

def shake():
  mouse.move( 50,  0, False, SHAKE_SPEED)
  mouse.move(-100, 0, False, SHAKE_SPEED)
  mouse.move( 100, 0, False, SHAKE_SPEED)
  mouse.move(-50,  0, False, SHAKE_SPEED)

  mouse.move(0,  50,  False, SHAKE_SPEED)
  mouse.move(0, -100, False, SHAKE_SPEED)
  mouse.move(0,  100, False, SHAKE_SPEED)
  mouse.move(0, -50,  False, SHAKE_SPEED)

def true():
  mouse.move(0,  50,  False, MOVE_SPEED)
  mouse.move(0, -100, False, MOVE_SPEED)
  mouse.move(0,  100, False, MOVE_SPEED)
  mouse.move(0, -50,  False, MOVE_SPEED)

def false():
  mouse.move( 50,  0, False, MOVE_SPEED)
  mouse.move(-100, 0, False, MOVE_SPEED)
  mouse.move( 100, 0, False, MOVE_SPEED)
  mouse.move(-50,  0, False, MOVE_SPEED)

def printState(state):
  if (state):
    print('success')
  else:
    print('failed')
