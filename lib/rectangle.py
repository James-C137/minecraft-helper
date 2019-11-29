import mouse

class Rectangle:
  MOUSE_SPEED = 0.1

  def __init__(self, x=0, y=0, w=0, h=0):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
  
  def outline(self):
    top   = self.y
    bot   = self.y + self.h
    left  = self.x
    right = self.x + self.w
    mouse.move(left,  top, duration=0)
    mouse.move(right, top, duration=self.MOUSE_SPEED)
    mouse.move(right, bot, duration=self.MOUSE_SPEED)
    mouse.move(left,  bot, duration=self.MOUSE_SPEED)
    mouse.move(left,  top, duration=self.MOUSE_SPEED)
