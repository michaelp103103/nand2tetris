
// function Sys.init 0 
(Sys.init)
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

// push constant 4000 
@4000
D=A
@SP
M=M+1
A=M-1
M=D

// pop pointer 0 
@SP
AM=M-1
D=M
@THIS
M=D

// push constant 5000 
@5000
D=A
@SP
M=M+1
A=M-1
M=D

// pop pointer 1 
@SP
AM=M-1
D=M
@THAT
M=D

// call Sys.main 0 
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
@Sys.main
0;JMP
(Sys.init$ret.0)

// pop temp 1 
@SP
AM=M-1
D=M
@6
M=D

// label LOOP 
(Sys.init$LOOP)

// goto LOOP 
@Sys.init$LOOP
0;JMP

// function Sys.main 5 
(Sys.main)
@5
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

// push constant 4001 
@4001
D=A
@SP
M=M+1
A=M-1
M=D

// pop pointer 0 
@SP
AM=M-1
D=M
@THIS
M=D

// push constant 5001 
@5001
D=A
@SP
M=M+1
A=M-1
M=D

// pop pointer 1 
@SP
AM=M-1
D=M
@THAT
M=D

// push constant 200 
@200
D=A
@SP
M=M+1
A=M-1
M=D

// pop local 1 
@LCL
D=M
@1
D=D+A
@SP
A=M
M=D
@SP
AM=M-1
D=M
A=A+1
A=M
M=D

// push constant 40 
@40
D=A
@SP
M=M+1
A=M-1
M=D

// pop local 2 
@LCL
D=M
@2
D=D+A
@SP
A=M
M=D
@SP
AM=M-1
D=M
A=A+1
A=M
M=D

// push constant 6 
@6
D=A
@SP
M=M+1
A=M-1
M=D

// pop local 3 
@LCL
D=M
@3
D=D+A
@SP
A=M
M=D
@SP
AM=M-1
D=M
A=A+1
A=M
M=D

// push constant 123 
@123
D=A
@SP
M=M+1
A=M-1
M=D

// call Sys.add12 1 
@Sys.main$ret.0
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
@4
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
0;JMP
(Sys.main$ret.0)

// pop temp 0 
@SP
AM=M-1
D=M
@5
M=D

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

// push local 2 
@LCL
D=M
@2
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D

// push local 3 
@LCL
D=M
@3
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D

// push local 4 
@LCL
D=M
@4
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

//add
@SP
AM=M-1
D=M
A=A-1
M=D+M

//add
@SP
AM=M-1
D=M
A=A-1
M=D+M

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

// function Sys.add12 0 
(Sys.add12)
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

// push constant 4002 
@4002
D=A
@SP
M=M+1
A=M-1
M=D

// pop pointer 0 
@SP
AM=M-1
D=M
@THIS
M=D

// push constant 5002 
@5002
D=A
@SP
M=M+1
A=M-1
M=D

// pop pointer 1 
@SP
AM=M-1
D=M
@THAT
M=D

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

// push constant 12 
@12
D=A
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
