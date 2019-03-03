list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tofind = 5
found = False
for i in range(len(list)):
    found = list[i] == tofind
    if found:

        if found:
            print("Element found on index: ",i)
        else:
            print("absent")


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1
print(hits)