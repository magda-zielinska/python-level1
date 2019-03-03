list = [10, 1, 8, 3, 5]

sum = 0

for i in range(len(list)):
    sum += list[i]
print(sum)


for i in range(len(list)):
    sum += 1
print(sum)


for i in list:
    sum += 1
print(sum)

#swapping values:

variable1 = 1
variable2 = 2

auxiliary = variable1
variable1 = variable2
variable2 = auxiliary

# better way:

variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1
