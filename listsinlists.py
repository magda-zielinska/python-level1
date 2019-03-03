L = [0, 1, 2, 3]
x = 1
for e in L:
    x *= e
print(x)

lst = [3, 1, -1]
lst[-1] = lst[-2]
print(lst)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)

lst = [3, 1, -2]
print(lst[lst[ -1]])

lst = [1,2,3,4]
print(lst[ -3: -2])

l1 = [1,2,3]
l2 = []
for v in l1:
    l2.insert(0,v)
print(l2)

l1 = [1,2,3]
for v in range(len(l1)):
    l1.insert(1,l1[v])
print(l1)

T = [[3 - i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += T[i][i]
print(s)

L = [[0, 1, 2, 3] for i in range(2)]
print(L[2][0])