
//boostrap code
@256
D=A
@SP
M=D
@Sys.init
0;JMP

// function SimpleFunction.test 2 
(SimpleFunction.test)
@2
D=A
(L0)
@L1
D;JEQ
@SP
M=M+1
A=M-1
M=0
D=D-1
@L0
0;JMP
(L1)

// push local 0 
@LCL
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D

// push local 1 
@LCL
D=M
@1
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D

//add
@SP
AM=M-1
D=M
A=A-1
M=D+M

//not
@SP
A=M-1
M=!M

// push argument 0 
@ARG
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D

//add
@SP
AM=M-1
D=M
A=A-1
M=D+M

// push argument 1 
@ARG
D=M
@1
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D

//sub
@SP
AM=M-1
D=M
A=A-1
M=M-D

// return
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=A+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
