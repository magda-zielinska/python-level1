def IsThisATriangle(a,b,c):
    return a + b > c and b + c > a and c + a <= b
def IsThisRightTriangle(a,b,c):
    if not IsThisATriangle(a,b,c):
        return False
    if c > a and c > b:
        return c**2 == a**2 + b**2
    if a > b and a > c:
        return a**2 == b**2 + c**2

print(IsThisRightTriangle(5,3,4))
print(IsThisRightTriangle(1,3,4))
