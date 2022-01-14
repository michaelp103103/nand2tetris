# Nand2Tetris: Project 8
# Notes:
# - Generate startup code ONLY when    
#   translating a directory.
# - DO NOT generate startup code when 
#   translating a single file.

import sys
import os

from helpers import *
from code_writer import *
from parse import *

#command line argument must be an absolute path
inputPath = sys.argv[1]

if os.path.isfile(inputPath):
  k = inputPath.rfind(".")
  outputFp = inputPath[:k] + ".asm"
  parser = Parser(inputPath)
  codeWriter = CodeWriter(outputFp)
  codeWriter.setFileName(inputPath)
  translate_file(parser, codeWriter)
  
  codeWriter.Close()

else:
  dirName = os.path.basename(os.path.normpath(inputPath))
  outputFn = dirName + ".asm"
  outputFp = os.path.join(inputPath, outputFn)
  codeWriter = CodeWriter(outputFp)

  #codeWriter.writeInit() #write bootstrap code

  for file in os.listdir(inputPath):
    if file[-3:] == ".vm":
      inputFp = os.path.join(inputPath,file)
      parser = Parser(inputFp)
      codeWriter.setFileName(inputFp)
      translate_file(parser, codeWriter)

  codeWriter.Close()