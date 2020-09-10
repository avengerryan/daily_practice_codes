
# display calendar

# python has a built in function, calendar to work with date related tasks.

# we import the calendar module. built in function month() inside the module takes in the year and the month and displays

# importing calendar module
import calendar

yy = 2014   # year
mm= 11      # month

# to take month and year input from the user
# yy = int(input('Enter year: '))
# mm= int(input('enter month: '))

# display the calendar
print(calendar.month(yy, mm))