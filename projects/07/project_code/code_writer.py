"""
Author: Michael Piskozub
Date Created: 7/12/2021

The CodeWriter module of the VM translator was built for project 7 of the Nand to Tetris MOOC by The Hebrew University of Jerusalem.

The CodeWriter module writes the hack assembly code corresponding to the input VM code command to the output file.

See nand2tetris.org/project07 for the project description.
"""

class CodeWriter():

  labelCnt = 0

  arithToAssembly = { #maps arithmetic/logical commands to hack assembly
    "add": ''.join([
      "@SP\n",
      "AM=M-1\n",
      "D=M\n",
      "A=A-1\n",
      "M=D+M\n"
      ]),
      
    "sub": ''.join([
      "@SP\n",
      "AM=M-1\n",
      "D=M\n",
      "A=A-1\n",
      "M=M-D\n"
      ]),

    "neg": ''.join([
      "@SP\n",
      "A=M-1\n",
      "M=-M\n"
    ]),

    "eq": ''.join([
      "@SP\n",
      "AM=M-1\n",
      "D=M\n",
      "A=A-1\n",
      "D=M-D\n",
      "@ONE\n", #replace w/ unique label
      "D;JEQ\n",
      "D=0\n",
      "@TWO\n", #replace w/ unique label
      "0;JMP\n",
      "(ONE)\n",#replace w/ unique label
      "D=-1\n",
      "(TWO)\n",#replace w/ unique label
      "@SP\n",
      "A=M-1\n",
      "M=D\n"
    ]),

  "gt": ''.join([
      "@SP\n",
      "AM=M-1\n",
      "D=M\n",
      "A=A-1\n",
      "D=M-D\n",
      "@ONE\n", #replace w/ unique label
      "D;JGT\n",
      "D=0\n",
      "@TWO\n", #replace w/ unique label
      "0;JMP\n",
      "(ONE)\n",#replace w/ unique label
      "D=-1\n",
      "(TWO)\n",#replace w/ unique label
      "@SP\n",
      "A=M-1\n",
      "M=D\n"
  ]),

  "lt": ''.join([
      "@SP\n",
      "AM=M-1\n",
      "D=M\n",
      "A=A-1\n",
      "D=M-D\n",
      "@ONE\n", #replace w/ unique label
      "D;JLT\n",
      "D=0\n",
      "@TWO\n", #replace w/ unique label
      "0;JMP\n",
      "(ONE)\n",#replace w/ unique label
      "D=-1\n",
      "(TWO)\n",#replace w/ unique label
      "@SP\n",
      "A=M-1\n",
      "M=D\n"
  ]),

    "and": ''.join([
      "@SP\n",
      "AM=M-1\n",
      "D=M\n",
      "A=A-1\n",
      "M=D&M\n"
    ]),

    "or": ''.join([
      "@SP\n",
      "AM=M-1\n",
      "D=M\n",
      "A=A-1\n",
      "M=D|M\n"
    ]),

    "not": ''.join([
      "@SP\n",
      "A=M-1\n",
      "M=!M\n"
    ])
  }

  pshPopToAssemb = {  #maps push/pop commands to hack assembly
    "push": {
      "constant": lambda self, index :
        ''.join([
          "@" + index + "\n",
          "D=A\n",
          "@SP\n",
          "M=M+1\n",
          "A=M-1\n",
          "M=D\n"
    ]),
      "local": lambda self, index :
        ''.join([
          "@LCL\n",
          "D=M\n",
          "@" + index + "\n",
          "A=D+A\n",
          "D=M\n",
          "@SP\n",
          "M=M+1\n",
          "A=M-1\n",
          "M=D\n"
        ]),

      "argument": lambda self, index :
        ''.join([
          "@ARG\n",
          "D=M\n",
          "@" + index + "\n",
          "A=D+A\n",
          "D=M\n",
          "@SP\n",
          "M=M+1\n",
          "A=M-1\n",
          "M=D\n"
        ]),

      "this": lambda self, index :
        ''.join([
          "@THIS\n",
          "D=M\n",
          "@" + index + "\n",
          "A=D+A\n",
          "D=M\n",
          "@SP\n",
          "M=M+1\n",
          "A=M-1\n",
          "M=D\n"
        ]),

      "that": lambda self, index :
        ''.join([
          "@THAT\n",
          "D=M\n",
          "@" + index + "\n",
          "A=D+A\n",
          "D=M\n",
          "@SP\n",
          "M=M+1\n",
          "A=M-1\n",
          "M=D\n"
        ]),

      "pointer": lambda self, index :
        ''.join([
          "@" + ["THIS", "THAT"][int(index)] + "\n",
          "D=M\n",
          "@SP\n",
          "M=M+1\n",
          "A=M-1\n",
          "M=D\n"
        ]),

      "temp": lambda self, index :
        ''.join([
          "@" + str(5 + int(index)) + "\n",
          "D=M\n",
          "@SP\n",
          "M=M+1\n",
          "A=M-1\n",
          "M=D\n"
        ]),

      "static": lambda self, index :
        ''.join([
          "@" + self.filePrefix + "." + index + "\n",
          "D=M\n",
          "@SP\n",
          "M=M+1\n",
          "A=M-1\n",
          "M=D\n",
        ])
    },
    
    "pop": {
      "local": lambda self, index :
        ''.join([
          "@LCL\n",
          "D=M\n",
          "@" + index + "\n",
          "D=D+A\n",
          "@SP\n",
          "A=M\n",
          "M=D\n",
          "@SP\n",
          "AM=M-1\n",
          "D=M\n",
          "A=A+1\n",
          "A=M\n",
          "M=D\n"
        ]),

      "argument": lambda self, index :
        ''.join([
          "@ARG\n",
          "D=M\n",
          "@" + index + "\n",
          "D=D+A\n",
          "@SP\n",
          "A=M\n",
          "M=D\n",
          "@SP\n",
          "AM=M-1\n",
          "D=M\n",
          "A=A+1\n",
          "A=M\n",
          "M=D\n"
        ]),

      "this": lambda self, index :
        ''.join([
          "@THIS\n",
          "D=M\n",
          "@" + index + "\n",
          "D=D+A\n",
          "@SP\n",
          "A=M\n",
          "M=D\n",
          "@SP\n",
          "AM=M-1\n",
          "D=M\n",
          "A=A+1\n",
          "A=M\n",
          "M=D\n"
        ]),

      "that": lambda self, index :
        ''.join([
          "@THAT\n",
          "D=M\n",
          "@" + index + "\n",
          "D=D+A\n",
          "@SP\n",
          "A=M\n",
          "M=D\n",
          "@SP\n",
          "AM=M-1\n",
          "D=M\n",
          "A=A+1\n",
          "A=M\n",
          "M=D\n"
        ]),

      "pointer": lambda self, index :
        ''.join([
          "@SP\n",
          "AM=M-1\n",
          "D=M\n",
          "@" + ["THIS", "THAT"][int(index)] + "\n",
          "M=D\n"
        ]),

      "temp": lambda self, index :
        ''.join([
          "@SP\n",
          "AM=M-1\n",
          "D=M\n",
          "@" + str(5 + int(index)) + "\n",
          "M=D\n"
        ]),

      "static": lambda self, index :
        ''.join([
          "@SP\n",
          "AM=M-1\n",
          "D=M\n",
          "@" + self.filePrefix + "." + index + "\n"
          "M=D\n"
        ])
    }
  }

  def __init__(self, filepath):
    """Takes output filepath and returns the CodeWriter object that writes to that output file.
    
    :param str filepath: path to output file
    :return: CodeWriter object that writes to the output file
    :rtype: CodeWriter
    """

    self.filePrefix = filepath.split("/")[-1][:-4]
    self.file = open(filepath, "w")

  def writeArithmetic(self, command):
    """Translates the input arithmetic/logical VM command to hack assembly code and writes the hack assembly code to the output file.

    :param str command: the command to be translated
    :return: no return value
    """
    #1st line is comment containing the command to be translated
    firstLine = "\n//" + command + "\n"
    translated = self.arithToAssembly[command]

    #if command is eq, gt, or lt, replace the "ONE" & "TWO" labels with a unique label
    if command in ["eq", "gt", "lt"]:
      for oldLab in ["ONE", "TWO"]:
        newLab = "L" + str(self.labelCnt)
        translated = translated.replace(oldLab, newLab)
        self.labelCnt += 1

    translated = firstLine + translated
    
    self.file.write(translated) #write the translated assembly code to output file

  def WritePushPop(self, command, segment, index):
    """Translates the input push/pop VM command to hack assembly code and writes the hack assembly code to the output file.
    
    :param str command: the command to be translated
    :param str segment: the memory segment to push from/pop to
    :param str index: the index in the memory segment to push from/pop to
    :return: no return value
    """

    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", command, segment, index, "\n"])

    translated = firstLine + self.pshPopToAssemb[command][segment](self, index) #translated code

    self.file.write(translated) #write the translated assembly code to output file

  def Close(self):
    """
    Closes the output file.
    
    :return: no return value
    """
    
    self.file.close()