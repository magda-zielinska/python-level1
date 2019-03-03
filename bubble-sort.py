list = [8, 10, 6, 2, 4]

swapped = True
while swapped:
    swapped = False
    for i in range(len(list)-1):
        if list[i] > list[i + 1]:
            swapped = True
            list[i],list[i + 1]=list[i + 1],list[i]
print(list)


list2 = []
swapped = True
num = int(input("How many elements do you want to sort? "))
for i in range(num):
    val = float(input("Enter next element: "))
    list2.append(val)
while swapped:
    swapped = False
    for i in range(len(list2)-1):
        if list2[i] > list2[i + 1]:
            swapped = True
            list2[i], list2[i + 1] = list2[i + 1], list2[i]
print("Sorted: ")
print(list2)


list3 = [12, 11, 8, 3, 6, 1]
list3.sort()
print(list3)

