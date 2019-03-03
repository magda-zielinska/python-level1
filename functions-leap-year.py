def IsYearLeap(year):
    if year < 1582:
        return True
    if year % 100 == 0:
        return True
    elif year % 4 != 0:
        return False
    elif year % 400 == 0:
        return False
    else:
        return False
        
        
        
#        if (year % 100 == 0):
#            return True
#        else:
#            return False

#
# put your code here
#

testdata = [1900, 2000, 2016, 1987]
testresults = [True, True, False, False]
for i in range(len(testdata)):
	yr = testdata[i]
	print(yr,"->",end="")
	result = IsYearLeap(yr)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")