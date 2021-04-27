## Em (esolang)

***GOTO AND JMP ARE CURRENTLY BROKEN, WILL BE FIXED WHEN I STOP PROCRASTINATING***

esoteric language (very) loosely based on cpu architecture. 

assembly like language is compiled into byte machine code that is loaded into an emulated rom. (ex. 02G41500)

-------------------------------------------------------------------------------------------------------------

## Todo: 

- [ ] fix goto and jmp
- [ ] add more kernel calls
- [x] - timing and clock
- [ ] - http requests
- [x] - os things (make folders, delete, windows.h things)
- [ ] - sockets
- [ ] change compiler to use octal instead of hex
- [ ] change sleep to use milliseconds (has to use octal first)
- [ ] add more features inspired by intel syntax
- [ ] - pointers


- [ ] write a c compiler in it (Kapp)

-------------------------------------------------------------------------------------------------------------

## Documentation: 

instruction syntax: **\[opcode\] \[arg1\] \[arg2\] \[arg3\]** *(ex: mov eax ecx)*

##	Instructions:


 * mov: \[register to move to\] \[register or value to move] (ex: mov eax 5) (ex: mov df de)
 	* moves an integer value to a register
 	
 * smov: \[register to move to] \[char to add] \[mode] (ex: smov de a 0) (ex: smov de 65 1)
 	* concatenates a char to the end of a string register (mode 0: char literal, 1: ascii char code)
 	
 * spop: \[register to pop] \[mode] (ex: spop de 0)
 	* removes the first or last character depending on the mode (mode 0: last, 1: first)
 	
 * syscall: (ex: syscall)
 	* calls the kernel
 	
 * push: \[register or value to push to stack] (ex: push eax)
 	* pushes a value to the top of the stack
 	
 * pop: \[register to pop to] (ex: pop ebx)
 	* pops the top of the stack to a register
 	
 * add: \[register to add to] \[register or value to add] (ex: add ecx 3)
 	* adds the second value to the first
 	
 * sub: \[register to subtract to] \[register or value to subtract] (ex: sub ecx 3)
 	* subtracts the second value to the first
 	
 * mul: \[register to multiply to] \[register or value to multiply] (ex: mul ecx 3)
 	* multiplies the second value to the first
 	
 * div: \[register to divide to] \[register or value to divide] (ex: div ecx 3)
 	* divides the second value to the first
 	
 * mod: \[register to modulus to] \[register or value to modulus] (ex: add ecx 3)
 	* modulus the second value to the first
 	
 * nop: (ex: nop)
 	* pauses execution for 0.1 seconds
 	
 * del: \[register to empty] (ex: del eax)
 	* empties a register
 	
 * len: \[register to measure] \[destination of the length] (ex: len de) (ex: len eax)
 	* gets the length of a string or int register
 	
 * lbl: \[name of label (int 0-255)] (ex: lbl 1)
 	* sets a label
 	
 * jmp: \[label to jump to] (ex: jmp 1)
 	* jumps to a label
 	
 * je: \[label to jump to] \[first value (register)] \[second value (int or register)] (ex: je 1 eax 10)
 	* jumps to a label if the two values are equal
 	
 * jne: \[label to jump to] \[first value (register)] \[second value (int or register)] (ex: jne 1 eax 10)
 	* jumps to a label if the two values are not equal
 	
 * jl: \[label to jump to] \[first value (register)] \[second value (int or register)] (ex: jl 1 eax 10)
 	* jumps to a label if the first value is less than the second
 	
 * jle: \[label to jump to] \[first value (register)] \[second value (int or register)] (ex: jle 1 eax 10)
 	* jumps to a label if the first value is less than or equal to the second
 	
 * jg: \[label to jump to] \[first value (register)] \[second value (int or register)] (ex: jg 1 eax 10)
 	* jumps to a label if the first value is greater than the second
 	
 * jge: \[label to jump to] \[first value (register)] \[second value (int or register)] (ex: jge 1 eax 10)
 	* jumps to a label if the first value is greater than or equal to the second
 	
 * jz: \[label to jump to] \[value (register)] (ex: jz 1 eax)
 	* jumps to a label if the value is zero
 	
 * jnz: \[label to jump to] \[value (register)] (ex: jnz 1 eax)
 	* jumps to a label if the value is not zero



##	Kernel Functions: 

eax | name | ebx | ecx | edx | de | df
-|-|-|-|-|-|-
1 | print 	|	value   |	mode	|	-	|		-		|			string to print
2	|	read file|	-		|	-	|		-	|		file name/output|	-
3 	|	write file|	- 	|		mode|		-|			file name 	|		string to write
4 	|	write ram|	value 	|	mode	|	address	|	value	|			-
5 	|	read ram |	-		 |	mode|		address	|	- 	|				-
6 	|	end proc |	- 	|		- 	|		-		|	- 	|				-
7 	|	system time 	|	- 		|	- 	|	- 	|		-	 |				-
8	|	sleep	|	time (milliseconds)		|	-	|	-	|	-	|	-
9 	|	make directory 	|	- 		|	- 	|	- 	|		folder name	 |				-
10 	|	delete file 	|	- 		|	- 	|	- 	|		file name	 |				-
11 	|	delete folder 	|	- 		|	- 	|	- 	|		folder name	 |				-


 * `print`: prints a value to the command line
 	* __eax__: 1
 	* __ebx__: value to print (int)
 	* __ecx__: 0/1 (mode to print, 0: int (ebx), 1: string (de))
 	* __de__: value to print (string)

 * `read file`: reads a file to a register
 	* __eax__: 2
 	* __de__: file name/output

 * `write file`: writes a string to a file
 	* __eax__: 3
 	* __ecx__: mode (mode 0: overwrite, 1: append)
 	* __de__: file name
 	* __df__: string to write
 
 * `write ram`: writes a value to the ram
 	* __eax__: 4
 	* __ebx__: value (int)
 	* __ecx__: mode (mode 0: int, 1: string)
 	* __edx__: address
 	* __de__: value (string)
 
 * `read ram`: reads a value from the ram
 	* __eax__: 5
 	* __edx__: address
 	* __edx__: type (mode 0: int (to eax), 1: string (to de))
 
 * `end process`: ends process early
 	* __eax__: 6
 
 * `system time`: get the current time (returned to eax)
 	* __eax__: 7
 
 * `sleep`: sleep for an amount of seconds
 	* __eax__: 8
 	* __ebx__: seconds

 * `make directory`: make a folder
 	* __eax__: 9
 	* __de__: folder name

 * `delete file`: remove a file
 	* __eax__: 10
 	* __de__: folder name

 * `delete directory`: remove a folder
 	* __eax__: 11
 	* __de__: folder name

--------------------------------------------------------------------------------------------------

#### Machine Code: 
Each line of assembly is translated into 8 bytes. Each group is split into four groups of two.

1st group: opcode\
2nd-4th group: arguments in hex

If the first bit in an argument is `G`, it refers to the registers:\
G0: eax\
G1: ebx\
...\
GE: dg\
GF: dh

--------------------------------------------------------------------------------------------------

