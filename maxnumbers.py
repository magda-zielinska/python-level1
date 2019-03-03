number = int(input("Enter value or -1 to stop: "))

max = -9999999

while number != -1:
    if number > max:
        max = number
    nextnumber = int(input("Enter another value or -1 to stop: "))

print("The largest number is" ,max)