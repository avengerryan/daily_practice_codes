# checking leap year

# a leap year is exactly divisible by 4, except for century years
# example
# 2017 is not a leap year
# 1900 is not a leap year
# 2012 is a leap year


# year= 2000

# to get year (integer input) from the user
year= int(input('enter a year:'))

# using nested if
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print('{0} is a leap year'.format(year))
        else:
            print('{0} is not a leap year'.format(year))
    else:
        print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))
