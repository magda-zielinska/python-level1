list = [0, 3, 12, 8, 2]
print(5 in list)
print(5 not in list)
print(12 in list)

list2 = [6, 3, 11, 5, 1, 9, 7, 15, 13]
max = list2[0]
for i in range(1,len(list2)):
        if list2[i] > max:
            max = list2[i]
print(max)

list3 = [6, 9, 2, 18, 4, 3]
max = list3[0]
for i in list3[1:]:
        if i > max:
            max = i
print(max)