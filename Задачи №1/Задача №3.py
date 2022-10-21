from operator import truediv
import calendar
from pickle import TRUE
import string


def is_valid_UCN(ucn, should_bypass_checksum=False):
    #Moje i direktno da go parsnem kum string poneje to ako veche e string taka ili inache shte si ostane string
    #ucn = str(ucn) 
    if(isinstance(ucn, int)): ucn = str(ucn) 

    #Luckily, these seem to work even when the string has a leading 0, so 09 gets converted to 9 for example
    yearBorn = int(''.join(ucn[0:2])) #[ucn[i] for i in range(0,2)]
    monthBorn = int(''.join(ucn[2:4])) #[ucn[i] for i in range(2,4)]
    dayBorn = int(''.join(ucn[4:6])) #[ucn[i] for i in range(4,6)]

    born1800 = 21 <= monthBorn <= 32
    born1900 = 1 <= monthBorn <= 12
    born2000 = 41 <= monthBorn <= 52

    if(not(born1800 or born1900 or born2000)): 
        return False
    
    actualYearBorn = yearBorn + (1800 if born1800 else (1900 if born1900 else 2000))
    actualMonthBorn = monthBorn - (20 if born1800 else (40 if born2000 else 0))

    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if(calendar.isleap(actualYearBorn)): daysInMonth[1] += 1

    if(not(1 <= dayBorn <= daysInMonth[actualMonthBorn - 1])):
        return False
    
    if(should_bypass_checksum): 
        return True

    #x2	x4	x8	x5	x10	x9	x7	x3	x6	
    checkSumWeight = [2, 4, 8, 5, 10, 9, 7, 3, 6]

    expectedCheckSum = sum([int(ucn[i])*checkSumWeight[i] for i in range(0,9)]) % 11
    if(expectedCheckSum == 10): expectedCheckSum = 0

    checkSum = int(ucn[9])

    if(expectedCheckSum != checkSum): 
        return False
    
    return True

#Check sum is incorrect
print(True if is_valid_UCN("6101057509") == True else 1) 

#Check sum is incorrect but it doesn't matter
print(True if is_valid_UCN("6101057500", should_bypass_checksum=True) == True else 2)

#Check sum is incorrect
print(True if is_valid_UCN("6101057500") == False else 3) #3


#Month is correct.
print(True if is_valid_UCN("6910136669", True) == True else 4)

#Month is incorrect. 13th month doesn't exist
print(True if is_valid_UCN("6913136669", True) == False else 5)


#Day is correct.
print(True if is_valid_UCN("6910316669", True) == True else 6) #6

#Day is correct. Year is leap
print(True if is_valid_UCN("8002296669", True) == True else 7)


#Day is correct.
print(True if is_valid_UCN("9830316669", True) == True else 8)

#Day is correct. Year is leap
print(True if is_valid_UCN("9622296669", True) == True else 9) #9


#Day is correct.
print(True if is_valid_UCN("0450316669", True) == True else 10)

#Day is correct. Year is leap
print(True if is_valid_UCN("0442296669", True) == True else 11)


#Day is incorrect. Not 31th day in September
print(True if is_valid_UCN("6909316669", True) == False else 12) #12

#Day is incorrect. Year is not leap. No 29th day in February
print(True if is_valid_UCN("8102296669", True) == False else 13)


#Day is incorrect. Not 31th day in September
print(True if is_valid_UCN("9829316669", True) == False else 14)

#Day is incorrect. Year is not leap. No 29th day in February
print(True if is_valid_UCN("9722296669", True) == False else 15) #15


#Day is incorrect. Not 31th day in September
print(True if is_valid_UCN("0249316669", True) == False else 16)

#Day is incorrect. Year is not leap. No 29th day in February
print(True if is_valid_UCN("0342296669", True) == False else 17)


#Correct
print(True if is_valid_UCN("6101057509") == True else 18) #18


#Repeat the tests but with an integer. Where necessary, the UCN is changed so that is doesn't start with a 0

#Check sum is incorrect
print(True if is_valid_UCN(6101057509) == True else 19)

#Check sum is incorrect but it doesn't matter
print(True if is_valid_UCN(6101057500, should_bypass_checksum=True) == True else 20)

#Check sum is incorrect
print(True if is_valid_UCN(6101057500) == False else 21) #21


#Month is correct.
print(True if is_valid_UCN(6910136669, True) == True else 22)

#Month is incorrect. 13th month doesn't exist
print(True if is_valid_UCN(6913136669, True) == False else 23)


#Day is correct.
print(True if is_valid_UCN(6910316669, True) == True else 24) #24

#Day is correct. Year is leap
print(True if is_valid_UCN(8002296669, True) == True else 25)


#Day is correct.
print(True if is_valid_UCN(9830316669, True) == True else 26)

#Day is correct. Year is leap
print(True if is_valid_UCN(9622296669, True) == True else 27) #27


#Day is correct.
print(True if is_valid_UCN(1250316669, True) == True else 28)

#Day is correct. Year is leap
print(True if is_valid_UCN(1242296669, True) == True else 29)


#Day is incorrect. Not 31th day in September
print(True if is_valid_UCN(6909316669, True) == False else 30) #30

#Day is incorrect. Year is not leap. No 29th day in February
print(True if is_valid_UCN(8102296669, True) == False else 31)


#Day is incorrect. Not 31th day in September
print(True if is_valid_UCN(9829316669, True) == False else 32)

#Day is incorrect. Year is not leap. No 29th day in February
print(True if is_valid_UCN(9722296669, True) == False else 33) #33


#Day is incorrect. Not 31th day in September
print(True if is_valid_UCN(1349316669, True) == False else 34)

#Day is incorrect. Year is not leap. No 29th day in February
print(True if is_valid_UCN(1342296669, True) == False else 35)


#Correct
print(True if is_valid_UCN(6101057509) == True else 36) #36



