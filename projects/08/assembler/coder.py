class Code():
  destToBinary = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
  }
  compToBinary = {
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
  jumpToBinary = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
  }

  #returns the binary code of the dest mnemonic
  def dest(self, str):
    return self.destToBinary[str]
  
  #returns the binary code of the comp mnemonic
  def comp(self, str):
    return self.compToBinary[str]
  
  #returns the binary code of the jump mnemonic
  def jump(self, str):
    return self.jumpToBinary[str]