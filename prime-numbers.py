def IsPrime(num):
    if num % 2 == 0 and num > 2:
        return False
    if num % 3 == 0 and num > 3:
        return False
    if num % 4 == 0:
        return False
    else:
        return True
    
#
# put your code here
#

for i in range(1,20):
	if IsPrime(i + 1):
			print(i+1,end=" ")
print()