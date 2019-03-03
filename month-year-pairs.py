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
#
# your code is already here (from Lab 3.3.12.1)
#

def DaysInMonth(year,month):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year == False:
        month[2] = 28
    if year == True:
        month[2] = 29
#
# put your new code here
#

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [29, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"->",end="")
	result = DaysInMonth(yr,mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")