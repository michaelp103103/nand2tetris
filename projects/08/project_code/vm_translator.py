"""
Author: Michael Piskozub
Date Created: 7/20/2021

The Main module of the VM translator built for project 8 of the 
Nand to Tetris MOOC by The Hebrew University of Jerusalem.

The Main module drives the process of translating the input VM 
code to assembly code.

Input:
- fileName.vm: the name of a single source file, or
- directoryName: the name of a directory containing one or more
                 .vm source files.

Output:
- fileName.asm file, or
- directoryName.asm file

Process:
- Constructs a CodeWriter object.
- If the input is a .vm file:
   - Constructs a Parser to handle the input file.
   - Marches through the input file, parsing each line and
     generating code from it.
- If the input is a directory:
   - Handles every .vm file in the directory in the manner
     described above.

See nand2tetris.org/project08 for the project description.
"""

import sys #standard lib
import os

from helpers import * #local
from code_writer import *
from parse import *

#obtain input path
inputPath = sys.argv[1]

#input is file
if os.path.isfile(inputPath):
  k = inputPath.rfind(".")
  outputFp = inputPath[:k] + ".asm" #output file is 'fileName.asm'
  parser = Parser(inputPath)
  codeWriter = CodeWriter(outputFp)
  filePref = os.path.splitext(inputPath)[0]
  filePref = os.path.basename(filePref)
  codeWriter.setFileName(filePref) #filename needed for symbols
  translate_file(parser, codeWriter)
  
  codeWriter.Close()

#input is directory
else:
  dirName = os.path.basename(os.path.normpath(inputPath))
  outputFn = dirName + ".asm" #output file is 'directoryName.asm'
  outputFp = os.path.join(inputPath, outputFn)
  codeWriter = CodeWriter(outputFp)

  codeWriter.writeInit() #write bootstrap code

  for file in os.listdir(inputPath): #translate each .vm file
    filePref, fileExt = os.path.splitext(file)
    if fileExt == ".vm":
      inputFp = os.path.join(inputPath,file)
      parser = Parser(inputFp)
      codeWriter.setFileName(filePref) #filenames needed for symbols
      translate_file(parser, codeWriter)

  codeWriter.Close()