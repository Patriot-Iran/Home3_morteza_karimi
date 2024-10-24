"""
question 4
"""

import jdatetime
from dateutil.relativedelta import relativedelta
from datetime import datetime
def Calc_the_age(birth, to_now):
    """
    this function receives two variables to calculiate the accurate age

    birth= a date of birth
    to_now: now date


    it returns accurate age
    """
    
    difference=relativedelta(to_now, birth) #it returns the differnce od two dates
    print(f'your age is {difference.years} and {difference.months} month and {difference.days} day and'
    f'{difference.hours} hours and {difference.minutes} mins and {difference.seconds} seconds') #it prints the result of calculating


def calc_the_nextBirth(next_birth, to_now):
    """
    this function receives two variables to calculiate the accurate next birthdaty
    
    next_birth= a date of birth for next year
    to_now: now date


    it returns accurate the remaining time to next birth day
    
    """
    difference=relativedelta(next_birth, to_now)#it returns the differnce od two dates
    print(f'your next birth day is {difference.years} years and {difference.months} month and '
    f'{difference.days} day and {difference.hours} hours and {difference.minutes} mins and {difference.seconds} seconds')  #it prints the result of calculating


def geogre_to_jcal(birth):
    """
    this function receives one variables to convert the accurate birth day in jcal
    
    birth= a date of birth for in george
   


    it returns accurate the accurate birth day in jcal
    """
    
    jcal_date = jdatetime.datetime.fromgregorian(datetime=birth) #it converts to Jcal
  
    print("your jcal birth date is :",jcal_date.strftime('%Y/%m/%d   %H:%M:%S'))  # Adding a space between the date and time



birth=input ("enter your birth date and its exact time YYYY/MM/DD HH/MM/SS :\n") #it receives birth date and its time
birth=datetime.strptime(birth, '%Y/%m/%d %H:%M:%S') #it converts string to date and time
to_now=datetime.now()#it cosiders current date and time
next_birth=datetime(to_now.year +1, birth.month, birth.day, birth.hour, birth.minute, birth.second) #it is next year birth date


calc_the_nextBirth(birth, to_now)
calc_the_nextBirth(next_birth, to_now)
geogre_to_jcal(birth)