"""
Author: Michael Piskozub
Date Created: 7/12/2021

The Main module of the assembler built for project 6 of the Nand to 
Tetris MOOC by The Hebrew University of Jerusalem.

The Main module initializes the I/O files and drives the process of 
translating symbolic hack assembly code to binary.

See nand2tetris.org/project06 for the project description.
"""

import sys #standard lib

from helpers import * #local

assemble(sys.argv[1]) #run assembler on command line arg
#genListing(sys.argv[1]) #run listing program on comm line arg