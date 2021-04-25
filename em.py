class CPU:
	def __init__(self):
		self.mem = MEM()
		self.kernel = KERNEL()
	
	def load_proc(self, proc):
		for op in proc:
			self.mem.rom.append(op)
	
	def dump_mem(self):
		print('registers: ', self.mem.registers, '\n')
		print('rom: ', self.mem.rom, '\n')
		print('ram: ', self.mem.ram, '\n')
		print('stack: ', self.mem.stack, '\n')
	
	def run_proc(self):
		self.end_proc = 0
		while self.mem.registers['ESI'] < len(self.mem.rom):
			if(self.end_proc): break
			self.execute_op()
			self.mem.registers['ESI'] += 1
	
	def execute_op(self):
		op = self.mem.rom[self.mem.registers['ESI']][0:2]
		a1 = self.mem.rom[self.mem.registers['ESI']][2:4]
		a2 = self.mem.rom[self.mem.registers['ESI']][4:6]
		a3 = self.mem.rom[self.mem.registers['ESI']][6:8]
		if(self.mem.stack):
			self.mem.registers['ESP'] = self.mem.stack[-1]
		else:
			self.mem.registers['ESP'] = 0
		
		if(op == '0X'):
			self.dump_mem()
		
		if(op == '01'): #syscall
			self.kernel.call(self)
			
		elif(op == '02'): #mov
			if(a1[0] == 'G'):
				self.mem.registers[self.mem.reference[a1]] = self.mem.registers[self.mem.reference[a2]] if a2[0] == 'G' \
				else int(a2, 16)
				
		elif(op == '03'): #push
			if(a1[0] == 'G'):
				self.mem.stack.append(self.mem.registers[self.mem.reference[a1]])
			else:
				self.mem.stack.append(int(a1, 16))
				
		elif(op == '04'): #pop
			if(a1[0] == 'G'):
				self.mem.registers[self.mem.reference[a1]] = self.mem.stack.pop(-1)
				
		elif(op == '05'): #nop
			__import__('time').sleep(0.1);
			
		elif(op == '06'): #add
			if(a1[0] == 'G'):
				self.mem.registers[self.mem.reference[a1]] += self.mem.registers[self.mem.reference[a2]] if a2[0] == 'G' \
				else int(a2, 16)
				
		elif(op == '07'): #sub
			if(a1[0] == 'G'):
				self.mem.registers[self.mem.reference[a1]] -= self.mem.registers[self.mem.reference[a2]] if a2[0] == 'G' \
				else int(a2, 16)
				
		elif(op == '08'): #mul
			if(a1[0] == 'G'):
				self.mem.registers[self.mem.reference[a1]] *= self.mem.registers[self.mem.reference[a2]] if a2[0] == 'G' \
				else int(a2, 16)
				
		elif(op == '09'): #div
			if(a1[0] == 'G'):
				self.mem.registers[self.mem.reference[a1]] /= self.mem.registers[self.mem.reference[a2]] if a2[0] == 'G' \
				else int(a2, 16)
				
		elif(op == '0A'): #mod
			if(a1[0] == 'G'):
				self.mem.registers[self.mem.reference[a1]] %= self.mem.registers[self.mem.reference[a2]] if a2[0] == 'G' \
				else int(a2, 16)
				
		elif(op == '0B'): #smov
			self.mem.registers[self.mem.reference[a1]] = self.mem.registers[self.mem.reference[a1]] + chr(int(a2, 16))
			
		elif(op == '0C'): #spop
			self.mem.registers[self.mem.reference[a1]] = ''.join(list(self.mem.registers[self.mem.reference[a1]]) \
			[0:len(list(self.mem.registers[self.mem.reference[a1]])) - 1])
			
		elif(op == '0D'): #del
			if(type(self.mem.registers[self.mem.reference[a1]]) == int):
				self.mem.registers[self.mem.reference[a1]] = 0
			else:
				self.mem.registers[self.mem.reference[a1]] = ''
			
		elif(op == '0E'): #len
			self.mem.registers[self.mem.reference[a2]] = len(str(self.mem.registers[self.mem.reference[a1]]))
			
		elif(op == '0F'): #label
			self.mem.ram['labels'][int(a1, 16)] = int(a2, 16)
			
		elif(op == '10'): #jmp
			self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
			
		elif(op == '11'): #je
			if(a3[0] == 'G'):
				if(self.mem.registers[self.mem.reference[a2]] == self.mem.registers[self.mem.reference[a3]]):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
			else:
				if(self.mem.registers[self.mem.reference[a2]] == int(a3, 16)):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
					
		elif(op == '12'): #jne
			if(a3[0] == 'G'):
				if(self.mem.registers[self.mem.reference[a2]] != self.mem.registers[self.mem.reference[a3]]):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
			else:
				if(self.mem.registers[self.mem.reference[a2]] != int(a3, 16)):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
					
		elif(op == '13'): #jl
			if(a3[0] == 'G'):
				if(self.mem.registers[self.mem.reference[a2]] < self.mem.registers[self.mem.reference[a3]]):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
			else:
				if(self.mem.registers[self.mem.reference[a2]] < int(a3, 16)):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
					
		elif(op == '14'): #jle
			if(a3[0] == 'G'):
				if(self.mem.registers[self.mem.reference[a2]] <= self.mem.registers[self.mem.reference[a3]]):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
			else:
				if(self.mem.registers[self.mem.reference[a2]] <= int(a3, 16)):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
					
		elif(op == '15'): #jg
			if(a3[0] == 'G'):
				if(self.mem.registers[self.mem.reference[a2]] > self.mem.registers[self.mem.reference[a3]]):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
			else:
				if(self.mem.registers[self.mem.reference[a2]] > int(a3, 16)):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
					
		elif(op == '16'): #jge
			if(a3[0] == 'G'):
				if(self.mem.registers[self.mem.reference[a2]] >= self.mem.registers[self.mem.reference[a3]]):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
			else:
				if(self.mem.registers[self.mem.reference[a2]] >= int(a3, 16)):
					self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
					
		elif(op == '17'): #jz
			if(self.mem.registers[self.mem.reference[a2]] == 0):
				self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]
				
		elif(op == '18'): #jnz
			if(self.mem.registers[self.mem.reference[a2]] != 0):
				self.mem.registers['ESI'] = self.mem.ram['labels'][int(a1, 16)]

class KERNEL:
	def call(self, processor):
		self.eax = processor.mem.registers['EAX'] # dont use for writing
		self.ebx = processor.mem.registers['EBX'] # use proccessor for updating registers
		self.ecx = processor.mem.registers['ECX']
		self.edx = processor.mem.registers['EDX']
		self.de = processor.mem.registers['DE']
		self.df = processor.mem.registers['DF']
		
		if(self.eax == 1):   #print
			if(not int(self.ecx)):
				print(self.ebx)
			else:
				print(self.de)

		elif(self.eax == 2): #read file
			processor.mem.registers['DE'] = open(self.de).read()

		elif(self.eax == 3): #write file
			if(self.ecx == 0):
				open(self.de, 'w').write(self.df)
			else:
				open(self.de, 'a').write(self.df)

		elif(self.eax == 4): #write ram
			if(self.ecx == 0):
				processor.mem.ram[self.edx] = self.ebx
			else:
				processor.mem.ram[self.edx] = self.de
		
		elif(self.eax == 5): #read ram
			if(self.ecx == 0):
				processor.mem.registers['EAX'] = processor.mem.ram[self.edx]
			else:
				processor.mem.registers['DE'] = processor.mem.ram[self.edx]
		
		elif(self.eax == 6): #end process
			processor.end_proc = 1

class MEM:
	def __init__(self):
		self.registers = {
			'EAX': 0, #for syscalls
			'EBX': 0,
			'ECX': 0,
			'EDX': 0,
			
			'FAX': 0,
			'FBX': 0,
			'ESP': 0, #stack pointer
			'ESI': 0, #instruction pointer
			
			'DA': 0,  #general
			'DB': 0,
			'DC': 0,
			'DD': 0,
			'DE': '',
			'DF': '',
			'DG': '',
			'DH': ''
		}
		self.reference = {
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
			'GF': 'DH',
		}
		self.rom = []
		self.stack = []
		self.ram = {'labels': {}}

cpu = CPU()
cpu.load_proc([i for i in open('a.out').read().split(' ')])
cpu.run_proc()