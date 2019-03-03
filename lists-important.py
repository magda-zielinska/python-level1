# step 1
Beatles = []
print("Step 1:", Beatles)

# step 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")

print("Step 2:", Beatles)

# step 3
for i in Beatles:
    add = input("Add Stu Sutcliffe to the list")
    Beatles.append(add)
    add2 = input("Add Pete Best to the list")
    Beatles.append(add2)
    break
print("Step 3:", Beatles)

# step 4

del Beatles[3]
del Beatles[3]
print("Step 4:", Beatles)

# step 5

Beatles.insert(0,"Ringo Star")
print("Step 5:", Beatles)

print("The Fab",len(Beatles))