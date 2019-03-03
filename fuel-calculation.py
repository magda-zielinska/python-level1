def l100kmtompg(litres):
    m = litres / 100000
    mpg = m * 1609.344 * litres
    return mpg

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))

#
# put your code here
#

def mpgtol100km(miles):
    km = miles / 1.609344
    l100m = km / 3.785411784
    return l100m
#
# put your code here
#


print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))