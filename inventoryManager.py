import mouse as mouse
import keyboard as kb
import time
from typing import List

import lib.indicator as indicator
from lib.inventory import Inventory
from lib.vector2 import Vector2

class InventoryManager:
  MOUSE_SPEED = 0
  PAUSE_TIME = 0.055

  inventory:Inventory = None

  def __init__(self):
    self.inventory = Inventory()
  
  #region functionality
  def panicButton(self):
    kb.press_and_release('e')
    time.sleep(self.PAUSE_TIME)
    if ('totem-of-undying' in self.inventory.keyItems):
      self.fastSwap(self.inventory.keyItems['totem-of-undying'], self.inventory.offhandSlot)
    if ('water-bucket' in self.inventory.keyItems):
      self.fastSwap(self.inventory.keyItems['water-bucket'], self.inventory.hotbarSlot[8])
    kb.press_and_release('e')
    kb.press_and_release('9')
  #endregion

  #region setup
  def findInventory(self):
    print('setting bounds...')
    found = self.inventory.setBounds()
    indicator.printState(found)
    indicator.show(found)
    self.inventory.setSlots()
    print()

  def findKeyItem(self, name:str):
    print('finding item "' + name + '"...')
    found = self.inventory.findKeyItem(name)
    indicator.printState(found)
    indicator.show(found)
    print()

  def findKeyItems(self, names:List[str]):
    print('finding items...')
    for name in names:
      print('finding item "' + name + '"...')
      found = self.inventory.findKeyItem(name)
      indicator.printState(found)
    indicator.shake()
    print('done')
    print()
  
  def setup(self):
    self.findInventory()
    self.findKeyItems(['totem-of-undying', 'water-bucket'])
  #endregion

  #region utils
  def fastSwap(self, a:Vector2, b:Vector2):
    mouse.move(a.x, a.y, duration=self.MOUSE_SPEED)
    time.sleep(self.PAUSE_TIME)
    mouse.double_click()
    mouse.move(b.x, b.y, duration=self.MOUSE_SPEED)
    time.sleep(self.PAUSE_TIME)
    mouse.click()
    mouse.move(a.x, a.y, duration=self.MOUSE_SPEED)
    time.sleep(self.PAUSE_TIME)
    mouse.click()

  def showBounds(self):
    print('outlining bounds...')
    if (self.inventory.bounds == None):
      print('failed: bounds is not set')
      print()
      return
    self.inventory.showBounds()
    print('done')
    print()

  def showSlots(self):
    print('showing slots...')
    if (self.inventory.bounds == None):
      print('failed: bounds is not set')
      print()
      return
    inv = self.inventory
    # armorSlot
    for i in inv.armorSlot:
      i.show()
      time.sleep(self.PAUSE_TIME)
    # craftingSlot
    for i in inv.craftingSlot:
      i.show()
      time.sleep(self.PAUSE_TIME)
    # outputSlot
    inv.outputSlot.show()
    time.sleep(self.PAUSE_TIME)
    # offhandSlot
    inv.offhandSlot.show()
    time.sleep(self.PAUSE_TIME)
    # storageSlot
    for i in inv.storageSlot:
      for j in i:
        j.show()
        time.sleep(self.PAUSE_TIME)
    # hotbarSlot
    for i in inv.hotbarSlot:
      i.show()
      time.sleep(self.PAUSE_TIME)
    print('done')
    print()

  def showKeyItems(self):
    print('showing items...')
    keyItems = self.inventory.keyItems
    for key in keyItems.keys():
      keyItems[key].show()
      time.sleep(self.PAUSE_TIME)
    print('done')
    print()

  def debug(self):
    self.showBounds()
    self.showSlots()
    self.showKeyItems()
  #endregion
