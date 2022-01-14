class Parser():

  cArithmetic = "C_ARITHMETIC"
  cPush = "C_PUSH"
  cPop = "C_POP"
  cLabel = "C_LABEL"
  cGoto = "C_GOTO"
  cIf = "C_IF"
  cFunction = "C_FUNCTION"
  cReturn = "C_RETURN"
  cCall = "C_CALL"

  argToComType = {
    "add": cArithmetic,
    "sub": cArithmetic,
    "neg": cArithmetic,
    "eq": cArithmetic,
    "gt": cArithmetic,
    "lt": cArithmetic,
    "and": cArithmetic,
    "or": cArithmetic,
    "not": cArithmetic,
    "push": cPush,
    "pop": cPop,
    "if-goto": cIf,
    "goto": cGoto,
    "label": cLabel,
    "call": cCall,
    "function": cFunction,
    "return": cReturn
  }

  #remove whitespace
  def __removeWS(self, str):
    #remove comments
    str = str.split("//")[0]
    #remove leading/trailing whitespace
    str = str.strip()
    #split str into components
    l = str.split()
    return l

  def __init__(self, filepath):
    file = open(filepath, "r")
    self.lines = file.readlines()
    self.ind = 0
    self.mx = len(self.lines)
    self.line = []

  #are there more commands in input?
  def hasMoreCommands(self):
    i = self.ind
    curr = []

    while curr == []:
      if i <= (self.mx-1):
        curr = self.__removeWS(self.lines[i])
        i += 1
      else:
        return False

    return True

  #reads next command and makes it current command
  def advance(self):
    self.line = []

    while self.line == []:
      self.line = self.__removeWS(self.lines[self.ind])
      self.ind += 1
    
    return

  #what type of command is current line?
  def commandType(self):
    return self.argToComType[self.line[0]]

  #return 1st arg of command
  def arg1(self):
    if self.commandType() == self.cArithmetic:
      return self.line[0]
    return self.line[1]

  #return 2nd arg of command
  def arg2(self):
    return self.line[2]