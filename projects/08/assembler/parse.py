import re

class Parser():
  aCom = 0
  cCom = 1
  lCom = 2
  noCom = 3

  #remove whitespace
  def removeWS(self, str):
    #remove whitespace
    str = ''.join(str.split())
    #remove comments
    str = str.split("//")[0]
    return str
  
  def __init__(self, filepath):
    file = open(filepath, "r")
    self.lines = file.readlines()
    self.ind = 0
    self.mx = len(self.lines)
    self.line = ""

  #are there more commands in input?
  def hasMoreCommands(self):
    i = self.ind
    curr = ""

    while curr == "":
      if i <= (self.mx-1):
        curr = self.removeWS(self.lines[i])
        i += 1
      else:
        return False

    return True

  #reads next command and makes it current command
  def advance(self):
    self.line = ""

    while (self.line == "") or (self.line[0:2] == "//"):
      self.line = self.removeWS(self.lines[self.ind])
      self.ind += 1
    
    return

  #return the type of the current command
  def commandType(self):
    if self.line[0] == "@":
      return self.aCom
    if self.line[0] == "(":
      return self.lCom
    return self.cCom

  #returns symbol or decimal Xxx of the current command @Xxx or (Xxx)
  def symbol(self):
    if self.line[0] == "@":
      return self.line[1:].split("/")[0]
    if self.line[0] == "(":
      return self.line[1:].split(")")[0]

  #returns the dest mnemonic of the current C-command
  def dest(self):
    s = self.line.split("=")
    if len(s) == 2:
      return s[0]
    return ""
  
  #returns the comp mnemonic in the current C-command
  def comp(self):
    s = re.split('=', self.line)
    if len(s) == 2:
      s = s[1]
    else:
      s = s[0]
    s = re.split(';|/', s)
    return s[0]
  
  #returns the jump mnemonic in the current C-command
  def jump(self):
    s = re.split(';', self.line)
    if len(s) == 2:
      s = s[1]
    else:
      return ""
    s = re.split('/',s)
    return s[0]

  #advance to the next line
  def advanceListing(self):
    self.line = self.lines[self.ind]
    self.ind += 1
  
  #return the type of the current command
  def commTypeListing(self):
    line = self.line.lstrip()
    if line != "":
      if line[0] == "@":
        return self.aCom
      if line[0] == "(":
        return self.lCom
      if line[0] in ["!", "A", "M", "D", "0", "-", "1"]:
        return self.cCom
      return self.noCom
    return self.noCom

  #does the file have more lines?
  def hasMoreLines(self):
    return self.ind <= (self.mx-1)

  #return the unmodified source line
  def sourceLine(self):
    return self.line