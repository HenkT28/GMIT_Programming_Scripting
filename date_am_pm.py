import time
import datetime

from time import strftime
from datetime import date
from datetime import datetime

# %A, %B %e %Y %H %M %r

today = datetime.now()

day = today.day  

if (3 < day < 21) or (23 < day < 31):
  day = str(day) + 'th'
else:
  suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
  day = str(day) + suffixes[day % 10]


date_string = today.strftime("%A, %B # %Y at %I:%M%p")  

print(date_string.replace('#', day), end='')
	