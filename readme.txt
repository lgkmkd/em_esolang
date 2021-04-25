esoteric language (very) loosely based on cpu architecture. 

language is compiled into byte machine code that is loaded into rom. (ex. 02G41500)

-----------------------------------------------------------------------------------------

machine code: 

8 bits are split into four groups of two
1st group: opcode
2nd-4th group: arguments in hex

if the first bit in an argument is G, it refers to the registers:

G0: eax
G1: ebx
...
GE: dg
GF: dh

-----------------------------------------------------

todo:

- fix labels and jumps
- improve kernel
- 