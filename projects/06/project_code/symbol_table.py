"""
Author: Michael Piskozub
Date Created: 7/12/2021

The SymbolTable module of the assembler built for project 6 of 
the Nand to Tetris MOOC by The Hebrew University of Jerusalem.

The SymbolTable module keeps a correspondence between symbolic
labels and numeric addresses.

See nand2tetris.org/project06 for the project description.
"""

class SymbolTable():

  def __init__(self):
    """
    Constructor method for SymbolTable class.
    
    :return: No return value.
    """
    
    self.symTable = { #default symbols
      "SP": 0, #pointer registers
      "LCL": 1,
      "ARG": 2,
      "THIS": 3,
      "THAT": 4,
      'R0': 0, #registers
      'R1': 1,
      'R2': 2,
      'R3': 3,
      'R4': 4,
      'R5': 5,
      'R6': 6,
      'R7': 7,
      'R8': 8,
      'R9': 9,
      'R10': 10,
      'R11': 11,
      'R12': 12,
      'R13': 13,
      'R14': 14,
      'R15': 15,
      "SCREEN": 16384, #I/O
      "KBD": 24576
    }

  def addEntry(self, symbol, address):
    """
    Add a symbol -> address mapping to SymbolTable.
    
    :param str symbol: Symbol to store.
    :param int address: Corresponding address.
    :return: No return value.
    """
    
    self.symTable[symbol] = address

  def contains(self, symbol):
    """
    Return True if symbol in symTable. Return False otherwise.
    
    :param str symbol: Symbol to check in symTable.
    :return: True if symbol present, false otherwise.
    :rtype: bool
    """
    
    if symbol in self.symTable:
      return True
    return False

  def GetAddress(self, symbol):
    """
    Return the address corresponding to the input symbol.
    
    :param str symbol: Input symbol to query.
    :return: The address corresponding to input symbol.
    :rtype: int
    """
    
    return self.symTable[symbol]