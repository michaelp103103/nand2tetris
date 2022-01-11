// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@8191
D=A
@SCREEN
D=D+A
@last
M=D	// last address in memory map

(LOOP)
	@SCREEN
	D=A
	@addr
	M=D	// addr = screen base address

	@color
	M=0	// M=0 for white screen

	@KBD
	D=M
	@FILL_SCREEN
	D;JEQ	// if KBD == 0, goto FILL_SCREEN 

	@color
	M=-1	// M=-1 for black screen

	(FILL_SCREEN)
		@addr
		D=M
		@last
		D=D-M
		@LOOP
		D;JGT	// if addr > last, goto LOOP

		@color
		D=M
		@addr
		A=M
		M=D	// RAM[addr] = color
	
		@addr
		M=M+1	// addr = addr + 1

		@FILL_SCREEN
		0;JMP	// goto FULL_SCREEN		