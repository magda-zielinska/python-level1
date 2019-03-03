year = int(input("Enter a year: "))

if year < 1582:
    print("This year doesn´t fall in the Gregorian Era!")
if year % 4 != 0:
    print("It is a common year")
elif year % 100 == 0:
    print("It is a leap year")
elif year % 400 == 0:
    print("It is a common year")
else:
    print("It is a leap year")