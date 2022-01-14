class CodeWriter():

  labelCnt = 0

  funcToCnt = {"empty": 0}

  currFunc = ""

  arithToAssembly = {
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

  pshPopToAssemb = {
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

  branchToAssembly = {
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

  funcToAssembly = {
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
        "@" + str(5 - int(nArgs)) + "\n", # ARG = SP-5-nArgs
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

  initCode = ''.join([
    "@256\n", #set SP=256
    "D=A\n",
    "@SP\n",
    "M=D\n",
    "@Sys.init\n", # go to Sys.init
    "0;JMP\n"
  ])

  def __init__(self, outpath):
    self.file = open(outpath, "w")
    self.filePrefix = "" #input filename prefix

  #generate bootstrap code in asm file
  def writeInit(self):
    firstLine = "\n//boostrap code\n" #comment to indicate this is boostrap code

    translated = firstLine + self.initCode

    self.file.write(translated) #write to output file

  #sets name of file being translated
  def setFileName(self, path):
    self.filePrefix = path.split("/")[-1][:-3]

  def writeArithmetic(self, command):
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
    
    self.file.write(translated)

  def WritePushPop(self, command, segment, index):
    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", command, segment, index, "\n"])

    translated = firstLine + self.pshPopToAssemb[command][segment](self, index)

    self.file.write(translated)

  #get proper label
  def __getLabelSym(self, label):
    labelSym = ""
    if self.currFunc == "":
      labelSym = self.filePrefix + "." + label
    else:
      labelSym = self.currFunc + "$" + label

    return labelSym

  def writeLabel(self, label):
    labelSym = self.__getLabelSym(label)

    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "label", label, "\n"])

    translated = firstLine + self.branchToAssembly["label"](self,labelSym)

    self.file.write(translated)

  def writeGoto(self, label):
    labelSym = self.__getLabelSym(label)

    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "goto", label, "\n"])

    translated = firstLine + self.branchToAssembly["goto"](self,labelSym)

    self.file.write(translated)

  def writeIf(self, label):
    labelSym = self.__getLabelSym(label)

    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "if-goto", label, "\n"])

    translated = firstLine + self.branchToAssembly["if-goto"](self,labelSym)

    self.file.write(translated)

  def writeFunction(self, functionName, numVars):
    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "function", functionName, numVars, "\n"])

    #unique names for labels assembly code
    loopLabel = "L" + str(self.labelCnt)
    endLabel = "L" + str(self.labelCnt + 1)
    self.labelCnt += 2

    #function label in assembly code
    funcSym = functionName

    translated = firstLine + self.funcToAssembly["function"](self, funcSym, numVars, loopLabel, endLabel)

    self.file.write(translated)
    #make this function the current function
    self.currFunc = funcSym

  def writeCall(self, functionName, numArgs):
    #1st line is comment containing the command to be translated
    firstLine = " ".join(["\n//", "call", functionName, numArgs, "\n"])

    #return address
    returnLabel = ""

    if self.currFunc == "":
      returnLabel = self.filePrefix + "$ret." + str(self.funcToCnt["empty"])
      self.funcToCnt["empty"] += 1

    else:
      i = 0
      currFunc = self.currFunc

      if currFunc not in self.funcToCnt:
        i = 0
        self.funcToCnt[currFunc] = i + 1
      else:
        i = self.funcToCnt[currFunc]
        self.funcToCnt[currFunc] += 1

      returnLabel = currFunc + "$ret." + str(i)
    
    funcSym = functionName
    translated = firstLine + self.funcToAssembly["call"](self, funcSym, numArgs, returnLabel)

    self.file.write(translated)

  def writeReturn(self):
    #1st line is comment containing the command to be translated
    firstLine = "\n// return\n"

    #translate VM code to assembly
    translated = firstLine + self.funcToAssembly["return"](self)

    #write translated assembly code to file
    self.file.write(translated)

  #closes output file
  def Close(self):
    self.file.close()