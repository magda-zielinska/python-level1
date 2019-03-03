values = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here

unique = []
dupes = []
for i in values:
    if i not in unique:
        unique.append(i)
    else:
        dupes.append(i)


#
print("list with unique elements only:")
print(unique)