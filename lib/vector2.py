import mouse

class Vector2:
  MOUSE_SPEED = 0

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def show(self):
    mouse.move(self.x, self.y, duration=self.MOUSE_SPEED)
