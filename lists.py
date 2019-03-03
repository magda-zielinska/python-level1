numbers = [ 10, 5, 7, 2, 1 ]

numbers[0] = 111

numbers[1] = numbers[4]

print(numbers[0])

print(numbers)

print(len(numbers))

del numbers[1]
print(len(numbers))
print(numbers)

print(numbers[-1])
print(numbers[-2])

#method:

numbers.append(4)
#add to the end a value
print(len(numbers))
print(numbers)

numbers.insert(1,222)
print(numbers)

numbers.insert(2,333)
print(numbers)