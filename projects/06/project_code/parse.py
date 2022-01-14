"""
Author: Michael Piskozub
Date Created: 7/12/2021

The Parser module of the assembler built for project 6 of the 
Nand to Tetris MOOC by The Hebrew University of Jerusalem.

The Parser module encapsulates access to the input code. It
reads an assembly language command, parses it, and provides 
convenient access to the command's components (fields and
symbols). In addition, it removes all white space and comments.


See nand2tetris.org/project06 for the project description.
"""

import re #standard library

class Parser():
  aCom = 0 #command type ID
  cCom = 1
  lCom = 2
  noCom = 3

  def removeWS(self, str):
    """
    Remove the whitespace and comments from the input and 
    return it.

    :param str str: Input string.
    :return: Return the input string without whitespace or 
             comments.
    :rtype: str
    """
    #remove whitespace
    str = ''.join(str.split())
    #remove comments
    str = str.split("//")[0]
    return str
  
  def __init__(self, filepath):
    """
    Constructor method for the Parser class.
    
    :param str filepath: Input file to parse.
    :return: No return value.
    """
    
    file = open(filepath, "r")
    self.lines = file.readlines()
    self.ind = 0 #line index
    self.mx = len(self.lines) #number of lines
    self.line = "" #current line

  def hasMoreCommands(self):
    """
    Return True if there are more commands in the input.
    Return False otherwise.

    :return: True is there are more commands, False otherwise.
    :rtype: bool
    """
    
    i = self.ind #current line index
    curr = "" #current line

    while curr == "":
      if i <= (self.mx-1):
        #remove whitespace/comments
        curr = self.removeWS(self.lines[i])
        i += 1 #increment line index
      else: #no more lines
        return False

    return True

  def advance(self):
    """
    Read the next command and set it as the current command.

    :return: No return value.
    """

    self.line = "" #current line

    while (self.line == "") or (self.line[0:2] == "//"):
      #remove whitespace/comments
      self.line = self.removeWS(self.lines[self.ind])
      self.ind += 1
    
    return

  def commandType(self):
    """
    Return the type of the current command.

    :return: Type of the current command.
    :rtype: int
    """

    if self.line[0] == "@": #A-command
      return self.aCom
    if self.line[0] == "(": #L-command
      return self.lCom
    return self.cCom #C-command

  def symbol(self):
    """
    Return the symbol/decimal Xxx of the current command @Xxx
    or (Xxx).
    
    :return: Symbol/decimal Xxx if command is @Xxx or (Xxx).
    :rtype: str
    """

    if self.line[0] == "@": #A-command
      return self.line[1:].split("/")[0]
    if self.line[0] == "(": #L-command
      return self.line[1:].split(")")[0]

  def dest(self):
    """
    Return the dest mnemonic of the current C-command.

    :return: dest mnemonic of the current C-command.
    :rtype: str
    """

    # dest = comp; jump  <--  C-command format
    s = self.line.split("=")
    if len(s) == 2:
      return s[0] #obtain dest component
    return ""

  def comp(self):
    """
    Return the comp mnemonic of the current C-command.

    :return: comp mnemonic of the current C-command.
    :rtype: str
    """
    
    # dest = comp; jump  <--  C-command format
    s = re.split('=', self.line)
    if len(s) == 2: #command contains dest
      s = s[1]
    else: #command does NOT contain dest
      s = s[0]
    s = re.split(';|/', s)
    return s[0]
  
  def jump(self):
    """
    Return the jump mnemonic of the current C-command.
    
    :return: jump mnemonic of current C-command.
    :rtype: str
    """
    
    # dest = comp; jump  <--  C-command format
    s = re.split(';', self.line) 
    if len(s) == 2: #jump component exists
      s = s[1]
    else: #jump component does NOT exist
      return ""
    s = re.split('/',s)
    return s[0]

  def advanceListing(self):
    """
    (Used for listing file program)
    Advance to the next line.
    
    :return: No return value.
    """
    
    self.line = self.lines[self.ind]
    self.ind += 1
  
  def commTypeListing(self):
    """
    (Used for listing file program)
    Return the type of the current command.
    
    :return: Command type of current command.
    :rtype: int
    """
    
    line = self.line.lstrip() #remove leading whitespace
    if line != "": #line not empty
      if line[0] == "@": #A-command
        return self.aCom
      if line[0] == "(": #L-command
        return self.lCom
      if line[0] in ["!", "A", "M", "D", "0", "-", "1"]:#C-command
        return self.cCom
      return self.noCom #no command
    return self.noCom #no command

  def hasMoreLines(self):
    """
    Return True if more lines in file. Return False otherwise.

    :return: True if more lines, false otherwise.
    :rtype: bool
    """

    return self.ind <= (self.mx-1)

  def sourceLine(self):
    """
    Return the current, unmodified source line.
    
    :return: Current, unmodified source line.
    :rtype: str
    """
    
    return self.line