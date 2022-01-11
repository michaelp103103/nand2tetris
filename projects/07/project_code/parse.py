"""
Author: Michael Piskozub
Date Created: 7/12/2021

The Parser module of the VM translator was built for project 7 of the Nand to Tetris MOOC by The Hebrew University of Jerusalem.

The Parser module reads each line of the input file, parses each line into its lexical elements, and provides information about the command type as well as the command arguments for each line.

See nand2tetris.org/project07 for the project description.
"""

class Parser():

  cArithmetic = 1 #each command type has an id
  cPush = 2
  cPop = 3
  cLabel = 4
  cGoto = 5
  cIf = 6
  cFunction = 7
  cReturn = 8
  cCall = 9

  arithCommands = [ #valid commands
    "add",
    "sub",
    "neg",
    "eq",
    "gt",
    "lt",
    "and",
    "or",
    "not"
  ]
  pushCom = "push"
  popCom = "pop"

  def __removeWS(self, str):
    """Remove whitespace from str and return a list containing the lexical elements of the line, or an empty list if there are none.

    Ex. 
    If str = "push local 0", return ["push", "local", "0"]

    :param str str: a string
    :return: a list containing the lexical elements of the line or empty list if none present
    :rtype: list
    """
    
    #remove comments
    str = str.split("//")[0]
    #remove leading/trailing whitespace
    str = str.strip()
    #split str into components
    l = str.split()
    return l

  def __init__(self, filepath):
    """Takes input .vm filepath and returns the Parser object that reads that .vm file.
    
    :param str filepath: filepath to the input .vm file
    :return: Parser object that reads input .vm file
    :rtype: Parser
    """

    file = open(filepath, "r") #open input file
    self.lines = file.readlines() #list of all lines in input file
    self.ind = 0 #index of current line
    self.mx = len(self.lines) #number of lines in input file
    self.line = [] #current line

  def hasMoreCommands(self):
    """
    If there are more commands in the input file, return True. Otherwise, return False.
    
    :return: true if more commands present, false otherwise
    :rtype: bool
    """
    
    i = self.ind  #index of current line
    curr = [] #current line

    while curr == []: 
      if i <= (self.mx-1): #if there are more lines, check next line
        curr = self.__removeWS(self.lines[i]) #remove whitespace and comments
        i += 1
      else: #otherwise, no more commands
        return False

    return True #if curr != [], then another command exists

  def advance(self):
    """
    Advances the line to the next command in the input file.

    :return: no return value
    """

    self.line = [] #current line

    while self.line == []: #loop while current line doesn't contain command
      self.line = self.__removeWS(self.lines[self.ind]) #remove whitespace and comments
      self.ind += 1 #go to next line
    
    return #if self.line != [], then command has been found

  def commandType(self):
    """
    Returns the command type of the current command in the input file.
  
    :return: the command type id
    :rtype: int
    """
    if self.line[0] in self.arithCommands: #check if arithmetic/logical command
      return self.cArithmetic

    elif self.line[0] == self.pushCom: #check if push command
      return self.cPush

    elif self.line[0] == self.popCom: #check if pop command
      return self.cPop

    else:
      return

  def arg1(self):
    """
    Return the first lexical element of the current command if the command is an arithmetic/logical command (this defines the type of arithmetic/logical command). Otherwise, return the second lexical element (this determines which memory segment to push from/pop to).

    :return: the first lexical element of the current command if it's an arithmetic/logical command. otherwise, return the second lexical element.
    :rtype: str
    """
    if self.commandType() == self.cArithmetic: #check if command is arithmetic/logical command
      return self.line[0] #return firs lexical element
    return self.line[1] #return second lexical element

  def arg2(self):
    """
    Return the third lexical element of the current command. (Note that only push/pop commands have three lexical elements and calling this method on an arithmetic/logical command generates an error).

    :return: the third lexical element of the current command
    :rtype: str
    """

    return self.line[2] #return third lexical element