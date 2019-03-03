number1 = int(input("Give me a number..."))
number2 = int(input("Give me a number..."))
number3 = int(input("Give me a numner..."))

max = number1

if number2 > max:
    max = number2

if number3 > max:
    max = number3

print("The largest number is " ,max)