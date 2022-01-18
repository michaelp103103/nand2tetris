"""
Author: Michael Piskozub
Date Created: 7/20/2021

Helper functions for the VM translator modules.
"""

def translate_file(parser, codeWriter):
  """
  Translate an entire VM code file (.vm) to a hack assembly 
  code file (.asm).
  
  :param Parser parser: Parser object for the input .vm file 
                        being translated.
  :param CodeWriter codeWriter: CodeWriter object for the
                                output .asm file.
  """

  #translate all commands to assembly and write to output file
  while parser.hasMoreCommands():
    parser.advance() #go to next command
    commType = parser.commandType() #get command type

    if commType == parser.cArithmetic: #arithmetic/logical command
      codeWriter.writeArithmetic(parser.arg1())

    elif commType == parser.cPop: #pop command
      codeWriter.WritePushPop("pop", parser.arg1(), parser.arg2())
    
    elif commType == parser.cPush: #push command
      codeWriter.WritePushPop("push", parser.arg1(), parser.arg2())

    elif commType == parser.cLabel: #label command
      codeWriter.writeLabel(parser.arg1())
    
    elif commType == parser.cGoto: #goto command
      codeWriter.writeGoto(parser.arg1())

    elif commType == parser.cIf: #if-goto command
      codeWriter.writeIf(parser.arg1())

    elif commType == parser.cFunction: #function command
      codeWriter.writeFunction(parser.arg1(), parser.arg2())

    elif commType == parser.cCall: #call command
      codeWriter.writeCall(parser.arg1(), parser.arg2())

    elif commType == parser.cReturn: #return command
      codeWriter.writeReturn()