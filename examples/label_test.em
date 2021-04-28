smov de e 0
smov de v 0
smov de e 0
smov de n 0

mov eax 1
mov ebx 10

lbl 1
push ebx
mod ebx 2
jz 2 ebx
jmp 3

sub ebx 1
jnz 1 ebx
jmp 4

lbl 2
pop da
mov ecx 1
syscall
jmp 1

lbl 3
pop da
mov ecx 0
syscall
jmp 1


lbl 4
syscall