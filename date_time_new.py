# Henk Tjalsma, 2019
# Solution to problem 8 - datetime.py
# Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.
# Verbatim: https://www.guru99.com/date-time-and-datetime-classes-in-python.html
# https://tecadmin.net/get-current-date-time-python/
# https://www.robjwells.com/2013/10/date-suffixes-in-python/
# http://strftime.net/
# https://www.tutorialspoint.com/python/time_strftime.htm

# https://kapeli.com/cheat_sheets/strftime_Format_Codes.docset/Contents/Resources/Documents/index
# https://www.programcreek.com/python/example/351/datetime.strptime

# https://stackoverflow.com/questions/2925230/get-235pm-instead-of-0235pm-from-python-date-time
# That said, bear in mind that if the "%p" term gives you uppercase letters, it may be because the user set their locale to work that way, and by changing case you are overriding user preferences, which sometimes leads to bug reports. 
# Also, the user may want something other than "am" or "pm", such as "a.m." and "p.m.". 
# Also note that these are different for different locales (e.g. en_US locale gives AM or PM for %p, but de_DE gives am or pm) and you might not be getting characters in the encoding you assume.


import time
import datetime

from time import strftime
from datetime import date
from datetime import datetime

# %A, %B %e %Y %H %M %r

today = datetime.now()

# Setting the day variable, used in running the if/else statement and adding 1: 'st', 2: 'nd', 3: 'rd', and otherwise 'th' to the day.
day = today.day  

if (3 < day < 21) or (23 < day < 31):
  day = str(day) + 'th'
else:
  suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
  day = str(day) + suffixes[day % 10]


# date_string = today.strftime("%A, %B # %Y at %I:%M%p") - this translates to capital AM or PM.
date_string = today.strftime("%A, %B # %Y at ") + today.strftime('%I:%M%p').lower()

print(date_string.replace('#', day), end='')