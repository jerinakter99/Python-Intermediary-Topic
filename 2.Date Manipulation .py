#1: Get Current Date and Time
import datetime

now = datetime.datetime.now()

print(now)

#2: Get Current Date

import datetime

current_date = datetime.date.today()

print(current_date)
# 3: Get the current date using today()

from datetime import date

todays_date = date.today()

print("Today's date =", todays_date)
# 4: Print today's year, month and day
from datetime import date

today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#Python format datetime
#Python strftime() Method
from datetime import datetime

now = datetime.now()

t = now.strftime("%H:%M:%S")
print("Time:", t)

f1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", f1)

f2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", f2)




