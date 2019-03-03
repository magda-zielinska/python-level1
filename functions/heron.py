def IsThisATriangle(a,b,c):
    return a + b > c and b + c > a and c + a >= b

def Heron(a,b,c):
    p = (a+b)/2
    return (p*(p-a)+(p-b)*(p-c))**0,5

def FieldOfATriangle(a,b,c):
    if not IsThisATriangle(a,b,c):
        return None
    return Heron(a,b,c)

print(FieldOfATriangle(3.,3.,4.24))