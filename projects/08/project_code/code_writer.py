"""
Author: Michael Piskozub
Date Created: 7/20/2021

The CodeWriter module of the VM translator built for project 8 
of the Nand to Tetris MOOC by The Hebrew University of Jerusalem.

The CodeWriter module from project 7 was extended to add
additional functionality. The following additional routines were 
implemented for the CodeWriter module:

  setFileName: Informs the CodeWriter that the translation of a new
               VM file has started (called by the main program of
               the VM translator).

  writeInit: Writes the assembly instructions that effect the
             bootstrap code that initializes the VM. This code must
             be placed at the beginning of the generated *.asm file.

  writeLabel: Writes assembly code that effects the 'label' command.

  writeGoto: Writes assembly code that effects the 'goto' command.

  writeIf: Writes assembly code that effects the 'if-goto' command.

  writeFunction: Writes assembly code that effects the 'function'
                 command.

  writeCall: Writes assembly code that effects the 'call' command.

  writeReturn: Writes assembly code the effects the 'return' command.

See nand2tetris.org/project08 for the project description.
"""

class CodeWriter():

  labelCnt = 0 #running count appended to labels to make them unique

  funcToCnt = {"empty": 0} #maps function to # of calls in function

  currFunc = "" #current function

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

  pshPopToAssemb = { #maps push/pop commands to hack assembly
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

  branchToAssembly = { #maps 'goto', 'if-goto', & 'label' commands to assembly
    "goto": lambda self, labelSym :
      ''.join([
        "@" + labelSym + "\n",
        "0;JMP\n"
      ]),

    "if-goto": lambda self, labelSym :
      ''.join([
        "@SP\n",
        "AM=M-1\n",
        "D=M\n",
        "@" + labelSym + "\n",
        "D;JNE\n"
      ]),
    
    "label": lambda self, labelSym :
      ''.join([
        "(" + labelSym + ")\n",
      ])
  }

  funcToAssembly = { #maps 'function', 'call', and 'return' commands to assembly
    "function": lambda self, funcSym, nVars, loopLabel, endLabel: 
      ''.join([
        "(" + funcSym + ")\n",
        "@" + nVars + "\n",
        "D=A\n",
        "(" + loopLabel + ")\n",
        "@" + endLabel + "\n",
        "D;JEQ\n",
        "@SP\n",
        "M=M+1\n",
        "A=M-1\n",
        "M=0\n",
        "D=D-1\n",
        "@" + loopLabel + "\n",
        "0;JMP\n",
        "(" + endLabel + ")\n"
      ]),

    "call": lambda self, funcSym, nArgs, returnLabel : 
      ''.join([
        "@" + returnLabel + "\n", # save return address
        "D=A\n",
        "@SP\n",
        "M=M+1\n",
        "A=M-1\n",
        "M=D\n",
        "@LCL\n", # save LCL
        "D=M\n",
        "@SP\n",
        "M=M+1\n",
        "A=M-1\n",
        "M=D\n",
        "@ARG\n", # save ARG
        "D=M\n",
        "@SP\n",
        "M=M+1\n",
        "A=M-1\n",
        "M=D\n",
        "@THIS\n", # save THIS
        "D=M\n",
        "@SP\n",
        "M=M+1\n",
        "A=M-1\n",
        "M=D\n",
        "@THAT\n", # save THAT
        "D=M\n",
        "@SP\n",
        "M=M+1\n",
        "A=M-1\n",
        "M=D\n",
        "@" + str(5 + int(nArgs)) + "\n", # ARG = SP-5-nArgs
        "D=A\n",
        "@SP\n",
        "D=M-D\n",
        "@ARG\n",
        "M=D\n",
        "@SP\n", # LCL = SP
        "D=M\n",
        "@LCL\n",
        "M=D\n",
        "@" + funcSym + "\n", # go to the function code
        "0;JMP\n",
        "(" + returnLabel + ")\n" # return label
      ]),

    "return": lambda self:
      ''.join([
        "@LCL\n", #save end of frame in register R13
        "D=M\n",
        "@R13\n",
        "M=D\n",
        "@5\n", #save return address to caller
        "A=D-A\n",
        "D=M\n",
        "@R14\n",
        "M=D\n",
        "@SP\n",#move return value to arg[0]
        "AM=M-1\n",
        "D=M\n",
        "@ARG\n",
        "A=M\n",
        "M=D\n",
        "D=A+1\n",#reposition stack pointer
        "@SP\n",
        "M=D\n",
        "@R13\n",#restore THAT
        "AM=M-1\n",
        "D=M\n",
        "@THAT\n",
        "M=D\n",
        "@R13\n",#restore THIS
        "AM=M-1\n",
        "D=M\n",
        "@THIS\n",
        "M=D\n",
        "@R13\n",#restore ARG
        "AM=M-1\n",
        "D=M\n",
        "@ARG\n",
        "M=D\n",
        "@R13\n",#restore LCL
        "AM=M-1\n",
        "D=M\n",
        "@LCL\n",
        "M=D\n",
        "@R14\n",#return to caller
        "A=M\n",
        "0;JMP\n"
      ])
  }

  initSP = ''.join([
    "@256\n", #set SP=256
    "D=A\n",
    "@SP\n",
    "M=D\n"
  ])

  callSysInit = funcToAssembly["call"](None, #assembly code to call Sys.init
                                       funcSym = "Sys.init",
                                       nArgs = "0",
                                       returnLabel = "Sys.init$ret.0")

  initCode = initSP + callSysInit #boostrap code

  def __init__(self, outpath):
    """Takes output filepath and returns the CodeWriter object that writes to that output file.
    
    :param str outpath: path to output file
    :return: CodeWriter object that writes to the output file
    :rtype: CodeWriter
    """

    self.file = open(outpath, "w")
    self.filePrefix = "" #input filename prefix

  def writeInit(self):
    """
    Write the bootstrap code to the output .asm file. The bootstrap
    code should be written to address 0 in ROM.

    :return: No return value
    """

    firstLine = "\n//boostrap code\n" #comment to indicate this is boostrap code

    translated = firstLine + self.initCode

    self.file.write(translated) #write to output file

  def setFileName(self, filePref):
    """
    Save the name of the file currently being translated.
    
    :return: No return value.
    """
    
    self.filePrefix = filePref

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

    translated = firstLine + self.pshPopToAssemb[command][segment](self, index)

    self.file.write(translated)

  def __getLabelSym(self, label):
    """
    If no 'function' directive has been encountered yet prepend
    "filePrefix." to label, where filePrefix is the name of the
    current file being translated without the extension, and
    return it.

    Otherwise, prepend "currFunc$" to label, where currFunc is 
    the current function being translated, and return it.
    
    Ex.

    If label == 'myLabel' and the current function being translated
    is 'myFunction', then this method would return: 
    "myFunction$myLabel".

    :param str label: The input label.
    :return: The label updated as described above.
    :rtype: str
    """

    labelSym = ""
    if self.currFunc == "": #function directive NOT encountered
      labelSym = self.filePrefix + "." + label
    else: #function directive encountered
      labelSym = self.currFunc + "$" + label

    return labelSym

  def writeLabel(self, label):
    """
    Translate a VM code 'label' command to hack assembly code and
    write it to the output file.

    :param str label: The argument of the 'label' command
    :return: No return value
    """

    #get appropriate symbol from label
    labelSym = self.__getLabelSym(label)

    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "label", label, "\n"])

    translated = firstLine + self.branchToAssembly["label"](self,labelSym) #translate to assembly

    self.file.write(translated)

  def writeGoto(self, label):
    """
    Translate the VM code 'goto' command to hack assembly code and 
    write it to the output file.
    
    :param str label: The argument of the 'goto' command.
    :return: No return value.
    """

    #get appropriate symbol from label
    labelSym = self.__getLabelSym(label)

    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "goto", label, "\n"])

    translated = firstLine + self.branchToAssembly["goto"](self,labelSym) #translate to assembly

    self.file.write(translated)

  def writeIf(self, label):
    """
    Translate the VM code 'if-goto' command to hack assembly code
    and write it to the output file.
    
    :param str label: The argument of the 'if-goto' command.
    :return: No return value.
    """

    #get appropriate symbol from label
    labelSym = self.__getLabelSym(label)

    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "if-goto", label, "\n"])

    #translate to assembly
    translated = firstLine + self.branchToAssembly["if-goto"](self,labelSym)

    self.file.write(translated)

  def writeFunction(self, functionName, numVars):
    """
    Translate the VM code 'function' command to hack assembly code
    and write it to the output file.
    
    :param str functionName: First argument of the 'function' command
                             (the name of the function).
    :param str numVars: Second argument of the 'function' command
                        (number of local variables for the function)
    :return: No return value.
    """

    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "function", functionName, numVars, "\n"])

    #unique names for labels assembly code
    loopLabel = "L" + str(self.labelCnt)
    endLabel = "L" + str(self.labelCnt + 1)
    self.labelCnt += 2

    #function label in assembly code
    funcSym = functionName

    #translate to assembly
    translated = firstLine + self.funcToAssembly["function"](self, funcSym, numVars, loopLabel, endLabel)

    self.file.write(translated)
    #make this function the current function
    self.currFunc = funcSym

  def writeCall(self, functionName, numArgs):
    """
    Translate the VM code 'call' command to hack assembly code
    and write it to the output file.
    
    :param str functionName: First argument of 'call' command
                             (function being called).
    :param str numArgs: Second argument of 'call' command
                        (number of arguments to the function)
    :return: No return value.
    """

    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "call", functionName, numArgs, "\n"])

    #return address
    returnLabel = ""

    #'function' directive NOT yet encountered
    if self.currFunc == "":
      returnLabel = self.filePrefix + "$ret." + str(self.funcToCnt["empty"])
      self.funcToCnt["empty"] += 1

    #'function' directive has been encountered
    else:
      i = 0
      currFunc = self.currFunc

      #first 'call' directive encountered in current function
      if currFunc not in self.funcToCnt:
        i = 0
        self.funcToCnt[currFunc] = i + 1
      #NOT first 'call' directive encountered in current function
      else:
        i = self.funcToCnt[currFunc]
        self.funcToCnt[currFunc] += 1

      #currFunc$ret.i -- currFunc = the current function; i = current number of calls within currFunc
      returnLabel = currFunc + "$ret." + str(i)
    
    funcSym = functionName
    #translate to assembly
    translated = firstLine + self.funcToAssembly["call"](self, funcSym, numArgs, returnLabel)

    self.file.write(translated)

  def writeReturn(self):
    """
    Translate the VM code 'return' command to hack assembly code
    and write it to the output file.
    
    :return: No return value.
    """

    #1st line is comment containing the command to be translated
    firstLine = "\n// return\n"

    #translate VM code to assembly
    translated = firstLine + self.funcToAssembly["return"](self)

    #write translated assembly code to file
    self.file.write(translated)

  def Close(self):
    """
    Close the output file.
    
    :return: No return value.
    """

    self.file.close()