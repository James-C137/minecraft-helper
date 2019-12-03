import gc

from inventoryManager import InventoryManager
from subprograms.autoFisher import AutoFisher
from subprograms.panicButton import PanicButton

subPrograms = {}

def runCommand(args):
  if (args[0] == '/commands'):
      printCommands()
  elif (args[0] == '/toggle'):
    if (not len(args) == 2):
      wrongNArgs(1, len(args)-1)
      return
    toggleCommand(args[1])
  else:
    print('unknown command')

def toggleCommand(name:str):
  if (name in subPrograms.keys()):
    print('stopping {}...'.format(name))
    subPrograms[name].stop()
    subPrograms.pop(name)
    gc.collect()
    print('{} disabled'.format(name))
  else:
    program = None
    if (name == 'autoFisher'):
      program = AutoFisher()
    elif (name == 'panicButton'):
      program = PanicButton()
    else:
      print('unknown subProgram name "{}"'.format(name))
      return
    print('starting {}...'.format(name))
    subPrograms[name] = program
    print('{} enabled'.format(name))

def printCommands():
  print('/toggle [panicButton/autoFisher]')

def wrongNArgs(expected:int, actual:int):
  print('wrong number of arguments. expected {}, got {}'.format(expected, actual))

def init():
  print('Minecraft Helper v0.0.1 by James Zhao')
  print('type "/commands" to see all commands')
  print('========================================')
  while (True):
    choice = input()
    if (choice == ''):
      continue
    if (not choice[0] == '/'):
      print('invalid command, commands must start with "/"')
      continue
    args = choice.split(' ')
    runCommand(args)

init()
