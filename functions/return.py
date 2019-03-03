def strange(n):
    if(n % 2 == 0):
        return True

print(strange(2))
print(strange(1))

def strangelist(n):
    list = []
    for i in range(0,n):
        list.insert(0,i)
    return list

print(strangelist(5))


def sumoflist(n):
    sum = 0
    for el in n:
        sum += el
    return sum

print(sumoflist([1,2,3]))

