# 4-Bit-Emulator

I made a very basic 4-bit Emulator. Right now, it only has 7 instructions out of 16, and it is a Turing machine.

#Registors

A > Initial Register - 0x0
B > 0x1
C > 0x2
D > All ALU Operation Results Go Into Here - 0x3


#Instuctions
# 0000 0x0 (Value)
> Sets the value for the A register

# 0001 0x1 {reg1} {reg2}
> Moves the value of register[1] into register[2]

# 0010 0x2 {Reg1} {Reg2}
> Adds register[1] and register[2] into register D

# 0011 0x3 {Reg1} {Reg2}
> Subtracts register[1] from register[2] into register D

# 0100 0x4 (Value)
> Jumps to that value in memory

# 0101 0x5 (Reg)
> Prints the value of reg 

# 0110 0x6
> 

# 0111 0x7
> 

# 1000 0x8 
> 

# 1001 0x9
> Halts the computer
