max = -9999999
counter = 0
number = int(input("Enter value o -1 to stop: "))

while number != -1:

    if number == -1:
            continue
    counter +=15
    if number > max:
        max = number
    number = int(input("Enter value or -1 to stop: "))

if counter:
    print("The largest number is" ,max)
else:
    print("Are you kidding? You haven´t put any number!")


# or break in the place of continue