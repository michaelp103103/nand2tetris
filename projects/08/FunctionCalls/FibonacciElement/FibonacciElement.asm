
//boostrap code
@256
D=A
@SP
M=D
@Sys.init$ret.0
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$ret.0)

// function Main.fibonacci 0 
(Main.fibonacci)
@0
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

// push constant 2 
@2
D=A
@SP
M=M+1
A=M-1
M=D

//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@L2
D;JLT
D=0
@L3
0;JMP
(L2)
D=-1
(L3)
@SP
A=M-1
M=D

// if-goto IF_TRUE 
@SP
AM=M-1
D=M
@Main.fibonacci$IF_TRUE
D;JNE

// goto IF_FALSE 
@Main.fibonacci$IF_FALSE
0;JMP

// label IF_TRUE 
(Main.fibonacci$IF_TRUE)

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

// label IF_FALSE 
(Main.fibonacci$IF_FALSE)

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

// push constant 2 
@2
D=A
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

// call Main.fibonacci 1 
@Main.fibonacci$ret.0
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.0)

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

// push constant 1 
@1
D=A
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

// call Main.fibonacci 1 
@Main.fibonacci$ret.1
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)

//add
@SP
AM=M-1
D=M
A=A-1
M=D+M

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

// function Sys.init 0 
(Sys.init)
@0
D=A
(L4)
@L5
D;JEQ
@SP
M=M+1
A=M-1
M=0
D=D-1
@L4
0;JMP
(L5)

// push constant 4 
@4
D=A
@SP
M=M+1
A=M-1
M=D

// call Main.fibonacci 1 
@Sys.init$ret.0
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Sys.init$ret.0)

// label WHILE 
(Sys.init$WHILE)

// goto WHILE 
@Sys.init$WHILE
0;JMP
