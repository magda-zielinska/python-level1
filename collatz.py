while True:

    c0 = int(input("Give me a non-negative and non-zero number: "))

    count = 0

    while c0 != 1 and c0 != -1:
        if c0 % 2 == 0:
            c0 = c0 / 2
            print(c0)
            count += 1
            
        else:
            c0 = (3 * c0 + 1)
            print(c0)
            count += 1
            
    count = str(count)
    c0 = str(c0)
    
    print("\ntook " + count + " steps")
    