import mouse
import keyboard as kb

class AutoFisher():
  hookID = None

  isPressed = False
  toggleKey = 'ctrl+f'

  def __init__(self):
    self.start()

  def start(self):
    self.hookID = kb.add_hotkey(self.toggleKey, self.toggle)

  def stop(self):
    kb.remove_hotkey(self.hookID)

  def toggle(self):
    if (self.isPressed):
      mouse.release(button='right')
      self.isPressed = False
      print('@autoFisher: mouse2 released')
    else:
      mouse.press(button='right')
      self.isPressed = True
      print('@autoFisher: mouse2 pressed')
