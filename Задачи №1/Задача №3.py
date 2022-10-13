from operator import truediv
import calendar
from pickle import TRUE
import string


def is_valid_UCN(ucn, shoul_bypass_checksum=False):
    #Moje i direktno da go parsnem kum string poneje to ako veche e string taka ili inache shte si ostane string
    #ucn = str(ucn) 
    if(isinstance(ucn, int)): ucn = str(ucn) 

    yearBorn = int(''.join([ucn[i] for i in range(0,2)]))
    monthBorn = int(''.join([ucn[i] for i in range(2,4)]))
    dayBorn = int(''.join([ucn[i] for i in range(4,6)]))

    pre1900 = 21 <= monthBorn <= 32
    post1999 = 41 <= monthBorn <= 52
    during20thCentury = 1 <= monthBorn <= 12

    if(not(pre1900 or post1999 or during20thCentury)): 
        return False
    
    actualYearBorn = yearBorn + (1800 if pre1900 else (1900 if during20thCentury else 2000))
    actualMonthBorn = monthBorn - (20 if pre1900 else (40 if post1999 else 0))

    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if(calendar.isleap(actualYearBorn)): daysInMonth[1] += 1

    if(not(1 <= dayBorn <= daysInMonth[actualMonthBorn - 1])):
        return False
    
    if(shoul_bypass_checksum): 
        return True

    #x2	x4	x8	x5	x10	x9	x7	x3	x6	
    checkSumWeight = [2, 4, 8, 5, 10, 9, 7, 3, 6]

    expectedCheckSum = sum([int(ucn[i])*checkSumWeight[i] for i in range(0,8)]) % 11
    if(expectedCheckSum == 10): expectedCheckSum = 0

    checkSum = int(ucn[9])

    if(expectedCheckSum != checkSum): 
        return False
    
    return True

#Check sum is incorrect
print(is_valid_UCN("6101057509") == True)
#Check sum is incorrect but it doesn't matter
print(is_valid_UCN("6101057500", shoul_bypass_checksum=True) == True)
#Check sum is incorrect
print(is_valid_UCN("6101057500") == False) #3

#Month is correct.
print(is_valid_UCN("6910136669", True) == True)
#Month is incorrect. 13th month doesn't exist
print(is_valid_UCN("6913136669", True) == False)

#Day is correct.
print(is_valid_UCN("6910316669", True) == True) #6
#Day is correct. Year is leap
print(is_valid_UCN("8002296669", True) == True)

#Day is correct.
print(is_valid_UCN("9830316669", True) == True)
#Day is correct. Year is leap
print(is_valid_UCN("9622296669", True) == True) #9

#Day is correct.
print(is_valid_UCN("0450316669", True) == True)
#Day is correct. Year is leap
print(is_valid_UCN("0442296669", True) == True)

#Day is incorrect. Not 31th day in September
print(is_valid_UCN("6909316669", True) == False) #12
#Day is incorrect. Year is not leap. No 29th day in February
print(is_valid_UCN("8102296669", True) == False)

#Day is incorrect. Not 31th day in September
print(is_valid_UCN("9829316669", True) == False)
#Day is incorrect. Year is not leap. No 29th day in February
print(is_valid_UCN("9722296669", True) == False) #15

#Day is incorrect. Not 31th day in September
print(is_valid_UCN("0249316669", True) == False)
#Day is incorrect. Year is not leap. No 29th day in February
print(is_valid_UCN("0342296669", True) == False)

#Correct
print(is_valid_UCN("6101057509") == True) #18

#Repeat the tests but with an integer.

#Check sum is incorrect
print(is_valid_UCN(6101057509) == True)
#Check sum is incorrect but it doesn't matter
print(is_valid_UCN("6101057500", shoul_bypass_checksum=True) == True)
#Check sum is incorrect
print(is_valid_UCN("6101057500") == False) #21

#Month is correct.
print(is_valid_UCN("6910136669", True) == True)
#Month is incorrect. 13th month doesn't exist
print(is_valid_UCN("6913136669", True) == False)

#Day is correct.
print(is_valid_UCN("6910316669", True) == True) #24
#Day is correct. Year is leap
print(is_valid_UCN("8002296669", True) == True)

#Day is correct.
print(is_valid_UCN("9830316669", True) == True)
#Day is correct. Year is leap
print(is_valid_UCN("9622296669", True) == True) #27

#Day is correct.
print(is_valid_UCN("0450316669", True) == True)
#Day is correct. Year is leap
print(is_valid_UCN("0442296669", True) == True)

#Day is incorrect. Not 31th day in September
print(is_valid_UCN("6909316669", True) == False) #30
#Day is incorrect. Year is not leap. No 29th day in February
print(is_valid_UCN("8102296669", True) == False)

#Day is incorrect. Not 31th day in September
print(is_valid_UCN("9829316669", True) == False)
#Day is incorrect. Year is not leap. No 29th day in February
print(is_valid_UCN("9722296669", True) == False) #33

#Day is incorrect. Not 31th day in September
print(is_valid_UCN("0249316669", True) == False)
#Day is incorrect. Year is not leap. No 29th day in February
print(is_valid_UCN("0342296669", True) == False)

#Correct
print(is_valid_UCN("6101057509") == True) #36


