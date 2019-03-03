# shifting bits

Var = 17
VarRight = Var >> 1
# = 17 // 2 → 8 (shifting to the right by one bit is the same as integer division by two)
VarLeft = Var << 2
# = 17 * 4 → 68 (shifting to the left by two bits is the same as integer multiplication by four - second bit = 2*2 = 4)
print(Var, VarRight, VarLeft)
