import pyautogui as pgui
from typing import Dict, List

from .rectangle import Rectangle
from .utils import lerp
from .vector2 import Vector2

class Inventory:
  bounds:        Rectangle           = None
  keyItems:      Dict[str, Vector2]  = None
  armorSlot:    List[Vector2]       = None
  craftingSlot: List[Vector2]       = None
  outputSlot:    Vector2             = None
  offhandSlot:   Vector2             = None
  storageSlot:   List[List[Vector2]] = None
  hotbarSlot:    List[Vector2]       = None

  def __init__(self):
    self.keyItems = {}

  def setBounds(self):
    left = pgui.locateOnScreen('./img/inventory-left.png', confidence=0.95)
    right = pgui.locateOnScreen('./img/inventory-right.png', confidence=0.95)
    if (not left == None and not right == None):
      x0, y0 = left.left, left.top
      x1, y1 = right.left + right.width, right.top + right.height
      self.bounds = Rectangle(x0, y0, x1-x0, y1-y0)
      return True
    return False
  
  def showBounds(self):
    self.bounds.outline()

  def setSlots(self):
    if (self.bounds == None):
      print('error: bounds not set')
      return
    b = self.bounds
    # set armorSlot
    self.armorSlot = []
    for i in range(4):
      self.armorSlot.append(Vector2(
        b.x + b.w * 0.1,
        lerp(b.y + b.h * 0.1, b.y + b.h * 0.42, i/3)))
    # set craftingSlot
    self.craftingSlot = []
    for i in range(2):
      for j in range(2):
        self.craftingSlot.append(Vector2(
          lerp(b.x + b.h * 0.64, b.x + b.h * 0.75, j/1),
          lerp(b.y + b.h * 0.15, b.y + b.h * 0.265, i/1)))
    # set outputSlot
    self.outputSlot = Vector2(
      b.x + b.w * 0.915,
      b.y + b.h * 0.235)
    # set offhandSlot
    self.offhandSlot = Vector2(
      b.x + b.w * 0.475,
      b.y + b.h * 0.42)
    # set storageSlot
    self.storageSlot = []
    for i in range(3):
      row = []
      for j in range(9):
        row.append(Vector2(
          lerp(b.x + b.w * 0.1, b.x + b.w * 0.91, j/8),
          lerp(b.y + b.h * 0.55, b.y + b.w * 0.725, i/2)))
      self.storageSlot.append(row)
    # set hotbarlot
    self.hotbarSlot = []
    for i in range(9):
      self.hotbarSlot.append(Vector2(
        lerp(b.x + b.w * 0.1, b.x + b.w * 0.91, i/8),
        b.y + b.h * 0.9))

  def findKeyItem(self, name:str):
    filename = './img/' + name + '.png'
    b = self.bounds
    item = pgui.locateCenterOnScreen(filename, region=(b.x, b.y, b.w, b.h))
    if (not item == None):
      self.keyItems[name] = Vector2(item.x, item.y)
      return True
    return False
