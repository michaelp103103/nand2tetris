from coder import *
from parse import *
from symbol_table import *
import sys

def decToBin(num):
  res = list("0" * 15)
  ind = len(res)-1

  while num > 0:
    remainder = num % 2
    res[ind] = str(remainder)
    ind -= 1
    num = num // 2
  
  return "".join(res)

def noSymbolAssemble(filepath):
  parser = Parser(filepath)
  code = Code()
  k = filepath.rfind(".")
  filename = filepath[:k] + ".hack"

  with open(filename, "w") as f:
    while (parser.hasMoreCommands()):
      line = ""
      parser.advance()
      commType = parser.commandType()

      if commType == parser.aCom:
        addr = decToBin(int(parser.symbol()))
        line = "0" + addr
      elif commType == parser.cCom:
        comp = code.comp(parser.comp())
        dest = code.dest(parser.dest())
        jump = code.jump(parser.jump())
        line = "111" + comp + dest + jump

      line = line + "\n"
      f.write(line)

def assemble(filepath):
  parser = Parser(filepath)
  code = Code()
  symTable = SymbolTable()
  memCnt = 16
  instCnt = 0
  k = filepath.rfind(".")
  filename = filepath[:k] + ".hack"

  #first pass
  while(parser.hasMoreCommands()):
    parser.advance()
    commType = parser.commandType()
    symbol = parser.symbol()

    if (commType == parser.lCom) and parser.hasMoreCommands():
      symTable.addEntry(symbol, instCnt)

    if commType != parser.lCom:
      instCnt += 1

  #second pass
  parser = Parser(filepath)

  with open(filename, "w") as f:
    while (parser.hasMoreCommands()):
      line = ""
      parser.advance()
      commType = parser.commandType()

      #A command
      if commType == parser.aCom:
        num = 0
        symbol = parser.symbol()

        if symbol.isdecimal():
          num = int(symbol)
        elif symTable.contains(symbol):
          num = symTable.GetAddress(symbol)
        else:
          num = memCnt
          symTable.addEntry(symbol, memCnt)
          memCnt += 1

        addr = decToBin(num)
        line = "0" + addr
      
      #C Command
      elif commType == parser.cCom:
        comp = code.comp(parser.comp())
        dest = code.dest(parser.dest())
        jump = code.jump(parser.jump())
        line = "111" + comp + dest + jump
      
      #L command
      else:
        continue

      line = line + "\n"
      f.write(line)
      
def genListing(filepath):
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

#assemble(sys.argv[1])
genListing(sys.argv[1])