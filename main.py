import time
pc = 0x0
clockSpeed = 4
register = {
    0x0: 0x00, #A 0x0
    0x1: 0x00, #B 0x1
    0x2: 0x00, #C 0x2
    0x3: 0x00, #D 0x3
}
#-------------- Program
program = [
    0x001,
    0x101,
    0x000,
    0x201,
    0x110,
    0x131,
    0x503,
    0x402
]
#-------------- Program

while pc < len(program):
    instr = (program[pc] >> 8) & 0x0F
    opcode = program[pc] & 0xFF 
    HighOpcode = (opcode >> 4) & 0x0F
    LowOpcode = opcode & 0x0F

    if instr == 0x0: 
        register[0x0] = opcode
    elif instr == 0x1:
        register[LowOpcode] = register[HighOpcode]
    elif instr == 0x2:
        register[0x3] = register[HighOpcode] + register[LowOpcode]
    elif instr == 0x3:
        register[0x3] = register[LowOpcode] - register[HighOpcode]
    elif instr == 0x4:
        pc = opcode
    elif instr == 0x5:
        print(register[opcode])
    elif instr == 0x6:
        print("Halting...")
        exit()
    #print(f"A: {register[0x0]}, B: {register[0x1]}, C: {register[0x2]}, D: {register[0x3]}, PC: {pc}")
    pc += 0x1
    time.sleep(1 / clockSpeed)