code = open('examples/even.em', 'r').read().lower().split('\n')
machine = []

reference = {
    'G0': 'EAX', 
    'G1': 'EBX',
    'G2': 'ECX',
    'G3': 'EDX',
    'G4': 'FAX', 
    'G5': 'FBX',
    'G6': 'ESP',
    'G7': 'ESI',
    'G8': 'DA', 
    'G9': 'DB',
    'GA': 'DC',
    'GB': 'DD',
    'GC': 'DE', 
    'GD': 'DF',
    'GE': 'DG',
    'GF': 'DH'
}

reference = {y.lower():x for x,y in reference.items()}

for line in code:
    if(line == ''):
        pass
    
    args = line.split(' ')
    
    if(args[0] == 'syscall'):
        machine.append('01000000')
    
    if(args[0] == 'x'):
        machine.append('0X000000')
    
    if(args[0] == 'mov'):
        ins = []
        ins.append('02' + reference[args[1]])
        if(args[2] in reference.keys()):
            ins.append(reference[args[2]] + '00')
        else:
            ins.append(hex(int(args[2]))[2:].zfill(2) + '00')
        machine.append(''.join(ins))
    
    if(args[0] == 'push'):
        ins = []
        if(args[1] in reference.keys()):
            ins.append('03' + reference[args[1]] + '0000')
        else:
            ins.append('03' + hex(int(args[2]))[2:].zfill(2) + '0000')
        machine.append(''.join(ins))
    
    if(args[0] == 'pop'):
        ins = []
        ins.append('04' + reference[args[1]] + '0000')
        machine.append(''.join(ins))
    
    if(args[0] == 'nop'):
        machine.append('05000000')
    
    if(args[0] == 'add'):
        ins = []
        if(args[1] in reference.keys()):
            ins.append('06' + reference[args[1]])
        if(args[2] in reference.keys()):
            ins.append(reference[args[2]] + '00')
        else:
            ins.append(hex(int(args[2]))[2:].zfill(2) + '00')
        machine.append(''.join(ins))
    
    if(args[0] == 'sub'):
        ins = []
        if(args[1] in reference.keys()):
            ins.append('07' + reference[args[1]])
        if(args[2] in reference.keys()):
            ins.append(reference[args[2]] + '00')
        else:
            ins.append(hex(int(args[2]))[2:].zfill(2) + '00')
        machine.append(''.join(ins))
    
    if(args[0] == 'mul'):
        ins = []
        if(args[1] in reference.keys()):
            ins.append('08' + reference[args[1]])
        if(args[2] in reference.keys()):
            ins.append(reference[args[2]] + '00')
        else:
            ins.append(hex(int(args[2]))[2:].zfill(2) + '00')
        machine.append(''.join(ins))
    
    if(args[0] == 'div'):
        ins = []
        if(args[1] in reference.keys()):
            ins.append('09' + reference[args[1]])
        if(args[2] in reference.keys()):
            ins.append(reference[args[2]] + '00')
        else:
            ins.append(hex(int(args[2]))[2:].zfill(2) + '00')
        machine.append(''.join(ins))
    
    if(args[0] == 'mod'):
        ins = []
        if(args[1] in reference.keys()):
            ins.append('0A' + reference[args[1]])
        if(args[2] in reference.keys()):
            ins.append(reference[args[2]] + '00')
        else:
            ins.append(hex(int(args[2]))[2:].zfill(2) + '00')
        machine.append(''.join(ins))
    
    if(args[0] == 'smov'):
        ins = []
        if(int(args[3])):
            ins.append('0B' + reference[args[1]] + hex(int(args[2]))[2:].zfill(2) + '00')
        else:
            ins.append('0B' + reference[args[1]] + hex(ord(args[2]))[2:].zfill(2) + '00')
        machine.append(''.join(ins))
    
    if(args[0] == 'spop'):
        ins = []
        ins.append('0C' + reference[args[1]] + '0000')
        machine.append(''.join(ins))
    
    if(args[0] == 'del'):
        ins = []
        ins.append('0D' + reference[args[1]] + '0000')
        machine.append(''.join(ins))
    
    if(args[0] == 'len'):
        ins = []
        ins.append('0E' + reference[args[1]] + reference[args[2]] + '00')
        machine.append(''.join(ins))
    
    if(args[0] == 'lbl'):
        ins = []
        ins.append('0F' + hex(int(args[1]))[2:].zfill(2) + '0000')
        machine.append(''.join(ins))
    
    if(args[0] == 'jmp'):
        ins = []
        ins.append('10' + hex(int(args[1]))[2:].zfill(2) + '0000')
        machine.append(''.join(ins))
    
    if(args[0] == 'je'):
        ins = []
        if(args[3] in reference.keys()):
            ins.append('11' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + reference[args[3]])
        else:
            ins.append('11' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + hex(int(args[3]))[2:].zfill(2))
        machine.append(''.join(ins))
    
    if(args[0] == 'jne'):
        ins = []
        if(args[3] in reference.keys()):
            ins.append('12' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + reference[args[3]])
        else:
            ins.append('12' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + hex(int(args[3]))[2:].zfill(2))
        machine.append(''.join(ins))
    
    if(args[0] == 'jl'):
        ins = []
        if(args[3] in reference.keys()):
            ins.append('13' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + reference[args[3]])
        else:
            ins.append('13' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + hex(int(args[3]))[2:].zfill(2))
        machine.append(''.join(ins))
    
    if(args[0] == 'jle'):
        ins = []
        if(args[3] in reference.keys()):
            ins.append('14' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + reference[args[3]])
        else:
            ins.append('14' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + hex(int(args[3]))[2:].zfill(2))
        machine.append(''.join(ins))
    
    if(args[0] == 'jg'):
        ins = []
        if(args[3] in reference.keys()):
            ins.append('15' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + reference[args[3]])
        else:
            ins.append('15' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + hex(int(args[3]))[2:].zfill(2))
        machine.append(''.join(ins))
    
    if(args[0] == 'jge'):
        ins = []
        if(args[3] in reference.keys()):
            ins.append('16' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + reference[args[3]])
        else:
            ins.append('16' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + hex(int(args[3]))[2:].zfill(2))
        machine.append(''.join(ins))
    
    if(args[0] == 'jz'):
        ins = []
        ins.append('17' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + '00')
        machine.append(''.join(ins))
    
    if(args[0] == 'jnz'):
        ins = []
        ins.append('18' + hex(int(args[1]))[2:].zfill(2) + reference[args[2]] + '00')
        machine.append(''.join(ins))

i = 0
while i < len(machine):
    if(machine[i][0:2] == '0F'):
        j = machine[i][0:4] + hex(int(i))[2:].zfill(2) + machine[i][6:8]
        machine.insert(0, j)
        print(i, j)
        del machine[i + 1]
    i += 1

open('a.out', 'w').write(' '.join(machine))