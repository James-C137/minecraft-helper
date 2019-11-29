import keyboard as kb

import lib.indicator as indicator
from inventoryManager import InventoryManager

functionStates = [ False, False, False, False, False ]
functionHotkeys = [ [], [], [], [], [] ]
inventory = None

def toggleFunction(number):
  if (number == 0):
    indicator.shake()
    if (functionStates[number]):
      for i in functionHotkeys[0]:
        kb.remove_hotkey(i)
      print('========== panic button disabled ==========')
    else:
      functionHotkeys[0] = []
      functionHotkeys[0].append(kb.add_hotkey('ctrl+p', inventory.setup))
      functionHotkeys[0].append(kb.add_hotkey('ctrl+i', inventory.findInventory))
      functionHotkeys[0].append(kb.add_hotkey('ctrl+k', lambda:inventory.findKeyItems(['totem-of-undying', 'water-bucket'])))
      functionHotkeys[0].append(kb.add_hotkey('r', inventory.panicButton))
      functionHotkeys[0].append(kb.add_hotkey('ctrl+d+1', inventory.debug))
      print('========== panic button enabled ==========')
  elif (number == 1):
    indicator.shake()
    if (functionStates[number]):
      pass
    else:
      pass
  elif (number == 2):
    indicator.shake()
    if (functionStates[number]):
      pass
    else:
      pass
  elif (number == 3):
    indicator.shake()
    if (functionStates[number]):
      pass
    else:
      pass
  elif (number == 4):
    indicator.shake()
    if (functionStates[number]):
      pass
    else:
      pass
  functionStates[number] = not functionStates[number]

def init():
  print('Minecraft Helper v0.0.1 by James Zhao')
  print('This is a tool to help with miscellaneous Minecraft tasks')
  print('press ctrl + function number to toggle its usage and see its instructions')
  print('================================================================================')
  print('function #1 - panic button')
  print('function #2 - auto fisher')
  print('function #3 - auto miner')
  print('function #4 - auto clicker (for mob farms, etc.)')
  print('function #5 - auto bridger')
  print()
  indicator.shake()
  global inventory
  inventory = InventoryManager()

  kb.add_hotkey('ctrl+1', lambda:toggleFunction(0))
  kb.add_hotkey('ctrl+2', lambda:toggleFunction(1))
  kb.add_hotkey('ctrl+3', lambda:toggleFunction(2))
  kb.add_hotkey('ctrl+4', lambda:toggleFunction(3))
  kb.add_hotkey('ctrl+5', lambda:toggleFunction(4))
  kb.wait()

init()
