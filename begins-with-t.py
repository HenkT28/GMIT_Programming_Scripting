# Henk Tjalsma, 2019
# Solution to problem 2 - begins-with-t.py script
# Write a program that outputs whether or not today is a day that begins with the letter T.
# Verbatim: https://stackoverflow.com/a/9847269 - Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
# https://www.pythonprogramming.in/date-time/get-the-day-of-week-from-given-a-date-in-python.html

# import Python's datetime module
import datetime

# print("Present year: ", datetime.date.today().strftime("%Y"))
# print("Month of year: ", datetime.date.today().strftime("%B"))
# print("Week number of the year: ", datetime.date.today().strftime("%W"))
# print("Weekday of the week: ", datetime.date.today().strftime("%w"))
# print("Day of year: ", datetime.date.today().strftime("%j"))
# print("Day of the month : ", datetime.date.today().strftime("%d"))
# print("Day of week: ", datetime.date.today().strftime("%A"))

# Testing on Saturday 23/02/2019
# if datetime.datetime.today().weekday() == 5:
#  print("Yippee!")

# dayofweek = datetime.date(2019, 2, 23).strftime("%A")

# Tuesday - begins with T, weekday 1
if datetime.datetime.today().weekday() == 1:
   print("Yes - today begins with a T.")
#  print(dayofweek)
   print("weekday():", datetime.datetime.today().weekday())   
   print("isoweekday()", datetime.datetime.today().isoweekday())
# Thursday - begins with T, weekday 3   
elif datetime.datetime.today().weekday() == 3:  
  print("Yes - today begins with a T.")
#  print(dayofweek) 
  print("weekday():", datetime.datetime.today().weekday())
  print("isoweekday()", datetime.datetime.today().isoweekday())
else:
   print("No - today does not begin with a T.")   