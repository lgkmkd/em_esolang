mov da 10
mov db 0

lbl 1
dec da
jnz 1 da
jmp 2

lbl 2
inc db
jne 2 db 10
memdump