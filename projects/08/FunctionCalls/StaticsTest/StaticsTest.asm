
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

// function Class1.set 0 
(Class1.set)
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

// pop static 0 
@SP
AM=M-1
D=M
@Class1.0
M=D

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

// pop static 1 
@SP
AM=M-1
D=M
@Class1.1
M=D

// push constant 0 
@0
D=A
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

// function Class1.get 0 
(Class1.get)
@0
D=A
(L2)
@L3
D;JEQ
@SP
M=M+1
A=M-1
M=0
D=D-1
@L2
0;JMP
(L3)

// push static 0 
@Class1.0
D=M
@SP
M=M+1
A=M-1
M=D

// push static 1 
@Class1.1
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

// function Class2.set 0 
(Class2.set)
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

// pop static 0 
@SP
AM=M-1
D=M
@Class2.0
M=D

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

// pop static 1 
@SP
AM=M-1
D=M
@Class2.1
M=D

// push constant 0 
@0
D=A
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

// function Class2.get 0 
(Class2.get)
@0
D=A
(L6)
@L7
D;JEQ
@SP
M=M+1
A=M-1
M=0
D=D-1
@L6
0;JMP
(L7)

// push static 0 
@Class2.0
D=M
@SP
M=M+1
A=M-1
M=D

// push static 1 
@Class2.1
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

// function Sys.init 0 
(Sys.init)
@0
D=A
(L8)
@L9
D;JEQ
@SP
M=M+1
A=M-1
M=0
D=D-1
@L8
0;JMP
(L9)

// push constant 6 
@6
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 8 
@8
D=A
@SP
M=M+1
A=M-1
M=D

// call Class1.set 2 
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
@7
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Sys.init$ret.0)

// pop temp 0 
@SP
AM=M-1
D=M
@5
M=D

// push constant 23 
@23
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 15 
@15
D=A
@SP
M=M+1
A=M-1
M=D

// call Class2.set 2 
@Sys.init$ret.1
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
@7
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Sys.init$ret.1)

// pop temp 0 
@SP
AM=M-1
D=M
@5
M=D

// call Class1.get 0 
@Sys.init$ret.2
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
@Class1.get
0;JMP
(Sys.init$ret.2)

// call Class2.get 0 
@Sys.init$ret.3
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
@Class2.get
0;JMP
(Sys.init$ret.3)

// label WHILE 
(Sys.init$WHILE)

// goto WHILE 
@Sys.init$WHILE
0;JMP
