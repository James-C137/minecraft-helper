import gc

from autoFisher import AutoFisher
from panicButton import PanicButton

class CLIManager:
  COMMAND_NAMES = [
    '/commands',
    '/toggle'
    '/list'
  ]
  SUBPROGRM_NAMES = [
    'autoFisher',
    'panicButton'
  ]

  subprograms = {}

  def __init__(self):
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
      self.runCommand(args)

  def runCommand(self, args):
    if (args[0] == '/commands'):
        self.printCommands()
    elif (args[0] == '/toggle'):
      if (not len(args) == 2):
        self.wrongNArgs(1, len(args)-1)
        return
      self.toggleSubprogram(args[1])
    else:
      print('unknown command')

  def toggleSubprogram(self, name:str):
    if (name in self.subprograms.keys()):
      print('stopping {}...'.format(name))
      self.subprograms[name].stop()
      self.subprograms.pop(name)
      gc.collect()
      print('{} disabled'.format(name))
    else:
      print('starting {}...'.format(name))
      program = None
      if (name == 'autoFisher'):
        program = AutoFisher()
      elif (name == 'panicButton'):
        program = PanicButton()
      else:
        print('unknown subProgram name "{}"'.format(name))
        return
      self.subprograms[name] = program
      print('{} enabled'.format(name))

  #region helpers
  def printCommands(self):
    print('/toggle [panicButton/autoFisher]')

  def wrongNArgs(self, expected:int, actual:int):
    print('wrong number of arguments. expected {}, got {}'.format(expected, actual))
  #endregion
  
cli = CLIManager()
