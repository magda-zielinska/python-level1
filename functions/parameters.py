def message(no):
    print("Enter value number", no)

message(1)
a = input()

# you can define more parameters
# positional parameter passing
# you have to put positional arguments before keyword ones

def message2(what,no):
    print("Enter", what, "number", no)

message2("price",10)
message2("tax",5)

# keyword argument passing:

def introduction(firstname, lastname):
    print("Hello, my name is ",firstname,lastname)

introduction(firstname="James",lastname="Bond",)
introduction(lastname="Skywalker",firstname="Luke")
