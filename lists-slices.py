list1 = [1]
list2 = list1
list1[0] = 2
print(list2)

#solution: slices:

list3 = [2]
list4 = list3[:]
list3[0]= 4
print(list3)

list6 = [10, 8, 6, 4, 2, 5, 9, 3]
new_list = list6[1:3] # [start - count from the start 0, 1, 2.. : end - counting from the start but -1, because the
# last value doent count, so 3 - 1= 2, the value 2 - 0, 1, 2 ] - start is the index of the first element included in the slice;- end is the index of the first element not included in the slice.

print(new_list)

list7 = [10, 8, 6, 4, 2]
new_list2 = list7[1:-1]
print(new_list2)

list8 = [9, 7, 5, 3, 1]
del list8[1:3]
print(list8)

list9 = [9, 7, 5, 3, 1]
del list9[:]
print(list9)