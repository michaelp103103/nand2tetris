"""
Author: Michael Piskozub
Date Created: 7/12/2021

Helper functions for the assembler program.

See nand2tetris.org/project06 for the project description.
"""

from coder import * #local
from parse import *
from symbol_table import *

def decToBin(num):
  """
  Convert a decimal integer (as an int) to a 15-bit binary number 
  (as a str) and return it.

  :param int num: A decimal integer
  :return: A 15-bit binary integer
  :rtype: str
  """

  res = list("0" * 15) #res will contain the 15-bit number
  ind = len(res)-1 #set ind to index of the LSB in res

  while num > 0: #convert to binary
    remainder = num % 2 #if remainder exists, res[ind] = 1
    res[ind] = str(remainder)
    ind -= 1 #move to next most-significant bit
    num = num // 2
  
  return "".join(res) #join bits together and return

def noSymbolAssemble(filepath):
  """
  Translate a hack assembly program that does not contain symbols (i.e., no symbolic 
  references to memory addresses) into binary code.

  :param str filepath: input .asm file
  :return: no return value
  """

  parser = Parser(filepath) #parser for input file
  code = Code() #code translates commands to binary
  k = filepath.rfind(".")
  filename = filepath[:k] + ".hack" #output filename

  with open(filename, "w") as f:
    while (parser.hasMoreCommands()):
      line = "" #will contain binary code to output
      parser.advance() #go to next command
      commType = parser.commandType() #get command type

      if commType == parser.aCom: #translate according to comm type
        addr = decToBin(int(parser.symbol()))
        line = "0" + addr
      elif commType == parser.cCom:
        comp = code.comp(parser.comp()) #translate each C comm element
        dest = code.dest(parser.dest())
        jump = code.jump(parser.jump())
        line = "111" + comp + dest + jump

      line = line + "\n"
      f.write(line) #write line to output file

def assemble(filepath):
  """
  Translate a hack assembly program that contains symbols (i.e., contains symbolic 
  references to memory addresses) into binary code.

  :param str filepath: input .asm file
  :return: no return value
  """

  parser = Parser(filepath) #parser for input file
  code = Code() #translates commands to binary
  symTable = SymbolTable() #maps symbolic labels to addresses
  memCnt = 16 #next available memory address
  instCnt = 0 #running instruction count
  k = filepath.rfind(".")
  filename = filepath[:k] + ".hack" #output filename

  #first pass
  while(parser.hasMoreCommands()):
    parser.advance() #next command
    commType = parser.commandType() #get command type
    symbol = parser.symbol() #command symbol

    if (commType == parser.lCom) and parser.hasMoreCommands():
      symTable.addEntry(symbol, instCnt) #store label line

    if commType != parser.lCom:
      instCnt += 1

  #second pass
  parser = Parser(filepath) #start from beginning

  with open(filename, "w") as f:
    while (parser.hasMoreCommands()):
      line = ""
      parser.advance()
      commType = parser.commandType()

      #A command
      if commType == parser.aCom:
        num = 0
        symbol = parser.symbol() #get symbol

        if symbol.isdecimal(): #resolve symbol to address
          num = int(symbol)
        elif symTable.contains(symbol):
          num = symTable.GetAddress(symbol)
        else: #map variable symbol to address
          num = memCnt
          symTable.addEntry(symbol, memCnt)
          memCnt += 1

        addr = decToBin(num)
        line = "0" + addr
      
      #C Command
      elif commType == parser.cCom: #translate C comm elements
        comp = code.comp(parser.comp())
        dest = code.dest(parser.dest())
        jump = code.jump(parser.jump())
        line = "111" + comp + dest + jump
      
      #L command
      else:
        continue #L commands not translated

      line = line + "\n"
      f.write(line)
      
def genListing(filepath):
  """
  This function is used for project 8 to create listing files from the translated 
  .asm files.

  :param str filepath: input .asm file
  :return: no return value
  """
  
  parser = Parser(filepath)
  romAddr = 0 #rom address
  k = filepath.rfind(".")
  filename = filepath[:k] + ".list"   #output filename
    
  with open(filename, "w") as f:
    while parser.hasMoreLines():
      line = ""
      parser.advanceListing() #go to next line
      commType = parser.commTypeListing() #comm type of line
            
      #if comm type == noCom or lCom, output "\t instruction"
      if (commType == parser.noCom) or (commType == parser.lCom):
        line = "\t" + parser.sourceLine()
                
      #else, output "romAddr \t instruction"
      else:
        line = str(romAddr) + "\t" + parser.sourceLine()
        romAddr += 1
            
      f.write(line)   #write to output file