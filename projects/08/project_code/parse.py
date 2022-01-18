"""
Author: Michael Piskozub
Date Created: 7/20/2021

The Parser module of the VM translator built for project 8 of the 
Nand to Tetris MOOC by The Hebrew University of Jerusalem.

The Parser module from project 7 was extended so that the Parser
module could handle 'function', 'call', 'return', 'label', 'goto',
and 'if' commands. 

The Parser module handles the parsing of a single .vm file. It 
removes whitespace/comments and parses each VM command into its 
lexical elements.

See nand2tetris.org/project08 for the project description.
"""

class Parser():

  cArithmetic = 0 #command type id
  cPush = 1
  cPop = 2
  cLabel = 3
  cGoto = 4
  cIf = 5
  cFunction = 6
  cReturn = 7
  cCall = 8

  argToComType = { #maps command mnemonic to id
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

  def __removeWS(self, str):
    """
    Remove whitespace from str and return a list containing the lexical elements of the line, or an empty list if there are none.

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
    self.lines = file.readlines() #list all lines in input
    self.ind = 0 #line index
    self.mx = len(self.lines) #number of lines in input
    self.line = [] #current line

  def hasMoreCommands(self):
    """
    If there are more commands in the input file, return True. Otherwise, return False.
    
    :return: true if more commands present, false otherwise
    :rtype: bool
    """

    i = self.ind #index of current line
    curr = [] #current line

    while curr == []:
      if i <= (self.mx-1): #check if more lines exist
        curr = self.__removeWS(self.lines[i]) #remove whitespace/comments
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
      self.line = self.__removeWS(self.lines[self.ind]) #remove whitespace/comments
      self.ind += 1 #go to next line
    
    return #if self.line != [], then command has been found

  def commandType(self):
    """
    Returns the command type of the current command in the input file.
  
    :return: the command type id
    :rtype: int
    """

    return self.argToComType[self.line[0]]

  def arg1(self):
    """
    Return the first lexical element of the current command if the command is an arithmetic/logical command (this defines the type of arithmetic/logical command). Otherwise, return the second lexical element (this determines which memory segment to push from/pop to).

    :return: the first lexical element of the current command if it's an arithmetic/logical command. otherwise, return the second lexical element.
    :rtype: str
    """

    if self.commandType() == self.cArithmetic: #check if command is arithmetic/logical
      return self.line[0] #return first lexical element
    return self.line[1] #return second lexical element

  def arg2(self):
    """
    Return the third lexical element of the current command. (Note that calling this method on an arithmetic/logical command generates an error).

    :return: the third lexical element of the current command
    :rtype: str
    """

    return self.line[2] #return third lexical element