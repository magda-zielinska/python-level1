def BMI(weight, hight):
    return weight / hight**2

print(BMI(52.5, 1.65))


def BMI2(weight,hight):
    if hight < 1.0 or hight > 2.5 or \
        weight < 20 or weight > 200:
        return None
    return weight / hight**2

print(BMI2(325.5, 1.65))


#1 lb = 0.45359237 kg

def lbtokg(lb):
    return lb * 0.45359237
print(lbtokg(1))

def ftintom(ft,inch):
    return ft * 0.3048 + inch * 0.0254

print(ftintom(1,1))
print(ftintom(6,0))

# just feet without inches

def ftintom(ft,inch=0.0):
    return ft * 0.3048 + inch * 0.0254

print(ftintom(1,1))
print(ftintom(6))


def ftintom(ft,inch):
    return ft * 0.3048 + inch * 0.0254
def lbtokg(lb):
    return lb * 0.45359237
def BMI(weight,hight):
    if hight < 1.0 or hight > 2.5 or \
        weight < 20 or weight > 200:
        return None
    return weight / hight**2

print(BMI(hight=ftintom(5,7),weight=lbtokg(175)))



