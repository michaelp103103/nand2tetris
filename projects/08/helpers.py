"""
Description
"""

def translate_file(parser, codeWriter):
  while parser.hasMoreCommands():
    parser.advance()
    commType = parser.commandType()

    if commType == parser.cArithmetic:
      codeWriter.writeArithmetic(parser.arg1())

    elif commType == parser.cPop:
      codeWriter.WritePushPop("pop", parser.arg1(), parser.arg2())
    
    elif commType == parser.cPush:
      codeWriter.WritePushPop("push", parser.arg1(), parser.arg2())

    elif commType == parser.cLabel:
      codeWriter.writeLabel(parser.arg1())
    
    elif commType == parser.cGoto:
      codeWriter.writeGoto(parser.arg1())

    elif commType == parser.cIf:
      codeWriter.writeIf(parser.arg1())

    elif commType == parser.cFunction:
      codeWriter.writeFunction(parser.arg1(), parser.arg2())

    elif commType == parser.cCall:
      codeWriter.writeCall(parser.arg1(), parser.arg2())

    elif commType == parser.cReturn:
      codeWriter.writeReturn()