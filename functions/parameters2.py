# you can define more parameters
# positional parameter passing
# you have to put positional arguments before keyword ones

def sum(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)

# this is positional
sum(1,2,3)

# this is keyword
sum(c=3, b=2, a=1)

# mixed:
sum(3, c=1, b=2)

# predefined parameter:

def introduction(firstname, lastname="Smith"):
    print("My name is ",firstname, lastname)

introduction("Henry")
introduction(firstname="William")
introduction("James","Doe")

