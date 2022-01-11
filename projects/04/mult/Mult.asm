// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

@0
D=A
@product
M=D	// product = 0

@1
D=A
@i
M=D	// i = 1

	(LOOP)	// RAM[product] = RAM[R1] + RAM[R1] + .. + RAM[R1] (RAM[R0] times)
		@i
		D=M
		@R0
		D=D-M
		@SAVE
		D;JGT	// goto SAVE if i>R0

		@i
		M=M+1	// i = i + 1

		@R1
		D=M
		@product
		M=D+M	// product = product + R1

		@LOOP
		0;JMP	// return to beginning of loop

	(SAVE)
		@product
		D=M
		@R2
		M=D	// RAM[R2] = RAM[product]

		@END
		0;JMP	// goto END

	(END)
		@END
		0;JMP	// loops forever when finished