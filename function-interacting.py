def function(n):
    print("I got", n)
    n += 1
    print("I have ", n)

variable=1
function(variable)
print(variable)

def function2(list):
    print(list)
    list = [0,1]

L = [2,3]
function2(L)
print(L)

def function3(list):
    print(list)
    del list[0]

L = [2,3]
function3(L)
print(L)
