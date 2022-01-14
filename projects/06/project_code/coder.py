"""
Author: Michael Piskozub
Date Created: 7/12/2021

The Code module of the assembler built for project 6 of the Nand to 
Tetris MOOC by The Hebrew University of Jerusalem.

The Code module translates Hack assembly language mnemonics into
binary code.

See nand2tetris.org/project06 for the project description.
"""

class Code():
  destToBinary = { #dest mnemonic to binary
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
  }
  compToBinary = { #comp mnemonic to binary
    'M': '1110000', 
    '!M': '1110001', 
    '-M': '1110011', 
    'M+1': '1110111', 
    'M-1': '1110010', 
    'D+M': '1000010', 
    'D-M': '1010011', 
    'M-D': '1000111', 
    'D&M': '1000000', 
    'D|M': '1010101', 
    'A': '0110000', 
    '!A': '0110001', 
    '-A': '0110011', 
    'A+1': '0110111', 
    'A-1': '0110010', 
    'D+A': '0000010', 
    'D-A': '0010011', 
    'A-D': '0000111', 
    'D&A': '0000000', 
    'D|A': '0010101', 
    '0': '0101010', 
    '1': '0111111', 
    '-1': '0111010', 
    'D': '0001100', 
    '!D': '0001101', 
    '-D': '0001111', 
    'D+1': '0011111', 
    'D-1': '0001110'
  }
  jumpToBinary = { #jump mnemonic to binary
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
  }

  def dest(self, str):
    """
    Returns the binary code of the dest mnemonic for C-commands.
    
    :param str str: Input dest mnemonic.
    :return: The binary code corresponding to the dest mnemonic.
    :rtype: str
    """

    return self.destToBinary[str]
  
  def comp(self, str):
    """
    Returns the binary code of the comp mnemonic for C-commands.
    
    :param str str: Input comp mnemonic.
    :return: The binary code corresponding to the comp mnemonic.
    :rtype: str
    """
    
    return self.compToBinary[str]
  
  def jump(self, str):
    """
    Returns the binary code of the jump mnemonic for C-commands.

    :param str str: Input jump mnemonic.
    :return: The binary code corresponding to the jump mnemonic
    :rtype: str
    """

    return self.jumpToBinary[str]