import calendar
months = calendar.month_name

for i in months:
    print(i)
    
print(calendar.calendar(1982))

from datetime import date, time, datetime

import datetime

current = datetime.datetime.now()

print(current)