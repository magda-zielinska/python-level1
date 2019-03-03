def IsThisaTriangle(sideA,sideB,sideC):
    if sideA + sideB >= sideC:
        return True
    if sideA + sideB <= sideC:
        return False
    if sideB + sideC <= sideA:
        return True

print(IsThisaTriangle(2,3,7))

def IsThisATriangle(a,b,c):
    return a + b > c and b + c > a and c + a <= b

a=float(input("Give ma side a of the triangle"))
b=float(input("Give me the side b of the triangle"))
c=float(input("Give me the side c of the triangle"))
if IsThisATriangle(a,b,c):
    print("Congrats - it could be a triangle")
else:
    print("Sorry, it won´t be a triangle")

print(IsThisATriangle(1,1,1))
print(IsThisATriangle(1,1,3))