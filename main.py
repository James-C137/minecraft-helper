import time as time
import pyautogui as pgui
import keyboard as kb
import mouse as mouse

class Rectangle:
  def __init__(self, left, top, width=0, height=0):
    self.left = left
    self.top = top
    self.width = width
    self.height = height
  
  def show(self):
    left   = self.left
    right  = self.left + self.width
    top    = self.top
    bottom = self.top + self.height
    pgui.moveTo(left,  top,    0.25, pgui.easeOutQuad, _pause=False)
    pgui.moveTo(right, top,    0.25, pgui.easeOutQuad, _pause=False)
    pgui.moveTo(right, bottom, 0.25, pgui.easeOutQuad, _pause=False)
    pgui.moveTo(left,  bottom, 0.25, pgui.easeOutQuad, _pause=False)
    pgui.moveTo(left,  top,    0.25, pgui.easeOutQuad, _pause=False)
  
  def showCenter(self):
    x, y = self.getCenter()
    pgui.moveTo(x, y, 0.25, pgui.easeOutQuad, _pause=False)

  def getCenter(self):
    x = self.left + self.width / 2
    y = self.top + self.height / 2
    return (x, y)

class Inventory:
  def __init__(self):
    self.location = Rectangle(0, 0)
    self.hotbar   = []
    self.offHand  = Rectangle(0, 0)
    self.items    = {}

  def locate(self):
    left = pgui.locateOnScreen('./img/inventory-left.png', confidence=0.95, grayscale=True)
    right = pgui.locateOnScreen('./img/inventory-right.png', confidence=0.95, grayscale=True)
    if (not left == None and not right == None):
      x0, y0 = left.left, left.top
      x1, y1 = right.left + right.width, right.top + right.height
      self.location = Rectangle(x0, y0, x1-x0, y1-y0)
      self.hotbar = []
      for i in range(9):
        self.hotbar.append(Rectangle(
          self.location.left + self.location.width * (1/18) + self.location.width * (1/10) * i,
          self.location.top + self.location.height * 0.85,
          self.location.width * 0.1,
          self.location.width * 0.1))
      self.offHand = Rectangle(
        self.location.left + self.location.width * 0.425,
        self.location.top + self.location.height * 0.375,
        self.location.width * 0.1,
        self.location.width * 0.1)
      self.indicator()

  def locateItem(self, itemName:str):
    region = (self.location.left, self.location.top, self.location.width, self.location.height)
    item = pgui.locateCenterOnScreen('./img/' + itemName, region=region, confidence=0.95)
    self.items[itemName] = item

  def locateItems(self, itemNames:list):
    for i in itemNames:
      self.locateItem(i)
    self.indicator()

  def showLocation(self):
    self.location.show()
    for i in self.hotbar:
      i.showCenter()
    self.offHand.showCenter()

  def showItem(self, itemName):
    item = self.items[itemName]
    if (item == None):
      return
    pgui.moveTo(item.x, item.y, 0.25, pgui.easeOutQuad, _pause=False)

  def showItems(self):
    for i in self.items.keys():
      self.showItem(i)
  
  def panicButton(self):
    kb.press_and_release('e')
    totem = self.items['totem-of-undying.png']
    time.sleep(0.05)
    mouse.move(totem.x, totem.y)
    time.sleep(0.05)
    mouse.double_click()
    time.sleep(0.05)
    offHandX, offHandY = self.offHand.getCenter()
    mouse.move(offHandX, offHandY)
    time.sleep(0.05)
    mouse.click()
    time.sleep(0.05)
    water = self.items['water-bucket.png']
    mouse.move(water.x, water.y)
    time.sleep(0.05)
    mouse.double_click()
    time.sleep(0.05)
    hotbarX, hotbarY = self.hotbar[0].getCenter()
    mouse.move(hotbarX, hotbarY)
    time.sleep(0.05)
    mouse.click()
    time.sleep(0.05)
    kb.press_and_release('e')

  def indicator(self):
    pgui.move(50, 0, 0.05, pgui.easeOutQuad, _pause=False)
    pgui.move(-100, 0, 0.05, pgui.easeOutQuad, _pause=False)
    pgui.move(100, 0, 0.05, pgui.easeOutQuad, _pause=False)
    pgui.move(-100, 0, 0.05, pgui.easeOutQuad, _pause=False)
    pgui.move(50, 0, 0.05, pgui.easeOutQuad, _pause=False)

def init():
  pgui.PAUSE = 0.1
  pgui.MINIMUM_DURATION = 0.025

  inventory = Inventory()
  inventory.indicator()

  kb.add_hotkey('ctrl+l', inventory.locate)
  kb.add_hotkey('ctrl+i', lambda: inventory.locateItems(['totem-of-undying.png', 'water-bucket.png']))
  kb.add_hotkey('r', inventory.panicButton)
  kb.wait()

init()
