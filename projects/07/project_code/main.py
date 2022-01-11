"""
Author: Michael Piskozub
Date Created: 7/12/2021

The Main module of the VM translator built for project 7 of the Nand to Tetris MOOC by The Hebrew University of Jerusalem.

If the user entered 'filename.vm' as the command-line argument, then the Main module will translate the VM code in this file to Hack assembly code in the output file 'filename.asm'.

See nand2tetris.org/project07 for the project description.
"""

import sys #standard library

from code_writer import * #local source
from parse import *

inputFp = sys.argv[1]
k = inputFp.rfind(".")
outputFp = inputFp[:k] + ".asm" #output filename same as input, but has .asm extension

parser = Parser(inputFp)  #parser parses filename.vm
codeWriter = CodeWriter(outputFp) #codeWriter writes translated hack code to filename.asm

while parser.hasMoreCommands():
  parser.advance()  #go to next line in filename.vm
  commType = parser.commandType() #determine command type of current line

  if commType == parser.cArithmetic:  #determine if command type is arithmetic, pop, or push
    codeWriter.writeArithmetic(parser.arg1()) #translate and write to output file

  elif commType == parser.cPop:
    codeWriter.WritePushPop("pop", parser.arg1(), parser.arg2())
  
  elif commType == parser.cPush:
    codeWriter.WritePushPop("push", parser.arg1(), parser.arg2())

codeWriter.Close()  #close file after translation complete